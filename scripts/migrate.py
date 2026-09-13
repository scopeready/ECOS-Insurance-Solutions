#!/usr/bin/env python3
"""
One-time consolidation of the ECOS state Medicare sites into this repository.

    python3 scripts/migrate.py /path/to/parent-of-source-clones

For every source repo it copies the site's files into `<state>/`, then rewrites
every internal link, canonical, Open Graph URL, JSON-LD URL, sitemap entry and
form redirect so the pages live at

    https://www.ecosinsurancesolutions.com/<state>/...

Nothing about the page content changes. Three link styles existed:

  abs  - root-absolute clean URLs (`/duluth`, `/site.css`). Prefixed with `/<state>`.
  rel  - relative links with `.html` (`medicare-basics.html`, `style.css`).
         Rewritten to `/<state>/medicare-basics` and `/<state>/style.css`.

Cross-links between the state sites (the "Our network" strip and `sameAs`)
become internal paths on the new domain. Old-domain URLs in the copy no
longer exist anywhere in the output.

The script is kept for the record; re-running it overwrites the state folders
from the source clones.
"""
import os
import re
import shutil
import sys

NEW_HOST = "https://www.ecosinsurancesolutions.com"

# state slug, source repo directory, old origins (all spellings seen in the pages), link style
STATES = [
    ("arizona",    "medicare-enrollment-arizona",   ["https://www.medicareenrollmentarizona.com", "https://medicareenrollmentarizona.com"], "abs"),
    ("california", "california-medicare-enrollment", ["https://www.californiamedicareenrollment.com", "https://californiamedicareenrollment.com"], "abs"),
    ("colorado",   "colorado-medicare-enrollment",  ["https://www.coloradomedicareenrollment.com", "https://coloradomedicareenrollment.com"], "rel"),
    ("florida",    "medicare-enrollment-florida",   ["https://www.medicareenrollmentflorida.com", "https://medicareenrollmentflorida.com"], "abs"),
    ("georgia",    "georgiamedicareenrollment",     ["https://www.georgiamedicareenrollment.com", "https://georgiamedicareenrollment.com"], "rel"),
    ("minnesota",  "minnesota-medicare-enrollment", ["https://www.minnesotamedicareenrollment.com", "https://minnesotamedicareenrollment.com"], "abs"),
    ("nevada",     "nevada-medicare-enrollment",    ["https://www.medicareenrollmentnevada.com", "https://medicareenrollmentnevada.com"], "rel"),
    ("tennessee",  "tennessee-medicare-quotes",     ["https://www.tennesseemedicarequotes.com", "https://tennesseemedicarequotes.com"], "rel"),
    ("texas",      "texas-medicare-enrollment",     ["https://www.texasmedicareenrollment.com", "https://texasmedicareenrollment.com"], "abs"),
    ("utah",       "medicare-enrollment-utah",      ["https://www.medicareenrollmentutah.com", "https://medicareenrollmentutah.com"], "abs"),
]

# Files that belong to the old per-repo deployment, not to the pages.
SKIP_FILES = {"CLAUDE.md", "README.md", "README.txt", "CNAME", "vercel.json", "robots.txt", ".gitignore", ".vercelignore"}
SKIP_DIRS = {".git", ".github", "source", "node_modules"}

# Arizona carries a legacy generation (per-page directories) and stray upload
# duplicates next to the live flat files. Only the flat files are live.
ARIZONA_SKIP_DIRS = {"about", "contact", "guides", "medicare-advantage-vs-medigap-arizona", "turning-65-checklist-arizona",
                     "medicare-flagstaff-az", "medicare-kingman-az", "medicare-lake-havasu-city-az", "medicare-mesa-az",
                     "medicare-phoenix-az", "medicare-sedona-az", "medicare-tucson-az", "medicare-yuma-az"}
ARIZONA_SKIP_RE = re.compile(r"^index \(\d+\)\.html$")

