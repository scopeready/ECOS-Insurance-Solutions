/*
 * Retire With Confidence — book request modal + respectful offer popup.
 * Self-contained, dependency-free. Talks to /api/request-book (server-side validated,
 * rate-limited, and gated behind a signed one-time-use-style download link emailed to
 * the visitor). No personal information is ever placed in a URL or sent to analytics.
 */
(function () {
  "use strict";

  var EXCLUDED_PATH_FRAGMENTS = ["/privacy", "/terms", "/thank-you", "/404"];
  var MIN_DELAY_MS = 15000;
  var TIME_FALLBACK_MS = 25000;
  var SCROLL_FRACTION = 0.5;
  var DISMISS_DAYS = 30;
  var LS_DISMISS = "ecosBookDismissUntil";
  var LS_SUBMITTED = "ecosBookSubmitted";

  function safeLS(fn, fallback) {
    try {
      return fn();
    } catch (e) {
      return fallback;
    }
  }

  function isExcludedPage() {
    var path = window.location.pathname || "";
    for (var i = 0; i < EXCLUDED_PATH_FRAGMENTS.length; i++) {
      if (path.indexOf(EXCLUDED_PATH_FRAGMENTS[i]) !== -1) return true;
    }
    return false;
  }

  function track(name, params) {
    if (typeof window.gtag === "function") {
      window.gtag("event", name, params || {});
    }
  }

  function injectStyle() {
    var css =
      ".ecos-book-overlay{position:fixed;inset:0;background:rgba(10,31,64,.55);display:flex;align-items:center;justify-content:center;z-index:9999;padding:16px}" +
      ".ecos-book-modal{background:#fff;border-radius:14px;max-width:460px;width:100%;max-height:90vh;overflow:auto;padding:28px;position:relative;font-family:var(--body,'IBM Plex Sans',system-ui,sans-serif);box-shadow:0 24px 60px rgba(10,31,64,.35)}" +
      ".ecos-book-modal h2{font-family:var(--display,'Red Hat Display',system-ui,sans-serif);color:var(--navy,#0F2D5A);font-size:1.4rem;margin:0 0 6px}" +
      ".ecos-book-modal p.sub{color:var(--muted,#4A4F57);margin:0 0 18px;font-size:.98rem}" +
      ".ecos-book-modal-head{display:flex;gap:14px;align-items:flex-start;margin-bottom:18px}" +
      ".ecos-book-modal-head h2{margin:0 0 6px}" +
      ".ecos-book-modal-head p.sub{margin:0}" +
      ".ecos-book-cover-thumb{flex:0 0 auto;width:64px;height:auto;border-radius:5px;box-shadow:0 8px 20px rgba(10,31,64,.3)}" +
      ".ecos-book-modal label{display:block;font-weight:600;font-size:.92rem;margin:12px 0 4px;color:var(--ink,#1D2129)}" +
      ".ecos-book-modal input[type=text],.ecos-book-modal input[type=email],.ecos-book-modal input[type=tel]{width:100%;font:inherit;font-size:1rem;padding:11px 13px;border:1px solid #BFC3C9;border-radius:8px}" +
      ".ecos-book-modal .consent{display:flex;gap:9px;align-items:flex-start;margin:14px 0;font-size:.86rem;color:var(--muted,#4A4F57)}" +
      ".ecos-book-modal .consent input{width:auto;margin-top:4px}" +
      ".ecos-book-modal .hp{position:absolute;left:-9999px;top:-9999px}" +
      ".ecos-book-submit{margin-top:16px;width:100%;background:var(--gold,#C6A15B);color:var(--navy-deep,#0A1F40);border:none;border-radius:9px;padding:13px 18px;font-weight:700;font-size:1.02rem;cursor:pointer}" +
      ".ecos-book-submit:disabled{opacity:.6;cursor:default}" +
      ".ecos-book-close{position:absolute;top:12px;right:12px;background:none;border:none;font-size:1.3rem;line-height:1;cursor:pointer;color:var(--muted,#4A4F57);padding:6px}" +
      ".ecos-book-close:focus-visible,.ecos-book-submit:focus-visible,.ecos-book-modal input:focus-visible{outline:3px solid var(--gold-deep,#8A6A2B);outline-offset:2px}" +
      ".ecos-book-error{color:#9B2226;font-size:.9rem;margin-top:10px;display:none}" +
      ".ecos-book-error.show{display:block}" +
      ".ecos-book-success{text-align:center;padding:8px 0}" +
      ".ecos-book-success h2{margin-bottom:10px}" +
      ".ecos-book-popup{position:fixed;right:18px;bottom:18px;max-width:340px;background:#fff;border:1px solid #E3DCCF;border-radius:14px;box-shadow:0 14px 34px rgba(10,31,64,.25);padding:18px 18px 16px;z-index:9998;font-family:var(--body,'IBM Plex Sans',system-ui,sans-serif);transform:translateY(12px);opacity:0;transition:transform .3s ease,opacity .3s ease;pointer-events:none}" +
      ".ecos-book-popup.show{transform:translateY(0);opacity:1;pointer-events:auto}" +
      ".ecos-book-popup .eyebrow{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gold-deep,#8A6A2B);font-weight:700;margin-bottom:.4em}" +
      ".ecos-book-popup h3{font-family:var(--display,'Red Hat Display',system-ui,sans-serif);color:var(--navy,#0F2D5A);font-size:1.08rem;margin:0 0 6px}" +
      ".ecos-book-popup-head{display:flex;gap:10px;align-items:flex-start;margin-bottom:2px}" +
      ".ecos-book-popup-head .eyebrow{margin-bottom:.2em}" +
      ".ecos-book-popup-head h3{margin:0}" +
      ".ecos-book-popup p{font-size:.9rem;color:var(--muted,#4A4F57);margin:0 0 12px}" +
      ".ecos-book-popup .row{display:flex;gap:10px;align-items:center}" +
      ".ecos-book-popup button.cta{background:var(--gold,#C6A15B);color:var(--navy-deep,#0A1F40);border:none;border-radius:8px;padding:10px 14px;font-weight:700;font-size:.92rem;cursor:pointer}" +
      ".ecos-book-popup .ecos-book-close{position:absolute;top:8px;right:8px}" +
      ".ecos-book-popup{position:fixed}" +
      "@media (max-width:640px){.ecos-book-popup{left:0;right:0;bottom:0;max-width:none;border-radius:14px 14px 0 0;padding-bottom:20px}}" +
      "@media (prefers-reduced-motion:reduce){.ecos-book-popup{transition:none}}";
    var style = document.createElement("style");
    style.setAttribute("data-ecos-book", "");
    style.textContent = css;
    document.head.appendChild(style);
  }

  var lastFocused = null;

  function trapFocus(container, evt) {
    if (evt.key !== "Tab") return;
    var focusable = container.querySelectorAll(
      'a[href],button:not([disabled]),input:not([disabled]),select,[tabindex]:not([tabindex="-1"])'
    );
    if (!focusable.length) return;
    var first = focusable[0],
      last = focusable[focusable.length - 1];
    if (evt.shiftKey && document.activeElement === first) {
      evt.preventDefault();
      last.focus();
    } else if (!evt.shiftKey && document.activeElement === last) {
      evt.preventDefault();
      first.focus();
    }
  }

  function buildModal() {
    var overlay = document.createElement("div");
    overlay.className = "ecos-book-overlay";
    overlay.setAttribute("role", "presentation");
    overlay.style.display = "none";

    var modal = document.createElement("div");
    modal.className = "ecos-book-modal";
    modal.setAttribute("role", "dialog");
    modal.setAttribute("aria-modal", "true");
    modal.setAttribute("aria-labelledby", "ecosBookTitle");

    modal.innerHTML =
      '<button type="button" class="ecos-book-close" aria-label="Close">&times;</button>' +
      '<div class="ecos-book-form-view">' +
      '<div class="ecos-book-modal-head">' +
      '<img class="ecos-book-cover-thumb" src="/assets/book-cover.webp" alt="Retire With Confidence book cover" width="64" height="96">' +
      '<div>' +
      '<h2 id="ecosBookTitle">Get your free copy of Retire With Confidence</h2>' +
      '<p class="sub">The Medicare Guide &mdash; 295 pages, 2026 Edition. We\'ll email your download link.</p>' +
      '</div>' +
      '</div>' +
      '<form novalidate>' +
      '<label for="ecosBookName">Full name</label>' +
      '<input id="ecosBookName" name="name" type="text" autocomplete="name" required maxlength="100">' +
      '<label for="ecosBookEmail">Email address</label>' +
      '<input id="ecosBookEmail" name="email" type="email" autocomplete="email" required maxlength="254">' +
      '<label for="ecosBookPhone">Phone number</label>' +
      '<input id="ecosBookPhone" name="phone" type="tel" autocomplete="tel" required maxlength="20">' +
      '<label for="ecosBookZip">ZIP code</label>' +
      '<input id="ecosBookZip" name="zip" type="text" inputmode="numeric" autocomplete="postal-code" required maxlength="10">' +
      '<div><input class="hp" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true"></div>' +
      '<label class="consent"><input type="checkbox" name="consent_marketing"><span>Yes, I\'d also like a licensed agent to reach out about Medicare plan options by phone, text or email. Optional &mdash; leave unchecked to just get the book. See our <a href="/privacy" target="_blank" rel="noopener">Privacy Policy</a>.</span></label>' +
      '<button type="submit" class="ecos-book-submit">Send me the book</button>' +
      '<p class="ecos-book-error" role="alert"></p>' +
      '<p class="gov" style="font-size:.82rem;color:var(--muted,#4A4F57);margin-top:12px">ECOS Medicare Solutions is not connected with or endorsed by the United States government or the federal Medicare program. This is a solicitation for insurance.</p>' +
      "</form>" +
      "</div>" +
      '<div class="ecos-book-success" style="display:none">' +
      "<h2>Check your email</h2>" +
      "<p>We've sent your copy of <em>Retire With Confidence</em> to the address you provided. It should arrive within a few minutes &mdash; check spam if you don't see it.</p>" +
      '<button type="button" class="ecos-book-submit ecos-book-done">Close</button>' +
      "</div>";

    overlay.appendChild(modal);
    document.body.appendChild(overlay);

    var formView = modal.querySelector(".ecos-book-form-view");
    var successView = modal.querySelector(".ecos-book-success");
    var form = modal.querySelector("form");
    var errorEl = modal.querySelector(".ecos-book-error");
    var submitBtn = modal.querySelector(".ecos-book-submit");
    var startedAt = null;

    function openedFromExcludedCheck() {
      return false;
    }

    function open(trigger) {
      lastFocused = document.activeElement;
      overlay.style.display = "flex";
      startedAt = Date.now();
      form.reset();
      formView.style.display = "";
      successView.style.display = "none";
      errorEl.classList.remove("show");
      submitBtn.disabled = false;
      submitBtn.textContent = "Send me the book";
      document.addEventListener("keydown", onKeydown, true);
      var firstField = modal.querySelector("#ecosBookName");
      if (firstField) firstField.focus();
      track("book_form_opened", { trigger: trigger || "cta" });
    }

    function close() {
      overlay.style.display = "none";
      document.removeEventListener("keydown", onKeydown, true);
      if (lastFocused && typeof lastFocused.focus === "function") lastFocused.focus();
    }

    function onKeydown(evt) {
      if (evt.key === "Escape") {
        close();
        return;
      }
      trapFocus(modal, evt);
    }

    overlay.addEventListener("mousedown", function (evt) {
      if (evt.target === overlay) close();
    });
    modal.querySelectorAll(".ecos-book-close, .ecos-book-done").forEach(function (btn) {
      btn.addEventListener("click", close);
    });

    form.addEventListener("submit", function (evt) {
      evt.preventDefault();
      errorEl.classList.remove("show");
      var data = {
        name: form.name.value,
        email: form.email.value,
        phone: form.phone.value,
        zip: form.zip.value,
        website: form.website.value,
        consent_marketing: form.consent_marketing.checked,
        started_at: startedAt,
        page_url: window.location.href,
      };
      submitBtn.disabled = true;
      submitBtn.textContent = "Sending…";
      fetch("/api/request-book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data),
      })
        .then(function (r) {
          return r.json().then(function (json) {
            return { status: r.status, json: json };
          });
        })
        .then(function (res) {
          if (res.status === 200 && res.json && res.json.ok) {
            formView.style.display = "none";
            successView.style.display = "";
            safeLS(function () {
              localStorage.setItem(LS_SUBMITTED, "1");
            });
            track("book_request_succeeded", {});
          } else {
            var msg = (res.json && res.json.error) || "Something went wrong. Please try again.";
            errorEl.textContent = msg;
            errorEl.classList.add("show");
            submitBtn.disabled = false;
            submitBtn.textContent = "Send me the book";
            track("book_request_failed", {});
          }
        })
        .catch(function () {
          errorEl.textContent = "Network error. Please try again, or call us.";
          errorEl.classList.add("show");
          submitBtn.disabled = false;
          submitBtn.textContent = "Send me the book";
          track("book_request_failed", {});
        });
    });

    return { open: open, close: close };
  }

  function buildPopup(onOpenModal) {
    var popup = document.createElement("div");
    popup.className = "ecos-book-popup";
    popup.setAttribute("role", "dialog");
    popup.setAttribute("aria-label", "Free book offer");
    popup.innerHTML =
      '<button type="button" class="ecos-book-close" aria-label="Dismiss">&times;</button>' +
      '<div class="ecos-book-popup-head">' +
      '<img class="ecos-book-cover-thumb" src="/assets/book-cover.webp" alt="" width="48" height="72">' +
      '<div><p class="eyebrow">Free Book</p>' +
      "<h3>Retire With Confidence</h3></div>" +
      "</div>" +
      "<p>295 pages on Medicare, decided in plain English. Get your free copy by email.</p>" +
      '<div class="row"><button type="button" class="cta">Get the free book</button></div>';
    document.body.appendChild(popup);

    popup.querySelector(".cta").addEventListener("click", function () {
      hide();
      onOpenModal("popup");
    });
    popup.querySelector(".ecos-book-close").addEventListener("click", function () {
      hide();
      safeLS(function () {
        localStorage.setItem(LS_DISMISS, String(Date.now() + DISMISS_DAYS * 24 * 60 * 60 * 1000));
      });
    });
    popup.addEventListener("keydown", function (evt) {
      if (evt.key === "Escape") {
        hide();
        safeLS(function () {
          localStorage.setItem(LS_DISMISS, String(Date.now() + DISMISS_DAYS * 24 * 60 * 60 * 1000));
        });
      }
    });

    function show() {
      popup.classList.add("show");
      track("book_offer_displayed", {});
    }
    function hide() {
      popup.classList.remove("show");
    }

    return { show: show, hide: hide };
  }

  function scheduleAutoPopup(popupApi) {
    if (isExcludedPage()) return;
    var submitted = safeLS(function () {
      return localStorage.getItem(LS_SUBMITTED);
    }, null);
    if (submitted) return;
    var dismissUntil = Number(
      safeLS(function () {
        return localStorage.getItem(LS_DISMISS);
      }, 0)
    );
    if (dismissUntil && Date.now() < dismissUntil) return;

    var shown = false;
    var scrolled = false;
    var timeReached = false;
    var loadTime = Date.now();

    function maybeShow() {
      if (shown) return;
      if (Date.now() - loadTime < MIN_DELAY_MS) return;
      if (!scrolled && !timeReached) return;
      shown = true;
      popupApi.show();
      window.removeEventListener("scroll", onScroll);
    }

    function onScroll() {
      var doc = document.documentElement;
      var scrollableHeight = (doc.scrollHeight || 0) - window.innerHeight;
      if (scrollableHeight <= 0) return;
      var fraction = window.scrollY / scrollableHeight;
      if (fraction >= SCROLL_FRACTION) {
        scrolled = true;
        maybeShow();
      }
    }

    window.addEventListener("scroll", onScroll, { passive: true });
    setTimeout(function () {
      timeReached = true;
      maybeShow();
    }, TIME_FALLBACK_MS);
    setTimeout(maybeShow, MIN_DELAY_MS);
  }

  function init() {
    injectStyle();
    var modalApi = buildModal();
    var popupApi = buildPopup(modalApi.open);

    document.querySelectorAll(".js-book-open").forEach(function (btn) {
      btn.addEventListener("click", function () {
        modalApi.open("cta");
      });
    });

    scheduleAutoPopup(popupApi);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
