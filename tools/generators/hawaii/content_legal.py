"""Hawaii FAQ page, About, Privacy, Terms."""
FAQ_PAGE = [
    ("How much does it cost to work with ECOS Medicare Solutions?", "Nothing. Independent Medicare agents are paid by the insurance carriers when you enroll, so comparing plans, answering questions and reviewing your coverage each year is free to you. Your premium is the same whether you enroll through us, another agent or the carrier directly."),
    ("I have Kaiser now. Can I keep it when I go on Medicare?", "Yes, through Kaiser Permanente Senior Advantage, Kaiser&rsquo;s own Medicare Advantage plan. Kaiser is an integrated system, so a Medigap policy does not pay for care inside it. Senior Advantage&rsquo;s service area is Honolulu County, most of Hawaii County and the island of Maui; it is not sold on Kauai, Molokai or Lanai."),
    ("What is the difference between HMSA Akamai Advantage and a Medigap policy?", "Akamai Advantage is a Medicare Advantage plan built on HMSA&rsquo;s network, with separate Oahu and neighbor island plans and, on the neighbor islands, interisland travel help when HMSA refers you off-island. A Medigap policy pairs with Original Medicare and pays at any provider that accepts Medicare, on any island or the mainland, with no network and no referral. We set the two side by side with your doctors in front of us."),
    ("I live on a neighbor island and fly to Oahu for a specialist. Which plan covers that?", "Original Medicare with a Medigap policy covers any Medicare provider anywhere with no travel rule. HMSA&rsquo;s neighbor island plans include interisland travel help for approved referrals; Kaiser refers within Kaiser. Our Neighbor Islands guide goes through it island by island."),
    ("Does Hawaii have a Medigap birthday rule or annual switching window?", "No. Your six-month Medigap open enrollment when you first have Part B is the guaranteed window, plus guaranteed-issue events such as a plan leaving your county. Outside those, Hawaii insurers can use medical underwriting."),
    ("I am under 65 on Medicare because of a disability. Can I buy Medigap in Hawaii?", "Yes, on the same terms as someone turning 65. Hawaii requires every Medigap insurer to offer every plan, guaranteed issue and without health-based pricing, during the six months after your Part B begins, at the same rates as at 65. You get a fresh open enrollment at 65."),
    ("I am retiring from the State of Hawaii. What does EUTF require?", "EUTF retiree medical plans require you to enroll in Medicare Part B when you become eligible and to send EUTF proof within 60 days, or the retiree plan is cancelled. EUTF then reimburses eligible retirees for the Part B premium (and IRMAA for those hired before July 1, 2023), but never a late penalty."),
    ("I have TRICARE For Life. Do I need a Medigap policy or Part D?", "Usually neither. TFL pays secondary to Medicare and its pharmacy is creditable drug coverage. An MA-only Advantage plan can add dental or vision without duplicating the drug benefit. Our Pearl Harbor-Hickam, Schofield Barracks and Marine Corps Base Hawaii pages walk through it."),
    ("I use the VA. Do I still need Medicare Part B?", "In most cases, yes. VA medical care is not creditable coverage for Part B, so delaying it triggers a permanent penalty and leaves you without coverage at a non-VA hospital. VA pharmacy is creditable for Part D."),
    ("When can I enroll in or change my Medicare plan in Hawaii?", "Your Initial Enrollment Period is the seven months around your 65th birthday. The Annual Election Period runs October 15 to December 7; Medicare Advantage Open Enrollment runs January 1 to March 31. Moving to another island, losing a plan, qualifying for Med-QUEST, or a federally declared disaster opens a Special Enrollment Period."),
    ("What are the [[YEAR]] Medicare costs?", "Part B premium $202.90 a month, Part B deductible $283, Part A hospital deductible $1,736 per benefit period, Part D out-of-pocket cap $2,100. Higher earners pay IRMAA surcharges above $109,000 (single) or $218,000 (joint) of 2024 income. Our costs page has the full chart and calculators."),
    ("Can Hawaii help pay my Part B premium?", "Possibly. Hawaii&rsquo;s Medicare Savings Programs (QMB, SLMB, QI), run by the Med-QUEST Division, pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. Apply at mybenefits.hawaii.gov or 1-800-316-8005, or call Hawaii SHIP at 1-888-875-9229."),
    ("What is QUEST Integration?", "Hawaii&rsquo;s Medicaid managed-care program, run by the Med-QUEST Division of the Department of Human Services. It covers adults 65 and over and people with disabilities alongside everyone else, coordinating the Medicaid side, including long-term services and supports, while Medicare pays first for medical care."),
    ("Where can I get free, unbiased Medicare counseling in Hawaii?", "Hawaii SHIP, the Hawaii State Health Insurance Assistance Program, is run by the Executive Office on Aging in the Department of Health: 1-888-875-9229 (Oahu 808-586-7299; TTY 1-866-810-4379). You can also call 1-800-MEDICARE or use Medicare.gov. We are an independent agency, not a government program, and we say so on every page."),
    ("Do you offer every plan available in my area?", "No. We represent a number of insurance organizations and products in Hawaii, not all of them, and we will always say so. For the complete list, use Medicare.gov, 1-800-MEDICARE or Hawaii SHIP. For help choosing among the plans we do offer, call [[PHONE]]."),
    ("Where can I verify your Hawaii licence?", "Darin Weidauer holds Hawaii insurance license #18580338 (NPN 18580338). You can verify it through the Hawaii Insurance Division&rsquo;s licence search on the state open-data portal or through the NIPR."),
    ("Do you meet in person?", "We work with people across Hawaii by phone and video, which is how most families on six islands prefer it. Our sister agency has walk-in offices in Mesa and Sun City, Arizona."),
]

