// GET /api/download-book?token=...
// Serves the book PDF only for a valid, unexpired signed token. The token carries no
// personal information, so nothing sensitive ever appears in this URL or in logs.
//
// The PDF is never a plain static file on the site: its bytes live base64-encoded
// inside api/_lib/book-pdf-base64.js (an underscore-prefixed module, so Vercel never
// turns it into a routable function or serves it as a static asset — the only way to
// get the file out is to ask this endpoint for it with a valid token). The editable
// source copy lives at docs/retire-with-confidence-2026.pdf, which is excluded from
// deployment entirely by .vercelignore.

const { verifyDownloadToken } = require("./_lib/token");
const { trackServerEvent } = require("./_lib/ga");
const PDF_BASE64 = require("./_lib/book-pdf-base64");

const DOWNLOAD_FILENAME = "retire-with-confidence-2026.pdf";

module.exports = async (req, res) => {
  res.setHeader("Cache-Control", "no-store");

  const token = typeof req.query.token === "string" ? req.query.token : "";
  const verified = verifyDownloadToken(token);
  if (!verified.ok) {
    res.status(410).send(
      "This download link is no longer valid. Requesting the book again from the site will send you a fresh link."
    );
    return;
  }

  let pdf;
  try {
    pdf = Buffer.from(PDF_BASE64, "base64");
  } catch (e) {
    res.status(500).send("The book is temporarily unavailable. Please try again shortly or call us.");
    return;
  }

  trackServerEvent("book_download_link_clicked", {}); // fire-and-forget, no PII, never blocks the response

  res.setHeader("Content-Type", "application/pdf");
  res.setHeader("Content-Disposition", 'attachment; filename="' + DOWNLOAD_FILENAME + '"');
  res.setHeader("Content-Length", String(pdf.length));
  res.status(200).send(pdf);
};
