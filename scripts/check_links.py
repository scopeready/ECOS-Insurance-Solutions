#!/usr/bin/env python3
"""
Verify the consolidated site before a push.

  python3 scripts/check_links.py

Checks, over every HTML/XML/TXT file in the served tree:
  * every internal reference (href/src/action/srcset/url(), and every
    https://www.ecosinsurancesolutions.com/... URL) resolves to a file, using
    Vercel's cleanUrls rules (`/x` -> x.html or x/index.html);
  * no old-domain URL survives;
  * every state folder has index.html, sitemap.xml, llms.txt, 404.html;
  * every sitemap <loc> resolves;
  * every JSON-LD block parses.
Exit status is non-zero on any failure.
"""
import json
import os
import re
import sys
from urllib.parse import unquote

NEW_HOST = "https://www.ecosinsurancesolutions.com"
OLD_DOMAINS = ["georgiamedicareenrollment.com", "medicareenrollmentarizona.com", "californiamedicareenrollment.com",
               "minnesotamedicareenrollment.com", "medicareenrollmentnevada.com", "coloradomedicareenrollment.com",
               "tennesseemedicarequotes.com", "texasmedicareenrollment.com", "medicareenrollmentutah.com",
               "medicareenrollmentflorida.com"]
IGNORE_DIRS = {".git", "scripts", "tools", "docs", "node_modules"}
# Served, but not a state section: no index/sitemap/llms/404 expected inside.
ASSET_DIRS = {"assets"}


def served_files(root):
    out = set()
    for d, dirs, files in os.walk(root):
        dirs[:] = [x for x in dirs if x not in IGNORE_DIRS]
        for f in files:
            out.add(os.path.relpath(os.path.join(d, f), root).replace(os.sep, "/"))
    return out


def resolves(path, files):
    p = unquote(path.split("#")[0].split("?")[0])
    if p.startswith("/"):
        p = p[1:]
    if p == "":
        return "index.html" in files
    if p.endswith("/"):
        p = p[:-1]
    return p in files or p + ".html" in files or p + "/index.html" in files


def main():
    root = os.getcwd()
    files = served_files(root)
    errors = []
    checked = 0
    for rel in sorted(files):
        ext = os.path.splitext(rel)[1].lower()
        if ext not in (".html", ".xml", ".txt", ".css", ".js", ".json", ".webmanifest") or rel == "vercel.json":
            continue  # vercel.json holds redirect patterns, not links
        with open(os.path.join(root, rel), encoding="utf-8", errors="replace") as f:
            text = f.read()
        for od in OLD_DOMAINS:
            if re.search(r"(?i)" + re.escape(od), text):
                errors.append(f"{rel}: old domain {od} still present")
        if rel != "vercel.json" and re.search(r"https?://ecosinsurancesolutions\.com", text):
            errors.append(f"{rel}: new-domain URL without www")
        refs = set()
        if ext == ".html":
            for m in re.finditer(r'\b(?:href|src|action|poster)="([^"]*)"', text):
                refs.add(m.group(1))
            for m in re.finditer(r'srcset="([^"]*)"', text):
                for cand in m.group(1).split(","):
                    refs.add(cand.strip().split(" ")[0])
            for m in re.finditer(r"url\((['\"]?)([^)'\"]+)\1\)", text):
                refs.add(m.group(2))
            for m in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', text, re.S):
                try:
                    json.loads(m.group(1))
                except json.JSONDecodeError as e:
                    errors.append(f"{rel}: JSON-LD does not parse: {e}")
        for m in re.finditer(re.escape(NEW_HOST) + r"(/[^\s\"'<>)]*)?", text):
            refs.add(m.group(1) or "/")
        for r in refs:
            if not r or r.startswith(("#", "data:", "mailto:", "tel:", "sms:", "javascript:")):
                continue
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", r) or r.startswith("//"):
                continue
            checked += 1
            if not r.startswith("/"):
                errors.append(f"{rel}: relative reference left unrewritten: {r}")
                continue
            if r.endswith(".html") and not r.startswith("/tools"):
                errors.append(f"{rel}: internal link keeps .html: {r}")
            if not resolves(r, files):
                errors.append(f"{rel}: broken internal reference {r}")
    for d in sorted(x for x in os.listdir(root) if os.path.isdir(x) and x not in IGNORE_DIRS and x not in ASSET_DIRS):
        for need in ("index.html", "sitemap.xml", "llms.txt", "404.html"):
            if f"{d}/{need}" not in files:
                errors.append(f"{d}/: missing {need}")
    for need in ("index.html", "sitemap.xml", "robots.txt", "llms.txt", "404.html", "vercel.json"):
        if need not in files:
            errors.append(f"root: missing {need}")
    print(f"{len(files)} served files, {checked} internal references checked")
    if errors:
        seen = set()
        for e in errors:
            if e not in seen:
                seen.add(e)
                print("FAIL", e)
        print(f"{len(seen)} problems")
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
