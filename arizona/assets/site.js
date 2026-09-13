/* Medicare Enrollment Arizona — shared site JS (guarded for all pages) */
(function () {
  "use strict";

  // current year
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = new Date().getFullYear();

  // mobile menu
  var hamb = document.getElementById("hamb");
  var navlinks = document.getElementById("navlinks");
  if (hamb && navlinks) {
    hamb.addEventListener("click", function () {
      var open = navlinks.classList.toggle("open");
      hamb.setAttribute("aria-expanded", open ? "true" : "false");
    });
    navlinks.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        navlinks.classList.remove("open");
        hamb.setAttribute("aria-expanded", "false");
      });
    });
  }

  // cost tabs
  var tabs = document.querySelectorAll(".tab");
  if (tabs.length) {
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        tabs.forEach(function (t) { t.setAttribute("aria-selected", "false"); });
        document.querySelectorAll(".panel").forEach(function (p) { p.classList.remove("active"); });
        tab.setAttribute("aria-selected", "true");
        var target = document.getElementById(tab.getAttribute("aria-controls"));
        if (target) target.classList.add("active");
      });
    });
  }

  // FAQ category filter
  var cats = document.querySelectorAll(".faqcat");
  if (cats.length) {
    var items = document.querySelectorAll("#faqList .qa");
    cats.forEach(function (c) {
      c.addEventListener("click", function () {
        cats.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        c.setAttribute("aria-pressed", "true");
        var cat = c.dataset.cat;
        items.forEach(function (it) {
          var show = cat === "all" || it.dataset.cat === cat;
          it.style.display = show ? "" : "none";
          if (!show) it.removeAttribute("open");
        });
      });
    });
  }

  // Initial Enrollment Period tool
  var iepBtn = document.getElementById("iepBtn");
  if (iepBtn) {
    var ySel = document.getElementById("iepYear");
    var nowY = new Date().getFullYear();
    for (var y = nowY - 1; y <= nowY + 3; y++) {
      var o = document.createElement("option");
      o.value = y; o.textContent = y; ySel.appendChild(o);
    }
    var months = ["January","February","March","April","May","June","July","August","September","October","November","December"];
    function monthLabel(idx, yr) {
      var m = ((idx % 12) + 12) % 12;
      var yy = yr + Math.floor(idx / 12);
      return months[m] + " " + yy;
    }
    iepBtn.addEventListener("click", function () {
      var m = document.getElementById("iepMonth").value;
      var yv = ySel.value;
      var res = document.getElementById("iepResult");
      if (m === "" || yv === "") {
        res.innerHTML = "<strong>Please choose both a month and a year.</strong>";
        res.classList.add("show"); return;
      }
      var mi = parseInt(m, 10), yr2 = parseInt(yv, 10);
      var start = monthLabel(mi - 3, yr2);
      var end = monthLabel(mi + 3, yr2);
      var birth = months[mi] + " " + yr2;
      res.innerHTML =
        "<div>Your <strong>Initial Enrollment Period</strong> runs:</div>" +
        "<div class='win'>" + start + " &nbsp;\u2192&nbsp; " + end + "</div>" +
        "<div>That's the 3 months before, the month of, and the 3 months after your 65th birthday in <strong>" + birth + "</strong>. " +
        "Enroll in the first 3 months for coverage to start as early as " + months[mi] + " " + yr2 + ". " +
        "Questions? Call Darin Weidauer at ECOS Medicare Solutions at <strong>602-935-4382</strong>, or Arizona SHIP (free) at <strong>1-800-432-4040</strong>.</div>";
      res.classList.add("show");
    });
  }

  // Late-enrollment penalty calculator
  var penBtn = document.getElementById("penBtn");
  if (penBtn) {
    var PARTB = 202.90, NBBP = 38.99; // 2026 figures
    penBtn.addEventListener("click", function () {
      var part = document.getElementById("penPart").value;
      var m = parseInt(document.getElementById("penMonths").value, 10);
      var res = document.getElementById("penResult");
      if (isNaN(m) || m < 0) {
        res.innerHTML = "<strong>Enter how many months you went without coverage.</strong>";
        res.classList.add("show"); return;
      }
      if (part === "B") {
        var yrs = Math.floor(m / 12), pct = yrs * 10;
        if (pct === 0) {
          res.innerHTML = "<div>A " + m + "-month gap is less than one full year, so <strong>no Part B penalty</strong> applies yet. The penalty adds 10% for each full 12 months you could have had Part B but didn't.</div>";
        } else {
          var extra = pct / 100 * PARTB, total = PARTB + extra;
          res.innerHTML = "<div>A " + m + "-month gap = <strong>" + yrs + " full year" + (yrs > 1 ? "s" : "") + "</strong> late.</div>" +
            "<div class='win'>+" + pct + "% \u2192 about $" + extra.toFixed(2) + "/mo extra</div>" +
            "<div>Roughly <strong>$" + total.toFixed(2) + "/month</strong> total for Part B ($202.90 standard + penalty), for as long as you have Part B. Based on the 2026 premium. A Special Enrollment Period can avoid this.</div>";
        }
      } else {
        if (m === 0) {
          res.innerHTML = "<div>With no gap, there's <strong>no Part D penalty</strong>. It's 1% of the national base premium ($38.99 in 2026) for each month without creditable drug coverage.</div>";
        } else {
          var extra2 = Math.round(m * 0.01 * NBBP / 0.1) * 0.1;
          res.innerHTML = "<div>A " + m + "-month gap = <strong>" + m + "%</strong> penalty.</div>" +
            "<div class='win'>about $" + extra2.toFixed(2) + "/mo extra</div>" +
            "<div>Added to your Part D plan premium for as long as you have drug coverage (1% \u00d7 $38.99 \u00d7 " + m + " months, 2026). It can change yearly with the base premium.</div>";
        }
      }
      res.classList.add("show");
    });
  }
})();

