"""Hawaii topic pages, part B: turning 65, neighbor islands, veterans, Med-QUEST, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_DCCA_MEDIGAP, SRC_SHIP_HI, SRC_SHIP_NAT, SRC_U65,
                              SRC_KP_2026, SRC_KP_SOB, SRC_HMSA_NI, SRC_HMSA_TRAVEL, SRC_HMSA_VISITOR, SRC_MQ_APPLY, SRC_MQ_PROGRAMS, SRC_MQ_QI,
                              SRC_EUTF_B, SRC_EUTF_FAQ, SRC_PHCA, SRC_TFL, SRC_VA, SRC_VAPIHCS, SRC_OVS, SRC_DVIDS, SRC_CMS_MAUI, SRC_AHEC,
                              SRC_AMBULANCE, SRC_KUPUNA_CG, SRC_KUPUNA_CARE, SRC_ADRC, SRC_HHSC, SRC_QUEENS, SRC_MAUIHEALTH, SRC_KP_LAHAINA)
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, state by state", "https://www.mymedigaprate.com/switching-medigap-plans")
SRC_MMR_T65 = ("MyMedigapRate: turning 65 in Hawaii", "https://www.mymedigaprate.com/turning-65/hawaii")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in Hawaii guide", crumb="Turning 65", scene="diamondhead",
     title="Turning 65 in Hawaii: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Hawaii: your 7-month enrollment window, the Medigap open enrollment that does not repeat, EUTF retirees and Part B, the Prepaid Health Care Act and working past 65, Kaiser or HMSA, and a checklist. Free help from a licensed Hawaii agent.",
     llm="Turning 65 in Hawaii: enrollment windows, the parts of Medicare, EUTF Part B rules for state and county retirees, still-working rules under the Prepaid Health Care Act, the Kaiser-or-HMSA choice, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Hawaii: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Hawaii, where the right answer for a Kaiser family in Mililani is not the right answer for an EUTF retiree in Hilo.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you have Part B. In Hawaii it does not repeat: there is no birthday rule and no annual switching window.",
               "Retiring from the State, the DOE, UH or a county? EUTF requires you to enroll in Part B and send proof within 60 days, then reimburses the premium. A late penalty is never reimbursed.",
               "Still working with employer coverage under the Prepaid Health Care Act? If the employer has 20 or more employees you can usually delay Part B without penalty and get a Special Enrollment Period later; under 20, Medicare pays first and you should enroll.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Hawaii twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
<h2>1. Your enrollment window: the 7-month Initial Enrollment Period</h2>
<p>Your Initial Enrollment Period (IEP) is seven months long: the three months <em>before</em> the month you turn 65, your birthday month, and the three months <em>after</em>. Signing up in the three months before your birthday means coverage starts the first of your birthday month. You enroll through Social Security (online at ssa.gov, by phone, or at the Honolulu, Hilo, Kahului or Lihue office); if you already draw Social Security you are enrolled in A and B automatically.</p>
<ul>
<li><strong>Part A</strong> (hospital) is premium-free for most people, so most enroll when first eligible.</li>
<li><strong>Part B</strong> (medical) carries the $202.90 standard monthly premium in [[YEAR]] &mdash; and a timing decision if you are still working (see below).</li>
</ul>
<h2>2. The parts of Medicare, briefly</h2>
<ul>
<li><strong>Part A</strong> &mdash; inpatient hospital, skilled nursing, hospice.</li>
<li><strong>Part B</strong> &mdash; doctors, outpatient care, preventive services.</li>
<li><strong>Part C (Medicare Advantage)</strong> &mdash; a private all-in-one alternative that bundles A, B and usually drug coverage, sold by county. In Hawaii that mostly means Kaiser Senior Advantage or HMSA Akamai Advantage.</li>
<li><strong>Part D</strong> &mdash; prescription drug coverage.</li>
<li><strong>Medigap</strong> &mdash; a supplement that pairs with A and B and works with any Medicare provider on any island or the mainland. It does not work at Kaiser.</li>
</ul>
<h2>3. Your big decision: two paths</h2>
<table class="ctable">
<caption>The two ways most people in Hawaii put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider that accepts Medicare, on any island or the mainland; predictable costs; monthly premiums. Not Kaiser.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a network that is either Kaiser&rsquo;s own system or HMSA&rsquo;s (or a national carrier&rsquo;s), sold island by island.</td></tr>
</tbody></table>
<p>Where you get care tilts the answer. If your doctors are Kaiser doctors and you want to keep them, the path is Kaiser Senior Advantage, and its service area is Honolulu County, most of Hawaii County and the island of Maui. If your doctors are at Queen&rsquo;s, Hawaii Pacific Health, the public hospitals or in independent practice, you have a real choice between HMSA or a national Advantage plan and Original Medicare with a supplement. On Kauai, Molokai and Lanai, and for anyone who flies to Oahu or the mainland for specialty care, a Medigap policy&rsquo;s any-provider access is often the practical answer; our <a href="/neighbor-islands">Neighbor Islands guide</a> goes through it. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above, and in Hawaii it does not repeat. Our research site sets the two side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/hawaii">turning 65 in Hawaii</a>.</p>
<h2>4. Retiring from the state or a county: what EUTF requires</h2>
<div class="note-box"><p>The Hawaii Employer-Union Health Benefits Trust Fund covers retirees of the State, the Department of Education, the University of Hawaii and the counties &mdash; a large share of everyone turning 65 in Hawaii. Its rules are specific. <strong>You must enroll in Medicare Part B when you become eligible</strong> (Hawaii Revised Statutes &sect;87A-23) and send EUTF proof of enrollment within 60 days, or your EUTF retiree medical and drug plans are cancelled. In return, <strong>EUTF reimburses your Part B premium</strong>: retirees hired before July 1, 2023 are reimbursed the premium and any IRMAA surcharge; retirees hired on or after that date are reimbursed the standard premium only. EUTF never reimburses a late-enrollment penalty. Your EUTF Medicare plan (Kaiser Senior Advantage or the HMSA retiree plan, depending on what you chose) is then your coverage; we help you understand what it includes and whether anything else makes sense alongside it.</p></div>
<h2>5. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are enrolled in Part B &mdash; during it no Hawaii insurer can turn you down or charge more for your health, at any age. Afterward, insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>6. Still working at 65?</h2>
<p>Hawaii&rsquo;s Prepaid Health Care Act requires employers to provide health coverage to employees who work 20 or more hours a week, so most people working at 65 have an employer plan. Whether you can delay Part B without penalty depends on the federal rule: if the employer has <strong>20 or more employees</strong>, the employer plan pays first and you can usually delay Part B and get an eight-month Special Enrollment Period when you stop working; if it has <strong>fewer than 20</strong>, Medicare pays first and you should enroll in Parts A and B at 65 to avoid gaps. A retiree plan or COBRA does not count as active employment. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll.</p>
<h2>7. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage &mdash; and if you are an EUTF retiree, enroll and send the proof.</li>
<li>Decide whether you are staying with Kaiser (Senior Advantage) or choosing between HMSA, a national plan and a Medigap policy.</li>
<li>Check that your doctors and prescriptions are covered before you enroll, and that the plan reaches the island you get specialty care on.</li>
<li>If you live on a neighbor island or travel to the mainland, read the <a href="/neighbor-islands">Neighbor Islands guide</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Med-QUEST, see <a href="/medicaid">Med-QUEST and the Medicare Savings Programs</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help people across Hawaii sort through it every day &mdash; clearly, patiently, and at no cost to you. Hawaii SHIP (1-888-875-9229) offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("I am retiring from the State of Hawaii. Do I have to take Part B?", "Yes. EUTF retiree medical plans require you to enroll in Medicare Part B when you become eligible and to send EUTF proof within 60 days, or the plan is cancelled. EUTF reimburses the Part B premium for eligible retirees (and IRMAA for those hired before July 1, 2023), but never a late penalty."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If your employer has 20 or more employees, the employer plan pays first and you may delay Part B without penalty and get a Special Enrollment Period later. If it has fewer than 20, Medicare pays first and you should enroll at 65. Confirm the size before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Hawaii?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, island, travel and budget. If you want to keep Kaiser, Senior Advantage is the answer. If you use Queen&rsquo;s, Hawaii Pacific Health or the public hospitals, or fly for specialty care, we compare HMSA and the national plans against a Medigap policy with you."),
           ("What is different about turning 65 in Hawaii?", "Three things. Kaiser and HMSA cover most of the state, so which system your doctors belong to comes first. Your island decides the plan menu and how far you travel for specialists. And a large share of people reach 65 as EUTF retirees, military retirees with TRICARE For Life, or veterans using the VA, each with rules of their own.")],
     sources=[SRC_CMS, SRC_EUTF_FAQ, SRC_EUTF_B, SRC_PHCA, SRC_DCCA_MEDIGAP, SRC_KP_SOB, SRC_SHIP_HI, SRC_MMR_T65], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Hawaii"),

dict(slug="neighbor-islands", nav_title="Medicare on the neighbor islands and traveling for care", crumb="Neighbor Islands", scene="napali",
     title="Medicare on the Neighbor Islands: Flying to Oahu or the Mainland for Care | ECOS Medicare Solutions",
     desc="Which Medicare plans work when the specialist is on Oahu or the mainland: Medigap travels anywhere, HMSA's neighbor island plans include interisland travel help, Kaiser refers within Kaiser, and what to check on Kauai, Molokai, Lanai, Maui and Hawaii Island.",
     llm="Medicare for neighbor island residents (Hawaii Island, Maui, Molokai, Lanai, Kauai) who fly to Oahu or the mainland for care: which plans travel, HMSA interisland travel benefit, Kaiser referrals, air ambulance, moving between islands, mainland transplants, kupuna caregiving",
     eyebrow="Guide · When care is a flight away", h1="Medicare on the neighbor islands, and when the specialist is on Oahu",
     sub="Hawaii Island, Maui, Molokai, Lanai and Kauai each have a hospital or two and a plane ticket for the rest. Here is which plans follow you to Queen&rsquo;s, Straub, Kaiser Moanalua or a mainland cancer center &mdash; and which stop at the shoreline.",
     keyfacts=["A Medigap policy with Original Medicare works with any provider in the U.S. that accepts Medicare, on any island or the mainland, with no referral or travel rule. It is the simplest interisland coverage there is. It does not cover Kaiser.",
               "HMSA&rsquo;s neighbor island Akamai Advantage plans (Standard and Standard Plus, PPOs) include help with interisland travel when HMSA determines the specialty care you need is not available on your island and refers you to a participating specialist elsewhere. Kaiser Senior Advantage refers members within Kaiser, usually to Oahu; its service area does not include Kauai, Molokai or Lanai.",
               "Hawaii was short 833 full-time-equivalent physicians in 2025 according to the University of Hawaii&rsquo;s workforce report, with the largest gaps on the neighbor islands; Maui County has the highest primary-care shortage in the state.",
               "Medicare Part B covers medically necessary emergency ambulance transport, including air ambulance when ground transport cannot get you to the care you need; you pay 20% after the deductible with Original Medicare, which a Medigap policy covers.",
               "Moving your permanent residence to another island, or to Hawaii from the mainland, opens a Special Enrollment Period. A federally declared disaster &mdash; the August 2023 Maui wildfires triggered one &mdash; does too."],
     body="""<p>Most of the state&rsquo;s subspecialists work on Oahu, and a lot of the rest work in Seattle, San Francisco or Los Angeles. A resident of Hilo, Kihei, Kaunakakai or Kapaa can expect that some of their care will involve an airport. The Medicare rules are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>Which plans travel</h2>
