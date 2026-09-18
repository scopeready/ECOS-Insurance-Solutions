// Transactional email via Resend's HTTP API (https://resend.com). No SDK dependency —
// this is a static site with no build step, so every API function uses only the
// platform's built-in fetch and Node builtins.
//
// Requires env vars:
//   RESEND_API_KEY    - secret API key from the Resend dashboard
//   RESEND_FROM_EMAIL - a "Name <address@domain>" sender on a domain verified in Resend
// Both must be set in Vercel Project Settings -> Environment Variables. Nothing here
// is hard-coded.

const NAVY = "#0F2D5A";
const NAVY_DEEP = "#0A1F40";
const GOLD = "#C6A15B";
const GROUND = "#F7F2E8";

function isConfigured() {
  return !!(process.env.RESEND_API_KEY && process.env.RESEND_FROM_EMAIL);
}

async function sendEmail({ to, subject, html, text, replyTo }) {
  if (!isConfigured()) {
    throw new Error("Email delivery is not configured (RESEND_API_KEY / RESEND_FROM_EMAIL)");
  }
  const res = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: "Bearer " + process.env.RESEND_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      from: process.env.RESEND_FROM_EMAIL,
      to: [to],
      subject,
      html,
      text,
      reply_to: replyTo || undefined,
    }),
  });
  if (!res.ok) {
    const detail = await res.text().catch(() => "");
    throw new Error("Resend API error " + res.status + ": " + detail.slice(0, 300));
  }
  return res.json();
}

function shell(bodyHtml) {
  return (
    '<div style="background:' + GROUND + ';padding:32px 16px;font-family:Georgia,\'Times New Roman\',serif">' +
    '<div style="max-width:560px;margin:0 auto;background:#ffffff;border-radius:12px;overflow:hidden;border:1px solid #E3DCCF">' +
    '<div style="background:' + NAVY + ';padding:22px 28px">' +
    '<span style="color:#ffffff;font-family:Arial,Helvetica,sans-serif;font-weight:700;font-size:18px;letter-spacing:.02em">ECOS Medicare Solutions</span>' +
    "</div>" +
    '<div style="padding:28px 28px 8px;color:#1D2129;font-size:16px;line-height:1.55">' +
    bodyHtml +
    "</div>" +
    '<div style="padding:20px 28px 26px;color:#6E7480;font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;border-top:1px solid #EFE9DE;margin-top:12px">' +
    "ECOS Medicare Solutions is not connected with or endorsed by the United States government or the federal Medicare program. " +
    "This is a solicitation for insurance. A licensed insurance agent may contact you." +
    "</div>" +
    "</div>" +
    "</div>"
  );
}

// The delivery email: focused on handing over the book, nothing else competing for attention.
async function sendBookDeliveryEmail({ to, name, downloadUrl }) {
  const firstName = (name || "").split(" ")[0] || "there";
  const html = shell(
    '<h1 style="font-family:Georgia,\'Times New Roman\',serif;color:' + NAVY + ';font-size:22px;margin:0 0 14px">Your copy of Retire With Confidence is ready</h1>' +
    "<p>Hi " + firstName + ",</p>" +
    "<p>Thanks for requesting <em>Retire With Confidence: The Medicare Guide</em>. Your copy is ready to download below.</p>" +
    '<p style="text-align:center;margin:28px 0">' +
    '<a href="' + downloadUrl + '" style="background:' + GOLD + ';color:' + NAVY_DEEP + ';font-family:Arial,Helvetica,sans-serif;font-weight:700;text-decoration:none;padding:14px 28px;border-radius:8px;display:inline-block">Download Your Book (PDF)</a>' +
    "</p>" +
    '<p style="font-size:13px;color:#6E7480">This link is unique to you and expires in 7 days. If it stops working, just reply to this email and we\'ll send a fresh copy.</p>' +
    "<p>If you'd like help applying anything in the guide to your own situation, a licensed agent on our team is glad to walk through it with you at no cost &mdash; just reply to this email or call the number on our site.</p>" +
    "<p>&mdash; ECOS Medicare Solutions</p>"
  );
  const text =
    "Hi " + firstName + ",\n\n" +
    "Thanks for requesting Retire With Confidence: The Medicare Guide. Download your copy here (link expires in 7 days):\n" +
    downloadUrl +
    "\n\nIf you'd like help applying anything in the guide to your situation, just reply to this email.\n\n" +
    "-- ECOS Medicare Solutions";
  return sendEmail({ to, subject: "Your copy of Retire With Confidence is ready", html, text });
}

// Internal notification so a lead is never silently lost while a CRM/lead-storage
// integration is being configured. Sent to LEAD_NOTIFY_EMAIL, never to the visitor.
async function sendLeadNotification({ name, email, phone, zip, consentMarketing, pageUrl }) {
  const to = process.env.LEAD_NOTIFY_EMAIL;
  if (!to) return; // no-op until an internal recipient is configured
  const html = shell(
    '<h2 style="font-family:Arial,Helvetica,sans-serif;color:' + NAVY + ';font-size:18px;margin:0 0 14px">New book request</h2>' +
    '<table style="font-family:Arial,Helvetica,sans-serif;font-size:14px;width:100%;border-collapse:collapse">' +
    row("Name", name) +
    row("Email", email) +
    row("Phone", phone) +
    row("ZIP", zip) +
    row("Wants marketing contact", consentMarketing ? "Yes" : "No") +
    row("Page", pageUrl || "") +
    "</table>"
  );
  return sendEmail({ to, subject: "New Retire With Confidence book request", html, text: JSON.stringify({ name, email, phone, zip, consentMarketing }) });
}

function row(label, value) {
  return (
    '<tr><td style="padding:4px 10px 4px 0;color:#6E7480;white-space:nowrap">' + label + '</td>' +
    '<td style="padding:4px 0;color:#1D2129">' + escapeHtml(String(value == null ? "" : value)) + "</td></tr>"
  );
}

function escapeHtml(s) {
  return s.replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

module.exports = { isConfigured, sendBookDeliveryEmail, sendLeadNotification };
