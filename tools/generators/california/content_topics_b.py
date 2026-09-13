"""California topic pages, part B: costs, turning 65, moving, wildfires, veterans, Medi-Cal, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_HICAP, SRC_INS_CODE, SRC_CHA_OE, SRC_CHA_RULES, SRC_DHCS_ASSET, SRC_JIA,
                              SRC_DHCS_MMP, SRC_DHCS_DSNP, SRC_CHA_MEDICAL, SRC_CMS_FIRE, SRC_CMS_CAPHE, SRC_SEP, SRC_TFL, SRC_VA)
from costs_page import costs_page
SRC_CALPERS = ("CalPERS: Medicare requirements for retirees and CalPERS Medicare health plans", "https://www.calpers.ca.gov/page/retirees/health-and-medicare/medicare")
SRC_AZ = ("Medicare Enrollment Arizona (sister site with Mesa and Sun City offices)", "https://www.medicareenrollmentarizona.com")
SRC_NV = ("Medicare Enrollment Nevada (sister site)", "https://medicareenrollmentnevada.com")
SRC_TX = ("Texas Medicare Enrollment (sister site)", "https://texasmedicareenrollment.com")
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, the rules state by state", "https://www.mymedigaprate.com/switching-medigap-plans")

TOPICS_B = [
costs_page("sierra",
    "In California the usual surprises are the sale of a house that tripled in value, a business sale, stock options exercised in a last working year, or a Roth conversion two years back.",
    "Possibly. California&rsquo;s Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through your county Medi-Cal office; HICAP (1-800-434-0222) can walk you through it. Note that an asset limit ($130,000 for one person) returned on January 1, 2026. See our Medicare + Medi-Cal page.",
    [SRC_CMS, SRC_COSTS, SRC_DHCS_ASSET]),

dict(slug="turning-65", nav_title="Turning 65 in California guide", crumb="Turning 65", scene="coast",
     title="Turning 65 in California: Medicare Enrollment Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in California: your seven-month enrollment window, Kaiser or not, Medigap open enrollment and the birthday rule, CalPERS rules, Part B while still working, and the deadlines with lifelong penalties. Free help from a licensed California agent (CA License #0M00978).",
     llm="Turning 65 in California: the Initial Enrollment Period, the Kaiser decision, Medigap open enrollment and the birthday rule, CalPERS retirees, working past 65, late penalties",
     eyebrow="Your situation · Turning 65", h1="Turning 65 in California: what to do, and when",
     sub="Seven months to enroll, one six-month window to buy any Medigap policy without health questions, a Kaiser decision most Californians have to make, and a few deadlines that carry a lifelong penalty. Here is the order to do things in.",
     keyfacts=["Your Initial Enrollment Period runs seven months: the three months before your 65th birthday month, that month, and the three after. Enroll in the first three for coverage to start the month you turn 65.",
               "If you are already collecting Social Security, Parts A and B start automatically. If not, you enroll through Social Security; nobody enrolls you.",
               "Your Medigap open enrollment is the six months after Part B begins at 65: any plan, any carrier, no health questions. After that, California&rsquo;s birthday rule lets you switch to equal or lesser benefits each year, but a first purchase may be underwritten.",
               "Still working with employer coverage from an employer with 20 or more employees? You can usually delay Part B without penalty and get a Special Enrollment Period later. CalPERS retirees must enroll in Part B and move to a CalPERS Medicare plan."],
     body="""<h2>Your enrollment timeline</h2>
