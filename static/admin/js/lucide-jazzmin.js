(function () {
  // ---------- Carrega Lucide (ícones) ----------
  function loadLucide(cb) {
    var s = document.createElement("script");
    s.src = "https://unpkg.com/lucide@latest/dist/umd/lucide.min.js";
    s.async = true;
    s.onload = cb;
    document.head.appendChild(s);
  }

  // Mapeia texto do menu -> ícone Lucide
  var ICONS = {
    // apps
    "auth": "shield-check",
    "user": "user-round",
    "weather": "cloud-sun",
    // models
    "Users": "users",
    "Groups": "users",
    "Stations": "leaf",
    "Readings": "activity",
  };

  function applyIcons() {
    var nav = document.getElementById("jazzy-sidebar-menu");
    if (!nav) return;

    nav.querySelectorAll("a.nav-link").forEach(function (a) {
      var fa = a.querySelector("i.nav-icon");
      if (fa) fa.remove();

      var text = (a.textContent || "").trim();
      var appHeader = a.closest("ul") && a.closest("ul").previousElementSibling
        ? a.closest("ul").previousElementSibling.textContent.trim().toLowerCase()
        : null;

      var icon = ICONS[text] || (appHeader ? ICONS[appHeader] : null);
      if (!icon) return;

      if (!a.querySelector("[data-lucide]")) {
        var span = document.createElement("span");
        span.setAttribute("data-lucide", icon);
        a.prepend(span);
      }
    });

    if (window.lucide && window.lucide.createIcons) {
      window.lucide.createIcons();
    }
  }

  // ---------- Vagalumes na tela de login ----------
  function spawnFireflies() {
    var isLogin =
      document.body.classList.contains("login-page") ||
      document.body.className.includes("login");

    if (!isLogin) return;

    var n = 18; // quantidade de "vagalumes"
    for (var i = 0; i < n; i++) {
      var f = document.createElement("div");
      f.className = "firefly";
      // posições/tempos aleatórios via CSS variables
      var x0 = Math.random() * 100, y0 = Math.random() * 100;
      var x1 = Math.random() * 100, y1 = Math.random() * 100;
      var dur = 10 + Math.random() * 12; // 10s..22s

      f.style.setProperty("--x0", x0 + "vw");
      f.style.setProperty("--y0", y0 + "vh");
      f.style.setProperty("--x1", x1 + "vw");
      f.style.setProperty("--y1", y1 + "vh");
      f.style.setProperty("--dur", dur + "s");

      document.body.appendChild(f);
    }
  }

  // Inicializa tudo
  loadLucide(function () {
    var ready = function () {
      applyIcons();
      spawnFireflies();
    };

    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", ready);
    } else {
      ready();
    }

    // Reaplica ícones ao abrir/fechar menus
    document.addEventListener("click", function (e) {
      if (e.target && (e.target.matches(".nav-link") || e.target.closest(".nav-link"))) {
        setTimeout(applyIcons, 100);
      }
    });
  });
})();
