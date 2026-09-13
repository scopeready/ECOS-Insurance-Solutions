"""Florida FAQ page, About, Privacy, Terms."""
FAQ_PAGE = [
    ("How much does it cost to work with ECOS Medicare Solutions?", "Nothing. Independent Medicare agents are paid by the insurance carriers when you enroll, so comparing plans, answering questions and reviewing your coverage each year is free to you. Your premium is the same whether you enroll through us, another agent or the carrier directly."),
    ("My Medicare Advantage plan was discontinued in my Florida county. What now?", "You get a Special Enrollment Period to choose a new plan and, because you lost coverage through no fault of your own, generally a guaranteed-issue right to buy a Medigap policy without health questions, usually within 63 days of the coverage ending. AvMed&rsquo;s exit and UnitedHealthcare&rsquo;s county cuts for 2026 both qualify. Call before the deadline on your notice."),
    ("Does Florida have a Medigap birthday rule or annual switching window?", "No. Your six-month Medigap open enrollment at 65 is the guaranteed window, plus guaranteed-issue events such as a plan leaving your county. Outside those, Florida insurers can use medical underwriting. Because Florida requires issue-age rating, the policy you buy at 65 is also priced on that age for good, which is one more reason to buy early."),
    ("What does issue-age rating mean for my Medigap premium?", "Florida requires insurers to set your premium by the age at which you buy and prohibits raising it because you got older. Premiums still rise with the carrier&rsquo;s filed increases, which apply to everyone in the block. The rule rewards buying at 65 and holding on; someone who waits until 72 pays a 72-year-old&rsquo;s rate for life."),
    ("I am under 65 on Medicare because of a disability. Can I buy Medigap in Florida?", "Yes. Since 2009 Florida gives people under 65 on Medicare a six-month guaranteed-issue window when they enroll in Part B, and insurers must offer them at least one plan. Premiums for under-65 policies are higher. You get a fresh open enrollment for every plan at 65."),
    ("Does Mayo Clinic Jacksonville or Moffitt accept Medicare Advantage plans?", "Both accept Original Medicare and therefore every Medigap policy. Each contracts with some Medicare Advantage plans and not others, and the list changes yearly. If Mayo, Moffitt, Cleveland Clinic Florida, Baptist Health or Tampa General is your care, we confirm the plan&rsquo;s status in writing before you enroll."),
    ("I just moved to Florida. Do I have to change my Medicare plan?", "Medicare Advantage and Part D plans are tied to your county of residence, so the move gives you a Special Enrollment Period to choose plans sold here. A Medigap policy from another state usually stays in force but may be re-rated for Florida. If you came from a state with continuous guaranteed issue, such as New York or Connecticut, know that Florida does not have it; see our New to Florida page."),
    ("I am a snowbird. Does my plan work up north in the summer?", "A Medigap policy with Original Medicare works anywhere in the country that takes Medicare. Most Medicare Advantage plans cover only emergencies outside their service area, though a few PPOs have travel benefits. Choose based on where you actually see doctors; we look at both addresses."),
    ("A hurricane made me miss an enrollment deadline. Am I out of luck?", "Usually not. A FEMA-declared disaster opens a Special Enrollment Period for people who lived in a declared county, or who rely on someone who did, and missed a valid election period because of it. Part D plans must also allow early refills in the emergency area. Our Hurricanes page has the details."),
    ("I have TRICARE For Life. Do I need a Medigap policy or Part D?", "Usually neither. TFL pays secondary to Medicare and its pharmacy is creditable Part D coverage. You do need Part B, and you must keep it. Our Veterans page covers the exceptions."),
    ("I use the VA. Do I still need Medicare Part B?", "In most cases, yes. VA medical care is not creditable coverage for Part B, so delaying Part B adds a lifelong penalty, and VA care does not cover you at non-VA hospitals in an emergency. Many Florida veterans keep both."),
    ("When can I enroll in or change my Medicare plan in Florida?", "Your Initial Enrollment Period is the seven months around your 65th birthday. The Annual Election Period is October 15 to December 7, and Medicare Advantage Open Enrollment runs January 1 to March 31. Moving to Florida, losing a plan, a disaster declaration, or qualifying for Medicaid or Extra Help each open a Special Enrollment Period."),
    ("What are the [[YEAR]] Medicare costs?", "Part B premium $202.90 a month, Part B deductible $283, Part A hospital deductible $1,736 per benefit period, Part D out-of-pocket cap $2,100, maximum Part D deductible $615. IRMAA surcharges begin at $109,000 of modified adjusted gross income for a single filer and $218,000 for a joint return, looking back two tax years. See our costs page for the full table."),
    ("Can Florida help pay my Part B premium?", "Possibly. Florida&rsquo;s Medicare Savings Programs (QMB, SLMB and QI) pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply through ACCESS Florida at myaccessflorida.com; SHINE (1-800-963-5337) can help. Qualifying also enrolls you in Extra Help for Part D."),
    ("What is SMMC Long-Term Care?", "Florida&rsquo;s Medicaid managed-care program for long-term services: nursing-facility care and the home- and community-based services that keep people out of one. Eligibility runs through DCF and the CARES assessment, and there is a waitlist for home-based care. Florida aligns its D-SNPs with these plans so one organization can coordinate Medicare and Medicaid."),
    ("Where can I get free, unbiased Medicare counseling in Florida?", "SHINE (Serving Health Insurance Needs of Elders), Florida&rsquo;s State Health Insurance Assistance Program, run by the Department of Elder Affairs through the Area Agencies on Aging: 1-800-963-5337. It is free and independent, and we point people to it."),
    ("Do you offer every plan available in my area?", "No. We represent a number of insurance organizations and products in Florida, not all of them. For a complete list, use Medicare.gov, 1-800-MEDICARE or SHINE."),
    ("Do you meet in person?", "We work with Floridians statewide by phone and video, which is how most people prefer it across a state this long. If you are in Arizona for part of the year, our sister agency has offices in Mesa and Sun City."),
]