ABOUT_BODY = """<div class="author" style="margin-bottom:2rem">
<img class="author__photo" src="/darin.jpg" width="600" height="600" alt="Darin Weidauer, independent Medicare insurance agent and credentialed gerontologist" loading="lazy" decoding="async">
<div>
<ul class="creds"><li>HI License #18580338 · NPN 18580338</li><li>Credentialed gerontologist (2014)</li><li>Registered Social Security Analyst&reg;</li><li>MBA, Pepperdine</li><li>Master&rsquo;s in Long-Term Care, USC</li><li>22-yr USAF veteran (retired officer)</li></ul>
<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Hawaii retirees and people approaching 65 make sense of their Medicare options &mdash; clearly, patiently, and with no cost to them.</p>
</div></div>
<h2>Background</h2>
<p>A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine University and a Master&rsquo;s in Long-Term Care from the University of Southern California&rsquo;s Leonard Davis School of Gerontology, where he became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>
<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education: one-on-one reviews, no-cost community workshops, the free 295-page guide <a href="/retirement-guide"><em>Retire With Confidence</em></a>, and the pages on this site, every one of which he wrote or reviewed. He is also the founder of MyECOS360, an agency operating system for independent insurance agents, and the author of its training on <a href="https://www.myecos360.com/insurance-lead-economics">insurance lead economics</a>.</p>
<h2>How he is paid, and what that means for you</h2>
<p>ECOS Medicare Solutions is an independent agency: appointed with a number of Medicare Advantage, Medigap and Part D carriers in Hawaii, employed by none of them. When you enroll in a plan through us, the carrier pays us a commission. That commission comes out of the carrier&rsquo;s filed rate &mdash; it is never added to your premium. You pay the same whether you enroll through us, through another agent, or directly with the insurer; going direct does not make a policy cheaper, and using us does not make it dearer.</p>
<p>We do not represent every plan sold in Hawaii, and we say so on every page. For a complete list, use Medicare.gov, 1-800-MEDICARE, or Hawaii SHIP (1-888-875-9229), the state&rsquo;s free and independent counseling program run by the Executive Office on Aging.</p>
<h2>Licensing</h2>
<p>Darin Weidauer holds <strong>Hawaii insurance license #18580338</strong> and is a licensed insurance agent in Hawaii and fifteen other states &mdash; Arizona, California, Colorado, Georgia, Indiana, Minnesota, Nevada, New Mexico, North Carolina, Ohio, South Carolina, Tennessee, Texas, Utah and Washington &mdash; under National Producer Number 18580338, which you can verify with the Hawaii Insurance Division of the Department of Commerce and Consumer Affairs or the NIPR. The multi-state licence is what lets us help mainland retirees who move to Kona or Kihei bring their coverage with them, and help families with a parent on one island and children on another or on the mainland.</p>
<h2>Where else you will find him</h2>
<ul>
<li><a href="https://www.myecos360.com/darin-weidauer" rel="noopener">Author page at MyECOS360</a> &mdash; the canonical profile</li>
<li><a href="https://www.linkedin.com/in/darin-weidauer-3165a816b/" rel="noopener">LinkedIn</a> and <a href="https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ" rel="noopener">YouTube</a></li>
<li>Sister sections: <a href="https://www.ecosinsurancesolutions.com/arizona" rel="noopener">Medicare Enrollment Arizona</a>, <a href="https://www.ecosinsurancesolutions.com/california" rel="noopener">California Medicare Enrollment</a>, <a href="https://www.ecosinsurancesolutions.com/washington" rel="noopener">Washington Medicare Enrollment</a>, and <a href="https://www.mymedigaprate.com" rel="noopener">MyMedigapRate</a>, where Medigap rate filings &mdash; Hawaii&rsquo;s included &mdash; are published filing by filing.</li>
</ul>
<h2>How to reach him</h2>
<p>Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form at the top of this page. We work with people on every island by phone and video.</p>
"""

