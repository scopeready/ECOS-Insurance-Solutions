"""Ohio topic pages, part B: turning 65, retiree coverage, veterans, Medicaid / MyCare Ohio, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_OSHIIP, SRC_ODI_MEDICARE, SRC_ODI_MEDIGAP, SRC_BENEFITS_OH, SRC_ODI_MSP,
                              SRC_ODM_MYCARE, SRC_ODM_MYCARE_PLANS, SRC_COA_MYCARE, SRC_OAFP_MYCARE, SRC_TFL, SRC_VA, SRC_HIO, SRC_MRO_U65)
SRC_OPERS = ("OPERS: the OPERS Connector (Via Benefits) and the Health Reimbursement Arrangement", "https://www.opers.org/healthcare/plan-options/connector.shtml")
SRC_OPERS_OE = ("OPERS: 2026 open enrollment insert for HRA recipients", "https://www.opers.org/pubs-archive/healthcare/open-enrollment/2026-open-enrollment-insert.pdf")
SRC_STRS = ("STRS Ohio: Medicare enrollment", "https://www.strsoh.org/receiving-benefits/medicare-enrollment.html")
SRC_STRS_PLANS = ("STRS Ohio: plans and premiums", "https://www.strsoh.org/receiving-benefits/plans-and-premiums.html")
SRC_SERS = ("SERS Ohio: 2026 Medicare plan and premiums", "https://www.ohsers.org/retirees/health-care-in-retirement/plans-and-premiums/")
SRC_OPF = ("OP&amp;F retiree health plan for Medicare-eligible members (Alight Retiree Health Solutions)", "https://www.myexchangeconnection.com/Clients/OP-F/ARHE_MedTrans_Trans-Guide_OPF-P2_022719F_Web.aspx")
SRC_OPF_HOME = ("Ohio Police &amp; Fire Pension Fund", "https://www.op-f.org/")
SRC_UAW = ("UAW Retiree Medical Benefits Trust: Medicare enrollment", "https://www.uawtrust.org/medicareenrollment")
SRC_FL = ("Medicare Enrollment Florida (sister section of this site)", "https://www.ecosinsurancesolutions.com/florida")
SRC_MMR_SWITCH = ("MyMedigapRate: switching Medigap plans, state by state", "https://www.mymedigaprate.com/switching-medigap-plans")
SRC_VA_CLE = ("VA Northeast Ohio Healthcare System: Louis Stokes Cleveland VA Medical Center", "https://www.va.gov/northeast-ohio-health-care/locations/louis-stokes-cleveland-department-of-veterans-affairs-medical-center/")
SRC_VA_COL = ("VA Central Ohio Healthcare System: Chalmers P. Wylie Veterans Outpatient Clinic (Columbus)", "https://www.va.gov/central-ohio-health-care/locations/chalmers-p-wylie-veterans-outpatient-clinic/")
SRC_VA_DIR = ("Licking County Veterans Service Office: Ohio VA medical facilities", "https://lickingcounty.gov/depts/veterans/medical_facilities.htm")
SRC_SPECTRUM = ("Spectrum News 1: Veterans of Ohio by the numbers (Nov 11, 2025)", "https://spectrumnews1.com/oh/toledo/news/2025/11/11/veterans-of-ohio-by-numbers")
SRC_WPMC = ("Wright-Patterson Medical Center (88th Medical Group)", "https://wrightpatterson.tricare.mil/")
SRC_WP_RAO = ("Dayton Daily News: Wright-Patterson&rsquo;s Retiree Activities Office reopens", "https://www.daytondailynews.com/military/wright-pattersons-retiree-activities-office-reopens-provides-wide-range-of-services/7SJEYXR6LVGEPGSDVVLXO6FENI/")
SRC_DSCC = ("Defense Logistics Agency: Defense Supply Center Columbus", "https://www.dla.mil/Land-and-Maritime/About/Locations/Columbus/")
SRC_DSCC_MI = ("MilitaryINSTALLATIONS: Defense Supply Center Columbus", "https://installations.militaryonesource.mil/military-installation/defense-supply-center-columbus")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in Ohio guide", crumb="Turning 65", scene="buckeye",
     title="Turning 65 in Ohio: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in Ohio: your 7-month enrollment window, the Medigap open enrollment that does not repeat, still-working rules, OPERS and STRS retiree steps, the deadlines with lifelong penalties, and a checklist. Free help from a licensed Ohio agent.",
     llm="Turning 65 in Ohio: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap by county and hospital system, public-pension retiree steps, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in Ohio: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for Ohio, where the right answer in Cuyahoga County is not always the right answer in Vinton County, and where a state pension changes the steps.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In Ohio it does not repeat: there is no birthday rule and no annual switching window.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later. Retiree coverage from OPERS, STRS, SERS or a union trust does <strong>not</strong> let you delay; they all expect Parts A and B at 65.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the Ohio twists that most guides leave out. When you are ready, we walk through your specific options at no cost; OSHIIP (800-686-1578) offers free, unbiased state counseling as well.</p>
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
<caption>The two ways most Ohioans put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly.</td></tr>
</tbody></table>
<p>Where you live and where you get care tilt the answer. In Cleveland, Columbus, Cincinnati, Akron, Dayton and Toledo the Advantage menu is deep, but every plan draws its network around some hospital systems and not others, so the first question is which system your doctors belong to. In the Appalachian counties along the river and the farm counties of the northwest the menu is shorter and got shorter for 2026, and a Medigap policy&rsquo;s any-provider access is often the practical choice. If you expect to use Cleveland Clinic and University Hospitals in the same year, or a referral to the James, a supplement removes the network question entirely. Public-pension retirees are a third case &mdash; OPERS, STRS, SERS and OP&amp;F each steer the choice &mdash; and so are military retirees with TRICARE For Life; see <a href="/retiree-coverage">retiree coverage</a> and <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above, and in Ohio it does not repeat. Our research site sets the two side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/ohio">turning 65 in Ohio</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no Ohio insurer can turn you down or charge more for your health. Afterward, Ohio insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. Ohio&rsquo;s big employers &mdash; the state and the universities, the school districts, the hospital systems, the auto and steel plants &mdash; generally qualify while you are still on the payroll; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll.</p>
<div class="note-box"><p><strong>Already retired on OPERS, STRS, SERS or OP&amp;F?</strong> Retiree coverage is not &ldquo;employer coverage&rdquo; for this purpose. Each system expects you to enroll in Parts A and B when first eligible and to send proof; OPERS then pays its HRA allowance only for a plan bought through Via Benefits, and STRS and SERS move you into their Aetna Medicare plan. Missing the step can cost you both the Part B penalty and the pension system&rsquo;s subsidy. See <a href="/retiree-coverage">retiree coverage</a>.</p></div>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage &mdash; and if your coverage is a pension retiree plan, plan on enrolling.</li>
<li>Find out how deep the Advantage menu is in your county, and whether it changed for [[YEAR]].</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage &mdash; or the path your retirement system sets.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if a specific hospital system is your care.</li>
<li>If you winter in Florida or travel, ask how the plan behaves out of state; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">MyCare Ohio</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help Ohioans sort through it every day &mdash; clearly, patiently, and at no cost to you.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. Retiree coverage from OPERS, STRS, SERS, OP&amp;F or a union trust does not count; they all expect Part B at 65."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in Ohio?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget, county and any retiree coverage. The Advantage menu is deep in the metros and thin in much of Appalachian and rural Ohio, and every plan draws its network around some hospital systems and not others. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in Ohio?", "Three things. Ohio&rsquo;s hospital systems contract plan by plan, so the network question comes before price. Ohio&rsquo;s Medigap open enrollment does not repeat and there is no under-65 Medigap requirement, so using the window well matters. And a large share of Ohioans reach 65 with a public pension or union retiree plan that dictates the next step.")],
     sources=[SRC_CMS, SRC_ODI_MEDICARE, SRC_ODI_MEDIGAP, SRC_OSHIIP, SRC_OPERS, SRC_STRS], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in Ohio"),

dict(slug="retiree-coverage", nav_title="Medicare for Ohio public-pension and union retirees: OPERS, STRS, SERS, OP&amp;F, UAW trust", crumb="Retiree coverage", scene="millvalley",
     title="OPERS, STRS, SERS &amp; Union Retiree Coverage with Medicare in Ohio | ECOS Medicare Solutions",
     desc="How Ohio retiree coverage fits with Medicare: the OPERS HRA and Via Benefits connector, the STRS and SERS Aetna Medicare plans, OP&amp;F&rsquo;s stipend through Alight, the UAW Retiree Medical Benefits Trust, and what an outside agent can and cannot do for you.",
     llm="Medicare for Ohio public-pension and union retirees: OPERS HRA via Via Benefits, STRS Ohio and SERS Ohio group Aetna Medicare Advantage PPO with SilverScript Part D, OP&amp;F stipend via Alight, UAW Retiree Medical Benefits Trust Part A/B rules, spouses, snowbirds",
     eyebrow="Your situation · Pension &amp; union retirees", h1="Medicare for Ohio public-pension and union retirees",
     sub="Ohio is a state of retirement systems &mdash; OPERS, STRS, SERS, OP&amp;F, the UAW trust, the steel and auto retiree plans. Each coordinates with Medicare its own way, and the way decides your Medicare choice before any brochure does.",
     keyfacts=["Every Ohio retirement system and retiree trust expects you to enroll in Medicare Parts A and B when first eligible and to send proof. Retiree coverage is not a reason to delay Part B.",
               "<strong>OPERS</strong> funds a Health Reimbursement Arrangement (HRA) for Medicare-eligible benefit recipients, but deposits it only if you enroll in Parts A and B and then buy a Medicare Advantage plan, or a Medigap policy plus Part D, through Via Benefits, the OPERS Connector (Medicare line 1-844-287-9945).",
               "<strong>STRS Ohio</strong> and <strong>SERS Ohio</strong> enrol Medicare-eligible retirees in a group Aetna Medicare Advantage PPO with Part D through SilverScript, once proof of Medicare enrollment is on file. A separate Part D plan or an individual Advantage plan can disrupt the group coverage.",
               "<strong>OP&amp;F</strong> stopped sponsoring group coverage in 2019 and instead pays a monthly stipend into an HRA for plans bought through Alight Retiree Health Solutions. <strong>The UAW Retiree Medical Benefits Trust</strong> pays as if you have Parts A and B whether or not you enrolled; skipping Part B leaves you paying Medicare&rsquo;s share yourself."],
     body="""<p>Ask a room of Ohio 65-year-olds where their health coverage comes from and you will hear OPERS, STRS, SERS, OP&amp;F, &ldquo;the trust,&rdquo; a steel or auto retiree plan, a hospital system&rsquo;s retiree plan, or a city or county plan long before you hear &ldquo;I picked one off Medicare.gov.&rdquo; That is the Ohio twist. The retirement system or trust usually decides the shape of your Medicare coverage, and the mistakes people make are not about choosing the wrong plan but about missing the step their system required. Here is how each of the big ones works, and where an independent agent fits.</p>
