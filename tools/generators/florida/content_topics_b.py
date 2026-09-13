"""Florida topic pages, part B: costs, turning 65, new to Florida, hurricanes, veterans, Medicaid, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_SHINE, SRC_FLOIR, SRC_KFF_MEDIGAP, SRC_ACCESS, SRC_AHCA, SRC_ELDER_HELP, SRC_CMS_HURR, SRC_SEP, SRC_TFL, SRC_VA)
from costs_page import costs_page
SRC_MN_SNOW = ("Minnesota Medicare Enrollment (sister site): Medicare for Minnesota snowbirds", "https://minnesotamedicareenrollment.com/snowbirds")
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, the rules state by state", "https://www.mymedigaprate.com/switching-medigap-plans")

TOPICS_B = [
costs_page("keys",
    "In Florida the usual surprises are the sale of a house up north the year you moved, a Roth conversion, or a big capital gain two years back.",
    "Possibly. Florida&rsquo;s Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through the Department of Children and Families at myaccessflorida.com; SHINE (1-800-963-5337) can walk you through it. See our Florida Medicaid page.",
    [SRC_CMS, SRC_COSTS, SRC_ACCESS]),

dict(slug="turning-65", nav_title="Turning 65 in Florida guide", crumb="Turning 65", scene="beach",
     title="Turning 65 in Florida: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Florida: your 7-month enrollment window, why Florida's issue-age Medigap rule rewards buying now, still-working rules, the deadlines with lifelong penalties, and a checklist. Free help from a licensed Florida agent.",
     llm="Turning 65 in Florida: enrollment windows, the parts of Medicare, why issue-age Medigap rating rewards buying at 65, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Florida: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Florida, where the age you buy a Medigap policy sets its price for life.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In Florida it does not repeat, and because Florida requires issue-age rating, a policy bought at 65 is priced at 65 for life.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Florida twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
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
<li><strong>Part C (Medicare Advantage)</strong> &mdash; a private all-in-one alternative that bundles A, B and usually drug coverage, sold by county; the way most Floridians go.</li>
<li><strong>Part D</strong> &mdash; prescription drug coverage.</li>
<li><strong>Medigap</strong> &mdash; a supplement that pairs with A and B and works anywhere in the country; issue-age rated in Florida.</li>
</ul>
<h2>3. Your big decision: two paths</h2>
<table class="ctable">
<caption>The two ways most Floridians put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G, N or high-deductible G) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; a premium that is higher in Florida but priced at your buying age for life.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly, and changed a lot for [[YEAR]].</td></tr>
</tbody></table>
<p>Florida&rsquo;s issue-age rule tilts the timing. If you think you will ever want a Medigap policy, the cheapest it will ever be is at 65, in your open enrollment, with no health questions. If Mayo, Moffitt, Cleveland Clinic or UHealth is in your future, or you split the year with another state, a supplement removes the network question. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>. Our research site sets the two deadlines side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/florida">turning 65 in Florida</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no Florida insurer can turn you down or charge more for your health. Afterward, Florida insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Florida&rsquo;s big employers &mdash; the state, the school districts, the universities, the hospital systems, Publix, Disney &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll. State and county retirees with Florida Retirement System coverage have their own rules; ask us.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Decide whether you will ever want a Medigap policy &mdash; in Florida, the answer decides when to buy it.</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if a specific institution is your care.</li>
<li>If you just moved here or split the year, read the <a href="/new-to-florida">new-to-Florida guide</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">the savings programs</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Floridians sort through it every day &mdash; clearly, patiently, and at no cost to you. SHINE (1-800-963-5337) offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Florida?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel and budget. Florida&rsquo;s Advantage menu is deep but changed a lot for [[YEAR]]; Florida&rsquo;s Medigap premiums are high but issue-age rated. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in Florida?", "Medigap is issue-age rated, so the age you buy sets the price for life and your six-month window at 65 matters more than in most states; the Advantage market is the largest and most changeable in the country; and a lot of people arrive here on Medicare from another state, which has its own rules.")],
     sources=[SRC_CMS, SRC_KFF_MEDIGAP, SRC_FLOIR, SRC_SHINE], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Florida"),

dict(slug="new-to-florida", nav_title="Moving to Florida on Medicare, and Medicare for snowbirds", crumb="New to Florida", scene="keys",
     title="Moving to Florida on Medicare &amp; Snowbird Coverage | ECOS Medicare Solutions",
     desc="What a move to Florida does to your Medicare: the Special Enrollment Period, county-based plan menus, keeping or replacing a Medigap policy, why rights differ from New York or Connecticut, and which plans work when you split the year.",
     llm="Moving to Florida on Medicare: the Special Enrollment Period a move opens, county-based Advantage and Part D menus, keeping an out-of-state Medigap policy, losing continuous guaranteed issue from NY/CT/MA/ME, and which plans work for snowbirds",
     eyebrow="Guide · New residents &amp; snowbirds", h1="Moving to Florida on Medicare, and Medicare for snowbirds",
     sub="Nobody arrives in Florida without a Medicare plan; the question is whether the one you brought still works here. Here is what a move does to your coverage, what a winter does, and what to do about each.",
     keyfacts=["Medicare Advantage and Part D plans are sold by county. Changing your permanent residence to Florida ends your old plan and opens a Special Enrollment Period, generally two months after the move, to pick plans sold in your new county.",
               "A Medigap policy from another state usually stays in force after a move, re-rated to Florida&rsquo;s prices, which are higher. Whether to keep it or replace it is a real comparison, and issue-age rating changes the math.",
               "New York, Connecticut, Massachusetts and Maine let residents buy or switch Medigap without underwriting year-round; Florida does not. Moving here past 65 does not create a Florida guaranteed-issue right for Medigap.",
               "If you winter here without moving, your plan from home applies: a Medigap policy works anywhere; most Advantage HMOs cover only emergencies in Florida."],
     body="""<p>Florida gains more new residents on Medicare every year than any other state, and every one of them brings a plan built for somewhere else. Whether you are moving here for good or wintering here from Minnesota, the rules are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>If you are moving to Florida</h2>