<div class="timeline">
<div class="tl"><strong>3 months before your birthday month</strong><p>Enroll in Parts A and B through Social Security (ssa.gov or 1-800-772-1213) unless you are already receiving Social Security, in which case your card arrives automatically. Decide the <a href="/kaiser">Kaiser question</a>: staying in Kaiser means Senior Advantage; leaving means Original Medicare with Medigap, or a non-Kaiser Advantage plan.</p></div>
<div class="tl"><strong>Your birthday month</strong><p>Part B starts on the first of the month. Your six-month Medigap open enrollment begins now. Your Advantage or Part D election can take effect the same day.</p></div>
<div class="tl"><strong>3 months after</strong><p>The Initial Enrollment Period closes. Enrolling in Part B in these last months delays your start date. Missing it entirely, without creditable employer coverage, adds a permanent 10%-per-year penalty.</p></div>
<div class="tl"><strong>63 days after any creditable drug coverage ends</strong><p>The Part D clock: go 63 or more days without creditable coverage and a permanent penalty begins to accrue.</p></div>
<div class="tl"><strong>Every year, for 60 days from your birthday</strong><p>California&rsquo;s Medigap birthday rule: switch your supplement to any carrier&rsquo;s plan of equal or lesser benefits with no health questions. Mark it on the calendar; we do.</p></div>
</div>
<h2>Still working at 65?</h2>
<p>If you or your spouse are actively working and the employer has 20 or more employees, that group plan pays first and you can delay Part B without penalty, then use an eight-month Special Enrollment Period when the job or coverage ends. Employer plans with fewer than 20 employees generally pay <em>secondary</em> to Medicare, so you usually need Part B at 65. Note that COBRA and retiree coverage do not count as active employment. HSA contributions must stop before Part A begins (Part A is retroactive up to six months when you enroll later, which trips up a lot of people).</p>
<h2>CalPERS retirees: a different menu</h2>
<p>If your retiree health coverage comes through CalPERS, the rules are set by CalPERS: you must enroll in Medicare Parts A and B when eligible and then transfer into a CalPERS Medicare health plan (Kaiser Senior Advantage, the UnitedHealthcare and Anthem/Blue Shield Medicare plans, PERS Platinum and others, depending on the year). Many State and CSU retirees are reimbursed for part or all of their Part B premium. The individual-market plans on this site are separate from that menu. We can still explain Medicare itself, Part B timing and IRMAA plainly, and help you understand how the CalPERS options compare.</p>
<h2>The three decisions</h2>
<ol>
<li><strong>Kaiser or not.</strong> This comes first in California, because it closes or opens every other door. <a href="/kaiser">Our Kaiser page</a> lays it out honestly.</li>
<li><strong>Original Medicare plus Medigap and Part D, or Medicare Advantage.</strong> Freedom to use any doctor in the country versus a medical group with lower upfront costs and extras. <a href="/medicare-supplement">Medigap</a> and <a href="/medicare-advantage">Advantage</a> pages explain each.</li>
<li><strong>Which company and plan.</strong> Compared at your ZIP code against your doctors, their medical group, and your prescriptions.</li>
</ol>
<div class="note-box"><p><strong>The one thing not to do:</strong> assume you can buy Medigap later. Outside your six-month open enrollment, a guaranteed-issue event, or the birthday rule (which covers switching, not a first purchase), California insurers can ask health questions. If you might ever want a supplement, the cheapest time to buy one is at 65.</p></div>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65 in California?", "Enroll during the three months before your birthday month so coverage starts the month you turn 65. Your Initial Enrollment Period lasts seven months in total."),
           ("Does California have a Medigap birthday rule for people turning 65?", "The birthday rule is for people who already have a Medigap policy and want to switch. At 65, your six-month open enrollment is broader: any plan, any carrier, no health questions. Buy in that window; use the birthday rule to re-shop in later years."),
           ("I am retiring through CalPERS. What is different?", "CalPERS requires you to enroll in Medicare Parts A and B when eligible and move into a CalPERS Medicare plan to keep your CalPERS coverage; many State and CSU retirees get Part B reimbursed. Those plans are separate from the individual-market plans on this site."),
           ("What happens if I miss my Medicare enrollment deadline?", "Without creditable employer coverage, you wait for the General Enrollment Period (Jan 1&ndash;Mar 31) and pay a permanent Part B penalty of 10% for each full year you delayed. Part D has its own permanent penalty after 63 days without creditable coverage.")],
     sources=[SRC_MEDIGAP_GOV, SRC_INS_CODE, SRC_CHA_OE, SRC_CALPERS, SRC_HICAP], cta="Turning 65 soon? Let&rsquo;s map your timeline together.", about="Turning 65 and enrolling in Medicare in California"),

