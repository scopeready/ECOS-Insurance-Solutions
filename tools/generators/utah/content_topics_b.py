"""Utah topic pages, part B: costs, turning 65, snowbirds, veterans, Medicaid, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_UID, SRC_DAAS, SRC_SHIP_UT, SRC_UT_MEDICAID, SRC_DWS, SRC_TFL, SRC_VA)
from costs_page import costs_page
SRC_AZ = ("Medicare Enrollment Arizona (sister site with Mesa and Sun City offices)", "https://www.medicareenrollmentarizona.com")
SRC_NV = ("Medicare Enrollment Nevada (sister site)", "https://medicareenrollmentnevada.com")

TOPICS_B = [
costs_page("saltlake",
    "On the Wasatch Front the usual surprises are the sale of a house that tripled in value, a business sale, or a Roth conversion two years back.",
    "Possibly. Utah&rsquo;s Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through the Department of Workforce Services at jobs.utah.gov/mycase or 1-866-435-7414; Utah SHIP (800-541-7735) can walk you through it. See our Utah Medicaid page.",
    [SRC_CMS, SRC_COSTS, SRC_DWS]),

dict(slug="turning-65", nav_title="Turning 65 in Utah guide", crumb="Turning 65", scene="wasatch",
     title="Turning 65 in Utah: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Utah: your 7-month enrollment window, the Medigap open enrollment that does not repeat here, the Intermountain-or-the-U question, still-working rules, and a checklist. Free help from a licensed Utah agent.",
     llm="Turning 65 in Utah: enrollment windows, the parts of Medicare, the Intermountain vs University of Utah network question, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Utah: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Utah, where the plan you pick is mostly a decision about which hospital system you live in.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In Utah it does not repeat: no birthday rule, no annual switching window.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Utah twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
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
<li><strong>Part C (Medicare Advantage)</strong> &mdash; a private all-in-one alternative that bundles A, B and usually drug coverage; in Utah, usually built on one hospital system.</li>
<li><strong>Part D</strong> &mdash; prescription drug coverage.</li>
<li><strong>Medigap</strong> &mdash; a supplement that pairs with A and B and works anywhere in the country.</li>
</ul>
<h2>3. Your big decision: two paths, and one Utah question</h2>
<table class="ctable">
<caption>The two ways most Utahns put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Intermountain, the U, MountainStar and Holy Cross all covered, no network; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a network that, in Utah, usually follows one hospital system.</td></tr>
</tbody></table>
<p>The Utah question is which system your doctors belong to. If your family doctor is at an Intermountain clinic and your specialists are at Intermountain Medical Center, a Select Health plan or another Intermountain-network plan can fit well. If you see a doctor at the U, or might need Huntsman, the answer changes. If you are not sure, or if you split between systems, a Medigap policy removes the question. Our research site sets the two deadlines side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/utah">turning 65 in Utah</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no Utah insurer can turn you down or charge more for your health. Afterward, Utah insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Utah&rsquo;s big employers &mdash; the state, the universities, Intermountain, the school districts, Hill AFB civilian jobs &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll. State retirees with PEHP coverage have their own rules; ask us.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Write down which hospital system each of your doctors belongs to.</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll.</li>
<li>If you winter in St. George, Mesquite or Arizona, read the <a href="/snowbirds">snowbird guide</a> first; if you are a veteran or Hill AFB retiree, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">the savings programs</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Utahns sort through it every day &mdash; clearly, patiently, and at no cost to you. Utah SHIP (800-541-7735) offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Utah?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel and budget, and in Utah on whether your care sits inside one hospital system. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in Utah?", "The network question is a system question (Intermountain, the U, MountainStar, Holy Cross), your Medigap open enrollment does not repeat here, and a lot of Utahns winter out of state, which favors a supplement.")],
     sources=[SRC_CMS, SRC_UID, SRC_DAAS, SRC_SHIP_UT], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Utah"),

dict(slug="snowbirds", nav_title="Medicare for Utah snowbirds (St. George, Mesquite, Arizona)", crumb="Snowbirds", scene="redcliffs",
     title="Medicare for Utah Snowbirds: St. George, Mesquite &amp; Arizona | ECOS Medicare Solutions",
     desc="Which Utah Medicare plans work when you winter in St. George, Mesquite or Arizona: Medigap travels, most Advantage HMOs cover emergencies only, county rules for St. George, and our Arizona and Nevada sister sites.",
     llm="Medicare for Utah snowbirds and second-home owners: St. George (in-state, county rules), Mesquite and Arizona (out of state), which plans work, residency, Part D away from home",
     eyebrow="Guide · Winters south", h1="Medicare for Utah snowbirds: St. George, Mesquite and Arizona",
     sub="Half the Wasatch Front seems to head south in January. Whether your winter place is in Washington County, across the line in Mesquite, or down in Mesa, here is which plans follow you and which stop at the county line.",
     keyfacts=["A Medigap policy with Original Medicare works with any provider in the U.S. that accepts Medicare &mdash; St. George, Mesquite, Mesa or Yuma &mdash; all year. It is the simplest two-home coverage there is.",
               "St. George is still Utah, but Medicare Advantage and Part D plans are sold by county: a Salt Lake County HMO covers St. George Regional only as an out-of-network or emergency provider unless the plan includes Washington County.",
               "Most Advantage HMOs cover only emergencies and urgent care outside their service area; some PPOs cover routine care out of network at higher cost; a few plans have a travel benefit.",
               "Your plan is tied to the county of your permanent residence. Wintering away does not change that; changing your legal residence does, and it opens a Special Enrollment Period."],
     body="""<p>Utah&rsquo;s snowbirds have a shorter migration than most: down I-15 to St. George, over the line to Mesquite, or on to Arizona. The Medicare rules are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>Which plans travel</h2>
