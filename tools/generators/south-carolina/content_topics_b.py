"""South Carolina topic pages, part B: turning 65, moving to South Carolina (with hurricanes), veterans, Medicaid, SNPs, the free guide."""
from content_topics_a import (SRC_CMS, SRC_COSTS, SRC_MA_GOV, SRC_MEDIGAP_GOV, SRC_SEP, SRC_CMS_HURR, SRC_SCDOI, SRC_SCDOI_GUIDE, SRC_ICARE, SRC_ICARE_CMS,
                              SRC_MRO, SRC_HIO_SC, SRC_MMR_SC, SRC_MMR_T65, SRC_MMR_SWITCH, SRC_SCDHHS_APPLY, SRC_SCDHHS_ELIG, SRC_PRIME, SRC_SNP,
                              SRC_TFL, SRC_VA, SRC_VA_CHS, SRC_VA_COLA, SRC_NOVANT, SRC_NCDOI_HELENE, SRC_MEDICAID_HELENE)
SRC_FL_NEW = ("Florida Medicare Enrollment (sister section): moving to Florida on Medicare", "https://www.ecosinsurancesolutions.com/florida/new-to-florida")
SRC_MN_SNOW = ("Minnesota Medicare Enrollment (sister section): Medicare for Minnesota snowbirds", "https://www.ecosinsurancesolutions.com/minnesota/snowbirds")

