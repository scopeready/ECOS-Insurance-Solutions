"""Indiana topic pages, part A: Advantage, Medigap, Part D, costs."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_SHIP_IN = ("Indiana SHIP (State Health Insurance Assistance Program), Indiana Department of Insurance, 800-452-4800", "https://www.in.gov/ship/")
SRC_SHIP_NAT = ("SHIP National Technical Assistance Center: Indiana", "https://www.shiphelp.org/ships/indiana/")
SRC_SHIP_MEDIGAP = ("Indiana SHIP: Medicare Supplement plans", "https://www.in.gov/ship/medicare-supplement-plans")
SRC_IDOI = ("Indiana Department of Insurance", "https://www.in.gov/idoi/")
SRC_IDOI_LOOKUP = ("Indiana insurance licence lookup (Sircon, on behalf of the Indiana Department of Insurance)", "https://www.sircon.com/ComplianceExpress/Inquiry/consumerInquiry.do?nonSscrb=Y")
SRC_HEA1226 = ("Indiana Department of Insurance: HEA 1226 fact sheet (Medicare supplement birthday rule)", "https://www.in.gov/idoi/files/HEA-1226-Fact-Sheet.docx")
SRC_ASKSHIP = ("Indiana SHIP: AskSHIP, December 2025 (the birthday rule explained)", "https://www.in.gov/ship/files/AskSHIP-12-25.pdf")
SRC_SEA215 = ("Indiana SHIP: Medicare Supplement guaranteed issue for people under 65 (SEA 215)", "https://www.in.gov/ship/files/SEA215_release1.pdf")
SRC_IC_9_1 = ("Indiana Code 27-8-13-9.1: Medicare supplement policies for individuals with disabilities and end stage renal disease", "https://law.justia.com/codes/indiana/title-27/article-8/chapter-13/section-27-8-13-9-1/")
SRC_MMR_IN = ("MyMedigapRate: Indiana Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/indiana")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_HCD = ("Healthcare Dive: UnitedHealthcare, Humana, Aetna scale back Medicare Advantage plans for 2026", "https://www.healthcaredive.com/news/medicare-advantage-plans-2026-unitedhealthcare-humana-aetna/801761/")
SRC_HCD_2027 = ("Healthcare Dive: Humana to exit more Medicare Advantage plans in 2027", "https://www.healthcaredive.com/news/humana-2027-medicare-advantage-plan-exits-q2-2026/826441/")
SRC_IUHP = ("IU Health Plans: Medicare Advantage enrollment after the Elevance Health acquisition (January 1, 2025)", "https://www.iuhealthplans.org/medicare-advantage-plans/shopping-for-medicare-advantage-plans/iu-health-plans-medicare-advantage-enrollment")
SRC_HIO_IN = ("healthinsurance.org: Medicare in Indiana (enrollment figures)", "https://www.healthinsurance.org/medicare/indiana/")
SRC_FSSA_APPLY = ("Indiana Medicaid (FSSA): apply and check status &mdash; Medicaid and the Medicare Savings Programs", "https://www.in.gov/medicaid/apply-and-check-status/")
SRC_FSSA_ABD = ("Indiana Medicaid: Aged, Blind and Disabled programs", "https://www.in.gov/medicaid/members/aged-blind-and-disabled/")
SRC_PATHWAYS = ("FSSA: Indiana PathWays for Aging launch (July 1, 2024)", "https://www.in.gov/fssa/files/FSSA-announces-launch-of-Indiana-PathWays.pdf")
SRC_HOOSIERRX = ("Indiana Medicaid: HoosierRx &mdash; help paying your Medicare Part D premium", "https://www.in.gov/medicaid/members/files/HRx_Flyer.pdf")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in Indiana", crumb="Medicare Advantage", scene="monument",
     title="Medicare Advantage Plans in Indiana [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in Indiana: hospital-system networks, $0 premiums, the IU Health Plans move to Anthem, the 2026 carrier pullbacks, and what a non-renewal notice gives you. Free help from a licensed Indiana agent.",
     llm="Medicare Advantage (Part C) in Indiana: how hospital-system networks and bundled benefits work, the IU Health Plans transition to Anthem for 2026, the national 2026 carrier exits, and what a non-renewal notice gives you",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in Indiana",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a network that is drawn around Indiana&rsquo;s big hospital systems, in a year when several plans changed hands.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "Roughly half of Indiana&rsquo;s Medicare beneficiaries are in Advantage plans. Marion, Lake, Allen, Hamilton and Vanderburgh counties have the deepest menus; many rural counties have a handful of plans.",
               "IU Health Plans, the Advantage plan built on the IU Health system, was acquired by Elevance Health (Anthem&rsquo;s parent) on January 1, 2025, and its members were moved to Anthem plans for 2026. Nationally, UnitedHealthcare and Humana withdrew from hundreds of counties for 2026, and Humana has announced more exits for 2027.",
               "A plan leaving your county gives you a Special Enrollment Period and, in most cases, a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. In Indiana the largest carriers are Anthem Blue Cross and Blue Shield, Humana, UnitedHealthcare, Aetna and Wellcare, and which of them sells in <em>your</em> county &mdash; and which hospitals sit in the network &mdash; changes every year.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks drawn around hospital systems</h2>
<p>Advantage plans use provider networks (HMO or PPO) and are sold by county. That is the single most important thing to check before you enroll: whether your doctors and your hospital are in the plan&rsquo;s network, and whether your medications are on its drug list. Indiana&rsquo;s care is organized into a few large systems that each sign their own contracts &mdash; IU Health, Ascension St. Vincent, Community Health Network, Franciscan Health and Eskenazi in and around Indianapolis; Parkview Health and Lutheran Health Network in Fort Wayne; Deaconess and Ascension St. Vincent in Evansville; Beacon Health System and Saint Joseph Health System in South Bend and Elkhart; Methodist Hospitals, Community Healthcare System and Franciscan in the Region. A $0-premium plan that includes one may exclude the one across town. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="warn-box"><p><strong>What changed for 2026, and why it matters this fall.</strong> IU Health Plans, the Advantage plan many central and southern Hoosiers chose because it was built on IU Health, was acquired by Elevance Health on January 1, 2025, and its Medicare Advantage members received Anthem plan information for 2026. Health Alliance, the Carle-owned plan sold in parts of Indiana, closed at the end of 2025. And nationally UnitedHealthcare left 225 counties and Humana 198 for the 2026 plan year, with Humana announcing further reductions for 2027. If you were moved into a new plan, or picked one in a hurry last fall, the Annual Election Period starting October 15 is the time to check it actually fits.</p></div>
<h2>If your plan left your county</h2>
<p>A non-renewal notice is not just bad news; it opens doors. You get a Special Enrollment Period that runs past the normal deadlines, and because the plan left you involuntarily, federal rules give most people a <strong>guaranteed-issue right</strong> to buy a <a href="/medicare-supplement">Medigap policy</a> without medical underwriting &mdash; even if you are well past your original six-month Medigap window. The right is time-limited (generally 63 days after your coverage ends), so do not let the notice sit. Indiana&rsquo;s new birthday rule does not help here: it lets existing Medigap policyholders switch, not Advantage members buy in.</p>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, who are comfortable using a plan network, and who live where the menu is deep. If you winter in Florida, see a specialist in Louisville, Cincinnati or Chicago, or want to use any provider nationwide, compare it against a <a href="/medicare-supplement">Medigap policy</a> &mdash; our <a href="/snowbirds">snowbirds and border-care guide</a> walks through the difference. Military retirees with TRICARE For Life have their own calculation; see <a href="/veterans">Veterans</a>.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans for people with both Medicare and <a href="/medicaid">Indiana Medicaid</a>, which can be aligned with the PathWays for Aging plan on the Medicaid side.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("I was on IU Health Plans. What happened to my plan?", "IU Health Plans was acquired by Elevance Health, Anthem&rsquo;s parent company, on January 1, 2025. Coverage did not change for 2025, and for 2026 members received Anthem plan information. If you were moved, check that your IU Health doctors, your other providers and your prescriptions are in the new plan; the Annual Election Period is the time to change it if not."),
           ("My Indiana Advantage plan left my county. Can I get a Medigap policy now?", "In most cases, yes. Losing your plan through no fault of your own gives you a guaranteed-issue right to buy a Medigap policy without health questions, generally within 63 days of the coverage ending, plus a Special Enrollment Period to pick a new Advantage or Part D plan. Call before the deadline on your notice."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Special circumstances, including moving counties, open other windows.")],
     sources=[SRC_MA_GOV, SRC_IUHP, SRC_KFF, SRC_HCD, SRC_HCD_2027, SRC_HIO_IN, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in Indiana"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in Indiana, including the birthday rule", crumb="Medicare Supplement", scene="coveredbridge",
     title="Medicare Supplement Plans in Indiana: Plan G, Plan N &amp; the Birthday Rule | ECOS Medicare Solutions",
     desc="Indiana Medigap explained: the standardized plans, the six-month open enrollment, the new Indiana birthday rule for switching carriers, under-65 rights since 2025, guaranteed issue after a plan exit, and how to compare carriers on filed rate history.",
     llm="Medicare Supplement (Medigap) in Indiana: standardized plans A-N, the six-month open enrollment, the Indiana Medigap birthday rule (HEA 1226 / HEA 1260, 2026), under-65 guaranteed issue (SEA 215, 2025), guaranteed-issue events, comparing carriers on filed rate history",
     eyebrow="Plans · Medigap", h1="Medicare Supplement (Medigap) plans in Indiana",
     sub="A Medigap policy works alongside Original Medicare to pay much of what it leaves to you, and lets you use any provider in the country that accepts Medicare &mdash; IU Health, a Louisville or Chicago specialist, or the clinic in your county seat. And since 2026, Indiana lets you shop it every year.",
     keyfacts=["Indiana uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company, so the comparison is price and rate history.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. During it, no insurer can turn you down or charge more for your health.",
               "<strong>Indiana&rsquo;s birthday rule (new for 2026).</strong> If you are 65 or older and already have a Medigap policy, you can apply to a different insurer for the same plan letter without medical underwriting in a window that opens 31 days before your birthday and closes 31 days after it. The new policy starts the first of the month after you apply. Enacted as HEA 1226 (2025) and amended by HEA 1260 for policies issued or renewed on or after March 15, 2026.",
               "<strong>Under 65?</strong> Since January 1, 2025 (SEA 215), Hoosiers on Medicare because of a disability or ESRD get their own six-month open enrollment when Part B starts; insurers must offer them coverage, and the law limits what they can be charged for Plans A, B and D.",
               "Losing an Advantage plan or employer coverage through no fault of your own creates a guaranteed-issue right, generally 63 days long."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. The Indiana Department of Insurance regulates the policies; the benefits inside each plan letter are set federally.</p>
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
<tr><th scope="row">Winters in Florida, care in Louisville or Chicago</th><td>Covered anywhere in the U.S.</td><td>Emergencies only on most plans out of area</td></tr>
<tr><th scope="row">Switching later</th><td>Indiana&rsquo;s birthday rule: same plan letter, any insurer, no health questions, every year</td><td>Annual Election Period and MA Open Enrollment</td></tr>
</tbody></table>
<h2>The plans Hoosiers actually buy</h2>
<p><strong>Plan G</strong> covers everything Original Medicare leaves behind except the Part B deductible ($283 in [[YEAR]]). <strong>Plan N</strong> costs less in exchange for small office and emergency copays and no coverage of Part B excess charges. <strong>High-deductible Plan G</strong> has a much lower premium and a deductible you pay first. <strong>Plan F</strong> still exists for people who were eligible before 2020 but cannot be sold to anyone newer. Because benefits are standardized, we compare companies on price and on how fast they have raised it.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, every plan a company sells is guaranteed available regardless of health.</li>
<li><strong>The Indiana birthday rule, every year after that.</strong> If you are 65 or older and already hold a Medigap policy, each year you can apply to another insurer for the same plan letter (including its variations, such as high-deductible G) without underwriting. The window opens 31 days before your birthday and closes 31 days after it, and the new policy takes effect the first day of the month after you sign the application. The rule came in as HEA 1226 of 2025 and was amended by HEA 1260 of 2026, which applies to policies delivered, issued or renewed on or after March 15, 2026. It is a switching rule, not a first-purchase rule: you need to be in a Medigap policy already.</li>
<li><strong>Under 65 on disability or ESRD.</strong> Since January 1, 2025, Indiana Code 27-8-13-9.1 (SEA 215) gives people under 65 who are enrolled in Medicare their own six-month guaranteed-issue window when Part B begins, requires insurers that sell Medigap at 65 to offer it to them, and limits what they can be charged for Plans A, B and D. A second open enrollment for every plan still arrives at 65.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage plan or employer coverage through no fault of your own gives you a window (generally 63 days) to buy certain plans without underwriting.</li>
<li><strong>Outside those windows,</strong> Indiana insurers can use medical underwriting. Moving from Advantage to Medigap after the first year, for example, usually means answering health questions.</li>
</ul>
<div class="note-box"><p><strong>Timing matters.</strong> A condition that would be irrelevant at 65 can mean a decline at 72 if you are trying to leave Advantage for Medigap. If you already have a Medigap policy, put your birthday on the calendar: the window is about two months wide and it closes. If you are approaching 65, talk to us before the open enrollment ends. The exact wording of the birthday rule is in the Indiana Department of Insurance fact sheet and Indiana SHIP&rsquo;s December 2025 AskSHIP bulletin, both linked below.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between Indiana Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate increases with the Indiana Department of Insurance, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/indiana">Indiana Medigap rate history</a>, with each figure tied to the filing it came from. If your premium has already gone up and you want to know why, <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes &mdash; and with the birthday rule, the answer in Indiana is now &ldquo;shop it in your window,&rdquo; not &ldquo;live with it.&rdquo;</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; IU Health and Ascension St. Vincent without a network question, a specialist across the river in Louisville or up the road in Chicago &mdash; predictable costs, and coverage that travels. That last point is why so many <a href="/snowbirds">Hoosier snowbirds</a> keep a supplement. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings, which the birthday rule now lets you answer.</p>""",
     faqs=[("What is the Indiana Medigap birthday rule?", "An annual switching window for people 65 and older who already have a Medigap policy. Beginning 31 days before your birthday and ending 31 days after it, you can apply to a different insurer for the same plan letter without medical underwriting, and the new policy starts the first of the following month. It was enacted as HEA 1226 (2025) and amended by HEA 1260 for policies issued or renewed on or after March 15, 2026. It does not let an Advantage member buy Medigap without underwriting; that takes open enrollment or a guaranteed-issue event."),
           ("Can I move from Plan G to Plan N with the birthday rule?", "The rule is written around the same plan letter, including variations of that letter. If you want a different letter, that is a separate application that the insurer can underwrite. We check the current wording with the Department of Insurance fact sheet before you apply, because the 2026 amendment changed details."),
           ("Do I need a separate drug plan with Medigap?", "Yes. Medigap does not include prescription coverage, so most people add a standalone Part D plan. We help you pick one around your specific medications."),
           ("Can I be turned down for Medigap in Indiana?", "Not during your six-month open enrollment, not during your birthday-rule window (same plan letter, existing policyholders 65+), and not during a guaranteed-issue event such as your Advantage plan leaving your county. Outside those windows, Indiana insurers can use medical underwriting."),
           ("I am under 65 on disability. Can I buy Medigap in Indiana?", "Yes. Since January 1, 2025, Indiana law gives people under 65 on Medicare their own six-month guaranteed-issue window when Part B begins, requires insurers to offer them coverage, and limits what they can be charged for Plans A, B and D. You get a fresh open enrollment for every plan at 65."),
           ("How much does an Indiana Medigap policy cost?", "It depends on the plan letter, your age, ZIP code, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MEDIGAP_GOV, SRC_HEA1226, SRC_ASKSHIP, SRC_SEA215, SRC_IC_9_1, SRC_SHIP_MEDIGAP, SRC_IDOI, SRC_MMR_IN, SRC_CMS], cta="Let&rsquo;s see whether Plan G, Plan N or something else fits you &mdash; or whether your birthday window is the moment to switch.", about="Medicare supplement insurance in Indiana"),

dict(slug="part-d", nav_title="Medicare Part D plans in Indiana", crumb="Part D", scene="farm",
     title="Medicare Part D Plans in Indiana [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in Indiana: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications and pharmacy (Kroger, Meijer, CVS, Walgreens, independents), the late penalty, Extra Help and HoosierRx.",
     llm="Part D drug plans in Indiana: 2026 $2,100 cap, choosing by your medications and pharmacy, penalties, Extra Help through Indiana Medicare Savings Programs, and HoosierRx premium help",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in Indiana",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Medigap policy, or nothing else.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life and VA pharmacy are creditable.",
               "Qualifying for an Indiana Medicare Savings Program or Medicaid automatically qualifies you for Extra Help. Separately, HoosierRx, Indiana&rsquo;s state pharmaceutical assistance program, pays up to $70 a month toward a Part D premium for eligible Hoosiers 65 and older."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list and your pharmacy</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at the Kroger or Meijer in Carmel may be expensive at the independent pharmacy in Rockville. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, most union retiree plans, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources. In Indiana, qualifying for a Medicare Savings Program (QMB, SLMB or QI) through FSSA&rsquo;s Division of Family Resources qualifies you for Extra Help automatically. Indiana also runs its own program, <strong>HoosierRx</strong>, which pays up to $70 a month toward a Part D plan premium for Hoosiers 65 and older with limited income. See <a href="/medicaid">Indiana Medicaid, PathWays for Aging and the Medicare Savings Programs</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer or union retiree plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("What is HoosierRx?", "Indiana&rsquo;s state pharmaceutical assistance program. It pays up to $70 a month toward your Medicare Part D plan premium if you are 65 or older, an Indiana resident, and under its income limits. It is run through Indiana Medicaid; Indiana SHIP (800-452-4800) can help you apply."),
           ("Does my pharmacy matter?", "Yes. Each plan has preferred pharmacies where copays are lowest. Kroger, Meijer, CVS, Walgreens, Walmart and independents are preferred in different plans; we check yours when we compare."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_COSTS, SRC_HOOSIERRX, SRC_FSSA_APPLY], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in Indiana"),

dict(slug="medicare-costs", nav_title="[[YEAR]] Medicare costs, full IRMAA chart, and penalty/IRMAA calculators", crumb="[[YEAR]] Costs", scene="quarry",
     title="[[YEAR]] Medicare Costs &amp; IRMAA in Indiana | ECOS Medicare Solutions",
     desc="[[YEAR]] Medicare costs for Indiana: Part A/B/D premiums and deductibles, the full IRMAA income chart, and free calculators for IRMAA and late-enrollment penalties.",
     llm="2026 Medicare costs: Part A/B/D premiums and deductibles, the full IRMAA chart, and calculators for IRMAA and the Part B / Part D late penalties",
     eyebrow="Costs · Verified [[YEAR]] figures", h1="[[YEAR]] Medicare costs and IRMAA, with calculators",
     sub="Every dollar figure on this page comes from the CMS release for [[YEAR]]. The calculators are estimates for planning; Social Security and Medicare set your official amounts.",
     keyfacts=["[[YEAR]] Part B standard premium $202.90/month; Part B deductible $283; Part A hospital deductible $1,736 per benefit period.",
               "[[YEAR]] Part D: out-of-pocket cap $2,100; maximum deductible $615; national base premium $38.99.",
               "IRMAA surcharges begin above $109,000 (single) or $218,000 (joint) of 2024 modified adjusted gross income, and are a cliff: $1 over a threshold moves you to the whole next tier. A farmland sale, a lump-sum pension payout or a Roth conversion two years ago is the usual surprise.",
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
<p>If your income is above the thresholds below, you pay an income-related surcharge on top of your Part B and Part D premiums. Your [[YEAR]] IRMAA is based on the income (MAGI) from your <strong>2024</strong> tax return. IRMAA is a cliff: going $1 over a threshold moves you into the whole next tier. In Indiana the usual surprises are the sale of farmland or a family business, a lump-sum pension payout, or a Roth conversion two years back.</p>
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
           ("Can I get help paying the Part B premium in Indiana?", "Possibly. Indiana&rsquo;s Medicare Savings Programs (QMB, SLMB and QI), handled by FSSA&rsquo;s Division of Family Resources, pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through the FSSA Benefits Portal or 800-403-0864; see our Indiana Medicaid page.")],
     sources=[SRC_CMS, SRC_COSTS, SRC_FSSA_APPLY], cta="Not sure which costs apply to you? Let&rsquo;s look together.", about="Medicare costs and IRMAA"),
]
