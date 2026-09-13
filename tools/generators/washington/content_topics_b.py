"""Washington topic pages, part B: turning 65, the Medigap switching rule (this state's situational page), veterans, Apple Health, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_OIC, SRC_SHIBA, SRC_SHIBA_LOCAL, SRC_HIO_WA, SRC_MMR_WA, SRC_MMR_SWITCH,
                              SRC_HCA_APPLY, SRC_HCA_STD, SRC_TFL, SRC_VA, SRC_UW_2026)
SRC_MMR_T65 = ("MyMedigapRate: turning 65 in Washington", "https://www.mymedigaprate.com/turning-65/washington")
SRC_MMR_WHY = ("MyMedigapRate: why did my Medigap premium increase?", "https://www.mymedigaprate.com/why-did-my-medigap-premium-increase")
SRC_VA_SPOKANE = ("VA Spokane Health Care (Mann-Grandstaff VA Medical Center)", "https://www.va.gov/spokane-health-care/")
SRC_VA_WA = ("VA facilities in Washington State", "https://www.va.gov/directory/guide/fac_list_by_state.cfm?State=WA&dnum=All")
SRC_WDVA = ("Washington State Department of Veterans Affairs: federal VA benefits", "https://dva.wa.gov/resources/federal-va-benefits")
SRC_JBLM = ("Joint Base Lewis-McChord (Army garrison home page)", "https://home.army.mil/lewis-mcchord/")
SRC_KITSAP = ("Naval Base Kitsap (Navy Life Pacific Northwest)", "https://kitsap.navylifepnw.com/")
SRC_REPI = ("Department of Defense REPI: Washington installation facts", "https://www.repi.mil/Portals/44/Documents/State_Packages/Washington_ALLFacts.pdf")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in Washington State guide", crumb="Turning 65", scene="ferry",
     title="Turning 65 in Washington State: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Washington State: your 7-month enrollment window, the Medigap open enrollment, the state's year-round switching rule, still-working rules for Boeing, Microsoft, Amazon and PEBB, the deadlines with lifelong penalties, and a checklist.",
     llm="Turning 65 in Washington State: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap by county and hospital system, the year-round Medigap switching rule, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Washington State: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Washington, where the right answer in Bellevue is not always the right answer in Okanogan County.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In Washington it matters less for <em>switching</em> (existing policyholders can change plans any time) and more for <em>getting in</em>: outside a guaranteed window, insurers can ask health questions.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later. State and school retirees on PEBB have their own Medicare rules.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Washington twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
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
<caption>The two ways most Washingtonians put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums; in Washington, the freedom to change Medigap plans any time.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly.</td></tr>
</tbody></table>
<p>Where you live, and which system your doctors belong to, tilts the answer. In King, Pierce, Snohomish, Spokane and Clark counties the Advantage menu is deep, and the question is whether UW Medicine, Providence Swedish, MultiCare, Virginia Mason Franciscan or Kaiser Permanente Washington is inside the plan you like. East of the Cascades, on the Olympic Peninsula and along the coast, the menu is short and the nearest specialist may be a long drive, and a Medigap policy&rsquo;s any-provider access is often the practical choice. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, the second deadline is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above. Washington&rsquo;s <a href="/medigap-switching">year-round switching rule</a> means you will never be trapped in the wrong Medigap plan once you have one &mdash; but getting in without health questions still depends on using this window or a guaranteed-issue event. Our research site sets the two windows side by side: <a href="https://www.mymedigaprate.com/turning-65/washington">turning 65 in Washington</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no Washington insurer can turn you down or charge more for your health. Afterward, insurers can use medical underwriting for anyone <em>entering</em> Medigap outside a guaranteed-issue event; existing policyholders can still switch freely.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Washington&rsquo;s big employers &mdash; Boeing, Microsoft, Amazon, the state and its universities, the school districts, the health systems, the ports and the utilities &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll. State, school and higher-education retirees with PEBB coverage have their own Medicare enrollment rules; ask us before you assume the employer rules apply.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find out how deep the Advantage menu is in your county, and which hospital systems each plan includes for [[YEAR]].</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if UW Medicine, Fred Hutch or a specific system is your care.</li>
<li>If you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Apple Health, see the <a href="/medicaid">Medicare Savings Programs</a>; if you already hold a Medigap policy, read the <a href="/medigap-switching">switching rule</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Washingtonians sort through it every day &mdash; clearly, patiently, and at no cost to you. Washington SHIBA (800-562-6900), the Office of the Insurance Commissioner&rsquo;s volunteer counseling program, offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Washington?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget and county. The Advantage menu is deep in the Puget Sound counties, Spokane and Clark County and thin in much of rural Washington. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in Washington?", "Two things. Your county and your hospital system decide how much Medicare Advantage choice you really have, and the gap between Seattle and a rural county is wide. And once you hold a Medigap policy, Washington law lets you change it any time without health questions, so the Medigap decision at 65 is about getting in, not about being locked in.")],
     sources=[SRC_CMS, SRC_SHIBA, SRC_HIO_WA, SRC_MMR_T65], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Washington State"),

dict(slug="medigap-switching", nav_title="Washington's year-round Medigap switching rule", crumb="Switching Medigap", scene="sanjuans",
     title="Switching Medigap Plans Any Time in Washington State | ECOS Medicare Solutions",
     desc="Washington law lets existing Medigap policyholders change plans or carriers at any time of year without medical underwriting. What the rule does, the Plan A exception, why it does not cover leaving Medicare Advantage, and how to use it when your premium goes up.",
     llm="Washington's year-round Medigap switching rule: existing Medigap policyholders can change plans or carriers any time without underwriting; Plan A holders limited to Plan A; does not apply to a move from Medicare Advantage; how to use it after a rate increase",
     eyebrow="Your situation · Already have Medigap", h1="Washington&rsquo;s year-round Medigap switching rule, explained",
     sub="Most of the country gets one six-month window to buy a Medigap policy without health questions and is then stuck. Washington is different: once you hold a Medigap policy you can change it &mdash; plan letter or company &mdash; any time, with one exception. Here is exactly what that means.",
     keyfacts=["If you already have a Medigap policy, Washington law lets you switch to another Medigap plan, from the same insurer or a different one, at any time of year, and the insurer cannot use medical underwriting to refuse you or charge you more for your health.",
               "The one exception is Plan A: a Plan A holder can move only to another Plan A. Holders of Plans B through N can move to any of B through N (subject to the federal rule that Plans C and F are sold only to people eligible before 2020).",
               "The rule is for people who already hold a Medigap policy. It does not let a Medicare Advantage member into Medigap; for that you use your six-month open enrollment, a federal guaranteed-issue event, or underwriting.",
               "Practical uses: leave a carrier after a steep rate increase, step down from Plan F or G to Plan N as premiums rise, or move from a high-deductible plan to a full one when your health changes. Free help: Washington SHIBA, 800-562-6900."],
     body="""<p>In most states, the Medigap open enrollment at 65 is the only time an insurer must sell you any plan regardless of your health. Afterward, changing plans usually means answering health questions, and a retiree with a heart history or a cancer diagnosis is effectively locked into whatever they bought at 65, at whatever the carrier decides to charge. Washington State law removes that lock for people who already hold a Medigap policy. It is one of only a handful of states that does, and it changes how a Washingtonian should shop.</p>