TOPICS_B = [
dict(slug="turning-65", nav_title="Turning 65 in South Carolina guide", crumb="Turning 65", scene="battery",
     title="Turning 65 in South Carolina: Medicare Guide [[YEAR]] | ECOS Medicare Solutions",
     desc="Turning 65 in South Carolina: your 7-month enrollment window, the Medigap open enrollment that does not repeat, still-working rules, the deadlines with lifelong penalties, and a checklist. Free help from a licensed South Carolina agent.",
     llm="Turning 65 in South Carolina: enrollment windows, the parts of Medicare, the choice between Advantage and Medigap by county, no birthday rule, deadlines with lifelong penalties, and a checklist",
     eyebrow="Guide · New to Medicare", h1="Turning 65 in South Carolina: your Medicare starter guide",
     sub="What to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; written for South Carolina, where the right answer in Greenville County is not always the right answer in Hampton County, and the Medigap window does not come back.",
     keyfacts=["Your Initial Enrollment Period is 7 months: the 3 months before your birthday month, the month itself, and the 3 months after. Enroll in the first 3 to avoid a gap.",
               "Your Medigap open enrollment is a separate 6-month window that starts when you are 65 and have Part B. In South Carolina it does not repeat: there is no birthday rule and no annual switching window.",
               "Still working with qualifying employer coverage (generally 20+ employees)? You can usually delay Part B without penalty and get a Special Enrollment Period later. PEBA retirees have their own rules.",
               "Miss Part B or Part D without creditable coverage and the penalty lasts for life: 10% per 12 months for Part B; about 1% per month for Part D."],
     body="""<p>Turning 65 comes with a stack of Medicare mail and a few decisions that matter for the rest of your life. Here is the plain-English version &mdash; what to do, when, and which deadlines you really don&rsquo;t want to miss &mdash; with the South Carolina twists that most guides leave out. When you are ready, we walk through your specific options at no cost.</p>
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
<caption>The two ways most South Carolinians put their coverage together.</caption>
<thead><tr><th scope="col">Path</th><th scope="col">What it looks like</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare + extras</th><td>Parts A &amp; B, usually plus a <a href="/medicare-supplement">Medigap policy</a> (Plan G or N) and a standalone <a href="/part-d">Part D</a> plan. Any provider nationwide that accepts Medicare; predictable costs; monthly premiums.</td></tr>
<tr><th scope="row">Medicare Advantage</th><td>A single <a href="/medicare-advantage">Part C</a> plan that bundles everything, often $0 premium, with extras like dental and vision &mdash; using a county-based network that changes yearly.</td></tr>
</tbody></table>
<p>Where you live tilts the answer. In Greenville, Columbia, Charleston or Horry County the Advantage menu is deep and the networks include most of the big systems. In the rural counties of the Pee Dee, the Savannah River valley or the Lowcountry between Charleston and Beaufort, the menu is shorter, the drive to a hospital is longer, and a Medigap policy&rsquo;s any-provider access is often the practical choice. If MUSC, Prisma, Duke or Emory is in your future, a supplement removes the network question entirely. Military retirees with TRICARE For Life are a third case; see <a href="/veterans">Veterans</a>.</p>
<p>If you lean toward a supplement, there is a second deadline that is easy to miss: your Medigap open enrollment is its own six-month window, separate from the seven-month one above, and in South Carolina it does not repeat. Our research site sets the two side by side &mdash; <a href="https://www.mymedigaprate.com/turning-65/south-carolina">turning 65 in South Carolina</a>.</p>
<h2>4. Deadlines that carry lifelong penalties</h2>
<div class="note-box"><p><strong>Part B late penalty.</strong> If you don&rsquo;t enroll in Part B when first eligible (and don&rsquo;t have qualifying employer coverage), a permanent penalty of 10% per 12 months is added to your premium for life.</p>
<p><strong>Part D late penalty.</strong> Going 63+ days without creditable drug coverage can add a permanent surcharge to your Part D premium.</p>
<p><strong>Medigap open enrollment.</strong> Your six-month Medigap open enrollment begins when you are 65 <em>and</em> enrolled in Part B &mdash; during it no South Carolina insurer can turn you down or charge more for your health. Afterward, South Carolina insurers can use medical underwriting, and there is no birthday rule to fall back on.</p></div>
<h2>5. Still working at 65?</h2>
<p>If you (or your spouse) have qualifying employer coverage, you may be able to delay Part B without penalty and get a Special Enrollment Period when that coverage ends. The rules depend on employer size (20 or more employees is the usual line) and whether the drug coverage is creditable. South Carolina&rsquo;s big employers &mdash; the state and its universities, the school districts, the health systems, the manufacturers along I-85, the port &mdash; generally qualify; a small business, a retiree plan, or COBRA may not. It is worth a quick conversation before you decide, and a form (CMS-L564) from your employer when you do enroll. State and school-district retirees covered through PEBA have their own Medicare rules; ask us.</p>
<h2>6. A simple checklist</h2>
<ul>
<li>Mark your 7-month IEP on the calendar (it starts 3 months before your birthday month).</li>
<li>Decide on Part B based on whether you have other creditable coverage.</li>
<li>Find out how deep the Advantage menu is in your county, and whether it changed for [[YEAR]].</li>
<li>Choose your path: Original Medicare + Medigap + Part D, or Medicare Advantage.</li>
<li>Check that your doctors and prescriptions are covered before you enroll &mdash; especially if a specific system is your care.</li>
<li>If you split the year, or you just arrived, read <a href="/new-to-south-carolina">moving to South Carolina</a> first; if you are a veteran, see how <a href="/veterans">TRICARE or VA benefits</a> coordinate; if you have Medicaid, see <a href="/medicaid">Healthy Connections and the D-SNPs</a>.</li>
<li>Estimate your costs on our <a href="/medicare-costs">[[YEAR]] costs &amp; IRMAA page</a>.</li>
</ul>
<p>None of this has to be done alone. We help South Carolinians sort through it every day &mdash; clearly, patiently, and at no cost to you. I-CARE (800-868-9095), the state&rsquo;s free counseling program run by the Department on Aging, offers unbiased help as well.</p>""",
     faqs=[("When should I sign up for Medicare if I&rsquo;m turning 65?", "During your Initial Enrollment Period &mdash; the seven months that span the three months before your birthday month, your birthday month, and the three months after. Signing up in the first three months means coverage starts on the first of your birthday month."),
           ("Do I have to take Part B at 65 if I&rsquo;m still working?", "Not always. If you have qualifying employer coverage (generally from an employer with 20 or more employees), you may delay Part B without penalty and get a Special Enrollment Period later. The rules depend on the employer&rsquo;s size, so confirm before you decide."),
           ("Is it better to get Medicare Advantage or Original Medicare with Medigap in South Carolina?", "Neither is automatically better &mdash; it depends on your doctors, prescriptions, travel, budget and county. The Advantage menu is deep in the metros and along the coast and thinner in the rural counties. We compare both with you so the choice fits your life."),
           ("What is different about turning 65 in South Carolina?", "Your Medigap open enrollment does not repeat here &mdash; South Carolina has no birthday rule &mdash; so using it well matters more than in some states. Your county decides how many Advantage plans you can choose from. And a large share of South Carolinians reach 65 with TRICARE For Life or VA care, or arrive here already on Medicare, which changes the calculation.")],
     sources=[SRC_CMS, SRC_SCDOI, SRC_ICARE, SRC_MMR_T65], cta="Turning 65? Let&rsquo;s talk it through before the window closes.", about="Medicare enrollment for people turning 65 in South Carolina"),

dict(slug="new-to-south-carolina", nav_title="Moving to South Carolina on Medicare: the relocation SEP, Medigap across state lines, snowbirds and hurricane season", crumb="New to South Carolina", scene="pier",
     title="Moving to South Carolina on Medicare: Relocation SEP, Medigap &amp; Hurricanes | ECOS Medicare Solutions",
     desc="Retiring to Hilton Head, Bluffton, Myrtle Beach, Mount Pleasant or Fort Mill? What a move does to your Medicare: the relocation Special Enrollment Period, the guaranteed-issue Medigap window if you leave an Advantage plan, plans that travel, and what a hurricane declaration changes.",
     llm="Moving to South Carolina on Medicare: the two-month relocation Special Enrollment Period, the federal guaranteed-issue Medigap right when you leave an Advantage plan's service area, what happens to an out-of-state Medigap policy, snowbirds and half-backs, and the FEMA hurricane disaster SEP",
     eyebrow="Guide · New to South Carolina", h1="Moving to South Carolina on Medicare, and living on a hurricane coast",
     sub="Sun City Hilton Head, Bluffton, the Grand Strand, Mount Pleasant, Fort Mill: a lot of South Carolina&rsquo;s Medicare population arrived already on Medicare. Here is what the move does to your coverage &mdash; and what a hurricane declaration does to your deadlines once you are here.",
     keyfacts=["A permanent move opens a Special Enrollment Period to join a Medicare Advantage or Part D plan sold in your new county. Tell your old plan before you move and the window runs from the month before the move through two months after; tell it afterward and you get two full months from when you tell it.",
               "Leaving a Medicare Advantage plan because you moved out of its service area is a federal guaranteed-issue event: you can buy certain Medigap plans without health questions, generally within 63 days of the old coverage ending. Arriving here on an Advantage plan is your one clean door into a supplement, because South Carolina has no birthday rule.",
               "A Medigap policy from another state keeps working in South Carolina &mdash; it has no network and no service area &mdash; though the premium may be re-rated to your new address. Original Medicare never changes.",
               "If a FEMA-declared hurricane emergency or major disaster kept you from making an enrollment decision during a valid window, Medicare gives you a Special Enrollment Period afterward. Helene in 2024 triggered it for South Carolina counties."],
     body="""<p>South Carolina is one of the country&rsquo;s big retirement destinations: the Lowcountry around Hilton Head and Bluffton, the Grand Strand from Myrtle Beach to Georgetown, the Charleston suburbs, the York County towns south of Charlotte, and the lake country around Columbia and Greenville. Many of the people we help did not turn 65 here; they arrived here on Medicare from Ohio, New York, New Jersey, Pennsylvania or Florida. The Medicare rules for a move are not complicated, but they are unforgiving, so here they are plainly.</p>
<h2>What moves with you, and what does not</h2>
<table class="ctable">
<caption>How each part of your coverage behaves when your permanent address changes to South Carolina.</caption>
<thead><tr><th scope="col">Coverage</th><th scope="col">After the move</th><th scope="col">What to do</th></tr></thead>
<tbody>
<tr><th scope="row">Original Medicare (A and B)</th><td>Unchanged; it is federal</td><td>Update your address with Social Security</td></tr>
<tr><th scope="row">Medigap policy</th><td>Keeps working &mdash; no network, no service area; premium may be re-rated to South Carolina</td><td>Tell the carrier your new address; compare South Carolina prices while you are at it</td></tr>
<tr><th scope="row">Medicare Advantage plan</th><td>Tied to your old county; ends when you leave its service area</td><td>Use the relocation SEP to pick a plan sold here, or return to Original Medicare and use the guaranteed-issue Medigap window</td></tr>
<tr><th scope="row">Standalone Part D plan</th><td>Tied to your old region; ends when you leave</td><td>Use the relocation SEP to pick a plan sold here, checked against your pharmacy</td></tr>
</tbody></table>
<h2>The relocation Special Enrollment Period</h2>
<p>Medicare Advantage and Part D plans are sold by county, and you must live in the plan&rsquo;s service area. A permanent move outside it gives you a Special Enrollment Period to join a plan where you live now. If you tell your old plan <em>before</em> you move, the window opens the month before the move and runs two full months after it; if you tell it afterward, you get two full months from the month you tell it. What counts is your permanent residence &mdash; the address on your driver&rsquo;s licence and your tax return &mdash; not a five-month stay at the beach.</p>
<h2>The Medigap door that opens when you leave an Advantage plan</h2>
<p>This is the part most people miss. Federal rules give you a <strong>guaranteed-issue right</strong> to buy certain Medigap plans without medical underwriting when you leave a Medicare Advantage plan because you moved out of its service area. The window is short &mdash; generally 63 days after the old coverage ends &mdash; and in South Carolina it is worth more than in a birthday-rule state, because once it closes the only other way into a supplement is medical underwriting. If you are arriving on an Advantage plan and have any thought of a Medigap policy, decide before the window closes, not after your first winter. The state-by-state rules are on <a href="https://www.mymedigaprate.com/switching-medigap-plans">switching Medigap plans</a>.</p>
<div class="note-box"><p><strong>Keeping a Medigap policy from another state.</strong> A supplement issued in Pennsylvania or New York stays in force here; it pays alongside Original Medicare wherever you are. The carrier may re-rate the premium to your new ZIP code, up or down. Because South Carolina has no birthday rule, switching to a cheaper South Carolina carrier later means answering health questions, so the time to compare is now, while you are healthy enough to pass underwriting, or during the guaranteed-issue window if you have one. Our research site publishes each carrier&rsquo;s <a href="https://www.mymedigaprate.com/medigap-rate-history/south-carolina">South Carolina rate filings</a>.</p></div>
<h2>Snowbirds, half-backs and two homes</h2>
<p>Plenty of people keep a place here and a place elsewhere, and plenty of Florida retirees move &ldquo;halfway back&rdquo; to the Carolinas. The rule is the same in both directions: a Medigap policy with Original Medicare works with any provider in the country that accepts Medicare, in both states, all year. Most Advantage HMOs cover only emergencies and urgent care outside their service area; some PPOs cover routine care out of network at higher cost; a few plans carry a travel benefit for extended stays. If travel is the reason you are choosing an Advantage plan, we get the benefit in writing from the Evidence of Coverage before you enroll. Our <a href="https://www.ecosinsurancesolutions.com/florida/new-to-florida">Florida section</a> and <a href="https://www.ecosinsurancesolutions.com/minnesota/snowbirds">Minnesota section</a> cover the same question from the other end.</p>
<h2>Hurricane season and your Medicare</h2>
<p>Once you live on the coast, storms are part of the calendar. Medicare has a set of rules that switch on when the President or FEMA declares an emergency or major disaster, and they are worth knowing in June rather than in October.</p>
<ul>
<li><strong>The disaster Special Enrollment Period.</strong> If you were eligible to make a Medicare enrollment decision during a valid window &mdash; the Annual Election Period, the Medicare Advantage Open Enrollment Period, your Initial Enrollment Period, or another Special Enrollment Period &mdash; and a FEMA-declared emergency or major disaster kept you from making it, you get a Special Enrollment Period to make that decision afterward. It applies to people who live in the declared counties and to people who rely on someone in those counties to help them enroll. It does not give you a second bite at a decision you made on time; it gives you the bite you missed. Hurricane Helene in September 2024 brought a public health emergency and disaster declarations to South Carolina counties, and the SEP with them.</li>
<li><strong>Early refills.</strong> Once an emergency is declared for your area, Part D plans must allow early refills, cover fills at out-of-network pharmacies when yours is closed, and relax prior-authorization rules for medications you already take. Get a refill as soon as a hurricane <em>watch</em> is posted; pharmacies close before the warning.</li>
<li><strong>Care when you evacuate.</strong> Original Medicare and a Medigap policy work anywhere in the country, so an evacuee in Atlanta or Charlotte is covered as if at home. Medicare Advantage plans, during a declared disaster, must cover care from out-of-network providers at in-network cost-sharing when in-network care is unavailable and must waive referral requirements. That protection ends when the declaration does.</li>
</ul>
<h2>Becoming a South Carolinian on paper</h2>
<p>When the move is permanent &mdash; licence, voter registration, tax return &mdash; you choose from the plans sold in your new county, and the menu in Beaufort or Horry County is not the menu you left. Our agency is licensed in South Carolina and fifteen other states, including North Carolina, Georgia, Ohio and Minnesota, so we can move your coverage cleanly in either direction; for Florida, our Florida section&rsquo;s own licensed agent takes over.</p>""",
     faqs=[("I moved to South Carolina from an Advantage plan. Can I get a Medigap policy without health questions?", "In most cases, yes. Leaving an Advantage plan because you moved out of its service area is a federal guaranteed-issue event: you can buy certain Medigap plans without underwriting, generally within 63 days of the old coverage ending. South Carolina has no birthday rule afterward, so decide inside the window."),
           ("Does my Medigap policy from another state work in South Carolina?", "Yes. A Medigap policy pays alongside Original Medicare with any provider in the country that accepts Medicare, with no network and no service area. Tell the carrier your new address; the premium may be re-rated to South Carolina."),
           ("How long do I have to pick a new Advantage or Part D plan after I move?", "If you tell your old plan before the move, the Special Enrollment Period runs from the month before the move through two full months after it. If you tell it afterward, you get two full months from the month you tell it."),
           ("I missed the Annual Election Period because of a hurricane. Can I still change plans?", "If you lived in a county under a FEMA emergency or major disaster declaration during the election period, or relied on someone who did, you get a Special Enrollment Period to make the election you missed. Call your plan, 1-800-MEDICARE or us and name the storm and the county."),
           ("Can you help me if I split the year between South Carolina and Florida or up north?", "Yes. Our agency is licensed in South Carolina and fifteen other states, including North Carolina, Georgia, Ohio and Minnesota, so we can compare which of your plans travels and move your coverage cleanly when a stay becomes a move. Florida is served by our Florida section&rsquo;s own licensed agent.")],
     sources=[SRC_SEP, SRC_MEDIGAP_GOV, SRC_MA_GOV, SRC_CMS_HURR, SRC_NCDOI_HELENE, SRC_MEDICAID_HELENE, SRC_MMR_SWITCH, SRC_MMR_SC, SRC_FL_NEW, SRC_MN_SNOW], cta="Just moved, or about to? Let&rsquo;s make sure the move does not cost you a window.", about="Moving to South Carolina on Medicare and Medicare rules during FEMA-declared disasters"),

dict(slug="veterans", nav_title="Medicare for South Carolina veterans and military retirees", crumb="Veterans", scene="harbor",
     title="Medicare for South Carolina Veterans: TRICARE For Life &amp; VA | ECOS Medicare Solutions",
     desc="How TRICARE For Life and VA care (the Ralph H. Johnson VA in Charleston, the Dorn VA in Columbia) work with Medicare in South Carolina, why Part B timing matters even with VA care, and when an MA-only plan adds dental and vision. From a retired Air Force officer.",
     llm="Medicare for South Carolina veterans and military retirees: TRICARE For Life vs VA coordination, the Part B timing mistake, the Charleston and Columbia VA systems, and the retiree communities around Joint Base Charleston, Shaw AFB, Fort Jackson and Beaufort",
     eyebrow="Your situation · Veterans &amp; military retirees", h1="Medicare for South Carolina veterans and military retirees",
     sub="Joint Base Charleston, Shaw, Fort Jackson, Parris Island and the Beaufort air station all retire people here, and two VA health care systems serve them. How TRICARE For Life and VA health care each work with Medicare &mdash; explained by a retired Air Force officer who has been through the paperwork himself.",
     keyfacts=["TRICARE For Life requires Medicare Part A and Part B and pays secondary to Medicare. Its pharmacy is creditable, so a separate Part D plan is usually unnecessary, and a Medigap policy usually is too.",
               "VA health care does not coordinate with Medicare. VA medical coverage is <strong>not</strong> creditable for Part B, so delaying Part B because you have VA care can trigger a lifelong penalty; VA pharmacy <strong>is</strong> creditable for Part D.",
               "South Carolina VA care runs through the Ralph H. Johnson VA Health Care System in Charleston &mdash; with clinics in Beaufort, North Charleston, Goose Creek and Myrtle Beach &mdash; and the Columbia VA Health Care System anchored by the Wm. Jennings Bryan Dorn VA Medical Center.",
               "With TRICARE For Life, an MA-only plan (Advantage without drug coverage) can add dental or vision without duplicating your prescription benefit."],
     body="""<p>South Carolina retires a lot of military families: Air Force and Navy retirees around Joint Base Charleston, Air Force retirees from Shaw around Sumter, Army retirees from Fort Jackson around Columbia, and Marines from Parris Island and the Beaufort air station across the Lowcountry. How your military benefits coordinate with Medicare depends a lot on <em>which</em> benefit you have.</p>
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
<li>Having both Medicare and VA gives you <strong>more places to get care</strong> &mdash; MUSC or Prisma with Medicare, the VA for service-connected care and prescriptions.</li>
</ul></div>
</div>
<div class="note-box"><p><strong>The mistake we most want you to avoid:</strong> skipping Part B because you have VA care. Because VA medical coverage isn&rsquo;t creditable for Part B, delaying it can trigger a penalty that lasts as long as you have Medicare, and it leaves you with no coverage at a non-VA hospital. If you are approaching 65 with VA benefits, talk to us about timing first.</p></div>
<h2>The two VA systems</h2>
<p>The <strong>Ralph H. Johnson VA Health Care System</strong> in Charleston serves the coast &mdash; more than 100,000 veterans across a 22-county area of South Carolina and Georgia &mdash; through the medical center on Bee Street and community clinics in Beaufort, North Charleston, Goose Creek and Myrtle Beach. The <strong>Columbia VA Health Care System</strong>, anchored by the Wm. Jennings Bryan Dorn VA Medical Center, serves the Midlands, the Upstate and the Pee Dee. Veterans in Aiken and Edgefield counties often use the VA across the river in Augusta.</p>
<h2>Military clinics after 65</h2>
<p>The clinics at Joint Base Charleston, Shaw, Fort Jackson and the Beaufort installations continue to see retirees on a space-available basis under TRICARE rules; Medicare does not pay there, and none of them is a substitute for a civilian hospital. Most South Carolina military retirees pair TFL with civilian care nearby, and we have pages for the three largest retiree communities: <a href="/joint-base-charleston">Joint Base Charleston</a>, <a href="/shaw-afb">Shaw Air Force Base</a> and <a href="/fort-jackson">Fort Jackson</a>. Beaufort&rsquo;s Marine community is covered on our <a href="/beaufort">Beaufort page</a>.</p>
<h2>Which South Carolina plan fits a veteran</h2>
<ul>
<li><strong>VA care plus Original Medicare and a Medigap policy</strong> gives the widest choice: any hospital in the state, no network question, VA pharmacy for drugs. Many veterans skip Part D entirely because the VA pharmacy is creditable &mdash; keep the VA&rsquo;s letter as proof.</li>
<li><strong>VA care plus a $0-premium Advantage plan</strong> is common and can work, as long as you understand the network limits and that the VA and the plan will not coordinate a single bill.</li>
<li><strong>TFL plus an MA-only plan</strong> for dental, vision and hearing, if the extras are worth it and the network reaches your doctors.</li>
</ul>
<h2>How we help</h2>
<p>We look at exactly which benefits you carry, confirm your Part B timing, decide whether a separate drug plan adds anything, and &mdash; if it makes sense &mdash; compare an MA-only or Medigap option for the gaps. Darin served 22 years in the Air Force and retired as an officer; he has filled out the same forms you are looking at.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not affiliated with or endorsed by the U.S. Department of Veterans Affairs, the Department of Defense, the TRICARE program, the South Carolina Department of Veterans&rsquo; Affairs, or the federal Medicare program.</p>""",
     faqs=[("I have VA health care. Do I need Medicare Part B?", "In most cases, yes &mdash; enroll on time. VA medical coverage is not considered creditable for Part B, so delaying Part B can cause a permanent late penalty. Having both VA and Medicare gives you more options for where to get care."),
           ("With TRICARE For Life, do I need a Part D drug plan or a Medigap policy?", "Usually neither. TRICARE For Life pharmacy is creditable drug coverage, and TFL already pays secondary to Medicare, filling the gaps a supplement would. That is also why an MA-only plan can make sense if you want dental or vision."),
           ("Does Medicare pay at the Charleston VA or the Fort Jackson clinic?", "No. Medicare does not pay at VA or military facilities, and they do not cover Medicare cost-sharing. They operate separately, which is why many veterans keep both."),
           ("Is VA pharmacy coverage enough to avoid the Part D penalty?", "Yes. VA prescription coverage is creditable for Part D, so you can skip a Part D plan without a penalty as long as you keep it. Keep the VA&rsquo;s notice of creditable coverage in case you enroll in Part D later.")],
     sources=[SRC_TFL, SRC_VA, SRC_VA_CHS, SRC_VA_COLA, SRC_CMS], cta="Let&rsquo;s sort out your benefits together, veteran to veteran.", about="Medicare for veterans"),

dict(slug="medicaid", nav_title="Medicare + Healthy Connections Medicaid: Medicare Savings Programs, Extra Help, D-SNPs after Healthy Connections Prime", crumb="Healthy Connections Medicaid &amp; D-SNPs", scene="cotton",
     title="Medicare &amp; Healthy Connections Medicaid in South Carolina: QMB, SLMB, D-SNPs | ECOS Medicare Solutions",
     desc="How Medicare works with South Carolina's Healthy Connections Medicaid: Medicare Savings Programs (QMB, SLMB, QI) that pay the Part B premium, Extra Help, the Dual Special Needs Plans that replaced Healthy Connections Prime on January 1, 2026, and where to apply (apply.scdhhs.gov).",
     llm="Medicare and South Carolina Medicaid (dual eligible): Healthy Connections Medicaid run by SCDHHS, Medicare Savings Programs (QMB/SLMB/QI), Extra Help, the end of Healthy Connections Prime on December 31, 2025 and the move to D-SNPs, applying at apply.scdhhs.gov",
     eyebrow="Your situation · Dual eligible", h1="Medicare and Healthy Connections Medicaid: the Medicare Savings Programs and the D-SNPs that replaced Prime",
     sub="If you qualify for both Medicare and South Carolina Medicaid &mdash; or just for a Medicare Savings Program &mdash; you may pay far less. Here is how it works in South Carolina after the end of Healthy Connections Prime, and where to apply.",
     keyfacts=["South Carolina Medicaid is called Healthy Connections and is administered by the South Carolina Department of Health and Human Services (SCDHHS). Apply online at apply.scdhhs.gov or through a county eligibility office.",
               "Medicare Savings Programs (QMB, SLMB, QI) pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles and copays. SCDHHS considers you for QMB first, then SLMB, then QI. Qualifying for any of them automatically qualifies you for Extra Help with Part D costs.",
               "Healthy Connections Prime, the state&rsquo;s Medicare-Medicaid plan for people 65 and over, ended on December 31, 2025. People with both Medicare and Medicaid now use Dual Special Needs Plans (D-SNPs); SCDHHS partners with the plans that offer them.",
               "Free counseling on all of it: I-CARE, South Carolina&rsquo;s SHIP, 800-868-9095."],
     body="""<p>Some South Carolinians qualify for both Medicare and Medicaid &mdash; often called being &ldquo;dual eligible.&rdquo; When that happens, <strong>Medicare pays first</strong>, and Healthy Connections Medicaid may help with costs Medicare leaves behind, like premiums, deductibles and coinsurance, plus services Medicare does not cover at all, such as long-term care at home or in a nursing facility.</p>
<h2>How Medicaid works for seniors in South Carolina</h2>
<p>South Carolina Medicaid is <strong>Healthy Connections</strong>, administered by the <strong>South Carolina Department of Health and Human Services (SCDHHS)</strong>. South Carolina has not expanded Medicaid, so for adults 65 and over eligibility is based on income and resources under the state&rsquo;s aged, blind and disabled rules, and it is determined by SCDHHS &mdash; not by an insurance agency. You apply online at <strong>apply.scdhhs.gov</strong> or through your county eligibility office, and annual reviews can be completed the same way.</p>
<h2>What changed on January 1, 2026: the end of Healthy Connections Prime</h2>
<p>For a decade South Carolina ran <strong>Healthy Connections Prime</strong>, a Medicare-Medicaid plan that combined both programs in one card for people 65 and over. Under federal guidance, Prime ended on December 31, 2025. Members were encouraged to choose a <strong>Dual Special Needs Plan (D-SNP)</strong> &mdash; a Medicare Advantage plan built for people with both Medicare and Medicaid &mdash; and some were moved automatically to a D-SNP offered by their Prime plan&rsquo;s company. SCDHHS now partners with the health plans that offer D-SNPs so that the Medicare and Medicaid sides can be aligned. If you were in Prime and have not looked at your coverage since, this fall&rsquo;s Annual Election Period is the time.</p>
<h2>Programs that can lower your costs</h2>
<ul>
<li><strong>Medicare Savings Programs (MSPs)</strong> &mdash; QMB, SLMB and QI &mdash; pay the Part B premium ($202.90 in [[YEAR]]) and, for QMB, Medicare&rsquo;s deductibles, copays and coinsurance as well. Income limits change each year and are published by SCDHHS; if you do not qualify for QMB, SCDHHS automatically considers you for SLMB, then QI. You apply through SCDHHS, and you do not have to be on full Medicaid to qualify.</li>
<li><strong>Extra Help (Low-Income Subsidy)</strong> lowers what you pay for Part D premiums, deductibles and copays. If you qualify for an MSP or Medicaid you get Extra Help automatically; otherwise apply through Social Security.</li>
<li><strong>Dual Special Needs Plans (D-SNPs)</strong> coordinate the two programs, usually at $0 plan premium, and often add extras while keeping your Medicaid benefits intact. Which D-SNPs are sold in your county changes each year; we compare the ones offered where you live.</li>
</ul>
<p style="font-size:.92rem;color:var(--ink-soft)">Free, unbiased state counseling on all of this is available from I-CARE &mdash; Insurance Counseling Assistance and Referrals for Elders, South Carolina&rsquo;s State Health Insurance Assistance Program, run by the Department on Aging through your regional Area Agency on Aging &mdash; at 800-868-9095. When you are ready to talk through the Medicare side, we are here at <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>.</p>
<h2>How we help</h2>
<p>We help you understand whether a D-SNP is available and a good fit where you live, how a Medicare Savings Program and Extra Help could reduce your costs, and how to keep your Medicaid benefits working alongside Medicare. Eligibility decisions rest with SCDHHS and CMS; our job is to make the Medicare side clear.</p>
<p style="font-size:.95rem;color:var(--ink-soft)">ECOS Medicare Solutions is a private insurance agency and is not connected with or endorsed by Healthy Connections Medicaid, the South Carolina Department of Health and Human Services, or the federal Medicare program.</p>""",
     faqs=[("What happened to Healthy Connections Prime?", "Healthy Connections Prime, South Carolina&rsquo;s Medicare-Medicaid plan for people 65 and over, ended on December 31, 2025 under federal guidance. Members were encouraged to switch to a Dual Special Needs Plan, and some were moved automatically to a D-SNP from their Prime plan&rsquo;s company. If you have not reviewed your new plan, do it this fall."),
           ("Who counts as dual eligible in South Carolina?", "People who qualify for both Medicare and Healthy Connections Medicaid. There are full and partial categories; eligibility is determined by SCDHHS and CMS, based on income and resources."),
           ("Can South Carolina Medicaid pay my Part B premium?", "Possibly. The Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people who qualify, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply at apply.scdhhs.gov; I-CARE (800-868-9095) can help."),
           ("Where do I apply for Medicaid if I am over 65?", "Online at apply.scdhhs.gov or through your county SCDHHS eligibility office. South Carolina has not expanded Medicaid, so eligibility for seniors follows the aged, blind and disabled rules.")],
     sources=[SRC_PRIME, SRC_SNP, SRC_SCDHHS_APPLY, SRC_SCDHHS_ELIG, SRC_ICARE, SRC_CMS], cta="Let&rsquo;s check what you qualify for.", about="Medicare and South Carolina Medicaid dual eligibility"),

dict(slug="chronic-snp", nav_title="Chronic Special Needs Plans (C-SNP) in South Carolina", crumb="Chronic SNPs", scene="foothills",
     title="Chronic SNPs (C-SNP) in South Carolina | ECOS Medicare Solutions",
     desc="Chronic Special Needs Plans in South Carolina: which conditions qualify, what a C-SNP offers, and whether one beats a regular Advantage plan or a Medigap policy for you.",
     llm="Chronic Special Needs Plans (C-SNP) in South Carolina for qualifying chronic conditions",
     eyebrow="Your situation · Chronic conditions", h1="Chronic Special Needs Plans (C-SNPs) in South Carolina",
     sub="Medicare Advantage plans built around one chronic condition &mdash; diabetes, heart disease, lung disease, kidney failure &mdash; with care coordination and a drug list to match.",
     keyfacts=["A C-SNP is a Medicare Advantage plan limited to people with a specific qualifying chronic condition, verified by a provider.",
               "It includes Part D, usually a formulary built around the condition, and care coordination; premiums are often $0 or low.",
               "Availability varies by South Carolina county and is concentrated in the metros and along the coast; a regular Advantage plan or a Medigap policy may still serve you better.",
               "You can enroll in a C-SNP outside the normal windows when you are first diagnosed or first qualify."],
     body="""<p>A Chronic Special Needs Plan (C-SNP) is a type of Medicare Advantage plan built for people living with a specific severe or disabling chronic condition. Instead of a one-size-fits-all plan, a C-SNP shapes its provider network, drug list and care coordination around that condition. South Carolina, with high rates of diabetes and heart disease, has C-SNPs in many of its larger counties.</p>
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
<div class="note-box"><p><strong>Is it the right move?</strong> A C-SNP can be a strong fit if your care centers on one chronic condition and you want coordinated support. But it is still a network plan, so the question of whether your endocrinologist or cardiologist at MUSC, Prisma or McLeod is in it applies, and a regular Medicare Advantage plan or a <a href="/medicare-supplement">Medigap policy</a> may serve you better depending on your doctors and other needs. We compare them with you &mdash; no cost, no pressure.</p></div>
<p>Related: <a href="/institutional-snp">Institutional SNPs (I-SNPs)</a> for facility-level care, and <a href="/medicaid">Dual SNPs</a> for people with both Medicare and Healthy Connections Medicaid.</p>""",
     faqs=[("Who can join a Chronic Special Needs Plan in South Carolina?", "People with Medicare Parts A and B who have a qualifying chronic condition, confirmed by a provider, and who live in the plan&rsquo;s service area. Availability varies by county and changes each plan year."),
           ("Does a C-SNP include drug coverage?", "Yes. C-SNPs are Medicare Advantage plans that include Part D prescription coverage, usually with a formulary tailored to the plan&rsquo;s target condition."),
           ("How much does your help cost?", "Nothing. Independent agents are paid by the carriers when you enroll, so comparing plans is free to you.")],
     sources=[SRC_MA_GOV], cta="Let&rsquo;s see whether a C-SNP fits your condition.", about="Chronic Special Needs Plans", priority="0.6"),

dict(slug="institutional-snp", nav_title="Institutional Special Needs Plans (I-SNP) in South Carolina", crumb="Institutional SNPs", scene="horse",
     title="Institutional SNPs (I-SNP) in South Carolina | ECOS Medicare Solutions",
     desc="Institutional Special Needs Plans in South Carolina for people in a nursing facility or needing that level of care at home: who qualifies, what an I-SNP does, and how it fits with Healthy Connections Medicaid.",
     llm="Institutional Special Needs Plans (I-SNP) in South Carolina for facility-level care",
     eyebrow="Your situation · Facility-level care", h1="Institutional Special Needs Plans (I-SNPs) in South Carolina",
     sub="Medicare Advantage plans for people who live in a nursing facility, or need that level of care at home, with care brought to where you live.",
     keyfacts=["An I-SNP is a Medicare Advantage plan for people who live, or are expected to live, 90 days or more in a qualifying facility, or who need that level of care at home per a state assessment.",
               "It brings care coordination on site &mdash; often nurse practitioners working with facility staff &mdash; and includes Part D.",
               "In South Carolina, many people in long-term care also qualify for Healthy Connections Medicaid; a D-SNP may then be the better fit, and we compare the two."],
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
<div class="note-box"><p><strong>Helping a parent or loved one?</strong> Choosing or changing a plan for someone in a facility can feel overwhelming. We walk through eligibility, what an I-SNP covers, and how it compares with other options &mdash; including a <a href="/medicaid">Dual SNP</a> if Healthy Connections Medicaid is paying for the care &mdash; patiently, and at no cost.</p></div>
<p>Related: <a href="/chronic-snp">Chronic SNPs (C-SNPs)</a> and <a href="/medicaid">Healthy Connections Medicaid &amp; D-SNPs</a>.</p>""",
     faqs=[("Who qualifies for an Institutional SNP?", "Generally, people with Medicare who live in (or are expected to need, for 90+ days) a qualifying institutional setting such as a nursing facility, or who need an institutional level of care at home, as determined by an approved assessment."),
           ("Can someone living at home join an I-SNP?", "Sometimes. Certain I-SNPs (institutional-equivalent plans) serve people who need a facility level of care but live at home. Availability depends on the plans offered in your South Carolina county."),
           ("Can you help a family member enroll?", "Yes. We regularly help adult children and caregivers understand the options for a parent or loved one, including how an I-SNP or D-SNP coordinates with a facility and with Healthy Connections Medicaid.")],
     sources=[SRC_MA_GOV, SRC_SNP], cta="Let&rsquo;s talk through care options for a facility setting.", about="Institutional Special Needs Plans", priority="0.6"),

dict(slug="retirement-guide", nav_title="Retire With Confidence — free 295-page retirement guide", crumb="Free Retirement Guide", scene="falls",
     title="Retire With Confidence: Free 2026 Retirement Guide | ECOS Medicare Solutions",
     desc="Retire With Confidence: a free 295-page 2026 guide to Medicare, Social Security and the money decisions of retirement, by a licensed South Carolina agent, gerontologist and Registered Social Security Analyst. Emailed free.",
     llm="Medicare, Social Security, and the money decisions that decide your retirement. Free 295-page 2026 guide, emailed on request by a licensed South Carolina agent",
     eyebrow="Free 295-page guide · 2026 Edition", h1="Retire With Confidence",
     sub="Medicare, Social Security, and the money decisions that decide your retirement &mdash; the ones that come at you between 62 and 75, most with deadlines, several expensive to get wrong in ways nobody tells you about until later. It is free, and there is nothing to buy at the end of it.",
     form_title="Where should we send it?",
     keyfacts=["Forty-seven chapters in six parts: Medicare fundamentals, IRMAA and the income traps, Social Security claiming, retirement income, long-term care and final expense, and a 2026 quick-reference section.",
               "Written by Darin Weidauer, gerontologist, Registered Social Security Analyst and retired Air Force officer &mdash; the licensed agent behind this site.",
               "Emailed on request. Nothing downloads from this page, nothing is for sale, and a phone call is optional."],
     body="""<h2>What&rsquo;s in it: forty-seven chapters, six parts</h2>
<div class="grid grid--3" style="margin:1.4rem 0 2rem">
<article class="card"><h3>Medicare: your foundation</h3><p>The four parts, the seven-month enrollment window, what Medicare covers and the gaps it leaves, Original Medicare against Medicare Advantage, Medigap, and Part D.</p></article>
<article class="card"><h3>IRMAA and the income traps</h3><p>The surcharge nobody warns you about, the late-enrollment penalties that never end, and how selling the house up north, a business, or converting an IRA can raise your Medicare premium two years later.</p></article>
<article class="card"><h3>Social Security</h3><p>How the benefit is calculated, claiming at 62 against 67 against 70, spousal and survivor benefits, the earnings test, how much of it is taxed, and the rules for teachers and other public employees outside Social Security.</p></article>
<article class="card"><h3>Retirement income planning</h3><p>Building the income stack, the tax difference between a 401(k), an IRA and a Roth, life insurance in retirement, and where you live changing what you keep.</p></article>
<article class="card"><h3>Protecting what you have built</h3><p>Long-term care and the hybrid policies that return your money, where you will live, caring for aging parents, and final expense planning.</p></article>
<article class="card"><h3>Future-proofing &amp; reference</h3><p>The annual Medicare review, the decision timeline from 59&frac12; to 75+, a glossary of 60+ terms, a 2026 quick-reference card, and what changed for 2026.</p></article>
</div>
<h2>Who wrote it</h2>
<p>Darin Weidauer &mdash; gerontologist, 22-year U.S. Air Force veteran, independent insurance agent licensed in South Carolina, and Registered Social Security Analyst. He is the licensed agent behind this site, and he is independent &mdash; appointed with a number of carriers rather than employed by one. That is worth knowing before you read anything he has written about insurance.</p>
<p>Why give it away? The rest of this site answers a narrow question: what Medicare plans are available where you live in South Carolina. The book answers the wider one &mdash; the decisions that arrive between 62 and 75, including the ones a move to the coast brings forward.</p>
<div class="note-box"><p>The guide is educational &mdash; it is not a quote, an offer of coverage, or a recommendation to buy, drop or change any policy. Use the form at the top of the page and it will be in your inbox within a few minutes; check your spam folder if not.</p></div>""",
     faqs=[("Is the guide really free?", "Yes. It is emailed to you at no cost, with nothing to buy and no obligation. A licensed agent will call only if you ask for a call on the form."),
           ("Is it specific to South Carolina?", "The book covers Medicare and retirement decisions nationally. For South Carolina specifics &mdash; the no-birthday-rule Medigap market, moving here on Medicare, Healthy Connections Medicaid and the D-SNPs, the military communities &mdash; use the guides on this site alongside it."),
           ("Will I be added to a mailing list?", "You will receive the guide and, if you asked for a call, a call. You can opt out of any further contact at any time by replying or telling us.")],
     sources=[], cta="Get Retire With Confidence, free.", about="Retirement planning, Medicare and Social Security", schema_type="WebPage", priority="0.7"),
]
