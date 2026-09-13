"""Utah topic pages, part A: Advantage, Medigap, Part D, costs."""
SRC_CMS = ("CMS: 2026 Medicare Parts A &amp; B Premiums and Deductibles (Nov 14, 2025)", "https://www.cms.gov/newsroom/fact-sheets/2026-medicare-parts-b-premiums-and-deductibles")
SRC_COSTS = ("Medicare.gov: Medicare costs", "https://www.medicare.gov/basics/costs/medicare-costs")
SRC_MA_GOV = ("Medicare.gov: Medicare Advantage plans", "https://www.medicare.gov/health-drug-plans/health-plans")
SRC_MEDIGAP_GOV = ("Medicare.gov: Medigap (Medicare Supplement Insurance)", "https://www.medicare.gov/health-drug-plans/medigap")
SRC_PARTD_GOV = ("Medicare.gov: Drug coverage (Part D)", "https://www.medicare.gov/health-drug-plans/part-d")
SRC_UID = ("Utah Insurance Department: Medicare supplement (Medigap) information and plan comparison", "https://insurance.utah.gov/consumers/health/medicare-supplement")
SRC_DAAS = ("Utah Division of Aging and Adult Services: SHIP Medicare counseling (800-541-7735)", "https://daas.utah.gov")
SRC_SHIP_UT = ("SHIP National Technical Assistance Center: Utah", "https://www.shiphelp.org/ships/utah/")
SRC_KFF = ("KFF: Medicare Advantage 2026 Spotlight, a first look at plan offerings", "https://www.kff.org/medicare/medicare-advantage-2026-spotlight-a-first-look-at-plan-offerings/")
SRC_SELECT = ("Select Health: Medicare Advantage plans in Utah", "https://selecthealth.org/medicare/ma-plans-utah")
SRC_MMR_UT = ("MyMedigapRate: Utah Medigap rate history, filing by filing", "https://www.mymedigaprate.com/medigap-rate-history/utah")
SRC_UT_MEDICAID = ("Utah Medicaid (Department of Health and Human Services)", "https://medicaid.utah.gov")
SRC_DWS = ("Utah Department of Workforce Services: apply for Medicaid and Medicare Savings Programs (myCase)", "https://jobs.utah.gov/mycase")
SRC_TFL = ("TRICARE For Life", "https://www.tricare.mil/tfl")
SRC_VA = ("VA health care and other insurance", "https://www.va.gov/health-care/about-va-health-benefits/va-health-care-and-other-insurance/")

