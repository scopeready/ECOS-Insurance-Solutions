"""Florida site identity, home page, navigation."""
from datetime import date
TODAY = date(2026, 9, 4)
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#0f5c6e"/>'
        '<circle cx="21" cy="19" r="7" fill="#e7c486"/><path d="M21 7v4M21 27v4M9 19h4M29 19h4M12.5 10.5l2.8 2.8M26.7 24.7l2.8 2.8M29.5 10.5l-2.8 2.8M15.3 24.7l-2.8 2.8" stroke="#e7c486" stroke-width="2.4" stroke-linecap="round"/>'
        '<path d="M6 33c5-3 10-3 15 0s10 3 15 0" stroke="#9fd0dc" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#0f5c6e"/>'
           '<circle cx="21" cy="19" r="7" fill="#e7c486"/><path d="M21 7v4M21 27v4M9 19h4M29 19h4M12.5 10.5l2.8 2.8M26.7 24.7l2.8 2.8M29.5 10.5l-2.8 2.8M15.3 24.7l-2.8 2.8" stroke="#e7c486" stroke-width="2.4" stroke-linecap="round"/>'
           '<path d="M6 33c5-3 10-3 15 0s10 3 15 0" stroke="#9fd0dc" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://medicareenrollmentflorida.com", domain="medicareenrollmentflorida.com", name="Medicare Enrollment Florida",
    org="ECOS Medicare Solutions", state="Florida", abbr="FL", demonym="Floridians",
    # TODO(Darin): swap for a Florida (305 / 407 / 813 / 904) number.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Georgia Medicare Enrollment", "https://georgiamedicareenrollment.com"), ("Tennessee Medicare Quotes", "https://www.tennesseemedicarequotes.com"),
             ("Minnesota Medicare Enrollment", "https://minnesotamedicareenrollment.com"), ("Texas Medicare Enrollment", "https://texasmedicareenrollment.com"),
             ("Medicare Enrollment Arizona", "https://www.medicareenrollmentarizona.com"), ("Medicare Enrollment Nevada", "https://medicareenrollmentnevada.com"),
             ("Colorado Medicare Enrollment", "https://coloradomedicareenrollment.com"), ("Medicare Enrollment Utah", "https://medicareenrollmentutah.com"), ("California Medicare Enrollment", "https://www.californiamedicareenrollment.com"),
             ("MyMedigapRate — Medigap rate research", "https://www.mymedigaprate.com"), ("MyECOS360 — Darin's author page", "https://www.myecos360.com/darin-weidauer")],
    sameas_org_extra=["https://howdoiapplyformedicare.com", "https://medicareadvantageanswers.com", "https://dentalinsurancetomorrow.com"],
    sameas_darin=["https://www.myecos360.com/darin-weidauer", "https://www.linkedin.com/in/darin-weidauer-3165a816b/", "https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ",
                  "https://www.medicareenrollmentarizona.com/about", "https://minnesotamedicareenrollment.com/about", "https://texasmedicareenrollment.com/about", "https://medicareenrollmentutah.com/about", "https://www.californiamedicareenrollment.com/about", "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or SHINE (Serving Health Insurance Needs of Elders, Florida&rsquo;s State Health Insurance Assistance Program, 1-800-963-5337) to get information on all of your options."),
    not_affiliated="the State of Florida, the Florida Department of Elder Affairs, the Agency for Health Care Administration, Florida Medicaid, or the Florida Office of Insurance Regulation",
    ship_name="Florida SHINE", ship_phone="1-800-963-5337",
    brand_tag="Plain-English Medicare help in Florida", theme_color="#0f5c6e",
    footer_tagline="Plain-English Medicare guidance for Florida retirees, new residents and people approaching 65. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping Florida retirees, new residents and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Jacksonville and the Panhandle to Miami and Naples.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and Florida Medicaid dual eligibility",
                 "Moving to Florida on Medicare", "Hurricane disaster Special Enrollment Periods", "Medicare for military retirees"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "My plan was discontinued", "I just moved to Florida", "Medicare Advantage", "Medicare Supplement (Medigap)",
                      "Part D drug plan", "I split the year between states", "I have VA / TRICARE", "I have Medicaid too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Moving to Florida, losing a plan, or a hurricane disaster declaration each open a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for cities and regions across Florida',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/new-to-florida">Moving to Florida &amp; snowbirds</a>', '<a href="/medicaid">Florida Medicaid and Medicare Savings Programs</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="beach", h1="Florida Medicare questions, answered plainly",
                  sub="The questions we hear most from Floridians &mdash; about plans dropping doctors, AvMed&rsquo;s exit, Medigap prices and issue-age rating, moving here from up north, hurricanes, TRICARE, and what any of this costs. Short answers, with links to the longer ones.",
                  title="Florida Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Floridians ask most: the 2026 Advantage changes, Medigap issue-age rating and under-65 rights, moving to Florida on Medicare, hurricane SEPs, SHINE, and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for Florida retirees, new residents and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, from Pensacola and Jacksonville through Orlando, Tampa Bay and The Villages to Miami, Naples and the Keys.",
    llm_facts=["Florida uses the federal Medigap plan letters (A–N), requires issue-age rating (premiums cannot rise because you get older) and prohibits attained-age rating; it has no birthday rule. Since 2009 Florida gives people under 65 on Medicare a six-month guaranteed-issue window when they enroll in Part B, and insurers must offer them at least one plan. The Office of Insurance Regulation regulates Medigap.",
               "More than half of Florida's Medicare beneficiaries are in Medicare Advantage. For the 2026 plan year AvMed left the Florida Medicare market (about 35,000 members), UnitedHealthcare reduced plans in Broward, Miami-Dade, Palm Beach, Hillsborough, Pinellas, Lee, Collier and other counties, and several carriers trimmed dental, vision and OTC extras. Florida Blue sells Advantage plans in every county.",
               "Florida's SHIP is SHINE (Serving Health Insurance Needs of Elders), run by the Florida Department of Elder Affairs through the Area Agencies on Aging: 1-800-963-5337 (the Elder Helpline).",
               "Florida Medicaid is administered by the Agency for Health Care Administration; eligibility is determined by the Department of Children and Families through ACCESS Florida (myaccessflorida.com). Long-term care runs through the Statewide Medicaid Managed Care Long-Term Care program, and Florida aligns D-SNPs with Medicaid plans. Medicare Savings Programs (QMB, SLMB, QI) are applied for through DCF and automatically qualify the enrollee for Part D Extra Help.",
               "A FEMA-declared disaster (hurricanes included) opens a Special Enrollment Period for people in the declared counties who missed an enrollment deadline because of it.",
               "Florida has the largest snowbird and new-retiree inflow in the country and major military-retiree communities around Jacksonville's naval bases, MacDill Air Force Base and the Pensacola–Eglin corridor; VA care runs through the Miami, West Palm Beach, Tampa (Haley), Bay Pines, Orlando and North Florida/South Georgia systems."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/new-to-florida", "New to Florida"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in Florida</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/new-to-florida">Moving to Florida &amp; snowbirds</a>', '<a href="/hurricanes">Hurricanes &amp; Medicare</a>', '<a href="/veterans">Veterans</a>',
                   '<a href="/medicaid">Florida Medicaid &amp; savings programs</a>', '<a href="/faq">Questions Floridians ask</a>', '<a href="/about">About Darin</a>',
                   '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://elderaffairs.org/programs-and-services/serving-health-insurance-needs-of-elders-shine/" rel="noopener">SHINE (Florida&rsquo;s SHIP)</a>, 1-800-963-5337',
                                    '<a href="https://www.floir.com" rel="noopener">Florida Office of Insurance Regulation</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a county network &mdash; the dominant choice in Florida, and the one that changed most for [[YEAR]].", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and works with any provider nationwide &mdash; Mayo Jacksonville, Moffitt, Cleveland Clinic, or your doctor back in Ohio.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Florida Medicaid.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="beach", title="Medicare Help in Florida [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Floridians and new residents: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, statewide.",
    eyebrow="Medicare made clear · Statewide in Florida",
    h1="Medicare in Florida, explained by someone who actually teaches it.",
    sub="Turning 65, just moved here, or re-shopping because your plan dropped your doctor? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in Florida (NPN 18580338)"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="Florida is different", different_h2="Three things about Medicare in Florida that the national websites gloss over",
    different_lede="Florida has more people on Medicare Advantage than any state but California, more new retirees arriving every year than anywhere, and Medigap rules that reward buying early. Start with what actually shapes the choice here.",
    different_cards=[
        ("The Advantage market moved under your feet", "AvMed left for 2026, UnitedHealthcare cut plans across South Florida, Tampa Bay and the Gulf Coast, and extras were trimmed almost everywhere. A discontinued plan opens a Special Enrollment Period and, usually, a guaranteed-issue right to Medigap.", "/medicare-advantage", "What changed, and what to do"),
        ("Medigap is issue-age rated here", "Florida requires issue-age pricing: your premium cannot rise because you got older, only with the carrier&rsquo;s filed increases. It rewards buying at 65 and punishes waiting. Florida also guarantees a Medigap window to people under 65.", "/medicare-supplement", "Why the age you buy matters"),
        ("You brought your Medicare with you", "Moving from New York, Ohio or Minnesota changes your county, your plan menu, and sometimes your Medigap rights. The move itself opens a Special Enrollment Period; use it well.", "/new-to-florida", "Medicare for new Floridians"),
    ],
    options_h2="Four ways Floridians get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your county and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you spend the year. These are the situations Floridians ask us about most.",
    situations=[
        ("New to Florida &amp; snowbirds", "What a move does to your plan, which plans work when you split the year, and why your Medigap rights may differ from up north.", "/new-to-florida", "Moving to Florida on Medicare"),
        ("Hurricanes &amp; Medicare", "What a FEMA disaster declaration does to your enrollment deadlines, and how to keep prescriptions filled when you evacuate.", "/hurricanes", "Hurricanes &amp; Medicare"),
        ("Veterans &amp; military retirees", "TRICARE For Life, the VA (Miami, Tampa, Bay Pines, Orlando, Gainesville, West Palm), and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Florida Medicaid", "The Medicare Savings Programs that pay your Part B premium, Extra Help, SMMC long-term care, and the D-SNPs that coordinate both.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the Florida-specific choices in front of you, and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Florida retirees, new residents and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with Floridians by phone and video across all 67 counties. Find Medicare guidance for your city:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("My Florida Medicare Advantage plan was discontinued or dropped my doctor. What now?", "You are not alone: AvMed left the Florida Medicare market for 2026 and UnitedHealthcare cut plans in many counties. A non-renewal notice gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending. A dropped doctor mid-year is harder; call us and we will check whether a Special Enrollment Period applies."),
        ("Why are Medigap premiums so high in Florida, and what is issue-age rating?", "Florida requires issue-age rating: your premium is set by the age at which you buy and cannot rise because you got older, only with the carrier&rsquo;s filed increases. Insurers price that promise in, and Florida&rsquo;s claims costs are high, so premiums run above most states. The rule rewards buying at 65 and holding the policy."),
        ("I just moved to Florida. Do I have to change my Medicare plan?", "Medicare Advantage, Part D and most Medigap decisions are tied to your county of residence. Moving to Florida gives you a Special Enrollment Period to pick plans sold here; a Medigap policy from another state usually stays in force but may be re-rated. If you came from a state with continuous Medigap guaranteed issue, such as New York or Connecticut, your rights here are different. Our new-to-Florida guide walks through it."),
        ("I have VA or TRICARE benefits. Do I still need Medicare?", "Often, yes. VA health care and Medicare do not coordinate with each other, and TRICARE For Life requires you to have Medicare Parts A and B. Enrolling in Part B on time matters even with VA care, because VA medical coverage is not creditable for Part B and the late penalty lasts for life. Our Veterans page explains how these benefits fit together."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Florida, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and SHINE (1-800-963-5337) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your county and your calendar together.",
)

OG = dict(line1="Medicare help in", line2="Florida", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Statewide, by phone or video.", domain="medicareenrollmentflorida.com", mark="sun",
          palette=dict(primary=(15, 92, 110), dark=(10, 63, 76), gold=(231, 196, 134), paper=(246, 242, 232), sky=(217, 233, 238),
                       far=(201, 214, 217), mid=(122, 154, 74), green=(58, 122, 90)))