TEXT_EXT = {".html", ".htm", ".xml", ".txt", ".js", ".css", ".json", ".webmanifest", ".svg"}

URL_ATTRS = r"(?:href|src|action|poster|data-src|data-href|content)"


def is_text(path):
    return os.path.splitext(path)[1].lower() in TEXT_EXT


def copy_site(src_root, state, repo):
    src = os.path.join(src_root, repo)
    dst = os.path.join(os.getcwd(), state)
    if os.path.exists(dst):
        shutil.rmtree(dst)
    os.makedirs(dst)
    for name in sorted(os.listdir(src)):
        p = os.path.join(src, name)
        if os.path.isdir(p):
            if name in SKIP_DIRS:
                continue
            if state == "arizona" and name in ARIZONA_SKIP_DIRS:
                continue
            shutil.copytree(p, os.path.join(dst, name))
        else:
            if name in SKIP_FILES:
                continue
            if state == "arizona" and (ARIZONA_SKIP_RE.match(name) or name == "site.webmanifest"):
                # site.webmanifest in the Arizona upload is an HTML file, not a manifest.
                continue
            shutil.copy2(p, os.path.join(dst, name))
    if state == "arizona":
        # every Arizona page references /assets/ecos-logo.png, which the upload never had; the file is at the root
        logo_src, logo_dst = os.path.join(dst, "ecos-logo.png"), os.path.join(dst, "assets", "ecos-logo.png")
        if os.path.isfile(logo_src) and not os.path.isfile(logo_dst):
            shutil.copy2(logo_src, logo_dst)
    if state == "georgia":
        # the Georgia home page points its social-share image at og-georgia.png, which was never uploaded
        og_src, og_dst = os.path.join(dst, "og-image.png"), os.path.join(dst, "og-georgia.png")
        if os.path.isfile(og_src) and not os.path.isfile(og_dst):
            shutil.copy2(og_src, og_dst)
    # keep the generator engine for the states that have one, outside the served tree
    gen = os.path.join(src, "source")
    if os.path.isdir(gen):
        tdst = os.path.join(os.getcwd(), "tools", "generators", state)
        if os.path.exists(tdst):
            shutil.rmtree(tdst)
        shutil.copytree(gen, tdst)
    # keep the per-site working notes
    for note, out in (("CLAUDE.md", f"{state}.md"), ("README.md", f"{state}-README.md")):
        n = os.path.join(src, note)
        if os.path.isfile(n):
            shutil.copy2(n, os.path.join(os.getcwd(), "docs", "state-notes", out))
    return dst


def clean_path(path):
    """`/x/index.html` -> `/x`, `/x/y.html` -> `/x/y`, trailing slash dropped."""
    frag = ""
    m = re.match(r"^([^#?]*)([#?].*)?$", path)
    path, frag = m.group(1), m.group(2) or ""
    if path.endswith("/index.html"):
        path = path[: -len("/index.html")]
    elif path.endswith(".html"):
        path = path[:-5]
    if len(path) > 1 and path.endswith("/"):
        path = path[:-1]
    if frag.startswith("#") and path.endswith("/"):
        path = path[:-1]
    return path + frag


def rewrite_abs_links(text, state):
    """Root-absolute internal references get the state prefix."""
    def attr(m):
        val = m.group(2)
        if val.startswith("//"):
            return m.group(0)
        if val == "/":
            return f'{m.group(1)}="/{state}"'
        return f'{m.group(1)}="{clean_path("/" + state + val)}"'
    text = re.sub(rf'\b({URL_ATTRS})="(/[^"]*)"', attr, text)
    # srcset="/a.webp 800w, /b.webp 1600w"
    def srcset(m):
        parts = []
        for cand in m.group(1).split(","):
            cand = cand.strip()
            if cand.startswith("/") and not cand.startswith("//"):
                cand = "/" + state + cand
            parts.append(cand)
        return 'srcset="' + ", ".join(parts) + '"'
    text = re.sub(r'srcset="([^"]*)"', srcset, text)
    # CSS url(/assets/x)
    text = re.sub(r"url\((['\"]?)/(?!/)", rf"url(\1/{state}/", text)
    return text


