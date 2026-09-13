#!/usr/bin/env python3
"""
Simulate vercel.json's old-domain redirects and prove every destination exists.

    python3 scripts/check_redirects.py [/path/to/parent-of-old-site-clones]

Feeds every URL from the old sites' sitemaps (when the clones are available),
plus the www/apex, .html, trailing-slash, index.html, robots, sitemap and
asset spellings, through the redirect rules the way Vercel evaluates them
(first matching rule wins, path-to-regexp source, $1 capture), then checks
that each destination resolves to a file in this repo under cleanUrls
(`/x` -> x.html or x/index.html) after trailingSlash normalisation.
"""
import json
import os
import re
import sys
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NEW_HOST = "www.ecosinsurancesolutions.com"
CLONES = {  # state -> old repo directory name (for the old sitemaps)
    "arizona": "medicare-enrollment-arizona", "california": "california-medicare-enrollment",
    "colorado": "colorado-medicare-enrollment", "florida": "medicare-enrollment-florida",
    "georgia": "georgiamedicareenrollment", "minnesota": "minnesota-medicare-enrollment",
    "nevada": "nevada-medicare-enrollment", "tennessee": "tennessee-medicare-quotes",
    "texas": "texas-medicare-enrollment", "utah": "medicare-enrollment-utah",
}


def source_to_regex(src):
    """path-to-regexp subset used in vercel.json: literal path with unnamed regex groups."""
    out, i = "", 0
    while i < len(src):
        if src[i] == "(":
            depth, j = 1, i + 1
            while depth:
                depth += {"(": 1, ")": -1}.get(src[j], 0)
                j += 1
            out += src[i:j]
            i = j
        elif src[i] == "\\":
            out += src[i:i + 2]
            i += 2
        else:
            out += re.escape(src[i])
            i += 1
    return re.compile("^" + out + "$", re.I)


def apply(rules, host, path):
    for r in rules:
        host_ok = all(re.fullmatch(h["value"], host, re.I) for h in r.get("has", []) if h["type"] == "host")
        if not host_ok:
            continue
        m = source_to_regex(r["source"]).match(path)
        if m:
            dest = r["destination"]
            for k, v in enumerate(m.groups(), 1):
                dest = dest.replace(f"${k}", v or "")
            return dest
    return None


def served(path):
    p = path.lstrip("/")
    if p.endswith("/"):
        p = p[:-1]  # trailingSlash:false -> 308 to the version without
    if p == "":
        return os.path.isfile(os.path.join(ROOT, "index.html"))
    return any(os.path.isfile(os.path.join(ROOT, c)) for c in (p, p + ".html", p + "/index.html"))


def main():
    clones = sys.argv[1] if len(sys.argv) > 1 else None
    cfg = json.load(open(os.path.join(ROOT, "vercel.json")))
    rules = cfg["redirects"]
    states = {}
    for r in rules:
        for h in r.get("has", []):
            m = re.match(r"\(www\\\.\)\?(.+)", h["value"])
            if m:
                dom = m.group(1).replace("\\.", ".")
                st = r["destination"].split(NEW_HOST + "/")[1].split("/")[0]
                states.setdefault(st, dom)
    cases = []  # (host, path, note)
    for st, dom in states.items():
        for host in (dom, "www." + dom):
            cases += [(host, "/", "home"), (host, "/index.html", "index.html"), (host, "/index", "index"),
                      (host, "/robots.txt", "robots"), (host, "/sitemap.xml", "sitemap"), (host, "/llms.txt", "llms"),
                      (host, "/privacy", "clean"), (host, "/privacy.html", ".html"), (host, "/privacy/", "slash")]
        if clones:
            sm = os.path.join(clones, CLONES.get(st, ""), "sitemap.xml")
            if os.path.isfile(sm):
                for loc in re.findall(r"<loc>([^<]+)</loc>", open(sm).read()):
                    u = urlparse(loc.strip())
                    cases.append((u.netloc, u.path or "/", "old sitemap"))
                    cases.append(("www." + u.netloc if not u.netloc.startswith("www.") else u.netloc[4:], u.path or "/", "old sitemap, other host"))
    # a few real asset paths per template family
    cases += [("medicareenrollmentarizona.com", "/assets/styles.css", "asset"), ("georgiamedicareenrollment.com", "/site.css", "asset"),
              ("medicareenrollmentnevada.com", "/style.css", "asset"), ("texasmedicareenrollment.com", "/darin.jpg", "asset"),
              ("www.medicareenrollmentarizona.com", "/medicare-yuma-az/", "AZ legacy canonical"),
              ("coloradomedicareenrollment.com", "/medicare-denver-co.html", "CO page"),
              ("www.tennesseemedicarequotes.com", "/index.html", "TN canonical home"),
              ("ecosinsurancesolutions.com", "/texas/houston", "apex of new domain")]
    bad, seen = [], set()
    for host, path, note in cases:
        if (host, path) in seen:
            continue
        seen.add((host, path))
        dest = apply(rules, host, path)
        if not dest:
            bad.append((host, path, note, "NO RULE MATCHED"))
            continue
        u = urlparse(dest)
        if u.netloc != NEW_HOST:
            bad.append((host, path, note, f"wrong host: {dest}"))
        elif not served(u.path):
            bad.append((host, path, note, f"destination missing: {dest}"))
    print(f"{len(seen)} old URLs simulated across {len(states)} domains")
    for b in bad:
        print("FAIL", *b)
    if bad:
        sys.exit(1)
    print("OK — every old URL redirects to an existing page or file on", NEW_HOST)


if __name__ == "__main__":
    main()
