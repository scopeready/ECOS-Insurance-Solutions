# Building a new state section with the generator

This is the brief for adding a state to www.ecosinsurancesolutions.com using the
shared generator engine (the one that built California, Florida, Minnesota, Texas
and Utah). Read it fully before writing anything.

## Where things are

- Repository root: `/home/user/ecos-insurance-solutions`. Do **not** `git commit` or `git push`; the
  orchestrator does that.
- Reference implementation: `tools/generators/texas/` (read every file) and the pages it produces in
  `texas/` (open `texas/index.html`, `texas/houston.html`, `texas/medicare-supplement.html` for the feel).
- Rules that carry over: `docs/state-notes/texas.md`, `docs/state-notes/california.md`.
- Build: `python3 tools/build_state.py <state> --og` writes `<state>/` from `tools/generators/<state>/`.
- Check: `python3 scripts/check_links.py` must end with `OK`. Fix every failure inside your own state
  folder; failures in another state's folder belong to whoever is building it (report them, do not touch).

## Files to create in `tools/generators/<state>/`

Copy **unchanged** from `tools/generators/texas/`: `generate.py`, `site.js`, `analytics.js`, `og.py`,
`content.py`. The engine is meant to be identical across states; do not edit it.

Copy `site.css` and change only the header comment and the colour token values in `:root` (keep the
token names `--lake`, `--lake-dark`, `--lake-tint`, `--spruce`, `--maple`, `--paper`, `--paper-2`, …; the
engine's inline styles reference them). Pick a palette from the state's landscape.

Write fresh, for this state: `content_site.py`, `content_places.py`, `content_topics_a.py`,
`content_topics_b.py`, `content_legal.py`, `scenes.py`. The Texas modules are the **schema**: same
dict keys, same list shapes, same tokens (`[[PHONE]]`, `[[TEL]]`, `[[EMAIL]]`, `[[QUOTE]]`, `[[YEAR]]`,
`[[STATE]]`, `[[SHIP]]`, `[[SHIPPHONE]]`). The prose is **not** Texas with the nouns swapped: write it
for this state, from what you verified.

## SITE values that are fixed

```python
url="https://www.ecosinsurancesolutions.com/<state>"      # no trailing slash
domain="ecosinsurancesolutions.com/<state>"
name="<State> Medicare Enrollment"
org="ECOS Medicare Solutions"
# TODO(Darin): replace with the <State> number once he provides it. Main line as placeholder.
phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338"
# no state_license / state_license_label keys until Darin provides the number — see below
web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer"
plan_year=2026, TODAY = date(2026, 9, 13)
fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615",
         partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000")   # 2026 CMS figures, verbatim
```

`network` lists every other section of this site plus the two research sites, with these exact URLs
(drop your own state from the list):

```
("Medicare Enrollment Arizona", "https://www.ecosinsurancesolutions.com/arizona")
("California Medicare Enrollment", "https://www.ecosinsurancesolutions.com/california")
("Colorado Medicare Enrollment", "https://www.ecosinsurancesolutions.com/colorado")
("Medicare Enrollment Florida", "https://www.ecosinsurancesolutions.com/florida")
("Georgia Medicare Enrollment", "https://www.ecosinsurancesolutions.com/georgia")
("Hawaii Medicare Enrollment", "https://www.ecosinsurancesolutions.com/hawaii")
("Indiana Medicare Enrollment", "https://www.ecosinsurancesolutions.com/indiana")
("Minnesota Medicare Enrollment", "https://www.ecosinsurancesolutions.com/minnesota")
("Medicare Enrollment Nevada", "https://www.ecosinsurancesolutions.com/nevada")
("New Mexico Medicare Enrollment", "https://www.ecosinsurancesolutions.com/new-mexico")
("North Carolina Medicare Enrollment", "https://www.ecosinsurancesolutions.com/north-carolina")
("Ohio Medicare Enrollment", "https://www.ecosinsurancesolutions.com/ohio")
("South Carolina Medicare Enrollment", "https://www.ecosinsurancesolutions.com/south-carolina")
("Tennessee Medicare Quotes", "https://www.ecosinsurancesolutions.com/tennessee")
("Texas Medicare Enrollment", "https://www.ecosinsurancesolutions.com/texas")
("Medicare Enrollment Utah", "https://www.ecosinsurancesolutions.com/utah")
("Washington Medicare Enrollment", "https://www.ecosinsurancesolutions.com/washington")
("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com")
("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")
```

`sameas_org_extra` as in Texas. `sameas_darin`: the MyECOS360, LinkedIn and YouTube URLs from Texas, plus
`https://www.ecosinsurancesolutions.com/<other-state>/about` for arizona, california, florida, minnesota,
texas, utah and `https://www.mymedigaprate.com/about`. Never write an old single-state domain anywhere
(`texasmedicareenrollment.com` and the like); the checker fails on them.

## The licence number

Darin has not yet supplied this state's producer licence number. The engine shows one only when
`SITE["state_license"]` exists, so leave the key out. Everywhere the Texas text names "TX License
#2514981" by hand (trust strip, About credentials, About "Licensing", FAQ "Where can I verify your
licence", Terms, `llm_facts`), write the NPN only and put a `# TODO(Darin): add <ST> licence number`
comment next to it in the module. Never invent a number. The About "Licensing" paragraph lists the
states he is licensed in: Arizona, California, Colorado, Florida, Georgia, Hawaii, Indiana, Minnesota,
Nevada, New Mexico, North Carolina, Ohio, South Carolina, Tennessee, Texas, Utah and Washington.

## Topic pages (slugs the engine and the site chrome depend on)

`content_topics_a.py`: `medicare-advantage`, `medicare-supplement`, `part-d`, `medicare-costs`.
`content_topics_b.py`: `turning-65`, one **state-specific situational page** in place of Texas's
`winter-texans` (choose the situation that actually matters in this state and name the slug for it),
`veterans`, `medicaid`, `chronic-snp`, `institutional-snp`, `retirement-guide`.

Every `href` in `NAV`, `FOOTER_COLS`, `PLACE_CARDS`, `notfound_links`, `HOME["different_cards"]`,
`HOME["situations"]` and inside page bodies must point at a slug that exists (a topic, a city, a
region, a base, `/about`, `/faq`, `/privacy`, `/terms`, `/#areas`, `/#get-help`). The checker catches
broken ones after the build; fix them at the source.

Each topic page needs `keyfacts` (answer-first), `faqs` (mirrored into FAQPage JSON-LD), and `sources`
(name, URL) for every state-specific claim on the page. Keep the `retirement-guide` page's shape
(the book offer: emailed on request, nothing for sale), adapted to the state's readers.

## Places

`REGIONS`: 6–9 regions that together cover **every county in the state** (the `counties` string of
each region lists its counties; a reader from any county should find their region). Each region:
`slug, name, short, scene, eyebrow, h1, sub, counties, cities (slugs), systems, note, intro (2 paras),
faqs (3)`. `CITIES`: 14–20 cities, weighted to where people on Medicare live. Each city: `slug, name,
county, region (slug), scene, sub, communities, systems (real, named health systems / hospitals you
verified serve that city), intro (2 paras), faqs (3), nearby (3–4 existing city/base slugs)`.
`BASES`: 0–3 military communities where a large military-retiree population lives near an
installation; empty list is acceptable if the state has none of note. Do not name a hospital you could
not verify.

## Scenes

`scenes.py` must define every `scene` key referenced anywhere (HOME, faq_page, topics, regions,
cities, bases). Write 8–10 layered-silhouette SVG scenes in the state palette, following the helper
pattern in the Texas file (`wrap`, `sun`, `ground`, plus your own landscape helpers). They should
read as this state: its coastline, mountains, farmland, skylines, landmarks.

## Facts, and how to get them

Use WebSearch and WebFetch. Verify, then cite, every state-specific claim: the SHIP program's name and
phone; the Medicaid program's name and the agency that runs it, plus its aged/disabled managed-care
program if one exists; the insurance department's name and licence-lookup; Medigap rules (plan
letters or a waiver structure, any birthday/anniversary/year-round switching rule, under-65 access);
Medicare Savings Programs; any state supplement to Extra Help; veteran population and VA medical
centres; 2026 Medicare Advantage carrier exits or county changes **only if a source names them**;
disaster-related Special Enrollment Periods where relevant (hurricanes, wildfires, floods); and the
big health systems per region. Where a source contradicts your assumption, the source wins. Where you
cannot verify, leave it out; a page that says less is fine, a page that is wrong is not.

Do not invent carrier counts ("10 carriers") or lists. Do not invent premiums. The only dollar figures
are the 2026 CMS figures above and figures you cite to a source on that page.

## Legal

`content_legal.py`: FAQ page (12–16 questions this state's readers ask), About body (same structure as
Texas, this state's facts), Privacy (name the state's consumer privacy law only if one applies and you
verified it; otherwise omit that sentence), Terms (governing law: this state; SHIP named).

## Compliance wording that stays

TPMO disclaimer with this state's SHIP named; "not connected with or endorsed by the U.S. government
or the federal Medicare program"; the consent checkbox and `consent_text` (the engine renders them);
no health questions on any form; the compensation disclosure in the footer (engine). `not_affiliated`
names the state, its Medicaid agency and its insurance department.

## Finish

1. `python3 tools/build_state.py <state> --og` builds cleanly.
2. `python3 scripts/check_links.py` prints `OK` (or only failures outside your folder).
3. In `<state>/*.html`, `grep -l "Texas\|Texan\|STAR+PLUS\|HICAP\|\[\["` returns nothing.
4. Open two or three built pages and read them as a resident would.
5. Report: page count, the sources behind the key state facts, what you left out as unverifiable, and
   the TODOs you left for Darin (licence number, phone).
