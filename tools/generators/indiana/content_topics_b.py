"""Indiana topic pages, part B: turning 65, snowbirds & border care, veterans, Medicaid, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_SHIP_IN, SRC_SHIP_NAT, SRC_IDOI, SRC_HEA1226, SRC_ASKSHIP,
                              SRC_FSSA_APPLY, SRC_FSSA_ABD, SRC_PATHWAYS, SRC_HOOSIERRX, SRC_TFL, SRC_VA)
SRC_HCC = ("Indiana Medicaid: Hoosier Care Connect", "https://www.in.gov/medicaid/members/member-programs/hoosier-care-connect/")
SRC_PATHWAYS_HUB = ("FSSA: PathWays for Aging launching in July (program summary)", "https://www.in.gov/fssa/thehub/more-hot-topics/pathways-for-aging-launching-in-july")
SRC_VA_IN = ("VA Indiana Health Care: Richard L. Roudebush VA Medical Center, Indianapolis", "https://www.va.gov/indiana-health-care/")
SRC_VA_NIN = ("VA Northern Indiana Health Care System (Fort Wayne and Marion)", "https://www.va.gov/northern-indiana-health-care/")
SRC_VA_MARION = ("Marion VA Health Care System, including the Evansville VA Health Care Center", "https://www.va.gov/marion-health-care/")
SRC_USAFACTS = ("USAFacts: Veterans in Indiana", "https://usafacts.org/topics/veterans/state/indiana/")
SRC_FL_NEW = ("Medicare Enrollment Florida (sister section): Medicare for people new to Florida", "https://www.ecosinsurancesolutions.com/florida/new-to-florida")
SRC_MN_SNOW = ("Minnesota Medicare Enrollment (sister section): Medicare for Minnesota snowbirds", "https://www.ecosinsurancesolutions.com/minnesota/snowbirds")
SRC_AZ = ("Medicare Enrollment Arizona (sister section with Mesa and Sun City offices)", "https://www.ecosinsurancesolutions.com/arizona")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in Indiana guide", crumb="Turning 65", scene="speedway",
     title="Turning 65 in Indiana: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Indiana: your 7-month enrollment window, the Medigap open enrollment, what to do with a union or employer retiree plan, still-working rules, the deadlines with lifelong penalties, and a checklist. Free help from a licensed Indiana agent.",
     llm="Turning 65 in Indiana: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap, union and employer retiree plans, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Indiana: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Indiana, where a lot of people reach 65 with a union or employer retiree plan in hand and a real question about whether to keep it.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. Indiana now adds a birthday-rule window every year after that, but only for switching between Medigap policies, not for buying in from Advantage.",
               "A union or employer retiree plan is often a group Medicare Advantage plan or a group supplement. Dropping it is frequently permanent, so compare before you cancel anything.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Indiana twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
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
<caption>The two ways most Hoosiers put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums; Indiana&rsquo;s birthday rule for switching later.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a network drawn around one or more hospital systems, that changes yearly.</td></tr>
</tbody></table>
<p>Where you live and where you get care tilt the answer. In Indianapolis, Fort Wayne, Evansville and South Bend the Advantage menu is deep, but the networks are drawn around systems &mdash; IU Health, Ascension St. Vincent, Community, Franciscan, Parkview, Lutheran, Deaconess, Beacon &mdash; and a plan that includes one may exclude another. In rural counties the menu is shorter. If you winter in Florida, or your specialist is in Louisville, Cincinnati or Chicago, a supplement removes the network question entirely. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above. Indiana&rsquo;s new birthday rule lets you shop the policy every year afterward, but only once you have one. Our research site sets the windows side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/indiana">turning 65 in Indiana</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no Indiana insurer can turn you down or charge more for your health. Afterward, insurers can use medical underwriting unless you are inside the birthday-rule window (same plan letter, existing policyholders) or a guaranteed-issue event.</p></div>
<h2>5. Still working at 65, or retiring with a plan in hand?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Indiana&rsquo;s big employers &mdash; the state, the universities, the school corporations, the health systems, Lilly, Cummins, the automakers and the mills &mdash; generally qualify; a small business or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll.</p>
<p><strong>Retiree plans are the Indiana question.</strong> A large share of Hoosiers reach 65 with a retiree plan from a union trust, a former employer, the state or a school corporation. Those plans usually turn into one of two things at 65: a <em>group</em> Medicare Advantage plan or a <em>group</em> supplement, often with drug coverage built in and a premium the trust or employer helps pay. Two things to know before you touch it: retiree drug coverage is normally creditable, so you can hold off on your own Part D without a penalty while you have it; and dropping a retiree plan to buy something on the individual market is frequently a one-way door &mdash; many trusts do not let you back in. Bring the retiree plan&rsquo;s annual notice to your review and we will set it beside the individual options honestly, including the case for leaving it alone.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find your retiree plan&rsquo;s notice, if you have one, and read what it becomes at 65.</li>
<li>Find out how deep the Advantage menu is in your county, and which hospital systems each plan includes for [[YEAR]].</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if a specific system is your care.</li>
<li>If you winter away or cross a state line for care, read the <a href="/snowbirds">snowbirds and border-care guide</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">PathWays for Aging</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Hoosiers sort through it every day &mdash; clearly, patiently, and at no cost to you. Indiana SHIP (800-452-4800) offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("I have a union or employer retiree plan. Should I keep it or buy my own?", "Compare before you cancel anything. Retiree plans usually become a group Advantage plan or a group supplement at 65, the drug coverage is normally creditable, and leaving is often permanent. Sometimes the retiree plan is the best deal available; sometimes an individual plan is. We set them side by side with the numbers."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Indiana?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget and county. The Advantage menu is deep in the metros and drawn around hospital systems; a Medigap policy has no network and now comes with an annual switching window. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in Indiana?", "Three things. Many Hoosiers arrive at 65 with a retiree plan that needs a decision. Indiana&rsquo;s Advantage networks are drawn around a handful of hospital systems, so your doctor decides your shortlist. And since 2026 Indiana has a Medigap birthday rule, which makes a supplement easier to keep affordable over time.")],
     sources=[SRC_CMS, SRC_SHIP_IN, SRC_SHIP_NAT, SRC_HEA1226], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Indiana"),

dict(slug="snowbirds", nav_title="Medicare for Hoosier snowbirds and border commuters", crumb="Snowbirds &amp; border care", scene="dunes",
     title="Medicare for Hoosier Snowbirds &amp; Border Care | ECOS Medicare Solutions",
     desc="Which Medicare plans work when you winter in Florida or Arizona, or see a doctor in Louisville, Cincinnati or Chicago: Medigap travels, most Advantage HMOs cover emergencies only, and residency decides your county.",
     llm="Medicare for Indiana snowbirds who winter in Florida, Arizona or the Gulf Coast, and for Hoosiers who cross into Kentucky, Ohio, Illinois or Michigan for care: which plans work out of area, residency rules, Part D away from home",
     eyebrow="Guide · Two homes, or two states", h1="Medicare for Hoosier snowbirds and border commuters",
     sub="Whether you leave Fort Wayne for Fort Myers each January, or live in Jeffersonville and see every specialist in Louisville, the rule is the same: some plans follow you and some stop at the network line.",
     keyfacts=["A Medigap policy with Original Medicare works with any provider in the U.S. that accepts Medicare, in both states, all year. It is the simplest two-home coverage there is, and Indiana&rsquo;s birthday rule now lets you re-shop it annually.",
               "Most Medicare Advantage HMOs cover only emergencies and urgent care outside their service area; some PPOs cover routine care out of network at higher cost; a few plans have a travel benefit. Read the Evidence of Coverage, not the brochure.",
               "Your plan is tied to the county of your permanent residence. Wintering away for four months does not change that; moving your legal residence does, and it opens a Special Enrollment Period.",
               "Indiana borders four states, and Hoosiers in the Region, along the Ohio River and in the northern tier routinely use Chicago, Louisville, Cincinnati and Michigan hospitals. An Advantage network may or may not reach across the line. Our Florida, Arizona and Minnesota sections cover the other end of the trip."],
     body="""<p>Indiana is a state people leave in January and a state whose edges lean on other states&rsquo; hospitals. Retirees from Fort Wayne, Kokomo and Carmel head for Florida&rsquo;s Gulf Coast, Arizona, or the Texas coast; families in Lake County drive to Chicago for a specialist, families in Clark and Floyd counties cross the bridge to Louisville, Dearborn County looks to Cincinnati, and the northern tier uses Michigan. The Medicare rules for all of this are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>Which plans travel</h2>
