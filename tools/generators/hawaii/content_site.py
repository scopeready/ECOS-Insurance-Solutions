"""Hawaii site identity, home page, navigation. Tokens [[PHONE]] etc. are filled by generate.py."""
from datetime import date

TODAY = date(2026, 9, 13)
# Mark: a rising sun over an ocean swell — deep-ocean circle, plumeria-gold sun, sand wave.
LOGO = ('<svg class="brand__mark" width="42" height="42" viewBox="0 0 42 42" aria-hidden="true"><circle cx="21" cy="21" r="20" fill="#0d4f6c"/>'
        '<circle cx="21" cy="19" r="8" fill="#e7c486"/><path d="M5 27c5-5 11-5 16 0s11 5 16 0v8H5z" fill="#f7f3ea"/><path d="M5 30c5-4 11-4 16 0s11 4 16 0" stroke="#0d4f6c" stroke-width="2" fill="none"/></svg>')
FAVICON = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 42 42"><circle cx="21" cy="21" r="20" fill="#0d4f6c"/>'
           '<circle cx="21" cy="19" r="8" fill="#e7c486"/><path d="M5 27c5-5 11-5 16 0s11 5 16 0v8H5z" fill="#f7f3ea"/><path d="M5 30c5-4 11-4 16 0s11 4 16 0" stroke="#0d4f6c" stroke-width="2" fill="none"/></svg>')
ICON = lambda p: f'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">{p}</svg>'

