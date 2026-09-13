"""New Mexico topic pages, part B: turning 65, rural New Mexico & the IHS, veterans, Turquoise Care, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_SEP, SRC_OSI, SRC_ALTSD_SHIP, SRC_SHIP_NM, SRC_SB21, SRC_HIO_NM,
                              SRC_NMMIP, SRC_FIERCE, SRC_HCA_TC, SRC_HCA_PLANS, SRC_HSD_MSP, SRC_TFL, SRC_VA)
SRC_RURAL_PLAN = ("New Mexico Rural Health Plan, Rural Health Planning Workgroup (Legislative Health &amp; Human Services Committee, 2019)", "https://www.nmlegis.gov/handouts/LHHS%20092519%20Item%202%20New%20Mexico%20Rural%20Health%20Plan.pdf")
SRC_CAH = ("CMS: Critical Access Hospitals", "https://www.cms.gov/medicare/health-safety-standards/certification-compliance/critical-access-hospitals")
SRC_KFF_IHS = ("KFF: The role of Medicare and the Indian Health Service for American Indians and Alaska Natives", "https://www.kff.org/medicare/the-role-of-medicare-and-the-indian-health-service-for-american-indians-and-alaska-natives-health-access-and-coverage/")
SRC_IHS_PRC = ("Indian Health Service: Purchased/Referred Care, alternate resources (payer of last resort)", "https://www.ihs.gov/prc/eligibility/requirements-alternate-resources/")
SRC_HCGOV_AIAN = ("HealthCare.gov: health coverage for American Indians and Alaska Natives", "https://www.healthcare.gov/american-indians-alaska-natives/")
SRC_CMS_AIAN = ("CMS: Medicare for American Indians and Alaska Natives", "https://www.cms.gov/training-education/partner-outreach-resources/american-indian-alaska-native/medicare-ia-ans")
SRC_GIMC = ("Indian Health Service: Gallup Indian Medical Center", "https://www.ihs.gov/navajo/healthcarefacilities/gallup/")
SRC_VA_NM = ("VA New Mexico health care: about us", "https://www.va.gov/new-mexico-health-care/about-us/")
SRC_USAFACTS_VET = ("USAFacts: Veterans in New Mexico (U.S. Census Bureau 2020&ndash;2024 estimates)", "https://usafacts.org/topics/veterans/state/new-mexico/")
SRC_KIRTLAND = ("TRICARE: 377th Medical Group, Kirtland AFB", "https://tricare.mil/GettingCare/FindDoctor/MTF/Facilities/377th-Medical-Group-Kirtland-Air-Force-Base-Medical-Facility")
SRC_HOLLOMAN = ("Holloman AFB: 49th Medical Group", "https://holloman.tricare.mil/")
SRC_CANNON = ("Cannon AFB: 27th Special Operations Medical Group", "https://cannon.tricare.mil/")
SRC_GCRMC = ("CHRISTUS Health: agreement to acquire Gerald Champion Regional Medical Center", "https://www.christushealth.org/connect/news/gerald-champion")
SRC_AZ = ("Medicare Enrollment Arizona (sister section with Mesa and Sun City offices)", "https://www.ecosinsurancesolutions.com/arizona")
SRC_TX_ELPASO = ("Texas Medicare Enrollment (sister section): Medicare in El Paso", "https://www.ecosinsurancesolutions.com/texas/el-paso")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in New Mexico guide", crumb="Turning 65", scene="sandia",
     title="Turning 65 in New Mexico: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in New Mexico: your 7-month enrollment window, the Medigap open enrollment you get once, the 2027 birthday rule, still-working rules for the labs, the base and the state, the deadlines with lifelong penalties, and a checklist. Free help from a licensed agent.",
     llm="Turning 65 in New Mexico: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap by county and distance, the 2027 birthday rule, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in New Mexico: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for New Mexico, where the right answer in Bernalillo County is not always the right answer in Catron County.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. Use it well: after it, New Mexico insurers can underwrite, and the birthday rule that starts in 2027 only lets you move to equal or lesser benefits.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the New Mexico twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
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
<caption>The two ways most New Mexicans put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly.</td></tr>
</tbody></table>
<p>Where you live tilts the answer. In Albuquerque, Rio Rancho, Santa Fe or Las Cruces the Advantage menu is deep and the networks include the big systems. In the mountain and plains counties the menu is short, the hospital is a Critical Access Hospital with 25 beds, and the specialist is in Albuquerque, El Paso or Lubbock, which is where a Medigap policy&rsquo;s any-provider access earns its premium. If you turn 65 this fall, note that Presbyterian is discontinuing most of its Advantage plans for 2027, so a Presbyterian plan is not a long-term choice this year. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>. If your care runs through an IHS or tribal facility, see <a href="/rural-new-mexico">rural New Mexico and the IHS</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above. Our research site sets the two side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/new-mexico">turning 65 in New Mexico</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no New Mexico insurer can turn you down or charge more for your health. Afterward, insurers can use medical underwriting. From January 1, 2027, the state&rsquo;s birthday rule gives you a 60-day window each year to move to a plan of equal or lesser benefits &mdash; useful, but it does not let you buy up later, so pick the plan you want now.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. New Mexico&rsquo;s big employers &mdash; the national labs and their contractors, the universities, the state and the school districts, the hospital systems, the oil-and-gas companies in the Permian, the Air Force bases&rsquo; civilian workforce &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll. Public-employee retirees on a state or educational retiree plan have their own rules; ask us.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find out how deep the Advantage menu is in your county, and whether it changed for [[YEAR]] or is changing for 2027.</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if your specialist is out of town or out of state.</li>
<li>If you live far from a hospital or use an IHS clinic, read the <a href="/rural-new-mexico">rural New Mexico guide</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">Turquoise Care</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help New Mexicans sort through it every day &mdash; clearly, patiently, and at no cost to you. New Mexico SHIP (800-432-2080), run by the Aging and Long-Term Services Department, offers free, unbiased state counseling as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in New Mexico?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget and county. The Advantage menu is deep in the Albuquerque, Santa Fe and Las Cruces areas and thin in much of rural New Mexico, and Presbyterian is leaving most of that market for 2027. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in New Mexico?", "Distance. Your county decides how many Advantage plans you can choose from, and whether the nearest in-network specialist is across town or across the state. New Mexico does not sell Medigap under 65, so the six-month window at 65 is your first full one, and the 2027 birthday rule only lets you move sideways or down afterward. And a large share of New Mexicans reach 65 with TRICARE For Life, VA care or IHS eligibility, which changes the calculation.")],
     sources=[SRC_CMS, SRC_SB21, SRC_ALTSD_SHIP, SRC_SHIP_NM, SRC_FIERCE], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in New Mexico"),

dict(slug="rural-new-mexico", nav_title="Medicare in rural New Mexico: distance to care, networks and the Indian Health Service", crumb="Rural New Mexico", scene="pinon",
     title="Medicare in Rural New Mexico: Distance, Networks &amp; the IHS | ECOS Medicare Solutions",
     desc="Which Medicare plans work when the nearest hospital is an hour away, when your specialist is in Albuquerque, El Paso or Lubbock, or when your care runs through an IHS or tribal facility. Networks, Critical Access Hospitals, out-of-area rules and how Medicare fits with the Indian Health Service.",
     llm="Medicare in rural New Mexico: counties without hospitals, Critical Access Hospitals, Advantage networks and out-of-area rules, cross-border specialists in Texas, Colorado and Arizona, and how Medicare coordinates with the Indian Health Service and tribal facilities",
     eyebrow="Your situation · Distance to care", h1="Medicare in rural New Mexico: when the nearest hospital is an hour away",
     sub="Half of New Mexico&rsquo;s counties are small and far apart, several have no hospital at all, and the specialist is often in another city or another state. Here is how to choose a plan that works at that distance &mdash; including for families whose care runs through the Indian Health Service.",
     keyfacts=["New Mexico&rsquo;s 2019 Rural Health Plan found that 5 of the state&rsquo;s 12 &ldquo;small town rural&rdquo; counties had no hospital, all of them a significant distance from the nearest one, and that 6 of the 7 hospitals in the other small-town counties were Critical Access Hospitals &mdash; 25-bed facilities that, by federal definition, sit more than 35 miles (or 15 mountain miles) from the next hospital.",
               "A Medigap policy with Original Medicare works with any provider in the U.S. that accepts Medicare, so an Albuquerque, El Paso, Lubbock or Denver referral is covered the same as care at home. Most Advantage HMOs cover only emergencies and urgent care outside their service area; PPOs cover out-of-network care at higher cost.",
               "The Indian Health Service is not health insurance. Its Purchased/Referred Care program is the payer of last resort and requires eligible patients to use resources such as Medicare when they have them, and enrolling in Medicare pays for care an IHS or tribal facility cannot provide or that is too far away. IHS eligibility does not change when you enroll.",
               "A plan leaving your county, and a FEMA-declared emergency or disaster that made you miss an enrollment window, each open a Special Enrollment Period."],
     body="""<p>The Medicare rules are the same in Reserve as in Albuquerque. What differs is what they mean on the ground. A &ldquo;network&rdquo; in Bernalillo County is a list of hospitals across town; in Catron, Harding or Hidalgo County it may be a Critical Access Hospital an hour away and a specialist three hours beyond that. This page is about choosing coverage that still works at those distances &mdash; and, because so many rural New Mexicans get their care through the Indian Health Service, about how Medicare and the IHS fit together.</p>