<h2>The rule every system shares: enroll in Parts A and B on time</h2>
<p>Retiree coverage is not &ldquo;current employer coverage&rdquo; for Medicare&rsquo;s purposes, so it does not let you delay Part B without a penalty. Every Ohio system expects you to enroll in Parts A and B during your Initial Enrollment Period and send proof. Miss it and you can lose both ways: Medicare&rsquo;s lifelong Part B penalty on one side, and your pension system&rsquo;s subsidy or plan enrollment on the other. If you are approaching 65 on any of these plans, the first thing we check is your Part B date.</p>
<h2>OPERS: an allowance, but only through the Connector</h2>
<p>The Ohio Public Employees Retirement System does not enrol Medicare-eligible retirees in a group plan. Instead it funds a <strong>Health Reimbursement Arrangement (HRA)</strong> &mdash; a tax-free account that reimburses premiums, deductibles, copays and other eligible expenses &mdash; and administers it through <strong>Via Benefits, the OPERS Connector</strong>. To receive the monthly HRA deposits you must enroll in Medicare Parts A and B and then choose a Medicare Advantage plan, or a Medigap policy, plus a Part D plan, <em>through Via Benefits</em>. A Via Benefits licensed benefit advisor does the enrollment; the plans themselves are ordinary individual-market plans sold in your county.</p>
<div class="note-box"><p><strong>Where we fit for OPERS retirees.</strong> We cannot enrol you in the plan that unlocks your HRA &mdash; Via Benefits must do that &mdash; and we will tell you so up front. What we can do is help you understand the choice before the call: which of your county&rsquo;s plans include your hospital system, whether a Medigap policy or an Advantage plan is the better use of the allowance, what your six-month Medigap open enrollment means, and how a spouse who is not yet 65 fits. Then you go to Via Benefits knowing what you want. Call Via Benefits at 1-844-287-9945 (Medicare) when you are ready to enrol; the 2026 open enrollment insert is linked below.</p></div>
<h2>STRS Ohio and SERS Ohio: a group Medicare Advantage plan of their own</h2>
<p>The State Teachers Retirement System and the School Employees Retirement System both sponsor a <strong>group Aetna Medicare Advantage PPO</strong> for Medicare-eligible retirees, with prescription coverage through <strong>SilverScript</strong>, a Medicare Part D plan, and pharmacy administration by CVS Caremark. STRS moves you from its pre-Medicare Aetna plan into the Aetna Medicare Plan once it has proof of your Medicare enrollment; failing to send that proof affects your STRS coverage. SERS runs the same structure with its own premiums, and offers dental through Delta Dental and vision through VSP. Because the group plan already includes Part D, buying a separate individual Part D plan &mdash; or an individual Advantage plan &mdash; can knock you out of the group coverage, so do not sign anything without checking with your system first.</p>
<p>Where we help STRS and SERS retirees: deciding whether the group plan or the individual market is the better fit for you and your spouse (some retirees with a high premium tier compare a Medigap policy and an individual Part D plan against it), understanding the network and the Part B premium you still pay Medicare, and handling the spouse who is on Medicare but not eligible for the group plan. If you do leave the group plan, we make sure you understand what you give up and whether you can return.</p>
<h2>OP&amp;F: a stipend through Alight</h2>
<p>The Ohio Police &amp; Fire Pension Fund stopped sponsoring group health insurance in 2019 and now pays a <strong>monthly stipend into an HRA</strong> for retirees who buy coverage on the individual market through its connector, <strong>Alight Retiree Health Solutions</strong>. Medicare-eligible retirees enrol through Alight in a Medicare Advantage plan or a Medigap policy plus Part D; open enrollment runs November 1 to December 15, and enrolling through Alight within the window after your employer coverage ends is what turns the stipend on. As with OPERS, the enrollment must go through the connector to keep the money flowing, and we tell you that first.</p>
<h2>The UAW Retiree Medical Benefits Trust and other union plans</h2>
<p>Ohio&rsquo;s auto retirees &mdash; the Toledo Jeep and transmission plants, Avon Lake, Lordstown, the Honda supply chain&rsquo;s union shops, Defiance, Parma &mdash; largely carry coverage through the <strong>UAW Retiree Medical Benefits Trust</strong>. The Trust requires enrollment in Part A at 65 and pays its benefits <em>as if</em> you have Parts A and B whether or not you enrolled in Part B; if you skip Part B, the Trust does not pay what Medicare would have paid and you owe it yourself. Surviving spouses 65 and over must enrol in both A and B to keep Trust coverage. Retiree Health Care Connect (866-637-7555) is the Trust&rsquo;s help line. Steelworker, utility, railroad and building-trades retiree plans follow their own documents, but the pattern is the same: Parts A and B on time, and check with the plan before adding anything.</p>
<h2>Spouses, second homes and Florida</h2>
<ul>
<li><strong>A spouse under 65</strong> usually stays on the pre-Medicare side of the same system; the Medicare-eligible spouse&rsquo;s choice should not strand them. We map both timelines.</li>
<li><strong>A spouse without the pension</strong> is often on the open Medicare market while you are in a group plan or an HRA. That is where an independent agent does the most good.</li>
<li><strong>Snowbirds.</strong> A Medigap policy travels; the STRS and SERS Aetna PPO and most individual PPOs cover out-of-network care at a price; an HMO covers emergencies only. If you spend winters in Florida, price the plan on how it behaves in Naples or The Villages, not at home. Our <a href="https://www.ecosinsurancesolutions.com/florida">Florida section</a> covers the other end, and the state-by-state Medigap switching rules are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</li>
</ul>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency. It is not affiliated with OPERS, STRS Ohio, SERS Ohio, OP&amp;F, HPRS, Via Benefits, Alight, the UAW Retiree Medical Benefits Trust, or any employer or union plan, and it cannot enrol you in a plan that those systems require you to purchase through their own connector.</p>""",
     faqs=[("I am an OPERS retiree. Can you enrol me in a Medicare plan?", "Not in the plan that unlocks your HRA &mdash; OPERS pays the allowance only for a plan bought through Via Benefits, its connector, so that enrollment has to go through Via Benefits at 1-844-287-9945. We help you understand the choice beforehand (which plans include your hospital system, Medigap versus Advantage, your spouse&rsquo;s timing) so the call is short and the plan is right."),
           ("I retired from teaching. Do I need to buy a Part D plan when I turn 65?", "Generally not. The STRS Ohio Aetna Medicare Plan includes Part D coverage through SilverScript, and enrolling in a separate Part D plan can disrupt the group plan. Send STRS your proof of Medicare enrollment and let it move you into the Medicare plan; check with STRS at 888-227-7877 before buying anything else."),
           ("My retiree plan says it will pay as if I have Part B. Can I skip Part B?", "You can, but it costs you twice. The UAW trust and similar plans pay only the share left after Medicare would have paid, so without Part B you owe Medicare&rsquo;s share yourself, and Medicare adds a lifelong 10%-per-year penalty if you enrol later. Enrol in Part B on time."),
           ("My spouse has no pension coverage. What do we do?", "Your spouse shops the open Medicare market in your county while you stay in the group plan or the HRA. We compare Advantage and Medigap for the spouse with the same doctors and pharmacy in mind, and time both enrollments so nobody has a gap.")],
     sources=[SRC_OPERS, SRC_OPERS_OE, SRC_STRS, SRC_STRS_PLANS, SRC_SERS, SRC_OPF, SRC_OPF_HOME, SRC_UAW, SRC_CMS, SRC_FL, SRC_MMR_SWITCH], cta="Retired on an Ohio pension? Let&rsquo;s make Medicare fit the plan you already have.", about="Medicare coordination with Ohio public-pension and union retiree coverage"),

dict(slug="veterans", nav_title="Medicare for Ohio veterans and military retirees", crumb="Veterans", scene="flightline",
     title="Medicare for Ohio Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (Cleveland, Columbus, Cincinnati, Dayton, Chillicothe) work with Medicare in Ohio, why Part B timing matters even with VA care, Wright-Patterson retirees, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for Ohio veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, Ohio VA medical centers, Wright-Patterson AFB and the Defense Supply Center Columbus retiree communities",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for Ohio veterans and military retirees",
     sub="Ohio has about 606,000 veterans and, around Wright-Patterson, one of the Air Force&rsquo;s largest retiree communities. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "Ohio VA care runs through the Louis Stokes Cleveland VA Medical Center (24 northeast Ohio counties), the Cincinnati VA Medical Center (Cincinnati and Fort Thomas, Kentucky), the Dayton VA Medical Center, the Chillicothe VA Medical Center, and the Chalmers P. Wylie VA Ambulatory Care Center in Columbus, which is an outpatient facility rather than a hospital.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>Ohio is home to roughly 606,000 veterans (Census Bureau 2020&ndash;2024 estimate) and to the retiree communities around Wright-Patterson Air Force Base near Dayton and the Defense Supply Center Columbus in Whitehall. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; Cleveland Clinic or the James with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>Where Ohio veterans get VA care</h2>
<p>The <strong>Louis Stokes Cleveland VA Medical Center</strong> provides full primary, secondary and tertiary care to veterans in 24 northeast Ohio counties, with community clinics across the region. The <strong>Cincinnati VA Medical Center</strong> has divisions in Cincinnati and Fort Thomas, Kentucky, and serves 17 counties in Ohio, Kentucky and Indiana. The <strong>Dayton VA Medical Center</strong> offers a full range of medical, surgical, mental-health, geriatric and hospice care. The <strong>Chillicothe VA Medical Center</strong> provides medical care and nursing-home services and is the chronic mental-health referral center for southern Ohio and parts of West Virginia and Kentucky. Columbus veterans use the <strong>Chalmers P. Wylie VA Ambulatory Care Center</strong>, a large outpatient facility rather than a hospital; inpatient care is referred out, which is one more reason Part B matters in central Ohio.</p>
<h2>Military hospitals after 65</h2>
<p><strong>Wright-Patterson Medical Center</strong>, run by the 88th Medical Group, continues to see retirees under TRICARE rules, and the base&rsquo;s Retiree Activities Office works with TRICARE and the Dayton VA on exactly the questions this page covers. Medicare does not pay at a military hospital. Most Wright-Patt retirees pair TFL with civilian care at Kettering Health or Premier Health, and the Defense Supply Center Columbus is the DEERS and ID-card office for central Ohio families. We have pages for both communities: <a href="/wright-patterson-afb">Wright-Patterson AFB</a> and <a href="/defense-supply-center-columbus">Defense Supply Center Columbus</a>.</p>
<h2>Which Ohio plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
<li><strong>A veteran with an OPERS, STRS or union retiree plan</strong> layers a third set of rules on top; see <a href="/retiree-coverage">retiree coverage</a>.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the Ohio Department of Veterans Services, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at Wright-Patterson Medical Center or the Cleveland VA?", "No. Medicare does not pay at military or VA facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is there a VA hospital in Columbus?", "Columbus has the Chalmers P. Wylie VA Ambulatory Care Center, a large outpatient facility with primary and specialty care, but not an inpatient VA hospital; inpatient care is referred to other VA medical centers or community hospitals. That makes Part B, which pays at those community hospitals, especially important for central Ohio veterans."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_VA_CLE, SRC_VA_COL, SRC_VA_DIR, SRC_SPECTRUM, SRC_WPMC, SRC_WP_RAO, SRC_DSCC, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Ohio Medicaid: Next Generation MyCare Ohio, Medicare Savings Programs, Extra Help", crumb="Ohio Medicaid &amp; MyCare", scene="ohioriver",
     title="Medicare &amp; Ohio Medicaid: MyCare Ohio, QMB, SLMB | ECOS Medicare Solutions",
     desc="How Medicare works with Ohio Medicaid: Next Generation MyCare Ohio (launched January 1, 2026, statewide by August), Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, and where to apply (benefits.ohio.gov, 800-324-8680).",
     llm="Medicare and Ohio Medicaid (dual eligible): Next Generation MyCare Ohio FIDE-SNP from 2026, Medicare Savings Programs (QMB/SLMB/QI) through the Ohio Department of Medicaid, Extra Help, applying at benefits.ohio.gov",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Ohio Medicaid: MyCare Ohio and the Medicare Savings Programs",
     sub="If you qualify for both Medicare and Ohio Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in Ohio in 2026, the year MyCare Ohio was rebuilt, and where to apply.",
     keyfacts=["Ohio Medicaid is administered by the Ohio Department of Medicaid. Apply at benefits.ohio.gov, through your county Job and Family Services office, or by calling the Ohio Medicaid Consumer Hotline at 800-324-8680.",
               "<strong>Next Generation MyCare Ohio</strong> launched January 1, 2026 as a fully integrated dual-eligible special needs plan (FIDE-SNP) &mdash; one plan for both Medicare and Medicaid &mdash; replacing the MyCare Ohio demonstration that ended December 31, 2025. The plans are Anthem Blue Cross and Blue Shield, Buckeye Health Plan, CareSource and Molina Healthcare of Ohio. It began in the original 29 MyCare counties and was scheduled to reach all 88 counties between April 1 and August 1, 2026.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. They are not subject to Ohio estate recovery, and qualifying automatically brings Part D Extra Help.",
               "Free counseling: OSHIIP, 800-686-1578, helps with Medicare Savings Program applications at no cost."],
     body="""<p>Some Ohioans qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Ohio Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in Ohio</h2>
