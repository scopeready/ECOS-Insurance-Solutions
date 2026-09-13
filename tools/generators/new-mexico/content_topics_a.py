"""New Mexico topic pages, part A: Advantage, Medigap, Part D, costs."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_SEP = ("Medicare.gov: Special Enrollment Periods", "https://www.medicare.gov/basics/get-started-with-medicare/get-more-coverage/joining-a-plan/special-enrollment-periods")
SRC_OSI = ("New Mexico Office of Superintendent of Insurance", "https://www.osi.state.nm.us")
SRC_OSI_LIC = ("NM Office of Superintendent of Insurance: license status verification", "https://osi.state.nm.us/en/insurance-professionals/license-status-verification/")
SRC_ALTSD_SHIP = ("NM Aging &amp; Long-Term Services Department: State Health Insurance Assistance Program (800-432-2080)", "https://aging.nm.gov/services/aging-disability-resource-center-adrc/medicare/ship")
SRC_SHIP_NM = ("SHIP National Technical Assistance Center: New Mexico", "https://www.shiphelp.org/ships/new-mexico/")
SRC_SB21 = ("NM Aging &amp; Long-Term Services Department: Senate Bill 21 (2026), Medigap annual open enrollment (birthday rule)", "https://www.aging.nm.gov/2026-legislature/senate-bill-21-2026/")
SRC_BECKERS_BDAY = ("Becker&rsquo;s Payer Issues: West Virginia, New Mexico to roll out Medigap birthday rules", "https://www.beckerspayer.com/policy-updates/west-virginia-new-mexico-to-roll-out-medigap-birthday-rules/")
SRC_HIO_NM = ("healthinsurance.org: Medicare in New Mexico (enrollment, plan counts, under-65 Medigap, NMMIP)", "https://www.healthinsurance.org/medicare/new-mexico/")
SRC_NMMIP = ("New Mexico Medical Insurance Pool: eligibility and coverage (Medicare Carve-Out Plan)", "https://nmmip.org/eligibility-and-coverage/benefits-and-eligibility/")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_FIERCE = ("Fierce Healthcare: Presbyterian Healthcare Services to discontinue MA plans in 2027", "https://www.fiercehealthcare.com/payers/presbyterian-healthcare-services-discontinue-ma-plans-2027")
SRC_SEARCHLIGHT = ("Searchlight New Mexico: lawmakers press Presbyterian Health Plan over changes", "https://searchlightnm.org/new-mexico-lawmakers-press-presbyterian-health-plan-over-changes/")
SRC_BCBSNM = ("Blue Cross and Blue Shield of New Mexico: Medicare Advantage plans in 31 New Mexico counties in 2026", "https://www.bcbsnm.com/newsroom/news-releases/2025/medicare-advantage-plans-2026")
SRC_MMR_NM = ("MyMedigapRate: New Mexico Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/new-mexico")
SRC_HCA_TC = ("New Mexico Health Care Authority: Turquoise Care overview", "https://www.hca.nm.gov/turquoise-care/")
SRC_HCA_PLANS = ("New Mexico Health Care Authority: Turquoise Care health plans", "https://www.hca.nm.gov/turquoise-care-health-plans/")
SRC_HSD_MSP = ("NM Human Services Department (now the Health Care Authority), July 12, 2021: asset test eliminated for Medicare Savings Programs", "https://www.hsd.state.nm.us/2021/07/12/hsd-makes-it-easier-for-low-income-seniors-to-afford-medicare/")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in New Mexico", crumb="Medicare Advantage", scene="balloons",
     title="Medicare Advantage Plans in New Mexico [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in New Mexico: networks, $0 premiums, Presbyterian's exit from most Advantage plans for 2027, what a non-renewal notice gives you, and how county menus differ from Albuquerque to Catron County. Free help from a licensed agent.",
     llm="Medicare Advantage (Part C) in New Mexico: how networks and bundled benefits work, Presbyterian Health Plan's 2027 exit from most Advantage plans, county-by-county availability, and what a non-renewal notice gives you",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in New Mexico",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a county-by-county network, in a state where the biggest local carrier is stepping back for 2027.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "Roughly 470,000 New Mexicans have Medicare and, as of January 2026, about half were in Advantage plans. 73 Advantage plans were on sale across the state for [[YEAR]], averaging about 24 per county, with Bernalillo and Do&ntilde;a Ana counties far deeper than the rural ones.",
               "Presbyterian Health Plan announced in June 2026 that it will discontinue most of its Medicare Advantage plans for 2027, affecting about 30,000 members. It keeps its Dual Plus plan for people who also have Medicaid. Coverage runs through December 31, 2026.",
               "A plan leaving you at year end gives you the Annual Election Period (Oct 15&ndash;Dec 7) to choose, a Special Enrollment Period if you need more time, and in most cases a guaranteed-issue right to buy a Medigap policy without health questions, for a limited window around the date the coverage ends."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. In New Mexico the plans on sale for [[YEAR]] come from national carriers &mdash; Blue Cross and Blue Shield of New Mexico, for example, sells Advantage plans in 31 of the 33 counties &mdash; and, through the end of this year, from Presbyterian Health Plan, the Albuquerque system&rsquo;s own insurer. Which of them sells in <em>your</em> county changes every October.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks, county by county</h2>
<p>Advantage plans use provider networks (HMO or PPO) and are sold by county. That is the single most important thing to check before you enroll: whether your doctors and your hospital are in the plan&rsquo;s network, and whether your medications are on its drug list. New Mexico&rsquo;s care is organized around a handful of systems &mdash; Presbyterian, UNM Health and Lovelace in the Albuquerque area, Christus St. Vincent in Santa Fe, San Juan Regional in Farmington, MountainView and Memorial Medical Center in Las Cruces &mdash; and each contracts with some plans and not others. Outside the cities the question is sharper: the nearest in-network specialist may be in Albuquerque, El Paso or Lubbock, and the plan&rsquo;s rules for out-of-area care decide whether that drive is covered. Our <a href="/rural-new-mexico">rural New Mexico guide</a> walks through it. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="warn-box"><p><strong>What changed for 2027, and why it matters this fall.</strong> In June 2026 Presbyterian Healthcare Services said it will discontinue most of its Medicare Advantage plans for the 2027 plan year, citing more than $59 million in losses on them in 2025, rising medical costs and regulatory change. About 30,000 members are affected; roughly 150 health-plan jobs are being cut. Presbyterian keeps its <strong>Dual Plus</strong> Special Needs Plan for people with both Medicare and Medicaid. Nothing changes for 2026 &mdash; your coverage runs through December 31 &mdash; but if you are on a Presbyterian Advantage plan, the Annual Election Period that opens October 15 is when you choose what comes next, and the choice includes Original Medicare with a Medigap policy, not only another Advantage plan. Nationally, UnitedHealthcare left 225 counties and Humana 198 for 2026, so county menus elsewhere in the state can shift too.</p></div>
<h2>If your plan is leaving</h2>
<p>A non-renewal notice is not just bad news; it opens doors. Because the plan is leaving you involuntarily, federal rules give most people a <strong>guaranteed-issue right</strong> to buy a <a href="/medicare-supplement">Medigap policy</a> without medical underwriting &mdash; even if you are years past your original six-month Medigap window &mdash; and a Special Enrollment Period to pick a new Advantage or Part D plan if you miss the December 7 deadline. The Medigap right is time-limited (generally it runs from the notice until about 63 days after your coverage ends), so do not let the notice sit. New Mexico&rsquo;s new birthday rule does not start until January 1, 2027, and it only lets you move between Medigap plans, so it is not a substitute for using this window well.</p>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, who are comfortable using a plan network, and who live where the menu is deep and the hospitals are close. If you live an hour from the nearest hospital, see specialists in another state, split the year with Arizona or Texas, or simply want to use any provider nationwide, compare it against a <a href="/medicare-supplement">Medigap policy</a>. Military retirees with TRICARE For Life have their own calculation; see <a href="/veterans">Veterans</a>.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans for people with both Medicare and <a href="/medicaid">Turquoise Care</a>, New Mexico&rsquo;s Medicaid program.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("Presbyterian is ending my Advantage plan for 2027. Can I get a Medigap policy now?", "In most cases, yes. Losing your plan through no fault of your own gives you a guaranteed-issue right to buy a Medigap policy without health questions for a limited window around the date the coverage ends, plus the Annual Election Period and a Special Enrollment Period to pick new Advantage or Part D coverage. Your 2026 coverage continues through December 31. Call before the deadline on your notice."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Special circumstances, including moving counties, open other windows.")],
     sources=[SRC_MA_GOV, SRC_HIO_NM, SRC_FIERCE, SRC_SEARCHLIGHT, SRC_BCBSNM, SRC_KFF, SRC_SEP, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in New Mexico"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in New Mexico", crumb="Medicare Supplement", scene="adobe",
     title="Medicare Supplement Plans in New Mexico: Plan G, Plan N &amp; the 2027 Birthday Rule | ECOS Medicare Solutions",
     desc="New Mexico Medigap explained: the standardized plans, the six-month open enrollment, the 60-day birthday rule that starts January 1, 2027, under-65 access through NMMIP, guaranteed issue after a plan exit, and comparing carriers on filed rate history.",
     llm="Medicare Supplement (Medigap) in New Mexico: standardized plans A-N regulated by OSI, the six-month open enrollment, the SB 21 birthday rule effective 2027, no under-65 requirement (NMMIP carve-out plan instead), guaranteed-issue events, comparing carriers on filed rate history",
     eyebrow="Plans · Medigap", h1="Medicare Supplement (Medigap) plans in New Mexico",
     sub="A Medigap policy works alongside Original Medicare to pay much of what it leaves to you, and lets you use any provider in the country that accepts Medicare &mdash; UNM, Christus St. Vincent, an El Paso or Denver specialist, or the clinic in your county seat.",
     keyfacts=["New Mexico uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company, so the comparison is price and rate history. The Office of Superintendent of Insurance (OSI) regulates the policies.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. During it, no insurer can turn you down or charge more for your health.",
               "From January 1, 2027, Senate Bill 21 (2026) gives New Mexicans on Medigap a 60-day window each year, starting the first day of their birthday month, to switch to a Medigap plan of equal or lesser benefits without medical underwriting.",
               "New Mexico does not require insurers to sell Medigap to people under 65 on Medicare, and as of 2026 none were doing so. The New Mexico Medical Insurance Pool (NMMIP) offers a Medicare Carve-Out Plan to under-65 beneficiaries who have Parts A and B.",
               "Losing an Advantage plan or employer coverage through no fault of your own creates a guaranteed-issue right. Presbyterian&rsquo;s exit from most Advantage plans for 2027 will trigger it for a lot of New Mexicans this fall."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. The New Mexico Office of Superintendent of Insurance regulates the policies; the benefits inside each plan letter are set federally.</p>
<h2>How Medigap is different from Advantage</h2>
<table class="ctable">
<caption>A simplified comparison &mdash; the right choice depends on your health, doctors, county and budget.</caption>
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Medicare Supplement (Medigap)</th><th scope="col">Medicare Advantage</th></tr></thead>
<tbody>
<tr><th scope="row">Provider access</th><td>Any provider in the U.S. that accepts Medicare &mdash; no networks, no county lines, no state lines</td><td>Plan network (HMO/PPO), sold by county</td></tr>
<tr><th scope="row">Drug coverage</th><td>Add a separate Part D plan</td><td>Usually built in</td></tr>
<tr><th scope="row">Monthly premium</th><td>A monthly premium for the policy</td><td>Often $0 plan premium</td></tr>
<tr><th scope="row">Out-of-pocket</th><td>Very predictable; little to pay at the point of care on Plan G</td><td>Copays/coinsurance up to an annual cap</td></tr>
<tr><th scope="row">Extras (dental/vision)</th><td>Not included</td><td>Often included</td></tr>
<tr><th scope="row">Long drives and second homes</th><td>Covered anywhere in the U.S. &mdash; El Paso, Lubbock, Denver, Tucson</td><td>Emergencies only on most plans out of area</td></tr>
</tbody></table>
<h2>The plans New Mexicans actually buy</h2>
<p><strong>Plan G</strong> covers everything Original Medicare leaves behind except the Part B deductible ($283 in [[YEAR]]). <strong>Plan N</strong> costs less in exchange for small office and emergency copays and no coverage of Part B excess charges. <strong>High-deductible Plan G</strong> has a much lower premium and a deductible you pay first. <strong>Plan F</strong> still exists for people who were eligible before 2020 but cannot be sold to anyone newer. Because benefits are standardized, we compare companies on price and on how fast they have raised it.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, every plan a company sells is guaranteed available regardless of health.</li>
<li><strong>The birthday rule, from January 1, 2027.</strong> Senate Bill 21, signed in March 2026, gives people who already have a Medigap policy a 60-day window each year, beginning on the first day of their birthday month, to move to a Medigap plan of equal or lesser benefits without medical underwriting. The law as written does not confine you to your current insurer, and the state expects it to help more than 70,000 policyholders. The Superintendent of Insurance&rsquo;s implementing rules will settle the details, such as exactly which plans count as &ldquo;equal or lesser&rdquo;; we will update this page when they are published.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage plan or employer coverage through no fault of your own gives you a window (generally about 63 days after the coverage ends) to buy certain plans without underwriting. Presbyterian&rsquo;s 2027 exit will trigger this for many New Mexicans.</li>
<li><strong>Under 65 on disability.</strong> New Mexico does not require insurers to offer Medigap to people under 65, and OSI confirmed none were doing so voluntarily as of 2026. The state&rsquo;s high-risk pool, the New Mexico Medical Insurance Pool, offers a <strong>Medicare Carve-Out Plan</strong> to under-65 beneficiaries who have both Part A and Part B. A full open enrollment for every plan letter arrives at 65.</li>
<li><strong>Outside those windows,</strong> New Mexico insurers can use medical underwriting. Until the birthday rule starts, switching later usually means answering health questions.</li>
</ul>
<div class="note-box"><p><strong>Timing matters.</strong> A condition that would be irrelevant at 65 can mean a decline at 72, and the 2027 birthday rule only lets you move sideways or down in benefits, not up. If you are approaching 65, or your Advantage plan just sent a non-renewal notice, talk to us before the window closes.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between New Mexico Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate increases with the Office of Superintendent of Insurance, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/new-mexico">New Mexico Medigap rate history</a>, with each figure tied to the filing it came from. If your premium has already gone up and you want to know why, <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes.</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; UNM or Christus St. Vincent without a network question, an El Paso oncologist from Silver City, a Denver specialist from Farmington &mdash; predictable costs, and coverage that travels. In a state with New Mexico&rsquo;s distances, that is a lot of people; our <a href="/rural-new-mexico">rural New Mexico guide</a> explains why. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings.</p>""",
     faqs=[("Do I need a separate drug plan with Medigap?", "Yes. Medigap does not include prescription coverage, so most people add a standalone Part D plan. We help you pick one around your specific medications."),
           ("Can I be turned down for Medigap in New Mexico?", "Not during your six-month open enrollment, not during a guaranteed-issue event such as your Advantage plan leaving, and &mdash; from January 1, 2027 &mdash; not during your 60-day birthday window if you are moving to a plan of equal or lesser benefits. Outside those windows, New Mexico insurers can use medical underwriting."),
           ("What is New Mexico&rsquo;s Medigap birthday rule?", "Senate Bill 21 (2026) creates an annual guaranteed-issue window for people who already have a Medigap policy: 60 days beginning on the first day of your birthday month, to switch to a Medigap plan with equal or lesser benefits, with no health questions. It takes effect January 1, 2027."),
           ("I am under 65 on disability. Can I buy Medigap in New Mexico?", "New Mexico does not require insurers to sell Medigap to people under 65, and as of 2026 none did. The New Mexico Medical Insurance Pool&rsquo;s Medicare Carve-Out Plan is the state&rsquo;s alternative for under-65 beneficiaries with Parts A and B. You get a full open enrollment for every plan at 65."),
           ("How much does a New Mexico Medigap policy cost?", "It depends on the plan letter, your age, ZIP code, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MEDIGAP_GOV, SRC_SB21, SRC_BECKERS_BDAY, SRC_HIO_NM, SRC_NMMIP, SRC_OSI, SRC_MMR_NM, SRC_CMS], cta="Let&rsquo;s see whether Plan G, Plan N or something else fits you.", about="Medicare supplement insurance in New Mexico"),

dict(slug="part-d", nav_title="Medicare Part D plans in New Mexico", crumb="Part D", scene="plains",
     title="Medicare Part D Plans in New Mexico [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in New Mexico: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications and pharmacy (chain, independent, mail order, IHS), the late penalty, and Extra Help through New Mexico's Medicare Savings Programs.",
     llm="Part D drug plans in New Mexico: 2026 $2,100 cap, choosing by your medications and pharmacy, penalties, Extra Help through New Mexico Medicare Savings Programs (no asset test)",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in New Mexico",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Medigap policy, or nothing else.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life and VA pharmacy are creditable.",
               "Qualifying for a New Mexico Medicare Savings Program (QMB, SLMB or QI) &mdash; which has no asset test in New Mexico &mdash; or for Medicaid automatically qualifies you for Extra Help, which cuts Part D premiums and copays substantially."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list and your pharmacy</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at a chain pharmacy in Albuquerque may be expensive at the one independent pharmacy in a mountain town. In much of New Mexico the practical question is which pharmacy you can actually reach: mail order at 90-day supplies solves a lot of it, and if you fill prescriptions at an IHS or tribal pharmacy, ask how the plan treats that. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources. In New Mexico, qualifying for a Medicare Savings Program (QMB, SLMB or QI) through the Health Care Authority qualifies you for Extra Help automatically, and New Mexico dropped the asset test for those programs in 2021, so only your income counts. See <a href="/medicaid">Turquoise Care, the Medicare Savings Programs and Extra Help</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Does my pharmacy matter?", "Yes. Each plan has preferred pharmacies where copays are lowest, and in rural New Mexico the preferred chain may be an hour away. We check the pharmacy you actually use, and whether mail order makes more sense, when we compare."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_COSTS, SRC_HSD_MSP], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in New Mexico"),

dict(slug="medicare-costs", nav_title="[[YEAR]] Medicare costs, full IRMAA chart, and penalty/IRMAA calculators", crumb="[[YEAR]] Costs", scene="ristras",
     title="[[YEAR]] Medicare Costs &amp; IRMAA in New Mexico | ECOS Medicare Solutions",
     desc="[[YEAR]] Medicare costs for New Mexico: Part A/B/D premiums and deductibles, the full IRMAA income chart, and free calculators for IRMAA and late-enrollment penalties.",
     llm="2026 Medicare costs: Part A/B/D premiums and deductibles, the full IRMAA chart, and calculators for IRMAA and the Part B / Part D late penalties",
     eyebrow="Costs · Verified [[YEAR]] figures", h1="[[YEAR]] Medicare costs and IRMAA, with calculators",
     sub="Every dollar figure on this page comes from the CMS release for [[YEAR]]. The calculators are estimates for planning; Social Security and Medicare set your official amounts.",
     keyfacts=["[[YEAR]] Part B standard premium $202.90/month; Part B deductible $283; Part A hospital deductible $1,736 per benefit period.",
               "[[YEAR]] Part D: out-of-pocket cap $2,100; maximum deductible $615; national base premium $38.99.",
               "IRMAA surcharges begin above $109,000 (single) or $218,000 (joint) of 2024 modified adjusted gross income, and are a cliff: $1 over a threshold moves you to the whole next tier. A land sale, a year of Permian Basin royalties, a Los Alamos or Sandia retirement payout, or a Roth conversion two years ago is the usual surprise.",
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
<p>Most people pay $0 for Part A because they paid Medicare taxes while working. Part D, Medicare Advantage and Medigap premiums vary by plan and carrier; Medigap Plan G covers everything above except the Part B deductible. If your income is limited, New Mexico&rsquo;s <a href="/medicaid">Medicare Savings Programs</a> can pay the Part B premium, and New Mexico has no asset test for them.</p>
<h2>[[YEAR]] IRMAA: what higher earners pay</h2>
<p>If your income is above the thresholds below, you pay an income-related surcharge on top of your Part B and Part D premiums. Your [[YEAR]] IRMAA is based on the income (MAGI) from your <strong>2024</strong> tax return. IRMAA is a cliff: going $1 over a threshold moves you into the whole next tier. In New Mexico the usual surprises are a land or ranch sale, a strong year of oil-and-gas royalties in the Permian, a lump-sum retirement payout from the labs or the base, or a Roth conversion two years back.</p>
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
           ("Can I get help paying the Part B premium in New Mexico?", "Possibly. New Mexico&rsquo;s Medicare Savings Programs (QMB, SLMB and QI), run by the Health Care Authority, pay the Part B premium for people with limited income, and QMB also covers Medicare&rsquo;s deductibles and copays. New Mexico has no asset test for these programs, so only income counts. See our Turquoise Care and Medicare Savings Programs page.")],
     sources=[SRC_CMS, SRC_COSTS, SRC_HSD_MSP], cta="Not sure which costs apply to you? Let&rsquo;s look together.", about="Medicare costs and IRMAA"),
]
