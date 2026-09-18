"""New Mexico site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 13)
# Mark: a high-desert sun over a mesa. (Deliberately not the Zia sun symbol, which belongs to Zia Pueblo.)
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#1f5e66"/>'
        '<circle cx="21" cy="16" r="7" fill="#deaa6e"/><path d="M6 30l7-9h16l7 9z" fill="#c68a5c"/><path d="M6 30h30v3H6z" fill="#8a9a76"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#1f5e66"/>'
           '<circle cx="21" cy="16" r="7" fill="#deaa6e"/><path d="M6 30l7-9h16l7 9z" fill="#c68a5c"/><path d="M6 30h30v3H6z" fill="#8a9a76"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.ecosinsurancesolutions.com/new-mexico", domain="ecosinsurancesolutions.com/new-mexico", name="New Mexico Medicare Enrollment",
    org="ECOS Medicare Solutions", state="New Mexico", abbr="NM", demonym="New Mexicans",
    # TODO(Darin): replace with the New Mexico (505 / 575) number once he provides it. The agency's main line is the placeholder.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # New Mexico producer licence (same digits as the NPN); the engine shows it beside Darin's name site-wide.
    state_license="18580338", state_license_label="NM License",
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
             ("North Carolina Medicare Enrollment", "https://www.ecosinsurancesolutions.com/north-carolina"),
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
          "Please contact Medicare.gov, 1-800-MEDICARE, or the New Mexico State Health Insurance Assistance Program (New Mexico SHIP, run by the Aging and Long-Term Services "
          "Department&rsquo;s Aging and Disability Resource Center, 800-432-2080) to get information on all of your options."),
    not_affiliated="the State of New Mexico, the New Mexico Health Care Authority, Turquoise Care (New Mexico Medicaid), the New Mexico Aging and Long-Term Services Department, the Indian Health Service, or the New Mexico Office of Superintendent of Insurance",
    ship_name="New Mexico SHIP", ship_phone="800-432-2080",
    brand_tag="Plain-English Medicare help in New Mexico", theme_color="#1f5e66",
    footer_tagline="Plain-English Medicare guidance for New Mexico retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping New Mexico retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Albuquerque and Santa Fe to Las Cruces, Farmington, Roswell and the villages in between.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and New Mexico Medicaid dual eligibility",
                 "Turquoise Care", "Medicare for military retirees", "Medicare in rural New Mexico", "Medicare and the Indian Health Service"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My plan is leaving (Presbyterian or another carrier)", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I live far from a hospital", "I have VA / TRICARE", "I have Medicaid (Turquoise Care) too", "I use IHS or a tribal clinic"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. A plan leaving your county opens a Special Enrollment Period, and from January 1, 2027, New Mexico adds a 60-day Medigap birthday window.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across New Mexico',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/rural-new-mexico">Medicare in rural New Mexico</a> &mdash; distance, networks and the IHS', '<a href="/medicaid">Turquoise Care, Medicare Savings Programs and Extra Help</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="sandia", h1="New Mexico Medicare questions, answered plainly",
                  sub="The questions we hear most from New Mexicans &mdash; about Presbyterian leaving Medicare Advantage, the 2027 birthday rule, Medigap under 65, Turquoise Care, the IHS, the VA, long drives to a specialist, and what any of this costs. Short answers, with links to the longer ones.",
                  title="New Mexico Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions New Mexicans ask most: Presbyterian's 2027 Advantage exit, the new Medigap birthday rule, under-65 Medigap, Turquoise Care, IHS, the VA, rural networks and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for New Mexico retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from Albuquerque, Rio Rancho and Santa Fe to Las Cruces, Farmington, Roswell, Clovis, Gallup and the mountain and plains counties between.",
    llm_facts=["Darin Weidauer holds New Mexico insurance license #18580338 (NPN 18580338).",
               "New Mexico uses the federal Medigap plan letters (A–N); the Office of Superintendent of Insurance (OSI) regulates Medigap and verifies producer licences. New Mexico does not require insurers to sell Medigap to people under 65 on Medicare; the New Mexico Medical Insurance Pool (NMMIP) offers a Medicare Carve-Out Plan to under-65 disabled beneficiaries with Parts A and B.",
               "Senate Bill 21 (2026) gives New Mexico a Medigap birthday rule effective January 1, 2027: a 60-day window starting on the first day of the policyholder's birthday month to switch to a Medigap plan of equal or lesser benefits without medical underwriting.",
               "Roughly 470,000 New Mexicans have Medicare and, as of January 2026, about half were in Medicare Advantage. Presbyterian Health Plan announced in June 2026 that it will discontinue most of its Medicare Advantage plans for 2027 (about 30,000 members), keeping its Dual Plus D-SNP; affected members choose new coverage during the October 15–December 7, 2026 Annual Election Period.",
               "New Mexico's SHIP is run by the Aging and Long-Term Services Department's Aging and Disability Resource Center: 800-432-2080.",
               "New Mexico Medicaid is Turquoise Care, run by the New Mexico Health Care Authority (HCA) since July 1, 2024 (it replaced Centennial Care); members choose among four health plans: Blue Cross and Blue Shield of New Mexico, Presbyterian Health Plan, Molina Healthcare and UnitedHealthcare Community Plan. Medicare Savings Programs (QMB, SLMB, QI) are administered by HCA; New Mexico eliminated the asset test for them effective January 1, 2021, and qualifying confers Part D Extra Help automatically.",
               "About 130,000 veterans live in New Mexico. VA New Mexico Health Care System runs the Raymond G. Murphy VA Medical Center in Albuquerque and 13 community clinics; military-retiree communities surround Kirtland AFB (Albuquerque), Holloman AFB (Alamogordo), Cannon AFB (Clovis) and White Sands Missile Range (Las Cruces).",
               "The Indian Health Service is not health insurance and its Purchased/Referred Care program is the payer of last resort, so IHS encourages eligible tribal members to enroll in Medicare; Medicare pays IHS and tribal facilities for covered care."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/rural-new-mexico", "Rural NM"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in New Mexico</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/rural-new-mexico">Rural New Mexico &amp; the IHS</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Turquoise Care &amp; Medicare Savings Programs</a>',
                   '<a href="/faq">Questions New Mexicans ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://aging.nm.gov/services/aging-disability-resource-center-adrc/medicare/ship" rel="noopener">New Mexico SHIP (ALTSD)</a>, 800-432-2080',
                                    '<a href="https://www.osi.state.nm.us" rel="noopener">Office of Superintendent of Insurance</a>',
                                    '<a href="https://www.hca.nm.gov" rel="noopener">NM Health Care Authority (Turquoise Care)</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a local network &mdash; so your hospital system, your county and your prescriptions matter, and so does whether the carrier will still be here next year.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; UNM, Christus St. Vincent, a specialist in El Paso or Denver, or the clinic in your county seat.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Turquoise Care (New Mexico Medicaid).", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="sandia", title="Medicare Help in New Mexico [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for New Mexicans: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Albuquerque to Las Cruces and Farmington to Hobbs.",
    eyebrow="Medicare made clear · Statewide in New Mexico",
    h1="Medicare in New Mexico, explained by someone who actually teaches it.",
    sub="Turning 65, retiring, or re-shopping because Presbyterian is leaving Medicare Advantage? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in New Mexico &middot; NM License #18580338 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="New Mexico is different", different_h2="Three things about Medicare in New Mexico that the national websites gloss over",
    different_lede="New Mexico has 33 counties, about half its Medicare population in Advantage plans, one home-grown carrier walking away from most of that business for 2027, and distances that turn a &ldquo;network&rdquo; into a three-hour drive. Start with what is actually for sale where you live.",
    different_cards=[
        ("Presbyterian is leaving Medicare Advantage", "In June 2026 Presbyterian Health Plan announced it will discontinue most of its Medicare Advantage plans for 2027 &mdash; about 30,000 members &mdash; keeping only its Dual Plus plan for people who also have Medicaid. Coverage runs through December 31; the switch happens in this fall&rsquo;s Annual Election Period, and a non-renewal opens a guaranteed-issue path to Medigap.", "/medicare-advantage", "What a non-renewal notice gives you"),
        ("Distance is part of the plan", "Several New Mexico counties have no hospital at all, and most rural ones have a 25-bed Critical Access Hospital and a long road to Albuquerque, Las Cruces, El Paso or Lubbock for anything more. An Advantage network that looks fine on paper can mean a referral three hours away; a Medigap policy has no network to check.", "/rural-new-mexico", "Medicare in rural New Mexico"),
        ("A birthday rule arrives in 2027", "Senate Bill 21 gives New Mexicans on Medigap a 60-day window each year, starting the first day of their birthday month, to move to a plan of equal or lesser benefits without health questions &mdash; from January 1, 2027. Until then, the six-month window at 65 is the one that counts, and New Mexico does not require Medigap to be sold under 65.", "/medicare-supplement", "How Medigap works here"),
    ],
    options_h2="Four ways New Mexicans get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and how far you are willing to drive. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you live. These are the situations New Mexicans ask us about most.",
    situations=[
        ("Rural New Mexico &amp; the IHS", "Which plans work when the nearest hospital is an hour away, when your care runs through an IHS or tribal facility, or when your specialist is in El Paso or Denver.", "/rural-new-mexico", "Medicare at a distance"),
        ("My plan is leaving", "Presbyterian&rsquo;s 2027 exit is the big one, but carriers also drop counties each year. What a discontinuation notice gives you, and the deadline that comes with it.", "/medicare-advantage", "What to do next"),
        ("Veterans &amp; military retirees", "TRICARE For Life, the Raymond G. Murphy VA and its community clinics, Kirtland, Holloman, Cannon and White Sands &mdash; and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Turquoise Care", "New Mexico Medicaid, the Medicare Savings Programs that pay your Part B premium with no asset test, and Dual Special Needs Plans that coordinate both.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the New Mexico-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps New Mexico retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with New Mexicans by phone and video across all 33 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("Presbyterian is ending my Medicare Advantage plan. What do I do?", "Your coverage continues through December 31, 2026. Presbyterian announced in June 2026 that it will discontinue most of its Advantage plans for 2027, keeping only its Dual Plus plan for people who also have Medicaid. You choose new coverage during the Annual Election Period, October 15 to December 7, and because the plan is leaving you involuntarily you generally also get a guaranteed-issue right to buy a Medigap policy without health questions, for a limited time around the date the coverage ends. Call before the deadline on your notice."),
        ("When can I enroll in or change my Medicare plan in New Mexico?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving counties, losing a plan, or qualifying for Medicaid opens a Special Enrollment Period. From January 1, 2027, people already on Medigap also get a 60-day birthday window each year."),
        ("Does a Medicare Advantage plan cover me at UNM, Presbyterian or Christus St. Vincent?", "Only if that hospital and your doctors are in the plan&rsquo;s network, which is set by the plan and changes yearly. With Original Medicare and a Medigap policy there is no network: any hospital in New Mexico &mdash; or in El Paso, Lubbock or Denver &mdash; that accepts Medicare is covered. We confirm your providers in writing before you enroll."),
        ("I have VA or TRICARE benefits, or I use an IHS clinic. Do I still need Medicare?", "Usually, yes. VA health care and Medicare do not coordinate with each other, TRICARE For Life requires Medicare Parts A and B, and the Indian Health Service is not insurance &mdash; it is the payer of last resort and encourages eligible members to enroll in Medicare. Enrolling in Part B on time matters in all three cases, because the late penalty lasts for life. Our Veterans and Rural New Mexico pages explain how each fits."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in New Mexico, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and New Mexico SHIP (800-432-2080) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and how far you drive, together.",
)

OG = dict(line1="Medicare help in", line2="New Mexico", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="ecosinsurancesolutions.com/new-mexico", mark="sun",
          palette=dict(primary=(31, 94, 102), dark=(20, 63, 69), gold=(222, 170, 110), paper=(246, 239, 228), sky=(232, 217, 198),
                       far=(201, 184, 163), mid=(138, 154, 118), green=(107, 125, 90)))

# Home-page photo band (served from <state>/img/, kept across rebuilds by tools/build_state.py)
HERO_PHOTO = {'src': '/img/hero-new-mexico-1600.webp', 'src_sm': '/img/hero-new-mexico-800.webp', 'alt': 'A couple watching hot-air balloons lift off at dawn at the Albuquerque Balloon Fiesta, with the Sandia Mountains behind', 'pos': '50% 45%'}

# Place-page hero photos (city, base and region pages): /img/<slug>-<w>.webp, placed by hand.
PLACE_PHOTOS = {'albuquerque-metro': {'src': '/img/albuquerque-metro-1600.webp', 'src_sm': '/img/albuquerque-metro-800.webp', 'alt': 'A retired couple ride the Sandia Peak aerial tramway car with Albuquerque spread out far below', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'santa-fe-north-central': {'src': '/img/santa-fe-north-central-1600.webp', 'src_sm': '/img/santa-fe-north-central-800.webp', 'alt': 'A retired couple walk the adobe Santa Fe Plaza beneath the wooden portal of the Palace of the Governors', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'northwest-four-corners': {'src': '/img/northwest-four-corners-1600.webp', 'src_sm': '/img/northwest-four-corners-800.webp', 'alt': 'A retired couple stand in the desert with the great volcanic spire of Shiprock rising behind', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'northeast-high-plains': {'src': '/img/northeast-high-plains-1600.webp', 'src_sm': '/img/northeast-high-plains-800.webp', 'alt': 'A retired couple walk high plains grassland with the Sangre de Cristo mountains on the horizon', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'las-cruces-southwest': {'src': '/img/las-cruces-southwest-1600.webp', 'src_sm': '/img/las-cruces-southwest-800.webp', 'alt': 'A retired couple walk a pecan orchard with the jagged Organ Mountains behind', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'southeast-permian': {'src': '/img/southeast-permian-1600.webp', 'src_sm': '/img/southeast-permian-800.webp', 'alt': 'A retired couple walk the Pecos River path in Carlsbad with cottonwoods', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'east-clovis-portales': {'src': '/img/east-clovis-portales-1600.webp', 'src_sm': '/img/east-clovis-portales-800.webp', 'alt': 'A retired couple walk a prairie road with a windmill and a huge sky on the eastern plains', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'central-mountains': {'src': '/img/central-mountains-1600.webp', 'src_sm': '/img/central-mountains-800.webp', 'alt': 'A retired couple walk the white gypsum dunes of White Sands at sunset', 'pos': '50% 50%', 'w': 1600, 'h': 1073}, 'albuquerque': {'src': '/img/albuquerque-1200.webp', 'src_sm': '/img/albuquerque-800.webp', 'alt': 'A retired couple walk the Old Town plaza in Albuquerque with the adobe San Felipe church', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'rio-rancho': {'src': '/img/rio-rancho-1200.webp', 'src_sm': '/img/rio-rancho-800.webp', 'alt': 'A retired couple walk a mesa trail above the Rio Grande bosque with the Sandia Mountains', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'los-lunas': {'src': '/img/los-lunas-1200.webp', 'src_sm': '/img/los-lunas-800.webp', 'alt': 'A retired couple walk among golden cottonwoods in the Rio Grande bosque', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'santa-fe': {'src': '/img/santa-fe-1200.webp', 'src_sm': '/img/santa-fe-800.webp', 'alt': 'A retired couple walk Canyon Road past adobe galleries hung with red chile ristras', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'roswell': {'src': '/img/roswell-1200.webp', 'src_sm': '/img/roswell-800.webp', 'alt': 'A retired couple walk the red bluffs and blue lakes of Bottomless Lakes State Park', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'farmington': {'src': '/img/farmington-1200.webp', 'src_sm': '/img/farmington-800.webp', 'alt': 'A retired couple walk the Animas River trail with cottonwoods and sandstone bluffs', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'clovis': {'src': '/img/clovis-1200.webp', 'src_sm': '/img/clovis-800.webp', 'alt': 'A retired couple walk a wide prairie with grain elevators and a windmill', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'hobbs': {'src': '/img/hobbs-1200.webp', 'src_sm': '/img/hobbs-800.webp', 'alt': 'A retired couple walk a prairie at sunset with pumpjacks far off', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'alamogordo': {'src': '/img/alamogordo-1200.webp', 'src_sm': '/img/alamogordo-800.webp', 'alt': 'A retired couple walk the white dunes of White Sands', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'las-cruces': {'src': '/img/las-cruces-1200.webp', 'src_sm': '/img/las-cruces-800.webp', 'alt': 'A retired couple walk the plaza of Old Mesilla with the twin-towered basilica', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'carlsbad': {'src': '/img/carlsbad-1200.webp', 'src_sm': '/img/carlsbad-800.webp', 'alt': 'A retired couple walk the Pecos River flume walk in Carlsbad', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'gallup': {'src': '/img/gallup-1200.webp', 'src_sm': '/img/gallup-800.webp', 'alt': 'A retired couple walk beneath the red sandstone cliffs of Red Rock Park near Gallup', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'deming': {'src': '/img/deming-1200.webp', 'src_sm': '/img/deming-800.webp', 'alt': 'A retired couple walk Rockhound State Park with the Florida Mountains behind', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'los-alamos': {'src': '/img/los-alamos-1200.webp', 'src_sm': '/img/los-alamos-800.webp', 'alt': 'A retired couple stand beneath the cliff dwellings and wooden ladders of Bandelier', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'silver-city': {'src': '/img/silver-city-1200.webp', 'src_sm': '/img/silver-city-800.webp', 'alt': 'A retired couple walk the trail beneath the Gila cliff dwellings', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'taos': {'src': '/img/taos-1200.webp', 'src_sm': '/img/taos-800.webp', 'alt': 'A retired couple stand before the multistory adobe buildings of Taos Pueblo', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'ruidoso': {'src': '/img/ruidoso-1200.webp', 'src_sm': '/img/ruidoso-800.webp', 'alt': 'A retired couple walk a pine trail near Ruidoso with Sierra Blanca behind', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'artesia': {'src': '/img/artesia-1200.webp', 'src_sm': '/img/artesia-800.webp', 'alt': 'A retired couple walk a small-town main street in Artesia with bronze sculptures, storefront lettering blank', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'kirtland-afb': {'src': '/img/kirtland-afb-1200.webp', 'src_sm': '/img/kirtland-afb-800.webp', 'alt': 'A retired couple walk a Sandia foothills trail with Albuquerque below', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'holloman-afb': {'src': '/img/holloman-afb-1200.webp', 'src_sm': '/img/holloman-afb-800.webp', 'alt': 'A retired couple walk a pistachio orchard near Alamogordo with the Sacramento Mountains behind', 'pos': '50% 50%', 'w': 1200, 'h': 800}, 'cannon-afb': {'src': '/img/cannon-afb-1200.webp', 'src_sm': '/img/cannon-afb-800.webp', 'alt': 'A retired couple walk a prairie trail near Clovis with a windmill and grain elevators far off', 'pos': '50% 50%', 'w': 1200, 'h': 800}}