<table class="ctable">
<caption>How each plan type behaves once you leave your home island. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Care on another island</th><th scope="col">Care on the mainland</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Medigap</th><td>Any provider that accepts Medicare, no referral; the supplement pays its share the same as at home</td><td>Same &mdash; any Medicare provider in the country</td></tr>
<tr><th scope="row">HMSA Akamai Advantage (neighbor island PPO)</th><td>In-network providers statewide; interisland travel help when HMSA refers you off-island for care not available at home</td><td>Out-of-network costs, except in states covered by HMSA&rsquo;s visitor/traveler program, where in-network costs apply</td></tr>
<tr><th scope="row">Kaiser Permanente Senior Advantage</th><td>Care within Kaiser; referral to Kaiser on Oahu for what your island&rsquo;s Kaiser office does not provide</td><td>Emergencies and urgent care; some Kaiser regions honor visiting-member arrangements &mdash; ask before you travel</td></tr>
<tr><th scope="row">National-carrier Advantage HMO/PPO</th><td>Per the plan&rsquo;s network and rules; HMOs generally require in-network care</td><td>Emergencies only on most HMOs; PPOs cover out-of-network at higher cost</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Same; check that a preferred pharmacy exists where you are going</td></tr>
</tbody></table>
<div class="note-box"><p><strong>Read the actual travel benefit, not the brochure.</strong> HMSA&rsquo;s interisland travel help applies when HMSA determines the care is not available on your island from a participating provider and refers you; it is not a general airfare benefit. Kaiser&rsquo;s referrals stay inside Kaiser. If a travel benefit is the reason you are choosing a plan, we get it in writing from the Evidence of Coverage before you enroll.</p></div>
<h2>Island by island</h2>
<ul>
<li><strong>Hawaii Island.</strong> Hilo Benioff Medical Center and Kona Community Hospital are the public acute-care hospitals; Queen&rsquo;s North Hawaii in Waimea is a rural hospital in the Queen&rsquo;s system; Kaiser has a Kona office and Senior Advantage covers most of the county. Subspecialty care often means Oahu. See <a href="/hilo">Hilo</a>, <a href="/kailua-kona">Kailua-Kona</a> and <a href="/waimea">Waimea</a>.</li>
<li><strong>Maui.</strong> Maui Memorial in Wailuku is the island&rsquo;s only acute-care hospital, run by Maui Health and open to all patients; Kaiser has offices in Maui Lani, Wailuku and Kihei and a temporary Lahaina clinic in Kaanapali while a permanent one is built. Kaiser Senior Advantage covers the island of Maui. See <a href="/kahului">Kahului</a>, <a href="/kihei">Kihei</a> and <a href="/lahaina">Lahaina</a>.</li>
<li><strong>Molokai and Lanai.</strong> Molokai General (Queen&rsquo;s) and Lanai Community Hospital (Maui Health) are small critical-access hospitals; complex cases leave by air. Kaiser Senior Advantage is not sold on either island. See <a href="/kaunakakai">Kaunakakai</a>.</li>
<li><strong>Kauai.</strong> Wilcox in Lihue (Hawaii Pacific Health), Kauai Veterans Memorial in Waimea and Samuel Mahelona in Kapaa; no Kaiser service area. Most specialty care is a flight to Honolulu. See <a href="/lihue">Lihue</a> and <a href="/kapaa">Kapaa</a>.</li>
</ul>
<h2>When it is an emergency: air ambulance</h2>
<p>Medicare Part B covers ambulance transport to the nearest appropriate facility when it is medically necessary and any other transport could endanger your health, and that includes air ambulance when ground transport cannot get you there fast enough or at all &mdash; the normal situation for a serious case on Molokai, Lanai or the rural ends of Hawaii Island. With Original Medicare you pay 20% of the Medicare-approved amount after the Part B deductible; a Medigap Plan G covers that 20%. Advantage plans cover emergency ambulance too, with their own copays. Non-emergency interisland travel for a scheduled appointment is a different thing: Original Medicare does not pay for the plane ticket, and only certain Advantage plans help.</p>
<h2>Moving between islands, or moving here</h2>
<p>Advantage and Part D plans are sold by county, and you must live in the plan&rsquo;s service area. Moving your permanent residence from Oahu to Kona, or from Maui to Molokai, ends a plan that does not serve the new county and opens a Special Enrollment Period to choose one that does. Moving to Hawaii from the mainland works the same way: an Advantage HMO from California or Washington generally covers only emergencies here, and changing your legal residence lets you pick from what is sold in your new county. A Medigap policy is different &mdash; once issued it stays in force wherever you live, though the premium may be re-rated. Our agency is licensed in Hawaii and fifteen other states, so we can move coverage cleanly in either direction; the state-by-state switching rules are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>
<h2>After a disaster</h2>
<p>The August 2023 Maui wildfires triggered a federal public health emergency, and CMS opened a Special Enrollment Period for people who could not enroll, disenroll or switch plans because of it, and required Part D plans to cover prescriptions at out-of-network pharmacies for displaced members. The same mechanism applies to any federally declared disaster or emergency in Hawaii. If a disaster changed where you live, where you get care or which pharmacy you use, tell us; the relief has dates and rules of its own.</p>
<h2>Caring for a kupuna at a distance</h2>
<p>A lot of the calls we get from the neighbor islands are from an adult child on Oahu or the mainland helping a parent in Hilo or Hanapepe. Two state programs are worth knowing alongside Medicare. <strong>Kupuna Care</strong>, run by the Executive Office on Aging through the county Aging and Disability Resource Centers, provides home-delivered meals, personal care, homemaker help, adult day care and transportation to help older adults stay at home. The <strong>Kupuna Caregivers Program</strong> helps working family caregivers &mdash; those employed 30 or more hours a week caring for someone 60 or older &mdash; with up to $70 a day toward those same services; it is not an entitlement, so funding limits apply. Both start with a call to the statewide ADRC at 808-643-2372. On the Medicare side, we help you understand a parent&rsquo;s plan, whether a <a href="/medicaid">Medicare Savings Program</a> could pay their Part B premium, and whether an <a href="/institutional-snp">Institutional SNP</a> fits if they are in a care home.</p>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so filling a prescription in Honolulu or Seattle is not a problem. Pricing can be: plans have <em>preferred</em> pharmacies where copays are lowest, and the preferred chain on Oahu may not have a store on Lanai. Mail order at 90-day supplies solves most of it. We check your island&rsquo;s pharmacies when we compare plans.</p>""",
     faqs=[("I live on Kauai and fly to Honolulu for a specialist. Which plan covers that?", "Original Medicare with a Medigap policy covers any provider that accepts Medicare, on any island, with no referral or travel rule. HMSA&rsquo;s neighbor island Akamai Advantage plans include interisland travel help when HMSA refers you to a participating specialist on another island. Kaiser Senior Advantage is not sold on Kauai. We read the plan&rsquo;s travel rules with you before you enroll."),
           ("Does Medicare pay for my flight to Oahu for an appointment?", "Original Medicare does not pay for non-emergency travel. It does cover medically necessary emergency ambulance transport, including air ambulance when ground transport cannot get you to care. Certain Advantage plans, including HMSA&rsquo;s neighbor island plans, help with interisland travel when they refer you off-island; the terms are plan-specific."),
           ("I have Kaiser on the Big Island. What happens when I need care Kaiser does not offer here?", "Kaiser refers you within Kaiser, usually to its Moanalua Medical Center and specialists on Oahu. Ask Kaiser what travel assistance applies to a referral; it is set by the plan, and we help you read it."),
           ("Can I get treatment on the mainland with a Hawaii plan?", "With Original Medicare and a Medigap policy, yes, at any provider that accepts Medicare. With an Advantage plan, emergencies are covered everywhere; routine or planned care on the mainland depends on the plan, and HMSA&rsquo;s visitor/traveler program extends in-network costs to a list of states. We confirm before you book."),
           ("I am moving from Oahu to Maui. What happens to my plan?", "Changing your permanent residence to another county opens a Special Enrollment Period. An Advantage or Part D plan that does not serve Maui County ends; you choose from what is sold there. A Medigap policy stays in force. We handle the switch.")],
     sources=[SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_HMSA_NI, SRC_HMSA_TRAVEL, SRC_HMSA_VISITOR, SRC_KP_SOB, SRC_AHEC, SRC_AMBULANCE, SRC_CMS_MAUI, SRC_KUPUNA_CARE, SRC_KUPUNA_CG, SRC_ADRC, SRC_HHSC, SRC_QUEENS, SRC_MAUIHEALTH, SRC_KP_LAHAINA, SRC_MMR_SWITCH], cta="Care on another island? Let&rsquo;s make sure your plan follows you."),

dict(slug="veterans", nav_title="Medicare for Hawaii veterans and military retirees", crumb="Veterans", scene="pearlharbor",
     title="Medicare for Hawaii Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Matsunaga VA at Tripler, the Akaka clinic in Kapolei, clinics in Hilo, Kona, Maui and Kauai) work with Medicare in Hawaii, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for Hawaii veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, the VA Pacific Islands Health Care System, Tripler, and the retiree communities around Pearl Harbor-Hickam, Schofield and Kaneohe Bay",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Hawaii veterans and military retirees",
     sub="Hawaii has more than 110,000 veterans and one of the largest military-retiree communities in the Pacific. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "The state Office of Veterans&rsquo; Services counts roughly 112,000&ndash;117,000 veterans in Hawaii: about 85,000 on Oahu, 16,000 on Hawaii Island, 11,000 in Maui County and 4,000 on Kauai. About 13,000 military retirees and 18,500 retiree family members are covered under TRICARE in Hawaii.",
               "VA care runs through the VA Pacific Islands Health Care System: the Spark M. Matsunaga VA Medical Center on the Tripler campus, the Daniel K. Akaka VA Clinic in Kapolei (opened 2024), and clinics in Hilo, Kailua-Kona, Maui and Kauai, with a VA physician on Molokai three days a week and visiting clinicians on Lanai.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Hawaii&rsquo;s veterans are concentrated where the bases are &mdash; Pearl Harbor and Hickam, Schofield Barracks and Wheeler, Marine Corps Base Hawaii at Kaneohe Bay &mdash; and scattered across every island. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
<div class="twocol">
<div class="panel panel--good"><h3>TRICARE For Life (TFL)</h3>
<ul>
<li>Requires you to have Medicare <strong>Part A and Part B</strong>.</li>
<li>Pays <strong>secondary</strong> to Medicare &mdash; it wraps around Medicare like a supplement.</li>
<li>TFL pharmacy is <strong>creditable</strong>, so a separate Part D plan is usually unnecessary.</li>
<li>TFL can pair with a Medicare Advantage plan; because drug coverage already exists, an <strong>MA-only plan</strong> (Advantage without Part D) can add dental or vision without duplicating your Rx.</li>
<li>Because TFL already fills Medicare&rsquo;s gaps, a Medigap policy is usually unnecessary too.</li>
</ul></div>
<div class="panel panel--note"><h3>VA health care</h3>
<ul>
<li>Separate from Medicare &mdash; the two <strong>do not coordinate</strong> and don&rsquo;t disrupt each other.</li>
<li>Medicare doesn&rsquo;t pay at VA facilities; the VA doesn&rsquo;t cover Medicare cost-sharing.</li>
<li>VA medical is <strong>not creditable</strong> for Part B &mdash; enroll in Part B on time to avoid a lifelong penalty.</li>
<li>VA pharmacy <strong>is creditable</strong> for Part D, so you can rely on it for drug coverage.</li>
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; Queen&rsquo;s, Straub or Kaiser with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Where VA care is in Hawaii</h2>
<p>The VA Pacific Islands Health Care System is based at the Spark M. Matsunaga VA Medical Center on the Tripler campus in Honolulu, where the VA shares inpatient care with Tripler Army Medical Center under a VA/DoD agreement. The Daniel K. Akaka VA Clinic in Kapolei, opened in April 2024, brought primary care, specialty care, imaging and urgent care to West Oahu. Community clinics serve Hilo, Kailua-Kona, Maui and Kauai; a VA physician sees patients at the Molokai Rural Health Center three days a week, and traveling clinicians visit Lanai. For a neighbor island veteran the practical point is that VA specialty care often means a flight to Honolulu, which is one more reason to hold Medicare alongside the VA for care closer to home.</p>
<h2>Military hospitals after 65</h2>
<p>Tripler Army Medical Center continues to see retirees on a space-available basis under TRICARE rules. Medicare does not pay there. Most Hawaii military retirees pair TFL with civilian care nearby, and we have pages for the three big retiree communities: <a href="/joint-base-pearl-harbor-hickam">Joint Base Pearl Harbor-Hickam</a>, <a href="/schofield-barracks">Schofield Barracks and Wheeler</a> and <a href="/marine-corps-base-hawaii">Marine Corps Base Hawaii</a>.</p>
<h2>Which Hawaii plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital on any island, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill. Kaiser members need Kaiser Senior Advantage to keep Kaiser.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Hawaii Office of Veterans&rsquo; Services, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care, which matters on an island where the VA clinic is small."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at Tripler or the Matsunaga VA?", "No. Medicare does not pay at military or VA facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_VAPIHCS, SRC_OVS, SRC_DVIDS, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Med-QUEST (Hawaii Medicaid): QUEST Integration, Medicare Savings Programs, Extra Help", crumb="Med-QUEST &amp; savings programs", scene="plantation",
     title="Medicare &amp; Med-QUEST (Hawaii Medicaid): QUEST Integration, QMB, SLMB | ECOS Medicare Solutions",
     desc="How Medicare works with Med-QUEST, Hawaii's Medicaid program: QUEST Integration for adults 65+, Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, Dual Special Needs Plans, and where to apply (mybenefits.hawaii.gov, 1-800-316-8005).",
     llm="Medicare and Med-QUEST (Hawaii Medicaid, dual eligible): QUEST Integration managed care, Medicare Savings Programs (QMB/SLMB/QI) through the Med-QUEST Division, Extra Help, D-SNPs, applying at mybenefits.hawaii.gov",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Med-QUEST: QUEST Integration and the Medicare Savings Programs",
     sub="If you qualify for both Medicare and Med-QUEST &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in Hawaii, and where to apply.",
     keyfacts=["Hawaii Medicaid is Med-QUEST, run by the Med-QUEST Division of the Department of Human Services. Adults 65 and over and people with disabilities who qualify get their benefits through QUEST Integration, a managed-care program that has covered aged, blind and disabled members alongside everyone else since 2015 and includes long-term services and supports.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. Income limits change each year and use Hawaii&rsquo;s higher federal poverty level. Apply at mybenefits.hawaii.gov, by phone at 1-800-316-8005, or at a Med-QUEST eligibility office.",
               "Qualifying for a Medicare Savings Program or Med-QUEST automatically qualifies you for Extra Help with Part D costs.",
               "Dual Special Needs Plans (D-SNPs) are Advantage plans for people with both Medicare and Med-QUEST; HMSA&rsquo;s Akamai Advantage Dual Care is one, and it is part of the state&rsquo;s Medicaid managed-care program. Free counseling: Hawaii SHIP, 1-888-875-9229."],
     body="""<p>Some people in Hawaii qualify for both Medicare and Med-QUEST &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Med-QUEST may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a care home.</p>
