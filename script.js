document.addEventListener("DOMContentLoaded", () => {
  // Intersection Observer for scroll-reveal animations
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("visible");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1, rootMargin: "0px 0px -40px 0px" },
  );

  document.querySelectorAll(".fade-up").forEach((el) => observer.observe(el));

  // Show the scroll-to-top button only after scrolling down past the hero
  const scrollTop = document.getElementById("scrollTop");
  if (scrollTop) {
    const hiddenClasses = ["opacity-0", "translate-y-3", "pointer-events-none"];
    const toggle = () => {
      if (window.scrollY > 600) {
        scrollTop.classList.remove(...hiddenClasses);
      } else {
        scrollTop.classList.add(...hiddenClasses);
      }
    };
    window.addEventListener("scroll", toggle, { passive: true });
    toggle();

    scrollTop.addEventListener("click", () => {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  // Side quick-nav: one dot per numbered section (+01, +02, …), built from
  // whatever sections the page actually has so the markup never drifts out
  // of sync with the nav.
  const sectionNav = document.getElementById("sectionNav");
  if (sectionNav) {
    const sections = Array.from(document.querySelectorAll("main [aria-labelledby], footer[id]"))
      .map((el) => {
        const numberEl = el.querySelector(".label.text-ink-900");
        const labelEl = el.matches("footer") ? el.querySelector(".label.text-ink-500") : document.getElementById(el.getAttribute("aria-labelledby"));
        if (!numberEl || !labelEl) return null;
        // Jump links target the heading id directly rather than minting a
        // new id on the section — sections here are sometimes wrapper
        // elements whose own id (if any) already means something else.
        const targetId = el.matches("footer") ? el.id : el.getAttribute("aria-labelledby");
        return { el, targetId, number: numberEl.textContent.trim(), label: labelEl.textContent.trim() };
      })
      .filter(Boolean);

    if (sections.length > 1) {
      sectionNav.innerHTML = sections
        .map(
          (s) =>
            `<a href="#${s.targetId}" data-section="${s.targetId}" class="group flex items-center gap-3 py-1.5" aria-label="${s.label}">
              <span class="side-nav-line h-px w-6 shrink-0 bg-ink-300 transition-all"></span>
              <span class="side-nav-label max-w-[14ch] break-words text-[11px] font-semibold uppercase tracking-[0.14em] text-ink-300 opacity-0 transition-opacity">${s.number} ${s.label}</span>
            </a>`,
        )
        .join("");

      const links = Array.from(sectionNav.querySelectorAll("[data-section]"));
      const setActive = (id) => {
        links.forEach((link) => {
          const active = link.dataset.section === id;
          link.classList.toggle("is-active", active);
        });
      };

      const sectionObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) setActive(entry.target.dataset.navTarget);
          });
        },
        { rootMargin: "-45% 0px -45% 0px", threshold: 0 },
      );
      sections.forEach((s) => {
        s.el.dataset.navTarget = s.targetId;
        sectionObserver.observe(s.el);
      });
      setActive(sections[0].targetId);
    }
  }
});