dict(slug="moving", nav_title="Moving to or from California on Medicare (Arizona, Nevada, Texas, Idaho, and the reverse)", crumb="Moving", scene="desert",
     title="Moving To or From California on Medicare | Arizona, Nevada, Texas &amp; Back | ECOS Medicare Solutions",
     desc="Leaving California for Arizona, Nevada, Texas, Idaho or Oregon on Medicare, or arriving here: the Special Enrollment Period a move opens, what happens to Medigap and its birthday rule, Kaiser across state lines, and Part D. One agency licensed on both sides of the move.",
     llm="Moving to or from California on Medicare: the move Special Enrollment Period, Medigap portability and losing the birthday rule, Kaiser in other states, Part D, and sister agencies in Arizona, Nevada, Texas, Utah, Colorado and Florida",
     eyebrow="Your situation · Moving", h1="Moving to or from California on Medicare",
     sub="More retirees leave California every year than arrive, mostly for Arizona, Nevada, Texas and Idaho &mdash; and a move changes your county, your plan menu, and sometimes your Medigap rights. The same agency is licensed on both ends of most of those moves.",
     keyfacts=["A permanent move outside your plan&rsquo;s service area opens a Special Enrollment Period to pick a Medicare Advantage or Part D plan sold at your new address, generally the month before through two months after the move.",
               "A Medigap policy travels with you: it works with Original Medicare anywhere in the country, and the carrier re-rates it to your new state. What does not travel is California&rsquo;s birthday rule. Arizona, Nevada and Texas have no equivalent, so a Medigap change there usually means underwriting.",
               "Kaiser Senior Advantage does not follow you to a state without Kaiser. Leaving Kaiser country means starting over with new doctors, and the move SEP is the moment to choose between Medigap and a new Advantage plan.",
               "Arriving in California from a state with continuous guaranteed issue (New York, Connecticut) or a different birthday rule (Oregon, Nevada&rsquo;s narrower version): California&rsquo;s rules now apply, including its 60-day birthday rule for anyone who already holds a Medigap policy."],
     body="""<h2>Leaving California</h2>
<p>Your Advantage or Part D plan is tied to your county, so a permanent move outside its service area ends it and opens a Special Enrollment Period to enroll in a plan sold where you land. Tell your plan the move date, and use the window; it closes two months after you move.</p>
<ul>
<li><strong>Arizona.</strong> A deep Advantage market in Maricopa and Pima, thin in rural counties, no birthday rule, and a large Kaiser-free landscape: if you were in Senior Advantage, you will be choosing new doctors either way. <a href="https://www.medicareenrollmentarizona.com" rel="noopener">Our Arizona agency</a> has offices in Mesa and Sun City.</li>
<li><strong>Nevada.</strong> Nevada has its own birthday rule, but it is narrower than California&rsquo;s and reaches only carriers with open blocks; a Medigap policy you hold from California continues, re-rated. <a href="https://medicareenrollmentnevada.com" rel="noopener">Our Nevada site</a> covers Las Vegas, Henderson and Reno.</li>
<li><strong>Texas.</strong> No birthday rule, no state-standardized plans, a deep Advantage market in the cities and 2026 rural exits. <a href="https://texasmedicareenrollment.com" rel="noopener">Our Texas site</a> explains what is different.</li>
<li><strong>Utah, Colorado and Florida.</strong> Each has its own sister site: <a href="https://medicareenrollmentutah.com" rel="noopener">Utah</a>, <a href="https://coloradomedicareenrollment.com" rel="noopener">Colorado</a> and <a href="https://medicareenrollmentflorida.com" rel="noopener">Florida</a>, where issue-age Medigap rating rewards buying early.</li>
<li><strong>Idaho and Oregon.</strong> Idaho has a birthday rule of its own (63 days); Oregon has one too (30 days). Your California Medigap policy continues in either, re-rated; a change there follows that state&rsquo;s rule.</li>
</ul>
<div class="note-box"><p><strong>Before you go:</strong> if you hold a Medigap policy and your birthday is coming, use California&rsquo;s birthday rule to move to the carrier with the best rate history <em>before</em> the move. Once you are gone, that annual no-questions switch is gone with you in most states.</p></div>
<h2>Arriving in California</h2>
<p>The move SEP works the same way in reverse. Your first decision is the <a href="/kaiser">Kaiser question</a>; your second is that a Medigap policy from your old state continues here, re-rated for California, and from now on you get the 60-day birthday rule each year. If you arrive with a Medicare Advantage plan, you choose a new one sold in your California county, or use the move as a guaranteed-issue event to buy Medigap without health questions. People arriving from New York or Connecticut should know California does not have year-round guaranteed issue.</p>
<h2>Splitting the year</h2>
<p>Palm Springs to Oregon, San Diego to Idaho, the Bay Area to Arizona: if you keep a California address and spend months elsewhere, a Medigap policy with Original Medicare covers you at any provider in both places. Most Advantage plans cover only emergencies outside their service area, though some PPOs carry travel benefits, and Senior Advantage has a visiting-member arrangement only in other Kaiser regions. We look at both addresses before recommending anything.</p>
<h2>Part D when you move</h2>
<p>Your Part D plan is tied to your region too. Use the move SEP to pick one sold at the new address, and re-check the formulary and preferred pharmacies; the same medication list can price very differently across state lines.</p>""",
     faqs=[("I am moving from California to Arizona. Does my Medicare plan come with me?", "Original Medicare and a Medigap policy do; the carrier re-rates the policy for Arizona. A Medicare Advantage or Part D plan does not, and the move gives you a Special Enrollment Period to choose one sold in your new county. Our Arizona agency can take it from there."),
           ("Does California&rsquo;s birthday rule apply after I move?", "No. The birthday rule is California law and applies to California residents. Arizona and Texas have no equivalent; Nevada, Oregon and Idaho have their own narrower versions. Use California&rsquo;s rule before you leave if a switch is worth making."),
           ("Can I keep Kaiser if I move out of state?", "Only where Kaiser operates (Oregon and Washington, Colorado, Hawaii, Georgia, the Mid-Atlantic). Elsewhere Senior Advantage ends with the move, and you choose new coverage and new doctors."),
           ("I just moved to California. Do I have to change my Medicare plan?", "Advantage and Part D plans are tied to your county, so yes, the move gives you a Special Enrollment Period to choose plans sold here. A Medigap policy from another state usually stays in force, re-rated; once you are a California resident you also get the annual birthday rule.")],
     sources=[SRC_SEP, SRC_CHA_RULES, SRC_MMR_SWITCH, SRC_AZ, SRC_NV, SRC_TX], cta="Moving? Let&rsquo;s make sure your coverage lands with you.", about="Moving to or from California on Medicare"),

