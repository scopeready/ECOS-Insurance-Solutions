"""South Carolina topic pages, part A: Advantage, Medigap, Part D, costs."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_SEP = ("Medicare.gov: Special Enrollment Periods, including moving and FEMA-declared disasters", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan/special-enrollment-periods")
SRC_CMS_HURR = ("CMS: hurricane and tropical storm emergency response actions", "https://www.cms.gov/about-cms/what-we-do/emergency-response/past-emergencies/hurricanes-tropical-storms")
SRC_SCDOI = ("South Carolina Department of Insurance: Medicare Supplement Insurance", "https://doi.sc.gov/639/Medicare-Supplement-Insurance")
SRC_SCDOI_GUIDE = ("South Carolina Department of Insurance: Medicare Supplement Insurance 2026 Shopper&rsquo;s Guide", "https://doi.sc.gov/809/Medicare-Supplement-Shoppers-Guide")
SRC_SCDOI_LOOKUP = ("South Carolina Department of Insurance: individual licensee search", "https://online.doi.sc.gov/eng/Public/Queries/IndvdlLicSrch.aspx")
SRC_ICARE = ("South Carolina Department on Aging: Medicare counseling through I-CARE (800-868-9095)", "https://aging.sc.gov/node/11")
SRC_ICARE_CMS = ("CMS SHIP directory: I-CARE, Insurance Counseling Assistance and Referrals for Elders, South Carolina", "https://www.cms.gov/contacts/i-care-insurance-counseling-assistance-and-referrals-elders/general-beneficiary-contact/1562201")
SRC_MRO = ("medicareresources.org: Medigap eligibility for people under 65, by state", "https://www.medicareresources.org/medicare-eligibility-and-enrollment/medigap-eligibility-for-americans-under-age-65-varies-by-state/")
SRC_HIO_SC = ("healthinsurance.org: Medicare in South Carolina (enrollment, Advantage share, Medigap rules)", "https://www.healthinsurance.org/medicare/south-carolina/")
SRC_KFF_2026 = ("KFF: Medicare Advantage in 2026, enrollment update and key trends", "https://www.kff.org/medicare/medicare-advantage-in-2026-enrollment-update-and-key-trends/")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_HCD = ("Healthcare Dive: UnitedHealthcare, Humana, Aetna scale back Medicare Advantage plans for 2026", "https://www.healthcaredive.com/news/medicare-advantage-plans-2026-unitedhealthcare-humana-aetna/801761/")
SRC_MMR_SC = ("MyMedigapRate: South Carolina Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/south-carolina")
SRC_MMR_T65 = ("MyMedigapRate: turning 65 in South Carolina", "https://www.mymedigaprate.com/turning-65/south-carolina")
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, the rules state by state", "https://www.mymedigaprate.com/switching-medigap-plans")
SRC_MMR_WHY = ("MyMedigapRate: why did my Medigap premium increase?", "https://www.mymedigaprate.com/why-did-my-medigap-premium-increase")
SRC_SCDHHS_APPLY = ("apply.scdhhs.gov: apply for Healthy Connections Medicaid and the Medicare Savings Programs", "https://apply.scdhhs.gov")
SRC_SCDHHS_ELIG = ("SCDHHS: program eligibility and income limits", "https://www.scdhhs.gov/members/program-eligibility-and-income-limits")
SRC_PRIME = ("SCDHHS: Healthy Connections Prime (ended December 31, 2025)", "https://scdhhs.gov/service/healthy-connections-prime")
SRC_SNP = ("SCDHHS: about Dual Special Needs Plans (D-SNPs)", "https://www.scdhhs.gov/members/managed-care-plan-information/dual-special-needs-plans/about-special-needs-plans-snps")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")
SRC_VA_CHS = ("VA: Ralph H. Johnson VA Health Care System, Charleston", "https://www.va.gov/charleston-health-care/")
SRC_VA_COLA = ("VA: Columbia VA Health Care System (Wm. Jennings Bryan Dorn VA Medical Center)", "https://www.va.gov/columbia-south-carolina-health-care/")
SRC_NOVANT = ("Novant Health: acquisition of Hilton Head Hospital, Coastal Carolina Hospital and East Cooper Medical Center (Feb 2024)", "https://www.novanthealth.org/newsroom/releases-20240201")
SRC_NCDOI_HELENE = ("North Carolina Department of Insurance: Special Enrollment Period for Medicare recipients affected by Helene (Oct 2024)", "https://www.ncdoi.gov/news/press-releases/2024/10/04/special-enrollment-period-medicare-recipients-affected-helenes-damage")
SRC_MEDICAID_HELENE = ("Medicaid.gov: Section 1135 waiver flexibilities, South Carolina 2024 Hurricane Helene disaster relief", "https://www.medicaid.gov/state-resource-center/disaster-response-toolkit/federal-disaster-resources/170866")
SRC_NIPR_SC = ("NIPR: South Carolina insurance licensing overview", "https://nipr.com/contact-state/south-carolina")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in South Carolina", crumb="Medicare Advantage", scene="harbor",
     title="Medicare Advantage Plans in South Carolina [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in South Carolina: networks built around MUSC, Prisma, Roper St. Francis and the regional systems, $0 premiums, the national 2026 pullbacks, and what a non-renewal notice gives you. Free help from a licensed South Carolina agent.",
     llm="Medicare Advantage (Part C) in South Carolina: how networks and bundled benefits work, roughly 46% of the state's beneficiaries enrolled, plans in all 46 counties, the 2026 national carrier pullbacks, and what a non-renewal notice gives you",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in South Carolina",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a county-by-county network, in a state where the big health systems each sign their own contracts.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "About 1.25 million South Carolinians are on Medicare and roughly 46% of them are in Advantage plans as of early 2026, close to the national share. Advantage plans are marketed in all 46 counties, but the menu in Greenville, Charleston or Horry County is much deeper than in Allendale or McCormick.",
               "For the 2026 plan year UnitedHealthcare, Humana and Aetna each cut the number of counties they serve nationally. Your Annual Notice of Change, not a headline, tells you whether your South Carolina plan changed.",
               "A plan leaving your county gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. In South Carolina the plan is sold by county, and which carriers sell in <em>your</em> county &mdash; and which hospitals they have signed &mdash; changes every October.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks, county by county</h2>
<p>Advantage plans use provider networks (HMO or PPO) and are sold by county. That is the single most important thing to check before you enroll: whether your doctors and your hospital are in the plan&rsquo;s network, and whether your medications are on its drug list. South Carolina&rsquo;s care is organized into a handful of large systems &mdash; Prisma Health in the Upstate and Midlands, MUSC Health from Charleston to Florence, Lancaster and Columbia, Roper St. Francis and Trident in the Lowcountry, Spartanburg Regional, McLeod and Grand Strand along the coast and the Pee Dee, Lexington Medical Center, AnMed, Self Regional, Tidelands and the Novant hospitals in Beaufort and Jasper counties &mdash; and each contracts with some plans and not others. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="warn-box"><p><strong>What changed for 2026, and why it matters this fall.</strong> Nationally, UnitedHealthcare, Humana and Aetna each reduced the number of counties they serve for the 2026 plan year, and premiums rose for many plans that charge one. We have not seen a source naming specific South Carolina county exits, so we will not invent a list: your Annual Notice of Change, mailed by the end of September, is the document that tells you whether your plan&rsquo;s premium, network or drug list changed. If you were moved into a new plan, or picked one in a hurry last fall, the Annual Election Period starting October 15 is the time to check it actually fits.</p></div>
<h2>If your plan left your county</h2>
<p>A non-renewal notice is not just bad news; it opens doors. You get a Special Enrollment Period that runs past the normal deadlines, and because the plan left you involuntarily, federal rules give most people a <strong>guaranteed-issue right</strong> to buy a <a href="/medicare-supplement">Medigap policy</a> without medical underwriting &mdash; even if you are well past your original six-month Medigap window. The right is time-limited (generally 63 days after your coverage ends), so do not let the notice sit. South Carolina has no birthday rule or annual Medigap window to fall back on afterward.</p>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, who are comfortable using a plan network, and who live where the menu is deep. If you split the year between the coast and a grandchild up north, see specialists at Duke, Emory or Mayo, or want to use any provider nationwide, compare it against a <a href="/medicare-supplement">Medigap policy</a> &mdash; our <a href="/new-to-south-carolina">moving to South Carolina guide</a> walks through which plans travel. Military retirees with TRICARE For Life have their own calculation; see <a href="/veterans">Veterans</a>.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans for people with both Medicare and <a href="/medicaid">Healthy Connections Medicaid</a>, which took over from Healthy Connections Prime at the start of 2026.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("My South Carolina Advantage plan left my county. Can I get a Medigap policy now?", "In most cases, yes. Losing your plan through no fault of your own gives you a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending, plus a Special Enrollment Period to pick a new Advantage or Part D plan. Call before the deadline on your notice."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Moving, a FEMA disaster declaration and other circumstances open other windows.")],
     sources=[SRC_MA_GOV, SRC_HIO_SC, SRC_KFF_2026, SRC_KFF, SRC_HCD, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in South Carolina"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in South Carolina", crumb="Medicare Supplement", scene="marsh",
     title="Medicare Supplement Plans in South Carolina: Plan G, Plan N &amp; the Rules | ECOS Medicare Solutions",
     desc="South Carolina Medigap explained: the standardized plans, the six-month open enrollment that does not repeat, no birthday rule, under-65 options, guaranteed issue after a move or a plan exit, and how to compare carriers on filed rate history. Free help from a licensed South Carolina agent.",
     llm="Medicare Supplement (Medigap) in South Carolina: standardized plans A-N, the six-month open enrollment, no birthday or anniversary rule, under-65 access not required by state law, guaranteed-issue events, comparing carriers on filed rate history",
     eyebrow="Plans · Medigap", h1="Medicare Supplement (Medigap) plans in South Carolina",
     sub="A Medigap policy works alongside Original Medicare to pay much of what it leaves to you, and lets you use any provider in the country that accepts Medicare &mdash; MUSC, Prisma, Duke across the line, or the clinic in your county seat.",
     keyfacts=["South Carolina uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company, so the comparison is price and rate history.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. During it, no insurer can turn you down or charge more for your health. South Carolina has no birthday rule, anniversary rule or annual window afterward.",
               "South Carolina law does not require insurers to sell Medigap to people under 65 who are on Medicare because of a disability. Some carriers do so voluntarily, and the state&rsquo;s high-risk pool offers guaranteed-issue options for that group; at 65 you get the full open enrollment like everyone else.",
               "Losing an Advantage plan, moving out of an Advantage plan&rsquo;s service area, or losing employer coverage through no fault of your own creates a guaranteed-issue right, generally 63 days long. For a state that adds tens of thousands of retirees a year, the moving one matters."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. The South Carolina Department of Insurance regulates the policies and publishes a yearly shopper&rsquo;s guide; the benefits inside each plan letter are set federally.</p>
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
<tr><th scope="row">Travel and second homes</th><td>Covered anywhere in the U.S.</td><td>Emergencies only on most plans out of area</td></tr>
</tbody></table>
<h2>The plans South Carolinians actually buy</h2>
<p><strong>Plan G</strong> covers everything Original Medicare leaves behind except the Part B deductible ($283 in [[YEAR]]). <strong>Plan N</strong> costs less in exchange for small office and emergency copays and no coverage of Part B excess charges. <strong>High-deductible Plan G</strong> has a much lower premium and a deductible you pay first. <strong>Plan F</strong> still exists for people who were eligible before 2020 but cannot be sold to anyone newer. Because benefits are standardized, we compare companies on price and on how fast they have raised it.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, every plan a company sells is guaranteed available regardless of health.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage plan or employer coverage through no fault of your own, or moving out of your Advantage plan&rsquo;s service area, gives you a window (generally 63 days) to buy certain plans without underwriting. If you are arriving in South Carolina from an Advantage plan up north, this is your door into a supplement; see <a href="/new-to-south-carolina">moving to South Carolina</a>.</li>
<li><strong>Under 65 on disability.</strong> South Carolina does not require insurers to offer Medigap to people under 65. Some carriers choose to, usually at a higher premium, and the state&rsquo;s high-risk pool has offered guaranteed-issue Medigap options for people under 65 on Medicare. I-CARE (800-868-9095) and the Department of Insurance shopper&rsquo;s guide list what is currently sold; a fresh open enrollment for every plan arrives at 65.</li>
<li><strong>Outside those windows,</strong> South Carolina insurers can use medical underwriting, and South Carolina has no birthday rule, anniversary rule or annual Medigap window. Switching later usually means answering health questions.</li>
</ul>
<div class="note-box"><p><strong>Timing matters.</strong> A condition that would be irrelevant at 65 can mean a decline at 72. If you are approaching 65, just moved here, or your Advantage plan sent a non-renewal notice, talk to us before the window closes.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between South Carolina Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate increases with the South Carolina Department of Insurance, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/south-carolina">South Carolina Medigap rate history</a>, with each figure tied to the filing it came from. If your premium has already gone up and you want to know why, <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes &mdash; and in a state with no birthday rule, whether you can move to a cheaper carrier depends on your health, so ask before you cancel anything.</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; MUSC or Prisma without a network question, a specialist at Duke or Emory from a rural county &mdash; predictable costs, and coverage that travels. That last point is why so many <a href="/new-to-south-carolina">retirees who split the year</a> keep a supplement. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings.</p>""",
     faqs=[("Do I need a separate drug plan with Medigap?", "Yes. Medigap does not include prescription coverage, so most people add a standalone Part D plan. We help you pick one around your specific medications."),
           ("Can I be turned down for Medigap in South Carolina?", "Not during your six-month open enrollment, and not during a guaranteed-issue event such as your Advantage plan leaving your county or you moving out of its service area. Outside those windows, South Carolina insurers can use medical underwriting, and South Carolina has no birthday rule or annual switching window."),
           ("Is Plan F still available in South Carolina?", "Only to people who became eligible for Medicare before January 1, 2020. Everyone newer chooses from Plans G, N, high-deductible G and the others. We walk through which fits you."),
           ("I am under 65 on disability. Can I buy Medigap in South Carolina?", "State law does not require insurers to sell to you, but some carriers do, and South Carolina&rsquo;s high-risk pool has offered guaranteed-issue Medigap options for people under 65 on Medicare. Premiums for under-65 coverage are generally higher. I-CARE (800-868-9095) can tell you what is currently offered, and you get a full open enrollment for every plan at 65."),
           ("How much does a South Carolina Medigap policy cost?", "It depends on the plan letter, your age, ZIP code, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MEDIGAP_GOV, SRC_SCDOI, SRC_SCDOI_GUIDE, SRC_MRO, SRC_HIO_SC, SRC_MMR_SC, SRC_MMR_SWITCH, SRC_CMS], cta="Let&rsquo;s see whether Plan G, Plan N or something else fits you.", about="Medicare supplement insurance in South Carolina"),

dict(slug="part-d", nav_title="Medicare Part D plans in South Carolina", crumb="Part D", scene="peaches",
     title="Medicare Part D Plans in South Carolina [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in South Carolina: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications and pharmacy (Publix, CVS, Walgreens, Walmart, independents), the late penalty, hurricane refills, and Extra Help.",
     llm="Part D drug plans in South Carolina: 2026 $2,100 cap, choosing by your medications and pharmacy, penalties, early refills in a declared hurricane emergency, Extra Help through South Carolina's Medicare Savings Programs",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in South Carolina",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Medigap policy, or nothing else.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life and VA pharmacy are creditable.",
               "Qualifying for a South Carolina Medicare Savings Program or Healthy Connections Medicaid automatically qualifies you for Extra Help, which cuts Part D premiums and copays substantially. During a declared hurricane emergency, plans must allow early refills in the affected area."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list and your pharmacy</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at the Publix in Mount Pleasant may be expensive at the independent pharmacy in Walterboro. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Hurricanes and refills</h2>
<p>When a hurricane emergency is declared for your area, Medicare requires Part D plans to lift refill-too-soon limits so you can fill early before you evacuate, to allow out-of-network pharmacies when yours is closed, and to relax prior-authorization rules for medications you already take. Ask your pharmacy for an emergency refill as soon as a watch is posted for the coast; do not wait for the warning. Our <a href="/new-to-south-carolina">moving to South Carolina guide</a> covers the rest, including the disaster Special Enrollment Period.</p>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources. In South Carolina, qualifying for a Medicare Savings Program (QMB, SLMB or QI) through SCDHHS qualifies you for Extra Help automatically. See <a href="/medicaid">Healthy Connections Medicaid and the Medicare Savings Programs</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Does my pharmacy matter?", "Yes. Each plan has preferred pharmacies where copays are lowest. Publix, CVS, Walgreens, Walmart and independents are preferred in different plans; we check yours when we compare."),
           ("Can I get an early refill before a hurricane?", "Yes, once an emergency is declared for your area. Part D plans must lift refill-too-soon limits and allow out-of-network pharmacies in the affected area. Ask your pharmacy as soon as a watch is posted."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_COSTS, SRC_CMS_HURR, SRC_SCDHHS_APPLY], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in South Carolina"),

dict(slug="medicare-costs", nav_title="[[YEAR]] Medicare costs, full IRMAA chart, and penalty/IRMAA calculators", crumb="[[YEAR]] Costs", scene="statehouse",
     title="[[YEAR]] Medicare Costs &amp; IRMAA in South Carolina | ECOS Medicare Solutions",
     desc="[[YEAR]] Medicare costs for South Carolina: Part A/B/D premiums and deductibles, the full IRMAA income chart, and free calculators for IRMAA and late-enrollment penalties.",
     llm="2026 Medicare costs: Part A/B/D premiums and deductibles, the full IRMAA chart, and calculators for IRMAA and the Part B / Part D late penalties",
     eyebrow="Costs · Verified [[YEAR]] figures", h1="[[YEAR]] Medicare costs and IRMAA, with calculators",
     sub="Every dollar figure on this page comes from the CMS release for [[YEAR]]. The calculators are estimates for planning; Social Security and Medicare set your official amounts.",
     keyfacts=["[[YEAR]] Part B standard premium $202.90/month; Part B deductible $283; Part A hospital deductible $1,736 per benefit period.",
               "[[YEAR]] Part D: out-of-pocket cap $2,100; maximum deductible $615; national base premium $38.99.",
               "IRMAA surcharges begin above $109,000 (single) or $218,000 (joint) of 2024 modified adjusted gross income, and are a cliff: $1 over a threshold moves you to the whole next tier. The sale of a house up north before the move, or a Roth conversion two years ago, is the usual surprise.",
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
<p>If your income is above the thresholds below, you pay an income-related surcharge on top of your Part B and Part D premiums. Your [[YEAR]] IRMAA is based on the income (MAGI) from your <strong>2024</strong> tax return. IRMAA is a cliff: going $1 over a threshold moves you into the whole next tier. For a lot of new South Carolinians the surprise is the year they sold the house in New Jersey or Ohio; for others it is a Roth conversion or a business sale two years back.</p>
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
           ("Can I get help paying the Part B premium in South Carolina?", "Possibly. South Carolina&rsquo;s Medicare Savings Programs (QMB, SLMB and QI), run by SCDHHS, pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply at apply.scdhhs.gov; see our Healthy Connections Medicaid page.")],
     sources=[SRC_CMS, SRC_COSTS, SRC_SCDHHS_APPLY], cta="Not sure which costs apply to you? Let&rsquo;s look together.", about="Medicare costs and IRMAA"),
]