<table class="ctable">
<caption>How each plan type behaves once you are outside its service area. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Routine care in St. George, Mesquite or Arizona</th><th scope="col">What you pay there</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Medigap</th><td>Any provider that accepts Medicare</td><td>Same as at home &mdash; the supplement pays its share anywhere</td></tr>
<tr><th scope="row">Medicare Advantage PPO</th><td>Out-of-network providers, if the plan allows</td><td>Higher out-of-network copays or coinsurance; check the plan&rsquo;s out-of-network maximum</td></tr>
<tr><th scope="row">Medicare Advantage HMO</th><td>Emergencies and urgent care only, on most plans</td><td>Routine care generally not covered out of area</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Preferred-pharmacy pricing may differ; check that a chain near your winter home is preferred</td></tr>
</tbody></table>
<h2>St. George is Utah, but it is a different county</h2>
<p>This catches people every year. Advantage and Part D plans are sold by county, and a plan from Salt Lake, Utah or Davis County covers Washington County providers only as its rules allow &mdash; usually emergencies only for an HMO, out-of-network rates for a PPO. Some Utah plans, including some Select Health plans, cover both ends of I-15 in-network; many do not. If you winter in St. George on a Wasatch Front Advantage plan, we check the plan&rsquo;s service area and whether Intermountain St. George Regional is in-network before anything else.</p>
<div class="note-box"><p><strong>A few Advantage plans offer a &ldquo;visitor&rdquo; or &ldquo;travel&rdquo; benefit</strong> that extends in-network coverage for up to six or twelve months away from home, and some national carriers let you use their network in other states. It is plan-specific and it changes. If a travel benefit is the reason you are choosing an Advantage plan, we get it in writing from the Evidence of Coverage before you enroll.</p></div>
<h2>Mesquite and Arizona</h2>
<p>Across the state line the picture is simpler and harsher: an out-of-state HMO covers emergencies and urgent care, and that is it. A Medigap policy covers Mesa View in Mesquite, Banner in Mesa, or Yuma Regional the same way it covers Intermountain at home. If you are on an Advantage plan and spend four or five months in Arizona every year, the honest comparison is a Medigap policy or a PPO with a documented travel benefit. Our sister sites cover the other end: <a href="https://medicareenrollmentnevada.com">Medicare Enrollment Nevada</a> and <a href="https://www.medicareenrollmentarizona.com">Medicare Enrollment Arizona</a>, which has offices in Mesa and Sun City.</p>
<h2>Residency: the rule that decides everything</h2>
<p>You must live in a county-based plan&rsquo;s service area &mdash; meaning your <em>permanent</em> residence. Wintering away for four or five months does not change that; most plans allow up to six months, and some up to twelve, out of area before they disenroll you. What does change it is moving your legal residence: registering to vote, licensing the car, filing as an Arizona or Nevada resident. That triggers a Special Enrollment Period, ends your Utah plan, and means choosing from the plans sold in your new county. A Medigap policy is different: once issued it stays in force wherever you live, though the premium may be re-rated to the new state.</p>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so filling a prescription in St. George or Mesa is not a problem. Pricing can be: plans have <em>preferred</em> pharmacies where copays are lowest, and the Smith&rsquo;s that is preferred at home may not have a preferred counterpart near your winter place. Mail order at 90-day supplies solves most of it. We check both ZIP codes when we compare plans.</p>""",
     faqs=[("Does my Salt Lake Advantage plan work in St. George?", "Only as the plan&rsquo;s rules allow. Plans are sold by county; an HMO from Salt Lake County usually covers emergencies only in Washington County unless its service area includes it, and some Utah plans do cover both. We check the service area and whether St. George Regional is in-network before you enroll."),
           ("Does a Utah Medigap policy work in Mesquite or Arizona?", "Yes. A Medigap policy pays alongside Original Medicare with any provider in the country that accepts Medicare, with no network and no service area."),
           ("How long can I be out of state without losing my Advantage plan?", "It depends on the plan; most allow up to six months out of the service area, some up to twelve. Changing your legal residence ends the plan regardless of time, and gives you a Special Enrollment Period to pick a plan where you live now."),
           ("Can you help me if I become an Arizona or Nevada resident?", "Yes. Our agency is licensed in Arizona and Nevada as well as Utah, with offices in Mesa and Sun City through our Arizona site, so we help you move your coverage cleanly, including the Medigap switching rules that differ by state.")],
     sources=[SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_AZ, SRC_NV], cta="Wintering south? Let&rsquo;s make sure your plan comes with you."),

dict(slug="veterans", nav_title="Medicare for Utah veterans and Hill AFB retirees", crumb="Veterans", scene="hillafb",
     title="Medicare for Utah Veterans: TRICARE For Life &amp; the VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (the Wahlen VA in Salt Lake and its Ogden, Provo, St. George and Logan clinics) work with Medicare in Utah, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision.",
     llm="Medicare for Utah veterans and Hill AFB retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, the Wahlen VA and its clinics",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Utah veterans and Hill AFB retirees",
     sub="How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Utah&rsquo;s VA care runs through the George E. Wahlen VA Medical Center in Salt Lake City and community clinics in Ogden, Provo, St. George, Logan, Price, Roosevelt and elsewhere.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Utah is home to roughly 120,000 veterans and, around Hill Air Force Base, one of the Mountain West&rsquo;s largest military-retiree communities. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; Intermountain or the U with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Hill AFB after 65</h2>
<p>The 75th Medical Group clinic on base continues to see retirees on a space-available basis under TRICARE rules; Medicare does not pay there. Most Hill retirees pair TFL with civilian care at Intermountain Layton, McKay-Dee or Ogden Regional. Our <a href="/hill-afb">Hill Air Force Base page</a> walks through the neighborhood specifics.</p>
<h2>Which Utah plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Utah Department of Veterans and Military Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at the Wahlen VA or the Hill AFB clinic?", "No. Medicare does not pay at VA or military facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Utah Medicaid: Medicare Savings Programs, Extra Help, D-SNPs", crumb="Utah Medicaid &amp; savings programs", scene="utahvalley",
     title="Medicare &amp; Utah Medicaid: QMB, SLMB &amp; Extra Help | ECOS Medicare Solutions",
     desc="How Medicare works with Utah Medicaid: the Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, Dual Special Needs Plans, and where to apply (Department of Workforce Services, myCase).",
     llm="Medicare and Utah Medicaid (dual eligible): Medicare Savings Programs (QMB/SLMB/QI) through the Department of Workforce Services, Extra Help, D-SNPs, the Aging Waiver",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Utah Medicaid: the savings programs that pay your premiums",
     sub="If you qualify for both Medicare and Utah Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in Utah, and where to apply.",
     keyfacts=["Utah Medicaid is run by the Utah Department of Health and Human Services; eligibility is determined by the Department of Workforce Services. Apply at jobs.utah.gov/mycase, by phone at 1-866-435-7414, or at a DWS office.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. Utah uses the federal income and resource limits, which change each year.",
               "Qualifying for a Medicare Savings Program or Medicaid automatically qualifies you for Extra Help with Part D costs.",
               "Dual Special Needs Plans (D-SNPs) are Advantage plans for people with both Medicare and Medicaid. Free counseling: Utah SHIP, 800-541-7735."],
     body="""<p>Some Utahns qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Utah Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home through the Aging Waiver or in a nursing facility.</p>