ABOUT_BODY = """<div class="author" style="margin-bottom:2rem">
<img class="author__photo" src="/darin.jpg" width="600" height="600" alt="Darin Weidauer, independent Medicare insurance agent and credentialed gerontologist" loading="lazy" decoding="async">
<div>
<ul class="creds"><li>NPN 18580338 · licensed in Florida</li><li>Credentialed gerontologist (2014)</li><li>Registered Social Security Analyst&reg;</li><li>MBA, Pepperdine</li><li>Master&rsquo;s in Long-Term Care, USC</li><li>22-yr USAF veteran (retired officer)</li></ul>
<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Florida retirees and people approaching 65 make sense of their Medicare options &mdash; clearly, patiently, and with no cost to them.</p>
</div></div>
<h2>Background</h2>
<p>A 22-year U.S. Air Force veteran who retired as an officer &mdash; and who spent Air Force years alongside the retirees now settled around MacDill, Eglin and Pensacola &mdash; Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine University and a Master&rsquo;s in Long-Term Care from the University of Southern California&rsquo;s Leonard Davis School of Gerontology, where he became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>
<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education: one-on-one reviews, no-cost community workshops, the free 295-page guide <a href="/retirement-guide"><em>Retire With Confidence</em></a>, and the pages on this site, every one of which he wrote or reviewed. He is also the founder of MyECOS360, an agency operating system for independent insurance agents, and the author of its training on <a href="https://www.myecos360.com/insurance-lead-economics">insurance lead economics</a>.</p>
<h2>How he is paid, and what that means for you</h2>
<p>ECOS Medicare Solutions is an independent agency: appointed with a number of Medicare Advantage, Medigap and Part D carriers in Florida, employed by none of them. When you enroll in a plan through us, the carrier pays us a commission. That commission comes out of the carrier&rsquo;s filed rate &mdash; it is never added to your premium. You pay the same whether you enroll through us, through another agent, or directly with the insurer; going direct does not make a policy cheaper, and using us does not make it dearer.</p>
<p>We do not represent every plan sold in Florida, and we say so on every page. For a complete list, use Medicare.gov, 1-800-MEDICARE, or SHINE (1-800-963-5337), Florida&rsquo;s free and independent counseling program.</p>
<h2>Licensing</h2>
<p>Darin is a licensed insurance agent in Florida and sixteen other states &mdash; Arizona, California, Colorado, Georgia, Hawaii, Indiana, Minnesota, Nevada, New Mexico, North Carolina, Ohio, South Carolina, Tennessee, Texas, Utah and Washington &mdash; under National Producer Number 18580338, which you can verify with the Florida Department of Financial Services or the NIPR. The multi-state licence is what lets us follow <a href="/new-to-florida">snowbirds</a> home to Minnesota, Ohio and Georgia in the summer, and new Floridians through the move itself.</p>
<h2>Where else you will find him</h2>
<ul>
<li><a href="https://www.myecos360.com/darin-weidauer" rel="noopener">Author page at MyECOS360</a> &mdash; the canonical profile</li>
<li><a href="https://www.linkedin.com/in/darin-weidauer-3165a816b/" rel="noopener">LinkedIn</a> and <a href="https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ" rel="noopener">YouTube</a></li>
<li>Sister sites: <a href="https://www.medicareenrollmentarizona.com" rel="noopener">Medicare Enrollment Arizona</a>, <a href="https://georgiamedicareenrollment.com" rel="noopener">Georgia Medicare Enrollment</a>, <a href="https://minnesotamedicareenrollment.com" rel="noopener">Minnesota Medicare Enrollment</a>, <a href="https://texasmedicareenrollment.com" rel="noopener">Texas Medicare Enrollment</a>, and <a href="https://www.mymedigaprate.com" rel="noopener">MyMedigapRate</a>, where Medigap rate filings &mdash; Florida&rsquo;s included &mdash; are published filing by filing.</li>
</ul>
<h2>How to reach him</h2>
<p>Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form at the top of this page. We work with Floridians statewide by phone and video.</p>
"""

