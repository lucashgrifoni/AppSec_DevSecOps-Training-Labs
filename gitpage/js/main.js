/**
 * AppSec & DevSecOps Training Labs — GitHub Pages interactions
 * Vanilla JS: canvas background, parallax, tilt, scroll reveal, mobile nav.
 */
(function () {
  "use strict";

  var prefersReduced =
    typeof window !== "undefined" &&
    window.matchMedia &&
    window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function setYear() {
    var el = document.getElementById("year");
    if (el) el.textContent = String(new Date().getFullYear());
  }

  /* --- Mobile navigation --- */
  function initMobileNav() {
    var toggle = document.querySelector(".nav-toggle");
    var panel = document.getElementById("mobile-nav");
    if (!toggle || !panel) return;

    toggle.addEventListener("click", function () {
      var open = panel.classList.toggle("is-open");
      panel.hidden = !open;
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    panel.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        panel.classList.remove("is-open");
        panel.hidden = true;
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* --- Scroll reveal --- */
  function initReveal() {
    var nodes = document.querySelectorAll("[data-reveal]");
    if (!nodes.length) return;

    if (prefersReduced) {
      nodes.forEach(function (n) {
        n.classList.add("is-visible");
      });
      return;
    }

    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            observer.unobserve(e.target);
          }
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.08 }
    );

    nodes.forEach(function (node, i) {
      node.style.setProperty("--reveal-delay", (i % 6) * 40 + "ms");
      observer.observe(node);
    });
  }

  /* --- Mouse parallax (hero) --- */
  function initParallax() {
    if (prefersReduced) return;

    var root = document.querySelector(".hero");
    if (!root) return;

    var title = root.querySelector(".hero-title");
    var visual = root.querySelector(".hero-visual");
    var layers = [title, visual].filter(Boolean);

    root.addEventListener(
      "pointermove",
      function (e) {
        var rect = root.getBoundingClientRect();
        var x = (e.clientX - rect.left) / rect.width - 0.5;
        var y = (e.clientY - rect.top) / rect.height - 0.5;
        if (title) {
          title.style.transform =
            "translate3d(" + x * 14 + "px," + y * 10 + "px,0) perspective(900px) rotateX(" + y * -4 + "deg) rotateY(" + x * 6 + "deg)";
        }
        if (visual) {
          visual.style.transform =
            "translate3d(" + x * -10 + "px," + y * -8 + "px,0)";
        }
      },
      { passive: true }
    );

    root.addEventListener(
      "pointerleave",
      function () {
        layers.forEach(function (el) {
          el.style.transform = "";
        });
      },
      { passive: true }
    );
  }

  /* --- Tilt on cards --- */
  function initTilt() {
    if (prefersReduced) return;

    document.querySelectorAll("[data-tilt]").forEach(function (card) {
      var capGlow = card.querySelector(".cap-glow");

      card.addEventListener(
        "pointermove",
        function (e) {
          var r = card.getBoundingClientRect();
          var px = (e.clientX - r.left) / r.width;
          var py = (e.clientY - r.top) / r.height;
          var rx = (py - 0.5) * -10;
          var ry = (px - 0.5) * 12;
          card.style.transform =
            "perspective(900px) rotateX(" + rx + "deg) rotateY(" + ry + "deg) translateZ(4px)";
          if (capGlow) {
            capGlow.style.setProperty("--mx", px * 100 + "%");
            capGlow.style.setProperty("--my", py * 100 + "%");
          }
        },
        { passive: true }
      );

      card.addEventListener(
        "pointerleave",
        function () {
          card.style.transform = "";
        },
        { passive: true }
      );
    });
  }

  /* --- Canvas: grid nodes + links --- */
  function initCanvas() {
    var canvas = document.getElementById("bg-canvas");
    if (!canvas || !canvas.getContext) return;

    var ctx = canvas.getContext("2d");
    if (!ctx) return;

    var w = 0;
    var h = 0;
    var dpr = Math.min(window.devicePixelRatio || 1, 2);

    var nodes = [];
    var NODE_COUNT = prefersReduced ? 0 : 72;

    function resize() {
      w = window.innerWidth;
      h = window.innerHeight;
      canvas.width = Math.floor(w * dpr);
      canvas.height = Math.floor(h * dpr);
      canvas.style.width = w + "px";
      canvas.style.height = h + "px";
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

      nodes = [];
      for (var i = 0; i < NODE_COUNT; i++) {
        nodes.push({
          x: Math.random() * w,
          y: Math.random() * h,
          vx: (Math.random() - 0.5) * 0.35,
          vy: (Math.random() - 0.5) * 0.35,
          r: Math.random() * 1.6 + 0.6
        });
      }
    }

    function step() {
      if (NODE_COUNT === 0) {
        ctx.clearRect(0, 0, w, h);
        return;
      }

      ctx.clearRect(0, 0, w, h);

      var i;
      var j;
      var a;
      var b;
      var dist;
      var maxDist = prefersReduced ? 0 : Math.min(120, w * 0.12);

      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        a.x += a.vx;
        a.y += a.vy;
        if (a.x < 0 || a.x > w) a.vx *= -1;
        if (a.y < 0 || a.y > h) a.vy *= -1;
      }

      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        for (j = i + 1; j < nodes.length; j++) {
          b = nodes[j];
          dist = Math.hypot(a.x - b.x, a.y - b.y);
          if (dist < maxDist) {
            var alpha = (1 - dist / maxDist) * 0.22;
            ctx.strokeStyle = "rgba(8, 185, 139," + alpha + ")";
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(a.x, a.y);
            ctx.lineTo(b.x, b.y);
            ctx.stroke();
          }
        }
      }

      for (i = 0; i < nodes.length; i++) {
        a = nodes[i];
        ctx.fillStyle = "rgba(213, 216, 221, 0.45)";
        ctx.beginPath();
        ctx.arc(a.x, a.y, a.r, 0, Math.PI * 2);
        ctx.fill();
      }

      requestAnimationFrame(step);
    }

    resize();
    if (!prefersReduced) {
      requestAnimationFrame(step);
    } else {
      ctx.clearRect(0, 0, w, h);
    }

    window.addEventListener("resize", function () {
      resize();
    });
  }

  function boot() {
    setYear();
    initMobileNav();
    initReveal();
    initParallax();
    initTilt();
    initCanvas();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
