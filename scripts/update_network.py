#!/usr/bin/env python3
"""
Bring every section's "Our network" links and JSON-LD sameAs up to the full
list of state sections on this site.

    python3 scripts/update_network.py            # edits the hand-built sections and the generator sources
    python3 tools/build_state.py <state>         # then rebuild each generator-based section

Hand-built sections (Arizona, Georgia: a footer strip; Colorado, Nevada,
Tennessee: an "also serves:" line) are edited in place in every page.
Generator-based sections have their `network=[...]` / `NETWORK = [...]`
source list rewritten; rebuild them afterwards. Every section's `sameAs`
array gains the missing state URLs. Idempotent.
"""
import json
import os
import re
import sys

HOST = "https://www.ecosinsurancesolutions.com"
# slug, footer-strip label, short label for the "also serves" line
STATES = [
    ("arizona", "Medicare Enrollment Arizona", "Arizona"),
    ("california", "California Medicare Enrollment", "California"),
    ("colorado", "Colorado Medicare Enrollment", "Colorado"),
    ("florida", "Medicare Enrollment Florida", "Florida"),
    ("georgia", "Georgia Medicare Enrollment", "Georgia"),
    ("hawaii", "Hawaii Medicare Enrollment", "Hawaii"),
    ("indiana", "Indiana Medicare Enrollment", "Indiana"),
    ("minnesota", "Minnesota Medicare Enrollment", "Minnesota"),
    ("nevada", "Medicare Enrollment Nevada", "Nevada"),
    ("new-mexico", "New Mexico Medicare Enrollment", "New Mexico"),
    ("north-carolina", "North Carolina Medicare Enrollment", "North Carolina"),
    ("ohio", "Ohio Medicare Enrollment", "Ohio"),
    ("south-carolina", "South Carolina Medicare Enrollment", "South Carolina"),
    ("tennessee", "Tennessee Medicare Quotes", "Tennessee"),
    ("texas", "Texas Medicare Enrollment", "Texas"),
    ("utah", "Medicare Enrollment Utah", "Utah"),
    ("washington", "Washington Medicare Enrollment", "Washington"),
]
RESEARCH = [("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"),
            ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")]
STRIP_STATES = {"arizona", "georgia"}
ALSO_STATES = {"colorado", "nevada", "tennessee"}
GENERATOR_STATES = {"california", "florida", "minnesota", "texas", "utah", "hawaii", "indiana", "new-mexico",
                    "north-carolina", "ohio", "south-carolina", "washington"}


def state_url(slug):
    return f"{HOST}/{slug}"


def fix_sameas(text, own):
    def repl(m):
        try:
            arr = json.loads("[" + m.group(1) + "]")
        except json.JSONDecodeError:
            return m.group(0)
        have = set(arr)
        add = [state_url(s) for s, _, _ in STATES if s != own and state_url(s) not in have]
        if not add:
            return m.group(0)
        # keep the state links together: insert after the last existing state link, else at the front
        idx = max((i for i, u in enumerate(arr) if u.startswith(HOST + "/")), default=-1) + 1
        arr[idx:idx] = add
        return '"sameAs":' + json.dumps(arr, ensure_ascii=False, separators=(",", ":"))
    return re.sub(r'"sameAs":\[(.*?)\]', repl, text)


def fix_strip(text, own):
    """Arizona / Georgia: `<a href=".../state" rel="noopener">Label</a> &middot; ...` before the MyMedigapRate link."""
    def repl(m):
        block = m.group(0)
        missing = [(s, lab) for s, lab, _ in STATES if s != own and state_url(s) not in block]
        if not missing:
            return block
        ins = "".join(f'<a href="{state_url(s)}" rel="noopener">{lab}</a> &middot; ' for s, lab in missing)
        return block.replace('<a href="https://www.mymedigaprate.com"', ins + '<a href="https://www.mymedigaprate.com"', 1)
    return re.sub(r'Our network(?: of sites)?:</span>.*?</div>', repl, text, flags=re.S)


def fix_also(text, own):
    """Colorado / Nevada / Tennessee: `also serves: <a ...>Colorado</a> | <a ...>Georgia</a></p>`."""
    def repl(m):
        block = m.group(0)
        missing = [(s, short) for s, _, short in STATES if s != own and state_url(s) not in block]
        if not missing:
            return block
        ins = "".join(f' | <a href="{state_url(s)}" style="color:rgba(255,255,255,.5)">{short}</a>' for s, short in missing)
        return block[:-len("</p>")] + ins + "</p>"
    return re.sub(r'also serves:.*?</p>', repl, text, flags=re.S)


def fix_generator_source(path, own):
    src = open(path, encoding="utf-8").read()
    entries = [(lab, state_url(s)) for s, lab, _ in STATES if s != own] + RESEARCH
    body = ",\n             ".join(f'("{lab}", "{u}")' for lab, u in entries)
    if re.search(r"^NETWORK = \[", src, re.M):
        new = re.sub(r"^NETWORK = \[.*?^\]", "NETWORK = [\n    " + body.replace("\n             ", "\n    ") + ",\n]", src, count=1, flags=re.S | re.M)
    else:
        new = re.sub(r"network=\[.*?\],\n", "network=[" + body + "],\n", src, count=1, flags=re.S)
    if new != src:
        open(path, "w", encoding="utf-8").write(new)
        return True
    return False


def main():
    global STATES
    root = os.getcwd()
    # Only link sections that exist; the list grows as states are built and this script is re-run.
    STATES = [t for t in STATES if os.path.isdir(os.path.join(root, t[0]))]
    changed = 0
    for slug, _, _ in STATES:
        d = os.path.join(root, slug)
        if not os.path.isdir(d):
            print(f"{slug}: no folder yet, skipped")
            continue
        if slug in GENERATOR_STATES:
            gen = os.path.join(root, "tools", "generators", slug)
            for cand in ("content_site.py", "generate.py"):
                p = os.path.join(gen, cand)
                if os.path.isfile(p) and ("network=[" in open(p, encoding="utf-8").read() or "NETWORK = [" in open(p, encoding="utf-8").read()):
                    if fix_generator_source(p, slug):
                        print(f"{slug}: network list updated in tools/generators/{slug}/{cand} — rebuild it")
                    break
            continue
        n = 0
        for name in os.listdir(d):
            if not name.endswith(".html"):
                continue
            p = os.path.join(d, name)
            text = open(p, encoding="utf-8").read()
            new = fix_sameas(text, slug)
            new = fix_strip(new, slug) if slug in STRIP_STATES else fix_also(new, slug)
            if new != text:
                open(p, "w", encoding="utf-8").write(new)
                n += 1
        changed += n
        print(f"{slug}: {n} pages updated")
    print(f"{changed} hand-built pages changed")


if __name__ == "__main__":
    main()