<h2>How Medicaid works for seniors in Hawaii</h2>
<p>Hawaii&rsquo;s Medicaid program is <strong>Med-QUEST</strong>, administered by the <strong>Med-QUEST Division of the Department of Human Services</strong>. Eligibility for adults 65 and over is based on income and resources under the state&rsquo;s aged-and-disabled rules, and it is determined by Med-QUEST &mdash; not by an insurance agency. You apply online at <strong>mybenefits.hawaii.gov</strong>, by phone at <strong>1-800-316-8005</strong>, or on paper at the Med-QUEST eligibility office on your island. Once eligible, you receive your benefits through <strong>QUEST Integration</strong>, Hawaii&rsquo;s Section 1115 managed-care program, in which a health plan coordinates Medicaid services, including long-term services and supports, while Medicare continues to pay first for medical care.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Income limits are set against Hawaii&rsquo;s federal poverty level, which is higher than the mainland&rsquo;s, and change each year. You apply through Med-QUEST, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Med-QUEST you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Med-QUEST benefits intact. In Hawaii, HMSA&rsquo;s Akamai Advantage Dual Care is a D-SNP that is part of the state&rsquo;s Medicaid managed-care program, so the two sides can be aligned; other carriers may offer D-SNPs on some islands.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from Hawaii SHIP &mdash; the Hawaii State Health Insurance Assistance Program, run by the Executive Office on Aging &mdash; at 1-888-875-9229. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Med-QUEST benefits working alongside Medicare. Eligibility decisions rest with Med-QUEST and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Med-QUEST, the Hawaii Department of Human Services, or the federal Medicare program.</p>""",
     faqs=[("What is QUEST Integration?", "Hawaii&rsquo;s Medicaid managed-care program, run by the Med-QUEST Division. Since 2015 it has covered adults 65 and over and people with disabilities alongside everyone else, with a health plan coordinating your Medicaid services, including long-term services and supports, while Medicare keeps paying first for your medical care."),
           ("Who counts as dual eligible in Hawaii?", "People who qualify for both Medicare and Med-QUEST. There are full and partial categories; eligibility is determined by the Med-QUEST Division and CMS, based on income and resources."),
           ("Can Med-QUEST pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply at mybenefits.hawaii.gov or 1-800-316-8005; Hawaii SHIP (1-888-875-9229) can help."),
           ("Where do I apply for Med-QUEST if I am over 65?", "Online at mybenefits.hawaii.gov, by phone at 1-800-316-8005, or on paper at the Med-QUEST eligibility office on your island.")],
     sources=[SRC_MQ_QI, SRC_MQ_PROGRAMS, SRC_MQ_APPLY, SRC_SHIP_HI, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Med-QUEST dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Hawaii", crumb="Chronic SNPs", scene="maunakea",
     title="Chronic SNPs (C-SNP) in Hawaii | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Hawaii: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Hawaii for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Hawaii",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Hawaii county and is thinner on the neighbor islands; a regular Advantage plan or a Medigap policy may still serve you better, and Kaiser members are served inside Kaiser.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. In Hawaii the number of C-SNPs is small and concentrated on Oahu; on the neighbor islands the honest comparison is usually against a regular Advantage plan, Kaiser Senior Advantage, or Original Medicare with a Medigap policy.</p>
<h2>Conditions that can qualify</h2>
<p>Medicare defines the chronic conditions a C-SNP can serve. Common examples include:</p>
<ul>
<li>Diabetes mellitus</li>
<li>Chronic heart failure and certain cardiovascular disorders</li>
<li>Chronic lung disorders such as COPD</li>
<li>End-stage renal disease (ESRD) requiring dialysis</li>
<li>Certain other qualifying chronic conditions</li>
</ul>
<p>You generally need a provider to verify that you have the qualifying condition in order to enroll, and a diagnosis gives you a Special Enrollment Period to join one outside the normal windows.</p>
<h2>What a C-SNP usually offers</h2>
<ul>
<li><strong>Care coordination</strong> tailored to your condition, often including a care team or coordinator.</li>
<li><strong>A drug formulary</strong> built with your condition&rsquo;s medications in mind, plus included Part D coverage.</li>
<li><strong>Extra benefits</strong> that vary by plan, and frequently a $0 or low plan premium.</li>
</ul>
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist or cardiologist is in it &mdash; and whether it reaches the island you see them on &mdash; applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. Dialysis patients on a neighbor island should ask specifically how the plan handles the dialysis center nearest home. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Med-QUEST.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Hawaii?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county, is thinner on the neighbor islands, and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Hawaii", crumb="Institutional SNPs", scene="koolau",
     title="Institutional SNPs (I-SNP) in Hawaii | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Hawaii for people in a care home or nursing facility, or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Med-QUEST, QUEST Integration and Kupuna Care.",
     llm="Institutional Special Needs Plans (I-SNP) in Hawaii for facility-level care, alongside QUEST Integration long-term services and the state Kupuna Care and Kupuna Caregivers programs",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Hawaii",
     sub="Medicare Advantage plans for people who live in a nursing facility or care home, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D. Availability in Hawaii is limited and concentrated on Oahu.",
               "In Hawaii, many people in long-term care also qualify for Med-QUEST through QUEST Integration, which covers long-term services and supports; a D-SNP aligned with the QUEST plan may then be the better fit, and we compare the two.",
               "For families keeping a kupuna at home, the state&rsquo;s Kupuna Care and Kupuna Caregivers programs (through the county ADRC, 808-643-2372) sit alongside Medicare, not inside it."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility or care home, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul>
<li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li>
<li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment.</li>
</ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers &mdash; a real consideration where the hospital is a flight away.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming, more so from another island. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP aligned with QUEST Integration</a> if Med-QUEST is paying for the care &mdash; patiently, and at no cost. If the plan is to keep your kupuna at home instead, the state&rsquo;s Kupuna Care program (meals, personal care, homemaker help, adult day care, transportation) and the Kupuna Caregivers Program (up to $70 a day toward those services for family caregivers who work 30 or more hours a week) both start with a call to the Aging and Disability Resource Center at 808-643-2372.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a>, <a href="/medicaid">Med-QUEST and the Medicare Savings Programs</a>, and the <a href="/neighbor-islands">Neighbor Islands guide</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Hawaii county, and is limited outside Oahu."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with QUEST Integration, and we do it by phone and video from any island.")],
     sources=[SRC_MA_GOV, SRC_MQ_QI, SRC_KUPUNA_CARE, SRC_KUPUNA_CG, SRC_ADRC], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="outrigger",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Hawaii agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Hawaii agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling a house or a rental, or converting an IRA, can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed, and the rules for public employees whose pensions come from outside Social Security.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Hawaii, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Hawaii. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Hawaii?", "The book covers Medicare and retirement decisions nationally. For Hawaii specifics &mdash; Kaiser and HMSA, EUTF, neighbor island care, Med-QUEST, the military communities &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
