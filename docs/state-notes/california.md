# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

Static marketing / lead-generation site for ECOS Medicare Solutions (agent: Darin Weidauer, NPN 18580338) serving **California**, at https://www.californiamedicareenrollment.com. One of the ECOS state sites (Arizona, Georgia, Minnesota, Nevada, Colorado, Tennessee, Texas, Utah, Florida, plus the MyMedigapRate research site and Darin's MyECOS360 author page); they cross-link in the footer "Our network" strip and in the Organization `sameAs`.

## The generator is the source of truth

`source/generate.py` is the **shared engine** used by the newer ECOS state sites (Minnesota was the first); it should stay identical across them. Everything California-specific lives in the `source/content_*.py` modules, `source/scenes.py` (SVG hero art) and `source/site.css` (palette). **Edit the source and re-run `python3 source/generate.py`; never hand-edit a generated page.**

- Identity, phone, Web3Forms key, plan-year figures, network list, TPMO wording, nav, footer columns, home page: `content_site.py`.
- Regions, cities, military-community pages: `content_places.py` (one dict each; the generator writes the page, the footer links, the sitemap and both llms files).
- Guide pages: `content_topics_a.py` / `content_topics_b.py`; each has `keyfacts` (answer-first summary), `faqs` (mirrored into FAQPage JSON-LD) and `sources`.
- Links are root-absolute clean URLs (`/los-angeles`, not `los-angeles.html`). Vercel `cleanUrls` and GitHub Pages both resolve them.
- CSS tokens keep the names from the first (Minnesota) build (`--lake`, `--spruce`, `--maple`) with California values; do not rename them, the engine's inline styles reference `--lake-dark`.

## Compliance — do not weaken

CMS/TPMO rules apply.

- Every page carries the TPMO disclaimer and the "not connected with or endorsed by the United States government or the federal Medicare program" wording, plus the licensing/compensation disclosure, in the footer. Keep them.
- 1-800-MEDICARE, Medicare.gov and **California HICAP (1-800-434-0222)** are named as the official, independent alternatives.
- The lead form carries the permission-to-contact checkbox and its wording; the hidden `consent_text` records exactly what was agreed. Do not remove either. The form asks no health questions.
- **Do not invent or "update" dollar figures.** The 2026 Medicare figures come from the CMS release of Nov 14, 2025 and live in `SITE["fig"]` plus the costs page. California-specific claims (the 60-day birthday rule, the under-65 window, Kaiser Senior Advantage, the 2026 Anthem PPO exit and county cuts, the Medi-Cal asset limit reinstated January 1, 2026, Medi-Medi Plans in 41 counties, CalPERS rules, wildfire SEPs) are cited in each page's "Sources" block. Change them only with a source in hand.
- California facts other states' pages get wrong: California uses the **federal plan letters**, has a **60-day Medigap birthday rule** (starting on the birthday, equal or lesser benefits, any carrier, existing policyholders only), requires insurers to **offer Medigap to under-65 disabled beneficiaries** (not ESRD), and **Kaiser Senior Advantage is the only way to keep Kaiser on Medicare** (Medigap does not work at Kaiser). Most non-Kaiser Advantage plans delegate care to a **medical group**. Medicaid is **Medi-Cal** (DHCS; county eligibility; asset limit **$130,000 + $65,000 per additional person from Jan 1, 2026**), aligned D-SNPs are **Medi-Medi Plans** (41 counties in 2026), and CalPERS retirees use CalPERS Medicare plans. A FEMA disaster declaration (wildfires) opens a Special Enrollment Period. Do not paste Texas/Utah/Florida copy into this site.
- **The California licence number (#0M00978) must stay next to Darin's name everywhere** (Cal. Ins. Code §1725.5). The engine renders it from `SITE["state_license"]`; the trust strip, About, FAQ, Privacy and Terms carry it by hand.
- The phone number is the agency's main line as a deliberate placeholder (see README); the carrier list is not enumerated anywhere on purpose.

## Preview / checks

```bash
python3 source/generate.py && python3 -m http.server 8000   # open /index.html, /los-angeles.html
```
After a build: every JSON-LD block must parse, every `/slug` link must have a file, no `[[TOKEN]]` may remain, and `sitemap.xml` must list exactly the indexable pages.