dict(slug="wildfires", nav_title="Wildfires and Medicare: disaster Special Enrollment Periods, prescriptions, evacuations", crumb="Wildfires", scene="redwoods",
     title="Wildfires &amp; Medicare in California: Disaster SEPs, Prescriptions, Evacuations | ECOS Medicare Solutions",
     desc="What a wildfire emergency does to your Medicare: the FEMA disaster Special Enrollment Period, early prescription refills and out-of-network pharmacies, replacing durable medical equipment, and what to keep in the go-bag. From an agent licensed in California (CA License #0M00978).",
     llm="Wildfires and Medicare in California: the disaster Special Enrollment Period, Part D early refills, out-of-network pharmacies, replacing equipment, evacuation checklist",
     eyebrow="Your situation · Wildfires", h1="Wildfires and Medicare: what changes when the county is under a disaster declaration",
     sub="California has had a federal disaster declaration for fire almost every year, from Paradise to the Los Angeles fires of January 2025. Here is what the declaration does to your Medicare deadlines and your prescriptions &mdash; and what to pack.",
     keyfacts=["A FEMA-declared emergency or major disaster opens a Medicare Special Enrollment Period for people who live in the declared area (or rely on someone who does) and missed a valid enrollment period because of it. It runs from the start of the incident period and lasts two full calendar months after it ends, or up to a year.",
               "In the emergency area, Part D plans must lift refill-too-soon limits, replace lost or destroyed medications, and cover out-of-network pharmacies at the plan&rsquo;s usual allowance. Advantage plans must cover care from out-of-network providers at in-network cost sharing while the emergency lasts.",
               "Medicare pays to replace durable medical equipment (oxygen, CPAP, wheelchairs, diabetic supplies) lost in a declared disaster without the usual waiting periods.",
               "Deadlines are extended, not erased: the SEP exists to let you make the election you would have made. Call before you assume the window has closed."],
     body="""<h2>The disaster Special Enrollment Period</h2>
<p>When FEMA or a state, county or local government declares an emergency or major disaster, Medicare opens a Special Enrollment Period for anyone who lives in the declared area &mdash; or who relies on someone who does to make health-care decisions &mdash; and who missed a valid enrollment period (the Annual Election Period, the Advantage Open Enrollment Period, or another SEP) because of it. You can then make the election you would have made. The window opens with the incident period and runs two full calendar months after it ends, or longer if the declaration is extended, up to a year.</p>
<p>The January 2025 Los Angeles fires opened both a FEMA declaration and a federal public health emergency; earlier declarations covered the Camp Fire in Butte County, the Tubbs and Kincade fires in Sonoma, the Caldor and Dixie fires in the Sierra, and many others. If your county was declared and you missed a deadline, the SEP is real and we will help you use it.</p>
<h2>Prescriptions during an emergency</h2>
<ul>
<li><strong>Early refills.</strong> Part D plans must remove refill-too-soon edits in the affected area, so you can refill before the usual date.</li>
<li><strong>Lost or destroyed medications</strong> can be replaced; the plan must cover the replacement.</li>
<li><strong>Out-of-network pharmacies.</strong> If you evacuate somewhere without a network pharmacy, the plan must cover an out-of-network fill at its usual allowance; keep the receipt.</li>
<li><strong>Prior authorizations</strong> and other utilization rules are relaxed for the duration.</li>
</ul>
<h2>Care and equipment</h2>
<p>Medicare Advantage plans must cover care from out-of-network providers, including hospitals, at in-network cost sharing while the emergency lasts, and waive referral requirements. Original Medicare works anywhere regardless. Medicare will pay to replace durable medical equipment and supplies lost in the disaster &mdash; oxygen concentrators, CPAP machines, wheelchairs, walkers, glucose monitors &mdash; without the standard replacement waiting periods.</p>
<h2>What to keep in the go-bag</h2>
<ul>
<li>Your Medicare card and your plan card (or a photo of both on your phone).</li>
<li>A current medication list with doses and the prescribing doctor.</li>
<li>Your pharmacy&rsquo;s phone number and your plan&rsquo;s member-services number.</li>
<li>A week of medications, rotated; more if you can.</li>
<li>Your doctors&rsquo; names and portal logins.</li>
</ul>
<div class="note-box"><p><strong>If you evacuated and missed a deadline:</strong> call us or 1-800-MEDICARE and say the words &ldquo;disaster Special Enrollment Period.&rdquo; The election you meant to make can usually still be made.</p></div>""",
     faqs=[("A wildfire made me miss the December 7 deadline. Am I out of luck?", "Usually not. A FEMA-declared disaster opens a Special Enrollment Period for people who lived in a declared county, or who rely on someone who did, and missed a valid election period because of it. Call us and we will file the election."),
           ("Can I refill my prescriptions early if I have to evacuate?", "Yes, in a declared emergency area. Part D plans must lift refill-too-soon limits, replace lost medications and cover out-of-network pharmacies at the plan&rsquo;s usual allowance."),
           ("My CPAP was lost in the fire. Will Medicare replace it?", "Yes. Medicare pays to replace durable medical equipment and supplies lost in a declared disaster without the usual replacement waiting period. Your supplier or doctor can start the order."),
           ("Does my Medicare Advantage plan cover me at a hospital outside its network during an evacuation?", "During a declared emergency, yes, at in-network cost sharing, and referral rules are waived. Original Medicare with a Medigap policy works at any Medicare provider regardless.")],
     sources=[SRC_SEP, SRC_CMS_FIRE, SRC_CMS_CAPHE], cta="Affected by a fire? Let&rsquo;s sort out your coverage first.", about="Wildfire emergencies and Medicare in California"),

