"""North Carolina topic pages, part B: turning 65, moving to North Carolina, veterans, Medicaid, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_SEP_GOV, SRC_SHIIP, SRC_NCDOI_MEDIGAP, SRC_NCDOI_U65, SRC_NC_MEDICAID_APPLY,
                              SRC_MQB, SRC_DB101, SRC_TFL, SRC_VA, SRC_UNC_EXIT, SRC_SHP)
SRC_HELENE_SEP = ("NC Department of Insurance (Oct 4, 2024): Special Enrollment Period for Medicare recipients affected by Helene&rsquo;s damage", "https://www.ncdoi.gov/news/press-releases/2024/10/04/special-enrollment-period-medicare-recipients-affected-helenes-damage")
SRC_HELENE_NCSU = ("NC Cooperative Extension, Yancey County: Special Enrollment Period for Medicare recipients affected by Hurricane Helene (25 counties, through Feb 16, 2025)", "https://yancey.ces.ncsu.edu/2024/11/special-enrollment-period-for-medicare-recipients-affected-by-hurricane-helene")
SRC_MIL_TAX = ("Our NC Military (NC Department of Military and Veterans Affairs): military pension tax exemption", "https://ourncmilitary.nc.gov/blog/2022/02/25/military-pension-tax-exemption")
SRC_SS_TAX = ("SmartAsset: North Carolina retirement tax friendliness (Social Security exempt from state income tax)", "https://smartasset.com/retirement/north-carolina-retirement-taxes")
SRC_PINEHURST = ("GOBankingRates via AOL: Pinehurst named a top retirement hotspot (2025)", "https://www.aol.com/north-carolina-town-retirement-hotspot-174207738.html")
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, state by state", "https://www.mymedigaprate.com/switching-medigap-plans")
SRC_DMVA = ("NC Department of Military and Veterans Affairs: reports and statistics (veteran population)", "https://www.milvets.nc.gov/reports-and-statistics")
SRC_VA_FAY = ("VA Fayetteville Coastal health care", "https://www.va.gov/fayetteville-coastal-health-care/")
SRC_VA_SAL = ("VA Salisbury health care: about us (Salisbury VAMC, Charlotte and Kernersville Health Care Centers)", "https://www.va.gov/salisbury-health-care/about-us/")
SRC_VA_ASH = ("VA Asheville health care (Charles George VA Medical Center)", "https://www.va.gov/asheville-health-care/")
SRC_VA_DUR = ("VA Durham health care", "https://www.va.gov/durham-health-care/")
SRC_FT_BRAGG = ("U.S. Army (2025): Fort Liberty becomes Fort Bragg, renamed for Battle of the Bulge hero", "https://www.army.mil/article/283622/fort_liberty_becomes_fort_bragg_renamed_for_battle_of_bulge_hero")
SRC_WOMACK = ("Womack Army Medical Center: about us", "https://womack.tricare.mil/About-Us")
SRC_NMCCL = ("Naval Medical Center Camp Lejeune", "https://camp-lejeune.tricare.mil/")
SRC_SJAFB = ("4th Medical Group, Seymour Johnson AFB: about us", "https://seymourjohnson.tricare.mil/About-Us")
SRC_TAILORED = ("NC Medicaid: Behavioral Health and I/DD Tailored Plans", "https://medicaid.ncdhhs.gov/tailored-plans")
SRC_TP_FACT = ("NC Medicaid: Tailored Plan information for beneficiaries (fact sheet)", "https://medicaid.ncdhhs.gov/documents/tailored-plan-member-fact-sheet/open")
SRC_EXPANSION = ("NCDHHS (Dec 1, 2025): North Carolina celebrates two years of Medicaid expansion", "https://www.ncdhhs.gov/news/press-releases/2025/12/01/north-carolina-celebrates-two-years-medicaid-expansion")
SRC_ABD = ("Buncombe County HHS: Medicaid for age 65 &amp; older, blind, or disabled", "https://www.buncombenc.gov/421/Medicaid-for-Age-65-Older-Blind-or-Disab")
SRC_PACE = ("NC Medicaid: Program of All-Inclusive Care for the Elderly (PACE)", "https://medicaid.ncdhhs.gov/providers/programs-and-services/long-term-care/program-all-inclusive-care-elderly-pace")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in North Carolina guide", crumb="Turning 65", scene="blueridge",
     title="Turning 65 in North Carolina: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in North Carolina: your 7-month enrollment window, the Medigap open enrollment that does not repeat, State Health Plan and still-working rules, the deadlines with lifelong penalties, and a checklist. Free help from a licensed NC agent.",
     llm="Turning 65 in North Carolina: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap by county and hospital system, State Health Plan retirees, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in North Carolina: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for North Carolina, where the right answer in Wake County is not always the right answer in Hyde County.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In North Carolina it does not repeat: there is no birthday rule and no annual switching window.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later. Retiring state employees and teachers move to the State Health Plan&rsquo;s Medicare plans and need Parts A and B in place.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the North Carolina twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
<h2>1. Your enrollment window: the 7-month Initial Enrollment Period</h2>
<p>Your Initial Enrollment Period (IEP) is seven months long: the three months <em>before</em> the month you turn 65, your birthday month, and the three months <em>after</em>. Signing up in the three months before your birthday means coverage starts the first of your birthday month. You enroll through Social Security (online at ssa.gov, by phone, or at an office); if you already draw Social Security you are enrolled in A and B automatically.</p>
<ul>
<li><strong>Part A</strong> (hospital) is premium-free for most people, so most enroll when first eligible.</li>
<li><strong>Part B</strong> (medical) carries the $202.90 standard monthly premium in [[YEAR]] &mdash; and a timing decision if you are still working (see below).</li>
</ul>
<h2>2. The parts of Medicare, briefly</h2>
<ul>
<li><strong>Part A</strong> &mdash; inpatient hospital, skilled nursing, hospice.</li>
<li><strong>Part B</strong> &mdash; doctors, outpatient care, preventive services.</li>
<li><strong>Part C (Medicare Advantage)</strong> &mdash; a private all-in-one alternative that bundles A, B and usually drug coverage, sold by county.</li>
<li><strong>Part D</strong> &mdash; prescription drug coverage.</li>
<li><strong>Medigap</strong> &mdash; a supplement that pairs with A and B and works anywhere in the country.</li>
</ul>
<h2>3. Your big decision: two paths</h2>
<table class="ctable">
<caption>The two ways most North Carolinians put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly.</td></tr>
</tbody></table>
<p>Where you live, and which hospital system you use, tilt the answer. In Charlotte, the Triangle and the Triad the Advantage menu is deep, but the systems contract selectively: for 2026 UNC Health is out of network with Humana, WellCare and Cigna Advantage plans, and CarolinaEast in New Bern left Blue Cross NC&rsquo;s. In the mountains, the Outer Banks and the farm counties the menu is short and the nearest specialist may be in Virginia or Tennessee, and a Medigap policy&rsquo;s any-provider access is often the practical choice. If Duke, UNC or Mayo is in your future, a supplement removes the network question entirely. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above, and in North Carolina it does not repeat. Our research site sets the two side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/north-carolina">turning 65 in North Carolina</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no North Carolina insurer can turn you down or charge more for your health. Afterward, North Carolina insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. North Carolina&rsquo;s big employers &mdash; the state and the universities, the school districts, the hospital systems, the banks in Charlotte, the Research Triangle companies &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll.</p>
<p>State employees and teachers have a specific path: at retirement the State Health Plan moves Medicare-eligible retirees to its Humana Group Medicare Advantage plans, and it requires Medicare Parts A and B to be in place. Whether to stay on that group plan or choose an individual plan is a separate question; ask us and we will lay both out with the plan&rsquo;s own documents.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find out how deep the Advantage menu is in your county, and whether your hospital system is in the plans you are considering for [[YEAR]].</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if a specific system is your care.</li>
<li>If you just moved here, read <a href="/moving-to-north-carolina">Moving to North Carolina</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid or limited income, see <a href="/medicaid">NC Medicaid and the MQB programs</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help North Carolinians sort through it every day &mdash; clearly, patiently, and at no cost to you. NC SHIIP (855-408-1212), with volunteer counselors in all 100 counties, offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in North Carolina?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget and county. The Advantage menu is deep in the big metros and thin in the mountains and on the coast, and the big hospital systems contract selectively. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in North Carolina?", "Which hospital system your doctors belong to decides more than the premium does, and 2026 showed why when UNC Health left three Advantage networks. Your Medigap open enrollment does not repeat in North Carolina, so using it well matters. And a large share of North Carolinians reach 65 with TRICARE For Life, VA care or the State Health Plan, each of which changes the calculation.")],
     sources=[SRC_CMS, SRC_NCDOI_MEDIGAP, SRC_SHIIP, SRC_UNC_EXIT, SRC_SHP], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in North Carolina"),

dict(slug="moving-to-north-carolina", nav_title="Medicare when you move to North Carolina", crumb="Moving to North Carolina", scene="riverport",
     title="Moving to North Carolina on Medicare: Relocation SEP &amp; What Travels | ECOS Medicare Solutions",
     desc="Retiring to Pinehurst, Brunswick County, the Triangle, Lake Norman or the mountains from another state? The relocation Special Enrollment Period, what happens to a Medigap policy, the birthday-rule states you may be leaving, TRICARE moves, and the hurricane rule on the coast.",
     llm="Medicare when you move to North Carolina from another state: the relocation Special Enrollment Period for Advantage and Part D, keeping or replacing a Medigap policy, leaving a birthday-rule state, State Health Plan and TRICARE moves, and disaster Special Enrollment Periods after hurricanes",
     eyebrow="Guide · New to the state", h1="Moving to North Carolina on Medicare",
     sub="Whether you are retiring to a golf course in Moore County, a beach town in Brunswick County, a grandchild in Cary or a mountain in Watauga, the rule is the same: some of your coverage follows you and some stops at the state line. Here is which is which.",
     keyfacts=["Moving outside your Medicare Advantage or Part D plan&rsquo;s service area opens a Special Enrollment Period: tell the plan before you move and the window runs from the month before through two full months after; tell it afterward and it runs the month you tell them plus two more.",
               "A Medigap policy with Original Medicare works with any provider in the U.S. that accepts Medicare and stays in force when you move; the premium may be re-rated to North Carolina. North Carolina has no birthday rule, so if you are leaving a state that has one, decide before you go.",
               "North Carolina does not tax Social Security benefits, and since 2021 has exempted qualifying military retirement pay from state income tax &mdash; two reasons so many people move here at exactly the age Medicare rules start to bite.",
               "A FEMA-declared disaster opens another Special Enrollment Period. After Hurricane Helene, 25 western counties had one through February 16, 2025; the coast has had them after hurricanes before."],
     body="""<p>North Carolina is a destination state now: Pinehurst tops national best-places-to-retire lists, Brunswick County&rsquo;s beach towns keep landing on them, and the Triangle, Lake Norman, Asheville and the High Country draw retirees from the Northeast, the Midwest and Florida. Most of them arrive already on Medicare, and the plan they bring usually does not work here beyond emergencies. The rules are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>Which coverage travels</h2>
