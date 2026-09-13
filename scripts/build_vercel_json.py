#!/usr/bin/env python3
"""
Regenerate vercel.json: clean URLs, security headers, and the permanent
redirects from every old single-state domain to its section here.

    python3 scripts/build_vercel_json.py

For each old domain (apex and www, matched by a host regex) the rules are, in
order — Vercel takes the first match:

    /                    -> /<state>
    /index.html, /index  -> /<state>
    /robots.txt          -> /robots.txt          (one robots file for the whole site)
    /<dir>/index.html    -> /<state>/<dir>       (Arizona's legacy per-page folders)
    /<page>.html         -> /<state>/<page>      (Colorado, Nevada, Tennessee, Georgia links)
    /<page>/             -> /<state>/<page>      (Arizona's old canonicals)
    /<anything>          -> /<state>/<anything>  (clean URLs, assets, sitemap.xml, llms.txt)

All are 308 permanent redirects. Query strings pass through. The apex of the
new domain redirects to www as well, matching the domain-level redirect in
the Vercel dashboard.
"""
import json
from pathlib import Path

NEW = "https://www.ecosinsurancesolutions.com"
STATES = [
    ("arizona", "medicareenrollmentarizona.com"),
    ("california", "californiamedicareenrollment.com"),
    ("colorado", "coloradomedicareenrollment.com"),
    ("florida", "medicareenrollmentflorida.com"),
    ("georgia", "georgiamedicareenrollment.com"),
    ("minnesota", "minnesotamedicareenrollment.com"),
    ("nevada", "medicareenrollmentnevada.com"),
    ("tennessee", "tennesseemedicarequotes.com"),
    ("texas", "texasmedicareenrollment.com"),
    ("utah", "medicareenrollmentutah.com"),
]


def rules():
    out = [{"source": "/(.*)", "has": [{"type": "host", "value": "ecosinsurancesolutions.com"}],
            "destination": f"{NEW}/$1", "permanent": True}]
    for state, domain in STATES:
        has = [{"type": "host", "value": "(www\\.)?" + domain.replace(".", "\\.")}]
        for source, dest in (
            ("/", f"{NEW}/{state}"),
            ("/index.html", f"{NEW}/{state}"),
            ("/index", f"{NEW}/{state}"),
            ("/robots.txt", f"{NEW}/robots.txt"),
            ("/(.*)/index.html", f"{NEW}/{state}/$1"),
            ("/(.*)\\.html", f"{NEW}/{state}/$1"),
            ("/(.*)/", f"{NEW}/{state}/$1"),
            ("/(.*)", f"{NEW}/{state}/$1"),
        ):
            out.append({"source": source, "has": has, "destination": dest, "permanent": True})
    return out


def main():
    cfg = {
        "$schema": "https://openapi.vercel.sh/vercel.json",
        "cleanUrls": True,
        "trailingSlash": False,
        "headers": [
            {"source": "/(.*)", "headers": [
                {"key": "X-Content-Type-Options", "value": "nosniff"},
                {"key": "Referrer-Policy", "value": "strict-origin-when-cross-origin"},
                {"key": "X-Frame-Options", "value": "SAMEORIGIN"}]},
            {"source": "/(.*)", "missing": [{"type": "host", "value": "www.ecosinsurancesolutions.com"}],
             "headers": [{"key": "X-Robots-Tag", "value": "noindex, nofollow"}]},
        ],
        "redirects": rules(),
    }
    root = Path(__file__).resolve().parent.parent
    (root / "vercel.json").write_text(json.dumps(cfg, indent=2) + "\n")
    print(f"vercel.json: {len(cfg['redirects'])} redirect rules")


if __name__ == "__main__":
    main()
