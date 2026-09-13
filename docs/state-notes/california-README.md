# California Medicare Enrollment

Static lead-generation site for **ECOS Medicare Solutions** (Darin Weidauer, NPN 18580338) serving California — https://www.californiamedicareenrollment.com

## What's here

- `*.html` at the repo root — the site (indexable pages + thank-you + 404), served at clean URLs (`/los-angeles`, `/kaiser`).
- `site.css`, `site.js`, `analytics.js`, `favicon.svg`, `og-image.png`, `darin.jpg` — shared assets.
- `sitemap.xml`, `robots.txt`, `llms.txt`, `llms-full.txt` — crawl and AI-discovery files.
- `vercel.json` (clean URLs, security headers), `CNAME` + `.nojekyll` (GitHub Pages fallback).
- `source/` — **the generator.** `generate.py` is the shared ECOS state-site engine; everything California-specific is in `content_site.py` (identity, home), `content_places.py` (regions, cities, military communities), `content_topics_a.py` / `content_topics_b.py` (guide pages; `costs_page.py` holds the shared costs-page template), `content_legal.py` (FAQ, about, privacy, terms), `scenes.py` (hero art) and `site.css` (palette). `og.py` renders the share image.

## California licence number

Cal. Ins. Code §1725.5 requires the producer licence number next to the licensee's name in advertising. `SITE["state_license"] = "0M00978"` in `source/content_site.py` makes the engine print **CA License #0M00978** beside every mention of Darin's name (footer, byline, about page, Person JSON-LD, llms files); it is also written into the home-page trust strip and the legal pages by hand. Do not remove it.

## Editing

```bash
python3 source/generate.py     # rebuild every page + sitemap + llms files
python3 source/og.py           # rebuild og-image.png (needs Pillow)
python3 -m http.server 8000    # preview: open /index.html, /los-angeles.html etc.
```

Edit the `source/content_*.py` files, re-run, commit. Do not hand-edit the generated HTML — the next build overwrites it.

## Before launch (Darin's checklist)

1. **Phone number.** `phone`/`tel` in `source/content_site.py` are the agency's main line; swap in a California number and rebuild.
2. **GA4.** Set `MEASUREMENT_ID` in `analytics.js` (it stays silent until you do).
3. **Web3Forms.** The form uses the shared agency key, so leads already arrive; create a California-specific key if you want them routed separately.
4. **TPMO disclaimer.** The footer uses the count-free CMS wording. Add California carrier/product counts to `tpmo` in `content_site.py` if wanted.
5. The 2026 Anthem PPO exit and the Aetna/UnitedHealthcare/Humana county reductions are cited to KFF, Kiplinger and a California trade article; re-check each October when the next year's landscape is published.
6. Vercel: import the repo, add the domain, set the production branch to `main`.
