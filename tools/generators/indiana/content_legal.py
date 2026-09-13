"""Indiana FAQ page, About, Privacy, Terms."""
FAQ_PAGE = [
    ("How much does it cost to work with ECOS Medicare Solutions?", "Nothing. Independent Medicare agents are paid by the insurance carriers when you enroll, so comparing plans, answering questions and reviewing your coverage each year is free to you. Your premium is the same whether you enroll through us, another agent or the carrier directly."),
    ("What is the Indiana Medigap birthday rule?", "A switching window Indiana added for 2026 (HEA 1226, amended by HEA 1260). If you are 65 or older and already have a Medigap policy, you can apply to a different insurer for the same plan letter without medical underwriting in a window that opens 31 days before your birthday and closes 31 days after it. The new policy starts the first of the following month. It is for existing Medigap policyholders; it does not let an Advantage member buy a supplement without underwriting."),
    ("My Medigap premium just went up. What can I do in Indiana?", "Use the birthday rule. Put your birthday on the calendar, and in the window around it we compare every Indiana carrier&rsquo;s current premium and filed rate history for your plan letter, then move you if a better-priced policy exists. Outside the window, a switch usually means health questions."),
    ("I am under 65 on Medicare because of a disability. Can I buy Medigap in Indiana?", "Yes. Since January 1, 2025 (SEA 215, Indiana Code 27-8-13-9.1), people under 65 on Medicare get their own six-month guaranteed-issue window when Part B begins, insurers must offer them coverage, and the law limits what they can be charged for Plans A, B and D. You get a fresh open enrollment for every plan at 65."),
    ("My Medicare Advantage plan left my Indiana county, or I was moved to a new plan. What now?", "A plan that leaves you gives you a Special Enrollment Period and, because you lost coverage through no fault of your own, generally a guaranteed-issue right to buy a Medigap policy without health questions, usually within 63 days of the coverage ending. If you were moved rather than dropped &mdash; as IU Health Plans members were moved under Anthem for 2026 &mdash; the Annual Election Period is when to check that the new plan fits."),
    ("Are my IU Health, Ascension St. Vincent or Parkview doctors in a Medicare Advantage plan?", "It depends on the plan and the year. Every big Indiana system accepts Original Medicare, and therefore every Medigap policy. Each contracts with some Advantage plans and not others, and the list changes every October. If a specific system or doctor is your care, we confirm the plan&rsquo;s status in writing before you enroll."),
    ("I winter in Florida. Does my Indiana plan work there?", "A Medigap policy with Original Medicare works anywhere in the U.S. Most Medicare Advantage HMOs cover only emergencies out of area; some PPOs and travel benefits go further. See our snowbirds guide, and our Florida and Arizona sections for the view from the other end."),
    ("I live near Louisville, Cincinnati or Chicago and my doctors are across the line. Which plan works?", "With Original Medicare and a Medigap policy, any out-of-state provider that accepts Medicare is covered. With an Advantage plan, only if that provider is in the plan&rsquo;s network, which we confirm before you enroll."),
    ("I have a union or employer retiree plan. Should I keep it?", "Compare before you cancel anything. Retiree plans usually become a group Advantage plan or a group supplement at 65, the drug coverage is normally creditable, and leaving is often permanent. We set the retiree plan beside the individual options with the numbers, including the case for leaving it alone."),
    ("I have TRICARE For Life. Do I need a Medigap policy or Part D?", "Usually neither. TFL pays secondary to Medicare and its pharmacy is creditable drug coverage. An MA-only Advantage plan can add dental or vision without duplicating the drug benefit."),
    ("I use the VA. Do I still need Medicare Part B?", "In most cases, yes. VA medical care is not creditable coverage for Part B, so delaying it triggers a permanent penalty and leaves you without coverage at a non-VA hospital. VA pharmacy is creditable for Part D."),
    ("When can I enroll in or change my Medicare plan in Indiana?", "Your Initial Enrollment Period is the seven months around your 65th birthday. The Annual Election Period runs October 15 to December 7; Medicare Advantage Open Enrollment runs January 1 to March 31. Moving counties, losing a plan, or qualifying for Medicaid opens a Special Enrollment Period, and the birthday rule covers Medigap-to-Medigap switches."),
    ("What are the [[YEAR]] Medicare costs?", "Part B premium $202.90 a month, Part B deductible $283, Part A hospital deductible $1,736 per benefit period, Part D out-of-pocket cap $2,100. Higher earners pay IRMAA surcharges above $109,000 (single) or $218,000 (joint) of 2024 income. Our costs page has the full chart and calculators."),
    ("Can Indiana help pay my Part B premium or my drug plan?", "Possibly. Indiana&rsquo;s Medicare Savings Programs (QMB, SLMB, QI), handled by FSSA&rsquo;s Division of Family Resources, pay the Part B premium for people with limited income and resources, and QMB also covers Medicare&rsquo;s deductibles and copays. HoosierRx pays up to $70 a month toward a Part D premium for eligible Hoosiers 65 and older. Apply through the FSSA Benefits Portal or 800-403-0864, or call Indiana SHIP at 800-452-4800."),
    ("What is Indiana PathWays for Aging?", "Indiana&rsquo;s Medicaid managed-care program for Hoosiers 60 and older who qualify for Medicaid on the basis of age, blindness or disability, launched July 1, 2024 and run by Anthem, Humana and UnitedHealthcare. It coordinates the Medicaid side, including long-term services and supports, while Medicare pays first for medical care."),
    ("Where can I get free, unbiased Medicare counseling in Indiana?", "Indiana SHIP, the State Health Insurance Assistance Program run by the Indiana Department of Insurance: 800-452-4800, with counseling sites across the state. You can also call 1-800-MEDICARE or use Medicare.gov. We are an independent agency, not a government program, and we say so on every page."),
    ("Do you offer every plan available in my area?", "No. We represent a number of insurance organizations and products in Indiana, not all of them, and we will always say so. For the complete list, use Medicare.gov, 1-800-MEDICARE or Indiana SHIP. For help choosing among the plans we do offer, call [[PHONE]]."),
    ("Where can I verify your Indiana licence?", "Darin Weidauer holds Indiana insurance license #3951814 (NPN 18580338). You can verify it through the Indiana Department of Insurance&rsquo;s licence lookup (run by Sircon) or through the NIPR."),
    ("Do you meet in person?", "We work with Hoosiers statewide by phone and video, which is how most people prefer it across 92 counties. Our sister agency has walk-in offices in Mesa and Sun City, Arizona, for snowbirds who are there for the winter."),
]