<h2>The map, honestly</h2>
<p>The state&rsquo;s 2019 Rural Health Plan, prepared for the Legislature, counted 12 &ldquo;small town rural&rdquo; counties; five had no hospital at all, and six of the seven hospitals in the rest were Critical Access Hospitals. A Critical Access Hospital is a federal designation for a hospital with up to 25 beds that is more than a 35-mile drive from the next hospital (15 miles in mountainous terrain or on secondary roads), which is a good description of Taos, Silver City, Deming, Lovington and much of the map between them. Larger regional hospitals anchor Farmington, Gallup, Roswell, Carlsbad, Hobbs, Clovis, Alamogordo and Las Cruces, and Valencia County&rsquo;s residents drive to Albuquerque. For cancer care, cardiac surgery or a sub-specialist, most of the state drives to Albuquerque or Santa Fe, and the borders leak: Las Cruces and Silver City look to El Paso, the eastern plains to Lubbock and Amarillo, the Four Corners to Durango and Denver, and the bootheel and Gila country to Tucson.</p>
<h2>Which plans travel</h2>
<table class="ctable">
<caption>How each plan type behaves once you are outside its service area or its network. Emergencies are covered by every plan, everywhere in the U.S.</caption>
<thead><tr><th scope="col">Plan type</th><th scope="col">Routine and specialty care out of area</th><th scope="col">What you pay there</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + Medigap</th><td>Any provider that accepts Medicare &mdash; UNM, El Paso, Lubbock, Denver, Tucson</td><td>Same as at home &mdash; the supplement pays its share anywhere</td></tr>
<tr><th scope="row">Medicare Advantage PPO</th><td>Out-of-network providers, if the plan allows</td><td>Higher out-of-network copays or coinsurance; check the plan&rsquo;s out-of-network maximum</td></tr>
<tr><th scope="row">Medicare Advantage HMO</th><td>Emergencies and urgent care only, on most plans; referrals must be to in-network providers</td><td>Routine care generally not covered out of network or out of area</td></tr>
<tr><th scope="row">Part D (standalone or built in)</th><td>National pharmacy networks; mail order</td><td>Preferred-pharmacy pricing may differ; in many towns mail order is the preferred option</td></tr>
</tbody></table>
<div class="note-box"><p><strong>Read the network the way you drive it.</strong> A plan can be sold in your county and still have no in-network cardiologist within 150 miles. Before you enroll in an Advantage plan out here, we check three things in writing: whether your local hospital and clinic are in-network, where the nearest in-network specialists in the fields you use actually are, and what the plan says about care across the state line &mdash; because a network that reaches El Paso is worth more in Las Cruces than one that reaches Albuquerque.</p></div>
<h2>If you live near a border</h2>
<p>Medicare itself has no state lines, and a Medigap policy issued in New Mexico pays the same at a hospital in El Paso, Lubbock, Durango or Tucson. Advantage and Part D plans are sold by county and their networks stop where the carrier&rsquo;s contracts stop, so a Las Cruces plan may or may not include El Paso&rsquo;s hospitals. Our agency is licensed in Texas, Arizona and Colorado as well as New Mexico, and our <a href="https://www.ecosinsurancesolutions.com/texas/el-paso">El Paso</a> and <a href="https://www.ecosinsurancesolutions.com/arizona">Arizona</a> sections cover the view from the other side. If you split the year between New Mexico and Arizona or Texas, your plan follows your <em>permanent</em> residence; changing it opens a Special Enrollment Period and means choosing from the plans sold in the new county.</p>
<h2>Medicare and the Indian Health Service</h2>
<p>A large share of rural New Mexicans &mdash; on the Navajo Nation, in the Pueblos, on the Jicarilla and Mescalero Apache reservations and in the border towns around them &mdash; get their care through IHS, tribal or urban Indian health programs. Three things are worth knowing, each straight from the federal sources.</p>
<ul>
<li><strong>IHS is not health insurance.</strong> HealthCare.gov and the IHS both say so plainly, and the federal government encourages eligible members of federally recognized tribes to enroll in coverage they qualify for, Medicare included. Enrolling does not change your eligibility for IHS or tribal care.</li>
<li><strong>Purchased/Referred Care is the payer of last resort.</strong> When an IHS facility refers you out &mdash; to a hospital in Gallup, Farmington, Albuquerque or Flagstaff &mdash; the PRC program requires you to use &ldquo;alternate resources&rdquo; such as Medicare or Medicaid first when you have them. Without Medicare, a referral can depend on PRC funds and priorities; with it, Medicare pays.</li>
<li><strong>Medicare pays IHS and tribal facilities.</strong> IHS and tribal hospitals such as Gallup Indian Medical Center bill Medicare for covered services, and third-party revenue from Medicare, Medicaid and private insurance is a significant part of their operating budgets. Medicare also pays for care IHS cannot provide or that is too far away &mdash; specialists, private hospitals, dialysis closer to home.</li>
</ul>
<p>What that means for the plan choice: Original Medicare with a Medigap policy works at any IHS, tribal or private facility that accepts Medicare, with no network question. A Medicare Advantage plan only pays an IHS or tribal facility as an in-network provider if the facility is in its network, so if you are considering one, ask specifically whether your IHS hospital or tribal clinic is listed, and what happens on a referral when it is not. If you also qualify for Turquoise Care, the Medicare Savings Programs on our <a href="/medicaid">Medicaid page</a> can pay your Part B premium, and New Mexico has no asset test for them. We are a private insurance agency, not connected with the IHS or any tribal government; for tribal-specific benefits questions, your facility&rsquo;s benefits coordinator and New Mexico SHIP (800-432-2080) are the right first calls.</p>
<h2>Disasters, fires and missed windows</h2>
<p>New Mexico&rsquo;s recent wildfire and flood seasons have displaced whole communities during enrollment season. If a FEMA-declared emergency or major disaster kept you from enrolling in or changing a plan during a window you were eligible for, Medicare gives you a Special Enrollment Period to do it afterward. Keep the notice from your plan, and call us or Medicare before assuming the window is gone.</p>
<h2>How we help</h2>
<p>We work with rural New Mexicans by phone and video, which is how most people out here prefer it. We map the plan&rsquo;s network against the way you actually get care &mdash; the clinic in town, the hospital in the county seat, the specialist in the city, the pharmacy or the mail-order box &mdash; and set an Advantage plan beside a Medigap policy so the trade-off is plain before you sign anything.</p>""",
     faqs=[("I live an hour from the nearest hospital. Which plan type makes sense?", "Often Original Medicare with a Medigap policy, because it has no network: the county hospital, the Albuquerque specialist and an El Paso or Lubbock referral are all covered the same way. An Advantage plan can work if its network genuinely reaches the providers you use; we check that in writing, including the nearest in-network specialists, before you enroll."),
           ("I get my care at an IHS clinic. Do I still need Medicare?", "The IHS says it is not health insurance and that its referral program is the payer of last resort, and it encourages eligible tribal members to enroll in Medicare. Enrolling does not affect your IHS eligibility, it pays the facility for your care, and it covers care the facility cannot provide. Enroll in Part B on time: the late penalty lasts for life."),
           ("Will a Medicare Advantage plan pay my IHS hospital?", "As an in-network provider only if that IHS or tribal facility is in the plan&rsquo;s network, which varies by plan and year. Original Medicare with a Medigap policy has no network to check. We confirm before you enroll."),
           ("Can I use a doctor in El Paso, Lubbock or Denver with a New Mexico plan?", "With Original Medicare and a Medigap policy, yes, anywhere in the country. With an Advantage plan, only if that provider is in the plan&rsquo;s network or the plan covers out-of-network care; we confirm before you enroll.")],
     sources=[SRC_RURAL_PLAN, SRC_CAH, SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_HCGOV_AIAN, SRC_IHS_PRC, SRC_KFF_IHS, SRC_CMS_AIAN, SRC_GIMC, SRC_SEP, SRC_TX_ELPASO, SRC_AZ], cta="Far from a hospital? Let&rsquo;s make sure your plan reaches the care you use."),

dict(slug="veterans", nav_title="Medicare for New Mexico veterans and military retirees", crumb="Veterans", scene="whitesands",
     title="Medicare for New Mexico Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (the Raymond G. Murphy VA in Albuquerque and its community clinics) work with Medicare in New Mexico, why Part B timing matters even with VA care, and which plans fit retirees near Kirtland, Holloman, Cannon and White Sands. From a retired Air Force officer.",
     llm="Medicare for New Mexico veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, VA New Mexico Health Care System, and the retiree communities around Kirtland AFB, Holloman AFB, Cannon AFB and White Sands Missile Range",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for New Mexico veterans and military retirees",
     sub="About 130,000 veterans live in New Mexico, many of them around three Air Force bases and an Army missile range. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "VA New Mexico Health Care System serves New Mexico, southern Colorado and West Texas through the Raymond G. Murphy VA Medical Center in Albuquerque and 13 community-based outpatient clinics.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>New Mexico is home to roughly 130,000 veterans and the retiree communities of Kirtland Air Force Base in Albuquerque, Holloman Air Force Base in Alamogordo, Cannon Air Force Base in Clovis and White Sands Missile Range outside Las Cruces. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; UNM, Presbyterian or the county hospital with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital &mdash; which, in most of New Mexico, is the only hospital within an hour. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>The VA in New Mexico</h2>
<p>VA New Mexico Health Care System runs the Raymond G. Murphy VA Medical Center in Albuquerque &mdash; a teaching hospital with a full range of services &mdash; and 13 community-based outpatient clinics across New Mexico and in Durango, Colorado, serving veterans in New Mexico, southern Colorado and West Texas. For a veteran in Farmington, Roswell or Silver City that usually means primary care at the local clinic and specialty care in Albuquerque; Medicare is what pays when the closer choice is the community hospital instead.</p>
<h2>Military clinics after 65</h2>
<p>The 377th Medical Group at Kirtland, the 49th Medical Group at Holloman and the 27th Special Operations Medical Group at Cannon are outpatient clinics rather than hospitals, and they see retirees under TRICARE rules on a space-available basis; Medicare does not pay there. In Alamogordo, Gerald Champion Regional Medical Center has been shared by Holloman&rsquo;s military community and civilians since 1999. Most New Mexico military retirees pair TFL with civilian care nearby, and we have pages for the three base communities: <a href="/kirtland-afb">Kirtland AFB</a>, <a href="/holloman-afb">Holloman AFB</a> and <a href="/cannon-afb">Cannon AFB</a>. White Sands Missile Range retirees around Las Cruces are covered on our <a href="/las-cruces">Las Cruces page</a>.</p>
<h2>Which New Mexico plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state or across the line in El Paso, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the New Mexico Department of Veterans Services, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care, which matters when the VA clinic is an hour away."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at the Kirtland clinic or the Albuquerque VA?", "No. Medicare does not pay at military or VA facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_VA_NM, SRC_USAFACTS_VET, SRC_KIRTLAND, SRC_HOLLOMAN, SRC_CANNON, SRC_GCRMC, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Turquoise Care (New Mexico Medicaid): Medicare Savings Programs, Extra Help", crumb="Turquoise Care &amp; Medicare Savings Programs", scene="adobe",
     title="Medicare &amp; New Mexico Medicaid: Turquoise Care, QMB, SLMB | ECOS Medicare Solutions",
     desc="How Medicare works with New Mexico Medicaid: Turquoise Care and its four health plans, Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium with no asset test, Extra Help, Dual Special Needs Plans, and where to apply through the Health Care Authority.",
     llm="Medicare and New Mexico Medicaid (dual eligible): Turquoise Care (Health Care Authority, since July 2024), Medicare Savings Programs (QMB/SLMB/QI) with no asset test, Extra Help, D-SNPs, applying through HCA / YesNM",
     eyebrow="Your situation · Dual eligible", h1="Medicare and New Mexico Medicaid: Turquoise Care and the Medicare Savings Programs",
     sub="If you qualify for both Medicare and New Mexico Medicaid &mdash; or just for a Medicare Savings Program, which has no asset test here &mdash; you may pay far less. Here is how it works in New Mexico, and where to apply.",
     keyfacts=["New Mexico Medicaid is <strong>Turquoise Care</strong>, run by the New Mexico Health Care Authority (HCA). It began July 1, 2024, replacing Centennial Care, and members choose among four health plans: Blue Cross and Blue Shield of New Mexico, Presbyterian Health Plan, Molina Healthcare and UnitedHealthcare Community Plan.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. New Mexico eliminated the asset test for all three effective January 1, 2021, so only income counts; income limits change each year. Apply through HCA.",
               "Qualifying for a Medicare Savings Program or Medicaid automatically qualifies you for Extra Help with Part D costs.",
               "Dual Special Needs Plans (D-SNPs) are Advantage plans for people with both Medicare and Medicaid. Presbyterian is keeping its Dual Plus D-SNP even as it drops its other Advantage plans for 2027. Free counseling: New Mexico SHIP, 800-432-2080."],
     body="""<p>Some New Mexicans qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and New Mexico Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in New Mexico</h2>