<p>Ohio Medicaid is administered by the <strong>Ohio Department of Medicaid</strong>, with eligibility handled through your county Department of Job and Family Services. Eligibility is determined by the state &mdash; not by an insurance agency &mdash; based on income and resources. You apply at <strong>benefits.ohio.gov</strong>, at your county JFS office, or by phone at <strong>800-324-8680</strong>, the Ohio Medicaid Consumer Hotline.</p>
<h2>MyCare Ohio, rebuilt for 2026</h2>
<p>For a decade Ohioans with both Medicare and Medicaid in 29 counties were served by <strong>MyCare Ohio</strong>, a federal demonstration that combined the two programs in one Medicare-Medicaid plan. That demonstration ended December 31, 2025. On January 1, 2026 the Ohio Department of Medicaid launched <strong>Next Generation MyCare</strong>, built instead as a <strong>fully integrated dual-eligible special needs plan (FIDE-SNP)</strong>: a Medicare Advantage plan and a Medicaid managed-care plan run by the same company, with one card, one care coordinator and one set of benefits that includes long-term services and supports. Four companies were chosen to run it: <strong>Anthem Blue Cross and Blue Shield, Buckeye Health Plan, CareSource and Molina Healthcare of Ohio</strong>. Phase one covered the 29 counties where MyCare already operated; the program was scheduled to expand to the rest of Ohio in phases between April 1 and August 1, 2026, which would make it statewide as of this writing. Because the timing of your county&rsquo;s phase and the rules for keeping Original Medicare alongside the Medicaid side are set by the state, confirm your own situation with the Ohio Medicaid Consumer Hotline or OSHIIP before changing anything.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. A fourth, QDWI, pays the Part A premium for certain working people with disabilities. Ohio&rsquo;s income and resource limits change each year; the Ohio Department of Insurance publishes a current guide (linked below). None of the four is subject to Ohio estate recovery, and you do not have to be on full Medicaid to qualify. Apply through Ohio Medicaid, and OSHIIP will help you fill in the application for free.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Next Generation MyCare plans and other Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from OSHIIP &mdash; the Ohio Senior Health Insurance Information Program, part of the Ohio Department of Insurance &mdash; at 800-686-1578. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a MyCare or other dual plan is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with the Ohio Department of Medicaid and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Ohio Medicaid, the Ohio Department of Medicaid, MyCare Ohio, or the federal Medicare program.</p>""",
     faqs=[("What is Next Generation MyCare Ohio?", "Ohio&rsquo;s program for people with both Medicare and Medicaid, relaunched January 1, 2026 as a fully integrated dual-eligible special needs plan (FIDE-SNP) run by Anthem Blue Cross and Blue Shield, Buckeye Health Plan, CareSource or Molina Healthcare of Ohio. It replaced the MyCare Ohio demonstration that ended December 31, 2025, started in the original 29 counties, and was scheduled to reach all 88 counties by August 1, 2026."),
           ("Who counts as dual eligible in Ohio?", "People who qualify for both Medicare and Ohio Medicaid. There are full and partial categories; eligibility is determined by the Ohio Department of Medicaid and CMS, based on income and resources."),
           ("Can Ohio Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply at benefits.ohio.gov or 800-324-8680; OSHIIP (800-686-1578) helps with the form for free."),
           ("Where do I apply for Medicaid if I am over 65?", "At benefits.ohio.gov, at your county Department of Job and Family Services, or by calling the Ohio Medicaid Consumer Hotline at 800-324-8680.")],
     sources=[SRC_ODM_MYCARE, SRC_ODM_MYCARE_PLANS, SRC_COA_MYCARE, SRC_OAFP_MYCARE, SRC_BENEFITS_OH, SRC_ODI_MSP, SRC_OSHIIP, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and Ohio Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in Ohio", crumb="Chronic SNPs", scene="amish",
     title="Chronic SNPs (C-SNP) in Ohio | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in Ohio: which conditions qualify, what a C-SNP offers, why they matter for under-65 Ohioans who cannot buy Medigap, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in Ohio for qualifying chronic conditions, including their role for under-65 beneficiaries who cannot buy Medigap in Ohio",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in Ohio",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by Ohio county and is concentrated in the metros; a regular Advantage plan or a Medigap policy may still serve you better.",
               "Because Ohio does not require insurers to sell Medigap under 65, C-SNPs and other Advantage plans are the main route for younger Ohioans on Medicare because of a disability.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. In Ohio they are sold mostly in the metro counties, and they carry an extra importance here: Ohio is one of the few states that does not require insurers to sell Medigap to people under 65, so for a younger Ohioan on Medicare because of diabetes, heart failure or kidney disease, a C-SNP is often the most tailored coverage available until 65.</p>
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist at OSU or your cardiologist at Cleveland Clinic is in it applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Next Generation MyCare Ohio</a> for people with both Medicare and Ohio Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in Ohio?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("I am under 65 on Medicare. Is a C-SNP my only option in Ohio?", "Not the only one, but often the best-tailored one. Ohio does not require insurers to sell Medigap under 65, so most younger beneficiaries choose among Medicare Advantage plans, including C-SNPs and, for people with Medicaid, MyCare Ohio. A full Medigap open enrollment begins at 65."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV, SRC_MRO_U65, SRC_HIO], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in Ohio", crumb="Institutional SNPs", scene="buckeye",
     title="Institutional SNPs (I-SNP) in Ohio | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in Ohio for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Ohio Medicaid and Next Generation MyCare.",
     llm="Institutional Special Needs Plans (I-SNP) in Ohio for facility-level care, and how they compare with Next Generation MyCare Ohio when Medicaid pays for care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in Ohio",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In Ohio, many people in long-term care also qualify for Medicaid; a Next Generation MyCare plan, which covers Medicare and Medicaid long-term services in one plan, may then be the better fit, and we compare the two."],
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
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Next Generation MyCare plan</a> if Ohio Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Ohio Medicaid &amp; MyCare Ohio</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your Ohio county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or a MyCare Ohio plan coordinates with a facility and with Ohio Medicaid.")],
     sources=[SRC_MA_GOV, SRC_ODM_MYCARE], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="hocking",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed Ohio agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed Ohio agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how a pension lump sum, the sale of a farm or a rental, or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed, and the Windfall Elimination and Government Pension Offset history that matters to Ohio&rsquo;s public retirees who never paid into Social Security.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in Ohio (OH License #1616139), and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in Ohio, and how they fit with OPERS, STRS, the VA or MyCare. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to Ohio?", "The book covers Medicare and retirement decisions nationally. For Ohio specifics &mdash; hospital-system networks, OPERS and STRS coordination, MyCare Ohio, the Wright-Patterson community &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