ABOUT_BODY = """<div class="author" style="margin-bottom:2rem">
<img class="author__photo" src="/darin.jpg" width="600" height="600" alt="Darin Weidauer, independent Medicare insurance agent and credentialed gerontologist" loading="lazy" decoding="async">
<div>
<ul class="creds"><li>IN License #3951814 · NPN 18580338</li><li>Credentialed gerontologist (2014)</li><li>Registered Social Security Analyst&reg;</li><li>MBA, Pepperdine</li><li>Master&rsquo;s in Long-Term Care, USC</li><li>22-yr USAF veteran (retired officer)</li></ul>
<p>Darin Weidauer is an independent Medicare insurance agent, credentialed gerontologist, and Registered Social Security Analyst&reg; who helps Indiana retirees and people approaching 65 make sense of their Medicare options &mdash; clearly, patiently, and with no cost to them.</p>
</div></div>
<h2>Background</h2>
<p>A 22-year U.S. Air Force veteran who retired as an officer, Darin holds five master&rsquo;s degrees, including an MBA and a Master&rsquo;s in Dispute Resolution from Pepperdine University and a Master&rsquo;s in Long-Term Care from the University of Southern California&rsquo;s Leonard Davis School of Gerontology, where he became a credentialed gerontologist in 2014 &mdash; studying the human side of aging, not just the paperwork.</p>
<p>A former Professor of Aerospace Studies at Loyola Marymount University who has lectured at more than 50 colleges and universities, Darin now channels that teaching instinct into plain-English Medicare education: one-on-one reviews, no-cost community workshops, the free 295-page guide <a href="/retirement-guide"><em>Retire With Confidence</em></a>, and the pages on this site, every one of which he wrote or reviewed. He is also the founder of MyECOS360, an agency operating system for independent insurance agents, and the author of its training on <a href="https://www.myecos360.com/insurance-lead-economics">insurance lead economics</a>.</p>
<h2>How he is paid, and what that means for you</h2>
<p>ECOS Medicare Solutions is an independent agency: appointed with a number of Medicare Advantage, Medigap and Part D carriers in Indiana, employed by none of them. When you enroll in a plan through us, the carrier pays us a commission. That commission comes out of the carrier&rsquo;s filed rate &mdash; it is never added to your premium. You pay the same whether you enroll through us, through another agent, or directly with the insurer; going direct does not make a policy cheaper, and using us does not make it dearer.</p>
<p>We do not represent every plan sold in Indiana, and we say so on every page. For a complete list, use Medicare.gov, 1-800-MEDICARE, or Indiana SHIP (800-452-4800), the state&rsquo;s free and independent counseling program run by the Indiana Department of Insurance.</p>
<h2>Licensing</h2>
<p>Darin Weidauer holds <strong>Indiana insurance license #3951814</strong> and is a licensed insurance agent in Indiana and fifteen other states &mdash; Arizona, California, Colorado, Georgia, Hawaii, Minnesota, Nevada, New Mexico, North Carolina, Ohio, South Carolina, Tennessee, Texas, Utah and Washington &mdash; under National Producer Number 18580338, which you can verify with the Indiana Department of Insurance&rsquo;s licence lookup or through the NIPR. The multi-state licence is what lets us follow <a href="/snowbirds">Hoosier snowbirds</a> to Arizona and Texas, and Hoosiers along the river to their doctors in Ohio; for Florida, our Florida section is served by its own licensed agent.</p>
<h2>Where else you will find him</h2>
<ul>
<li><a href="https://www.myecos360.com/darin-weidauer" rel="noopener">Author page at MyECOS360</a> &mdash; the canonical profile</li>
<li><a href="https://www.linkedin.com/in/darin-weidauer-3165a816b/" rel="noopener">LinkedIn</a> and <a href="https://www.youtube.com/channel/UCD1XkkknhQ3UT-8AteYD3vQ" rel="noopener">YouTube</a></li>
<li>Sister sections: <a href="https://www.ecosinsurancesolutions.com/florida" rel="noopener">Medicare Enrollment Florida</a>, <a href="https://www.ecosinsurancesolutions.com/arizona" rel="noopener">Medicare Enrollment Arizona</a>, <a href="https://www.ecosinsurancesolutions.com/ohio" rel="noopener">Ohio Medicare Enrollment</a>, and <a href="https://www.mymedigaprate.com" rel="noopener">MyMedigapRate</a>, where Medigap rate filings &mdash; Indiana&rsquo;s included &mdash; are published filing by filing.</li>
</ul>
<h2>How to reach him</h2>
<p>Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form at the top of this page. We work with Hoosiers statewide by phone and video.</p>
"""