<h2>What the rule says, plainly</h2>
<ul>
<li><strong>Who:</strong> anyone who currently has a Medigap (Medicare Supplement) policy.</li>
<li><strong>What:</strong> you may switch to another Medigap plan &mdash; a different plan letter, a different company, or both &mdash; and the new insurer must accept you without medical underwriting.</li>
<li><strong>When:</strong> any time of year. There is no annual window and no birthday or anniversary limit.</li>
<li><strong>The exception:</strong> if you hold <strong>Plan A</strong>, you may switch only to another Plan A. Holders of Plans B through N may move among Plans B through N.</li>
<li><strong>Federal rules still apply:</strong> Plans C and F (including high-deductible F) can be sold only to people who were eligible for Medicare before January 1, 2020. Everyone newer moves among G, N, high-deductible G and the other letters.</li>
</ul>
<h2>What the rule does <em>not</em> do</h2>
<div class="warn-box"><p><strong>It does not get you into Medigap from Medicare Advantage.</strong> The rule protects existing Medigap policyholders. If you are in an Advantage plan and want a supplement, you rely on your six-month open enrollment at 65, on a federal guaranteed-issue right (your plan leaving your county, the 12-month trial right after joining Advantage for the first time, losing employer coverage), or on passing underwriting. If you are weighing Advantage at 65 and think you might want Medigap later, that is the single most important thing to understand about Washington: the door out of Advantage is federal and time-limited; the door between Medigap plans is state law and always open.</p></div>
<p>It also does not freeze your premium. The new plan is priced at the new insurer&rsquo;s current rate for your age and ZIP code, and a premium can still rise later; the difference is that a rise is now a reason to shop rather than a trap. And a switch does not change your Part D plan, which has its own windows.</p>
<h2>How Washingtonians actually use it</h2>
<table class="ctable">
<caption>Common moves under the switching rule. Each is done without health questions.</caption>
<thead><tr><th scope="col">Situation</th><th scope="col">The move</th></tr></thead>
<tbody>
<tr><th scope="row">Your carrier filed a steep increase</th><td>Move the same plan letter to a carrier with a better filed rate history. We compare the filings on <a href="https://www.mymedigaprate.com/medigap-rate-history/washington">Washington Medigap rate history</a>.</td></tr>
<tr><th scope="row">Plan F or G is getting expensive</th><td>Step down to Plan N and accept small office and ER copays in exchange for a lower premium.</td></tr>
<tr><th scope="row">You bought high-deductible G on a budget, and your health changed</th><td>Move to standard Plan G so the deductible stops mattering.</td></tr>
<tr><th scope="row">You still hold Plan F from before 2020</th><td>You may keep it, or move to G or N if the premium no longer earns its keep; you cannot go back to F once you leave.</td></tr>
<tr><th scope="row">You hold Plan A</th><td>You may move to another company&rsquo;s Plan A only. Moving to a richer plan means underwriting.</td></tr>
</tbody></table>
<h2>Why this changes how you shop at 65</h2>
<p>In a state without this rule, the safest advice is to buy the richest plan you can afford at 65, because you may never be able to upgrade. In Washington the calculation is different: you can start with Plan N or high-deductible G and move to Plan G later if your health or your budget changes. What you cannot do is start in Medicare Advantage and count on moving to Medigap at 70 without health questions. That asymmetry is the heart of the Washington decision, and it is why we walk through the <a href="/medicare-supplement">Medigap</a> and <a href="/medicare-advantage">Advantage</a> paths together with you before you pick one.</p>
<h2>How to make the switch</h2>
<ol>
<li>Compare the plan letters and each carrier&rsquo;s current Washington premium and filed rate history for your age and ZIP code.</li>
<li>Apply for the new policy first, noting on the application that you are replacing an existing Medigap policy.</li>
<li>Once the new policy is issued, cancel the old one effective the same date, so there is no gap and no overlap.</li>
<li>Keep your Part D plan; it is unaffected.</li>
</ol>
<p>We handle the comparison and the paperwork at no cost; the premium is the same whether you switch through us, another agent or the carrier. For free, unbiased counseling, Washington SHIBA (800-562-6900) will walk through the same rule with you; the state-by-state picture is on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>""",
     faqs=[("Can I change my Medigap plan any time in Washington?", "If you already hold a Medigap policy, yes. Washington law lets you switch to another Medigap plan or carrier at any time of year without medical underwriting. The one limit is that a Plan A holder can move only to another Plan A."),
           ("I am in Medicare Advantage. Does the Washington rule let me buy Medigap without health questions?", "No. The rule is for existing Medigap policyholders. Leaving Advantage for Medigap uses your six-month open enrollment at 65, a federal guaranteed-issue right such as the 12-month trial right or your plan leaving your county, or medical underwriting."),
           ("My premium just went up. Should I switch?", "Possibly. Because Washington lets you move without underwriting, a steep increase is a reason to compare carriers&rsquo; filed rate histories for your plan letter, not a reason to panic. We compare the filings with you and handle the paperwork; there is no cost and no gap in coverage when it is done right."),
           ("Can I go from Plan N back up to Plan G?", "Yes. Holders of Plans B through N can move to any of B through N at any time without health questions. Only Plan A holders are limited, to another Plan A. Plans C and F remain closed to anyone who became eligible for Medicare after 2019.")],
     sources=[SRC_HIO_WA, SRC_OIC, SRC_MEDIGAP_GOV, SRC_MMR_SWITCH, SRC_MMR_WHY, SRC_SHIBA], cta="Holding a Medigap policy in Washington? Let&rsquo;s see whether a better one is a phone call away.", about="Washington Medigap switching rule"),

dict(slug="veterans", nav_title="Medicare for Washington State veterans and military retirees", crumb="Veterans", scene="cascades",
     title="Medicare for Washington Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (VA Puget Sound in Seattle and American Lake, Mann-Grandstaff in Spokane, Walla Walla, the Vancouver campus) work with Medicare in Washington State, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for Washington State veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, VA Puget Sound, Mann-Grandstaff, Walla Walla, and the retiree communities around JBLM, Naval Base Kitsap and Fairchild AFB",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Washington State veterans and military retirees",
     sub="From Joint Base Lewis-McChord and Naval Base Kitsap to Fairchild and Whidbey Island, Washington retires a lot of service members. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Washington VA care runs through VA Puget Sound (Seattle and American Lake in Tacoma, serving more than 125,000 veterans in 14 counties), Mann-Grandstaff VA Medical Center in Spokane (more than 30,000 veterans a year), the Jonathan M. Wainwright Memorial VA Medical Center in Walla Walla, and the Vancouver campus of VA Portland for Clark County.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Washington is a military state on Medicare. Joint Base Lewis-McChord supports more than 40,000 service members and more than 90,000 family members, veterans and retirees in Pierce and Thurston counties; Naval Base Kitsap is the third-largest naval installation in the country; Fairchild Air Force Base outside Spokane, Naval Air Station Whidbey Island at Oak Harbor and Naval Station Everett each have a retiree community around them. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; UW Medicine, Providence or MultiCare with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Where Washington veterans get VA care</h2>
<p><strong>VA Puget Sound Health Care System</strong> runs the Seattle medical center on Beacon Hill and the American Lake campus in Tacoma, with community clinics around the Sound. <strong>Mann-Grandstaff VA Medical Center</strong> in Spokane serves the Inland Northwest. The <strong>Jonathan M. Wainwright Memorial VA Medical Center</strong> in Walla Walla serves the southeast and the Tri-Cities. Clark County veterans use the Vancouver campus of the VA Portland Health Care System. The two military hospitals &mdash; Madigan Army Medical Center at JBLM and Naval Hospital Bremerton &mdash; see retirees on a space-available basis under TRICARE rules; Medicare does not pay there. We have pages for the three big retiree communities: <a href="/joint-base-lewis-mcchord">Joint Base Lewis-McChord</a>, <a href="/naval-base-kitsap">Naval Base Kitsap</a> and <a href="/fairchild-afb">Fairchild Air Force Base</a>.</p>
<h2>Which Washington plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs, and in Washington the freedom to <a href="/medigap-switching">change Medigap plans later</a>. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Washington State Department of Veterans Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at Madigan, Naval Hospital Bremerton or the Seattle VA?", "No. Medicare does not pay at military or VA facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_VA_SPOKANE, SRC_VA_WA, SRC_WDVA, SRC_JBLM, SRC_KITSAP, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Apple Health (Washington Medicaid): Medicare Savings Programs, Extra Help, D-SNPs", crumb="Apple Health &amp; Medicare Savings Programs", scene="gorge",
     title="Medicare &amp; Apple Health (Washington Medicaid): QMB, SLMB, QI-1 | ECOS Medicare Solutions",
     desc="How Medicare works with Apple Health, Washington's Medicaid program: the Medicare Savings Programs (QMB, SLMB, QI-1) that pay the Part B premium with income limits only for 2026, Extra Help, Dual Special Needs Plans, long-term care through DSHS, and where to apply.",
     llm="Medicare and Apple Health (Washington Medicaid, dual eligible): Medicare Savings Programs (QMB/SLMB/QI-1) run by the Health Care Authority and DSHS with income limits only for 2026, Extra Help, D-SNPs, long-term care through DSHS ALTSA, applying at hca.wa.gov and Washington Connection",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Apple Health: the Medicare Savings Programs and dual-eligible plans",
     sub="If you qualify for both Medicare and Apple Health &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in Washington, and where to apply.",
     keyfacts=["Apple Health is Washington&rsquo;s Medicaid program, run by the Washington State Health Care Authority (HCA). Eligibility for people 65 and over, for people with disabilities and for the Medicare Savings Programs is handled through the Department of Social and Health Services (DSHS).",
               "The Medicare Savings Programs pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. HCA&rsquo;s 2026 standards set QMB at 110% of the federal poverty level, SLMB at 120% and QI-1 at 138%, with income limits only &mdash; no resource test.",
               "Qualifying for a Medicare Savings Program or Apple Health automatically qualifies you for Extra Help with Part D costs.",
               "Dual Special Needs Plans (D-SNPs) are Advantage plans for people with both Medicare and Apple Health. Free counseling: Washington SHIBA, 800-562-6900; Apple Health customer service, 1-800-562-3022."],
     body="""<p>Some Washingtonians qualify for both Medicare and Apple Health &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Apple Health may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Apple Health works for seniors</h2>
