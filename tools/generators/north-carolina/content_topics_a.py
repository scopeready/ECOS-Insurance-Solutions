"""North Carolina topic pages, part A: Advantage, Medigap, Part D, costs."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_SEP_GOV = ("Medicare.gov: Special Enrollment Periods", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan/special-enrollment-periods")
SRC_SHIIP = ("NC Department of Insurance: Medicare and the Seniors&rsquo; Health Insurance Information Program (SHIIP), 855-408-1212", "https://www.ncdoi.gov/consumers/medicare-and-seniors-health-insurance-information-program-shiip")
SRC_NCDOI_MEDIGAP = ("NC Department of Insurance / SHIIP: Medicare Supplement (Medigap) plans", "https://www.ncdoi.gov/consumers/medicare-and-seniors-health-insurance-information-program-shiip/medicare-supplement-medigap-plans")
SRC_NCDOI_U65 = ("NC Department of Insurance: Medicare supplement insurance for beneficiaries under age 65 (G.S. 58-54-45)", "https://www.ncdoi.gov/documents/files/medigap-under-age-65/open")
SRC_NCDOI_LIC = ("NC Department of Insurance: licensee lookup", "https://www.ncdoi.gov/licensees")
SRC_HIO_NC = ("healthinsurance.org: Medicare in North Carolina (enrollment figures from KFF, January 2026; Medigap rating practices)", "https://www.healthinsurance.org/medicare/north-carolina/")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_UNC_EXIT = ("Becker&rsquo;s Hospital Review: health systems dropping Medicare Advantage plans for 2026 (UNC Health)", "https://www.beckershospitalreview.com/finance/16-health-systems-dropping-medicare-advantage-plans-2026/")
SRC_UNC_BR = ("UNC Health Blue Ridge: Medicare Advantage plan changes effective January 1, 2026", "https://www.unchealthblueridge.org/medicare-advantage-plan-changes/")
SRC_CE_BCBS = ("Blue Cross NC: statement on the CarolinaEast network change (July 1, 2026)", "https://mediacenter.bcbsnc.com/news/blue-cross-nc-statement-on-carolinaeast-network-change")
SRC_CE_WITN = ("WITN (July 2, 2026): CarolinaEast secures UnitedHealthcare extension, still out of network for BCBS Advantage patients", "https://www.witn.com/2026/07/02/carolinaeast-secures-unitedhealthcare-extension-still-out-network-bcbs-advantage-patients/")
SRC_SHP = ("NC State Health Plan: 2026 retiree benefits (Humana Group Medicare Advantage)", "https://www.shpnc.gov/2026-retiree-benefits")
SRC_SHP_2027 = ("NC Department of State Treasurer (June 5, 2026): State Health Plan approves strategic plan and Medicare Advantage benefits", "https://www.nctreasurer.gov/news/press-releases/2026/06/05/state-health-plan-approves-strategic-plan-and-medicare-advantage-benefits")
SRC_MMR_NC = ("MyMedigapRate: North Carolina Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/north-carolina")
SRC_NC_MEDICAID_APPLY = ("NC Medicaid: how to apply (ePASS, county DSS, 888-245-0179)", "https://medicaid.ncdhhs.gov/apply")
SRC_MQB = ("Carteret County DSS: Medicare Qualified Beneficiaries (MQB-Q, MQB-B, MQB-E)", "https://www.carteretcountync.gov/2217/Medicare-Qualified-Beneficiaries-MQB")
SRC_DB101 = ("DB101 North Carolina: Medicare Savings Programs and what you pay", "https://nc.db101.org/nc/programs/health_coverage/medicare2/program2b.htm")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in North Carolina", crumb="Medicare Advantage", scene="charlotte",
     title="Medicare Advantage Plans in North Carolina [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in North Carolina: networks, $0 premiums, the 2026 UNC Health and CarolinaEast network exits, the State Health Plan&rsquo;s Humana group plan, and what a network change gives you. Free help from a licensed NC agent.",
     llm="Medicare Advantage (Part C) in North Carolina: how networks and bundled benefits work, the 2026 UNC Health and CarolinaEast network exits, the State Health Plan group plan, and what a network change versus a county exit gives you",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in North Carolina",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a county-by-county network, in a state where the big hospital systems have started walking away from some of them.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "About 1.33 million North Carolinians, close to 58 percent of the state&rsquo;s roughly 2.3 million Medicare beneficiaries, are in Advantage plans as of January 2026. Mecklenburg, Wake, Guilford and Forsyth have dozens of plans each; the Outer Banks and the far-western counties have a handful.",
               "Effective January 1, 2026, UNC Health (UNC Hospitals, UNC Rex and UNC Health Blue Ridge included) is out of network with Humana, WellCare and HCSC (formerly Cigna) Advantage plans; State Health Plan retirees on Humana&rsquo;s group plan kept access. CarolinaEast Medical Center in New Bern left Blue Cross NC&rsquo;s Advantage network on July 1, 2026.",
               "A hospital leaving a network is not a plan leaving your county. Only the second gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to Medigap; the first is fixed in the October 15 to December 7 window or, for current members, January 1 to March 31."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. In North Carolina the biggest enrollments belong to UnitedHealthcare, Humana and Blue Cross Blue Shield of North Carolina, with Aetna, WellCare, Cigna (now HCSC), Devoted Health, Alignment Health and Experience Health &mdash; the HMO Blue Cross NC built with Duke Health &mdash; among the others. Which of them sells in <em>your</em> county changes every year.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks, and the systems that sign them</h2>
<p>Advantage plans use provider networks (HMO or PPO) and are sold by county. That is the single most important thing to check before you enroll: whether your doctors and your hospital are in the plan&rsquo;s network, and whether your medications are on its drug list. North Carolina&rsquo;s care is organized into a handful of big systems &mdash; Atrium Health, Novant Health, Duke Health, UNC Health, WakeMed, Cone Health, ECU Health, Mission Health, Cape Fear Valley, FirstHealth &mdash; and each contracts with some plans and not others. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="warn-box"><p><strong>What changed for 2026, and why it matters this fall.</strong> Nationally, UnitedHealthcare left 225 counties and Humana 198 for the 2026 plan year. In North Carolina the bigger story was hospitals leaving plans rather than plans leaving counties. Effective January 1, 2026, <strong>UNC Health</strong> &mdash; UNC Hospitals in Chapel Hill, UNC Rex in Raleigh, UNC Health Blue Ridge in Morganton and the rest of the system &mdash; is out of network with <strong>Humana, WellCare and HCSC (formerly Cigna)</strong> Medicare Advantage plans; the one exception is State Health Plan retirees on Humana&rsquo;s group plan. On <strong>July 1, 2026, CarolinaEast Medical Center</strong> in New Bern left Blue Cross NC&rsquo;s Advantage network, citing denials and payment delays, and has announced a UnitedHealthcare exit that an extension pushed back; CarolinaEast&rsquo;s physician practices stayed in network and emergency care is still covered. If you were affected and have not fixed it, the Annual Election Period starting October 15 is the time.</p></div>
<h2>A network change is not a county exit</h2>
<p>The two get confused, and the rights are different. If your <em>plan</em> withdraws from your county, the non-renewal notice opens a Special Enrollment Period and, because you lost coverage involuntarily, federal rules give most people a <strong>guaranteed-issue right</strong> to buy a <a href="/medicare-supplement">Medigap policy</a> without medical underwriting, generally within 63 days of the coverage ending. If your <em>hospital</em> leaves the plan&rsquo;s network but the plan stays, you usually get no special window and no Medigap guarantee; you fix it during the Annual Election Period (October 15 to December 7) or, if you are already in an Advantage plan, the Medicare Advantage Open Enrollment Period (January 1 to March 31), when you can switch plans once or return to Original Medicare. There is one more door: if you joined an Advantage plan for the first time within the last twelve months, the federal trial right lets you go back to Original Medicare and buy a Medigap policy without underwriting. North Carolina has no birthday rule to fall back on afterward.</p>
<h2>The State Health Plan&rsquo;s group plan</h2>
<p>Nearly 177,000 retired state employees and teachers get Medicare coverage through the North Carolina State Health Plan&rsquo;s Humana Group Medicare Advantage PPO plans. For 2026 the Plan split medical and pharmacy into two Humana cards, and in June 2026 its board approved higher out-of-pocket maximums and copays for 2027. The group plan kept in-network access to UNC Health when the individual Humana plans lost it. Whether to stay on it or move to an individual plan is a real question with its own arithmetic &mdash; the State Health Plan&rsquo;s rules on leaving and returning matter &mdash; and we walk through it with the plan documents in front of us rather than from memory.</p>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, who are comfortable using a plan network, and who live where the menu is deep and their system is in it. If you split the year between North Carolina and somewhere else, see specialists in another system or another state, or want to use any provider nationwide, compare it against a <a href="/medicare-supplement">Medigap policy</a>. Newcomers should read <a href="/moving-to-north-carolina">Moving to North Carolina</a> first; military retirees with TRICARE For Life have their own calculation, on <a href="/veterans">Veterans</a>.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans for people with both Medicare and <a href="/medicaid">NC Medicaid</a>, which are a large part of the menu in Eastern North Carolina.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("UNC Health or CarolinaEast left my Advantage plan&rsquo;s network. Can I get a Medigap policy now?", "Usually not on a guaranteed-issue basis: a hospital leaving a network is not the same as your plan leaving your county. You can move to a plan your hospital accepts, or back to Original Medicare, during the Annual Election Period (October 15 to December 7) or the January 1 to March 31 Advantage open enrollment. If you joined Advantage for the first time in the last twelve months, the federal trial right lets you return to Original Medicare and buy Medigap without underwriting."),
           ("My North Carolina Advantage plan left my county. Can I get a Medigap policy now?", "In most cases, yes. Losing your plan through no fault of your own gives you a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending, plus a Special Enrollment Period to pick a new Advantage or Part D plan. Call before the deadline on your notice."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Special circumstances, including moving counties and FEMA-declared disasters, open other windows.")],
     sources=[SRC_MA_GOV, SRC_HIO_NC, SRC_KFF, SRC_UNC_EXIT, SRC_UNC_BR, SRC_CE_BCBS, SRC_CE_WITN, SRC_SHP, SRC_SHP_2027, SRC_MEDIGAP_GOV, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in North Carolina"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in North Carolina", crumb="Medicare Supplement", scene="blueridge",
     title="Medicare Supplement Plans in North Carolina: Plan G, Plan N &amp; the Rules | ECOS Medicare Solutions",
     desc="North Carolina Medigap explained: the standardized plans, the six-month open enrollment, the under-65 right to Plan A, D or G, guaranteed-issue events, no birthday rule, and how to compare carriers on filed rate history. Free help from a licensed NC agent.",
     llm="Medicare Supplement (Medigap) in North Carolina: standardized plans A-N, the six-month open enrollment, under-65 right to Plan A, D or G under G.S. 58-54-45, guaranteed-issue events, no birthday rule, attained-age rating, comparing carriers on filed rate history",
     eyebrow="Plans · Medigap", h1="Medicare Supplement (Medigap) plans in North Carolina",
     sub="A Medigap policy works alongside Original Medicare to pay much of what it leaves to you, and lets you use any provider in the country that accepts Medicare &mdash; Duke, UNC, Atrium, Mission, a Virginia specialist from the Outer Banks, or the clinic in your county seat.",
     keyfacts=["North Carolina uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company, so the comparison is price and rate history.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. During it, no insurer can turn you down or charge more for your health. North Carolina has no birthday rule and no annual window afterward.",
               "Under G.S. 58-54-45, people under 65 on Medicare because of a disability can buy Plan A, D or G during a six-month window that starts when Part B begins. Premiums may be higher than at 65, and a pre-existing-condition wait of up to six months can apply unless you had prior creditable coverage.",
               "Losing an Advantage plan or employer coverage through no fault of your own creates a guaranteed-issue right, generally 63 days long. A hospital leaving your plan&rsquo;s network, as UNC Health and CarolinaEast did in 2026, does not."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. The North Carolina Department of Insurance regulates the policies; the benefits inside each plan letter are set federally.</p>
<h2>How Medigap is different from Advantage</h2>
<table class="ctable">
<caption>A simplified comparison &mdash; the right choice depends on your health, doctors, county and budget.</caption>
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Medicare Supplement (Medigap)</th><th scope="col">Medicare Advantage</th></tr></thead>
<tbody>
<tr><th scope="row">Provider access</th><td>Any provider in the U.S. that accepts Medicare &mdash; no networks, no county lines, no hospital-contract surprises</td><td>Plan network (HMO/PPO), sold by county</td></tr>
<tr><th scope="row">Drug coverage</th><td>Add a separate Part D plan</td><td>Usually built in</td></tr>
<tr><th scope="row">Monthly premium</th><td>A monthly premium for the policy</td><td>Often $0 plan premium</td></tr>
<tr><th scope="row">Out-of-pocket</th><td>Very predictable; little to pay at the point of care on Plan G</td><td>Copays/coinsurance up to an annual cap</td></tr>
<tr><th scope="row">Extras (dental/vision)</th><td>Not included</td><td>Often included</td></tr>
<tr><th scope="row">Travel and second homes</th><td>Covered anywhere in the U.S.</td><td>Emergencies only on most plans out of area</td></tr>
</tbody></table>
<h2>The plans North Carolinians actually buy</h2>
<p><strong>Plan G</strong> covers everything Original Medicare leaves behind except the Part B deductible ($283 in [[YEAR]]). <strong>Plan N</strong> costs less in exchange for small office and emergency copays and no coverage of Part B excess charges. <strong>High-deductible Plan G</strong> has a much lower premium and a deductible you pay first. <strong>Plan F</strong> still exists for people who were eligible before 2020 but cannot be sold to anyone newer. Because benefits are standardized, we compare companies on price and on how fast they have raised it &mdash; and in North Carolina nearly every policy is <em>attained-age</em> rated, meaning the premium rises as you get older regardless of when you bought it, so the rate history matters more than the first-year price.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, every plan a company sells is guaranteed available regardless of health.</li>
<li><strong>Under 65 on disability.</strong> North Carolina law (G.S. 58-54-45) guarantees people under 65 on Medicare the right to buy Plan A, D or G during a six-month window that starts when Part B begins. Insurers may charge more than the over-65 rate and may impose a pre-existing-condition wait of up to six months, waived if you had prior creditable coverage. A second, full open enrollment arrives at 65.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage plan or employer coverage through no fault of your own gives you a window (generally 63 days) to buy certain plans without underwriting. So does the federal trial right: leaving an Advantage plan within twelve months of joining it for the first time.</li>
<li><strong>Outside those windows,</strong> North Carolina insurers can use medical underwriting, and North Carolina has no birthday rule, anniversary rule or annual Medigap window. Switching later usually means answering health questions.</li>
</ul>
<div class="note-box"><p><strong>Timing matters.</strong> A condition that would be irrelevant at 65 can mean a decline at 72. If you are approaching 65, moving here from a state with a birthday rule, or your Advantage plan just sent a non-renewal notice, talk to us before the window closes. A hospital leaving your plan&rsquo;s network &mdash; as UNC Health did for Humana, WellCare and Cigna members in 2026 &mdash; is not a guaranteed-issue event on its own.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between North Carolina Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate increases with the North Carolina Department of Insurance, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/north-carolina">North Carolina Medigap rate history</a>, with each figure tied to the filing it came from. If your premium has already gone up and you want to know why, <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes.</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; Duke and UNC without a network question, Mission from a far-western county, a Norfolk specialist from the Outer Banks &mdash; predictable costs, and coverage that travels. That last point is why so many people who <a href="/moving-to-north-carolina">move to North Carolina</a> keep the supplement they arrived with. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings. Free, unbiased counseling on all of it is available from NC SHIIP at 855-408-1212.</p>""",
     faqs=[("Do I need a separate drug plan with Medigap?", "Yes. Medigap does not include prescription coverage, so most people add a standalone Part D plan. We help you pick one around your specific medications."),
           ("Can I be turned down for Medigap in North Carolina?", "Not during your six-month open enrollment, and not during a guaranteed-issue event such as your Advantage plan leaving your county. Outside those windows, North Carolina insurers can use medical underwriting, and North Carolina has no birthday rule or annual switching window."),
           ("Is Plan F still available in North Carolina?", "Only to people who became eligible for Medicare before January 1, 2020. Everyone newer chooses from Plans G, N, high-deductible G and the others. We walk through which fits you."),
           ("I am under 65 on disability. Can I buy Medigap in North Carolina?", "Yes. G.S. 58-54-45 guarantees you Plan A, D or G during a six-month window that starts when Part B begins. Premiums may be higher than at 65 and a pre-existing-condition wait of up to six months can apply unless you had creditable coverage. You get a fresh open enrollment for every plan at 65."),
           ("How much does a North Carolina Medigap policy cost?", "It depends on the plan letter, your age, ZIP code, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MEDIGAP_GOV, SRC_NCDOI_MEDIGAP, SRC_NCDOI_U65, SRC_HIO_NC, SRC_MMR_NC, SRC_SHIIP, SRC_CMS], cta="Let&rsquo;s see whether Plan G, Plan N or something else fits you.", about="Medicare supplement insurance in North Carolina"),

dict(slug="part-d", nav_title="Medicare Part D plans in North Carolina", crumb="Part D", scene="tobacco",
     title="Medicare Part D Plans in North Carolina [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in North Carolina: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications and pharmacy (Walgreens, CVS, Walmart, Harris Teeter, Food Lion, independents), the late penalty, and Extra Help through the MQB programs.",
     llm="Part D drug plans in North Carolina: 2026 $2,100 cap, choosing by your medications and pharmacy, penalties, Extra Help through North Carolina's MQB Medicare Savings Programs",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in North Carolina",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Medigap policy, or nothing else.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life and VA pharmacy are creditable.",
               "Qualifying for a North Carolina Medicare Savings Program (MQB-Q, MQB-B or MQB-E) or Medicaid automatically qualifies you for Extra Help, which cuts Part D premiums and copays substantially."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list and your pharmacy</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at a Harris Teeter in Cary may be expensive at the independent pharmacy in Sparta or on Ocracoke. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, the State Health Plan, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources. In North Carolina, qualifying for a Medicare Savings Program &mdash; the state labels them MQB-Q, MQB-B and MQB-E &mdash; through your county Department of Social Services qualifies you for Extra Help automatically. See <a href="/medicaid">NC Medicaid, the MQB programs and Extra Help</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer plan, the State Health Plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Does my pharmacy matter?", "Yes. Each plan has preferred pharmacies where copays are lowest. Walgreens, CVS, Walmart, Harris Teeter, Food Lion, Publix and independents are preferred in different plans; we check yours when we compare."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_COSTS, SRC_MQB, SRC_NC_MEDICAID_APPLY], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in North Carolina"),

dict(slug="medicare-costs", nav_title="[[YEAR]] Medicare costs, full IRMAA chart, and penalty/IRMAA calculators", crumb="[[YEAR]] Costs", scene="raleigh",
     title="[[YEAR]] Medicare Costs &amp; IRMAA in North Carolina | ECOS Medicare Solutions",
     desc="[[YEAR]] Medicare costs for North Carolina: Part A/B/D premiums and deductibles, the full IRMAA income chart, and free calculators for IRMAA and late-enrollment penalties.",
     llm="2026 Medicare costs: Part A/B/D premiums and deductibles, the full IRMAA chart, and calculators for IRMAA and the Part B / Part D late penalties",
     eyebrow="Costs · Verified [[YEAR]] figures", h1="[[YEAR]] Medicare costs and IRMAA, with calculators",
     sub="Every dollar figure on this page comes from the CMS release for [[YEAR]]. The calculators are estimates for planning; Social Security and Medicare set your official amounts.",
     keyfacts=["[[YEAR]] Part B standard premium $202.90/month; Part B deductible $283; Part A hospital deductible $1,736 per benefit period.",
               "[[YEAR]] Part D: out-of-pocket cap $2,100; maximum deductible $615; national base premium $38.99.",
               "IRMAA surcharges begin above $109,000 (single) or $218,000 (joint) of 2024 modified adjusted gross income, and are a cliff: $1 over a threshold moves you to the whole next tier. Selling the family land, a lake house or a business two years ago, or a Roth conversion, is the usual surprise.",
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
<p>If your income is above the thresholds below, you pay an income-related surcharge on top of your Part B and Part D premiums. Your [[YEAR]] IRMAA is based on the income (MAGI) from your <strong>2024</strong> tax return. IRMAA is a cliff: going $1 over a threshold moves you into the whole next tier. In North Carolina the usual surprises are the sale of family land or a lake or beach house, a business sale at retirement, or a Roth conversion two years back.</p>
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
           ("Can I get help paying the Part B premium in North Carolina?", "Possibly. North Carolina&rsquo;s Medicare Savings Programs &mdash; MQB-Q, MQB-B and MQB-E, the state&rsquo;s names for QMB, SLMB and QI &mdash; pay the Part B premium for people with limited income and resources, and MQB-Q also covers Medicare&rsquo;s deductibles and copays. Apply through your county Department of Social Services or ePASS; see our NC Medicaid page.")],
     sources=[SRC_CMS, SRC_COSTS, SRC_MQB, SRC_NC_MEDICAID_APPLY], cta="Not sure which costs apply to you? Let&rsquo;s look together.", about="Medicare costs and IRMAA"),
]