PRIVACY_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 13, 2026. This policy is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>This Privacy Policy explains how ECOS Medicare Solutions ("we," "us") handles information collected through the Indiana section of ecosinsurancesolutions.com (the "Site").</p>
<h2>Information we collect</h2>
<p>When you submit a form on the Site, we collect the information you provide: your name, phone number, email address, ZIP code or city, the topic you select, and a record of the consent you give (including the consent language shown and a date/time stamp). We do not ask for, and ask you not to send, health information through the form.</p>
<h2>How we use it</h2>
<p>We use your information to contact you about Medicare plan options and to provide the help you requested &mdash; by phone call, text message and email, consistent with the consent you provide. A licensed insurance agent may contact you. We do not sell your personal information.</p>
<h2>How your form is processed</h2>
<p>Our forms are delivered through a third-party form-processing service (Web3Forms), which transmits your submission to us. The Site loads web fonts from Google Fonts. We aim to limit data sharing to what is needed to operate the Site and respond to you.</p>
<h2>Analytics</h2>
<p>When enabled, we use Google Analytics to understand how visitors find and use this Site &mdash; which pages are read, and whether people call or submit a form. Google Analytics sets cookies and receives your IP address, device and browser type, and the pages you view. We use it in aggregate to improve the Site.</p><p>We do not send Google Analytics your name, phone number, email address or any information you type into a form. You can opt out across all sites using Google&rsquo;s <a href="https://tools.google.com/dlpage/gaoptout" rel="nofollow noopener" target="_blank">browser opt-out add-on</a>, or by using your browser&rsquo;s cookie controls.</p>
<h2>Your choices</h2>
<p>You can opt out of further contact at any time by telling us, replying STOP to texts, or unsubscribing from emails. To request that we delete your information, contact us using the details below. Indiana residents may also have rights under the Indiana Consumer Data Protection Act (Indiana Code 24-15, in effect from January 1, 2026) where it applies; contact us to exercise them.</p>
<h2>Data security</h2>
<p>We take reasonable measures to protect the information you share, but no method of transmission over the internet is completely secure.</p>
<h2>Children</h2>
<p>The Site is intended for adults making Medicare decisions and is not directed to children under 13.</p>
<h2>Contact us</h2>
<p>Questions about this policy? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a>, email <a href="mailto:[[EMAIL]]">[[EMAIL]]</a>, or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""

