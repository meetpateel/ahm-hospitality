// AHM Hospitality — shared client behavior
// (vanilla JS, no dependencies, loaded with `defer` on every page)

(function () {
  // ===== Mobile nav: hamburger toggles `.open` on the parent `.nav` =====
  document.querySelectorAll('.nav-toggle').forEach(function (btn) {
    var nav = btn.closest('.nav');
    if (!nav) return;
    btn.addEventListener('click', function () {
      var isOpen = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(isOpen));
    });
  });

  // Close the mobile menu when any link inside it is tapped, so navigating
  // anchors on the same page doesn't leave the drawer hanging.
  document.querySelectorAll('.nav .nav-links a').forEach(function (link) {
    link.addEventListener('click', function () {
      var nav = link.closest('.nav');
      if (nav) nav.classList.remove('open');
    });
  });

  // ===== Scroll reveal (used on .reveal elements, currently only on index) =====
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          e.target.classList.add('in');
          io.unobserve(e.target);
        }
      });
    }, { threshold: 0.12 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  }
})();
