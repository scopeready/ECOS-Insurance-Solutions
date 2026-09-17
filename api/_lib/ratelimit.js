// Best-effort in-process rate limiting. A serverless function instance is reused across
// nearby invocations but not shared across regions or cold starts, so this is a
// defense-in-depth layer, not the primary control — the primary control should be a
// Vercel Firewall rate-limit rule on /api/request-book (configured in the dashboard,
// no code or secrets required). See the deployment notes in CLAUDE.md.

const buckets = new Map();
const MAX_ENTRIES = 5000; // crude cap so the map can't grow unbounded between cold starts

function hit(key, limit, windowMs) {
  const now = Date.now();
  let bucket = buckets.get(key);
  if (!bucket || now - bucket.start > windowMs) {
    bucket = { start: now, count: 0 };
    if (buckets.size > MAX_ENTRIES) buckets.clear();
    buckets.set(key, bucket);
  }
  bucket.count += 1;
  return bucket.count <= limit;
}

// True if the honeypot field was filled (bots that autofill every field trip this).
function honeypotTripped(body) {
  return !!(body && typeof body === "object" && body.website);
}

// True if the form was submitted implausibly fast after it was opened, or the
// opened-at timestamp is missing/stale — a common signature of scripted submissions.
function submittedTooFast(startedAt, minMs, maxMs) {
  const n = Number(startedAt);
  if (!Number.isFinite(n)) return true;
  const elapsed = Date.now() - n;
  return elapsed < minMs || elapsed > maxMs;
}

module.exports = { hit, honeypotTripped, submittedTooFast };
