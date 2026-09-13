# ECOS Insurance Solutions

The consolidated website for ECOS Medicare Solutions (Darin Weidauer, NPN 18580338),
served at **https://www.ecosinsurancesolutions.com**. One static site, one section per
state, all deployed together from this repository through Vercel.

| Section | Was | Pages |
|---|---|---|
| `/arizona` | medicareenrollmentarizona.com | 39 |
| `/california` | californiamedicareenrollment.com | 72 |
| `/colorado` | coloradomedicareenrollment.com | 44 |
| `/florida` | medicareenrollmentflorida.com | 52 |
| `/georgia` | georgiamedicareenrollment.com | 36 |
| `/minnesota` | minnesotamedicareenrollment.com | 42 |
| `/nevada` | medicareenrollmentnevada.com | 51 |
| `/tennessee` | tennesseemedicarequotes.com | 46 |
| `/texas` | texasmedicareenrollment.com | 47 |
| `/utah` | medicareenrollmentutah.com | 40 |

The root (`index.html`) is the hub: it lists the states with their local phone numbers
and links out to the research sites. Everything under a state folder is the original
site, moved, with its links, canonicals and sitemap rewritten to the new address. No
copy was rewritten and no page was rebuilt.

## Layout

```
index.html, 404.html          hub home page and the site-wide 404
robots.txt                    one robots file for the whole site
sitemap.xml                   sitemap index -> sitemap-root.xml + <state>/sitemap.xml
llms.txt                      site summary for AI crawlers; each state keeps its own llms.txt / llms-full.txt
vercel.json                   clean URLs, security headers, and the redirects from every old domain
<state>/                      the ten state sections (see table)
docs/state-notes/             each old repo's CLAUDE.md and README, kept for the state-specific rules
tools/generators/<state>/     the Python generator for the five generator-built states (CA, FL, MN, TX, UT)
scripts/migrate.py            the one-time consolidation script (kept for the record)
scripts/check_links.py        pre-push check: every internal link resolves, no old domain survives
```

`docs`, `tools` and `scripts` are excluded from the deployment by `.vercelignore`.

## URLs

Vercel serves with `cleanUrls: true` and `trailingSlash: false`, so
`texas/houston.html` is `/texas/houston` and `colorado/index.html` is `/colorado`.
Every internal link in the tree is root-absolute and clean (`/colorado/medicare-basics`),
whichever style the source site used.

Each old domain redirects permanently to its state section, path for path, including the
`.html` and trailing-slash spellings the Colorado, Nevada, Tennessee and Arizona sites
used (`vercel.json` → `redirects`). For those redirects to fire, the old domains have to be
attached to this Vercel project.

## Checks

```bash
python3 scripts/check_links.py     # must print OK before pushing
python3 -m http.server 8000        # local preview; clean URLs do not resolve locally, open the .html files
```

## Compliance

This is a Medicare marketing site subject to CMS/TPMO rules. See `CLAUDE.md` and the
per-state notes in `docs/state-notes/`. Do not weaken the disclaimers, the consent
checkboxes, or the sourced dollar figures.
