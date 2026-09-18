// Server-side validation and sanitization for the book-request lead form.
// Every field submitted by a browser is untrusted; this is the only place that decides
// what is safe to store, email, or log.

const NAME_RE = /^[\p{L}\p{M}' .-]{2,100}$/u;
const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
const ZIP_RE = /^\d{5}(-\d{4})?$/;

function cleanString(v, max) {
  if (typeof v !== "string") return "";
  return v.replace(/[\r\n\t]+/g, " ").trim().slice(0, max);
}

function digitsOnly(v) {
  return typeof v === "string" ? v.replace(/\D+/g, "") : "";
}

// Formats a validated 10 or 11 digit US number as "(XXX) XXX-XXXX"; returns null if invalid.
function formatUsPhone(raw) {
  let d = digitsOnly(raw);
  if (d.length === 11 && d.startsWith("1")) d = d.slice(1);
  if (d.length !== 10) return null;
  return "(" + d.slice(0, 3) + ") " + d.slice(3, 6) + "-" + d.slice(6);
}

// Validates and normalizes a book-request submission.
// Returns { ok: true, data } or { ok: false, errors: string[] }.
function validateBookRequest(body) {
  const errors = [];
  body = body && typeof body === "object" ? body : {};

  const name = cleanString(body.name, 100);
  if (!NAME_RE.test(name)) errors.push("Please enter your full name.");

  const email = cleanString(body.email, 254).toLowerCase();
  if (!EMAIL_RE.test(email)) errors.push("Please enter a valid email address.");

  const phone = formatUsPhone(body.phone);
  if (!phone) errors.push("Please enter a valid 10-digit US phone number.");

  const zip = cleanString(body.zip, 10);
  if (!ZIP_RE.test(zip)) errors.push("Please enter a valid 5-digit ZIP code.");

  const consentMarketing = body.consent_marketing === true || body.consent_marketing === "true";

  if (errors.length) return { ok: false, errors };
  return {
    ok: true,
    data: { name, email, phone, zip: zip.slice(0, 5), consentMarketing },
  };
}

module.exports = { validateBookRequest, cleanString, digitsOnly };