SITE = dict(
    url="https://www.ecosinsurancesolutions.com/hawaii", domain="ecosinsurancesolutions.com/hawaii", name="Hawaii Medicare Enrollment",
    org="ECOS Medicare Solutions", state="Hawaii", abbr="HI", demonym="Hawaii residents",
    # TODO(Darin): replace with the Hawaii (808) number once he provides it. The agency's main line keeps the section from launching with a dead phone.
    phone="(702) 706-6564", tel="+17027066564", email="darinweidauer@ecos.care", npn="18580338",
    # Hawaii producer licence (same digits as the NPN); the engine shows it beside Darin's name site-wide.
    state_license="18580338", state_license_label="HI License",
    web3forms_key="fc793a1c-1dd6-4a2e-9078-e907c4ab0428", quote_url="https://planenroll.com/?purl=Darin-Weidauer",
    plan_year=2026, iso=TODAY.isoformat(), reviewed=TODAY.strftime("%B %-d, %Y"),
    fig=dict(partb="$202.90", partb_ded="$283", parta_ded="$1,736", partd_cap="$2,100", partd_ded="$615", partd_base="$38.99", irmaa_single="$109,000", irmaa_joint="$218,000"),
    network=[("Medicare Enrollment Arizona", "https://www.ecosinsurancesolutions.com/arizona"),
             ("California Medicare Enrollment", "https://www.ecosinsurancesolutions.com/california"),
             ("Colorado Medicare Enrollment", "https://www.ecosinsurancesolutions.com/colorado"),
             ("Medicare Enrollment Florida", "https://www.ecosinsurancesolutions.com/florida"),
             ("Georgia Medicare Enrollment", "https://www.ecosinsurancesolutions.com/georgia"),
             ("Indiana Medicare Enrollment", "https://www.ecosinsurancesolutions.com/indiana"),
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
                  "https://www.ecosinsurancesolutions.com/arizona/about", "https://www.ecosinsurancesolutions.com/california/about",
                  "https://www.ecosinsurancesolutions.com/minnesota/about", "https://www.ecosinsurancesolutions.com/texas/about", "https://www.ecosinsurancesolutions.com/utah/about",
                  "https://www.mymedigaprate.com/about"],
    tpmo=("We do not offer every plan available in your area. Any information we provide is limited to those plans we do offer in your area. "
          "Please contact Medicare.gov, 1-800-MEDICARE, or Hawaii SHIP (the Hawaii State Health Insurance Assistance Program, run by the State Executive Office on Aging, "
          "1-888-875-9229) to get information on all of your options."),
    not_affiliated="the State of Hawaii, the Hawaii Department of Human Services, the Med-QUEST Division (Hawaii Medicaid), or the Hawaii Insurance Division of the Department of Commerce and Consumer Affairs",
    ship_name="Hawaii SHIP", ship_phone="1-888-875-9229",
    brand_tag="Plain-English Medicare help in Hawaii", theme_color="#0d4f6c",
    footer_tagline="Plain-English Medicare guidance for Hawaii retirees and people approaching 65, on every island. Independent agency &mdash; we work for you, not a single carrier.",
    logo_svg=LOGO, favicon_svg=FAVICON,
    fonts_url="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&display=swap",
    org_description="Independent Medicare insurance agency helping Hawaii retirees and people approaching 65 compare Medicare Advantage, Medicare Supplement (Medigap), and Part D plans at no cost, from Honolulu and the Windward side to Hilo, Kona, Maui, Molokai, Lanai and Kauai.",
    knows_about=["Medicare Advantage", "Medicare Supplement", "Medigap", "Medicare Part D", "Special Needs Plans", "Medicare and Med-QUEST dual eligibility",
                 "Kaiser Permanente Senior Advantage and HMSA Akamai Advantage", "Neighbor island access to care", "Medicare for military retirees", "EUTF retiree Medicare rules"],
    interest_options=["I'm turning 65 soon", "Review my current plan", "Medicare Advantage", "Medicare Supplement (Medigap)", "Part D drug plan",
                      "I live on a neighbor island / I travel for care", "I'm an EUTF (state or county) retiree", "I have VA / TRICARE", "I have Med-QUEST (Medicaid) too"],
    enroll_note="Turning 65? Your Initial Enrollment Period is the 7 months around your birthday. Already on Medicare? The Annual Election Period is Oct 15&ndash;Dec 7, and Medicare Advantage Open Enrollment runs Jan 1&ndash;Mar 31. Moving to another island or losing a plan opens a Special Enrollment Period.",
    notfound_links=['<a href="/#areas">Areas we serve</a> &mdash; a Medicare guide for towns and islands across Hawaii',
                    '<a href="/medicare-costs">[[YEAR]] Medicare costs</a> &mdash; Part A, B, D and the IRMAA table',
                    '<a href="/medicare-advantage">Medicare Advantage</a> and <a href="/medicare-supplement">Medicare Supplement</a>',
                    '<a href="/part-d">Part D drug coverage</a>', '<a href="/turning-65">Turning 65</a> &mdash; your enrollment timeline',
                    '<a href="/neighbor-islands">Neighbor islands &amp; traveling for care</a>', '<a href="/medicaid">Med-QUEST, Medicare Savings Programs and Extra Help</a>',
                    '<a href="/veterans">Veterans and Medicare</a>'],
    faq_page=dict(scene="outrigger", h1="Hawaii Medicare questions, answered plainly",
                  sub="The questions we hear most from people in Hawaii &mdash; about Kaiser and HMSA, flying to Oahu for a specialist, EUTF and Part B, Medigap under 65, TRICARE For Life, Med-QUEST, and what any of this costs. Short answers, with links to the longer ones.",
                  title="Hawaii Medicare FAQ [[YEAR]] | ECOS Medicare Solutions",
                  desc="Plain answers to the Medicare questions Hawaii residents ask most: Kaiser vs HMSA, neighbor island care, EUTF retirees and Part B, Medigap under 65, TRICARE, Med-QUEST and 2026 costs."),
    llm_summary="Free, plain-English Medicare guidance for Hawaii retirees and people approaching 65. Compare Medicare Advantage, Medicare Supplement (Medigap) and Part D drug plans with a credentialed, independent agent at no cost. Statewide service by phone and video, on Oahu, Maui, Molokai, Lanai, Hawaii Island and Kauai.",
    llm_facts=["Darin Weidauer holds Hawaii insurance license #18580338 (NPN 18580338).",
               "Hawaii uses the federal Medigap plan letters (A–N) and has no birthday or anniversary switching rule; the Hawaii Insurance Division of the Department of Commerce and Consumer Affairs regulates Medigap. Hawaii requires insurers to offer every Medigap plan on a guaranteed-issue basis, at the same rates as at 65, during the six months after Part B begins, regardless of age — so people under 65 on Medicare because of a disability have the same Medigap window as everyone else.",
               "Hawaii is one of the most Medicare Advantage-heavy states in the country (KFF counts it among the states where 60% or more of eligible beneficiaries are in Advantage plans). Kaiser Permanente (Senior Advantage, an integrated system whose service area is Honolulu County, most of Hawaii County and the island of Maui) and HMSA (Akamai Advantage, Blue Cross Blue Shield of Hawaii, with separate Oahu and neighbor island plans) are the two largest. Medigap does not pay for care inside Kaiser; keeping Kaiser on Medicare means Kaiser Senior Advantage.",
               "Hawaii's SHIP is Hawaii SHIP, the Hawaii State Health Insurance Assistance Program, run by the Executive Office on Aging in the Department of Health: 1-888-875-9229 (Oahu 808-586-7299; TTY 1-866-810-4379).",
               "Hawaii Medicaid is Med-QUEST, run by the Med-QUEST Division of the Department of Human Services; adults 65+ and people with disabilities who qualify are served through the QUEST Integration managed-care program. Medicare Savings Programs (QMB, SLMB, QI) are handled by Med-QUEST and automatically qualify the enrollee for Part D Extra Help. Apply at mybenefits.hawaii.gov or 1-800-316-8005.",
               "Retired State of Hawaii and county employees on EUTF retiree plans must enroll in Medicare Part B when eligible (HRS 87A-23), and EUTF reimburses the Part B premium for eligible retirees.",
               "Hawaii has roughly 112,000–117,000 veterans (about 85,000 on Oahu) per the state Office of Veterans' Services, and around 13,000 military retirees under TRICARE. Tripler Army Medical Center, the Spark M. Matsunaga VA Medical Center on the Tripler campus, and the Daniel K. Akaka VA Clinic in Kapolei anchor military and veteran care, with VA clinics in Hilo, Kailua-Kona, Maui and Kauai.",
               "Neighbor island residents often fly to Oahu for specialty care. A Medigap policy with Original Medicare works with any Medicare provider on any island or the mainland; Advantage plans are island-specific, and HMSA's neighbor island plans include interisland travel help for approved treatment. The August 2023 Maui wildfires triggered a federal public health emergency and a Medicare Special Enrollment Period."],
)