<table class="ctable">
<caption>How each plan type behaves once you have moved to North Carolina.</caption>
<thead><tr><th scope="col">What you have</th><th scope="col">After the move</th><th scope="col">What to do</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare (A &amp; B)</th><td>Unchanged &mdash; Medicare is federal</td><td>Update your address with Social Security</td></tr>
<tr><th scope="row">Medigap policy</th><td>Stays in force; any provider that accepts Medicare, here or anywhere</td><td>Tell the insurer; expect the premium to be re-rated to your new ZIP code. Keep it unless a cheaper equivalent is worth underwriting for</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>Ends when you leave its service area (emergencies covered meanwhile)</td><td>Use the relocation Special Enrollment Period to pick a plan sold in your new county, or return to Original Medicare</td></tr>
<tr><th scope="row">Standalone Part D</th><td>Ends when you leave its service area</td><td>Same Special Enrollment Period; choose around your pharmacy here</td></tr>
<tr><th scope="row">Employer or State retiree plan</th><td>Depends on the plan &mdash; many group Advantage plans are national PPOs</td><td>Ask the former employer before you move; leaving some group plans is one-way</td></tr>
</tbody></table>
<h2>The relocation Special Enrollment Period</h2>
<p>Medicare Advantage and Part D plans are sold by county, and you must live in the plan&rsquo;s service area. Moving to North Carolina from another state, or from one North Carolina county to another where your plan is not sold, opens a Special Enrollment Period. If you tell your plan before you move, the window starts the month before the move and runs two full months after it; if you tell them after, it starts the month you tell them and runs two more months. During it you choose from the plans sold in your new county &mdash; and the menu in Moore County looks nothing like the one you left in Bergen County. We compare what is actually offered at your new ZIP code, confirm the local hospital system is in it, and check your pharmacy.</p>
<div class="note-box"><p><strong>If you are leaving a state with a birthday rule.</strong> California, Oregon, Illinois and about a dozen other states let Medigap policyholders switch carriers each year without health questions. North Carolina does not. Your existing Medigap policy comes with you and keeps working, but once you are a North Carolina resident, changing it means underwriting unless you are inside a federal guaranteed-issue window. If you have been meaning to switch to a cheaper carrier, do it under your old state&rsquo;s rule before you change your residence. Our research site lists each state&rsquo;s rule: <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p></div>
<h2>Residency, and what counts as a move</h2>
<p>A season at the beach does not change your plan; most Advantage plans allow six months out of area, some twelve. What changes it is moving your legal residence &mdash; a North Carolina driver&rsquo;s licence, voter registration, filing as a resident. That ends your old Advantage or Part D plan and starts the window above. Two-home households should pick the state they will actually file from and enroll there.</p>
<h2>Why so many people move here at 65</h2>
<p>North Carolina does not tax Social Security benefits, and since the 2021 tax year has exempted qualifying military retirement pay and survivor benefits from state income tax, which is part of why Fort Bragg and Camp Lejeune retirees stay and why retirees from the Northeast keep arriving. Other retirement income is taxed at the state&rsquo;s flat rate. None of that changes your Medicare, but it does change the arithmetic on IRMAA if a house sale or a Roth conversion comes with the move; see <a href="/medicare-costs">costs &amp; IRMAA</a>.</p>
<h2>Military moves</h2>
<p>TRICARE For Life is national, so a military retiree moving to Fayetteville, Jacksonville or Goldsboro keeps it unchanged; Womack, the Naval Medical Center and the Seymour Johnson clinic see retirees on a space-available basis. If you had a Medicare Advantage plan layered on TFL in your old state, the relocation window is when to decide whether one is worth having here. See <a href="/veterans">Veterans</a> and our base pages.</p>
<h2>The hurricane rule</h2>
<p>When FEMA declares an emergency or major disaster, Medicare opens a Special Enrollment Period for people who live in the declared area (or rely on someone who does) and missed another enrollment window because of it; it runs through two full months after the incident period ends. Hurricane Helene produced one for 25 western North Carolina counties, through February 16, 2025, and coastal hurricanes have produced them before. If a storm hits after you arrive and you missed a deadline in the chaos, call us and we will confirm whether the window is open.</p>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so a prescription fills the same in Southport as it did in Cleveland. Pricing can differ: plans have <em>preferred</em> pharmacies where copays are lowest, and the chain that was preferred up north may not be the one on your corner here. We check your new ZIP code when we compare plans.</p>
<p>Our agency is licensed in North Carolina and fifteen other states, so we can move your coverage cleanly in either direction &mdash; and if you are coming from Georgia, Tennessee, South Carolina, Ohio or Indiana, we have a sister site for the state you are leaving.</p>""",
     faqs=[("I moved to North Carolina from another state. Does my Medicare Advantage plan still work?", "For emergencies and urgent care, yes &mdash; every plan covers those anywhere in the U.S. For routine care, no, once you have left the service area, and moving your residence ends the plan. The relocation Special Enrollment Period lets you pick a plan sold in your new county or return to Original Medicare."),
           ("Does my Medigap policy from another state work in North Carolina?", "Yes. A Medigap policy pays alongside Original Medicare with any provider in the country that accepts Medicare, with no network and no service area, and it stays in force when you move. Tell the insurer your new address; the premium may be re-rated to North Carolina."),
           ("How long is the Special Enrollment Period when I move?", "If you notify your plan before the move, from the month before through two full months after it. If you notify them after, the month you tell them plus two more full months. Missing it means waiting for the October 15 to December 7 Annual Election Period."),
           ("I am coming from a state with a Medigap birthday rule. Should I switch before I move?", "If you want a cheaper carrier for the same plan letter, yes &mdash; use your old state&rsquo;s rule before you become a North Carolina resident. North Carolina has no birthday rule, so switching here later usually means medical underwriting."),
           ("Can you help me if I am moving the other way, out of North Carolina?", "Yes. Our agency is licensed in North Carolina and fifteen other states, so we help you move your coverage cleanly, including the Medigap switching rules that differ by state.")],
     sources=[SRC_SEP_GOV, SRC_MEDIGAP_GOV, SRC_NCDOI_MEDIGAP, SRC_MMR_SWITCH, SRC_HELENE_SEP, SRC_HELENE_NCSU, SRC_MIL_TAX, SRC_SS_TAX, SRC_PINEHURST], cta="Moving to North Carolina? Let&rsquo;s make sure your coverage arrives with you."),

dict(slug="veterans", nav_title="Medicare for North Carolina veterans and military retirees", crumb="Veterans", scene="longleaf",
     title="Medicare for North Carolina Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Durham, Fayetteville, Salisbury, Asheville) work with Medicare in North Carolina, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for North Carolina veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, the four North Carolina VA medical centers, and the retiree communities around Fort Bragg, Camp Lejeune and Seymour Johnson AFB",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for North Carolina veterans and military retirees",
     sub="North Carolina has the eighth-largest veteran population in the country and the fourth-largest military one. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "North Carolina VA care runs through four medical centers &mdash; Durham, Fayetteville, the W.G. (Bill) Hefner VA in Salisbury (with Charlotte and Kernersville Health Care Centers) and the Charles George VA in Asheville &mdash; plus dozens of community clinics.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>North Carolina is home to more than 615,000 veterans and the retiree communities of Fort Bragg, Camp Lejeune, Marine Corps Air Station Cherry Point and Seymour Johnson Air Force Base. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; Duke, UNC or Atrium with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Where the VA is in North Carolina</h2>
<p>Four VA medical centers cover the state. The <strong>Durham VA</strong> serves the Triangle and reaches east with clinics toward Greenville and Goldsboro. The <strong>Fayetteville Coastal VA</strong> serves the Fort Bragg and Camp Lejeune country and the coast down to Wilmington, with clinics in Jacksonville and Wilmington. The <strong>W.G. (Bill) Hefner VA in Salisbury</strong> serves the Charlotte metro and the Triad through its two Charlotte Health Care Centers and the Kernersville Health Care Center. The <strong>Charles George VA in Asheville</strong> serves 49,000 veterans across 23 mountain counties. Each is a separate system from the Medicare plan you choose, which is the point: keep both.</p>
<h2>Military hospitals after 65</h2>
<p>Womack Army Medical Center at Fort Bragg and Naval Medical Center Camp Lejeune continue to see retirees on a space-available basis under TRICARE rules; Seymour Johnson has an outpatient clinic, not a hospital. Medicare does not pay at any of them. Most North Carolina military retirees pair TFL with civilian care nearby, and we have pages for the three big retiree communities: <a href="/fort-bragg">Fort Bragg</a>, <a href="/camp-lejeune">Camp Lejeune</a> and <a href="/seymour-johnson-afb">Seymour Johnson AFB</a>.</p>
<h2>Which North Carolina plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at. North Carolina has also exempted qualifying military retirement pay from state income tax since 2021, which is one more reason so many retirees stay.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the North Carolina Department of Military and Veterans Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at Womack, the Naval Medical Center or the Durham VA?", "No. Medicare does not pay at military or VA facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_DMVA, SRC_VA_DUR, SRC_VA_FAY, SRC_VA_SAL, SRC_VA_ASH, SRC_FT_BRAGG, SRC_WOMACK, SRC_NMCCL, SRC_SJAFB, SRC_MIL_TAX, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + NC Medicaid: NC Medicaid Direct, Tailored Plans, the MQB programs, Extra Help", crumb="NC Medicaid &amp; MQB", scene="tobacco",
     title="Medicare &amp; NC Medicaid: MQB-Q, MQB-B, MQB-E, Extra Help | ECOS Medicare Solutions",
     desc="How Medicare works with NC Medicaid: NC Medicaid Direct and Tailored Plans for people with both, the MQB Medicare Savings Programs that pay the Part B premium, Extra Help, PACE, Dual Special Needs Plans, and where to apply (ePASS or your county DSS).",
     llm="Medicare and NC Medicaid (dual eligible): NC Medicaid Direct versus managed-care Standard and Tailored Plans, the MQB-Q/MQB-B/MQB-E Medicare Savings Programs through county DSS, Extra Help, PACE, D-SNPs, applying at ePASS",
     eyebrow="Your situation · Dual eligible", h1="Medicare and NC Medicaid: the MQB programs and how the two fit",
     sub="If you qualify for both Medicare and NC Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in North Carolina, and where to apply.",
     keyfacts=["NC Medicaid is administered by the North Carolina Department of Health and Human Services. People with both Medicare and Medicaid are excluded from the managed-care Standard Plans and are generally served through NC Medicaid Direct; Tailored Plans, launched July 1, 2024, serve people with significant behavioral-health, I/DD or traumatic-brain-injury needs.",
               "North Carolina&rsquo;s Medicare Savings Programs are labelled MQB: MQB-Q (the federal QMB), MQB-B (SLMB) and MQB-E (QI). They pay the Part B premium ($202.90 in [[YEAR]]) and, for MQB-Q, Medicare&rsquo;s deductibles and copays. Your county Department of Social Services decides eligibility; apply there or at ePASS.",
               "Qualifying for an MQB program or Medicaid automatically qualifies you for Extra Help with Part D costs.",
               "Dual Special Needs Plans (D-SNPs) are Advantage plans for people with both Medicare and Medicaid; PACE serves people 55 and over who need nursing-home-level care at home, at 14 sites across the state. Free counseling: NC SHIIP, 855-408-1212."],
     body="""<p>Some North Carolinians qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and NC Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in North Carolina</h2>
