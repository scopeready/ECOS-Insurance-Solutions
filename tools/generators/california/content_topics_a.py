"""California topic pages, part A: Medicare Advantage, Medigap, Part D, Kaiser."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_HICAP = ("California Department of Aging: HICAP Medicare counseling (1-800-434-0222)", "https://aging.ca.gov/Programs_and_Services/Medicare_Counseling/")
SRC_INS_CODE = ("California Insurance Code &sect;10192.11: Medicare supplement open enrollment and the birthday rule", "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=10192.11")
SRC_CHA_RULES = ("California Health Advocates: California&rsquo;s unique Medigap rules and extra consumer rights", "https://cahealthadvocates.org/understanding-californias-unique-medigap-rules-extra-consumer-rights/")
SRC_CHA_OE = ("California Health Advocates: Medigap open enrollment, the birthday rule and guaranteed issue", "https://cahealthadvocates.org/medigap/open-enrollment/")
SRC_MRO = ("medicareresources.org: Medigap eligibility for people under 65, by state", "https://www.medicareresources.org/medicare-eligibility-and-enrollment/medigap-eligibility-for-americans-under-age-65-varies-by-state/")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_KIP = ("Kiplinger: major insurers scale back Medicare Advantage and Part D plans for 2026", "https://www.kiplinger.com/retirement/medicare/insurers-scale-back-medicare-advantage-and-part-d-plans-for-2026")
SRC_PPO = ("Medical Insurance Today: the 2026 PPO Advantage shake-up in California", "https://medicalinsurancetoday.com/2026-ppo-medicare-changes-california/")
SRC_KPIHP = ("Kaiser Permanente Institute for Health Policy: Kaiser Permanente&rsquo;s participation in Medicare Advantage in California", "https://www.kpihp.org/blog/at-a-glance-kaiser-permanentes-participation-in-medicare-advantage-in-california/")
SRC_MMR_CA = ("MyMedigapRate: California Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/california")
SRC_DHCS_ASSET = ("California DHCS: Medi-Cal asset limit FAQ (limit reinstated January 1, 2026)", "https://www.dhcs.ca.gov/medi-cal/help/asset-limit-frequently-asked-questions/")
SRC_JIA = ("Justice in Aging: reinstatement of the Medi-Cal asset limit, what to know", "https://justiceinaging.org/reinstatement-of-medi-cal-asset-limit-faq/")
SRC_DHCS_MMP = ("California DHCS: Medi-Medi Plans", "https://www.dhcs.ca.gov/services/medi-medi-plans/")
SRC_DHCS_DSNP = ("California DHCS: Dual Eligible Special Needs Plans in California", "https://www.dhcs.ca.gov/providers-partners/dual-eligible-special-needs-plans-in-california/")
SRC_CHA_MEDICAL = ("California Health Advocates: Medi-Cal for people with Medicare", "https://cahealthadvocates.org/low-income-help/medi-cal-for-people-with-medicare/")
SRC_CMS_FIRE = ("CMS: wildfire emergency response actions", "https://www.cms.gov/about-cms/what-we-do/emergency-response/past-emergencies/wildfires")
SRC_CMS_CAPHE = ("CMS: resources and flexibilities for the California public health emergency (January 2025 wildfires)", "https://www.cms.gov/newsroom/news-alert/cms-announces-resources-and-flexibilities-assist-public-health-emergency-state-california")
SRC_SEP = ("Medicare.gov: Special Enrollment Periods, including FEMA-declared disasters", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan/special-enrollment-periods")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in California", crumb="Medicare Advantage", scene="losangeles",
     title="Medicare Advantage Plans in California [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in California: medical groups and networks, $0 premiums, Kaiser, the 2026 PPO exits, and what to do if your plan was discontinued. Free help from a licensed California agent (CA License #0M00978).",
     llm="Medicare Advantage (Part C) in California: how delegated medical groups and networks work, Kaiser Senior Advantage, the 2026 Anthem PPO exit and county withdrawals, and what a discontinued plan gives you",
     eyebrow="Plan type · Medicare Advantage (Part C)", h1="Medicare Advantage plans in California",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a medical group and a county network, in the state where Kaiser wrote the model and the PPO menu shrank for [[YEAR]].",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a county-based network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "About half of California&rsquo;s Medicare beneficiaries are in Advantage plans, and Kaiser Permanente Senior Advantage alone covers more than 1.4 million of them. Outside Kaiser, most California Advantage plans assign you to a delegated medical group, which decides which specialists you can see.",
               "For 2026 Anthem Blue Cross ended its Advantage PPO plans in California, Aetna closed plans and left counties, UnitedHealthcare and Humana withdrew from counties nationally including rural California, and the state&rsquo;s plan count fell from 421 to 402.",
               "A discontinued plan gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage. Many plans add dental, vision, hearing, an over-the-counter allowance and a gym benefit.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (Parts A and B) with plan copays instead of Medicare&rsquo;s 20% coinsurance.</li>
<li><strong>Prescription drug coverage</strong> (Part D) in most plans; a few &ldquo;MA-only&rdquo; plans leave it out for people with TRICARE For Life or VA pharmacy.</li>
<li><strong>Extras</strong> that vary by plan and were trimmed by several carriers for [[YEAR]].</li>
<li><strong>An annual out-of-pocket maximum</strong> on medical costs &mdash; something Original Medicare alone does not have.</li>
</ul>
<h2>The California twist: the medical group</h2>
<p>In most states an Advantage plan&rsquo;s network is a list of doctors. In California, most non-Kaiser plans work through <strong>delegated medical groups</strong> &mdash; Optum, Regal, Monarch, Hoag Physician Partners, Sutter, John Muir, Sharp Rees-Stealy and hundreds of others &mdash; and the group you are assigned to through your primary doctor decides which specialists and hospitals you can use. Two people on the same plan in the same city can have completely different access. That is the single most important thing to check before you enroll: not just whether your doctor takes the plan, but which group your doctor belongs to and what that group reaches. <a href="/kaiser">Kaiser Senior Advantage</a> is the exception; it is one integrated system.</p>
<h2>What changed for [[YEAR]] in California</h2>
<ul>
<li><strong>Anthem Blue Cross ended its Medicare Advantage PPO plans</strong> in California, which mattered most to people who chose a PPO for out-of-network freedom.</li>
<li><strong>Aetna closed plans and withdrew from counties</strong>, mostly PPOs, as part of a national pullback.</li>
<li><strong>UnitedHealthcare and Humana exited counties</strong> nationwide, and in California the rural North State, the high desert and the mountains felt it most.</li>
<li><strong>Extras were trimmed</strong> almost everywhere; the $0 premium survived, the dental allowance often did not.</li>
</ul>
<div class="note-box"><p><strong>If your plan was discontinued:</strong> your non-renewal notice opens a Special Enrollment Period, and because you lost coverage through no fault of your own you generally have a <strong>guaranteed-issue right to a Medigap policy</strong> without health questions, usually within 63 days of the coverage ending. That right is the door back to Original Medicare for people who could not otherwise pass underwriting. Call before the deadline on your notice.</p></div>
<h2>Who Advantage tends to fit in California</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, who are comfortable inside one medical group and one county, and who stay mostly in California. If you split the year with Arizona or Nevada, or see specialists at Stanford, UCLA or City of Hope that your group may not reach, weigh a <a href="/medicare-supplement">Medigap policy</a> carefully &mdash; and remember that California&rsquo;s birthday rule makes Medigap easier to keep affordable here than almost anywhere.</p>
<p>Related: <a href="/kaiser">Kaiser Permanente and Medicare</a>, <a href="/chronic-snp">Chronic Special Needs Plans</a>, <a href="/institutional-snp">Institutional SNPs</a>, and <a href="/medi-cal">Medi-Medi Plans</a> for people with both Medicare and Medi-Cal.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You must keep paying the Part B premium, and you use the plan&rsquo;s network and medical group."),
           ("Which Medicare Advantage carriers sell in California?", "Kaiser Permanente statewide in its service areas, plus SCAN, Alignment, Blue Shield of California, UnitedHealthcare, Humana, Wellcare/Health Net, Central Health, Brand New Day, Molina and regional plans, varying by county. We represent a number of them, not all; HICAP (1-800-434-0222) and Medicare.gov list every plan."),
           ("What does &lsquo;medical group&rsquo; mean on a California Advantage plan?", "Most non-Kaiser plans delegate your care to a physician group tied to your primary doctor. That group, not the insurer, approves referrals and decides which specialists and hospitals you can use. Checking the group is as important as checking the plan."),
           ("My plan was discontinued for [[YEAR]]. What are my options?", "Choose another Advantage plan in your county, or return to Original Medicare with a Medigap policy and a Part D plan. A discontinued plan usually gives you a guaranteed-issue right to Medigap, generally within 63 days of the coverage ending. We compare both paths with you.")],
     sources=[SRC_MA_GOV, SRC_KFF, SRC_KIP, SRC_PPO, SRC_KPIHP, SRC_MEDIGAP_GOV], cta="Not sure whether Advantage fits? Let&rsquo;s compare, no pressure.", about="Medicare Advantage in California"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in California", crumb="Medicare Supplement", scene="coast",
     title="Medicare Supplement Plans in California [[YEAR]] | Medigap &amp; the Birthday Rule | ECOS",
     desc="Medigap in California: the 60-day birthday rule, Plans G and N, the six-month open enrollment, guaranteed-issue rights, coverage for people under 65, and why premiums here reward shopping every year. Free help from a licensed California agent (CA License #0M00978).",
     llm="Medicare Supplement (Medigap) in California: the 60-day birthday rule, the six-month open enrollment at 65, under-65 rights, guaranteed issue, and how premiums are rated",
     eyebrow="Plan type · Medicare Supplement (Medigap)", h1="Medicare Supplement (Medigap) plans in California",
     sub="Original Medicare plus a Medigap policy: any doctor in the country who takes Medicare, no medical group, no referrals &mdash; and a California rule that lets you switch carriers every year without health questions.",
     keyfacts=["California uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company.",
               "<strong>The birthday rule:</strong> each year, for 60 days beginning on your birthday, you may switch to any carrier&rsquo;s Medigap plan with the same or lesser benefits, with no medical underwriting and no new waiting period. Use it to re-shop your premium every year.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. California also requires insurers to offer Medigap to people under 65 on Medicare because of disability, with a six-month window when Part B begins; that requirement does not cover under-65 ESRD. Everyone gets a fresh six-month open enrollment at 65.",
               "Losing an Advantage plan or employer coverage through no fault of your own creates a guaranteed-issue right, generally 63 days long. Most California Medigap premiums are attained-age rated, so they rise as you age; the filed rate history shows which carriers hold steady.",
               "A Medigap policy does not work at Kaiser Permanente. To keep Kaiser doctors on Medicare you need <a href=\"/kaiser\">Kaiser Senior Advantage</a>."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D plan</a> for prescriptions.</p>
<h2>How Medigap is different from Advantage</h2>
<table class="ctable">
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Original Medicare + Medigap</th><th scope="col">Medicare Advantage</th></tr></thead>
<tbody>
<tr><th scope="row">Provider access</th><td>Any provider in the U.S. that accepts Medicare &mdash; no medical group, no referrals, no county lines (Kaiser excepted)</td><td>Plan network and medical group, mostly within your county</td></tr>
<tr><th scope="row">Monthly cost</th><td>Part B premium + Medigap premium + Part D premium</td><td>Part B premium + plan premium (often $0)</td></tr>
<tr><th scope="row">Cost when you use care</th><td>Predictable; Plan G leaves only the Part B deductible ([[YEAR]]: $283)</td><td>Copays per visit, up to the plan&rsquo;s out-of-pocket max</td></tr>
<tr><th scope="row">Extras</th><td>Not included</td><td>Often dental, vision, hearing, OTC (trimmed for [[YEAR]])</td></tr>
<tr><th scope="row">Switching later</th><td>California&rsquo;s birthday rule lets you switch carriers every year without underwriting</td><td>Change plans each fall (AEP) or Jan&ndash;Mar (MA OEP)</td></tr>
</tbody></table>
<h2>California&rsquo;s birthday rule, plainly</h2>
<p>Every year, starting on your birthday and running for 60 days, you have the right to move your Medigap policy to <strong>any insurer</strong>&rsquo;s plan with the <strong>same or lesser benefits</strong> &mdash; no health questions, no waiting period. A Plan G with one carrier can become a Plan G with a cheaper carrier, or a Plan N. Most states make you pass medical underwriting to do that, which traps people in policies whose premiums have climbed for years. In California the trap does not close. We re-shop every client&rsquo;s supplement in the weeks before their birthday, as a matter of routine, using the <a href="https://www.mymedigaprate.com/medigap-rate-history/california" rel="noopener">filed rate history</a> to see which carriers have held their increases down.</p>
<h2>When you can buy without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment</strong> at 65 (or when you enroll in Part B at 65 or later): any plan, any carrier, no underwriting.</li>
<li><strong>Under 65 on Medicare because of disability:</strong> California requires insurers to offer Medigap, with a six-month window when your Part B begins. Premiums for under-65 policies run higher, and the requirement does not extend to people under 65 with ESRD. You get a fresh open enrollment for every plan at 65.</li>
<li><strong>Guaranteed-issue events:</strong> your Advantage plan is discontinued or leaves your county, your employer coverage ends, you move out of your plan&rsquo;s area, or you used the 12-month Advantage trial right. These generally run 63 days and cover a set of plan letters.</li>
<li><strong>The birthday rule</strong>, every year, for switching between plans of equal or lesser benefit.</li>
</ul>
<h2>How California premiums are priced</h2>
<p>Most California Medigap policies are <strong>attained-age rated</strong>: the premium rises with your age plus the carrier&rsquo;s filed increases. A few carriers use issue-age or community rating, which can be cheaper over a long horizon. Rather than guess, we look at the rate filings carrier by carrier, and because the birthday rule lets you change carriers every year, the initial price matters less here than a carrier&rsquo;s habit of raising it.</p>
<div class="note-box"><p><strong>The Kaiser exception.</strong> Kaiser Permanente does not generally treat Original Medicare patients outside emergencies, so a Medigap policy cannot get you Kaiser doctors. If you want Kaiser on Medicare, the route is <a href="/kaiser">Kaiser Senior Advantage</a>. If you want the freedom of Medigap, that means choosing non-Kaiser doctors. It is the first decision for a lot of Californians.</p></div>
<h2>Who Medigap tends to fit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; Stanford, UCLA, Cedars-Sinai, City of Hope without a group question &mdash; who split the year with another state, or who prefer a predictable premium over copays. If you are healthy, in one medical group, and want a $0 premium with extras, <a href="/medicare-advantage">Advantage</a> may fit better.</p>""",
     faqs=[("What is California&rsquo;s Medigap birthday rule?", "Each year, for 60 days beginning on your birthday, you can switch to any insurer&rsquo;s Medigap plan with the same or lesser benefits, with no medical underwriting. It lets Californians re-shop their supplement every year, which most states do not allow."),
           ("Which Medigap plan is best in California?", "For most people new to Medicare, Plan G or Plan N. Plan G covers everything but the Part B deductible; Plan N trades a lower premium for small office and ER copays. The right letter depends on your budget and how often you see a doctor, and the right carrier depends on its rate history."),
           ("Can I buy Medigap in California if I am under 65?", "Yes, if you are on Medicare because of a disability. California requires insurers to offer Medigap with a six-month open enrollment when your Part B begins. The requirement does not extend to people under 65 with ESRD. Everyone gets a fresh open enrollment at 65."),
           ("Can I use a Medigap policy at Kaiser?", "No. Kaiser Permanente does not generally treat Original Medicare patients outside emergencies. Keeping Kaiser doctors on Medicare means Kaiser Senior Advantage, a Medicare Advantage plan."),
           ("Why do Medigap premiums keep rising?", "Most California policies are attained-age rated, so premiums climb with your age plus the carrier&rsquo;s filed increases. The birthday rule is the answer: switch to a carrier with a better track record, every year if you need to.")],
     sources=[SRC_MEDIGAP_GOV, SRC_INS_CODE, SRC_CHA_OE, SRC_CHA_RULES, SRC_MRO, SRC_MMR_CA], cta="Want a quote comparison across carriers? Just ask.", about="Medicare Supplement (Medigap) in California"),

