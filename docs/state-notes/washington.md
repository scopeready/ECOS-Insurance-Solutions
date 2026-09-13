# Washington section — state notes

Built September 2026 with the shared generator engine (`tools/generators/washington/`,
copied unchanged from `tools/generators/texas/` for `generate.py`, `site.js`, `analytics.js`,
`og.py`, `content.py`). Rebuild with `python3 tools/build_state.py washington --og`; never
hand-edit `washington/*.html`. "Washington" on this site always means the State of Washington,
never the District of Columbia — keep "Washington State" in prose where it could be read otherwise.

## Facts the pages rely on (change only with a source in hand)

- **Medigap switching rule.** Washington law lets anyone who *already holds* a Medigap policy
  switch to another Medigap plan or carrier at any time of year without medical underwriting;
  a Plan A holder can move only to another Plan A. It does **not** let a Medicare Advantage member
  into Medigap — that still relies on the six-month open enrollment, a federal guaranteed-issue
  event, or underwriting. The situational page is `/washington/medigap-switching`. Do not paste a
  birthday-rule (CA/OR/NV/IL) or "no switching window" (TX/UT) paragraph into this section.
- **Under-65 Medigap access** is deliberately hedged ("depends on the carrier and current state
  rules; ask us or SHIBA") because it could not be verified when the section was built. Verify with
  the OIC before making a firmer statement.
- **SHIP** is SHIBA (Statewide Health Insurance Benefits Advisors), run by the Office of the
  Insurance Commissioner, 800-562-6900. Named in the TPMO disclaimer, footer, Terms and byline.
- **Medicaid** is Apple Health (Health Care Authority); aged/disabled and Medicare Savings Program
  eligibility runs through DSHS (WashingtonConnection.org; Apple Health customer service
  1-800-562-3022). HCA's 2026 standards: QMB 110% FPL, SLMB 120%, QI-1 138%, **income limits only,
  no resource test**. No dollar MSP figures are printed; only the percentages.
- **2026 MA facts named on the pages:** UW Medicine not contracted with Humana, PacificSource or
  Wellpoint for 2026 (uwmedicine.org); national county exits UHC 109 / Humana 194 / Aetna 100,
  Kaiser unchanged (KFF 2026 spotlight). No Washington-county-specific exits are claimed.
- **Veterans:** VA Puget Sound (Seattle + American Lake, 125,000+ veterans, 14 counties),
  Mann-Grandstaff (Spokane, 30,000+/yr), Jonathan M. Wainwright Memorial (Walla Walla), Vancouver
  campus of VA Portland. Bases pages: JBLM, Naval Base Kitsap, Fairchild AFB (Whidbey and Everett are
  mentioned on the Veterans page but have no page).
- **Privacy** names the Washington My Health My Data Act (RCW 19.373). Terms: governing law Washington.
- Licence: `state_license="1010707"` / "WA License" in `content_site.py`; rendered by the engine
  site-wide and written by hand in the trust strip, About, FAQ, Terms and `llm_facts`.
- Phone is the agency main line (702-706-6564) as a placeholder — `TODO(Darin)` in `content_site.py`.
- The 2026 CMS figures are the shared ones (`SITE["fig"]`); the costs page carries the full IRMAA table.

## Conventions

- Nine regions cover all 39 counties (checked programmatically at build time in the session that
  built it; `counties` strings are the source of truth). 23 city pages, 3 base pages.
- `Texas Medicare Enrollment` appears on every page only as the footer network link and the About
  sister-section link; no Texas copy remains.
