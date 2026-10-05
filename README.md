# rmbergonia.com

Source for [rmbergonia.com](https://rmbergonia.com/) — the portfolio of **Ruther Bergonia**, a software systems architect and senior full-stack engineer in Metro Manila, Philippines. Laravel, Vue, React, Next.js, MySQL, Docker, and AI integration (Claude, OpenAI, RAG) for universities, institutional offices, and local businesses.

- [About](https://rmbergonia.com/about-ruther-bergonia/) · [Case studies](https://rmbergonia.com/work/) · [Services](https://rmbergonia.com/services/) · [Contact](https://rmbergonia.com/contact/)
- Selected work: [SURI](https://rmbergonia.com/work/suri-research-information-system/) (research information system, UP Manila, 15,000+ records), [GO-ARAL](https://rmbergonia.com/work/go-aral-graduate-support-platform/) (graduate admissions & ticketing), [ARIA](https://rmbergonia.com/work/aria-controlled-response-ai/) (controlled-response AI assistant), [RACE](https://rmbergonia.com/work/race-platform-orchestration/) (platform orchestration layer)
- [Sprntr](https://rmbergonia.com/services/) ([sprntr.dev](https://sprntr.dev/)): done-for-you website, CRM and booking for local businesses, from ₱15,000
- Machine-readable summary: [llms.txt](https://rmbergonia.com/llms.txt)

## Stack

Static HTML on GitHub Pages behind Cloudflare. Tailwind v3 compiled to `assets/tailwind.css`; no other build step.

```sh
# after editing any HTML
npx tailwindcss@3 -c tailwind.config.js -i tailwind.source.css -o assets/tailwind.css --minify

# re-render the Open Graph cards in images/og-*.png
tools/og/build.sh
```

`sitemap.xml` and `llms.txt` are maintained by hand — add new pages to both.

---

<a href="https://app.daily.dev/rockyruther"><img src="https://api.daily.dev/devcards/a67212517e854dd586a21195dcb136a1.png?r=sgd" width="400" alt="Ruther Bergonia's Dev Card"/></a>
