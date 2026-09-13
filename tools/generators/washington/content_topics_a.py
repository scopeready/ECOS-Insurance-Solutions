"""Washington topic pages, part A: Advantage, Medigap, Part D, costs. "Washington" means the state throughout."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_OIC = ("Washington State Office of the Insurance Commissioner (regulates Medigap; agent and company lookup)", "https://www.insurance.wa.gov")
SRC_SHIBA = ("Office of the Insurance Commissioner: get free Medicare help from SHIBA (800-562-6900)", "https://www.insurance.wa.gov/insurance-resources/medicare/get-free-medicare-help-shiba")
SRC_SHIBA_LOCAL = ("Office of the Insurance Commissioner: find a local SHIBA office", "https://www.insurance.wa.gov/insurance-resources/medicare/get-free-medicare-help-shiba/find-local-shiba-office")
SRC_HIO_WA = ("healthinsurance.org: Medicare in Washington (Medigap switching rule, Plan A limit)", "https://www.healthinsurance.org/medicare/washington/")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_HCD = ("Healthcare Dive: UnitedHealthcare, Humana, Aetna scale back Medicare Advantage plans for 2026", "https://www.healthcaredive.com/news/medicare-advantage-plans-2026-unitedhealthcare-humana-aetna/801761/")
SRC_UW_2026 = ("UW Medicine: health insurance plan changes for 2026", "https://www.uwmedicine.org/patient-resources/billing-and-insurance/open-enrollment/health-insurance-plan-changes-2026")
SRC_MMR_WA = ("MyMedigapRate: Washington Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/washington")
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, state by state", "https://www.mymedigaprate.com/switching-medigap-plans")
SRC_HCA_APPLY = ("Washington State Health Care Authority: apply for Apple Health coverage", "https://www.hca.wa.gov/free-or-low-cost-health-care/apply-coverage")
SRC_HCA_STD = ("Washington State Health Care Authority: Apple Health income and resource standards (HCA 19-0096)", "https://www.hca.wa.gov/assets/free-or-low-cost/income-standards.pdf")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in Washington State", crumb="Medicare Advantage", scene="skyline",
     title="Medicare Advantage Plans in Washington State [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in Washington State: networks built around UW Medicine, Providence Swedish, MultiCare, Virginia Mason Franciscan and Kaiser Permanente Washington, the 2026 contract changes, and the east-west gap. Free help from a licensed Washington agent.",
     llm="Medicare Advantage (Part C) in Washington State: how networks and bundled benefits work, which big systems contract with which plans, UW Medicine's 2026 changes, and the thin menus east of the Cascades",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in Washington State",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a county-by-county network, in a state where the network question is really a question about which hospital system you use.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "Washington&rsquo;s care is organized into large systems &mdash; UW Medicine, Providence Swedish, MultiCare, Virginia Mason Franciscan Health, Kaiser Permanente Washington, PeaceHealth, Confluence, Kadlec &mdash; and each contracts with some plans and not others. For 2026 UW Medicine has said it will not be contracted with Humana, PacificSource or Wellpoint plans.",
               "Nationally, for the 2026 plan year UnitedHealthcare left 109 counties, Humana 194 and Aetna 100; Kaiser neither entered nor left any. Whether your Washington county was touched is a ZIP-code question we check before anything else.",
               "A plan leaving your county gives you a Special Enrollment Period and, in most cases, a federal guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. Which companies sell in <em>your</em> county, and which hospitals sit inside each plan&rsquo;s network, changes every year &mdash; and in Washington State that second question usually settles the choice.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks, system by system</h2>
<p>Advantage plans use provider networks (HMO or PPO) and are sold by county. That is the single most important thing to check before you enroll: whether your doctors and your hospital are in the plan&rsquo;s network, and whether your medications are on its drug list. Washington&rsquo;s big systems each contract on their own terms &mdash; UW Medicine (Harborview, UW Medical Center, Valley Medical Center), Providence Swedish, MultiCare (Tacoma, Puyallup, Auburn, Spokane, Yakima), Virginia Mason Franciscan Health, EvergreenHealth, Overlake, PeaceHealth (Bellingham, Vancouver, Longview), Confluence Health in Wenatchee, Kadlec in the Tri-Cities and Providence Sacred Heart in Spokane. Kaiser Permanente Washington is different again: it is both an insurer and a care system, and its Advantage plans are built around its own medical centers. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="warn-box"><p><strong>What changed for 2026, and why it matters this fall.</strong> UW Medicine has said it will not be contracted with Humana, PacificSource or Wellpoint (formerly Amerigroup) plans for 2026. Nationally, UnitedHealthcare offered plans in 109 fewer counties, Humana in 194 fewer and Aetna in 100 fewer, while Kaiser neither entered nor left any county. If you were moved into a new plan, or your Seattle-area plan quietly lost a system, the Annual Election Period starting October 15 is the time to check it actually fits.</p></div>
<h2>Two Washingtons</h2>
<p>West of the Cascades &mdash; King, Pierce, Snohomish, Thurston, Clark, Whatcom, Kitsap &mdash; the Advantage menu is deep and the networks usually include most of the big systems, so the comparison is about extras, drug costs and which system your doctors belong to. East of the passes and along the coast the menu is short, several counties lean on a single public hospital district, and a specialist may mean a drive to Spokane, Yakima, the Tri-Cities or over the mountains to Seattle. Out there, a $0-premium plan with a network that stops at the county line can be a poor bargain, and Original Medicare with a <a href="/medicare-supplement">Medigap policy</a> is often the practical answer.</p>
<h2>If your plan left your county</h2>
<p>A non-renewal notice is not just bad news; it opens doors. You get a Special Enrollment Period that runs past the normal deadlines, and because the plan left you involuntarily, federal rules give most people a <strong>guaranteed-issue right</strong> to buy a <a href="/medicare-supplement">Medigap policy</a> without medical underwriting, generally for 63 days after your coverage ends. Once you hold that Medigap policy, Washington&rsquo;s <a href="/medigap-switching">year-round switching rule</a> lets you move between Medigap plans later without health questions; it does not, however, get you <em>into</em> Medigap from an Advantage plan, so use the federal window when it comes.</p>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, who are comfortable using a plan network, and who live where the menu is deep. If you spend winters in Arizona or summers on the Peninsula, see specialists outside the network, or want to use any provider nationwide, compare it against a <a href="/medicare-supplement">Medigap policy</a>. Military retirees with TRICARE For Life have their own calculation; see <a href="/veterans">Veterans</a>.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans for people with both Medicare and <a href="/medicaid">Apple Health</a>.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("Is UW Medicine in my Advantage plan for 2026?", "UW Medicine has said it will not be contracted with Humana, PacificSource or Wellpoint plans for 2026, and its contracted list changes each fall. UW Medicine accepts Original Medicare and therefore any Medigap policy. If UW Medicine, Fred Hutch, Providence Swedish or Virginia Mason is your care, we confirm the plan&rsquo;s status in writing before you enroll."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Special circumstances, including moving counties or your plan leaving, open other windows.")],
     sources=[SRC_MA_GOV, SRC_UW_2026, SRC_KFF, SRC_HCD, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in Washington State"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in Washington State", crumb="Medicare Supplement", scene="rainier",
     title="Medicare Supplement Plans in Washington State: Plan G, Plan N &amp; the Switching Rule | ECOS Medicare Solutions",
     desc="Washington Medigap explained: the standardized plans, the six-month open enrollment, the state law that lets policyholders switch plans any time without underwriting (Plan A excepted), guaranteed-issue events, and how to compare carriers on filed rate history.",
     llm="Medicare Supplement (Medigap) in Washington State: standardized plans A-N, the six-month open enrollment, the year-round switching rule for existing policyholders (Plan A limited to Plan A), guaranteed-issue events, comparing carriers on filed rate history",
     eyebrow="Plans · Medigap", h1="Medicare Supplement (Medigap) plans in Washington State",
     sub="A Medigap policy works alongside Original Medicare to pay much of what it leaves to you, lets you use any provider in the country that accepts Medicare &mdash; UW, Fred Hutch, a hospital district in Okanogan County &mdash; and, in Washington, can be changed at any time once you have one.",
     keyfacts=["Washington uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company, so the comparison is price and rate history. The Office of the Insurance Commissioner regulates the policies.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. During it, no insurer can turn you down or charge more for your health.",
               "Washington law then lets anyone who already has a Medigap policy switch to another Medigap plan at any time of year without medical underwriting. The one limit: a Plan A holder can move only to another Plan A. Plans B through N can move to any of B through N.",
               "The switching rule is for existing Medigap policyholders. Coming from Medicare Advantage, you rely on your open enrollment, a federal guaranteed-issue event (such as your plan leaving the county, or the 12-month trial right), or underwriting."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. The Washington State Office of the Insurance Commissioner regulates the policies; the benefits inside each plan letter are set federally.</p>
<h2>How Medigap is different from Advantage</h2>
<table class="ctable">
<caption>A simplified comparison &mdash; the right choice depends on your health, doctors, county and budget.</caption>
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Medicare Supplement (Medigap)</th><th scope="col">Medicare Advantage</th></tr></thead>
<tbody>
<tr><th scope="row">Provider access</th><td>Any provider in the U.S. that accepts Medicare &mdash; no networks, no county lines</td><td>Plan network (HMO/PPO), sold by county</td></tr>
<tr><th scope="row">Drug coverage</th><td>Add a separate Part D plan</td><td>Usually built in</td></tr>
<tr><th scope="row">Monthly premium</th><td>A monthly premium for the policy</td><td>Often $0 plan premium</td></tr>
<tr><th scope="row">Out-of-pocket</th><td>Very predictable; little to pay at the point of care on Plan G</td><td>Copays/coinsurance up to an annual cap</td></tr>
<tr><th scope="row">Extras (dental/vision)</th><td>Not included</td><td>Often included</td></tr>
<tr><th scope="row">Changing plans later</th><td>In Washington, any time, without health questions (Plan A excepted)</td><td>Annual and open-enrollment windows, or a Special Enrollment Period</td></tr>
</tbody></table>
<h2>The plans Washingtonians actually buy</h2>
<p><strong>Plan G</strong> covers everything Original Medicare leaves behind except the Part B deductible ($283 in [[YEAR]]). <strong>Plan N</strong> costs less in exchange for small office and emergency copays and no coverage of Part B excess charges. <strong>High-deductible Plan G</strong> has a much lower premium and a deductible you pay first. <strong>Plan F</strong> still exists for people who were eligible before 2020 but cannot be sold to anyone newer. Because benefits are standardized, we compare companies on price and on how fast they have raised it.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, every plan a company sells is guaranteed available regardless of health.</li>
<li><strong>Already have a Medigap policy? Any time.</strong> Washington law lets an existing Medigap policyholder move to another Medigap plan, from the same company or a different one, at any point in the year without medical underwriting. The single exception is Plan A: if you hold Plan A, you can move only to another Plan A. Our <a href="/medigap-switching">switching guide</a> explains what that does and does not let you do.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage plan or employer coverage through no fault of your own, or using the 12-month trial right after a first Advantage plan, gives you a federal window (generally 63 days) to buy certain plans without underwriting.</li>
<li><strong>Under 65 on Medicare because of a disability?</strong> Federal law does not guarantee you a Medigap open enrollment before 65, and what a Washington carrier will offer you, and at what price, depends on the carrier and current state rules. Ask us or SHIBA before you assume; you get a full open enrollment at 65 either way.</li>
<li><strong>Coming from Medicare Advantage without one of those events,</strong> Washington insurers can use medical underwriting. The year-round rule helps only once you are inside Medigap.</li>
</ul>
<div class="note-box"><p><strong>Timing still matters.</strong> The switching rule makes Washington one of the easiest states in the country to be a Medigap policyholder in &mdash; but only if you get in during a window when no one can ask health questions. If you are approaching 65, or your Advantage plan just sent a non-renewal notice, talk to us before the window closes.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between Washington Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate changes with the Office of the Insurance Commissioner, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/washington">Washington Medigap rate history</a>, with each figure tied to the filing it came from. Because Washington lets you move without underwriting, a steep increase is a reason to shop, not a trap &mdash; <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes.</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; UW Medicine or Fred Hutch without a network question, a Seattle specialist from a Ferry County address &mdash; predictable costs, and coverage that travels to a second home in Arizona or a grandchild in Idaho. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings, softened in Washington by the freedom to move.</p>""",
     faqs=[("Do I need a separate drug plan with Medigap?", "Yes. Medigap does not include prescription coverage, so most people add a standalone Part D plan. We help you pick one around your specific medications."),
           ("Can I be turned down for Medigap in Washington?", "Not during your six-month open enrollment, not during a federal guaranteed-issue event, and not when you switch from one Medigap plan to another under Washington&rsquo;s year-round rule (Plan A holders can move only to another Plan A). Coming from Medicare Advantage outside a guaranteed-issue event, insurers can use medical underwriting."),
           ("Is Plan F still available in Washington?", "Only to people who became eligible for Medicare before January 1, 2020. Everyone newer chooses from Plans G, N, high-deductible G and the others. Existing Plan F holders in Washington can move to Plan G or N any time without health questions if the premium becomes hard to justify."),
           ("Does Washington&rsquo;s switching rule let me leave Medicare Advantage for Medigap?", "No. It is for people who already hold a Medigap policy. Leaving Advantage for Medigap uses your six-month open enrollment, a federal guaranteed-issue right such as the 12-month trial right or your plan leaving your county, or medical underwriting."),
           ("How much does a Washington Medigap policy cost?", "It depends on the plan letter, your age, ZIP code, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MEDIGAP_GOV, SRC_HIO_WA, SRC_OIC, SRC_MMR_WA, SRC_MMR_SWITCH, SRC_SHIBA, SRC_CMS], cta="Let&rsquo;s see whether Plan G, Plan N or something else fits you.", about="Medicare supplement insurance in Washington State"),

dict(slug="part-d", nav_title="Medicare Part D plans in Washington State", crumb="Part D", scene="orchards",
     title="Medicare Part D Plans in Washington State [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in Washington State: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications and pharmacy (Fred Meyer, Safeway, Costco, Walgreens, independents), the late penalty, and Extra Help through the Medicare Savings Programs.",
     llm="Part D drug plans in Washington State: 2026 $2,100 cap, choosing by your medications and pharmacy, penalties, Extra Help through Washington's Medicare Savings Programs",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in Washington State",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Medigap policy, or nothing else.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life and VA pharmacy are creditable.",
               "Qualifying for a Washington Medicare Savings Program or Apple Health automatically qualifies you for Extra Help, which cuts Part D premiums and copays substantially. For 2026 the Medicare Savings Programs have income limits only, with no asset test."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list and your pharmacy</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at a Fred Meyer in Puyallup may be expensive at the one pharmacy in Republic or Pomeroy. Washington&rsquo;s pharmacy map shifted in 2025 as chains closed stores, so check that the pharmacy you actually use is still preferred, not the one that was. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources. In Washington, qualifying for a Medicare Savings Program (QMB, SLMB or QI-1) or for Apple Health qualifies you for Extra Help automatically, and for 2026 the Medicare Savings Programs look only at income. See <a href="/medicaid">Apple Health and the Medicare Savings Programs</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Does my pharmacy matter?", "Yes. Each plan has preferred pharmacies where copays are lowest. Fred Meyer, Safeway, Costco, Walgreens, Walmart and independents are preferred in different plans, and a rural county may have only one pharmacy; we check yours when we compare."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_COSTS, SRC_HCA_STD, SRC_HCA_APPLY], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in Washington State"),

dict(slug="medicare-costs", nav_title="[[YEAR]] Medicare costs, full IRMAA chart, and penalty/IRMAA calculators", crumb="[[YEAR]] Costs", scene="cascades",
     title="[[YEAR]] Medicare Costs &amp; IRMAA in Washington State | ECOS Medicare Solutions",
     desc="[[YEAR]] Medicare costs for Washington State: Part A/B/D premiums and deductibles, the full IRMAA income chart, and free calculators for IRMAA and late-enrollment penalties.",
     llm="2026 Medicare costs: Part A/B/D premiums and deductibles, the full IRMAA chart, and calculators for IRMAA and the Part B / Part D late penalties",
     eyebrow="Costs · Verified [[YEAR]] figures", h1="[[YEAR]] Medicare costs and IRMAA, with calculators",
     sub="Every dollar figure on this page comes from the CMS release for [[YEAR]]. The calculators are estimates for planning; Social Security and Medicare set your official amounts.",
     keyfacts=["[[YEAR]] Part B standard premium $202.90/month; Part B deductible $283; Part A hospital deductible $1,736 per benefit period.",
               "[[YEAR]] Part D: out-of-pocket cap $2,100; maximum deductible $615; national base premium $38.99.",
               "IRMAA surcharges begin above $109,000 (single) or $218,000 (joint) of 2024 modified adjusted gross income, and are a cliff: $1 over a threshold moves you to the whole next tier. A house sale in King County, a year of stock-option or RSU income, or a Roth conversion two years ago is the usual surprise.",
               "Part B late penalty: 10% for each full 12 months without Part B or creditable coverage, for life. Part D late penalty: about 1% of the base premium per month without creditable drug coverage."],
     body="""<p>Medicare&rsquo;s costs change every year, so here are the current <strong>[[YEAR]]</strong> figures, the full income-related surcharge (IRMAA) chart, and a few simple calculators. These are estimates to help you plan &mdash; your official amounts come from Social Security and Medicare. We refresh this page every year when CMS publishes the new numbers, usually in November.</p>
<h2>[[YEAR]] Original Medicare costs</h2>
<table class="ctable">
<caption>Source: CMS [[YEAR]] Medicare Parts A &amp; B Premiums and Deductibles (released Nov 14, 2025) and [[YEAR]] Part D parameters.</caption>
<thead><tr><th scope="col">Item</th><th scope="col">[[YEAR]] amount</th></tr></thead>
<tbody>
<tr><th scope="row">Part B standard premium</th><td>$202.90 / month</td></tr>
<tr><th scope="row">Part B annual deductible</th><td>$283</td></tr>
<tr><th scope="row">Part A hospital deductible</th><td>$1,736 per benefit period</td></tr>
<tr><th scope="row">Part A coinsurance, days 61&ndash;90</th><td>$434 / day</td></tr>
<tr><th scope="row">Part A coinsurance, lifetime reserve days</th><td>$868 / day</td></tr>
<tr><th scope="row">Skilled nursing coinsurance, days 21&ndash;100</th><td>$217 / day</td></tr>
<tr><th scope="row">Part D maximum deductible</th><td>$615</td></tr>
<tr><th scope="row">Part D out-of-pocket cap</th><td>$2,100 / year</td></tr>
<tr><th scope="row">Part D national base beneficiary premium</th><td>$38.99 (used for penalties)</td></tr>
</tbody></table>
<p>Most people pay $0 for Part A because they paid Medicare taxes while working. Part D, Medicare Advantage and Medigap premiums vary by plan and carrier; Medigap Plan G covers everything above except the Part B deductible.</p>
<h2>[[YEAR]] IRMAA: what higher earners pay</h2>
<p>If your income is above the thresholds below, you pay an income-related surcharge on top of your Part B and Part D premiums. Your [[YEAR]] IRMAA is based on the income (MAGI) from your <strong>2024</strong> tax return. IRMAA is a cliff: going $1 over a threshold moves you into the whole next tier. Washington has no state income tax, which makes it easy to lose track of federal MAGI; the usual surprises here are the sale of a Seattle-area house, a year of vested stock or a big bonus before retirement, or a Roth conversion two years back.</p>
<table class="ctable">
<caption>[[YEAR]] IRMAA tiers. Part D amounts are added to your plan&rsquo;s premium. Source: CMS / SSA, [[YEAR]].</caption>
<thead><tr><th scope="col">Single filer (2024 MAGI)</th><th scope="col">Married filing jointly</th><th scope="col">Part B total / month</th><th scope="col">Part D surcharge / month</th></tr></thead>
<tbody>
<tr><td>$109,000 or less</td><td>$218,000 or less</td><td>$202.90</td><td>$0.00</td></tr>
<tr><td>$109,001&ndash;$137,000</td><td>$218,001&ndash;$274,000</td><td>$284.10</td><td>+$14.50</td></tr>
<tr><td>$137,001&ndash;$171,000</td><td>$274,001&ndash;$342,000</td><td>$405.80</td><td>+$37.50</td></tr>
<tr><td>$171,001&ndash;$205,000</td><td>$342,001&ndash;$410,000</td><td>$527.50</td><td>+$60.40</td></tr>
<tr><td>$205,001&ndash;$499,999</td><td>$410,001&ndash;$749,999</td><td>$649.20</td><td>+$83.30</td></tr>
<tr><td>$500,000 or more</td><td>$750,000 or more</td><td>$689.90</td><td>+$91.00</td></tr>
</tbody></table>
<p style="font-size:.92rem;color:var(--ink-soft)">Married filing separately uses a compressed two-tier structure with a single threshold at $109,000 &mdash; if that is you, call us and we will walk through it. If your income has dropped since 2024 because you retired, sold a business or lost a spouse, you can ask Social Security to use this year&rsquo;s income instead (Form SSA-44).</p>
<h2>Estimate your numbers</h2>
<p>These calculators are <strong>estimates</strong> using published [[YEAR]] figures. They store nothing. For your official amount, see Medicare.gov or contact Social Security.</p>
<div class="calc">
  <h3>1. IRMAA estimator</h3>
  <div class="field"><label for="fs">Filing status</label>
    <select id="fs"><option value="single">Single / head of household</option><option value="joint">Married filing jointly</option></select></div>
  <div class="field"><label for="magi">Your 2024 income (MAGI)</label>
    <input id="magi" type="number" inputmode="numeric" min="0" step="1000" placeholder="e.g. 95000"></div>
  <button class="btn btn--primary" type="button" onclick="calcIrmaa()">Estimate my premiums</button>
  <div class="calc__result" id="irmaaOut" role="status" aria-live="polite"></div>
</div>
<div class="calc">
  <h3>2. Part B late-enrollment penalty</h3>
  <p style="margin:0 0 .6rem;font-size:.98rem;color:var(--ink-soft)">10% is added for each full 12 months you could have had Part B but didn&rsquo;t (and lacked other qualifying coverage). The penalty generally lasts as long as you have Part B.</p>
  <div class="field"><label for="bmonths">Full months without Part B after you were eligible</label>
    <input id="bmonths" type="number" inputmode="numeric" min="0" step="1" placeholder="e.g. 24"></div>
  <button class="btn btn--primary" type="button" onclick="calcPartB()">Estimate Part B penalty</button>
  <div class="calc__result" id="bOut" role="status" aria-live="polite"></div>
</div>
<div class="calc">
  <h3>3. Part D late-enrollment penalty</h3>
  <p style="margin:0 0 .6rem;font-size:.98rem;color:var(--ink-soft)">Roughly 1% of the national base premium ($38.99 in [[YEAR]]) for each full month you went without creditable drug coverage. It is added to your Part D premium and recalculated each year.</p>
  <div class="field"><label for="dmonths">Full months without creditable drug coverage</label>
    <input id="dmonths" type="number" inputmode="numeric" min="0" step="1" placeholder="e.g. 15"></div>
  <button class="btn btn--primary" type="button" onclick="calcPartD()">Estimate Part D penalty</button>
  <div class="calc__result" id="dOut" role="status" aria-live="polite"></div>
</div>
<div class="note-box"><p>Estimates only, for planning. Your official premiums and any penalty are set by Social Security and Medicare. Want help reading your own numbers or appealing an IRMAA determination (Form SSA-44)? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p></div>
<script>
(function(){
  var fmt=function(n){return '$'+n.toLocaleString('en-US',{minimumFractionDigits:2,maximumFractionDigits:2});};
  var single=[109000,137000,171000,205000,499999], joint=[218000,274000,342000,410000,749999];
  var partB=[202.90,284.10,405.80,527.50,649.20,689.90], partD=[0,14.50,37.50,60.40,83.30,91.00];
  window.calcIrmaa=function(){
    var st=document.getElementById('fs').value, magi=parseFloat(document.getElementById('magi').value), out=document.getElementById('irmaaOut');
    if(isNaN(magi)||magi<0){out.innerHTML='<p>Please enter your 2024 income to see an estimate.</p>';return;}
    var t=st==='joint'?joint:single, idx=0; for(var i=0;i<t.length;i++){if(magi>t[i])idx++;}
    var b=partB[idx], d=partD[idx];
    var msg = idx===0 ? 'Based on that income, you would pay the <strong>standard</strong> Part B premium of '+fmt(b)+' per month and <strong>no</strong> Part D surcharge.'
      : 'Estimated [[YEAR]] Part B premium: <strong>'+fmt(b)+'/month</strong>. Estimated Part D surcharge: <strong>+'+fmt(d)+'/month</strong> on top of your plan premium.';
    out.innerHTML='<p>'+msg+'</p><p class="calc__fine">Estimate based on 2024 MAGI and [[YEAR]] CMS/SSA figures. Official tier is set by Social Security.</p>';
  };
  window.calcPartB=function(){
    var m=parseInt(document.getElementById('bmonths').value,10), out=document.getElementById('bOut');
    if(isNaN(m)||m<0){out.innerHTML='<p>Enter the number of months to see an estimate.</p>';return;}
    var periods=Math.floor(m/12), pct=periods*10, pen=202.90*0.10*periods, tot=202.90+pen;
    if(periods===0){out.innerHTML='<p>Fewer than 12 full months generally means <strong>no</strong> Part B penalty. Keep proof of any other creditable coverage.</p>';return;}
    out.innerHTML='<p>Estimated penalty: <strong>+'+pct+'%</strong> &rarr; about <strong>'+fmt(pen)+'/month</strong> added to Part B, for an estimated total of <strong>'+fmt(tot)+'/month</strong>.</p><p class="calc__fine">Based on the [[YEAR]] standard premium; the penalty generally continues for as long as you have Part B.</p>';
  };
  window.calcPartD=function(){
    var m=parseInt(document.getElementById('dmonths').value,10), out=document.getElementById('dOut');
    if(isNaN(m)||m<0){out.innerHTML='<p>Enter the number of months to see an estimate.</p>';return;}
    var pen=Math.round((0.01*38.99*m)/0.10)*0.10;
    out.innerHTML='<p>Estimated Part D penalty: about <strong>'+fmt(pen)+'/month</strong>, added to your Part D plan premium.</p><p class="calc__fine">Based on the [[YEAR]] national base premium of $38.99; recalculated each year as that figure changes.</p>';
  };
})();
</script>""",
     faqs=[("What is the standard Medicare Part B premium for [[YEAR]]?", "The standard Part B premium is $202.90 per month in [[YEAR]], with a $283 annual deductible. Higher-income beneficiaries pay more through IRMAA."),
           ("What is IRMAA?", "IRMAA (Income-Related Monthly Adjustment Amount) is a surcharge added to your Part B and Part D premiums if your income is above certain thresholds. For [[YEAR]] it is based on your 2024 tax return and starts above $109,000 (single) or $218,000 (joint)."),
           ("What is the Part D out-of-pocket cap in [[YEAR]]?", "$2,100. Once your spending on covered drugs reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Can I get help paying the Part B premium in Washington?", "Possibly. Washington&rsquo;s Medicare Savings Programs (QMB, SLMB and QI-1) pay the Part B premium for people with limited income, and QMB also covers Medicare&rsquo;s deductibles and copays. For 2026 they have income limits only, with no asset test. Apply through the Health Care Authority and DSHS; see our Apple Health page.")],
     sources=[SRC_CMS, SRC_COSTS, SRC_HCA_STD], cta="Not sure which costs apply to you? Let&rsquo;s look together.", about="Medicare costs and IRMAA"),
]
