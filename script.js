document.addEventListener('DOMContentLoaded', () => {
    // Select all elements with the 'fade-in' class
    const observerElements = document.querySelectorAll('.fade-in');

    // Create an Intersection Observer
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Add the 'visible' class when the element comes into view
                entry.target.classList.add('visible');
                // Optional: Unobserve the element if you only want it to fade in once
                // observer.unobserve(entry.target); 
            }
        });
    }, {
        threshold: 0.1, // Trigger when 10% of the element is visible
        rootMargin: "0px 0px -50px 0px"
    });

    // Attach observer to each element
    observerElements.forEach(el => {
        observer.observe(el);
    });
});