<p>New Mexico Medicaid is administered by the <strong>New Mexico Health Care Authority (HCA)</strong>, the agency that took over from the Human Services Department in 2024. Its managed-care program is <strong>Turquoise Care</strong>, which replaced Centennial Care on July 1, 2024. Most members, including seniors and people with disabilities, get their Medicaid benefits through one of four health plans &mdash; Blue Cross and Blue Shield of New Mexico, Presbyterian Health Plan, Molina Healthcare of New Mexico and UnitedHealthcare Community Plan &mdash; which coordinate Medicaid services, including long-term services and supports, while Medicare continues to pay first for medical care. Eligibility is determined by HCA, not by an insurance agency; you apply through the state&rsquo;s YesNM portal or an HCA income-support office.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. New Mexico eliminated the resource (asset) test for all three programs effective January 1, 2021, so only your income counts, and the income limits change each year. You apply through HCA, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> are Medicare Advantage plans designed for people with both Medicare and Medicaid; they coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact. In New Mexico several of the Turquoise Care plans&rsquo; parent companies also sell D-SNPs, so the two sides can be aligned; Presbyterian&rsquo;s Dual Plus is the one Advantage plan it is keeping for 2027.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from New Mexico SHIP &mdash; the State Health Insurance Assistance Program, run by the Aging and Long-Term Services Department&rsquo;s Aging and Disability Resource Center &mdash; at 800-432-2080. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Turquoise Care benefits working alongside Medicare. Eligibility decisions rest with HCA and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Turquoise Care, the New Mexico Health Care Authority, or the federal Medicare program.</p>""",
     faqs=[("What is Turquoise Care?", "New Mexico&rsquo;s Medicaid managed-care program, run by the Health Care Authority since July 1, 2024, when it replaced Centennial Care. Members choose one of four health plans &mdash; Blue Cross and Blue Shield of New Mexico, Presbyterian, Molina or UnitedHealthcare Community Plan &mdash; which coordinates Medicaid services while Medicare keeps paying first for medical care."),
           ("Who counts as dual eligible in New Mexico?", "People who qualify for both Medicare and New Mexico Medicaid. There are full and partial categories; eligibility is determined by HCA and CMS, based on income and, for full Medicaid, resources."),
           ("Can New Mexico Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. New Mexico has no asset test for these programs. Apply through HCA; New Mexico SHIP (800-432-2080) can help."),
           ("Where do I apply for Medicaid if I am over 65?", "Through the New Mexico Health Care Authority &mdash; online at the YesNM portal or at an HCA income-support office. HCA says processing can take up to 45 days and it may ask for more documents.")],
     sources=[SRC_HCA_TC, SRC_HCA_PLANS, SRC_HSD_MSP, SRC_ALTSD_SHIP, SRC_FIERCE, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and New Mexico Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in New Mexico", crumb="Chronic SNPs", scene="bosque",
     title="Chronic SNPs (C-SNP) in New Mexico | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in New Mexico: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in New Mexico for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in New Mexico",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by New Mexico county and is concentrated in the Albuquerque area; a regular Advantage plan or a Medigap policy may still serve you better, especially where the specialist is a long drive away.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. In New Mexico, where diabetes and kidney disease are common and dialysis chairs are far apart, the idea is appealing; the network is what decides whether it works.</p>
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist, cardiologist or dialysis center is in it &mdash; and how far away the in-network one is &mdash; applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Turquoise Care.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in New Mexico?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in New Mexico", crumb="Institutional SNPs", scene="sandia",
     title="Institutional SNPs (I-SNP) in New Mexico | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in New Mexico for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Turquoise Care.",
     llm="Institutional Special Needs Plans (I-SNP) in New Mexico for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in New Mexico",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In New Mexico, many people in long-term care also qualify for Medicaid through Turquoise Care; a D-SNP aligned with the Turquoise Care plan may then be the better fit, and we compare the two."],
     body="""<p>An Institutional Special Needs Plan (I-SNP) is a Medicare Advantage plan for people who live in &mdash; or are expected to need the level of care provided by &mdash; an institution such as a nursing facility, or who need that level of care while living at home.</p>