<p>Apple Health is administered by the <strong>Washington State Health Care Authority (HCA)</strong>. Washington expanded Medicaid for adults under 65, and it also runs a state-funded Apple Health Expansion program with capped enrollment for adults who do not qualify for the federally funded program because of immigration status. For adults 65 and over, and for people on Medicare because of a disability, eligibility follows the aged, blind and disabled rules (income and resources), and it is determined by <strong>DSHS</strong> &mdash; not by an insurance agency. You apply online through <strong>WashingtonConnection.org</strong>, by phone through Apple Health customer service at 1-800-562-3022, or at a DSHS Community Services office. Long-term services and supports &mdash; in-home care, assisted living, nursing-facility care &mdash; run through DSHS&rsquo;s Aging and Long-Term Support Administration. Unlike some states, Washington does not enroll seniors in a separate Medicaid managed-care program: Medicare stays the primary payer, Apple Health pays second, and coordination happens on the Medicare side through a Dual Special Needs Plan if you choose one.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI-1 &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. HCA&rsquo;s income and resource standards for 2026 set QMB at 110% of the federal poverty level, SLMB at 120% and QI-1 at 138%, with <strong>income limits only</strong>; Washington does not apply a resource test to these programs. You apply through DSHS, and you do not have to be on full Apple Health to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Apple Health you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Apple Health; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Apple Health benefits intact. Availability varies by county and is deepest in the Puget Sound counties, Spokane, Yakima and Clark County.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from Washington SHIBA &mdash; the Statewide Health Insurance Benefits Advisors, run by the Office of the Insurance Commissioner &mdash; at 800-562-6900. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Apple Health benefits working alongside Medicare. Eligibility decisions rest with DSHS, HCA and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Apple Health, the Washington State Health Care Authority, the Department of Social and Health Services, or the federal Medicare program.</p>""",
     faqs=[("What is Apple Health?", "Apple Health is the name of Washington State&rsquo;s Medicaid program, run by the Health Care Authority. For people 65 and over and people with disabilities, eligibility is determined by DSHS under the aged, blind and disabled rules, and long-term care runs through DSHS&rsquo;s Aging and Long-Term Support Administration."),
           ("Who counts as dual eligible in Washington?", "People who qualify for both Medicare and Apple Health. There are full and partial categories; eligibility is determined by DSHS, HCA and CMS, based on income and, for full Apple Health, resources."),
           ("Can Apple Health pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI-1) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. For 2026 the programs have income limits only, with no asset test. Apply through DSHS at WashingtonConnection.org or call 1-800-562-3022; Washington SHIBA (800-562-6900) can help."),
           ("Where do I apply for Apple Health if I am over 65?", "Online at WashingtonConnection.org, by calling Apple Health customer service at 1-800-562-3022, or at a DSHS Community Services office. Washington Healthplanfinder is for people under 65 applying on income alone.")],
     sources=[SRC_HCA_APPLY, SRC_HCA_STD, SRC_SHIBA, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Apple Health dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Washington State", crumb="Chronic SNPs", scene="rainforest",
     title="Chronic SNPs (C-SNP) in Washington State | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Washington State: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Washington State for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Washington State",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Washington county and is concentrated in the Puget Sound counties, Spokane and Clark County; a regular Advantage plan or a Medigap policy may still serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. In Washington they are sold mainly in the larger counties; in much of the state east of the Cascades the menu is short or empty.</p>
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist at UW or your cardiologist at Providence is in it applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. In Washington, remember the asymmetry: a Medigap policyholder can <a href="/medigap-switching">change plans any time</a>; an Advantage member who develops a serious condition cannot count on getting into Medigap later. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Apple Health.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Washington?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Washington State", crumb="Institutional SNPs", scene="palouse",
     title="Institutional SNPs (I-SNP) in Washington State | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Washington State for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Apple Health long-term care through DSHS.",
     llm="Institutional Special Needs Plans (I-SNP) in Washington State for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Washington State",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Washington, many people in long-term care also have Apple Health paying for the care through DSHS&rsquo;s Aging and Long-Term Support Administration; a D-SNP may then be the better fit, and we compare the two."],
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
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP</a> if Apple Health is paying for the care through DSHS &mdash; patiently, and at no cost. Washington&rsquo;s own long-term-care benefit, the WA Cares Fund, is separate from Medicare and from Apple Health; ask us how it fits alongside them.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Apple Health &amp; the Medicare Savings Programs</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Washington county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with Apple Health long-term care through DSHS.")],
     sources=[SRC_MA_GOV, SRC_HCA_APPLY], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="sanjuans",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Washington agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Washington agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling a house, a year of vested stock, or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, and how much of it is taxed.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep &mdash; Washington has no state income tax, which changes the arithmetic.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Washington, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Washington, and how the state&rsquo;s Medigap switching rule changes the decision. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Washington?", "The book covers Medicare and retirement decisions nationally. For Washington specifics &mdash; county-by-county Advantage menus, the Medigap switching rule, Apple Health, the JBLM and Kitsap retiree communities &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
