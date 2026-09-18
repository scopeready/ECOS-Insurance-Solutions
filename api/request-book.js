// POST /api/request-book
// Validates a "send me the book" submission server-side, applies spam controls, creates
// a signed time-limited download link (no personal data, no storage required for the
// link itself), records the lead, and emails the visitor their copy.
//
// Required env vars: BOOK_LINK_SECRET, RESEND_API_KEY, RESEND_FROM_EMAIL, PUBLIC_BASE_URL.
// Optional: LEAD_NOTIFY_EMAIL, SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY,
// GA_MEASUREMENT_ID, GA_MEASUREMENT_API_SECRET. See CLAUDE.md for what each does.

const { validateBookRequest } = require("./_lib/validate");
const { createDownloadToken } = require("./_lib/token");
const { sendBookDeliveryEmail, sendLeadNotification, isConfigured: emailConfigured } = require("./_lib/email");
const { storeLead } = require("./_lib/leads");
const { hit, honeypotTripped, submittedTooFast } = require("./_lib/ratelimit");

function clientIp(req) {
  const fwd = req.headers["x-forwarded-for"];
  if (typeof fwd === "string" && fwd.length) return fwd.split(",")[0].trim();
  return req.socket && req.socket.remoteAddress ? req.socket.remoteAddress : "unknown";
}

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");

  if (req.method !== "POST") {
    res.status(405).json({ ok: false, error: "Method not allowed" });
    return;
  }

  let body = req.body;
  if (typeof body === "string") {
    try {
      body = JSON.parse(body);
    } catch (e) {
      res.status(400).json({ ok: false, error: "Invalid request body" });
      return;
    }
  }
  body = body || {};

  // Spam controls: honeypot, plausible fill time, then per-IP and per-email rate limits.
  if (honeypotTripped(body)) {
    res.status(200).json({ ok: true }); // pretend success so bots don't learn anything
    return;
  }
  if (submittedTooFast(body.started_at, 1500, 30 * 60 * 1000)) {
    res.status(400).json({ ok: false, error: "Please try submitting the form again." });
    return;
  }

  const ip = clientIp(req);
  if (!hit("ip:" + ip, 8, 10 * 60 * 1000)) {
    res.status(429).json({ ok: false, error: "Too many requests. Please try again in a few minutes." });
    return;
  }

  const result = validateBookRequest(body);
  if (!result.ok) {
    res.status(400).json({ ok: false, error: result.errors[0], errors: result.errors });
    return;
  }
  const { name, email, phone, zip, consentMarketing } = result.data;

  if (!hit("email:" + email, 3, 24 * 60 * 60 * 1000)) {
    res.status(429).json({ ok: false, error: "This email has already requested the book recently. Check your inbox, or call us if you need help." });
    return;
  }

  if (!emailConfigured()) {
    // Fail honestly rather than pretend the book was sent.
    res.status(503).json({
      ok: false,
      error: "Book delivery isn't configured yet. Please call us and we'll get the guide to you directly.",
    });
    return;
  }

  const baseUrl = (process.env.PUBLIC_BASE_URL || "https://www.ecosinsurancesolutions.com").replace(/\/+$/, "");
  const token = createDownloadToken();
  const downloadUrl = baseUrl + "/api/download-book?token=" + encodeURIComponent(token);

  const pageUrl = typeof body.page_url === "string" ? body.page_url.slice(0, 300) : undefined;

  try {
    await sendBookDeliveryEmail({ to: email, name, downloadUrl });
  } catch (e) {
    res.status(502).json({ ok: false, error: "We couldn't send the email just now. Please try again shortly." });
    return;
  }

  // Lead capture happens after the visitor-facing email succeeds and is never allowed
  // to fail the request — a storage or notification hiccup shouldn't make a visitor
  // think they didn't get their book.
  try {
    const stored = await storeLead({ name, email, phone, zip, consentMarketing, pageUrl, source: "book-request" });
    if (!stored.stored) {
      await sendLeadNotification({ name, email, phone, zip, consentMarketing, pageUrl });
    }
  } catch (e) {
    try {
      await sendLeadNotification({ name, email, phone, zip, consentMarketing, pageUrl });
    } catch (e2) {
      // Both paths failed; nothing more we can do without risking the visitor-facing response.
    }
  }

  res.status(200).json({ ok: true });
};
