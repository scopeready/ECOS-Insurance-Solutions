"""California site identity, home page, navigation."""
from datetime import date
TODAY = date(2026, 9, 4)
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#1b4e73"/>'
        '<circle cx="21" cy="17" r="7" fill="#e9c46a"/><path d="M6 27c5-4 10-4 15 0s10 4 15 0" stroke="#9dc3dc" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
        '<path d="M6 33c5-4 10-4 15 0s10 4 15 0" stroke="#9dc3dc" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#1b4e73"/>'
           '<circle cx="21" cy="17" r="7" fill="#e9c46a"/><path d="M6 27c5-4 10-4 15 0s10 4 15 0" stroke="#9dc3dc" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
           '<path d="M6 33c5-4 10-4 15 0s10 4 15 0" stroke="#9dc3dc" stroke-width="2.4" fill="none" stroke-linecap="round"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.californiamedicareenrollment.com", domain="www.californiamedicareenrollment.com", name="California Medicare Enrollment",
    org="ECOS Medicare Solutions", state="California", abbr="CA", demonym="Californians",
    # California requires the producer licence number next to the licensee's name (Cal. Ins. Code 1725.5).
    state_license="0M00978", state_license_label="CA License",
    # TODO(Darin): swap for a California (213 / 415 / 619 / 916) number.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Medicare Enrollment Arizona", "https://www.medicareenrollmentarizona.com"), ("Medicare Enrollment Nevada", "https://medicareenrollmentnevada.com"),
             ("Colorado Medicare Enrollment", "https://coloradomedicareenrollment.com"), ("Medicare Enrollment Utah", "https://medicareenrollmentutah.com"),
             ("Texas Medicare Enrollment", "https://texasmedicareenrollment.com"), ("Medicare Enrollment Florida", "https://medicareenrollmentflorida.com"),
             ("Georgia Medicare Enrollment", "https://georgiamedicareenrollment.com"), ("Minnesota Medicare Enrollment", "https://minnesotamedicareenrollment.com"),
             ("Tennessee Medicare Quotes", "https://www.tennesseemedicarequotes.com"),
             ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"), ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")],
    sameas_org_extra=["https://howdoiapplyformedicare.com", "https://medicareadvantageanswers.com", "https://dentalinsurancetomorrow.com"],
    sameas_darin=["https://www.myecos360.com/darin-weidauer", "https://www.linkedin.com/in/darin-weidauer-3165a816b/", "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
                  "https://www.medicareenrollmentarizona.com/about", "https://minnesotamedicareenrollment.com/about", "https://texasmedicareenrollment.com/about",
                  "https://medicareenrollmentutah.com/about", "https://medicareenrollmentflorida.com/about", "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or HICAP (the Health Insurance Counseling and Advocacy Program, California&rsquo;s State Health Insurance Assistance Program, 1-800-434-0222) to get information on all of your options."),
    not_affiliated="the State of California, the California Department of Insurance, the California Department of Aging, HICAP, the Department of Health Care Services, Medi-Cal, Covered California, or CalPERS",
    ship_name="California HICAP", ship_phone="1-800-434-0222",
    brand_tag="Plain-English Medicare help in California", theme_color="#1b4e73",
    footer_tagline="Plain-English Medicare guidance for California retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping California retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from San Diego and Los Angeles through the Bay Area and Sacramento to the far north.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "California Medigap birthday rule", "Medicare Part D", "Special Needs Plans", "Kaiser Permanente Senior Advantage",
                 "Medicare and Medi-Cal dual eligibility", "Medi-Medi Plans", "Wildfire disaster Special Enrollment Periods", "Medicare for military retirees"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My plan was discontinued", "Medicare Advantage", "Medicare Supplement (Medigap)", "Part D drug plan",
                      "Kaiser vs. other plans", "I'm moving to or from California", "I have VA / TRICARE", "I have Medi-Cal too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31, and California&rsquo;s Medigap birthday rule gives you 60 days from your birthday each year to switch supplements without health questions.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across California',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/kaiser">Kaiser Permanente and Medicare</a>', '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/moving">Moving to or from California</a>', '<a href="/medi-cal">Medicare + Medi-Cal</a>', '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="goldengate", h1="California Medicare questions, answered plainly",
                  sub="The questions we hear most from Californians &mdash; about Kaiser, the birthday rule, the 2026 PPO shake-up, Medi-Cal&rsquo;s asset limit coming back, wildfires, TRICARE, CalPERS, and what any of this costs. Short answers, with links to the longer ones.",
                  title="California Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Californians ask most: the 60-day Medigap birthday rule, Kaiser Senior Advantage, the 2026 Advantage changes, Medi-Cal and the returning asset limit, wildfire SEPs, HICAP, and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for California retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from San Diego, Los Angeles and Orange County through the Inland Empire, the Bay Area and Sacramento to the Central Valley, the Central Coast and the far north.",
    llm_facts=["California uses the federal Medigap plan letters (A–N) and has a 60-day birthday rule: each year, starting on your birthday, you may switch to any carrier's Medigap plan of equal or lesser benefits with no health questions (Cal. Ins. Code §10192.11 as amended 2019, effective 2020). Insurers must offer Medigap to people under 65 on Medicare because of disability, with a six-month open enrollment when Part B begins; that requirement does not extend to under-65 ESRD. Everyone gets a fresh six-month open enrollment at 65. Most California Medigap premiums are attained-age rated.",
               "About half of California's Medicare beneficiaries are in Medicare Advantage, and Kaiser Permanente Senior Advantage alone covers more than 1.4 million Californians; Kaiser is a closed, integrated system, so a Medigap policy cannot be used at Kaiser. For the 2026 plan year Anthem Blue Cross ended its Advantage PPO plans in California, Aetna closed plans and left counties, and UnitedHealthcare and Humana exited counties nationally; California's plan count fell from 421 to 402.",
               "California's SHIP is HICAP, the Health Insurance Counseling and Advocacy Program, run by the California Department of Aging through local Area Agencies on Aging: 1-800-434-0222.",
               "Medi-Cal (California Medicaid) is administered by the Department of Health Care Services with eligibility handled by county offices. The Medi-Cal asset limit, eliminated in 2024, was reinstated on January 1, 2026 at $130,000 for one person plus $65,000 for each additional household member, and it applies to the Medicare Savings Programs (QMB, SLMB, QI). Under CalAIM, Medi-Medi Plans (exclusively aligned D-SNPs) are available in 41 counties for 2026.",
               "Darin Weidauer holds California insurance license #0M00978 (NPN 18580338). California law requires the license number to appear next to a licensee's name in advertising (Cal. Ins. Code §1725.5).",
               "A FEMA-declared disaster, including wildfires, opens a Special Enrollment Period for people in the declared counties who missed an enrollment deadline because of it, and Part D plans must lift refill-too-soon limits in the emergency area.",
               "CalPERS retirees must enroll in Medicare Part B when eligible and choose a CalPERS Medicare plan; the individual-market plans on this site are separate from CalPERS. Military retirees around San Diego, Camp Pendleton, Travis AFB, Vandenberg and Edwards use TRICARE For Life; VA care runs through the Greater Los Angeles, Long Beach, Loma Linda, San Diego, Palo Alto, San Francisco, Northern California and Central California systems."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/kaiser", "Kaiser"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>', '<a href="/kaiser">Kaiser Permanente &amp; Medicare</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in California</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/moving">Moving to or from California</a>', '<a href="/wildfires">Wildfires &amp; Medicare</a>', '<a href="/veterans">Veterans</a>',
                   '<a href="/medi-cal">Medicare + Medi-Cal</a>', '<a href="/faq">Questions Californians ask</a>', '<a href="/about">About Darin</a>',
                   '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://aging.ca.gov/Programs_and_Services/Medicare_Counseling/" rel="noopener">HICAP (California&rsquo;s SHIP)</a>, 1-800-434-0222',
                                    '<a href="https://www.insurance.ca.gov" rel="noopener">California Department of Insurance</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, built on a county network &mdash; the choice of about half of California, and the one that changed most for [[YEAR]].", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and works with any provider nationwide &mdash; UCLA, Stanford, Cedars, City of Hope, or your doctor in Arizona &mdash; with California&rsquo;s birthday rule to switch every year.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Kaiser Permanente", "Senior Advantage is its own world: everything in one system, and no Medigap route in. When it fits, and when it doesn&rsquo;t.", "/kaiser", "Kaiser &amp; Medicare"),
]