NAV = [("/medicare-advantage", "Plans"), ("/medicare-supplement", "Medigap"), ("/medicare-costs", "2026 Costs"), ("/turning-65", "Turning 65"),
       ("/neighbor-islands", "Neighbor Islands"), ("/veterans", "Veterans"), ("/#areas", "Areas")]

FOOTER_COLS = [
    ("Plans", ['<a href="/medicare-advantage">Medicare Advantage</a>', '<a href="/medicare-supplement">Medicare Supplement (Medigap)</a>',
               '<a href="/part-d">Part D drug plans</a>', '<a href="/chronic-snp">Chronic SNPs</a>', '<a href="/institutional-snp">Institutional SNPs</a>']),
    ("Resources", ['<a href="/retirement-guide">Free retirement guide</a>', '<a href="/turning-65">Turning 65 in Hawaii</a>', '<a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA</a>',
                   '<a href="/neighbor-islands">Neighbor islands &amp; traveling for care</a>', '<a href="/veterans">Veterans</a>', '<a href="/medicaid">Med-QUEST &amp; savings programs</a>',
                   '<a href="/faq">Questions Hawaii residents ask</a>', '<a href="/about">About Darin</a>', '<a href="/privacy">Privacy</a> &middot; <a href="/terms">Terms</a>']),
    ("Official &amp; independent", ['<a href="https://www.medicare.gov" rel="noopener">Medicare.gov</a>', '<a href="tel:+18006334227">1-800-MEDICARE</a>',
                                    '<a href="https://www.hawaiiship.org" rel="noopener">Hawaii SHIP</a>, 1-888-875-9229',
                                    '<a href="https://cca.hawaii.gov/ins/" rel="noopener">Hawaii Insurance Division (DCCA)</a>',
                                    '<a href="https://medquest.hawaii.gov" rel="noopener">Med-QUEST (Hawaii Medicaid)</a>']),
]

PLACE_CARDS = [
    ("Medicare Advantage", "All-in-one Part C plans, often $0 premium, that use a local network &mdash; in Hawaii that usually means choosing between Kaiser, HMSA and a few national carriers, island by island.", "/medicare-advantage", "How Advantage works"),
    ("Medicare Supplement", "Medigap pairs with Original Medicare and lets you see any provider that accepts Medicare &mdash; Queen&rsquo;s, Straub, Hilo Benioff, or a specialist on the mainland.", "/medicare-supplement", "How Medigap works"),
    ("Part D drug plans", "Standalone drug coverage chosen around your medications and pharmacy. [[YEAR]] out-of-pocket cap: $2,100.", "/part-d", "How Part D works"),
    ("Special Needs Plans", "Advantage plans built for a chronic condition, for nursing-facility care, or for people with both Medicare and Med-QUEST.", "/chronic-snp", "About SNPs"),
]