<h3>Your Advantage or Part D plan does not come with you</h3>
<p>Medicare Advantage and Part D plans are sold by county, and you must live in the plan&rsquo;s service area &mdash; meaning your <em>permanent</em> residence. When you move that residence to Florida, your old plan ends and you get a <strong>Special Enrollment Period</strong>: generally the month you tell the plan plus two more months, to enroll in plans sold in your new county. Use it. If you miss it you are on Original Medicare with no drug coverage until the next Annual Election Period, and the Part D penalty clock is running.</p>
<h3>Your Medigap policy probably does</h3>
<p>A Medigap policy is not tied to a county. Once issued it stays in force wherever you live, though the carrier will usually re-rate it to Florida&rsquo;s pricing, which runs above most states&rsquo;. You can keep it. Whether you should is a comparison: your existing policy may be attained-age rated and climbing every birthday, while a new Florida policy would be issue-age rated at your current age &mdash; but buying the new one may require underwriting, because a move alone does not create a Florida guaranteed-issue right for Medigap. We run the comparison with your actual premium and rate history in hand; the state-by-state rules are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>
<div class="warn-box"><p><strong>Moving from New York, Connecticut, Massachusetts or Maine?</strong> Those states let residents buy or switch Medigap without health questions year-round. Florida does not. If you are past 65 and think you might ever want a Medigap policy, buy it &mdash; or keep the one you have &mdash; <em>before</em> you change your residence. Once you are a Floridian, the only guaranteed windows are the ones on our <a href="/medicare-supplement">Medigap page</a>.</p></div>
<h3>Your county decides your menu</h3>
<p>The Florida menu is deep in Miami-Dade, Broward, Palm Beach, Hillsborough, Pinellas, Orange and the Villages corridor, and thinner in the Panhandle, the Keys and the rural interior. Which hospital systems a plan includes matters more than the premium; our <a href="/#areas">city and region pages</a> name them county by county.</p>
<h2>If you are a snowbird</h2>
<p>If you keep your permanent residence up north and winter here, your plan from home applies in Florida exactly as its rules say. A <strong>Medigap policy</strong> with Original Medicare covers Baptist, Cleveland Clinic, Lee Health or Sarasota Memorial the same way it covers your hospital at home. An <strong>Advantage HMO</strong> from Ohio or Minnesota covers emergencies and urgent care here and, on most plans, nothing else; a PPO may cover routine care out of network at higher cost; a few plans have a travel benefit that extends in-network coverage for up to six or twelve months. Wintering away for four or five months does not change your residence; most plans allow up to six months, some up to twelve, out of area before they disenroll you. Our Minnesota site covers the same question from the other end: <a href="https://minnesotamedicareenrollment.com/snowbirds">Medicare for Minnesota snowbirds</a>.</p>
<table class="ctable">
<caption>How each plan type from your home state behaves in Florida. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Routine care in Florida</th><th scope="col">What you pay here</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Medigap</th><td>Any provider that accepts Medicare</td><td>Same as at home &mdash; the supplement pays its share anywhere</td></tr>
<tr><th scope="row">Medicare Advantage PPO</th><td>Out-of-network providers, if the plan allows</td><td>Higher out-of-network copays or coinsurance; check the out-of-network maximum</td></tr>
<tr><th scope="row">Medicare Advantage HMO</th><td>Emergencies and urgent care only, on most plans</td><td>Routine care generally not covered out of area</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Preferred-pharmacy pricing may differ; check that Publix, CVS or Walgreens near you is preferred</td></tr>
</tbody></table>
<h2>Part D away from home</h2>
<p>Every Part D plan has a national pharmacy network, so filling a prescription in Naples or Nashua is not a problem. Pricing can be: plans have <em>preferred</em> pharmacies where copays are lowest, and Publix, which is preferred in many Florida plans, may not exist where you summer. Mail order at 90-day supplies solves most of it. We check both ZIP codes when we compare plans.</p>""",
     faqs=[("I just moved to Florida. How long do I have to pick a new plan?", "A permanent move out of your plan&rsquo;s service area opens a Special Enrollment Period: generally the month you notify the plan plus two more months, to enroll in Advantage or Part D plans sold in your new county. Miss it and you wait for the Annual Election Period."),
           ("Can I keep my Medigap policy from another state after moving to Florida?", "Usually yes. The policy stays in force and is typically re-rated to Florida&rsquo;s premiums. Whether to keep it or replace it depends on its rating method and rate history versus a new Florida issue-age policy, and replacing it may require underwriting. We run the comparison."),
           ("Does my Ohio or Minnesota Advantage plan work in Florida for the winter?", "For emergencies and urgent care, yes. For routine care, most HMOs do not; some PPOs cover out-of-network care at higher cost, and a few plans have a travel benefit. Read the Evidence of Coverage, and if travel is why you chose the plan, get the benefit in writing."),
           ("I am moving from New York. Do I keep my right to buy Medigap any time?", "No. New York&rsquo;s continuous guaranteed issue is a New York rule. Once you are a Florida resident past 65, Medigap is underwritten outside the guaranteed windows. If you may ever want a policy, buy or keep one before you change your residence.")],
     sources=[SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_SEP, SRC_KFF_MEDIGAP, SRC_MMR_SWITCH, SRC_MN_SNOW], cta="New to Florida? Let&rsquo;s make sure your plan made the move with you."),

dict(slug="hurricanes", nav_title="Hurricanes and Medicare: disaster Special Enrollment Periods and refills", crumb="Hurricanes &amp; Medicare", scene="everglades",
     title="Hurricanes &amp; Medicare in Florida: Disaster SEP, Refills &amp; Deadlines | ECOS Medicare Solutions",
     desc="What a FEMA hurricane declaration does to your Medicare in Florida: the disaster Special Enrollment Period if you missed a deadline, early Part D refills, out-of-network care during an evacuation, and what to keep in your go-bag.",
     llm="Hurricanes and Medicare in Florida: the FEMA disaster Special Enrollment Period, early Part D refills and relaxed pharmacy rules, out-of-network care during evacuation, documents to keep",
     eyebrow="Guide · Storm season", h1="Hurricanes and Medicare: what a disaster declaration changes",
     sub="Every Floridian on Medicare will sit through a hurricane season. Here is what a FEMA declaration does to your enrollment deadlines, your prescriptions and your care when you evacuate &mdash; before you need it.",
     keyfacts=["If a FEMA-declared emergency or major disaster kept you from making a Medicare enrollment decision during a valid window, you get a Special Enrollment Period to make it afterward. It covers residents of the declared counties and people who help them enroll.",
               "During a declared emergency, Part D plans in the affected area must lift refill-too-soon limits, allow out-of-network pharmacies, and relax prior-authorization rules for medications you already take.",
               "Medicare Advantage plans must cover care at out-of-network providers at in-network cost-sharing when the disaster makes in-network care unavailable, and must waive referral requirements. Original Medicare works anywhere.",
               "Keep your Medicare card, plan cards, a current medication list and your doctors&rsquo; names in your go-bag; Medicare.gov and your plan&rsquo;s app can replace the cards, but not in a shelter with no signal."],
     body="""<p>Ian, Idalia, Helene, Milton: Florida has learned that a hurricane changes more than the roof. Medicare has a set of rules that switch on when the President or FEMA declares an emergency or major disaster, and they are worth knowing in June rather than in October.</p>
