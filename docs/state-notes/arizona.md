# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

Static marketing/lead-generation site for ECOS Medicare Solutions (agent: Darin Weidauer, NPN 18580338) serving Arizona, live at https://www.medicareenrollmentarizona.com. There is no framework, package manager, build step, test suite, or linter in this repo — it holds hand-editable HTML plus shared assets. (The README references a `source/generate.py` generator, but that generator is **not** in this repository; only its output was uploaded. Edit the HTML directly.)

## Deployment

- Hosted on **Vercel**, auto-deploying from GitHub. `vercel.json` sets `cleanUrls: true` and `trailingSlash: false`, so `medicare-phoenix-az.html` is served at `/medicare-phoenix-az`.
- Internal links and asset paths are **root-absolute** (`/about`, `/assets/styles.css`) and internal links omit the `.html` suffix to match clean URLs. Canonical URLs have no `.html` and no trailing slash (e.g. `https://www.medicareenrollmentarizona.com/medicare-phoenix-az`).

## Which files are live (important)

The repo contains **two generations of the site plus stray upload artifacts**. Only the first group is current:

1. **Current (edit these)** — flat `*.html` files at the repo root (June 2026 generation): `index.html`, `404.html`, `about.html`, `contact.html`, `guides.html`, 9 city pages (`medicare-<city>-az.html`), and 2 guide pages (`medicare-advantage-vs-medigap-arizona.html`, `turning-65-checklist-arizona.html`). These match `sitemap.xml` and are what Vercel serves at the clean URLs.
2. **Legacy (do not edit, do not emulate)** — per-page directories (`about/`, `contact/`, `guides/`, `medicare-<city>-az/`, each containing an `index.html`) from the original June 7 generation, plus root-level `styles.css`, `hero.svg`, `pines.svg`, `redrock.svg`, `river.svg`, `saguaro.svg`, `favicon.svg`, `ecos-logo.png`.
3. **Stray artifacts** — `index (1).html` … `index (13).html` are leftover browser-upload duplicates (some are not even HTML; `index (12).html` is a JPEG). Ignore them.

Only delete legacy/stray files if the user asks.

### Asset history (why things look the way they do)

The original June 2026 upload was missing the current generation's stylesheet and hero photos (`/assets/photos/*.webp` never existed in the repo). These gaps were later fixed **in-repo**: `assets/styles.css` was rewritten from scratch for the current markup, hero images were replaced with generated SVG scenes in `assets/scenes/` (one per page, layered-silhouette desert style in the brand palette), social-share/JSON-LD images point at `assets/og-image.png`, and `/assets/favicon.svg` was added. If a generator package (`source/generate.py`) resurfaces, do not regenerate over these files blindly — the repo versions are the live source of truth.

## Site structure

- Shared assets live in `assets/`: `styles.css`, `site.js`, `scenes/` (SVG hero illustrations + favicon), `og-image.png`. Every current page loads `/assets/styles.css`, `/assets/site.js`, and Google Fonts (Fraunces + Libre Franklin).
- `assets/site.js` is dependency-free and guarded per-page. Most of its handlers (`#contactForm`, `#penBtn`, `#iepBtn`, hamburger, cost tabs) target the **legacy** generation's IDs and are inert on current pages; the block at the bottom (`#pbCalc`/`#pdCalc`) powers the homepage penalty calculators. The current contact form submits natively to Web3Forms via its `action` attribute — it does not go through site.js.
- The header logo is an **inline SVG** (`<svg class="logo-mark">`, an Arizona desert scene: sunset sky, sun, red-rock mesa, saguaro) duplicated in every current page — changing it means editing all 15 files with an identical find-and-replace.
- Google Analytics 4 snippets are installed with the placeholder ID `G-XXXXXXXXXX` on every page (3 occurrences per page); replacing it is a site-wide find-and-replace.

## Contact form

The form on `contact.html` POSTs natively to `https://api.web3forms.com/submit` (Web3Forms `access_key` in a hidden field) with a `botcheck` honeypot and a required `tcpa_consent` permission-to-contact checkbox. Do not remove the consent checkbox or its wording.

`assets/site.js` also contains a legacy dual-write handler (`#contactForm`) that additionally POSTs leads to a Supabase `website_leads` REST endpoint via `data-sb-url` / `data-sb-key` form attributes; it is inert on the current page because the form doesn't carry that ID. If lead capture to Supabase is wanted again, wire the current form to that handler rather than rewriting it.

## Key conventions

- **Pages are self-contained.** Header, nav, footer, disclaimers, GA snippet, and JSON-LD are duplicated in every HTML file. Any site-wide change must be applied to every current page — grep across the 15 flat files and verify with a count.
- **SEO/AI-discovery files must stay in sync with the page set**: when adding, renaming, or removing a page, update `sitemap.xml`, `llms.txt`, and `llms-full.txt` (clean URLs, no `.html`).
- Every current page has a canonical tag, meta description, Open Graph/Twitter tags, and JSON-LD structured data.

## Local preview

```bash
python3 -m http.server 8000   # note: clean URLs won't resolve locally; open the .html filenames directly
```

## Compliance — do not weaken

This is a Medicare marketing site subject to CMS/TPMO rules:

- Every page carries the TPMO disclaimer ("…not connected with or endorsed by the United States government or the federal Medicare program"). Preserve this wording site-wide.
- Pages cite specific plan-year dollar figures (Part B premium, deductibles, Part D cap). Do not invent or "update" these numbers — only change them when the user supplies verified figures, and keep `llms.txt`/`llms-full.txt` consistent with the pages.
- 1-800-MEDICARE is referenced as the official fallback; the business phone is 480-845-0246, with Mesa and Sun City offices listed site-wide.