dict(slug="part-d", nav_title="Medicare Part D plans in California", crumb="Part D", scene="valley",
     title="Medicare Part D Plans in California [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Part D in California: the $2,100 cap, formularies and pharmacy networks, the late-enrollment penalty, Extra Help, and what happens to prescriptions during a wildfire emergency. Free help from a licensed California agent.",
     llm="Medicare Part D drug coverage in California: 2026 $2,100 out-of-pocket cap, choosing a plan by your medications and pharmacy, the late-enrollment penalty, Extra Help, wildfire emergency refills",
     eyebrow="Plan type · Part D prescription drug coverage", h1="Medicare Part D plans in California",
     sub="Standalone drug coverage chosen around your actual prescriptions and your pharmacy &mdash; with a [[YEAR]] out-of-pocket cap of $2,100 and a penalty for waiting that never goes away.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life, VA pharmacy and most CalPERS retiree plans are creditable.",
               "During a declared wildfire emergency, Part D plans must lift refill-too-soon limits and cover out-of-network pharmacies in the affected area. Qualifying for a California Medicare Savings Program automatically qualifies you for Extra Help."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>The out-of-pocket cap is $2,100.</strong> After you reach it, covered drugs cost you nothing for the rest of the year. The cap continues the redesign that ended the old &ldquo;donut hole.&rdquo;</li>
<li><strong>The maximum deductible is $615.</strong> Plans may set it lower.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread pharmacy costs across the year in monthly installments instead of paying at the counter. It does not lower your cost; it smooths it.</li>
<li><strong>Fewer standalone plans and higher premiums</strong> in many states, as several national carriers pulled back for [[YEAR]].</li>
</ul>
<h2>How to choose a Part D plan</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. The same drug can be $5 on one plan and $95 on another. So we start with your medication list and your pharmacy, not the premium, and check whether Costco, CVS, Walgreens, Rite Aid&rsquo;s successors or your independent pharmacy is preferred.</p>
<h2>The late-enrollment penalty</h2>
<p>If you go 63 or more days in a row without creditable drug coverage after your Initial Enrollment Period ends, Medicare adds 1% of the national base premium ($38.99 in [[YEAR]]) for every month you went without, to your premium, <strong>for as long as you have Part D</strong>. If you do not take medications now, a low-premium plan is cheap insurance against that penalty.</p>
<h2>Wildfires and your prescriptions</h2>
<p>When a wildfire produces a federal or state emergency declaration, Part D plans in the affected area must let you refill early, replace lost medications, and use out-of-network pharmacies at the plan&rsquo;s usual allowance. If you evacuate, call the number on your card before you assume a refill will be denied. Our <a href="/wildfires">wildfires page</a> covers the enrollment side too.</p>
<h2>Help paying for Part D</h2>
<p>Extra Help (the Low-Income Subsidy) lowers premiums, deductibles and copays for people with limited income and resources. If you qualify for one of California&rsquo;s Medicare Savings Programs through Medi-Cal, you get Extra Help automatically. Note that the Medi-Cal asset limit returned on January 1, 2026; our <a href="/medi-cal">Medicare + Medi-Cal page</a> explains what it means for the Savings Programs.</p>""",
     faqs=[("Do I need Part D if I don&rsquo;t take any medications?", "Usually, yes &mdash; or other creditable coverage such as TRICARE For Life, VA pharmacy or a creditable CalPERS retiree plan. Without it, a permanent penalty accrues for every month you wait, and needs change. A low-premium plan is inexpensive protection."),
           ("Can I change my Part D plan every year?", "Yes. During the Annual Election Period (Oct 15&ndash;Dec 7) you can switch for the following January. Because formularies and preferred pharmacies change, an annual check is worth doing."),
           ("What happens to my prescriptions if I have to evacuate from a wildfire?", "In a declared emergency area your plan must allow early refills, replace lost medications and cover out-of-network pharmacies at its usual allowance. Call your plan; do not assume a refill will be refused."),
           ("Does Medicare Advantage include Part D?", "Most Advantage plans include it. A few MA-only plans do not, for people with TRICARE For Life or VA pharmacy; if you have neither, choose an Advantage plan with drug coverage or a standalone plan.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_CMS_FIRE, SRC_CHA_MEDICAL], cta="Bring your medication list and we&rsquo;ll price every plan against it.", about="Medicare Part D in California"),

dict(slug="kaiser", nav_title="Kaiser Permanente and Medicare in California: Senior Advantage vs. everything else", crumb="Kaiser &amp; Medicare", scene="goldengate",
     title="Kaiser Permanente &amp; Medicare in California [[YEAR]]: Senior Advantage vs. Medigap | ECOS Medicare Solutions",
     desc="Kaiser Permanente on Medicare in California: how Senior Advantage works, why a Medigap policy cannot be used at Kaiser, what leaving or joining Kaiser at 65 means, and how to decide. Plain-English help from a licensed independent agent (CA License #0M00978).",
     llm="Kaiser Permanente and Medicare in California: Kaiser Senior Advantage, why Medigap does not work at Kaiser, joining or leaving Kaiser at 65, how to decide",
     eyebrow="Your situation · Kaiser Permanente", h1="Kaiser Permanente and Medicare: the first decision most Californians make",
     sub="More than 1.4 million Californians take Medicare through Kaiser. It is a closed, integrated system with one way in on Medicare &mdash; Senior Advantage &mdash; and no Medigap route. Here is how to think about it without a sales pitch either way.",
     keyfacts=["Kaiser Permanente Senior Advantage is a Medicare Advantage HMO. Your care, hospitals, pharmacy and Part D are all inside Kaiser; there is no medical group to check because Kaiser is the medical group.",
               "A Medigap policy cannot be used at Kaiser. Kaiser does not generally treat Original Medicare patients outside emergencies, so &ldquo;Original Medicare plus a supplement, and keep my Kaiser doctor&rdquo; is not an option.",
               "If you are in Kaiser before 65 through an employer, Covered California or Medi-Cal, you can usually move into Senior Advantage at 65 with your records and doctors intact. If you are not in Kaiser, joining at 65 means starting fresh inside the system.",
               "Leaving Kaiser at 65 is the one moment it costs nothing to do so: your six-month Medigap open enrollment lets you buy any supplement with no health questions. Later, the birthday rule and guaranteed-issue rights still apply, but Senior Advantage&rsquo;s 12-month trial right is worth knowing."],
     body="""<p>Kaiser Permanente is the thing about California Medicare that the national websites cannot explain, because no other state has anything like it at this scale. Kaiser is an insurer, a hospital system and a medical group at once. On Medicare, that shows up as <strong>Kaiser Permanente Senior Advantage</strong>, a Medicare Advantage HMO that, in several Bay Area and Southern California counties, is the largest Medicare plan by a wide margin.</p>
<h2>How Senior Advantage works</h2>
<ul>
<li><strong>Everything inside Kaiser.</strong> Primary care, specialists, hospitals, labs, pharmacy and Part D are all Kaiser. Referrals happen inside the system, usually quickly, and your records follow you.</li>
<li><strong>Emergencies anywhere, routine care at Kaiser.</strong> Like other Advantage plans, it covers emergencies and urgent care outside the network, and routine care only inside it. Some Senior Advantage plans carry a travel benefit; we check yours.</li>
<li><strong>Premium and extras vary by county</strong> and by year. Several counties have a $0-premium option; others do not. Dental, hearing and fitness extras are plan-specific.</li>
<li><strong>Kaiser did not exit any counties for [[YEAR]]</strong>, unlike several national carriers, and its plans carry strong Star ratings.</li>
</ul>
<h2>Why a Medigap policy does not get you Kaiser</h2>
<p>A Medigap policy pays after Original Medicare pays, and it works with any provider that bills Original Medicare. Kaiser, outside emergencies, does not bill Original Medicare for routine care from non-members. So the combination many people ask for &mdash; Original Medicare, a Plan G, and my Kaiser doctor &mdash; does not exist. If keeping your Kaiser doctors matters most, Senior Advantage is the answer. If freedom to see Stanford, UCLA, Cedars-Sinai or City of Hope matters most, that means leaving Kaiser and pairing Original Medicare with a <a href="/medicare-supplement">Medigap policy</a>, or choosing a non-Kaiser Advantage plan built on those systems.</p>
<h2>Three situations, three answers</h2>
<ul>
<li><strong>Already in Kaiser and happy.</strong> Senior Advantage is usually the natural continuation. We still compare its county options against each other and check the Part D formulary against your medications.</li>
<li><strong>In Kaiser and thinking of leaving.</strong> Turning 65 is the cleanest moment: your Medigap open enrollment lets you buy any supplement without underwriting. Waiting is possible &mdash; the birthday rule and guaranteed-issue rights still exist &mdash; but a new Medigap purchase after your open enrollment usually means health questions.</li>
<li><strong>Not in Kaiser and considering it.</strong> You can join Senior Advantage during any valid enrollment period. You will get new doctors inside the system. If you try it and want out within 12 months of leaving a Medigap policy for the first time, the federal trial right lets you return to Medigap without underwriting.</li>
</ul>
<div class="note-box"><p><strong>We are independent, and we are not Kaiser.</strong> We can enroll you in Senior Advantage where we are appointed, or in the alternatives, or tell you plainly that your current coverage is the right one. The point of this page is that the Kaiser decision comes first and deserves an honest comparison, not a brochure.</p></div>
<p>Related: <a href="/medicare-advantage">Medicare Advantage in California</a>, <a href="/medicare-supplement">Medigap and the birthday rule</a>, and <a href="/turning-65">Turning 65 in California</a>.</p>""",
     faqs=[("Can I keep my Kaiser doctor when I go on Medicare?", "Yes, by enrolling in Kaiser Permanente Senior Advantage, Kaiser&rsquo;s Medicare Advantage plan. You cannot keep Kaiser doctors with Original Medicare and a Medigap policy, because Kaiser does not generally treat Original Medicare patients outside emergencies."),
           ("Is Kaiser Senior Advantage a Medicare Advantage plan?", "Yes. It is a Medicare Advantage HMO with Part D included in most versions, offered county by county across Kaiser&rsquo;s California service areas."),
           ("What if I leave Kaiser at 65 and regret it?", "If you left for Original Medicare and a Medigap policy, you can join Senior Advantage during the next Annual Election Period or another valid window. If you left Medigap for Senior Advantage and it is your first time in an Advantage plan, the federal trial right lets you return to Medigap without underwriting within 12 months."),
           ("Does Kaiser cover me when I travel?", "Emergency and urgent care are covered anywhere in the U.S. Routine care is inside Kaiser; some Senior Advantage plans include a travel benefit for visits to Kaiser regions in other states. We check the plan documents for your county."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing Kaiser against the alternatives is free to you, and your premium is the same either way.")],
     sources=[SRC_KPIHP, SRC_KFF, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_CHA_RULES], cta="Kaiser or not? Let&rsquo;s talk it through honestly.", about="Kaiser Permanente Senior Advantage and Medicare in California", priority="0.8"),
]
