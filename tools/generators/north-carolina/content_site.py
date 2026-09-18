"""North Carolina site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 13)
# Logo: a longleaf pine silhouette on a Carolina-blue-deepened disc, sea-oat gold.
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#1f4e79"/>'
        '<rect x="19.5" y="20" width="3" height="14" fill="#e9c46a"/><path d="M11 21c3-8 8-11 10-10 2-1 7 2 10 10-4-2-7-1-10 1-3-2-6-3-10-1z" fill="#e9c46a"/>'
        '<path d="M14 14c2-5 5-7 7-6 2-1 5 1 7 6-2-1-4-1-7 1-3-2-5-2-7-1z" fill="#e9c46a"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#1f4e79"/>'
           '<rect x="19.5" y="20" width="3" height="14" fill="#e9c46a"/><path d="M11 21c3-8 8-11 10-10 2-1 7 2 10 10-4-2-7-1-10 1-3-2-6-3-10-1z" fill="#e9c46a"/>'
           '<path d="M14 14c2-5 5-7 7-6 2-1 5 1 7 6-2-1-4-1-7 1-3-2-5-2-7-1z" fill="#e9c46a"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.ecosinsurancesolutions.com/north-carolina", domain="ecosinsurancesolutions.com/north-carolina", name="North Carolina Medicare Enrollment",
    org="ECOS Medicare Solutions", state="North Carolina", abbr="NC", demonym="North Carolinians",
    # TODO(Darin): replace with the North Carolina (704 / 919 / 336 / 910 / 828) number once he provides it. Main line as placeholder.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # North Carolina producer licence (same digits as the NPN); the engine renders it beside the NPN site-wide.
    state_license="18580338", state_license_label="NC License",
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
             ("Ohio Medicare Enrollment", "https://www.ecosinsurancesolutions.com/ohio"),
             ("South Carolina Medicare Enrollment", "https://www.ecosinsurancesolutions.com/south-carolina"),
             ("Tennessee Medicare Quotes", "https://www.ecosinsurancesolutions.com/tennessee"),
             ("Texas Medicare Enrollment", "https://www.ecosinsurancesolutions.com/texas"),
             ("Medicare Enrollment Utah", "https://www.ecosinsurancesolutions.com/utah"),
             ("Washington Medicare Enrollment", "https://www.ecosinsurancesolutions.com/washington"),
             ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"),
             ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")],
    sameas_org_extra=["https://howdoiapplyformedicare.com", "https://medicareadvantageanswers.com", "https://dentalinsurancetomorrow.com"],
    sameas_darin=["https://www.myecos360.com/darin-weidauer", "https://www.linkedin.com/in/darin-weidauer-3165a816b/", "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
                  "https://www.ecosinsurancesolutions.com/arizona/about", "https://www.ecosinsurancesolutions.com/california/about", "https://www.ecosinsurancesolutions.com/florida/about",
                  "https://www.ecosinsurancesolutions.com/minnesota/about", "https://www.ecosinsurancesolutions.com/texas/about", "https://www.ecosinsurancesolutions.com/utah/about",
                  "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or the North Carolina Seniors&rsquo; Health Insurance Information Program (SHIIP, North Carolina&rsquo;s State Health "
          "Insurance Assistance Program, 855-408-1212) to get information on all of your options."),
    not_affiliated="the State of North Carolina, the North Carolina Department of Health and Human Services, NC Medicaid, or the North Carolina Department of Insurance",
    ship_name="NC SHIIP", ship_phone="855-408-1212",
    brand_tag="Plain-English Medicare help in North Carolina", theme_color="#1f4e79",
    footer_tagline="Plain-English Medicare guidance for North Carolina retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping North Carolina retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Charlotte and the Triangle to the mountains and the Outer Banks.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and NC Medicaid dual eligibility",
                 "Medicare Savings Programs (MQB)", "Medicare for military retirees", "Moving to North Carolina on Medicare"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My hospital left my plan's network", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I'm moving to North Carolina", "I have VA / TRICARE", "I have Medicaid too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Moving into North Carolina, or a plan leaving your county, opens a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across North Carolina',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/moving-to-north-carolina">Moving to North Carolina</a> &mdash; the relocation Special Enrollment Period',
                    '<a href="/medicaid">NC Medicaid, the MQB programs and Extra Help</a>', '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="blueridge", h1="North Carolina Medicare questions, answered plainly",
                  sub="The questions we hear most from North Carolinians &mdash; about hospitals leaving Advantage networks, Medigap underwriting, the State Health Plan, moving here from up north, TRICARE at Fort Bragg and Camp Lejeune, and what any of this costs. Short answers, with links to the longer ones.",
                  title="North Carolina Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions North Carolinians ask most: hospital systems leaving Advantage networks, Medigap rules and under-65 rights, MQB programs, moving to NC, TRICARE and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for North Carolina retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from Charlotte, the Triangle and the Triad to Asheville, Wilmington, the Sandhills and the Outer Banks.",
    llm_facts=["Darin Weidauer holds North Carolina insurance license #18580338 (NPN 18580338), verifiable through the North Carolina Department of Insurance licensee lookup or the NIPR.",
               "North Carolina uses the federal Medigap plan letters (A-N) and has no birthday or anniversary switching rule; the North Carolina Department of Insurance regulates Medigap. Under G.S. 58-54-45, people under 65 on Medicare because of a disability can buy Plan A, D or G during a six-month window that starts when Part B begins.",
               "Roughly 2.3 million North Carolinians have Medicare and about 1.33 million of them, close to 58 percent, are in Medicare Advantage plans as of January 2026 (KFF). Effective January 1, 2026, UNC Health is out of network with Humana, WellCare and HCSC (formerly Cigna) Medicare Advantage plans, and CarolinaEast Medical Center in New Bern left Blue Cross NC's Medicare Advantage network on July 1, 2026.",
               "North Carolina's SHIP is the Seniors' Health Insurance Information Program (SHIIP), a division of the North Carolina Department of Insurance, with volunteer counselors in all 100 counties: 855-408-1212.",
               "NC Medicaid is administered by the North Carolina Department of Health and Human Services. Adults 65 and over who qualify are generally served through NC Medicaid Direct rather than the managed-care Standard Plans; Tailored Plans (launched July 1, 2024) serve people with significant behavioral-health, I/DD or TBI needs. Apply through ePASS or the county Department of Social Services; NC Medicaid Contact Center 888-245-0179. Medicaid expansion for adults 19-64 began December 1, 2023.",
               "North Carolina's Medicare Savings Programs are labelled MQB: MQB-Q (the federal QMB), MQB-B (SLMB) and MQB-E (QI). County DSS offices decide eligibility, and qualifying automatically brings Part D Extra Help.",
               "North Carolina has more than 615,000 veterans, the eighth-largest veteran population in the country, with VA medical centers in Durham, Fayetteville, Salisbury and Asheville, and large military-retiree communities around Fort Bragg (Fayetteville), Camp Lejeune (Jacksonville) and Seymour Johnson AFB (Goldsboro).",
               "Moving into North Carolina on Medicare opens a Special Enrollment Period for Medicare Advantage and Part D; a FEMA-declared disaster (as after Hurricane Helene in 25 western counties in 2024) opens another."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/moving-to-north-carolina", "Moving here"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in North Carolina</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/moving-to-north-carolina">Moving to North Carolina</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">NC Medicaid &amp; the MQB programs</a>',
                   '<a href="/faq">Questions North Carolinians ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://www.ncdoi.gov/consumers/medicare-and-seniors-health-insurance-information-program-shiip" rel="noopener">NC SHIIP</a>, 855-408-1212',
                                    '<a href="https://www.ncdoi.gov" rel="noopener">North Carolina Department of Insurance</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a local network &mdash; so which hospital system you use, your county and your prescriptions matter.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; Duke, UNC, Atrium, Mayo, or the clinic in your county seat.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and NC Medicaid.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="blueridge", title="Medicare Help in North Carolina [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for North Carolinians: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Charlotte to the Outer Banks.",
    eyebrow="Medicare made clear · Statewide in North Carolina",
    h1="Medicare in North Carolina, explained by someone who actually teaches it.",
    sub="Turning 65, retiring, moving here from up north, or re-shopping because your hospital left your plan&rsquo;s network? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in North Carolina &middot; NC License #18580338 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="North Carolina is different", different_h2="Three things about Medicare in North Carolina that the national websites gloss over",
    different_lede="North Carolina has 100 counties, close to six in ten of its Medicare beneficiaries in Advantage plans, and a care map drawn by a handful of big systems &mdash; Atrium, Novant, Duke, UNC, WakeMed, Cone, ECU Health, Mission &mdash; that each sign their own contracts. Start with which one your doctors belong to.",
    different_cards=[
        ("Your hospital system decides your menu", "For 2026 UNC Health is out of network with Humana, WellCare and HCSC (formerly Cigna) Advantage plans, and CarolinaEast in New Bern left Blue Cross NC&rsquo;s Advantage network on July 1. A system leaving your plan is not the same as a plan leaving your county, and the rights that follow are different.", "/medicare-advantage", "What a network change gives you"),
        ("Medigap has one window, and an under-65 rule", "North Carolina has no birthday rule. Your six-month Medigap open enrollment at 65 is the guaranteed window; after that, underwriting. Under 65 on disability? State law guarantees Plan A, D or G for six months after Part B starts.", "/medicare-supplement", "The Medigap rules here"),
        ("Half a million military families", "Fort Bragg, Camp Lejeune, Seymour Johnson and four VA medical centers make North Carolina the eighth-largest veteran state. TRICARE For Life and VA care each work with Medicare differently, and the Part B timing mistake is expensive and permanent.", "/veterans", "Veterans &amp; Medicare"),
    ],
    options_h2="Four ways North Carolinians get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you have come from. These are the situations North Carolinians ask us about most.",
    situations=[
        ("Moving to North Carolina", "Retiring to Pinehurst, Brunswick County, the Triangle or the mountains from another state: the relocation Special Enrollment Period, what happens to a Medigap policy, and the hurricane rule on the coast.", "/moving-to-north-carolina", "Medicare when you move here"),
        ("My hospital left my plan", "UNC Health, CarolinaEast and others have left Advantage networks. What a network change gives you, what it does not, and the deadline that comes with it.", "/medicare-advantage", "What to do next"),
        ("Veterans &amp; military retirees", "TRICARE For Life at Fort Bragg and Camp Lejeune, the Durham, Fayetteville, Salisbury and Asheville VAs &mdash; and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + NC Medicaid", "NC Medicaid Direct, the MQB programs that pay your Part B premium, Extra Help, PACE, and Dual Special Needs Plans that coordinate both.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the North Carolina-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer (NC License #18580338) is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps North Carolina retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with North Carolinians by phone and video across all 100 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("My hospital says it is leaving my Medicare Advantage plan&rsquo;s network. What do I do?", "First, check whether it is the hospital leaving the network or the plan leaving your county &mdash; they are different. For 2026 UNC Health left Humana, WellCare and HCSC (Cigna) Advantage networks, and CarolinaEast left Blue Cross NC&rsquo;s on July 1. A network change alone does not usually create a guaranteed-issue right to Medigap, but the Annual Election Period (October 15 to December 7) and, for current Advantage members, the January 1 to March 31 open enrollment let you move to a plan your hospital accepts, or back to Original Medicare. Call before the deadline."),
        ("When can I enroll in or change my Medicare plan in North Carolina?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving into the state or between counties, losing a plan, qualifying for Medicaid, or a FEMA-declared disaster opens a Special Enrollment Period."),
        ("Does North Carolina have a Medigap birthday rule?", "No. Your six-month Medigap open enrollment, which starts when you are 65 and enrolled in Part B, is the guaranteed window, along with federal guaranteed-issue events such as your Advantage plan leaving your county. Outside those, North Carolina insurers can use medical underwriting. If you are under 65 on Medicare because of a disability, state law guarantees you Plan A, D or G for six months after Part B begins."),
        ("I have VA or TRICARE benefits. Do I still need Medicare?", "Often, yes. VA health care and Medicare do not coordinate with each other, and TRICARE For Life requires you to have Medicare Parts A and B. Enrolling in Part B on time matters even with VA care, because VA medical coverage is not creditable for Part B and the late penalty lasts for life. Our Veterans page explains how these benefits fit together at Fort Bragg, Camp Lejeune and the four North Carolina VAs."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in North Carolina, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and NC SHIIP (855-408-1212) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your travel together.",
)

OG = dict(line1="Medicare help in", line2="North Carolina", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="ecosinsurancesolutions.com", mark="pine",
          palette=dict(primary=(31, 78, 121), dark=(20, 54, 89), gold=(233, 196, 106), paper=(246, 242, 233), sky=(207, 227, 243),
                       far=(169, 198, 222), mid=(110, 155, 192), green=(62, 107, 58)))

# Home-page photo band (served from <state>/img/, kept across rebuilds by tools/build_state.py)
HERO_PHOTO = {'src': '/img/hero-north-carolina-1600.webp', 'src_sm': '/img/hero-north-carolina-800.webp', 'alt': 'A couple walking the beach at Cape Hatteras, with the black-and-white striped lighthouse behind the dunes', 'pos': '50% 55%'}

# Place-page hero photos (city, base and region pages): /img/<slug>-<w>.webp, placed by hand.
PLACE_PHOTOS = {'charlotte-metro': {'src': '/img/charlotte-metro-1600.webp', 'src_sm': '/img/charlotte-metro-800.webp', 'alt': 'A retired couple walk Freedom Park with the uptown Charlotte skyline', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'triangle': {'src': '/img/triangle-1600.webp', 'src_sm': '/img/triangle-800.webp', 'alt': 'A retired couple walk the oak-shaded grounds of the State Capitol in Raleigh', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'triad': {'src': '/img/triad-1600.webp', 'src_sm': '/img/triad-800.webp', 'alt': 'A retired couple walk the brick sidewalks of Old Salem past historic Moravian buildings', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'western-nc-mountains': {'src': '/img/western-nc-mountains-1600.webp', 'src_sm': '/img/western-nc-mountains-800.webp', 'alt': 'A retired couple stand at a Blue Ridge Parkway overlook with layered blue ridges', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'sandhills-fayetteville': {'src': '/img/sandhills-fayetteville-1600.webp', 'src_sm': '/img/sandhills-fayetteville-800.webp', 'alt': 'A retired couple walk a path through longleaf pines beside a manicured golf course', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'eastern-nc-coastal-plain': {'src': '/img/eastern-nc-coastal-plain-1600.webp', 'src_sm': '/img/eastern-nc-coastal-plain-800.webp', 'alt': 'A retired couple walk the Neuse riverfront with cypress trees', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'wilmington-cape-fear': {'src': '/img/wilmington-cape-fear-1600.webp', 'src_sm': '/img/wilmington-cape-fear-800.webp', 'alt': 'A retired couple walk the Wilmington Riverwalk with a grey battleship across the river', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'outer-banks-northeast': {'src': '/img/outer-banks-northeast-1200.webp', 'src_sm': '/img/outer-banks-northeast-800.webp', 'alt': 'A retired couple walk a marsh boardwalk toward the black-and-white banded Bodie Island lighthouse', 'pos': '50% 50%', 'w': 1200, 'h': 805}, 'foothills': {'src': '/img/foothills-1600.webp', 'src_sm': '/img/foothills-800.webp', 'alt': 'A retired couple stand at Pilot Mountain with its rounded knob rising from the forest', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'charlotte': {'src': '/img/charlotte-1200.webp', 'src_sm': '/img/charlotte-800.webp', 'alt': 'A retired couple walk Romare Bearden Park with the uptown skyline', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'raleigh': {'src': '/img/raleigh-1200.webp', 'src_sm': '/img/raleigh-800.webp', 'alt': 'A retired couple walk the State Capitol grounds under old oaks', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'greensboro': {'src': '/img/greensboro-1200.webp', 'src_sm': '/img/greensboro-800.webp', 'alt': 'A retired couple walk the Greensboro Arboretum in spring bloom', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'durham': {'src': '/img/durham-1200.webp', 'src_sm': '/img/durham-800.webp', 'alt': 'A retired couple walk the brick warehouses of the American Tobacco Campus with the water tower', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'winston-salem': {'src': '/img/winston-salem-1200.webp', 'src_sm': '/img/winston-salem-800.webp', 'alt': 'A retired couple walk Old Salem past brick Moravian buildings', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'fayetteville': {'src': '/img/fayetteville-1200.webp', 'src_sm': '/img/fayetteville-800.webp', 'alt': 'A retired couple walk the square beneath the domed Market House in Fayetteville', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'cary': {'src': '/img/cary-1200.webp', 'src_sm': '/img/cary-800.webp', 'alt': 'A retired couple walk the lake boardwalk at Bond Park', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'wilmington': {'src': '/img/wilmington-1200.webp', 'src_sm': '/img/wilmington-800.webp', 'alt': 'A retired couple walk the Wilmington Riverwalk along the Cape Fear River', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'high-point': {'src': '/img/high-point-1200.webp', 'src_sm': '/img/high-point-800.webp', 'alt': 'A retired couple walk the city lake park in High Point', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'concord': {'src': '/img/concord-1200.webp', 'src_sm': '/img/concord-800.webp', 'alt': 'A retired couple walk a historic downtown street in Concord with brick storefronts, signs blank', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'asheville': {'src': '/img/asheville-1200.webp', 'src_sm': '/img/asheville-800.webp', 'alt': 'A retired couple stand at a mountain overlook above Asheville with blue ridges', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'greenville': {'src': '/img/greenville-1200.webp', 'src_sm': '/img/greenville-800.webp', 'alt': 'A retired couple walk the Town Common along the Tar River', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'gastonia': {'src': '/img/gastonia-1200.webp', 'src_sm': '/img/gastonia-800.webp', 'alt': 'A retired couple walk a trail at Crowders Mountain with the rocky summit', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'jacksonville': {'src': '/img/jacksonville-1200.webp', 'src_sm': '/img/jacksonville-800.webp', 'alt': 'A retired couple walk the New River waterfront in Jacksonville', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'chapel-hill': {'src': '/img/chapel-hill-1200.webp', 'src_sm': '/img/chapel-hill-800.webp', 'alt': 'A retired couple walk the brick paths past the Old Well with azaleas in bloom', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'hickory': {'src': '/img/hickory-1200.webp', 'src_sm': '/img/hickory-800.webp', 'alt': 'A retired couple walk a park in Hickory with the Blue Ridge foothills', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'pinehurst-southern-pines': {'src': '/img/pinehurst-southern-pines-1200.webp', 'src_sm': '/img/pinehurst-southern-pines-800.webp', 'alt': 'A retired couple walk a manicured golf fairway among longleaf pines in Pinehurst', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'new-bern': {'src': '/img/new-bern-1200.webp', 'src_sm': '/img/new-bern-800.webp', 'alt': 'A retired couple walk the formal gardens of Tryon Palace', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'mooresville': {'src': '/img/mooresville-1200.webp', 'src_sm': '/img/mooresville-800.webp', 'alt': 'A retired couple walk the shore of Lake Norman with sailboats', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'boone': {'src': '/img/boone-1200.webp', 'src_sm': '/img/boone-800.webp', 'alt': 'A retired couple cross the Mile High Swinging Bridge at Grandfather Mountain', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'fort-bragg': {'src': '/img/fort-bragg-1200.webp', 'src_sm': '/img/fort-bragg-800.webp', 'alt': 'A retired couple walk the Cape Fear River trail in Fayetteville', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'camp-lejeune': {'src': '/img/camp-lejeune-1200.webp', 'src_sm': '/img/camp-lejeune-800.webp', 'alt': 'A retired couple walk the beach at Topsail Island with a wooden pier', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'seymour-johnson-afb': {'src': '/img/seymour-johnson-afb-1200.webp', 'src_sm': '/img/seymour-johnson-afb-800.webp', 'alt': 'A retired couple walk the Cliffs of the Neuse with the river far below', 'pos': '50% 50%', 'w': 1200, 'h': 800}}
