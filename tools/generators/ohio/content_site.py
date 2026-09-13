"""Ohio site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 13)
# Mark: a buckeye nut (dark brown with the pale "eye") on a Lake Erie blue field.
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#1e4d78"/>'
        '<circle cx="21" cy="22" r="12" fill="#6b4a2b"/><ellipse cx="21" cy="17" rx="7" ry="5.5" fill="#e6d3a3"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#1e4d78"/>'
           '<circle cx="21" cy="22" r="12" fill="#6b4a2b"/><ellipse cx="21" cy="17" rx="7" ry="5.5" fill="#e6d3a3"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.ecosinsurancesolutions.com/ohio", domain="ecosinsurancesolutions.com/ohio", name="Ohio Medicare Enrollment",
    org="ECOS Medicare Solutions", state="Ohio", abbr="OH", demonym="Ohioans",
    # TODO(Darin): replace with the Ohio number once he provides it. Main line as placeholder.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # Ohio producer licence (Major Lines), shown beside Darin's name site-wide via the engine.
    state_license="1616139", state_license_label="OH License",
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
             ("South Carolina Medicare Enrollment", "https://www.ecosinsurancesolutions.com/south-carolina"),
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
          "Please contact Medicare.gov, 1-800-MEDICARE, or the Ohio Senior Health Insurance Information Program (OSHIIP, Ohio&rsquo;s State Health "
          "Insurance Assistance Program, run by the Ohio Department of Insurance, 800-686-1578) to get information on all of your options."),
    not_affiliated="the State of Ohio, the Ohio Department of Medicaid, MyCare Ohio, or the Ohio Department of Insurance",
    ship_name="OSHIIP", ship_phone="800-686-1578",
    brand_tag="Plain-English Medicare help in Ohio", theme_color="#1e4d78",
    footer_tagline="Plain-English Medicare guidance for Ohio retirees and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping Ohio retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Cleveland, Columbus and Cincinnati to Toledo, Dayton and the Ohio River counties.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and Ohio Medicaid dual eligibility",
                 "MyCare Ohio", "OPERS, STRS and SERS retiree coverage", "Medicare for military retirees", "Medicare Savings Programs"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My plan left my county", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I have OPERS / STRS / SERS / union retiree coverage", "I have VA / TRICARE", "I have Medicaid or MyCare Ohio"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. A plan leaving your county opens a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across Ohio',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/retiree-coverage">OPERS, STRS, SERS, OP&amp;F and union retiree coverage</a>', '<a href="/medicaid">Ohio Medicaid, MyCare Ohio and Medicare Savings Programs</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="buckeye", h1="Ohio Medicare questions, answered plainly",
                  sub="The questions we hear most from Ohioans &mdash; about which hospital system a plan includes, the 2026 plan shake-up, Medigap rules, OPERS and STRS coverage, MyCare Ohio, Wright-Patterson retirees, and what any of this costs. Short answers, with links to the longer ones.",
                  title="Ohio Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Ohioans ask most: Cleveland Clinic and OSU networks, Medigap rules and the under-65 gap, OPERS and STRS retiree plans, MyCare Ohio, TRICARE and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for Ohio retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, across all 88 counties from Cleveland, Columbus and Cincinnati to Toledo, Dayton, Youngstown and the Ohio River valley.",
    llm_facts=["Darin Weidauer holds Ohio insurance license #1616139 (NPN 18580338).",
               "Ohio uses the federal Medigap plan letters (A–N) and has no birthday or anniversary rule; outside the six-month open enrollment at 65 and guaranteed-issue events, Ohio insurers can use medical underwriting. Ohio does not require insurers to sell Medigap to people under 65 on Medicare because of a disability. The Ohio Department of Insurance regulates Medigap.",
               "Ohio has roughly 2.1 million Medicare beneficiaries. For 2026 Medical Mutual of Ohio did not renew some plans in 44 counties and Aetna ended its Smart Fit plan; the national carriers scaled back county footprints as well, and Humana has announced further reductions for 2027. Ohio-based Medicare Advantage carriers include Medical Mutual (MedMutual Advantage and Paramount Elite), MediGold (Mount Carmel / Trinity Health) and SummaCare (Summa Health).",
               "Ohio's SHIP is the Ohio Senior Health Insurance Information Program (OSHIIP), part of the Ohio Department of Insurance since 1992: 800-686-1578.",
               "Ohio Medicaid is administered by the Ohio Department of Medicaid; apply at benefits.ohio.gov or 800-324-8680. People with both Medicare and Medicaid are served by MyCare Ohio, which relaunched on January 1, 2026 as Next Generation MyCare, a fully integrated dual-eligible special needs plan (FIDE-SNP) offered by Anthem Blue Cross and Blue Shield, Buckeye Health Plan, CareSource and Molina Healthcare of Ohio, starting in the original 29 counties and scheduled to reach all 88 by August 1, 2026. Medicare Savings Programs (QMB, SLMB, QI) are handled by Ohio Medicaid and automatically qualify the enrollee for Part D Extra Help.",
               "Ohio public pension retirees keep employer coverage that decides their Medicare choice: OPERS pays a Health Reimbursement Arrangement only when the retiree buys a Medicare plan through Via Benefits (the OPERS Connector); STRS Ohio and SERS Ohio enrol Medicare-eligible retirees in a group Aetna Medicare Advantage PPO; OP&F pays a stipend through Alight Retiree Health Solutions. All require Medicare Parts A and B.",
               "Ohio has about 606,000 veterans (Census Bureau 2020–2024 estimate). VA care runs through the Louis Stokes Cleveland VA Medical Center, the Cincinnati, Dayton and Chillicothe VA Medical Centers and the Chalmers P. Wylie VA Ambulatory Care Center in Columbus. Wright-Patterson Air Force Base near Dayton anchors a large Air Force retiree community; the Defense Supply Center Columbus in Whitehall is the ID-card and retiree hub for central Ohio."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/retiree-coverage", "Retiree plans"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in Ohio</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/retiree-coverage">OPERS, STRS &amp; retiree coverage</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Ohio Medicaid &amp; MyCare Ohio</a>',
                   '<a href="/faq">Questions Ohioans ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://insurance.ohio.gov/consumers/medicare/01-oshiip" rel="noopener">OSHIIP (Ohio&rsquo;s SHIP)</a>, 800-686-1578',
                                    '<a href="https://insurance.ohio.gov" rel="noopener">Ohio Department of Insurance</a>',
                                    '<a href="https://benefits.ohio.gov" rel="noopener">Ohio Benefits (Medicaid)</a>, 800-324-8680']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a local network &mdash; so which hospital system your doctors belong to, your county and your prescriptions matter.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider nationwide that accepts Medicare &mdash; Cleveland Clinic, the James, or a clinic in Florida in February.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Ohio Medicaid (MyCare Ohio).", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="erie", title="Medicare Help in Ohio [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Ohioans: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, from Cleveland and Columbus to Cincinnati, Toledo and Dayton.",
    eyebrow="Medicare made clear · Statewide in Ohio",
    h1="Medicare in Ohio, explained by someone who actually teaches it.",
    sub="Turning 65, retiring from the state or a school district, or re-shopping because your plan changed for 2026? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in Ohio &middot; OH License #1616139 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="Ohio is different", different_h2="Three things about Medicare in Ohio that the national websites gloss over",
    different_lede="Ohio has 88 counties, some of the deepest Medicare Advantage menus in the country in Cuyahoga and Summit, hospital systems that contract plan by plan, and a huge population of public-pension and union retirees whose employer coverage decides the Medicare question before price does. Start with what actually applies to you.",
    different_cards=[
        ("Your hospital system decides the shortlist", "Cleveland Clinic, University Hospitals and MetroHealth; OSU Wexner, OhioHealth and Mount Carmel; UC Health, TriHealth, Christ and Mercy; Premier and Kettering &mdash; each contracts with some Advantage plans and not others, and several sell plans of their own (MediGold, SummaCare). Which system your doctors belong to is the first question, not the premium.", "/medicare-advantage", "How networks work in Ohio"),
        ("The map was redrawn for 2026", "Medical Mutual did not renew some of its plans in 44 Ohio counties, Aetna ended its Smart Fit plan, and the national carriers trimmed county footprints across the state. A non-renewal notice opens a Special Enrollment Period and, usually, a guaranteed-issue right to Medigap &mdash; but Ohio has no birthday rule to fall back on later.", "/medicare-supplement", "What a non-renewal notice gives you"),
        ("A state of pension retirees", "OPERS, STRS, SERS, OP&amp;F, the UAW trust and the steel and auto retiree plans each coordinate with Medicare differently. Some pay you an allowance only if you buy through their connector; some enrol you in a group Advantage plan; all of them expect Parts A and B on time.", "/retiree-coverage", "Retiree coverage &amp; Medicare"),
    ],
    options_h2="Four ways Ohioans get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county, your retiree benefits and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you spend the year. These are the situations Ohioans ask us about most.",
    situations=[
        ("OPERS, STRS, SERS &amp; union retirees", "How the OPERS HRA, the STRS and SERS Aetna Medicare plans, OP&amp;F&rsquo;s stipend and the UAW trust fit with Medicare &mdash; and what an outside agent can and cannot do for you.", "/retiree-coverage", "Retiree coverage &amp; Medicare"),
        ("My plan changed for 2026", "Medical Mutual, Aetna and the national carriers all trimmed Ohio plans for 2026. What a non-renewal notice gives you, and the deadline that comes with it.", "/medicare-advantage", "What to do next"),
        ("Veterans &amp; military retirees", "TRICARE For Life, VA care at Cleveland, Columbus, Cincinnati, Dayton and Chillicothe, Wright-Patterson &mdash; and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Ohio Medicaid", "Next Generation MyCare Ohio, the Medicare Savings Programs that pay your Part B premium, and Extra Help for Part D.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the Ohio-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer (OH License #1616139) is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Ohio retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with Ohioans by phone and video across all 88 counties. Find Medicare guidance for your city:",
    bases_lede="Near Wright-Patterson or the Defense Supply Center? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("My Medicare Advantage plan is leaving my Ohio county. What do I do?", "You are not alone: for 2026 Medical Mutual of Ohio did not renew some plans in 44 counties, Aetna ended its Smart Fit plan, and the national carriers scaled back county footprints. A non-renewal notice gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending. Ohio has no birthday rule to fall back on later, so call before the deadline on the notice."),
        ("When can I enroll in or change my Medicare plan in Ohio?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving counties, losing a plan, or qualifying for Medicaid opens a Special Enrollment Period."),
        ("Does Cleveland Clinic or OSU Wexner take Medicare Advantage?", "Both accept Original Medicare, and therefore any Medigap policy. Each contracts with some Medicare Advantage plans and not others, and the lists change every year. If Cleveland Clinic, University Hospitals, the James, OhioHealth, UC Health or another specific system is your care, we confirm the plan&rsquo;s network status in writing before you enroll."),
        ("I retired from the state, a school district or a union plant. Does that change my Medicare choice?", "Usually it decides it. OPERS pays its HRA allowance only when you buy a Medicare plan through Via Benefits; STRS and SERS put Medicare-eligible retirees into a group Aetna Medicare Advantage PPO; OP&amp;F pays a stipend through Alight; the UAW trust expects Parts A and B. Our retiree coverage page explains each one and where an independent agent fits."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Ohio, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and OSHIIP (800-686-1578) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your retiree benefits, your county and your travel together.",
)

OG = dict(line1="Medicare help in", line2="Ohio", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="ecosinsurancesolutions.com/ohio", mark="buckeye",
          palette=dict(primary=(30, 77, 120), dark=(19, 55, 90), gold=(217, 178, 95), paper=(244, 242, 236), sky=(219, 231, 241),
                       far=(205, 214, 210), mid=(143, 165, 131), green=(76, 107, 62)))