PRIVACY_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 4, 2026. This policy is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>This Privacy Policy explains how ECOS Medicare Solutions ("we," "us") handles information collected through Medicareenrollmentflorida.com (the "Site").</p>
<h2>Information we collect</h2>
<p>When you submit a form on the Site, we collect the information you provide: your name, phone number, email address, ZIP code or city, the topic you select, and a record of the consent you give (including the consent language shown and a date/time stamp). We do not ask for, and ask you not to send, health information through the form.</p>
<h2>How we use it</h2>
<p>We use your information to contact you about Medicare plan options and to provide the help you requested &mdash; by phone call, text message and email, consistent with the consent you provide. A licensed insurance agent may contact you. We do not sell your personal information.</p>
<h2>How your form is processed</h2>
<p>Our forms are delivered through a third-party form-processing service (Web3Forms), which transmits your submission to us. The Site loads web fonts from Google Fonts. We aim to limit data sharing to what is needed to operate the Site and respond to you.</p>
<h2>Analytics</h2>
<p>When enabled, we use Google Analytics to understand how visitors find and use this Site &mdash; which pages are read, and whether people call or submit a form. Google Analytics sets cookies and receives your IP address, device and browser type, and the pages you view. We use it in aggregate to improve the Site.</p><p>We do not send Google Analytics your name, phone number, email address or any information you type into a form. You can opt out across all sites using Google&rsquo;s <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow noopener" target="_blank">browser opt-out add-on</a>, or by using your browser&rsquo;s cookie controls.</p>
<h2>Your choices</h2>
<p>You can opt out of further contact at any time by telling us, replying STOP to texts, or unsubscribing from emails. To request that we delete your information, contact us using the details below. Florida residents may also have rights under the Florida Digital Bill of Rights; contact us to exercise them.</p>
<h2>Data security</h2>
<p>We take reasonable measures to protect the information you share, but no method of transmission over the internet is completely secure.</p>
<h2>Children</h2>
<p>The Site is intended for adults making Medicare decisions and is not directed to children under 13.</p>
<h2>Contact us</h2>
<p>Questions about this policy? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""

TERMS_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 4, 2026. This document is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>By using Medicareenrollmentflorida.com (the "Site"), operated by ECOS Medicare Solutions, you agree to these Terms of Use.</p>
<h2>Informational purpose</h2>
<p>The Site provides general information about Medicare to help you make decisions. It is not legal, tax or medical advice, and it is not a substitute for the official Medicare program or for Florida&rsquo;s free counseling program, SHINE. Medicare plan availability, costs and rules change and vary by county.</p>
<h2>Insurance offered through a licensed agent</h2>
<p>Insurance products referenced on the Site are offered through a licensed insurance agent (Darin Weidauer, NPN 18580338, licensed in Florida). Enrollment is subject to plan terms and eligibility. We do not offer every plan available in your area.</p>
<h2>No guarantee of accuracy</h2>
<p>We work to keep figures current and cite the year and source, but we do not warrant that all information is complete, current or error-free. Always confirm details with the official sources noted on the Site.</p>
<h2>External links</h2>
<p>The Site links to third-party websites (such as Medicare.gov and myflfamilies.com) and to other sites operated by ECOS Medicare Solutions. We are not responsible for the content or practices of third-party sites.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, ECOS Medicare Solutions is not liable for any damages arising from your use of the Site.</p>
<h2>Governing law</h2>
<p>These Terms are governed by the laws of the State of Florida.</p>
<h2>Contact us</h2>
<p>Questions? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a> or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""