/* Contact form -> Web3Forms (email) + Supabase (CRM leads). Progressive enhancement. */
(function () {
  var form = document.getElementById("contactForm");
  if (!form) return;
  var status = document.getElementById("cf-status");
  var btn = document.getElementById("cf-submit");
  function show(msg, ok) {
    status.textContent = msg;
    status.className = "cform-status show " + (ok ? "ok" : "err");
  }
  function toSupabase(data) {
    var url = form.getAttribute("data-sb-url");
    var key = form.getAttribute("data-sb-key");
    if (!url || !key) return Promise.resolve();
    var row = {
      full_name: data.name, phone: data.phone, email: data.email,
      zip_code: data.zip_code, preferred_office: data.preferred_office || null,
      best_time: data.best_time || null, message: data.message || null,
      permission_to_contact: true, consent_text: data.consent_text || null,
      page_url: window.location.href, user_agent: navigator.userAgent
    };
    return fetch(url + "/rest/v1/website_leads", {
      method: "POST",
      headers: { "Content-Type": "application/json", "apikey": key,
                 "Authorization": "Bearer " + key, "Prefer": "return=minimal" },
      body: JSON.stringify(row)
    }).catch(function () { /* non-blocking: email still delivers the lead */ });
  }
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var consent = document.getElementById("cf-consent");
    if (consent && !consent.checked) { show("Please check the permission-to-contact box so we can reply.", false); return; }
    if (!form.checkValidity()) { show("Please complete the required fields (name, phone, email, ZIP).", false); return; }
    var data = Object.fromEntries(new FormData(form).entries());
    data.botcheck = data.botcheck ? true : false;
    if (data.botcheck) return; // honeypot tripped
    if (btn) { btn.disabled = true; btn.style.opacity = ".7"; }
    show("Sending\u2026", true);
    toSupabase(data); // fire to CRM (non-blocking)
    fetch("https://api.web3forms.com/submit", {
      method: "POST",
      headers: { "Content-Type": "application/json", "Accept": "application/json" },
      body: JSON.stringify(data)
    }).then(function (r) { return r.json(); }).then(function (j) {
      if (j.success) {
        form.reset();
        show("Thank you! Your request was sent and ECOS Medicare Solutions will be in touch soon.", true);
      } else {
        show("Sorry, something went wrong. Please call 1-800-432-4040 or try again.", false);
      }
    }).catch(function () {
      show("Network error. Please call 1-800-432-4040 or try again.", false);
    }).finally(function () {
      if (btn) { btn.disabled = false; btn.style.opacity = "1"; }
    });
  });
})();

/* Homepage penalty calculators (Part B: #pbCalc, Part D: #pdCalc). Guarded. */
(function () {
  var PARTB = 202.90, NBBP = 38.99; // 2026 figures
  var pb = document.getElementById("pbCalc");
  if (pb) {
    pb.addEventListener("click", function () {
      var m = parseInt(document.getElementById("pbMonths").value, 10);
      var out = document.getElementById("pbOut");
      if (isNaN(m) || m < 0) { out.textContent = "Enter how many months you went without Part B."; return; }
      var yrs = Math.floor(m / 12), pct = yrs * 10;
      if (pct === 0) {
        out.textContent = "A " + m + "-month gap is less than one full year, so no Part B penalty applies yet. The penalty adds 10% for each full 12 months.";
      } else {
        var extra = pct / 100 * PARTB;
        out.textContent = "+" + pct + "% ≈ $" + extra.toFixed(2) + "/mo extra — about $" + (PARTB + extra).toFixed(2) + "/month total for Part B, for as long as you have it (2026 figures).";
      }
    });
  }
  var pd = document.getElementById("pdCalc");
  if (pd) {
    pd.addEventListener("click", function () {
      var m = parseInt(document.getElementById("pdMonths").value, 10);
      var out = document.getElementById("pdOut");
      if (isNaN(m) || m < 0) { out.textContent = "Enter how many months you went without creditable drug coverage."; return; }
      if (m === 0) {
        out.textContent = "With no gap, there's no Part D penalty.";
      } else {
        var extra = Math.round(m * 0.01 * NBBP / 0.1) * 0.1;
        out.textContent = "A " + m + "-month gap ≈ $" + extra.toFixed(2) + "/mo added to your Part D premium for as long as you have drug coverage (1% × $38.99 × " + m + ", 2026).";
      }
    });
  }
})();