<table class="ctable">
<caption>How each plan type behaves once you are outside its service area. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Routine care in the other state</th><th scope="col">What you pay there</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Medigap</th><td>Any provider that accepts Medicare</td><td>Same as at home &mdash; the supplement pays its share anywhere</td></tr>
<tr><th scope="row">Medicare Advantage PPO</th><td>Out-of-network providers, if the plan allows</td><td>Higher out-of-network copays or coinsurance; check the plan&rsquo;s out-of-network maximum</td></tr>
<tr><th scope="row">Medicare Advantage HMO</th><td>Emergencies and urgent care only, on most plans</td><td>Routine care generally not covered out of area</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Preferred-pharmacy pricing may differ; check that a chain near your other home is preferred</td></tr>
</tbody></table>
<div class="note-box"><p><strong>A few Advantage plans offer a &ldquo;visitor&rdquo; or &ldquo;travel&rdquo; benefit</strong> that extends in-network coverage for up to six or twelve months away from home, and some national carriers let you use their network in other states. It is plan-specific and it changes. If a travel benefit is the reason you are choosing an Advantage plan, we get it in writing from the Evidence of Coverage before you enroll.</p></div>
<h2>If you winter away</h2>
<p>Your plan comes from your Indiana county, because that is where you file your taxes and register your car. A Medigap policy covers the hospital in Naples or Mesa the same way it covers IU Health or Parkview. An Advantage HMO from Allen County probably does not, beyond emergencies, and a Florida doctor who is out of network can bill you in full. If you are on an Advantage plan and spend four months away every year, the honest comparison is a Medigap policy from Indiana or a PPO with a documented travel benefit. Our sister sections cover the other end of the trip: the Florida section&rsquo;s guide for <a href="https://www.ecosinsurancesolutions.com/florida/new-to-florida">people new to Florida</a>, served by its own Florida-licensed agent, and <a href="https://www.ecosinsurancesolutions.com/arizona">our Arizona section</a>, which has walk-in offices in Mesa and Sun City.</p>
<h2>If you cross a state line for care</h2>
<p>This is the quieter Indiana problem, and it affects more people than the snowbird one. Lake and Porter counties are part of the Chicago care market; Clark, Floyd and Harrison counties are part of Louisville&rsquo;s; Dearborn and Ohio counties are part of Cincinnati&rsquo;s; and the northern tier uses South Bend&rsquo;s systems, which themselves run hospitals in Michigan. With Original Medicare and a Medigap policy there is nothing to check. With an Advantage plan, the question is whether that Louisville cardiologist or Chicago cancer center is <em>in the network</em>, not whether it is across a state line &mdash; some Indiana plans include out-of-state providers, most do not, and a PPO&rsquo;s out-of-network rate applies if it does not. We confirm the specific provider before you enroll.</p>
<h2>Residency: the rule that decides everything</h2>
<p>Medicare Advantage and Part D plans are sold by county, and you must live in the plan&rsquo;s service area &mdash; meaning your <em>permanent</em> residence. Wintering away for four or five months does not change that; most plans allow up to six months, and some up to twelve, out of area before they disenroll you. What does change it is moving your legal residence: registering to vote, licensing the car, filing as a Florida resident. That triggers a Special Enrollment Period, ends your old plan, and means choosing from the plans sold in your new county. A Medigap policy is different: once issued it stays in force wherever you live, though the premium may be re-rated to the new state.</p>
<h2>If you make the move permanent</h2>
<p>Plenty of Hoosiers eventually do, and plenty come back to be near grandchildren. Darin is licensed in Indiana, Arizona, Texas, Minnesota and twelve other states, and our Florida section is served by its own licensed agent, so we can move your coverage cleanly in either direction; the state-by-state Medigap switching rules &mdash; including which states have a birthday rule like Indiana&rsquo;s &mdash; are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so filling a prescription in Sarasota or Scottsdale is not a problem. Pricing can be: plans have <em>preferred</em> pharmacies where copays are lowest, and the Kroger or Meijer that is preferred here may not have a preferred counterpart down south. Mail order at 90-day supplies solves most of it. We check both ZIP codes when we compare plans.</p>""",
     faqs=[("I winter in Florida. Does my Indiana Medicare Advantage plan work there?", "For emergencies and urgent care, yes &mdash; every plan covers those anywhere in the U.S. For routine care, most HMOs do not; some PPOs cover out-of-network care at higher cost, and a few plans have a travel benefit. Read the Evidence of Coverage, and if travel is why you chose the plan, get the benefit in writing."),
           ("Does an Indiana Medigap policy work in other states?", "Yes. A Medigap policy pays alongside Original Medicare with any provider in the country that accepts Medicare, with no network and no service area. It is the simplest travel coverage, and Indiana&rsquo;s birthday rule lets you re-shop it each year."),
           ("I live in Jeffersonville and my doctors are in Louisville. Which plan works?", "With Original Medicare and a Medigap policy, any Louisville provider that accepts Medicare is covered. With an Advantage plan, only if that provider is in the plan&rsquo;s network; some Indiana plans include Louisville systems and most do not. We confirm your specific doctors before you enroll."),
           ("How long can I be out of state without losing my Advantage plan?", "It depends on the plan; most allow up to six months out of the service area, some up to twelve. Changing your legal residence ends the plan regardless of time, and gives you a Special Enrollment Period to pick a plan where you live now."),
           ("Can you help me if I move to Florida or Arizona for good?", "Yes. Darin is licensed in Indiana and fifteen other states including Arizona and Texas, and our Florida section has its own licensed agent, so we help you move your coverage cleanly, including the Medigap switching rules that differ by state.")],
     sources=[SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_FL_NEW, SRC_AZ, SRC_MN_SNOW], cta="Two homes, or a doctor across the line? Let&rsquo;s make sure your plan covers both."),

dict(slug="veterans", nav_title="Medicare for Indiana veterans and military retirees", crumb="Veterans", scene="monument",
     title="Medicare for Indiana Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Roudebush in Indianapolis, VA Northern Indiana in Fort Wayne and Marion, the Evansville VA) work with Medicare in Indiana, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for Indiana veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, Indiana's VA medical centers (Roudebush, VA Northern Indiana, Evansville), NSA Crane and Grissom ARB",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Indiana veterans and military retirees",
     sub="Indiana is home to more than 325,000 veterans. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Indiana VA care runs through the Richard L. Roudebush VA Medical Center in Indianapolis (the state&rsquo;s tertiary referral hospital, with clinics from Lafayette to Terre Haute, Bloomington, Shelbyville and Crane), the VA Northern Indiana Health Care System (Fort Wayne and Marion campuses), and the Evansville VA Health Care Center, run by the Marion, Illinois VA for southwestern Indiana.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Indiana has no large active-duty base &mdash; its installations are Naval Support Activity Crane in Martin County and Grissom Air Reserve Base near Peru, plus Camp Atterbury and the Indiana National Guard &mdash; but it has a large veteran population spread across every county, and a great many military retirees who came home to Indiana after a career somewhere else. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; IU Health or Parkview with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Where Indiana veterans get VA care</h2>
<p>The <strong>Richard L. Roudebush VA Medical Center</strong> on West 10th Street in Indianapolis is the state&rsquo;s tertiary VA hospital and teaching center, taking referrals from the rest of Indiana and running community clinics in Bloomington, Brownsburg, Martinsville, Lafayette, Camp Atterbury, Crane, Shelbyville and Terre Haute. The <strong>VA Northern Indiana Health Care System</strong> serves the north from its Fort Wayne and Marion campuses. Southwestern Indiana is covered by the <strong>Evansville VA Health Care Center</strong>, a large outpatient facility that belongs to the Marion, Illinois VA and serves roughly 15,000 veterans a year, with a clinic in Vincennes. None of these is a substitute for Part B: a heart attack on the way to Roudebush ends up at the nearest civilian emergency room, and Medicare is what pays there.</p>
<h2>Which Indiana plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state or across the line in Louisville or Chicago, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Indiana Department of Veterans Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at the Roudebush VA or the Fort Wayne VA?", "No. Medicare does not pay at VA facilities, and the VA does not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_VA_IN, SRC_VA_NIN, SRC_VA_MARION, SRC_USAFACTS, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Indiana Medicaid: PathWays for Aging, Medicare Savings Programs, Extra Help, HoosierRx", crumb="Indiana Medicaid &amp; PathWays", scene="courthouse",
     title="Medicare &amp; Indiana Medicaid: PathWays for Aging, QMB, SLMB | ECOS Medicare Solutions",
     desc="How Medicare works with Indiana Medicaid: PathWays for Aging for Hoosiers 60+, Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, HoosierRx, Dual Special Needs Plans, and where to apply (FSSA Benefits Portal, 800-403-0864).",
     llm="Medicare and Indiana Medicaid (dual eligible): Indiana PathWays for Aging (60+, since July 2024; Anthem, Humana, UnitedHealthcare), Medicare Savings Programs (QMB/SLMB/QI) through FSSA, Extra Help, HoosierRx, D-SNPs, applying through the FSSA Benefits Portal",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Indiana Medicaid: PathWays for Aging and the Medicare Savings Programs",
     sub="If you qualify for both Medicare and Indiana Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in Indiana, and where to apply.",
     keyfacts=["Indiana Medicaid is administered by the Family and Social Services Administration (FSSA); eligibility is decided by its Division of Family Resources. For the aged, blind and disabled category the resource limit is $2,000 for a single person and $3,000 for a couple.",
               "Since July 1, 2024, Hoosiers 60 and older who qualify for Medicaid on the basis of age, blindness or disability &mdash; including people with both Medicare and Medicaid, people in nursing facilities and people on home- and community-based services &mdash; get their Medicaid through <strong>Indiana PathWays for Aging</strong>, a managed-care program run by Anthem, Humana and UnitedHealthcare.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. Income limits change each year. Apply through the FSSA Benefits Portal or 800-403-0864; qualifying automatically brings Part D Extra Help.",
               "HoosierRx, Indiana&rsquo;s state pharmaceutical assistance program, pays up to $70 a month toward a Part D premium for eligible Hoosiers 65 and older. Free counseling on all of it: Indiana SHIP, 800-452-4800."],
     body="""<p>Some Hoosiers qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Indiana Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in Indiana</h2>