<h2>How Medicaid works for seniors in Utah</h2>
<p>Utah Medicaid is administered by the <strong>Utah Department of Health and Human Services</strong>, and eligibility is determined by the <strong>Department of Workforce Services (DWS)</strong> &mdash; not by an insurance agency. For adults 65 and over, eligibility is based on income and resources under the aged rules. You apply online at jobs.utah.gov/mycase, by phone at 1-866-435-7414, or at a DWS employment center; county aging offices and Utah SHIP counselors can help with the paperwork.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Utah uses the federal income and resource limits, which change each year. You apply through DWS, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact. Availability varies by Utah county.</li>
<li><strong>The Aging Waiver</strong> pays for in-home services for people 65 and over who would otherwise need a nursing facility; ask your local Area Agency on Aging.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from Utah SHIP &mdash; the Senior Health Insurance Information Program, run by the Division of Aging and Adult Services &mdash; at 800-541-7735. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with DWS, the state and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Utah Medicaid, the Utah Department of Health and Human Services, the Department of Workforce Services, or the federal Medicare program.</p>""",
     faqs=[("Who counts as dual eligible in Utah?", "People who qualify for both Medicare and Utah Medicaid. There are full and partial categories; eligibility is determined by the Department of Workforce Services and CMS, based on income and resources."),
           ("Can Utah Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through DWS at jobs.utah.gov/mycase; Utah SHIP (800-541-7735) can help."),
           ("Where do I apply for Medicaid if I am over 65?", "Through the Department of Workforce Services: online at jobs.utah.gov/mycase, by phone at 1-866-435-7414, or at a DWS employment center."),
           ("What is a D-SNP?", "A Dual Special Needs Plan is a Medicare Advantage plan built for people who have both Medicare and Medicaid. It coordinates both programs, usually at $0 plan premium, and often adds extra benefits while you keep your Medicaid coverage.")],
     sources=[SRC_UT_MEDICAID, SRC_DWS, SRC_DAAS, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Utah Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Utah", crumb="Chronic SNPs", scene="hoodoos",
     title="Chronic SNPs (C-SNP) in Utah | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Utah: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Utah for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Utah",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Utah county and is concentrated along the Wasatch Front; a regular Advantage plan or a Medigap policy may still serve you better.",
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the Intermountain-or-the-U question applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Utah Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Utah?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Utah", crumb="Institutional SNPs", scene="wasatch",
     title="Institutional SNPs (I-SNP) in Utah | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Utah for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Utah Medicaid.",
     llm="Institutional Special Needs Plans (I-SNP) in Utah for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Utah",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Utah, many people in long-term care also qualify for Medicaid; a D-SNP may then be the better fit, and we compare the two."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul><li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li><li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment.</li></ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP</a> if Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Utah Medicaid &amp; savings programs</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Utah county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with Medicaid.")],
     sources=[SRC_MA_GOV, SRC_UT_MEDICAID], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="aspens",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Utah agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Utah agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling a house on the Wasatch Front or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, and how much of it is taxed &mdash; including Utah&rsquo;s own treatment of benefits.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Utah, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Utah. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Utah?", "The book covers Medicare and retirement decisions nationally. For Utah specifics &mdash; the Intermountain-or-the-U question, St. George winters, Hill AFB &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
