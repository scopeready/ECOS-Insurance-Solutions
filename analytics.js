/* ECOS Insurance Solutions — site analytics (Google Analytics 4), v2
 *
 * Drop-in replacement for /analytics.js. Same Measurement ID, same two
 * events as before, plus one new event for the online-enrollment links.
 *
 * Tracks, beyond standard pageviews:
 *   click_to_call        every tap/click on a phone number, labelled by where on
 *                        the page it sat and which number it was
 *   generate_lead        every lead form submitted
 *   click_enroll_online  every click on an outbound enrollment/quote link
 *                        (DestinationRx PlanCompare, PlanEnroll). A click is NOT
 *                        an enrollment: it only means the visitor left for the
 *                        platform. Completed enrollments are reported by the
 *                        platform operator, not by this site.
 *
 * Mark click_to_call and generate_lead as key events in GA4. Leave
 * click_enroll_online as a plain event so the two are never added together.
 *
 * Outbound links are recognised by host, so no page markup has to change:
 *   destinationrx.com  -> platform "destinationrx"
 *   planenroll.com     -> platform "planenroll"
 * A link may also carry data-enroll="destinationrx|planenroll" to force it.
 */
(function () {
  var MEASUREMENT_ID = 'G-7CXH7ZLSP1';

  if (!/^G-[A-Z0-9]{8,12}$/.test(MEASUREMENT_ID) || /^G-X+$/.test(MEASUREMENT_ID)) {
    if (window.console && console.info) {
      console.info('[analytics] No GA4 Measurement ID configured yet — tracking is off.');
    }
    return;
  }

  var s = document.createElement('script');
  s.async = true;
  s.src = 'https://www.googletagmanager.com/gtag/js?id=' + MEASUREMENT_ID;
  document.head.appendChild(s);

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }
  window.gtag = gtag;
  gtag('js', new Date());
  gtag('config', MEASUREMENT_ID);

  // Where on the page an element sits. Covers the hub homepage (new classes),
  // the state templates and the legacy templates.
  function placement(el) {
    var map = [
      ['.top-bar', 'top bar'], ['.topbar', 'top bar'],
      ['.site-header', 'header'], ['.site-head', 'header'], ['header.site', 'header'],
      ['.enroll-module', 'enrollment module'],
      ['.offices', 'offices'],
      ['.callcard', 'hero call card'], ['.cta-strip', 'cta strip'],
      ['.bottom-cta', 'bottom cta'],
      ['.hero', 'hero'], ['.inner-hero', 'hero'],
      ['.lead-card', 'lead form'], ['.form-card', 'lead form'], ['.review-form', 'lead form'],
      ['.state-grid', 'state grid'],
      ['.faq-list', 'faq'], ['.page-links', 'page links'],
      ['.site-footer', 'footer'], ['.site-foot', 'footer'], ['footer', 'footer'], ['.tpmo', 'footer'],
      ['.band', 'body content']
    ];
    for (var i = 0; i < map.length; i++) {
      try { if (el.closest(map[i][0])) return map[i][1]; } catch (e) {}
    }
    return 'body';
  }

  function pageInfo() {
    return { page_path: location.pathname, page_title: (document.title || '').slice(0, 100) };
  }

  function platformFor(a) {
    var forced = a.getAttribute('data-enroll');
    if (forced) return forced;
    var host = '';
    try { host = new URL(a.href, location.href).hostname; } catch (e) { return ''; }
    if (/destinationrx\.com$/i.test(host)) return 'destinationrx';
    if (/planenroll\.com$/i.test(host)) return 'planenroll';
    return '';
  }

  // click_to_call
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href^="tel:"]');
    if (!a) return;
    var info = pageInfo();
    gtag('event', 'click_to_call', {
      phone_number: a.getAttribute('href').replace('tel:', ''),
      link_placement: placement(a),
      page_path: info.page_path,
      page_title: info.page_title,
      transport_type: 'beacon'
    });
  }, true);

  // click_enroll_online — outbound to the enrollment platforms only.
  document.addEventListener('click', function (e) {
    var a = e.target && e.target.closest && e.target.closest('a[href]');
    if (!a) return;
    var platform = platformFor(a);
    if (!platform) return;
    var info = pageInfo();
    gtag('event', 'click_enroll_online', {
      platform: platform,
      link_text: (a.textContent || '').trim().slice(0, 60),
      link_placement: placement(a),
      page_path: info.page_path,
      page_title: info.page_title,
      transport_type: 'beacon'
    });
  }, true);

  // generate_lead
  document.addEventListener('submit', function (e) {
    var f = e.target;
    if (!f || f.tagName !== 'FORM') return;
    var info = pageInfo();
    var topic = f.querySelector('select');
    gtag('event', 'generate_lead', {
      form_id: f.id || f.getAttribute('name') || 'unnamed',
      form_placement: placement(f),
      lead_topic: topic ? topic.value : '',
      page_path: info.page_path,
      page_title: info.page_title,
      transport_type: 'beacon'
    });
  }, true);
})();
