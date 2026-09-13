# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this is

The consolidated ECOS Medicare Solutions website (agent: Darin Weidauer, NPN 18580338),
live at https://www.ecosinsurancesolutions.com. Seventeen state sections: ten former
single-state sites moved in (`/arizona`, `/california`, `/colorado`, `/florida`, `/georgia`,
`/minnesota`, `/nevada`, `/tennessee`, `/texas`, `/utah`) and seven built here with the
generator (`/hawaii`, `/indiana`, `/new-mexico`, `/north-carolina`, `/ohio`,
`/south-carolina`, `/washington`; see `docs/state-build-brief.md`). The root `index.html`
is a hub that lists them. Static HTML, no framework, no build step; hosted on Vercel, auto-deploying
from `main`.

Read `README.md` for the layout, and `docs/state-notes/<state>.md` before editing a state
section: each note carries that state's rules (Medigap plan structure, Medicaid program
name, birthday rules, licence number placement, placeholder phone numbers) written by the
people who built it. Those rules still apply.

## How the sections differ

Three template families were consolidated. Respect each one's conventions inside its folder:

- **Generator family** (California, Florida, Minnesota, Texas, Utah, and the seven new
  states): built by `tools/generators/<state>/generate.py`. Never hand-edit these folders;
  edit the `content_*.py` modules and run `python3 tools/build_state.py <state> --og`,
  which prefixes every link with `/<state>` and copies the result in. Adding a state:
  build it, then run `scripts/update_network.py`, rebuild every generator state, and add
  the hub card, footer entry, sitemap-index line and root `llms.txt` line.
- **Nevada template family** (Colorado, Nevada, Tennessee): hand-editable flat HTML; the
  Python build scripts were never in the repos. Header, nav, footer and JSON-LD are
  duplicated in every page, so a site-wide change in one of these folders means editing
  every file in it and verifying with a count.
- **Arizona and Georgia**: older flat HTML. Arizona's legacy per-page directories and stray
  upload duplicates were deliberately left behind.

## Site-wide rules

- **Links are root-absolute and clean** everywhere: `/texas/houston`, `/colorado/style.css`.
  Never write `.html` in a link or a relative path. Vercel's `cleanUrls` serves
  `texas/houston.html` at `/texas/houston`.
- **Cross-state links are internal.** The "Our network" footer strips and the JSON-LD
  `sameAs` lists point at `https://www.ecosinsurancesolutions.com/<state>`, never at the old
  domains. `scripts/check_links.py` fails if an old domain reappears.
- **Sitemaps and llms files stay in sync with the pages.** Each state has its own
  `sitemap.xml`, `llms.txt` and `llms-full.txt`; the root `sitemap.xml` is an index of them.
  Adding a state means adding its folder, its line in the sitemap index, root `llms.txt`,
  the hub page's state list and the footer, plus its old-domain redirect in `vercel.json`
  if it had one.
- **Run `python3 scripts/check_links.py` before every push.** It checks every internal
  reference resolves under the cleanUrls rules, no old domain survives, every JSON-LD block
  parses, and each section still has its index, sitemap, llms.txt and 404.
- **Florida's licensed agent is Ronilin Weidauer** (NPN 19427652, FL License #W690636), set through
  `SITE["agent"]` in the Florida generator; the engine names the agent of record while Darin remains
  the author. Any other section may name a different agent the same way.
- **Google Analytics 4 is one property for the whole site**, Measurement ID G-7CXH7ZLSP1, set as
  `MEASUREMENT_ID` in every section's `analytics.js`, in the generator copies under
  `tools/generators/*/analytics.js`, and in the root `analytics.js` the hub and 404 load.
  Change it everywhere at once or not at all.
- Each state keeps its own phone number and licence number. Several sections use the
  agency's main line (702-706-6564) as a deliberate placeholder; see the state notes.

## Compliance — do not weaken

CMS/TPMO rules apply to every page, the hub included.

- Every page carries the TPMO disclaimer and the "not connected with or endorsed by the
  United States government or the federal Medicare program" wording. Preserve it.
- 1-800-MEDICARE, Medicare.gov and each state's SHIP program are named as the official,
  independent alternatives. Keep them.
- Every lead form posts to Web3Forms with a `botcheck` honeypot and a required
  permission-to-contact checkbox whose wording is recorded in a hidden `consent_text`
  field. Do not remove or soften either. No form asks a health question.
- Dollar figures are the verified 2026 CMS figures, cited on each page. Do not invent or
  "update" them; change them only when the user supplies verified figures for the new
  plan year, and keep every page and llms file consistent.
- State licence numbers stay next to Darin's name where a state requires it (California
  #0M00978 under Cal. Ins. Code §1725.5; Arizona, Georgia, Minnesota, Texas and Utah also
  show theirs).
- The hub page names the agency as "ECOS Medicare Solutions" inside "ECOS Insurance
  Solutions"; keep the agency name the state pages use unless the user asks to rebrand.