<p>Indiana Medicaid is administered by the <strong>Family and Social Services Administration (FSSA)</strong>, and eligibility is decided by its Division of Family Resources &mdash; not by an insurance agency. For adults 65 and over, eligibility is based on income and resources under the aged, blind and disabled rules; the resource limit in that category is $2,000 for a single person and $3,000 for a couple. You apply through the <strong>FSSA Benefits Portal</strong>, by phone at <strong>800-403-0864</strong>, or at a local Division of Family Resources office.</p>
<p>Once eligible, how you receive Medicaid depends on your age. Since <strong>July 1, 2024</strong>, Hoosiers <strong>60 and older</strong> in the aged, blind and disabled category &mdash; including dual eligibles, nursing-facility residents and people on home- and community-based waiver services &mdash; are enrolled in <strong>Indiana PathWays for Aging</strong>, a managed-care program in which a health plan from Anthem, Humana or UnitedHealthcare coordinates Medicaid services, including long-term services and supports, with the stated goal of helping people stay at home rather than in a nursing home. Medicare continues to pay first for medical care. FSSA put the eligible population at more than 123,000 Hoosiers at launch. People under 60 who are blind or disabled and <em>not</em> on Medicare are served by <strong>Hoosier Care Connect</strong>; those under 60 who have both Medicare and Medicaid are generally served through Traditional Medicaid rather than a managed-care plan.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Income limits change each year and resource rules apply. You apply through FSSA, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>HoosierRx</strong> is Indiana&rsquo;s own state pharmaceutical assistance program. It pays up to $70 a month toward a Medicare Part D plan premium for Indiana residents 65 and older under its income limits, and it is run through Indiana Medicaid.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact. Each of the three PathWays companies is also a Medicare Advantage carrier, so where it offers a D-SNP in your county, the Medicare and Medicaid sides can sit under one company.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from Indiana SHIP &mdash; the State Health Insurance Assistance Program, run by the Indiana Department of Insurance &mdash; at 800-452-4800. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program, Extra Help and HoosierRx could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with FSSA and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Indiana Medicaid, the Indiana Family and Social Services Administration, or the federal Medicare program.</p>""",
     faqs=[("What is Indiana PathWays for Aging?", "Indiana&rsquo;s Medicaid managed-care program for Hoosiers 60 and older who qualify for Medicaid on the basis of age, blindness or disability, launched July 1, 2024. A health plan from Anthem, Humana or UnitedHealthcare coordinates your Medicaid services, including long-term services and supports, while Medicare keeps paying first for your medical care. Enrollment was automatic for existing members."),
           ("Who counts as dual eligible in Indiana?", "People who qualify for both Medicare and Indiana Medicaid. There are full and partial categories; eligibility is determined by FSSA and CMS, based on income and resources. Those 60 and older are served through PathWays for Aging."),
           ("Can Indiana Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through the FSSA Benefits Portal or 800-403-0864; Indiana SHIP (800-452-4800) can help."),
           ("What is HoosierRx?", "Indiana&rsquo;s state pharmaceutical assistance program, which pays up to $70 a month toward your Part D plan premium if you are 65 or older, an Indiana resident, and under its income limits. It is separate from federal Extra Help, and SHIP can help you apply."),
           ("Where do I apply for Medicaid if I am over 65?", "Through the FSSA Benefits Portal online, by calling 800-403-0864, or at a local Division of Family Resources office. Eligibility for seniors follows the aged, blind and disabled rules, including the $2,000 / $3,000 resource limit.")],
     sources=[SRC_PATHWAYS, SRC_PATHWAYS_HUB, SRC_FSSA_ABD, SRC_FSSA_APPLY, SRC_HCC, SRC_HOOSIERRX, SRC_SHIP_IN, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Indiana Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Indiana", crumb="Chronic SNPs", scene="lakes",
     title="Chronic SNPs (C-SNP) in Indiana | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Indiana: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Indiana for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Indiana",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Indiana county and is concentrated in the metros; a regular Advantage plan or a Medigap policy may still serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. In Indiana they are sold mostly in the larger counties, and the network question &mdash; is your IU Health endocrinologist or your Parkview cardiologist in it &mdash; applies just as it does to any other Advantage plan.</p>
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your specialist is in it applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Indiana Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Indiana?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Indiana", crumb="Institutional SNPs", scene="farm",
     title="Institutional SNPs (I-SNP) in Indiana | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Indiana for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Indiana Medicaid and PathWays for Aging.",
     llm="Institutional Special Needs Plans (I-SNP) in Indiana for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Indiana",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Indiana, many people in long-term care also qualify for Medicaid, and those 60 and older receive it through PathWays for Aging; a D-SNP aligned with the PathWays plan may then be the better fit, and we compare the two."],
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
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP aligned with PathWays for Aging</a> if Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Indiana Medicaid &amp; PathWays for Aging</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Indiana county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with PathWays for Aging.")],
     sources=[SRC_MA_GOV, SRC_PATHWAYS], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="coveredbridge",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Indiana agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Indiana agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling the farm, taking a lump-sum pension, or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed, and the rules for Hoosier teachers and public employees with a pension.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Indiana, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Indiana. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Indiana?", "The book covers Medicare and retirement decisions nationally. For Indiana specifics &mdash; the Medigap birthday rule, PathWays for Aging, hospital-system networks, retiree plans &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
