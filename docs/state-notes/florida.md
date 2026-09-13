# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

Static marketing / lead-generation site for ECOS Medicare Solutions (agent: Darin Weidauer, NPN 18580338) serving **Florida**, at https://medicareenrollmentflorida.com. One of the ECOS state sites (Arizona, Georgia, Minnesota, Nevada, Colorado, Tennessee, Texas, Utah, plus the MyMedigapRate research site and Darin's MyECOS360 author page); they cross-link in the footer "Our network" strip and in the Organization `sameAs`.

## The generator is the source of truth

`source/generate.py` is the **shared engine** used by the newer ECOS state sites (Minnesota was the first); it should stay identical across them. Everything Florida-specific lives in the `source/content_*.py` modules, `source/scenes.py` (SVG hero art) and `source/site.css` (palette). **Edit the source and re-run `python3 source/generate.py`; never hand-edit a generated page.**

- Identity, phone, Web3Forms key, plan-year figures, network list, TPMO wording, nav, footer columns, home page: `content_site.py`.
- Regions, cities, military-community pages: `content_places.py` (one dict each; the generator writes the page, the footer links, the sitemap and both llms files).
- Guide pages: `content_topics_a.py` / `content_topics_b.py`; each has `keyfacts` (answer-first summary), `faqs` (mirrored into FAQPage JSON-LD) and `sources`.
- Links are root-absolute clean URLs (`/tampa`, not `tampa.html`). Vercel `cleanUrls` and GitHub Pages both resolve them.
- CSS tokens keep the names from the first (Minnesota) build (`--lake`, `--spruce`, `--maple`) with Florida values; do not rename them, the engine's inline styles reference `--lake-dark`.

## Compliance — do not weaken

CMS/TPMO rules apply.

- Every page carries the TPMO disclaimer and the "not connected with or endorsed by the United States government or the federal Medicare program" wording, plus the licensing/compensation disclosure, in the footer. Keep them.
- 1-800-MEDICARE, Medicare.gov and **Florida SHINE (1-800-963-5337)** are named as the official, independent alternatives.
- The lead form carries the permission-to-contact checkbox and its wording; the hidden `consent_text` records exactly what was agreed. Do not remove either. The form asks no health questions.
- **Do not invent or "update" dollar figures.** The 2026 Medicare figures come from the CMS release of Nov 14, 2025 and live in `SITE["fig"]` plus the costs page. Florida-specific claims (issue-age rating, the under-65 window, no birthday rule, the 2026 AvMed exit and UnitedHealthcare county cuts, SMMC Long-Term Care, hurricane SEPs) are cited in each page's "Sources" block. Change them only with a source in hand.
- Florida facts other states' pages get wrong: Florida uses the **federal plan letters**, requires **issue-age Medigap rating** (attained-age is prohibited), has **no birthday rule**, gives **under-65 beneficiaries a six-month guaranteed-issue window** at Part B enrollment, runs Medicaid long-term care through **SMMC Long-Term Care** (eligibility via DCF / ACCESS Florida, assessment via CARES), and aligns D-SNPs with Medicaid plans. A FEMA disaster declaration opens a Special Enrollment Period. Do not paste Texas/Utah/Minnesota copy into this site.
- The phone number is the agency's main line as a deliberate placeholder (see README); the carrier list is not enumerated anywhere on purpose.

## Preview / checks

```bash
python3 source/generate.py && python3 -m http.server 8000   # open /index.html, /tampa.html
```
After a build: every JSON-LD block must parse, every `/slug` link must have a file, no `[[TOKEN]]` may remain, and `sitemap.xml` must list exactly the indexable pages.
