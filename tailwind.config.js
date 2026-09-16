/** @type {import('tailwindcss').Config} */
// Shared Tailwind config for the whole site (previously inlined per-page for the Play CDN).
// Regenerate assets/tailwind.css after editing any HTML:
//   npx tailwindcss@3 -c tailwind.config.js -i tailwind.source.css -o assets/tailwind.css --minify
module.exports = {
  content: ["./*.html", "./about-ruther-bergonia/**/*.html", "./contact/**/*.html", "./services/**/*.html", "./work/**/*.html", "./script.js"],
  theme: {
    extend: {
      colors: {
        // Pure white ground, matching the Flumen reference.
        paper: {
          DEFAULT: "#ffffff",
          raised: "#ffffff",
          sunk: "#f4f2ee",
        },
        ink: {
          900: "#111013",
          700: "#3a3740",
          500: "#57545d",
          300: "#8b8792",
          100: "#e3e0da",
        },
        // Monochrome only. There is no hue in this system: emphasis is carried
        // by weight, scale, and fill, so "accent" resolves to full-strength ink.
        accent: {
          DEFAULT: "#111013",
        },
      },
      fontFamily: {
        // Single-typeface system, matching the Flumen reference: Inter
        // everywhere, weight and tracking carry the register instead of a
        // second display face.
        sans: ["Inter", "Helvetica Neue", "Arial", "sans-serif"],
        body: ["Inter", "sans-serif"],
        label: ["Inter", "Helvetica Neue", "sans-serif"],
        mono: ["Inter", "Helvetica Neue", "sans-serif"],
      },
    },
  },
  plugins: [],
};
