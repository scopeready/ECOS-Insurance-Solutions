"""Utah site identity, home page, navigation."""
from datetime import date
TODAY = date(2026, 9, 4)
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#24466b"/>'
        '<path d="M9 32V22a12 12 0 0 1 24 0v10h-6V23a6 6 0 0 0-12 0v9z" fill="#e7c486"/><path d="M6 34h30" stroke="#b8522e" stroke-width="3" stroke-linecap="round"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#24466b"/>'
           '<path d="M9 32V22a12 12 0 0 1 24 0v10h-6V23a6 6 0 0 0-12 0v9z" fill="#e7c486"/><path d="M6 34h30" stroke="#b8522e" stroke-width="3" stroke-linecap="round"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://medicareenrollmentutah.com", domain="medicareenrollmentutah.com", name="Medicare Enrollment Utah",
    org="ECOS Medicare Solutions", state="Utah", abbr="UT", demonym="Utahns",
    # TODO(Darin): swap for a Utah (801 / 385 / 435) number.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # Utah requires... the producer licence number is shown beside Darin's name site-wide via the engine.
    state_license="713009", state_license_label="UT License",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Medicare Enrollment Arizona", "https://www.medicareenrollmentarizona.com"), ("Medicare Enrollment Nevada", "https://medicareenrollmentnevada.com"),
             ("Colorado Medicare Enrollment", "https://coloradomedicareenrollment.com"), ("Texas Medicare Enrollment", "https://texasmedicareenrollment.com"),
             ("Georgia Medicare Enrollment", "https://georgiamedicareenrollment.com"), ("Minnesota Medicare Enrollment", "https://minnesotamedicareenrollment.com"),
             ("Tennessee Medicare Quotes", "https://www.tennesseemedicarequotes.com"), ("Medicare Enrollment Florida", "https://medicareenrollmentflorida.com"), ("California Medicare Enrollment", "https://www.californiamedicareenrollment.com"),
             ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"), ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")],
    sameas_org_extra=["https://howdoiapplyformedicare.com", "https://medicareadvantageanswers.com", "https://dentalinsurancetomorrow.com"],
    sameas_darin=["https://www.myecos360.com/darin-weidauer", "https://www.linkedin.com/in/darin-weidauer-3165a816b/", "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
                  "https://www.medicareenrollmentarizona.com/about", "https://minnesotamedicareenrollment.com/about", "https://texasmedicareenrollment.com/about", "https://medicareenrollmentflorida.com/about", "https://www.californiamedicareenrollment.com/about", "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or Utah&rsquo;s Senior Health Insurance Information Program (SHIP, 800-541-7735) to get information on all of your options."),
    not_affiliated="the State of Utah, the Utah Department of Health and Human Services, Utah Medicaid, or the Utah Insurance Department",
    ship_name="Utah SHIP", ship_phone="800-541-7735",
    brand_tag="Plain-English Medicare help in Utah", theme_color="#24466b",
    footer_tagline="Plain-English Medicare guidance for Utah retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping Utah retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from the Wasatch Front to St. George.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and Utah Medicaid dual eligibility",
                 "Intermountain and University of Utah Health networks", "Medicare for military retirees", "Utah snowbirds"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "Medicare Advantage", "Medicare Supplement (Medigap)", "Part D drug plan",
                      "I winter in St. George / Arizona / Nevada", "I have VA / TRICARE", "I have Medicaid too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Moving counties opens a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across Utah',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/snowbirds">Snowbirds &amp; second homes</a>', '<a href="/medicaid">Utah Medicaid and Medicare Savings Programs</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="wasatch", h1="Utah Medicare questions, answered plainly",
                  sub="The questions we hear most from Utahns &mdash; about Intermountain and the U, Select Health, Medigap underwriting, St. George winters, Hill Air Force Base, and what any of this costs. Short answers, with links to the longer ones.",
                  title="Utah Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Utahns ask most: Intermountain vs University of Utah networks, Select Health, Medigap rules, St. George snowbirds, Hill AFB and TRICARE, and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for Utah retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from Logan and Ogden through the Salt Lake and Utah valleys to St. George and Moab.",
    llm_facts=["Darin Weidauer holds Utah insurance license #713009 (NPN 18580338).",
               "Utah uses the federal Medigap plan letters (A–N) and has no birthday or anniversary rule; the Utah Insurance Department regulates Medigap and publishes a plan comparison tool. Utah does not require insurers to sell Medigap to people under 65; a few companies choose to.",
               "Utah's care is dominated by two systems, Intermountain Health and University of Utah Health, plus MountainStar (HCA) and Holy Cross (CommonSpirit); Select Health is Intermountain's insurance arm, so the Advantage choice usually starts with which system a family uses.",
               "Utah's SHIP is the Senior Health Insurance Information Program, run by the Utah Department of Health and Human Services' Division of Aging and Adult Services with county aging offices: 800-541-7735.",
               "Utah Medicaid is run by the Department of Health and Human Services; eligibility for seniors is determined by the Department of Workforce Services (apply at jobs.utah.gov/mycase or 1-866-435-7414). Medicare Savings Programs (QMB, SLMB, QI) use the federal income and resource limits and automatically qualify the enrollee for Part D Extra Help.",
               "Hill Air Force Base in Davis County anchors a large TRICARE For Life community; the George E. Wahlen VA Medical Center in Salt Lake City serves veterans statewide with clinics in Ogden, Provo, St. George and Logan.",
               "Many Utahns winter in St. George, Mesquite (Nevada) or Arizona; a Medigap policy works in every state, most Advantage HMOs cover only emergencies outside their service area."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/snowbirds", "Snowbirds"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in Utah</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/snowbirds">Snowbirds &amp; second homes</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Utah Medicaid &amp; savings programs</a>',
                   '<a href="/faq">Questions Utahns ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://daas.utah.gov" rel="noopener">Utah SHIP (Division of Aging &amp; Adult Services)</a>, 800-541-7735',
                                    '<a href="https://insurance.utah.gov" rel="noopener">Utah Insurance Department</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a network &mdash; usually built around Intermountain, the U, MountainStar or Holy Cross.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; Huntsman, Intermountain, or a clinic in Mesquite.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Utah Medicaid.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="wasatch", title="Medicare Help in Utah [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Utahns: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Logan to St. George.",
    eyebrow="Medicare made clear · Statewide in Utah",
    h1="Medicare in Utah, explained by someone who actually teaches it.",
    sub="Turning 65, retiring, or wondering whether the plan built around your hospital system still fits? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in Utah &middot; UT License #713009 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="Utah is different", different_h2="Three things about Medicare in Utah that the national websites gloss over",
    different_lede="Utah&rsquo;s care runs through two big systems, its retirees migrate south every winter, and its Medigap rules give you exactly one clean shot. Start with what actually shapes the choice here.",
    different_cards=[
        ("It starts with your hospital system", "Intermountain Health or University of Utah Health? Select Health is Intermountain&rsquo;s own insurer, the U has its own plans, and MountainStar and Holy Cross contract separately. Which system your doctors belong to decides the Advantage shortlist before price does.", "/medicare-advantage", "Networks, plainly"),
        ("One clean Medigap window", "Utah has no birthday rule and does not make insurers sell Medigap to people under 65. Your six-month open enrollment at 65 is the guaranteed window; after it, health questions. Use it well.", "/medicare-supplement", "When you can buy without underwriting"),
        ("Half the state goes south in January", "St. George, Mesquite, Mesa, Yuma. A Medigap policy follows you; most Advantage HMOs cover only emergencies out of area. Our Arizona and Nevada sister sites pick up where this one stops.", "/snowbirds", "Medicare for Utah snowbirds"),
    ],
    options_h2="Four ways Utahns get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your winters. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you spend the year. These are the situations Utahns ask us about most.",
    situations=[
        ("Snowbirds &amp; second homes", "Which plans work in St. George, Mesquite or Mesa, and which ones only cover emergencies once you leave your county.", "/snowbirds", "Medicare for snowbirds"),
        ("Hill AFB &amp; veterans", "TRICARE For Life, the Wahlen VA in Salt Lake and its clinics, and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Utah Medicaid", "The Medicare Savings Programs that pay your Part B premium, Extra Help, and Dual Special Needs Plans that coordinate both.", "/medicaid", "Dual-eligible help"),
        ("Chronic conditions &amp; facility care", "Chronic Special Needs Plans for diabetes, heart or lung disease, and Institutional SNPs for people in a nursing facility.", "/chronic-snp", "About C-SNPs"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the Utah-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer (UT License #713009) is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Utah retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with Utahns by phone and video across all 29 counties. Find Medicare guidance for your city:",
    bases_lede="Near Hill Air Force Base? We help military retirees coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("Do I have to choose between Intermountain and the University of Utah?", "Not with Original Medicare and a Medigap policy &mdash; both accept Medicare, so both are covered with no network. With Medicare Advantage, often yes: Select Health plans are built on Intermountain, the U&rsquo;s plans on University of Utah Health, and other carriers contract with each differently. We confirm your doctors before you enroll."),
        ("When can I enroll in or change my Medicare plan in Utah?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving counties, losing a plan, or qualifying for Medicaid opens a Special Enrollment Period."),
        ("Does Utah have a Medigap birthday rule?", "No. Your six-month Medigap open enrollment at 65 is the guaranteed window, plus guaranteed-issue events such as an Advantage plan leaving your county. Outside those, Utah insurers can use medical underwriting, and Utah does not require them to sell to people under 65."),
        ("I winter in St. George, Mesquite or Arizona. Which plan works?", "A Medigap policy with Original Medicare works anywhere in the U.S. Most Medicare Advantage HMOs cover only emergencies outside their service area; St. George is in Utah, but Mesquite and Mesa are not. Our snowbird guide walks through it, and our sister agency has offices in Mesa and Sun City, Arizona."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Utah, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and Utah SHIP (800-541-7735) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your winters together.",
)

OG = dict(line1="Medicare help in", line2="Utah", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="medicareenrollmentutah.com", mark="arch",
          palette=dict(primary=(36, 70, 107), dark=(23, 48, 74), gold=(231, 196, 134), paper=(245, 241, 234), sky=(221, 230, 238),
                       far=(143, 163, 184), mid=(127, 154, 112), green=(74, 107, 82)))
