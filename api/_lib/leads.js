// Optional persistent lead storage. Nothing here is invented or hard-coded: if
// SUPABASE_URL and SUPABASE_SERVICE_ROLE_KEY are not both set in the Vercel project's
// environment variables, storeLead() is a no-op and the caller falls back to the
// internal email notification in email.js so no lead is silently lost.
//
// Deliberately uses the service-role key from the server only. The repo's earlier,
// now-legacy client-side Supabase handler (arizona/assets/site.js) posted with a
// public anon key straight from the browser; that pattern is not reused here.

function isConfigured() {
  return !!(process.env.SUPABASE_URL && process.env.SUPABASE_SERVICE_ROLE_KEY);
}

async function storeLead({ name, email, phone, zip, consentMarketing, pageUrl, source }) {
  if (!isConfigured()) return { stored: false, reason: "not-configured" };
  const url = process.env.SUPABASE_URL.replace(/\/+$/, "") + "/rest/v1/website_leads";
  const res = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      apikey: process.env.SUPABASE_SERVICE_ROLE_KEY,
      Authorization: "Bearer " + process.env.SUPABASE_SERVICE_ROLE_KEY,
      Prefer: "return=minimal",
    },
    body: JSON.stringify({
      full_name: name,
      email,
      phone,
      zip_code: zip,
      permission_to_contact: !!consentMarketing,
      source: source || "book-request",
      page_url: pageUrl || null,
    }),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => "");
    throw new Error("Supabase insert failed " + res.status + ": " + detail.slice(0, 300));
  }
  return { stored: true };
}

module.exports = { isConfigured, storeLead };