<p>NC Medicaid is administered by the <strong>North Carolina Department of Health and Human Services</strong>, and eligibility is decided by your <strong>county Department of Social Services</strong> &mdash; not by an insurance agency. North Carolina expanded Medicaid for adults 19 to 64 on December 1, 2023, but that expansion does not reach people 65 and over; for them, eligibility follows the aged, blind and disabled rules, with an income limit at the federal poverty level and a resource limit of $2,000 for one person. You apply online at <strong>ePASS</strong> (epass.nc.gov), by phone, or in person at the county DSS; the NC Medicaid Contact Center is 888-245-0179, and applications can take up to 45 days.</p>
<p>Once eligible, <em>how</em> you get Medicaid depends on your situation. Most North Carolinians on Medicaid are in managed-care <strong>Standard Plans</strong>, but people who also have Medicare are excluded from them and are served through <strong>NC Medicaid Direct</strong>, the state&rsquo;s fee-for-service program, with behavioral-health services through the regional LME/MCOs. People with significant mental-health, substance-use, intellectual or developmental disability, or traumatic-brain-injury needs &mdash; including dual eligibles on the Innovations or TBI waivers &mdash; are served by the <strong>Tailored Plans</strong> that launched July 1, 2024, which coordinate physical health, behavioral health and long-term services together. Medicare keeps paying first for medical care in either case.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs &mdash; the MQB programs.</strong> North Carolina labels them <strong>MQB-Q</strong> (the federal QMB), <strong>MQB-B</strong> (SLMB) and <strong>MQB-E</strong> (QI). All three pay the Part B premium ($202.90 in [[YEAR]]); MQB-Q also covers Medicare&rsquo;s deductibles, copays and coinsurance. Income and resource limits change each year and are set as a share of the federal poverty level. You apply through your county DSS, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MQB program or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact. They are a large part of the menu in Eastern North Carolina and the rural Piedmont.</li>
<li><strong>PACE</strong> &mdash; the Program of All-Inclusive Care for the Elderly &mdash; combines Medicare and Medicaid into one program of medical care, day services and support at home for people 55 and over who need a nursing-home level of care. North Carolina has 11 PACE organizations at 14 locations, each serving specific ZIP codes.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from NC SHIIP &mdash; the Seniors&rsquo; Health Insurance Information Program, a division of the North Carolina Department of Insurance, with volunteer counselors in all 100 counties &mdash; at 855-408-1212. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how an MQB program and Extra Help could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with your county DSS, NC Medicaid and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by NC Medicaid, the North Carolina Department of Health and Human Services, any county Department of Social Services, or the federal Medicare program.</p>""",
     faqs=[("What are MQB-Q, MQB-B and MQB-E?", "North Carolina&rsquo;s names for the three federal Medicare Savings Programs: MQB-Q is QMB, MQB-B is SLMB and MQB-E is QI. All three pay the Part B premium for people with limited income and resources; MQB-Q also pays Medicare&rsquo;s deductibles and copays. Your county Department of Social Services decides eligibility, and qualifying brings Part D Extra Help automatically."),
           ("Who counts as dual eligible in North Carolina?", "People who qualify for both Medicare and NC Medicaid. There are full and partial categories; eligibility is determined by the county DSS, NC Medicaid and CMS, based on income and resources."),
           ("Will I be in a Medicaid managed-care plan if I also have Medicare?", "Not a Standard Plan &mdash; people with both Medicare and Medicaid are excluded from those and are served through NC Medicaid Direct. If you have significant behavioral-health, I/DD or TBI needs, or are on the Innovations or TBI waiver, you may be in a Tailored Plan instead. Medicare pays first either way."),
           ("Where do I apply for Medicaid or an MQB program if I am over 65?", "At ePASS (epass.nc.gov), by phone, or at your county Department of Social Services; the NC Medicaid Contact Center is 888-245-0179. Medicaid expansion covers adults 19 to 64, so people 65 and over qualify under the aged, blind and disabled rules instead.")],
     sources=[SRC_NC_MEDICAID_APPLY, SRC_MQB, SRC_DB101, SRC_TAILORED, SRC_TP_FACT, SRC_EXPANSION, SRC_ABD, SRC_PACE, SRC_SHIIP, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and NC Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in North Carolina", crumb="Chronic SNPs", scene="piedmont",
     title="Chronic SNPs (C-SNP) in North Carolina | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in North Carolina: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in North Carolina for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in North Carolina",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by North Carolina county and is concentrated in the metros; a regular Advantage plan or a Medigap policy may still serve you better, especially if your specialist is at a system that has left the plan&rsquo;s network.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. North Carolina, with high rates of diabetes and heart disease in its eastern and rural counties, has C-SNPs in most of its metro markets.</p>
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist at Duke or your cardiologist at Atrium is in it applies &mdash; and in 2026 UNC Health left three Advantage networks &mdash; so a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and NC Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in North Carolina?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV, SRC_UNC_EXIT], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in North Carolina", crumb="Institutional SNPs", scene="blueridge",
     title="Institutional SNPs (I-SNP) in North Carolina | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in North Carolina for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with NC Medicaid and PACE.",
     llm="Institutional Special Needs Plans (I-SNP) in North Carolina for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in North Carolina",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In North Carolina, many people in long-term care also qualify for Medicaid through NC Medicaid Direct; a D-SNP, or PACE for people who can stay at home, may then be the better fit, and we compare them."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul>
<li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li>
<li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment.</li>
</ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP if NC Medicaid is paying for the care, or PACE</a> if staying at home is still possible &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">NC Medicaid, the MQB programs and PACE</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your North Carolina county; PACE is the other home-based option where a program serves your ZIP code."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP, a D-SNP or PACE coordinates with a facility and with NC Medicaid.")],
     sources=[SRC_MA_GOV, SRC_PACE], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="blueridge",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed North Carolina agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed North Carolina agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling the family land or the beach house, or converting an IRA, can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed federally, and the rules for teachers and state employees with a pension.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in North Carolina, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in North Carolina. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to North Carolina?", "The book covers Medicare and retirement decisions nationally. For North Carolina specifics &mdash; county-by-county Advantage menus, hospital-system networks, the MQB programs, TRICARE communities &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