dict(slug="veterans", nav_title="Medicare for California veterans and military retirees", crumb="Veterans", scene="harbor",
     title="Medicare for Veterans &amp; Military Retirees in California | TRICARE For Life, VA | ECOS Medicare Solutions",
     desc="Medicare for California veterans: TRICARE For Life, VA health care (Greater LA, San Diego, Palo Alto, Loma Linda, Long Beach, San Francisco, Sacramento, Fresno), why Part B timing matters, and which plans fit. From a retired Air Force officer licensed in California.",
     llm="Medicare for California veterans and military retirees: TRICARE For Life, VA care and Part B, the eight VA health systems in California, base-adjacent communities",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for California veterans and military retirees",
     sub="California has more veterans than any state and the largest military-retiree community in the country around San Diego. TRICARE For Life, the VA, and Medicare fit together in a specific order &mdash; explained by a 22-year Air Force veteran who retired as an officer.",
     keyfacts=["TRICARE For Life requires Medicare Parts A and B and then pays second to Medicare. For most TFL households, Original Medicare plus TFL is complete coverage; a Medigap policy is usually unnecessary and TFL pharmacy is creditable Part D coverage.",
               "VA health care and Medicare do not coordinate: the VA pays only at VA facilities, Medicare only at non-VA providers. VA care is <strong>not</strong> creditable coverage for Part B, so delaying Part B because you have the VA triggers a permanent penalty.",
               "California has eight VA health systems: Greater Los Angeles, Long Beach, Loma Linda, San Diego, Palo Alto, San Francisco, Northern California (Sacramento/Mather) and Central California (Fresno), plus dozens of clinics.",
               "An MA-only Medicare Advantage plan (no Part D) can add dental, vision and hearing for people with TFL or VA pharmacy without duplicating drug coverage; whether it is worth it depends on the network."],
     body="""<h2>TRICARE For Life: the short version</h2>
<p>When a military retiree or family member becomes eligible for Medicare, TRICARE For Life is the coverage that follows &mdash; but only with Medicare Parts A and B in place. Medicare pays first, TFL pays second, and for care Medicare covers there is usually nothing left. TFL&rsquo;s pharmacy benefit is creditable Part D coverage, so most TFL households need no standalone drug plan. The one non-negotiable is Part B: without it, TFL does not pay.</p>
<h2>VA health care: a different animal</h2>
<p>VA care is comprehensive inside the VA and nothing outside it. Medicare covers you at every non-VA hospital and doctor, which is where an emergency will take you. The VA&rsquo;s prescription benefit is creditable for Part D, but VA medical care is <strong>not</strong> creditable for Part B, so a veteran who skips Part B at 65 pays a permanent penalty when they enroll later. Most California veterans keep both.</p>
<h2>Where the VA is in California</h2>
<ul>
<li><strong>VA Greater Los Angeles</strong> (West LA medical center, Sepulveda, and clinics from Santa Barbara to the Antelope Valley) and <strong>VA Long Beach</strong> (Tibor Rubin) for the South Bay and Orange County.</li>
<li><strong>VA Loma Linda</strong> for the Inland Empire, high desert and Coachella Valley.</li>
<li><strong>VA San Diego</strong> (La Jolla) with clinics from Oceanside to Chula Vista.</li>
<li><strong>VA Palo Alto</strong> and <strong>VA San Francisco</strong> for the Bay Area, the Peninsula and the Central Coast.</li>
<li><strong>VA Northern California</strong> (Mather, Martinez, Redding, Chico, Fairfield) and <strong>VA Central California</strong> (Fresno) for the Valley and the North State.</li>
</ul>
<h2>Which plan, then?</h2>
<ul>
<li><strong>TFL households:</strong> Original Medicare Parts A and B plus TFL, no Medigap, no Part D. Consider an MA-only Advantage plan only if its extras are worth the network trade.</li>
<li><strong>VA-only veterans:</strong> Parts A and B on time, then Medigap or Advantage for the non-VA side of life; Part D is optional if VA pharmacy is working for you.</li>
<li><strong>Veterans with employer or CalPERS retiree coverage:</strong> those rules apply first; see <a href="/turning-65">Turning 65</a>.</li>
</ul>
<p>Base-adjacent guides: <a href="/san-diego-navy">Naval Base San Diego, Miramar &amp; Camp Pendleton</a>, <a href="/travis-afb">Travis AFB</a>, <a href="/vandenberg-sfb">Vandenberg SFB</a>, and <a href="/lemoore-nas">NAS Lemoore, Edwards AFB &amp; China Lake</a>.</p>""",
     faqs=[("I have TRICARE For Life. Do I need a Medigap policy or Part D?", "Usually neither. TFL pays secondary to Medicare and its pharmacy is creditable drug coverage. You do need Part B, and you must keep it."),
           ("I use the VA. Do I still need Medicare Part B?", "In most cases, yes. VA medical care is not creditable coverage for Part B, so delaying Part B adds a lifelong penalty, and VA care does not cover you at a non-VA hospital in an emergency."),
           ("Can I have Medicare Advantage and TRICARE For Life?", "Yes. TFL pays after the Advantage plan. An MA-only plan without Part D avoids duplicating TFL&rsquo;s pharmacy benefit; we check whether the extras are worth the network."),
           ("Does Medicare pay at a military hospital or a VA hospital?", "No. Military hospitals see retirees on a space-available basis under TRICARE, and VA facilities are paid by the VA. Medicare pays at civilian providers.")],
     sources=[SRC_TFL, SRC_VA, SRC_MA_GOV], cta="Retired from the service? Let&rsquo;s line up TRICARE, the VA and Medicare properly.", about="Medicare for veterans and military retirees in California"),