HOME = dict(
    scene="diamondhead", title="Medicare Help in Hawaii [[YEAR]] | ECOS Medicare Solutions",
    desc="Free, plain-English Medicare help for Hawaii: Medicare Advantage, Medigap and Part D compared by a credentialed independent agent, on Oahu, Maui, Hawaii Island and Kauai.",
    eyebrow="Medicare made clear · Every island in Hawaii",
    h1="Medicare in Hawaii, explained by someone who actually teaches it.",
    sub="Turning 65, retiring from the state or the county, or wondering whether your plan still covers the specialist you fly to Oahu for? Sit down with a credentialed independent agent who will walk you through Medicare Advantage, Medigap and Part D in plain English &mdash; patiently, and at no cost to you.",
    trust=[(ICON('<path d="M12 2l8 4v6c0 5-3.5 8.5-8 10-4.5-1.5-8-5-8-10V6z"/>'), "Licensed in Hawaii &middot; HI License #18580338 &middot; NPN 18580338"),
           (ICON('<path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c0 1 3 3 6 3s6-2 6-3v-5"/>'), "Gerontologist &amp; RSSA&reg;"),
           (ICON('<circle cx="12" cy="8" r="5"/><path d="M8 13l-2 9 6-4 6 4-2-9"/>'), "22-year U.S. Air Force veteran"),
           (ICON('<path d="M20 6L9 17l-5-5"/>'), "Always free to you")],
    different_eyebrow="Hawaii is different", different_h2="Three things about Medicare in Hawaii that the national websites gloss over",
    different_lede="Hawaii has two health plans that most of the state already belongs to, an ocean between most residents and the nearest specialist, and one of the highest Medicare Advantage enrollment rates in the country. Start with what is actually for sale on your island.",
    different_cards=[
        ("Kaiser or HMSA decides more than the premium", "Most of Hawaii gets care through Kaiser Permanente&rsquo;s own clinics and Moanalua Medical Center, or through HMSA&rsquo;s network of Queen&rsquo;s, Hawaii Pacific Health and independent doctors. Medigap does not pay inside Kaiser; keeping Kaiser on Medicare means Kaiser Senior Advantage. Which system you use decides the shortlist before price does.", "/medicare-advantage", "How Advantage works in Hawaii"),
        ("Your island decides your menu", "Advantage plans are sold by county, and Kaiser Senior Advantage&rsquo;s service area is Honolulu County, most of Hawaii Island and the island of Maui. On Kauai, Molokai and Lanai the choice is shorter, and specialty care is often a flight away. A Medigap policy works at any Medicare provider on any island or the mainland.", "/neighbor-islands", "Neighbor islands &amp; traveling for care"),
        ("Retirees with rules of their own", "State and county retirees on EUTF must take Part B and get the premium reimbursed. Oahu&rsquo;s military retirees reach 65 with TRICARE For Life waiting, and veterans who use the Matsunaga VA or the Akaka clinic still need Part B on time. Each is a different calculation.", "/veterans", "Veterans &amp; Medicare"),
    ],
    options_h2="Four ways people in Hawaii get covered",
    options_lede="There is no single &ldquo;best&rdquo; plan &mdash; only the one that fits your doctors, your prescriptions, your island and your travel. Here is the plain-English version of your choices.",
    situations_lede="The rules change a lot depending on what else you have and where you get your care. These are the situations Hawaii residents ask us about most.",
    situations=[
        ("Neighbor islands &amp; traveling for care", "Which plans follow you to Queen&rsquo;s or Straub from Hilo, Lihue or Kaunakakai, what HMSA&rsquo;s interisland travel benefit actually covers, and when a Medigap policy is the safer bet.", "/neighbor-islands", "Neighbor island Medicare"),
        ("EUTF retirees", "Retiring from the state, the DOE, UH or a county? EUTF requires Part B, reimburses the premium, and has a 60-day proof deadline that catches people. What to do and when.", "/turning-65", "Turning 65 &amp; EUTF"),
        ("Veterans &amp; military retirees", "TRICARE For Life, Tripler, the Matsunaga VA, the Akaka clinic in Kapolei &mdash; and why Part B timing still matters.", "/veterans", "Veterans &amp; Medicare"),
        ("Medicare + Med-QUEST", "QUEST Integration, the Medicare Savings Programs that pay your Part B premium, and Dual Special Needs Plans that coordinate both.", "/medicaid", "Dual-eligible help"),
    ],
    guide_p="A clear, step-by-step walk-through of your enrollment windows, the Hawaii-specific choices in front of you &mdash; Kaiser or HMSA, EUTF, neighbor island care &mdash; and the deadlines that carry a lifelong penalty if you miss them. No sign-up required.",
    author_html=("<p>Darin Weidauer (HI License #18580338) is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Hawaii retirees and people approaching 65 make sense of their options &mdash; clearly, patiently, and with no cost to them. A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine and a Master&rsquo;s in Long-Term Care from USC, and became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>"
                 "<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education through one-on-one reviews, no-cost workshops, and his book <em>Retire With Confidence</em>. <a href=\"/about\">More about Darin &rarr;</a></p>"),
    areas_lede="We work with people on every island by phone and video. Find Medicare guidance for your town:",
    bases_lede="Near a base? We help military retirees and veterans coordinate TRICARE, VA care and Medicare:",
    faqs=[
        ("How much does it cost to work with ECOS Medicare Solutions?", "There is no cost to you. Independent Medicare agents are paid by the insurance carriers when you enroll, so our help comparing plans, answering questions, and reviewing your coverage each year is free. Your plan premium is the same whether you enroll with our help or on your own."),
        ("I have Kaiser now. Can I keep it when I go on Medicare?", "Yes, through Kaiser Permanente Senior Advantage, Kaiser&rsquo;s own Medicare Advantage plan. Kaiser is an integrated system, so a Medigap policy does not pay for care inside it; if you want to keep your Kaiser doctors, Senior Advantage is the way. Its service area is Honolulu County, most of Hawaii County and the island of Maui, so we check that your island and your ZIP code are inside it."),
        ("I live on a neighbor island and fly to Oahu for a specialist. Which plan covers that?", "Original Medicare with a Medigap policy covers any provider that accepts Medicare, on any island or the mainland, with no referral or travel rule. HMSA&rsquo;s neighbor island Akamai Advantage plans include help with interisland travel when HMSA refers you to a specialist on another island; Kaiser refers within its own system. We read the plan&rsquo;s travel rules with you before you enroll."),
        ("When can I enroll in or change my Medicare plan in Hawaii?", "Most people first enroll during their Initial Enrollment Period, the seven months around their 65th birthday. After that, the Annual Election Period runs October 15 to December 7 each year, and the Medicare Advantage Open Enrollment Period runs January 1 to March 31. Moving to another island, losing a plan, or qualifying for Med-QUEST opens a Special Enrollment Period."),
        ("I am retiring from the State of Hawaii. What does EUTF require?", "EUTF retiree medical plans require you to enroll in Medicare Part B when you become eligible and to send EUTF proof within 60 days, or the retiree plan is cancelled. EUTF then reimburses eligible retirees for the Part B premium. We walk through the timing so nothing lapses."),
        ("Do you offer every Medicare plan available in my area?", "No &mdash; and we will always be upfront about that. We represent a number of insurance organizations and products in Hawaii, not all of them. The easiest next step is to call us at [[PHONE]] and we will walk through what fits you. To compare every option on your own, Medicare.gov, 1-800-MEDICARE, and Hawaii SHIP (1-888-875-9229) have the complete list."),
    ],
    cta_h2="Let&rsquo;s find the plan that fits your life on your island.",
    cta_lede="A short, friendly conversation &mdash; no pressure, no cost. We&rsquo;ll look at your doctors, your prescriptions, your island and your travel together.",
)

OG = dict(line1="Medicare help in", line2="Hawaii", sub1="Plain-English, no-cost guidance from a licensed independent agent,",
          sub2="gerontologist and Air Force veteran. Every island, by phone or video.", domain="ecosinsurancesolutions.com/hawaii", mark="sun",
          palette=dict(primary=(13, 79, 108), dark=(8, 58, 82), gold=(231, 196, 134), paper=(247, 243, 234), sky=(213, 232, 238),
                       far=(180, 208, 214), mid=(96, 150, 140), green=(63, 107, 74)))

# Home-page photo band (served from <state>/img/, kept across rebuilds by tools/build_state.py)
HERO_PHOTO = {'src': '/img/hero-hawaii-1600.webp', 'src_sm': '/img/hero-hawaii-800.webp', 'alt': 'A couple wearing plumeria leis at a clifftop lookout above Hanalei Bay on Kauai', 'pos': '50% 60%'}
