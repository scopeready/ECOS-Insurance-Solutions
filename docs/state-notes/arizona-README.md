# Medicare Enrollment Arizona — Complete Package
**ECOS Medicare Solutions · Darin Weidauer (NPN 18580338)**
Site: https://www.medicareenrollmentarizona.com

## What's in this zip
```
site/     ← THE WEBSITE. This is what you deploy (GitHub → Vercel). 15 pages + assets.
docs/     ← Your reference docs (do NOT deploy these):
            • PROJECT-STATUS.md   – living tracker: done / outstanding / your action items
            • DEPLOY.md           – step-by-step GitHub → Vercel deployment
            • SEO-GEO-PLAYBOOK.md – the master ranking checklist we reuse on every site
source/   ← The generator that builds the site:
            • generate.py – run `python3 generate.py` to rebuild all HTML
            • scenes.py   – regenerates the Arizona illustrations
            • og.py       – regenerates the social-share image
```

## Quick start
1. Open **docs/DEPLOY.md** and follow it: put the contents of **site/** on GitHub, import to Vercel, point your domain.
2. Open **docs/PROJECT-STATUS.md** — that's your checklist of what's left (GA4 ID, Web3Forms email, Google Business Profiles, lead routing, etc.).

## Quick facts
- 15 pages: home, 8 Arizona city pages, About, Contact, Guides hub + 2 guides, 404.
- SEO/GEO: canonical tags, sitemap.xml, robots.txt, JSON-LD schema, llms.txt + llms-full.txt.
- Contact form: emails via Web3Forms **and** saves to your Supabase `website_leads` table, with CMS Permission-to-Contact consent recorded.
- TPMO-compliant disclaimers on every page; both offices (Mesa + Sun City) site-wide.
- Google Analytics 4 code is installed with a placeholder ID — replace `G-XXXXXXXXXX` with your real Measurement ID (in source/generate.py, then rerun; or find-and-replace across site/).

## To edit content later
Edit `source/generate.py`, run `python3 generate.py` (it writes into the site folder), commit to GitHub — Vercel redeploys automatically.

_Last updated: 2026-06-07_