<h2>The disaster Special Enrollment Period</h2>
<p>If you were eligible to make a Medicare enrollment decision during a valid window &mdash; the Annual Election Period, the Medicare Advantage Open Enrollment Period, your Initial Enrollment Period, or another Special Enrollment Period &mdash; and a FEMA-declared emergency or major disaster kept you from making it, you get a Special Enrollment Period to make that decision afterward. It applies to people who live in the declared counties and to people who rely on someone in those counties to help them enroll, and it generally runs from the start of the incident until two months after it ends, or until the declaration is lifted. It does not give you a second bite at a decision you made on time; it gives you the bite you missed.</p>
<div class="note-box"><p><strong>How to use it.</strong> Call your plan, 1-800-MEDICARE, or us, say that you were affected by the named storm and missed the deadline, and name the county. You do not have to prove damage. The plan must process the election.</p></div>
<h2>Prescriptions before, during and after the storm</h2>
<p>Once an emergency is declared for your area, Part D plans must allow early refills (the &ldquo;refill too soon&rdquo; edit is lifted), must cover fills at out-of-network pharmacies when yours is closed, and must relax prior-authorization and step-therapy requirements for medications you were already taking. Get a refill as soon as a hurricane <em>watch</em> is posted &mdash; pharmacies close before the warning &mdash; and take the medication list with you. If you are on insulin, a refrigerated drug, or oxygen, tell your plan and your county&rsquo;s special-needs shelter registry now, not in September.</p>
<h2>Care when you have evacuated</h2>
<p>Original Medicare and a Medigap policy work anywhere in the country, so an evacuee in Atlanta or Birmingham is covered as if at home. Medicare Advantage plans, during a declared disaster, must cover care from out-of-network providers at in-network cost-sharing when in-network care is unavailable, must waive referral requirements, and must not charge more than in-network rates. That protection ends when the declaration does, so if you stay away long, call the plan.</p>
<h2>After the storm</h2>
<p>If you lost your Medicare card or plan cards, Medicare.gov and your plan&rsquo;s member site can replace them, and a pharmacy can usually look you up by name and date of birth. If your doctor&rsquo;s office was destroyed and you had to change doctors, that is a network question we can help with. And if the storm made you rethink where you want to live, a move to another county opens its own Special Enrollment Period; see <a href="/new-to-florida">moving to Florida</a>.</p>
<h2>The go-bag list</h2>
<ul>
<li>Medicare card, Medigap or Advantage card, Part D card (or photos of each on your phone).</li>
<li>A current medication list with doses, and at least a two-week supply.</li>
<li>Your doctors&rsquo; names and phone numbers, and your pharmacy&rsquo;s.</li>
<li>Your plan&rsquo;s member-services number, 1-800-MEDICARE, and SHINE (1-800-963-5337).</li>
<li>If you use a special-needs shelter, your county registration.</li>
</ul>""",
     faqs=[("I missed the Annual Election Period because of the hurricane. Can I still change plans?", "If you lived in a county under a FEMA emergency or major disaster declaration during the election period, or relied on someone who did, you get a Special Enrollment Period to make the election you missed, generally through two months after the incident period ends. Call your plan, 1-800-MEDICARE or us and name the storm and the county."),
           ("Can I get an early refill before a hurricane?", "Yes, once an emergency is declared for your area. Part D plans must lift refill-too-soon limits and allow out-of-network pharmacies in the affected area. Ask your pharmacy as soon as a watch is posted."),
           ("Does my Medicare Advantage plan cover me if I evacuate out of state?", "During a declared disaster, yes: the plan must cover out-of-network care at in-network cost-sharing when in-network care is unavailable and must waive referrals. Outside a declaration, most HMOs cover only emergencies out of area."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans, and helping you use a disaster Special Enrollment Period, is free to you.")],
     sources=[SRC_SEP, SRC_CMS_HURR, SRC_SHINE], cta="Storm season question? Ask before the watch is posted.", about="Medicare rules during FEMA-declared disasters"),

dict(slug="veterans", nav_title="Medicare for Florida veterans and military retirees", crumb="Veterans", scene="macdill",
     title="Medicare for Florida Veterans: TRICARE For Life &amp; the VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Miami, West Palm Beach, Tampa, Bay Pines, Orlando, Gainesville) work with Medicare in Florida, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision.",
     llm="Medicare for Florida veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, Florida VA systems, the Jacksonville, MacDill and Pensacola-Eglin communities",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Florida veterans and military retirees",
     sub="Florida has the third-largest veteran population in the country. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Florida&rsquo;s VA care runs through the Miami, West Palm Beach, Tampa (Haley), Bay Pines, Orlando and North Florida/South Georgia (Gainesville, Lake City) systems, with clinics in nearly every county.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Florida is home to roughly 1.4 million veterans and the retiree communities of NAS Jacksonville and Mayport, MacDill, NAS Pensacola, Whiting Field, Eglin, Hurlburt, Tyndall and Patrick. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; Mayo or Baptist with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Military hospitals after 65</h2>
<p>Naval Hospital Jacksonville, Naval Hospital Pensacola, the Eglin hospital and the MacDill clinic continue to see retirees on a space-available basis under TRICARE rules. Medicare does not pay there. Most Florida military retirees pair TFL with civilian care nearby, and we have pages for the three big retiree communities: <a href="/jacksonville-navy">NAS Jacksonville and Mayport</a>, <a href="/macdill-afb">MacDill</a>, and <a href="/pensacola-eglin">Pensacola and Eglin</a>.</p>
<h2>Which Florida plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Florida Department of Veterans&rsquo; Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at the Tampa or Miami VA, or at Naval Hospital Jacksonville?", "No. Medicare does not pay at VA or military facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Florida Medicaid: Medicare Savings Programs, SMMC, Extra Help, D-SNPs", crumb="Florida Medicaid &amp; savings programs", scene="everglades",
     title="Medicare &amp; Florida Medicaid: QMB, SLMB, SMMC &amp; D-SNPs | ECOS Medicare Solutions",
     desc="How Medicare works with Florida Medicaid: the Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, the SMMC long-term care program, aligned Dual Special Needs Plans, and where to apply (ACCESS Florida).",
     llm="Medicare and Florida Medicaid (dual eligible): Medicare Savings Programs (QMB/SLMB/QI) through DCF's ACCESS Florida, Extra Help, SMMC Long-Term Care, aligned D-SNPs",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Florida Medicaid: the programs that pay your premiums and your care",
     sub="If you qualify for both Medicare and Florida Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less, and Florida lines up its D-SNPs with its Medicaid plans so one company can coordinate both. Here is how it works, and where to apply.",
     keyfacts=["Florida Medicaid is administered by the Agency for Health Care Administration; eligibility is determined by the Department of Children and Families through ACCESS Florida (myaccessflorida.com). Florida did not expand Medicaid, so seniors qualify under the aged rules.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. Florida uses the federal income limits, which change each year. Apply through DCF.",
               "Qualifying for a Medicare Savings Program or Medicaid automatically qualifies you for Extra Help with Part D costs.",
               "Long-term care at home or in a nursing facility runs through the Statewide Medicaid Managed Care Long-Term Care program, and Florida aligns Dual Special Needs Plans with Medicaid plans so one organization coordinates both. Free counseling: SHINE, 1-800-963-5337."],
     body="""<p>Some Floridians qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Florida Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in Florida</h2>