<h2>Who an I-SNP is for</h2>
<ul>
<li>People who have lived, or are expected to live, in a qualifying facility (such as a skilled nursing or long-term care facility) for 90 days or more.</li>
<li>People who require an institutional level of care, sometimes provided at home, as confirmed by a state-approved assessment.</li>
</ul>
<h2>How it works</h2>
<ul>
<li><strong>On-site care coordination.</strong> I-SNPs typically bring care management to where the member lives, often with nurse practitioners or care teams who work directly with facility staff, which can mean fewer hospital transfers &mdash; a real consideration when the hospital is an hour away.</li>
<li><strong>Included Part D coverage</strong> and benefits designed around higher-needs care.</li>
<li><strong>Coordination with families</strong> on care decisions and transitions.</li>
</ul>
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP aligned with Turquoise Care</a> if Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Turquoise Care &amp; the Medicare Savings Programs</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your New Mexico county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with Turquoise Care.")],
     sources=[SRC_MA_GOV, SRC_HCA_TC], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="sandia",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed New Mexico agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed New Mexico agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling land, a year of royalties, a lab retirement payout or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed, and the rules for public employees whose careers were outside Social Security.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in New Mexico, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in New Mexico. The book answers the wider one &mdash; the decisions that arrive between 62 and 75.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to New Mexico?", "The book covers Medicare and retirement decisions nationally. For New Mexico specifics &mdash; county-by-county Advantage menus, Turquoise Care, the 2027 birthday rule, the IHS, the base communities &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
