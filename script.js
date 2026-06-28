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
  }
});