<p>Florida Medicaid is administered by the <strong>Agency for Health Care Administration (AHCA)</strong>, and eligibility is determined by the <strong>Department of Children and Families (DCF)</strong> &mdash; not by an insurance agency. Florida did not expand Medicaid, so for adults 65 and over eligibility is based on income and assets under the aged-and-disabled rules. You apply through <strong>ACCESS Florida</strong> at myaccessflorida.com, by phone, or at a DCF service center; SHINE counselors and the Area Agencies on Aging can help with the paperwork. Once eligible, most seniors receive their Medicaid benefits through a <strong>Statewide Medicaid Managed Care</strong> plan.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Florida uses the federal income limits, which change each year. You apply through DCF, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>SMMC Long-Term Care</strong> pays for nursing-facility care and for in-home services that let people who would otherwise need a facility stay home. It has its own financial rules and a waiting list for home-based services; the Aging and Disability Resource Center in your region screens for it.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras. Florida requires D-SNPs to be aligned with a Medicaid managed-care plan from the same company, so a full-benefit dual eligible in a D-SNP can have one organization coordinating everything.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from SHINE &mdash; Serving Health Insurance Needs of Elders, Florida&rsquo;s State Health Insurance Assistance Program, run by the Department of Elder Affairs &mdash; at 1-800-963-5337. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with DCF, AHCA and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Florida Medicaid, the Agency for Health Care Administration, the Department of Children and Families, or the federal Medicare program.</p>""",
     faqs=[("Who counts as dual eligible in Florida?", "People who qualify for both Medicare and Florida Medicaid. There are full and partial categories; eligibility is determined by the Department of Children and Families and CMS, based on income and assets."),
           ("Can Florida Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through ACCESS Florida at myaccessflorida.com; SHINE (1-800-963-5337) can help."),
           ("Where do I apply for Medicaid if I am over 65?", "Through the Department of Children and Families: online at myaccessflorida.com, by phone, or at a DCF service center. Florida did not expand Medicaid, so eligibility for seniors follows the aged-and-disabled rules."),
           ("What is an aligned D-SNP?", "A Dual Special Needs Plan whose company also runs your Florida Medicaid managed-care plan. Florida requires that alignment, so one organization can coordinate your Medicare, Medicaid and long-term services.")],
     sources=[SRC_AHCA, SRC_ACCESS, SRC_ELDER_HELP, SRC_SHINE, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Florida Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Florida", crumb="Chronic SNPs", scene="everglades",
     title="Chronic SNPs (C-SNP) in Florida | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Florida: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Florida for qualifying chronic conditions",
     eyebrow="Your situation &middot; Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Florida",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match. Florida has more of them than almost any state.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Florida is one of the deepest C-SNP markets in the country, concentrated in South Florida, Tampa Bay and Central Florida; availability still varies by county, and a regular Advantage plan or a Medigap policy may serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition.</p>
<h2>Conditions that can qualify</h2>
<p>Medicare defines the chronic conditions a C-SNP can serve. Common examples include:</p>
<ul><li>Diabetes mellitus</li><li>Chronic heart failure and certain cardiovascular disorders</li><li>Chronic lung disorders such as COPD</li><li>End-stage renal disease (ESRD) requiring dialysis</li><li>Certain other qualifying chronic conditions</li></ul>
<p>You generally need a provider to verify that you have the qualifying condition in order to enroll, and a diagnosis gives you a Special Enrollment Period to join one outside the normal windows.</p>
<h2>What a C-SNP usually offers</h2>
<ul>
<li><strong>Care coordination</strong> tailored to your condition, often including a care team or coordinator, and in Florida frequently a clinic-based primary care model.</li>
<li><strong>A drug formulary</strong> built with your condition&rsquo;s medications in mind, plus included Part D coverage.</li>
<li><strong>Extra benefits</strong> that vary by plan, and frequently a $0 or low plan premium.</li>
</ul>
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a county network plan, so the question of whether your cardiologist, your dialysis center or Moffitt is in it applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Florida Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Florida?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Florida", crumb="Institutional SNPs", scene="liveoaks",
     title="Institutional SNPs (I-SNP) in Florida | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Florida for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Florida Medicaid long-term care.",
     llm="Institutional Special Needs Plans (I-SNP) in Florida for facility-level care",
     eyebrow="Your situation &middot; Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Florida",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Florida, many people in long-term care also qualify for Medicaid through the Statewide Medicaid Managed Care Long-Term Care program; a D-SNP aligned with that plan may then be the better fit, and we compare the two."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul><li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li><li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment; in Florida the CARES program at the Department of Elder Affairs does that assessment.</li></ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions, including adult children who live out of state.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming, and in Florida the adult child is often calling from another state. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP</a> if Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Florida Medicaid &amp; savings programs</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Florida county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with Florida Medicaid long-term care.")],
     sources=[SRC_MA_GOV, SRC_AHCA, SRC_ELDER_HELP], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence &mdash; free 295-page retirement guide", crumb="Free Retirement Guide", scene="citrus",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Florida agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Florida agent",
     eyebrow="Free 295-page guide &middot; 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling the house up north the year you moved to Florida or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, and how much of it is taxed &mdash; and why Florida&rsquo;s lack of an income tax changes only part of that.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Florida, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Florida. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Florida?", "The book covers Medicare and retirement decisions nationally. For Florida specifics &mdash; issue-age Medigap rating, the 2026 Advantage changes, moving here from up north, hurricanes, MacDill and the Jacksonville bases &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
