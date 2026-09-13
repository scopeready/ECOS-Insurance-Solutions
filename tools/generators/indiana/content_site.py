"""Indiana site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 13)
# Mark: the torch from the Indiana state flag, in harvest gold on cornfield green.
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#2e5a3a"/>'
        '<path d="M21 7c3.2 3.4 5.4 6.6 5.4 10.2 0 2.6-1.6 4.6-3.6 5.4.8-1.6.6-3.4-.8-5.2-.6 1.8-1.8 3-3.2 4-1.4-1.6-1.6-3.6-.6-5.8-2.4 1.6-3.6 3.8-3.6 6.2 0 3.4 2.8 6 6.4 6s6.4-2.6 6.4-6C27.4 15.6 24.8 10.6 21 7z" fill="#e6c26a"/>'
        '<rect x="18.6" y="26" width="4.8" height="9" rx="1.2" fill="#e6c26a"/><rect x="15.5" y="33.6" width="11" height="2.4" rx="1.2" fill="#e6c26a"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#2e5a3a"/>'
           '<path d="M21 7c3.2 3.4 5.4 6.6 5.4 10.2 0 2.6-1.6 4.6-3.6 5.4.8-1.6.6-3.4-.8-5.2-.6 1.8-1.8 3-3.2 4-1.4-1.6-1.6-3.6-.6-5.8-2.4 1.6-3.6 3.8-3.6 6.2 0 3.4 2.8 6 6.4 6s6.4-2.6 6.4-6C27.4 15.6 24.8 10.6 21 7z" fill="#e6c26a"/>'
           '<rect x="18.6" y="26" width="4.8" height="9" rx="1.2" fill="#e6c26a"/><rect x="15.5" y="33.6" width="11" height="2.4" rx="1.2" fill="#e6c26a"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.ecosinsurancesolutions.com/indiana", domain="ecosinsurancesolutions.com/indiana", name="Indiana Medicare Enrollment",
    org="ECOS Medicare Solutions", state="Indiana", abbr="IN", demonym="Hoosiers",
    # TODO(Darin): replace with the Indiana (317 / 260 / 812 / 219) number once he provides it. The agency's main line is the placeholder.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # Indiana producer licence, shown beside Darin's name site-wide by the engine.
    state_license="3951814", state_license_label="IN License",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Medicare Enrollment Arizona", "https://www.ecosinsurancesolutions.com/arizona"),
             ("California Medicare Enrollment", "https://www.ecosinsurancesolutions.com/california"),
             ("Colorado Medicare Enrollment", "https://www.ecosinsurancesolutions.com/colorado"),
             ("Medicare Enrollment Florida", "https://www.ecosinsurancesolutions.com/florida"),
             ("Georgia Medicare Enrollment", "https://www.ecosinsurancesolutions.com/georgia"),
             ("Hawaii Medicare Enrollment", "https://www.ecosinsurancesolutions.com/hawaii"),
             ("Minnesota Medicare Enrollment", "https://www.ecosinsurancesolutions.com/minnesota"),
             ("Medicare Enrollment Nevada", "https://www.ecosinsurancesolutions.com/nevada"),
             ("New Mexico Medicare Enrollment", "https://www.ecosinsurancesolutions.com/new-mexico"),
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
          "Please contact Medicare.gov, 1-800-MEDICARE, or Indiana SHIP (the State Health Insurance Assistance Program, run by the Indiana Department "
          "of Insurance, 800-452-4800) to get information on all of your options."),
    not_affiliated="the State of Indiana, the Indiana Family and Social Services Administration, Indiana Medicaid, Indiana SHIP, or the Indiana Department of Insurance",
    ship_name="Indiana SHIP", ship_phone="800-452-4800",
    brand_tag="Plain-English Medicare help in Indiana", theme_color="#2e5a3a",
    footer_tagline="Plain-English Medicare guidance for Indiana retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping Indiana retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Indianapolis and Fort Wayne to Evansville, South Bend and the Region.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Indiana Medigap birthday rule", "Medicare Part D", "Special Needs Plans",
                 "Medicare and Indiana Medicaid dual eligibility", "Indiana PathWays for Aging", "Medicare for military retirees", "Hoosier snowbirds"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My Medigap premium went up", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I winter in Florida or Arizona", "I have VA / TRICARE", "I have Medicaid too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Already have a Medigap policy? Indiana&rsquo;s birthday rule opens a switching window around your birthday each year.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across Indiana',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/snowbirds">Hoosier snowbirds &amp; border care</a>', '<a href="/medicaid">Indiana Medicaid, PathWays for Aging and Medicare Savings Programs</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="farm", h1="Indiana Medicare questions, answered plainly",
                  sub="The questions we hear most from Hoosiers &mdash; about the new Medigap birthday rule, IU Health and Anthem, plans that changed for 2026, wintering in Florida, PathWays for Aging, the VA, and what any of this costs. Short answers, with links to the longer ones.",
                  title="Indiana Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Hoosiers ask most: the Indiana Medigap birthday rule, under-65 Medigap rights, PathWays for Aging, snowbird coverage, VA and TRICARE, and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for Indiana retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from Indianapolis, Fort Wayne, Evansville and South Bend to the Region, the Wabash Valley and the Ohio River towns.",
    llm_facts=["Darin Weidauer holds Indiana insurance license #3951814 (NPN 18580338).",
               "Indiana uses the federal Medigap plan letters (A–N), regulated by the Indiana Department of Insurance. Since 2026 Indiana has a Medigap birthday rule (HEA 1226 of 2025, amended by HEA 1260 of 2026): a policyholder 65 or older can switch to the same plan letter with another insurer, without health questions, in a window that opens 31 days before their birthday and closes 31 days after it; the new policy starts the first of the following month.",
               "Since January 1, 2025 (SEA 215, Indiana Code 27-8-13-9.1), Hoosiers under 65 who have Medicare because of a disability or ESRD get their own six-month Medigap open enrollment, and insurers must offer them coverage.",
               "Roughly half of Indiana's Medicare beneficiaries are in Medicare Advantage. IU Health Plans, the Advantage plan built on the IU Health system, was acquired by Elevance Health (Anthem's parent) on January 1, 2025, and its members were moved to Anthem plans for 2026. Nationally UnitedHealthcare and Humana withdrew from hundreds of counties for 2026, and Humana has announced further exits for 2027.",
               "Indiana's SHIP is the State Health Insurance Assistance Program, run by the Indiana Department of Insurance: 800-452-4800, with counseling sites across the state.",
               "Indiana Medicaid is administered by the Family and Social Services Administration (FSSA). Since July 1, 2024, Hoosiers 60 and older who qualify for Medicaid on the basis of age, blindness or disability, including people with both Medicare and Medicaid, receive it through Indiana PathWays for Aging, a managed-care program run by Anthem, Humana and UnitedHealthcare. Apply through the FSSA Benefits Portal or 800-403-0864. Medicare Savings Programs (QMB, SLMB, QI) are handled by FSSA's Division of Family Resources and automatically qualify the enrollee for Part D Extra Help. HoosierRx, the state pharmaceutical assistance program, pays up to $70 a month toward a Part D premium for eligible Hoosiers 65 and older.",
               "Indiana is home to more than 325,000 veterans. VA care runs through the Richard L. Roudebush VA Medical Center in Indianapolis, the VA Northern Indiana Health Care System (Fort Wayne and Marion campuses) and the Evansville VA Health Care Center, part of the Marion, Illinois VA. Indiana's main installations are Naval Support Activity Crane and Grissom Air Reserve Base.",
               "Many Hoosiers winter in Florida or Arizona, and many along the borders use hospitals in Louisville, Cincinnati and Chicago. A Medigap policy with Original Medicare works in every state; most Medicare Advantage HMOs cover only emergencies out of area."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/snowbirds", "Snowbirds"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in Indiana</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/snowbirds">Hoosier snowbirds &amp; border care</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Indiana Medicaid &amp; PathWays for Aging</a>',
                   '<a href="/faq">Questions Hoosiers ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://www.in.gov/ship/" rel="noopener">Indiana SHIP</a>, 800-452-4800',
                                    '<a href="https://www.in.gov/idoi/" rel="noopener">Indiana Department of Insurance</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a network &mdash; so whether your doctors are IU Health, Ascension St. Vincent, Community, Franciscan, Parkview or Deaconess matters.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; in Indianapolis, in Louisville or Chicago, or in Florida for the winter. Indiana now has a birthday rule for switching.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100. HoosierRx can help with the premium.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Indiana Medicaid through PathWays for Aging.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="monument", title="Medicare Help in Indiana [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Hoosiers: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Indianapolis to Fort Wayne, Evansville and the Region.",
    eyebrow="Medicare made clear · Statewide in Indiana",
    h1="Medicare in Indiana, explained by someone who actually teaches it.",
    sub="Turning 65, retiring from the plant or the school corporation, or re-shopping because your plan changed for 2026? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in Indiana &middot; IN License #3951814 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="Indiana is different", different_h2="Three things about Medicare in Indiana that the national websites gloss over",
    different_lede="Indiana has 92 counties, about half its Medicare population in Advantage plans, a Medigap switching rule that is brand new, and a care map organized around a handful of big systems that each contract on their own terms. Start with what is actually for sale where you live.",
    different_cards=[
        ("The birthday rule is new, and it changes the math", "Since 2026 a Hoosier 65 or older with a Medigap policy can move to the same plan letter at another insurer, with no health questions, in a window around each birthday. That turns a premium increase from something you absorb into something you shop. We track every Indiana carrier&rsquo;s filed rate history.", "/medicare-supplement", "How the birthday rule works"),
        ("Your hospital system decides your shortlist", "IU Health, Ascension St. Vincent, Community, Franciscan and Eskenazi in Indianapolis; Parkview and Lutheran in Fort Wayne; Deaconess in Evansville; Beacon and Saint Joseph in South Bend &mdash; each contracts with some Advantage plans and not others. And IU Health&rsquo;s own plan moved under Anthem for 2026.", "/medicare-advantage", "What changed for 2026"),
        ("A lot of Hoosiers leave for the winter, or cross a state line for care", "Florida in January, a specialist in Louisville, Cincinnati or Chicago in March. A Medigap policy follows you anywhere; most Advantage HMOs stop at the network line. Which one fits depends on how you actually live.", "/snowbirds", "Snowbirds &amp; border care"),
    ],
    options_h2="Four ways Hoosiers get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your winters. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you spend the year. These are the situations Hoosiers ask us about most.",
    situations=[
        ("Snowbirds &amp; border commuters", "Which plans work when you winter in Florida or Arizona, or see a doctor in Louisville, Cincinnati or Chicago.", "/snowbirds", "Medicare for Hoosier snowbirds"),
        ("My premium went up, or my plan changed", "Indiana&rsquo;s new Medigap birthday rule, what a plan-exit notice gives you, and the deadlines that come with each.", "/medicare-supplement", "What to do next"),
        ("Veterans &amp; military retirees", "TRICARE For Life, the Roudebush VA, VA Northern Indiana and the Evansville VA &mdash; and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Indiana Medicaid", "PathWays for Aging, the Medicare Savings Programs that pay your Part B premium, HoosierRx, and Dual Special Needs Plans that coordinate both.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the Indiana-specific choices in front of you &mdash; including what to do with a union or employer retiree plan &mdash; and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer (IN License #3951814) is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Indiana retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with Hoosiers by phone and video across all 92 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("What is Indiana&rsquo;s Medigap birthday rule?", "A switching window that Indiana added for 2026. If you are 65 or older and already have a Medigap policy, you can apply to another insurer for the same plan letter, without medical underwriting, in a window that opens 31 days before your birthday and closes 31 days after it; the new policy starts the first of the following month. It is the tool for a Hoosier whose Plan G premium just jumped. Details and the current wording are on our Medigap page and with Indiana SHIP."),
        ("When can I enroll in or change my Medicare plan in Indiana?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving counties, losing a plan, or qualifying for Medicaid opens a Special Enrollment Period, and the birthday rule covers Medigap-to-Medigap switches."),
        ("Are my IU Health or Ascension St. Vincent doctors in a Medicare Advantage plan?", "It depends on the plan and the year. Every big Indiana system accepts Original Medicare, and therefore any Medigap policy. Each contracts with some Advantage plans and not others, and the list changes every October &mdash; and for 2026 IU Health Plans&rsquo; own Advantage members were moved under Anthem. If a specific system or doctor is your care, we confirm the plan&rsquo;s status in writing before you enroll."),
        ("I have VA or TRICARE benefits. Do I still need Medicare?", "Often, yes. VA health care and Medicare do not coordinate with each other, and TRICARE For Life requires you to have Medicare Parts A and B. Enrolling in Part B on time matters even with VA care at Roudebush or Fort Wayne, because VA medical coverage is not creditable for Part B and the late penalty lasts for life. Our Veterans page explains how these benefits fit together."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Indiana, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and Indiana SHIP (800-452-4800) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your winters together.",
)

OG = dict(line1="Medicare help in", line2="Indiana", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="ecosinsurancesolutions.com/indiana", mark="sun",
          palette=dict(primary=(46, 90, 58), dark=(30, 63, 40), gold=(230, 194, 106), paper=(245, 240, 227), sky=(221, 229, 224),
                       far=(207, 214, 204), mid=(159, 180, 137), green=(95, 125, 60)))