def rewrite_rel_links(text, state):
    """Relative references (`about.html`, `style.css`) become `/<state>/about`, `/<state>/style.css`."""
    def attr(m):
        a, val = m.group(1), m.group(2)
        if a == "content":
            return m.group(0)  # meta content is never a relative page link on these sites
        if val == "" or val[0] in "#?/" or re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", val):
            return m.group(0)
        if val.startswith("index.html"):
            return f'{a}="{clean_path("/" + state + val[len("index.html"):] if val[len("index.html"):] else "/" + state)}"'
        return f'{a}="{clean_path("/" + state + "/" + val)}"'
    text = re.sub(rf'\b({URL_ATTRS})="([^"]*)"', attr, text)
    def srcset(m):
        parts = []
        for cand in m.group(1).split(","):
            cand = cand.strip()
            if cand and cand[0] not in "/#" and not re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", cand):
                cand = "/" + state + "/" + cand
            parts.append(cand)
        return 'srcset="' + ", ".join(parts) + '"'
    text = re.sub(r'srcset="([^"]*)"', srcset, text)
    text = re.sub(r"url\((['\"]?)(?![a-zA-Z][a-zA-Z0-9+.-]*:|/|#|data:)([^)'\"]+)", rf"url(\1/{state}/\2", text)
    return text


def rewrite_domains(text):
    """Every old-domain URL, from any state, becomes the new-domain path. Bare domain mentions too."""
    # pass 1: full URLs (both spellings of every origin) -> new-domain clean paths
    for state, _repo, origins, _style in STATES:
        for origin in origins:
            def repl(m, state=state):
                path = m.group(1) or ""
                if path in ("", "/"):
                    return f"{NEW_HOST}/{state}"
                return NEW_HOST + clean_path("/" + state + path)
            text = re.sub(re.escape(origin) + r"(/[^\s\"'<>)]*)?", repl, text)
    # pass 2: what is left are bare mentions in copy (form subject lines etc.)
    for state, _repo, origins, _style in STATES:
        bare = re.sub(r"^https://(www\.)?", "", origins[0])
        text = re.sub(r"(?i)\b(www\.)?" + re.escape(bare) + r"\b", f"ecosinsurancesolutions.com/{state}", text)
    # `/state/#frag` -> `/state#frag`
    text = re.sub(rf"({re.escape(NEW_HOST)}/[a-z]+)/#", r"\1#", text)
    return text


def rewrite_file(path, state, style):
    with open(path, encoding="utf-8", errors="surrogateescape") as f:
        text = f.read()
    ext = os.path.splitext(path)[1].lower()
    if ext in (".html", ".htm"):
        text = rewrite_abs_links(text, state) if style == "abs" else rewrite_rel_links(text, state)
    elif ext == ".css":
        text = re.sub(r"url\((['\"]?)/(?!/)", rf"url(\1/{state}/", text) if style == "abs" else \
               re.sub(r"url\((['\"]?)(?![a-zA-Z][a-zA-Z0-9+.-]*:|/|#|data:)([^)'\"]+)", rf"url(\1/{state}/\2", text)
    text = rewrite_domains(text)
    with open(path, "w", encoding="utf-8", errors="surrogateescape") as f:
        f.write(text)


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src_root = sys.argv[1]
    for state, repo, _origins, style in STATES:
        dst = copy_site(src_root, state, repo)
        n = 0
        for root, _dirs, files in os.walk(dst):
            for name in files:
                p = os.path.join(root, name)
                if is_text(p):
                    rewrite_file(p, state, style)
                    n += 1
        print(f"{state:11s} {repo:32s} {n} text files rewritten")


if __name__ == "__main__":
    main()