TERMS_BODY = """<p style="color:var(--ink-soft)"><em>Last updated: September 13, 2026. This document is provided as a starting template and should be reviewed by your attorney before launch.</em></p>
<p>By using the Indiana section of ecosinsurancesolutions.com (the "Site"), operated by ECOS Medicare Solutions, you agree to these Terms of Use.</p>
<h2>Informational purpose</h2>
<p>The Site provides general information about Medicare to help you make decisions. It is not legal, tax or medical advice, and it is not a substitute for the official Medicare program or for Indiana&rsquo;s free counseling program, Indiana SHIP (800-452-4800). Medicare plan availability, costs and rules change and vary by county.</p>
<h2>Insurance offered through a licensed agent</h2>
<p>Insurance products referenced on the Site are offered through a licensed insurance agent (Darin Weidauer, Indiana insurance license #3951814, NPN 18580338). Enrollment is subject to plan terms and eligibility. We do not offer every plan available in your area.</p>
<h2>No guarantee of accuracy</h2>
<p>We work to keep figures current and cite the year and source, but we do not warrant that all information is complete, current or error-free. Always confirm details with the official sources noted on the Site.</p>
<h2>External links</h2>
<p>The Site links to third-party websites (such as Medicare.gov and in.gov) and to other sections and sites operated by ECOS Medicare Solutions. We are not responsible for the content or practices of third-party sites.</p>
<h2>Limitation of liability</h2>
<p>To the fullest extent permitted by law, ECOS Medicare Solutions is not liable for any damages arising from your use of the Site.</p>
<h2>Governing law</h2>
<p>These Terms are governed by the laws of the State of Indiana.</p>
<h2>Contact us</h2>
<p>Questions? Call <a href="tel:[[TEL]]"><strong>[[PHONE]]</strong></a> or use the form on our <a href="/">home page</a>.</p>
<p style="font-size:.85rem;color:var(--ink-soft)">ECOS Medicare Solutions is not connected with or endorsed by the U.S. government or the federal Medicare program. This is a solicitation for insurance.</p>
"""