PRIVACY_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 13, 2026. This policy is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>This Privacy Policy explains how ECOS Medicare Solutions ("we," "us") handles information collected through the Hawaii section of ecosinsurancesolutions.com (the "Site").</p>
<h2>Information we collect</h2>
<p>When you submit a form on the Site, we collect the information you provide: your name, phone number, email address, ZIP code or city, the topic you select, and a record of the consent you give (including the consent language shown and a date/time stamp). We do not ask for, and ask you not to send, health information through the form.</p>
<h2>How we use it</h2>
<p>We use your information to contact you about Medicare plan options and to provide the help you requested &mdash; by phone call, text message and email, consistent with the consent you provide. A licensed insurance agent may contact you. We do not sell your personal information.</p>
<h2>How your form is processed</h2>
<p>Our forms are delivered through a third-party form-processing service (Web3Forms), which transmits your submission to us. The Site loads web fonts from Google Fonts. We aim to limit data sharing to what is needed to operate the Site and respond to you.</p>
<h2>Analytics</h2>
<p>When enabled, we use Google Analytics to understand how visitors find and use this Site &mdash; which pages are read, and whether people call or submit a form. Google Analytics sets cookies and receives your IP address, device and browser type, and the pages you view. We use it in aggregate to improve the Site.</p><p>We do not send Google Analytics your name, phone number, email address or any information you type into a form. You can opt out across all sites using Google&rsquo;s <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow noopener" target="_blank">browser opt-out add-on</a>, or by using your browser&rsquo;s cookie controls.</p>
<h2>Your choices</h2>
<p>You can opt out of further contact at any time by telling us, replying STOP to texts, or unsubscribing from emails. To request that we delete your information, contact us using the details below.</p>
<h2>Data security</h2>
<p>We take reasonable measures to protect the information you share, but no method of transmission over the internet is completely secure. If a breach of unencrypted personal information occurs, we will notify affected Hawaii residents as Hawaii&rsquo;s breach-notification law (Hawaii Revised Statutes chapter 487N) requires.</p>
<h2>Children</h2>
<p>The Site is intended for adults making Medicare decisions and is not directed to children under 13.</p>
<h2>Contact us</h2>
<p>Questions about this policy? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""

TERMS_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 13, 2026. This document is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>By using the Hawaii section of ecosinsurancesolutions.com (the "Site"), operated by ECOS Medicare Solutions, you agree to these Terms of Use.</p>
<h2>Informational purpose</h2>
<p>The Site provides general information about Medicare to help you make decisions. It is not legal, tax or medical advice, and it is not a substitute for the official Medicare program or for Hawaii&rsquo;s free counseling program, Hawaii SHIP (1-888-875-9229). Medicare plan availability, costs and rules change and vary by county and island.</p>
<h2>Insurance offered through a licensed agent</h2>
<p>Insurance products referenced on the Site are offered through a licensed insurance agent (Darin Weidauer, Hawaii insurance license #18580338, NPN 18580338). Enrollment is subject to plan terms and eligibility. We do not offer every plan available in your area.</p>
<h2>No guarantee of accuracy</h2>
<p>We work to keep figures current and cite the year and source, but we do not warrant that all information is complete, current or error-free. Always confirm details with the official sources noted on the Site.</p>
<h2>External links</h2>
<p>The Site links to third-party websites (such as Medicare.gov, hawaiiship.org and medquest.hawaii.gov) and to other sections and sites operated by ECOS Medicare Solutions. We are not responsible for the content or practices of third-party sites.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, ECOS Medicare Solutions is not liable for any damages arising from your use of the Site.</p>
<h2>Governing law</h2>
<p>These Terms are governed by the laws of the State of Hawaii.</p>
<h2>Contact us</h2>
<p>Questions? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a> or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""