TOPICS_A = [
dict(slug="medicare-advantage", nav_title="Medicare Advantage plans in Utah", crumb="Medicare Advantage", scene="saltlake",
     title="Medicare Advantage Plans in Utah [[YEAR]] | ECOS Medicare Solutions",
     desc="Medicare Advantage in Utah: Select Health, the University of Utah and the other carriers, why the network question starts with your hospital system, $0 premiums, and what to check every October. Free help from a licensed Utah agent.",
     llm="Medicare Advantage (Part C) in Utah: Select Health and the other carriers, networks built on Intermountain or University of Utah Health, bundled benefits, what changes each year",
     eyebrow="Plans · Part C", h1="Medicare Advantage plans in Utah",
     sub="All-in-one plans, often with a $0 premium and extras like dental and vision &mdash; riding on a network that, in Utah, is usually built around one hospital system.",
     keyfacts=["A Medicare Advantage plan bundles Part A, Part B and usually Part D into one private plan with a network. You keep paying the Part B premium ([[YEAR]]: $202.90) plus any plan premium.",
               "Utah&rsquo;s Advantage market is anchored by Select Health, Intermountain&rsquo;s own insurer, alongside UnitedHealthcare, Humana, Aetna, Cigna, Devoted Health and Regence BlueCross BlueShield of Utah. Salt Lake and Utah counties typically have more than two dozen plans; rural counties a handful.",
               "The network question in Utah is a system question: Intermountain, University of Utah Health, MountainStar or Holy Cross. A plan built on one may exclude the others.",
               "Plans change every October 1, and a plan leaving your county opens a Special Enrollment Period and, usually, a guaranteed-issue right to Medigap."],
     body="""<p>A Medicare Advantage plan (also called Part C) is an all-in-one alternative to Original Medicare, offered by private insurers that Medicare approves and pays. You still have Medicare, but the plan administers your Part A and Part B coverage and almost always folds in Part D drug coverage too. In Utah the market is unusual in one way: the largest hospital system, Intermountain Health, owns the largest local insurer, Select Health, so a lot of Utahns&rsquo; Advantage plan and hospital are the same company.</p>
<h2>What&rsquo;s usually included</h2>
<ul>
<li><strong>Hospital and medical coverage</strong> (your Part A and Part B benefits).</li>
<li><strong>Prescription drug coverage</strong> in most plans &mdash; so you don&rsquo;t buy a separate <a href="/part-d">Part D plan</a>.</li>
<li><strong>Extras Original Medicare doesn&rsquo;t cover</strong>, which can include dental, vision, hearing, fitness benefits, and an annual out-of-pocket maximum that caps what you spend on covered care.</li>
</ul>
<h2>The trade-off: networks built on systems</h2>
<p>Advantage plans use provider networks (HMO or PPO) and are sold by county. In Utah the network almost always follows a hospital system. Select Health plans are built on Intermountain (Intermountain Medical Center, LDS, Utah Valley, McKay-Dee, St. George Regional and their clinics). University of Utah Health has its own hospital, Huntsman Cancer Institute and clinics, and contracts with carriers on its own terms. MountainStar (St. Mark&rsquo;s, Ogden Regional, Timpanogos, Lone Peak) and Holy Cross (Salt Lake, Jordan Valley, Davis) contract separately again. A $0-premium plan that covers your family doctor at an Intermountain clinic may not cover the specialist you were referred to at the U. We confirm your providers and prescriptions are covered before you sign anything.</p>
<div class="note-box"><p><strong>The referral question.</strong> Utah&rsquo;s most specialized care &mdash; Huntsman, the U&rsquo;s transplant and neurology programs, Primary Children&rsquo;s adult congenital clinic &mdash; sits inside University of Utah Health. If there is any chance you will need it, ask whether the plan you are considering covers the U in-network before you look at the premium. A <a href="/medicare-supplement">Medigap policy</a> removes the question entirely.</p></div>
<h2>What to check every October</h2>
<p>Carriers redraw their county maps and benefits every year and announce the next year&rsquo;s plans on October 1. Nationally, 2026 saw large carriers withdraw from hundreds of counties and raise premiums on plans that charge one; Utah&rsquo;s metro counties kept a deep menu, while some rural counties have only a handful of plans. If your plan leaves your county, the non-renewal notice opens a Special Enrollment Period and, for most people, a <strong>guaranteed-issue right</strong> to buy a Medigap policy without medical underwriting &mdash; time-limited, generally 63 days after coverage ends. Utah has no birthday rule to fall back on afterward.</p>
<h2>Who Medicare Advantage tends to suit</h2>
<p>People who want predictable, lower upfront costs and value bundled extras, whose doctors sit inside one system, and who stay mostly in Utah. If you winter in Mesquite or Mesa, see specialists in more than one system, or want to use any provider nationwide, compare it against a <a href="/medicare-supplement">Medigap policy</a> &mdash; our <a href="/snowbirds">snowbird guide</a> walks through the difference. Hill AFB retirees with TRICARE For Life have their own calculation; see <a href="/veterans">Veterans</a>.</p>
<p>There are also specialized Advantage plans for specific situations: <a href="/chronic-snp">Chronic Special Needs Plans (C-SNPs)</a>, <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a>, and Dual Special Needs Plans for people with both Medicare and <a href="/medicaid">Utah Medicaid</a>.</p>""",
     faqs=[("Does Medicare Advantage replace Original Medicare?", "Not exactly. You keep Medicare, but a private Advantage plan administers your benefits and adds extras. You generally use the plan&rsquo;s network and its rules instead of Original Medicare&rsquo;s."),
           ("Is there really a $0 premium?", "Many Advantage plans have a $0 monthly plan premium, but you still pay your Part B premium ($202.90 in [[YEAR]]), and you may have copays, coinsurance and a deductible. We show you the full picture, not just the premium."),
           ("Does a Select Health plan cover the University of Utah?", "Select Health plans are built on Intermountain; whether a given plan includes University of Utah Health providers varies by plan and year. If the U is your care, we confirm the plan&rsquo;s network in writing before you enroll, or steer you to a Medigap policy."),
           ("Can I switch later if it isn&rsquo;t a fit?", "Yes. You can change during the Annual Election Period (Oct 15&ndash;Dec 7), and the Medicare Advantage Open Enrollment Period (Jan 1&ndash;Mar 31) lets current Advantage members switch once or return to Original Medicare. Special circumstances, including moving counties, open other windows.")],
     sources=[SRC_MA_GOV, SRC_SELECT, SRC_KFF, SRC_UID, SRC_CMS], cta="Let&rsquo;s compare your Advantage options &mdash; and the alternatives.", about="Medicare Advantage in Utah"),

dict(slug="medicare-supplement", nav_title="Medicare Supplement (Medigap) plans in Utah", crumb="Medicare Supplement", scene="wasatch",
     title="Medicare Supplement Plans in Utah: Plan G, Plan N &amp; the Rules | ECOS Medicare Solutions",
     desc="Utah Medigap explained: the standardized plans, the six-month open enrollment that does not repeat, no birthday rule, the under-65 gap, guaranteed-issue after a plan exit, and comparing carriers on filed rate history.",
     llm="Medicare Supplement (Medigap) in Utah: standardized plans A-N, the six-month open enrollment, no birthday rule, no under-65 requirement, guaranteed-issue events, comparing carriers on rate history",
     eyebrow="Plans · Medigap", h1="Medicare Supplement (Medigap) plans in Utah",
     sub="A Medigap policy works alongside Original Medicare to pay much of what it leaves to you, and lets you use any provider in the country that accepts Medicare &mdash; Intermountain and the U alike, and the clinic in Mesquite.",
     keyfacts=["Utah uses the federal standardized plans, sold by letter (Plan G and Plan N are the most common for people new to Medicare; Plan F is closed to anyone eligible after 2019). The same letter offers the same benefits from every company, so the comparison is price and rate history.",
               "Your six-month Medigap open enrollment starts the month you are 65 or older and enrolled in Part B. During it, no insurer can turn you down or charge more for your health. Utah has no birthday rule and no annual window afterward.",
               "Utah does not require insurers to sell Medigap to people under 65 on Medicare; a small number of companies choose to, often at higher premiums. Everyone gets a full open enrollment at 65.",
               "Losing an Advantage plan or employer coverage through no fault of your own creates a guaranteed-issue right, generally 63 days long. The Utah Insurance Department publishes a plan comparison tool."],
     body="""<p>Medicare Supplement insurance &mdash; usually called Medigap &mdash; is private coverage that pairs with Original Medicare (Parts A and B). Instead of replacing Medicare, it fills the gaps: the deductibles, copayments and coinsurance you&rsquo;d otherwise pay yourself. You then add a standalone <a href="/part-d">Part D drug plan</a> for prescriptions. The Utah Insurance Department regulates the policies; the benefits inside each plan letter are set federally.</p>
<h2>How Medigap is different from Advantage</h2>
<table class="ctable">
<caption>A simplified comparison &mdash; the right choice depends on your health, doctors, county and budget.</caption>
<thead><tr><th scope="col">&nbsp;</th><th scope="col">Medicare Supplement (Medigap)</th><th scope="col">Medicare Advantage</th></tr></thead>
<tbody>
<tr><th scope="row">Provider access</th><td>Any provider in the U.S. that accepts Medicare &mdash; Intermountain, the U, MountainStar, Holy Cross, and out of state</td><td>Plan network, usually built on one system</td></tr>
<tr><th scope="row">Drug coverage</th><td>Add a separate Part D plan</td><td>Usually built in</td></tr>
<tr><th scope="row">Monthly premium</th><td>A monthly premium for the policy</td><td>Often $0 plan premium</td></tr>
<tr><th scope="row">Out-of-pocket</th><td>Very predictable; little to pay at the point of care on Plan G</td><td>Copays/coinsurance up to an annual cap</td></tr>
<tr><th scope="row">Extras (dental/vision)</th><td>Not included</td><td>Often included</td></tr>
<tr><th scope="row">Winters in Mesquite or Mesa</th><td>Covered anywhere in the U.S.</td><td>Emergencies only on most plans out of area</td></tr>
</tbody></table>
<h2>The plans Utahns actually buy</h2>
<p><strong>Plan G</strong> covers everything Original Medicare leaves behind except the Part B deductible ($283 in [[YEAR]]). <strong>Plan N</strong> costs less in exchange for small office and emergency copays and no coverage of Part B excess charges. <strong>High-deductible Plan G</strong> has a much lower premium and a deductible you pay first. <strong>Plan F</strong> still exists for people who were eligible before 2020 but cannot be sold to anyone newer. Because benefits are standardized, we compare companies on price and on how fast they have raised it.</p>
<h2>When you can buy one without health questions</h2>
<ul>
<li><strong>Your six-month open enrollment.</strong> It starts the month you are 65 or older <em>and</em> enrolled in Part B. During it, every plan a company sells is guaranteed available regardless of health. In Utah this is the window: there is no birthday rule, anniversary rule or annual Medigap window afterward.</li>
<li><strong>Guaranteed-issue events.</strong> Losing an Advantage plan or employer coverage through no fault of your own gives you a window (generally 63 days) to buy certain plans without underwriting.</li>
<li><strong>Under 65 on disability.</strong> Utah does not require insurers to offer Medigap before 65. A few companies do, usually at higher premiums; the Utah Insurance Department&rsquo;s comparison tool lists them. Everyone gets a fresh open enrollment for every plan at 65.</li>
<li><strong>Outside those windows,</strong> Utah insurers can use medical underwriting. Switching later usually means answering health questions.</li>
</ul>
<div class="note-box"><p><strong>Timing matters more in Utah than in states with a birthday rule.</strong> A condition that would be irrelevant at 65 can mean a decline at 72, and there is no annual second chance here. If you are approaching 65, or your Advantage plan just sent a non-renewal notice, talk to us before the window closes.</p></div>
<h2>Compare the rate history, not just the first-year price</h2>
<p>Because the benefits are standardized, the only real differences between Utah Medigap companies are what they charge and how steeply they raise it later. That second part is public: every carrier files its rate increases with the Utah Insurance Department, and a policy that looks cheap at 65 can be the expensive one by 75. We publish that filing history on our research site, <a href="https://www.mymedigaprate.com/medigap-rate-history/utah">Utah Medigap rate history</a>, with each figure tied to the filing it came from. If your premium has already gone up and you want to know why, <a href="https://www.mymedigaprate.com/why-did-my-medigap-premium-increase">why Medigap premiums increase</a> covers the three causes.</p>
<h2>Who Medigap tends to suit</h2>
<p>People who want maximum freedom to choose doctors and hospitals &mdash; Intermountain and the U in the same year, a specialist in Salt Lake from Vernal or Moab &mdash; predictable costs, and coverage that travels. That last point is why so many Utah <a href="/snowbirds">snowbirds</a> keep a supplement. The cost is a monthly premium that rises with age and with the carrier&rsquo;s filings.</p>""",
     faqs=[("Do I need a separate drug plan with Medigap?", "Yes. Medigap does not include prescription coverage, so most people add a standalone Part D plan. We help you pick one around your specific medications."),
           ("Can I be turned down for Medigap in Utah?", "Not during your six-month open enrollment, and not during a guaranteed-issue event such as your Advantage plan leaving your county. Outside those windows, Utah insurers can use medical underwriting, and Utah has no birthday rule or annual switching window."),
           ("Is Plan F still available in Utah?", "Only to people who became eligible for Medicare before January 1, 2020. Everyone newer chooses from Plans G, N, high-deductible G and the others. We walk through which fits you."),
           ("I am under 65 on disability. Can I buy Medigap in Utah?", "Utah does not require it, so most companies do not sell Medigap before 65, and the few that do often charge more. The Utah Insurance Department&rsquo;s comparison tool lists them. You get a fresh open enrollment for every plan at 65."),
           ("How much does a Utah Medigap policy cost?", "It depends on the plan letter, your age, ZIP code, tobacco use and the carrier, and every carrier raises rates on its own schedule. We compare current premiums and each company&rsquo;s filed rate history with you; we do not publish a number here without the filing behind it.")],
     sources=[SRC_MEDIGAP_GOV, SRC_UID, SRC_MMR_UT, SRC_DAAS, SRC_CMS], cta="Let&rsquo;s see whether Plan G, Plan N or something else fits you.", about="Medicare supplement insurance in Utah"),

dict(slug="part-d", nav_title="Medicare Part D plans in Utah", crumb="Part D", scene="utahvalley",
     title="Medicare Part D Plans in Utah [[YEAR]] | ECOS Medicare Solutions",
     desc="Part D drug plans in Utah: the [[YEAR]] $2,100 cap, $615 maximum deductible, choosing by your medications and pharmacy (Smith's, Harmons, Walgreens, Intermountain pharmacies), the late penalty, and Extra Help.",
     llm="Part D drug plans in Utah: 2026 $2,100 cap, choosing by your medications and pharmacy, penalties, Extra Help through Utah's Medicare Savings Programs",
     eyebrow="Plans · Part D", h1="Medicare Part D drug plans in Utah",
     sub="Standalone prescription coverage chosen around your medications and your pharmacy &mdash; whether you pair it with Original Medicare, a Medigap policy, or nothing else.",
     keyfacts=["[[YEAR]] Part D out-of-pocket cap: $2,100. Once your spending on covered drugs reaches it, you pay $0 for covered medications the rest of the year.",
               "[[YEAR]] maximum Part D deductible: $615; many plans set a lower one or none. The national base premium used for penalties is $38.99.",
               "Going 63 or more days without creditable drug coverage after you are first eligible adds a permanent penalty to your premium. TRICARE For Life and VA pharmacy are creditable.",
               "Qualifying for a Utah Medicare Savings Program or Medicaid automatically qualifies you for Extra Help, which cuts Part D premiums and copays substantially."],
     body="""<p>Medicare Part D covers prescription drugs through private plans approved by Medicare. You can get it as a standalone plan alongside Original Medicare (and usually a <a href="/medicare-supplement">Medigap policy</a>), or built into most <a href="/medicare-advantage">Medicare Advantage</a> plans.</p>
<h2>What changed for [[YEAR]]</h2>
<ul>
<li><strong>$2,100 out-of-pocket cap.</strong> Once your spending on covered drugs reaches $2,100 in [[YEAR]], you pay $0 for covered medications the rest of the year.</li>
<li><strong>Deductible up to $615.</strong> That is the most a plan can charge as its [[YEAR]] deductible; many plans set a lower one or none at all.</li>
<li><strong>Premiums vary by plan.</strong> The [[YEAR]] national base beneficiary premium &mdash; the figure used to calculate penalties &mdash; is $38.99, but what you actually pay depends on the plan you choose.</li>
<li><strong>The Medicare Prescription Payment Plan</strong> lets you spread out-of-pocket drug costs across the year in monthly instalments instead of paying at the counter. It changes when you pay, not how much.</li>
</ul>
<h2>Choosing a plan is about your drug list and your pharmacy</h2>
<p>Every Part D plan has a formulary &mdash; its list of covered drugs and the tier (and cost) for each &mdash; and a pharmacy network with preferred pharmacies that cost less. Two plans with similar premiums can cost very different amounts once your specific prescriptions are run through them, and a plan that is cheap at Smith&rsquo;s in Sandy may be expensive at the one pharmacy in Moab. Intermountain&rsquo;s own pharmacies are preferred in some plans and not others. We compare plans using your actual medication list and your pharmacy, so the lowest <em>total</em> cost wins, not just the lowest premium.</p>
<div class="note-box"><p><strong>Watch the late-enrollment penalty.</strong> If you go 63 or more days without Part D or other creditable drug coverage after you are first eligible, a permanent penalty can be added to your premium for as long as you have Part D. Employer coverage, the VA pharmacy and TRICARE For Life are all creditable; keep proof. See our <a href="/medicare-costs">[[YEAR]] costs page</a> to estimate a penalty.</p></div>
<h2>Higher earners and lower incomes</h2>
<p>If your income is above the [[YEAR]] thresholds ($109,000 single / $218,000 joint, based on your 2024 tax return), you pay a Part D income-related surcharge (IRMAA) on top of your plan premium; our <a href="/medicare-costs">costs &amp; IRMAA page</a> lays out the brackets. At the other end, <strong>Extra Help</strong> (the Low-Income Subsidy) cuts Part D premiums and copays substantially for people with limited income and resources. In Utah, qualifying for a Medicare Savings Program (QMB, SLMB or QI) qualifies you for Extra Help automatically. See <a href="/medicaid">Utah Medicaid and the Medicare Savings Programs</a>.</p>""",
     faqs=[("When should I enroll in Part D?", "Usually when you first become eligible for Medicare, even if you take few or no medications &mdash; that avoids the late-enrollment penalty. Exceptions apply if you have other creditable drug coverage such as an employer plan, TRICARE For Life or VA pharmacy benefits."),
           ("What is the [[YEAR]] Part D out-of-pocket cap?", "$2,100. After your covered-drug spending reaches that amount in [[YEAR]], you pay nothing more for covered medications for the rest of the year."),
           ("Does my pharmacy matter?", "Yes. Each plan has preferred pharmacies where copays are lowest. Smith&rsquo;s, Harmons, Walgreens, Walmart, Intermountain pharmacies and independents are preferred in different plans; we check yours when we compare."),
           ("Can you help me pick a plan around my medications?", "Yes &mdash; that is the most useful thing we do here. Bring your medication list and pharmacy, and we compare plans on your total expected yearly cost.")],
     sources=[SRC_PARTD_GOV, SRC_CMS, SRC_COSTS, SRC_DWS], cta="Let&rsquo;s match a drug plan to your prescriptions.", about="Medicare Part D in Utah"),
]
