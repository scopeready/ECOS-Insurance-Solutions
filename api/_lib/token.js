// Stateless, signed download tokens for the book delivery link.
// No external storage is required: the token carries only a non-identifying random id
// and an expiry, HMAC-signed so it cannot be forged or altered. It never carries the
// visitor's name, email, phone or ZIP, so no personal information ever appears in a URL.

const crypto = require("crypto");

function getSecret() {
  const secret = process.env.BOOK_LINK_SECRET;
  if (!secret) throw new Error("BOOK_LINK_SECRET is not configured");
  return secret;
}

function base64url(input) {
  return Buffer.from(input).toString("base64url");
}

function sign(payload) {
  const secret = getSecret();
  const body = base64url(JSON.stringify(payload));
  const sig = crypto.createHmac("sha256", secret).update(body).digest("base64url");
  return body + "." + sig;
}

// Creates a download token valid for `ttlMs` milliseconds (default 7 days).
function createDownloadToken(ttlMs) {
  const exp = Date.now() + (ttlMs || 7 * 24 * 60 * 60 * 1000);
  const nonce = crypto.randomBytes(9).toString("base64url");
  return sign({ exp, nonce });
}

// Verifies a token's signature and expiry. Returns { ok: true } or { ok: false, reason }.
function verifyDownloadToken(token) {
  if (typeof token !== "string" || token.indexOf(".") === -1) {
    return { ok: false, reason: "malformed" };
  }
  const secret = getSecret();
  const [body, sig] = token.split(".");
  const expectedSig = crypto.createHmac("sha256", secret).update(body).digest("base64url");
  const sigBuf = Buffer.from(sig || "");
  const expectedBuf = Buffer.from(expectedSig);
  if (sigBuf.length !== expectedBuf.length || !crypto.timingSafeEqual(sigBuf, expectedBuf)) {
    return { ok: false, reason: "bad-signature" };
  }
  let payload;
  try {
    payload = JSON.parse(Buffer.from(body, "base64url").toString("utf8"));
  } catch (e) {
    return { ok: false, reason: "malformed" };
  }
  if (typeof payload.exp !== "number" || Date.now() > payload.exp) {
    return { ok: false, reason: "expired" };
  }
  return { ok: true };
}

module.exports = { createDownloadToken, verifyDownloadToken };
