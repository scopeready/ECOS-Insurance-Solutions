"""South Carolina site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 13)
# Brand mark: indigo disc, a marsh-gold palmetto (the state's tree) — the Sabal palmetto that gave the Palmetto State its name.
_PALM = ('<path d="M21 34c-1-9 0-15 0-20" stroke="#c9a84a" stroke-width="3" stroke-linecap="round"/>'
         '<g stroke="#c9a84a" stroke-width="2.6" stroke-linecap="round"><path d="M21 15L9 9M21 15L10 16M21 15L13 22M21 15l12-6M21 15l11 1M21 15l8 7M21 15l-3-9M21 15l3-9"/></g>'
         '<circle cx="21" cy="15" r="2.6" fill="#c9a84a"/>')
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#1f2d5c"/>' + _PALM + '</svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#1f2d5c"/>' + _PALM + '</svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.ecosinsurancesolutions.com/south-carolina", domain="ecosinsurancesolutions.com/south-carolina", name="South Carolina Medicare Enrollment",
    org="ECOS Medicare Solutions", state="South Carolina", abbr="SC", demonym="South Carolinians",
    # TODO(Darin): replace with the South Carolina number once he provides it. Main line as placeholder.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # South Carolina producer licence (same digits as the NPN); the engine shows it beside Darin's name site-wide.
    state_license="18580338", state_license_label="SC License",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Medicare Enrollment Arizona", "https://www.ecosinsurancesolutions.com/arizona"),
             ("California Medicare Enrollment", "https://www.ecosinsurancesolutions.com/california"),
             ("Colorado Medicare Enrollment", "https://www.ecosinsurancesolutions.com/colorado"),
             ("Medicare Enrollment Florida", "https://www.ecosinsurancesolutions.com/florida"),
             ("Georgia Medicare Enrollment", "https://www.ecosinsurancesolutions.com/georgia"),
             ("Hawaii Medicare Enrollment", "https://www.ecosinsurancesolutions.com/hawaii"),
             ("Indiana Medicare Enrollment", "https://www.ecosinsurancesolutions.com/indiana"),
             ("Minnesota Medicare Enrollment", "https://www.ecosinsurancesolutions.com/minnesota"),
             ("Medicare Enrollment Nevada", "https://www.ecosinsurancesolutions.com/nevada"),
             ("New Mexico Medicare Enrollment", "https://www.ecosinsurancesolutions.com/new-mexico"),
             ("North Carolina Medicare Enrollment", "https://www.ecosinsurancesolutions.com/north-carolina"),
             ("Ohio Medicare Enrollment", "https://www.ecosinsurancesolutions.com/ohio"),
             ("Tennessee Medicare Quotes", "https://www.ecosinsurancesolutions.com/tennessee"),
             ("Texas Medicare Enrollment", "https://www.ecosinsurancesolutions.com/texas"),
             ("Medicare Enrollment Utah", "https://www.ecosinsurancesolutions.com/utah"),
             ("Washington Medicare Enrollment", "https://www.ecosinsurancesolutions.com/washington"),
             ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"),
             ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")],
    sameas_org_extra=["https://howdoiapplyformedicare.com", "https://medicareadvantageanswers.com", "https://dentalinsurancetomorrow.com"],
    sameas_darin=["https://www.myecos360.com/darin-weidauer", "https://www.linkedin.com/in/darin-weidauer-3165a816b/", "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
                  "https://www.ecosinsurancesolutions.com/arizona/about", "https://www.ecosinsurancesolutions.com/california/about",
                  "https://www.ecosinsurancesolutions.com/minnesota/about", "https://www.ecosinsurancesolutions.com/texas/about", "https://www.ecosinsurancesolutions.com/utah/about",
                  "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or I-CARE (Insurance Counseling Assistance and Referrals for Elders, South Carolina&rsquo;s State Health "
          "Insurance Assistance Program run by the South Carolina Department on Aging, 800-868-9095) to get information on all of your options."),
    not_affiliated="the State of South Carolina, the South Carolina Department of Health and Human Services, Healthy Connections Medicaid, the South Carolina Department on Aging, or the South Carolina Department of Insurance",
    ship_name="I-CARE (South Carolina SHIP)", ship_phone="800-868-9095",
    brand_tag="Plain-English Medicare help in South Carolina", theme_color="#1f2d5c",
    footer_tagline="Plain-English Medicare guidance for South Carolina retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping South Carolina retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Greenville and Columbia to Charleston, Myrtle Beach and Hilton Head.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and Healthy Connections Medicaid dual eligibility",
                 "Moving to South Carolina on Medicare", "Hurricane disaster Special Enrollment Periods", "Medicare for military retirees and veterans"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "I just moved to South Carolina", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I have VA / TRICARE", "I have Medicaid too", "My premium went up"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Moving to South Carolina, losing a plan, or a FEMA hurricane declaration each open a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across South Carolina',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/new-to-south-carolina">Moving to South Carolina on Medicare</a>', '<a href="/medicaid">Healthy Connections Medicaid and the Medicare Savings Programs</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="marsh", h1="South Carolina Medicare questions, answered plainly",
                  sub="The questions we hear most from South Carolinians &mdash; about Medigap rules with no birthday window, moving here from up north, the end of Healthy Connections Prime, MUSC and Prisma networks, TRICARE, hurricanes, and what any of this costs. Short answers, with links to the longer ones.",
                  title="South Carolina Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions South Carolinians ask most: Medigap rules and under-65 options, moving to South Carolina, Healthy Connections Medicaid and D-SNPs, I-CARE, TRICARE, hurricane SEPs and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for South Carolina retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from the Upstate and the Midlands to Charleston, the Grand Strand, the Pee Dee and the Lowcountry.",
    llm_facts=["Darin Weidauer holds South Carolina insurance license #18580338 (NPN 18580338); verify through the South Carolina Department of Insurance licensee search or the NIPR.",
               "South Carolina uses the federal Medigap plan letters (A–N) and has no birthday rule, anniversary rule or annual switching window; the South Carolina Department of Insurance regulates Medigap. State law does not require insurers to sell Medigap to people under 65 on Medicare because of a disability, though some carriers do, and the state's high-risk pool offers guaranteed-issue options for that group.",
               "About 1.25 million South Carolinians are on Medicare and roughly 46% of them are in Medicare Advantage as of early 2026; Advantage plans are marketed in all 46 counties.",
               "South Carolina's SHIP is I-CARE (Insurance Counseling Assistance and Referrals for Elders), run by the South Carolina Department on Aging through the regional Area Agencies on Aging: 800-868-9095.",
               "South Carolina Medicaid is Healthy Connections, administered by the South Carolina Department of Health and Human Services (SCDHHS); apply at apply.scdhhs.gov. The Medicare Savings Programs (QMB, SLMB, QI) are also handled by SCDHHS and automatically qualify the enrollee for Part D Extra Help. Healthy Connections Prime, the state's Medicare-Medicaid plan for people 65 and over, ended on December 31, 2025; dual-eligible members now use Dual Special Needs Plans (D-SNPs).",
               "Veterans in South Carolina are served by the Ralph H. Johnson VA Health Care System in Charleston (with clinics in Beaufort, North Charleston, Goose Creek and Myrtle Beach) and the Columbia VA Health Care System anchored by the Wm. Jennings Bryan Dorn VA Medical Center; the largest military-retiree communities are around Joint Base Charleston, Shaw Air Force Base (Sumter), Fort Jackson (Columbia) and the Marine Corps installations at Beaufort.",
               "Moving to South Carolina opens a Special Enrollment Period to choose a plan sold in your new county, and leaving a Medicare Advantage plan's service area is a federal guaranteed-issue event for Medigap. A FEMA-declared hurricane emergency or major disaster opens a Special Enrollment Period for people in the declared counties who missed an enrollment deadline because of it."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/new-to-south-carolina", "New to SC"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in South Carolina</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/new-to-south-carolina">Moving to South Carolina &amp; hurricanes</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Healthy Connections Medicaid &amp; D-SNPs</a>',
                   '<a href="/faq">Questions South Carolinians ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://aging.sc.gov" rel="noopener">I-CARE, South Carolina&rsquo;s SHIP</a>, 800-868-9095',
                                    '<a href="https://doi.sc.gov" rel="noopener">South Carolina Department of Insurance</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a local network &mdash; so your providers, your county and your prescriptions matter.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; MUSC, Prisma, Duke or Emory across the line, or the hospital in your county seat.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Healthy Connections Medicaid.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="battery", title="Medicare Help in South Carolina [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for South Carolinians: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Greenville to Charleston and Myrtle Beach.",
    eyebrow="Medicare made clear · Statewide in South Carolina",
    h1="Medicare in South Carolina, explained by someone who actually teaches it.",
    sub="Turning 65, retiring, just moved to the coast, or re-shopping because your premium jumped? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in South Carolina &middot; SC License #18580338 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="South Carolina is different", different_h2="Three things about Medicare in South Carolina that the national websites gloss over",
    different_lede="South Carolina has 46 counties, about 1.25 million people on Medicare, a coast that fills with new retirees every year, and a Medigap rulebook with no second chances. Start with what actually applies where you live.",
    different_cards=[
        ("Your Medigap window does not come back", "South Carolina has no birthday rule and no annual switching window. The six-month open enrollment at 65, and a handful of guaranteed-issue events such as moving here from an Advantage plan&rsquo;s service area, are the only times a carrier must take you without health questions. Use them well.", "/medicare-supplement", "How Medigap works here"),
        ("Half the state moved here from somewhere else", "Bluffton, Hilton Head, Myrtle Beach, Mount Pleasant, Fort Mill: a lot of South Carolina&rsquo;s Medicare population arrived on Medicare. A move opens a Special Enrollment Period, changes your county&rsquo;s plan menu, and, if you left an Advantage plan behind, opens a Medigap window.", "/new-to-south-carolina", "Moving to South Carolina"),
        ("Healthy Connections Prime is gone", "South Carolina&rsquo;s Medicare-Medicaid plan for people 65 and over ended on December 31, 2025. People with both Medicare and Healthy Connections Medicaid now use Dual Special Needs Plans, and the Medicare Savings Programs that pay the Part B premium still run through SCDHHS.", "/medicaid", "Dual-eligible help"),
    ],
    options_h2="Four ways South Carolinians get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you live. These are the situations South Carolinians ask us about most.",
    situations=[
        ("New to South Carolina", "The relocation Special Enrollment Period, what happens to a Medigap policy from another state, and what a hurricane declaration does to your deadlines.", "/new-to-south-carolina", "Moving to South Carolina"),
        ("My premium went up", "Why Medigap rates rise, how South Carolina&rsquo;s rate filings are public, and what switching means in a state with no birthday rule.", "/medicare-supplement", "Medigap in South Carolina"),
        ("Veterans &amp; military retirees", "TRICARE For Life, the Charleston and Columbia VA systems, and why Part B timing still matters &mdash; from a retired Air Force officer.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Healthy Connections Medicaid", "The Medicare Savings Programs that pay your Part B premium, Extra Help, and the D-SNPs that replaced Healthy Connections Prime.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the South Carolina-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps South Carolina retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with South Carolinians by phone and video across all 46 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("Does South Carolina have a Medigap birthday rule?", "No. South Carolina follows the federal rules only: your six-month Medigap open enrollment when you are 65 and have Part B, plus guaranteed-issue events such as losing an Advantage plan through no fault of your own. Outside those, South Carolina insurers can use medical underwriting. That makes the first choice matter more here than in a birthday-rule state."),
        ("I just moved to South Carolina. What happens to my Medicare?", "Original Medicare comes with you unchanged. A Medicare Advantage or Part D plan is tied to your old county, so a permanent move gives you a Special Enrollment Period to pick a plan sold where you live now. If you leave an Advantage plan because you moved out of its service area, federal rules give you a guaranteed-issue right to buy certain Medigap plans without health questions, generally for 63 days. A Medigap policy from another state usually keeps working here; the premium may be re-rated."),
        ("When can I enroll in or change my Medicare plan in South Carolina?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving, losing a plan, qualifying for Medicaid, or a FEMA hurricane declaration opens a Special Enrollment Period."),
        ("I have VA or TRICARE benefits. Do I still need Medicare?", "Often, yes. VA health care and Medicare do not coordinate with each other, and TRICARE For Life requires you to have Medicare Parts A and B. Enrolling in Part B on time matters even with VA care, because VA medical coverage is not creditable for Part B and the late penalty lasts for life. Our Veterans page explains how these benefits fit together."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in South Carolina, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and I-CARE (800-868-9095) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your travel together.",
)

OG = dict(line1="Medicare help in", line2="South Carolina", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="ecosinsurancesolutions.com/south-carolina", mark="sun",
          palette=dict(primary=(31, 45, 92), dark=(20, 32, 74), gold=(201, 168, 74), paper=(246, 242, 233), sky=(223, 230, 240),
                       far=(207, 214, 200), mid=(157, 185, 138), green=(46, 107, 72)))

# Home-page photo band (served from <state>/img/, kept across rebuilds by tools/build_state.py)
HERO_PHOTO = {'src': '/img/hero-south-carolina-1600.webp', 'src_sm': '/img/hero-south-carolina-800.webp', 'alt': 'A couple strolling past the pastel houses of Rainbow Row in Charleston', 'pos': '50% 50%'}