dict(slug="medi-cal", nav_title="Medicare + Medi-Cal: Medicare Savings Programs, the 2026 asset limit, Extra Help, Medi-Medi Plans", crumb="Medi-Cal &amp; savings programs", scene="valley",
     title="Medicare + Medi-Cal in California [[YEAR]]: Savings Programs, Asset Limit, Medi-Medi Plans | ECOS Medicare Solutions",
     desc="Medicare and Medi-Cal together: the Medicare Savings Programs that pay your Part B premium, the asset limit that returned January 1, 2026 ($130,000), Extra Help, and the Medi-Medi Plans available in 41 counties. Free help from a licensed California agent.",
     llm="Medicare and Medi-Cal dual eligibility in California: Medicare Savings Programs (QMB, SLMB, QI), the Medi-Cal asset limit reinstated January 1, 2026, Extra Help, Medi-Medi Plans (exclusively aligned D-SNPs) in 41 counties",
     eyebrow="Your situation · Medicare + Medi-Cal", h1="Medicare and Medi-Cal together: what you may qualify for",
     sub="Programs that pay your Part B premium, cut your drug costs, and coordinate Medicare with Medi-Cal &mdash; and the asset limit that came back in 2026 after two years without one.",
     keyfacts=["The Medicare Savings Programs pay the Part B premium ([[YEAR]]: $202.90 a month) for people with limited income and resources: QMB also covers Medicare&rsquo;s deductibles and copays; SLMB and QI pay the premium only. Qualifying enrolls you automatically in Extra Help for Part D.",
               "<strong>The asset limit is back.</strong> California removed Medi-Cal&rsquo;s asset test in January 2024 and reinstated it on January 1, 2026 at $130,000 for one person, plus $65,000 for each additional household member. It applies to the aged, blind and disabled programs, long-term care and the Medicare Savings Programs. A home you live in, one vehicle and most retirement accounts are still exempt.",
               "Full Medi-Cal alongside Medicare covers what Medicare does not: Part B premiums and cost sharing, long-term care, and dental through Medi-Cal Dental.",
               "Medi-Medi Plans are exclusively aligned Dual Special Needs Plans: one organization runs your Medicare and your Medi-Cal managed-care plan. Under CalAIM they expanded from 12 counties to 41 for 2026."],
     body="""<h2>The Medicare Savings Programs</h2>
<table class="ctable">
<thead><tr><th scope="col">Program</th><th scope="col">What it pays</th></tr></thead>
<tbody>
<tr><th scope="row">QMB (Qualified Medicare Beneficiary)</th><td>Part B premium, Part A premium if any, and Medicare&rsquo;s deductibles, coinsurance and copays. Providers may not bill you for Medicare cost sharing.</td></tr>
<tr><th scope="row">SLMB (Specified Low-Income Medicare Beneficiary)</th><td>Part B premium only.</td></tr>
<tr><th scope="row">QI (Qualifying Individual)</th><td>Part B premium only; annual funding, first come first served.</td></tr>
</tbody></table>
<p>Income limits follow the federal poverty level and change each spring; the county Medi-Cal office applies them. Apply through your county office, BenefitsCal.com, or with help from HICAP (1-800-434-0222). Qualifying for any of the three automatically qualifies you for Extra Help, which lowers Part D premiums, deductibles and copays.</p>
<h2>The 2026 asset limit</h2>
<p>From January 2024 through December 2025, California had no asset test for Medi-Cal, which let many people with modest savings qualify for the Savings Programs. The 2025 state budget reinstated the limit effective <strong>January 1, 2026: $130,000 for a single person, plus $65,000 for each additional person in the household</strong> ($195,000 for a couple). It applies to non-MAGI Medi-Cal, including the aged, blind and disabled programs, Medi-Cal with a share of cost, long-term care, and the Medicare Savings Programs. Your primary home, one vehicle, household goods, most retirement accounts and certain burial funds do not count. People already enrolled are reviewed at their next annual renewal, not dropped immediately. If your savings sit near the line, get advice before you spend or move money; HICAP, Justice in Aging and a Medi-Cal planning attorney all handle this.</p>
<h2>Medi-Medi Plans (aligned D-SNPs)</h2>
<p>A Dual Special Needs Plan is a Medicare Advantage plan for people with both Medicare and Medi-Cal. California&rsquo;s version, the <strong>Medi-Medi Plan</strong>, requires that the same organization run your Medi-Cal managed-care plan, so Medicare, Medi-Cal, long-term services and care coordination come through one card and one care team. For 2026 they are available in 41 counties, up from 12, including Los Angeles (L.A. Care, Health Net, Molina, Anthem, Kaiser and others), Orange (CalOptima OneCare), San Diego, the Inland Empire (IEHP), Santa Clara, Alameda, San Francisco, Sacramento, Fresno and Kern. If you are dual-eligible, a Medi-Medi Plan is usually where we start, and we compare it against your current arrangement rather than assume.</p>
<h2>Long-term care</h2>
<p>Medicare covers short rehabilitation stays; Medi-Cal covers long-term nursing-facility care and, through programs like In-Home Supportive Services and the Assisted Living Waiver, care at home or in assisted living for people who qualify. The asset limit applies here too, with the well-known spousal protections. An <a href="/institutional-snp">Institutional SNP</a> or a Medi-Medi Plan can coordinate the Medicare side of that care.</p>""",
     faqs=[("Can Medi-Cal pay my Medicare Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through your county Medi-Cal office or BenefitsCal; HICAP (1-800-434-0222) can help. An asset limit of $130,000 for one person applies from 2026."),
           ("What is the Medi-Cal asset limit in 2026?", "$130,000 for a single person, plus $65,000 for each additional household member, effective January 1, 2026. Your home, one vehicle, household goods, most retirement accounts and certain burial funds are exempt. It applies to the Medicare Savings Programs as well as full Medi-Cal for seniors."),
           ("What is a Medi-Medi Plan?", "An exclusively aligned Dual Special Needs Plan: a Medicare Advantage plan run by the same organization as your Medi-Cal managed-care plan, so both programs are coordinated by one care team. Available in 41 counties for 2026."),
           ("Where do I apply for Medi-Cal if I am over 65?", "Through your county social services office, online at BenefitsCal.com, or with help from HICAP. Eligibility for people 65 and over follows the aged-and-disabled rules, including the 2026 asset limit.")],
     sources=[SRC_DHCS_ASSET, SRC_JIA, SRC_CHA_MEDICAL, SRC_DHCS_MMP, SRC_DHCS_DSNP, SRC_HICAP, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Medi-Cal dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in California", crumb="Chronic SNPs", scene="valley",
     title="Chronic SNPs (C-SNP) in California | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in California: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in California for qualifying chronic conditions",
     eyebrow="Your situation &middot; Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in California",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by California county and is concentrated in Los Angeles, Orange, San Diego, the Inland Empire and the Central Valley; a regular Advantage plan, Kaiser Senior Advantage or a Medigap policy may still serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition.</p>
<h2>Conditions that can qualify</h2>
<p>Medicare defines the chronic conditions a C-SNP can serve. Common examples include:</p>
<ul><li>Diabetes mellitus</li><li>Chronic heart failure and certain cardiovascular disorders</li><li>Chronic lung disorders such as COPD</li><li>End-stage renal disease (ESRD) requiring dialysis</li><li>Certain other qualifying chronic conditions</li></ul>
<p>You generally need a provider to verify that you have the qualifying condition in order to enroll, and a diagnosis gives you a Special Enrollment Period to join one outside the normal windows.</p>
<h2>What a C-SNP usually offers</h2>
<ul>
<li><strong>Care coordination</strong> tailored to your condition, often including a care team or coordinator.</li>
<li><strong>A drug formulary</strong> built with your condition&rsquo;s medications in mind, plus included Part D coverage.</li>
<li><strong>Extra benefits</strong> that vary by plan, and frequently a $0 or low plan premium.</li>
</ul>
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan with a medical group, so the question of whether your cardiologist, your dialysis center or your Stanford or UCLA specialist is reachable applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medi-cal">Medi-Medi Plans</a> for people with both Medicare and Medi-Cal.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in California?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in California", crumb="Institutional SNPs", scene="vineyards",
     title="Institutional SNPs (I-SNP) in California | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in California for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Medi-Cal long-term care.",
     llm="Institutional Special Needs Plans (I-SNP) in California for facility-level care",
     eyebrow="Your situation &middot; Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in California",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In California, many people in long-term care also qualify for Medi-Cal, which pays for the nursing-facility stay itself; a Medi-Medi Plan may then be the better fit, and we compare the two. The 2026 asset limit applies to long-term-care Medi-Cal."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul><li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li><li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment.</li></ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions, including adult children who live out of state.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medi-cal">Medi-Medi Plan</a> if Medi-Cal is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medi-cal">Medicare + Medi-Cal</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your California county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or Medi-Medi Plan coordinates with a facility and with Medi-Cal.")],
     sources=[SRC_MA_GOV, SRC_CHA_MEDICAL, SRC_DHCS_ASSET], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence &mdash; free 295-page retirement guide", crumb="Free Retirement Guide", scene="coast",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed California agent (CA License #0M00978), gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed California agent",
     eyebrow="Free 295-page guide &middot; 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site (CA License #0M00978).",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling a California house or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, and how much of it is taxed &mdash; federally, since California does not tax Social Security.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in California (CA License #0M00978), and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in California. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to California?", "The book covers Medicare and retirement decisions nationally. For California specifics &mdash; the Kaiser question, the birthday rule, Medi-Cal&rsquo;s asset limit, CalPERS, wildfire rules &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
