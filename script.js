document.addEventListener("DOMContentLoaded", () => {
  // 1. Intersection Observer for Scroll Animations
  const observerOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("visible");
      }
    });
  }, observerOptions);

  // Grab all elements with the Tailwind custom 'fade-in' class
  document.querySelectorAll(".fade-in").forEach((el) => {
    observer.observe(el);
  });

  // 2. Dynamic Navbar (Optional but recommended)
  // Makes the navbar transparent at the very top, and solid when scrolling down
  const nav = document.getElementById("navbar");
  window.addEventListener("scroll", () => {
    if (window.scrollY > 50) {
      nav.classList.add("bg-white/90", "backdrop-blur-md", "shadow-sm");
      nav.classList.remove("bg-transparent");
    } else {
      nav.classList.remove("bg-white/90", "backdrop-blur-md", "shadow-sm");
      nav.classList.add("bg-transparent");
    }
  });
});
