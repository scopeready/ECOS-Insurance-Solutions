// Server-side GA4 event for the one interaction our client-side JS can never see: a
// click on the download link inside the delivery email. No-op unless both env vars are
// set, and the payload never carries a name, email, phone or ZIP.
//
// Requires (both from GA4 Admin -> Data Streams -> Measurement Protocol API secrets):
//   GA_MEASUREMENT_ID          e.g. G-7CXH7ZLSP1 (same property already used site-wide)
//   GA_MEASUREMENT_API_SECRET  a Measurement Protocol API secret for that stream

const crypto = require("crypto");

async function trackServerEvent(name, params) {
  const measurementId = process.env.GA_MEASUREMENT_ID;
  const apiSecret = process.env.GA_MEASUREMENT_API_SECRET;
  if (!measurementId || !apiSecret) return; // not configured; never blocks the request

  const clientId = crypto.randomBytes(16).toString("hex"); // anonymous, not tied to the visitor
  const url =
    "https://www.google-analytics.com/mp/collect?measurement_id=" +
    encodeURIComponent(measurementId) +
    "&api_secret=" +
    encodeURIComponent(apiSecret);
  try {
    await fetch(url, {
      method: "POST",
      body: JSON.stringify({
        client_id: clientId,
        events: [{ name, params: params || {} }],
      }),
    });
  } catch (e) {
    // Analytics must never break the actual download.
  }
}

module.exports = { trackServerEvent };