HOME = dict(
    scene="goldengate", title="Medicare Help in California [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Californians: Medicare Advantage, Medigap, Kaiser and Part D compared by a credentialed independent agent (CA License #0M00978), statewide.",
    eyebrow="Medicare made clear · Statewide in California",
    h1="Medicare in California, explained by someone who actually teaches it.",
    sub="Turning 65, weighing Kaiser against everything else, or re-shopping because your PPO went away? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in California &middot; CA License #0M00978 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="California is different", different_h2="Three things about Medicare in California that the national websites gloss over",
    different_lede="California has more people on Medicare than any state, a health system built around integrated networks, and a Medigap rule almost no other state has. Start with what actually shapes the choice here.",
    different_cards=[
        ("The Kaiser question comes first", "More than 1.4 million Californians take Medicare through Kaiser Permanente Senior Advantage. It is a closed system: you cannot pair Original Medicare and a Medigap policy with Kaiser doctors. Decide whether you are staying in Kaiser before you compare anything else.", "/kaiser", "Kaiser &amp; Medicare, explained"),
        ("You get a birthday rule every year", "Each year, for 60 days starting on your birthday, California lets you move your Medigap policy to any carrier&rsquo;s plan of equal or lesser benefits with no health questions. Most states make you pass underwriting to switch. Use it, and never overpay for a Plan G again.", "/medicare-supplement", "How the birthday rule works"),
        ("The PPO menu shrank for 2026", "Anthem Blue Cross ended its Advantage PPO plans in California, Aetna closed plans and left counties, and UnitedHealthcare and Humana pulled out of counties too. A discontinued plan opens a Special Enrollment Period and, usually, a guaranteed-issue right to Medigap.", "/medicare-advantage", "What changed, and what to do"),
    ],
    options_h2="Four ways Californians get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you spend the year. These are the situations Californians ask us about most.",
    situations=[
        ("Moving to or from California", "Retiring to Arizona, Nevada, Texas or Idaho, or arriving here from somewhere else: what a move does to your plan, your Medigap rights and your Part D.", "/moving", "Medicare when you move"),
        ("Wildfires &amp; Medicare", "What a FEMA disaster declaration does to your enrollment deadlines, and how to keep prescriptions filled when you evacuate.", "/wildfires", "Wildfires &amp; Medicare"),
        ("Veterans &amp; military retirees", "TRICARE For Life, the VA (Greater LA, San Diego, Palo Alto, Loma Linda, Sacramento, Fresno), and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Medi-Cal", "The Medicare Savings Programs that pay your Part B premium, the asset limit that returned in 2026, Extra Help, and the Medi-Medi Plans that coordinate both.", "/medi-cal", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the California-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer is an independent Medicare insurance agent (CA License #0M00978), credentialed gerontologist, and Registered Social Security Analyst&reg; who helps California retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine University and a Master&rsquo;s in Long-Term Care from the University of Southern California&rsquo;s Leonard Davis School of Gerontology, where he became a credentialed gerontologist in 2014.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with Californians by phone and video across all 58 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("My California Medicare Advantage PPO was discontinued. What now?", "You are not alone: Anthem Blue Cross ended its Advantage PPOs in California for 2026 and Aetna closed plans in many counties. A non-renewal notice gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending. Our Medicare Advantage page walks through the choices."),
        ("What is California&rsquo;s Medigap birthday rule?", "Each year, for 60 days beginning on your birthday, you can switch your Medigap policy to any insurer&rsquo;s plan with the same or lesser benefits, with no medical underwriting. It is the reason Californians should re-shop their supplement every year; we do it for our clients as a matter of course."),
        ("Can I keep Kaiser when I go on Medicare?", "Yes, through Kaiser Permanente Senior Advantage, a Medicare Advantage plan. What you cannot do is keep Kaiser doctors with Original Medicare and a Medigap policy, because Kaiser does not generally treat Original Medicare patients outside emergencies. Our Kaiser page compares the two paths honestly."),
        ("I have VA or TRICARE benefits. Do I still need Medicare?", "Often, yes. VA health care and Medicare do not coordinate with each other, and TRICARE For Life requires you to have Medicare Parts A and B. Enrolling in Part B on time matters even with VA care, because VA medical coverage is not creditable for Part B and the late penalty lasts for life. Our Veterans page explains how these benefits fit together."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in California, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and HICAP (1-800-434-0222) have the complete lists."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your calendar together.",
)

OG = dict(line1="Medicare help in", line2="California", sub1="Plain-English, no-cost guidance from a licensed independent agent (CA Lic. #0M00978),",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="californiamedicareenrollment.com", mark="sun",
          palette=dict(primary=(27, 78, 115), dark=(16, 52, 79), gold=(233, 196, 106), paper=(247, 244, 236), sky=(219, 231, 240),
                       far=(183, 194, 163), mid=(138, 163, 115), green=(74, 107, 63)))
