# Ruther Bergonia — site knowledge

This document is the complete content of rmbergonia.com. The assistant answers ONLY from it.

## Identity

- Name: Ruther Bergonia. Pronouns not stated on the site.
- Title: Software Systems Architect & Senior Full-Stack Engineer.
- Location: Metro Manila, Philippines (GMT+8). Works remotely across time zones.
- Experience: 11+ years (career started 2015). Six platforms live.
- Current role: Systems architect at the Research Grants Administration Office (RGAO), University of the Philippines Manila. Official position title there is Senior Administrative Assistant II. Leads architecture and development of SURI, building TRACE, and ARIA.
- Also: independent contractor since 2018; runs Sprntr (websites + CRM for local businesses) and CNTXTQRY (AI practice tool for customer-service conversations).
- Availability: always open for work and new client projects. Remote projects across time zones. Replies within one business day.
- Email: ruther.bergonia@gmail.com (fastest way to reach him).
- LinkedIn: https://www.linkedin.com/in/ruther-bergonia-a9959813a/
- GitHub: https://github.com/rockyru
- daily.dev: https://app.daily.dev/rockyruther
- Resume / CV (PDF): https://rmbergonia.com/assets/ruther-bergonia-resume.pdf
- Site pages: Home https://rmbergonia.com/ · About https://rmbergonia.com/about-ruther-bergonia/ · Work https://rmbergonia.com/work/ · Services https://rmbergonia.com/services/ · Contact https://rmbergonia.com/contact/

## Tagline and positioning

- Homepage motto: "Scope. Build. Integrate. Operate." and "Software, built with method."
- Four practice areas: Product Engineering, Systems Architecture, Integration & AI, Cloud & Deployment.
- "Always available for your software engineering needs. Replies within a day."
- Summary: designs, builds, deploys, and maintains production software for universities, institutional offices, government-related teams, SaaS companies, and operational organizations, replacing fragmented spreadsheets and manual workflows with secure platforms.
- Why it matters (his words): "Because software today is more than a switch you flip on and off. Because bad planning gets expensive. And because reliability in a system isn't negotiable."
- About page headline: "One engineer. End to end. From the first schema to the running server."

## What he builds (homepage "What I build")

As a systems partner he scopes, builds, and stands behind software that has to keep working.
- Software Engineering: Laravel, Vue 3, React, TypeScript, Tailwind CSS.
- Infrastructure & Cloud: Docker, Nginx, MySQL, PostgreSQL, Redis, AWS, DigitalOcean, Cloudflare.
- Integrations & AI: REST APIs, system integrations, OAuth/SSO, AI & LLM integrations, automation.

## What he does (About page)

- Systems architecture: API-first service design, cross-system authentication, database architecture, platforms that share one set of records (e.g. TRACE, the research-team workspace built on SURI's API at UP Manila).
- Full-stack development: Laravel and PHP backends with Vue, React, and Next.js frontends (e.g. SURI).
- AI integration: controlled-response assistants built on approved sources with human handoff. This is the approach behind ARIA and the exam reviewer Alamat. Principle: AI should reduce operational risk, not add it.
- Infrastructure: Docker, Linux, and Nginx administration, VPS deployment, release management, production database architecture.

## Technical capabilities (full lists)

- Backend: PHP, Laravel, FastAPI, REST API design, MySQL, relational database design, authentication & authorization, role-based access control (RBAC), workflow automation, reporting engines.
- Frontend: Vue.js, React, Next.js, TypeScript, Tailwind CSS, progressive web apps, offline-first architectures, responsive and accessible interfaces.
- AI: Claude & OpenAI integration, Gemini, retrieval-augmented generation (RAG), controlled-response architectures, prompt engineering, AI-assisted workflow automation.
- Infrastructure: Docker, Linux server administration, Nginx, VPS & cloud deployment, CI/CD, release management, production database architecture. Also PostgreSQL, Redis, AWS, DigitalOcean, Cloudflare.

## How he builds (approach)

- Systems should grow instead of being rebuilt: API-first services, clean separation between platforms, authentication designed for an ecosystem rather than a single app.
- Continuity built in from the start: documentation, version-controlled code, reproducible infrastructure another engineer could pick up without starting over.
- AI features follow the same discipline: the assistant answers from approved sources and hands off to a human when something falls outside its scope, rather than guessing.
- Engagement style: "Tell me what's breaking." He gives an honest read on whether he is the right fit and how he'd approach it. If a spreadsheet is genuinely fine for now, he'll say that. Replies within one business day.
- Pattern from GO-ARAL/DRMS that defines his institutional work: architect the APIs and schemas first, treat access control as a first-class design concern, own the deployment, stay through training and post-deployment support.

## Career timeline

- 2025 — now: Systems architect, RGAO, UP Manila (position title: Senior Administrative Assistant II). Leads architecture and development of SURI (50+ users, reporting in seconds instead of days). Building TRACE, the research-team workspace on the same API and records. ARIA runs in the same ecosystem.
- 2025 — now: Independent contractor, SaaS architecture. Architecting a multi-tenant SaaS platform for digital advertising catalogs, with clean tenant isolation from the schema up.
- 2021 — 2025: Senior ICT Assistant, NGOHS (National Graduate Office for the Health Sciences), UP Manila. Built and ran DRMS and GO-ARAL: ~1,000 applicants a year, ~200 support requests a month. Owned the APIs, database schema, RBAC, and reporting behind both.
- 2021 — 2022: Full-stack developer, LMQ Tech (freelance, remote, US client). Built an ELK Stack operations dashboard with ticketing and reporting. Also managed servers, databases, and infrastructure.
- 2018 — 2020: Crosshair Technologies Solutions Inc. Built a demographic-targeted advertising platform on AWS.
- 2015 — 2017: Balibago Waterworks System, Inc. Where he started. Worked on their internal Job Order Requests Queueing application (Laravel and Vue), managed servers and database, helped field-test the mobile app for water meter reading and billing. Also built a company site.
- 2018 — present: Freelance / independent contractor for local and international clients: web applications plus managing servers, databases, and infrastructure. Project types: SaaS platform, real property management, logs monitoring, targeted advertisement.

## Selected work (case studies)

### SURI — research information system (UP Manila, RGAO)
- URL: https://rmbergonia.com/work/suri-research-information-system/
- Full name: System for UPM Research Intelligence.
- Role: Lead Engineer / Systems Architect. Client: RGAO, UP Manila. Stack: Laravel, Vue.js, MySQL. Status: in production, 2025.
- What it is: an API-first Laravel + Vue.js platform that unifies research registration, document management, reporting, and approval workflows. Serves 50+ users across multiple offices. Replaced manual spreadsheet compilation with reporting that runs in seconds (previously days).
- Problem: research administration generated registrations, documents, approvals, and reports that ran by hand across spreadsheets and disconnected tools. Manual compilation fragmented the record of research activity, made reporting a recurring project instead of a query, and left approvals without a system of record. Multiple offices, each with its own permissions and its own idea of what a "project" means.
- Modules: research registration (final registration, management, and funding records); document management; approval workflows (tracked and automated end to end); reporting.
- Architecture: API-first on Laravel with Vue.js frontend and MySQL. Authentication and role-based access control treated as architecture, not features, because SURI is designed to join a broader ecosystem (TRACE).
- Operations: he leads architecture and development and owns it through production: deployments, production database architecture, release management. Operated software, not a prototype.
- Outcome: 50+ active users, reporting that took days now runs in seconds.
- Engineering notes (as of 2026, for technical questions):
  - Stack: PHP 8.4, Laravel 12, MySQL 8; Vue 3 + Vite + TypeScript SPA with Pinia, vue-router and Tailwind. Study titles and objectives encrypted at rest (Laravel encrypted casts).
  - Sign-in: Google OAuth via Socialite, then a Sanctum cookie session for the SPA. University accounts admitted by domain, outside accounts by approved invitation; any account with no role or permission is turned away on every request. Mobile: one-time code with PKCE exchanged for ability-scoped bearer tokens expiring after 24 hours.
  - Access control: spatie/laravel-permission; roles super admin, admin, executive, project handler, encoder, researcher, research assistant, unit viewer; 38 named permissions enforced as route middleware. Unit viewers are scoped to one college or institute and the scope fails closed when no unit is set.
  - Domain model: about 170 Eloquent models, 250+ migrations. A research registration carries a temporary reference until approval mints the permanent one; status columns for pending, approved, rejected (with reconsideration); change requests add superseded. Also budget versions and fund tranches, purchase requests and orders, document tracking, contract review, help desk, publications, presentations.
  - Approval is one transaction: lock the row, mint the reference number, stamp registration and certificate dates, write an audit diff, generate the certificate PDF, queue the email after commit.
  - Audit trail: every write goes through a helper recording actor, action, table, record, JSON diff, IP, user agent and URL, and never throws. Validation errors, 404s and unhandled exceptions are stored in an error-log table.
  - Reporting: analytics hub with eight sections cached five minutes per filter set; seven prebuilt reports; model-written custom reports grounded in a query tool; exports to XLSX/CSV (OpenSpout), PDF (dompdf), DOCX (PhpWord); monthly, quarterly and annual scheduled reports; downloads logged.
  - Workflow automations: staff describe a rule in plain English, a model compiles it into a rule graph at authoring time, a person reviews and arms it, deterministic PHP runs it from model observers. Automations can never delete, approve or reject.
  - API: versioned routes under api/v1 (32 route files), FormRequest validation, one error envelope, named rate limiters per feature, shared-secret or HMAC middleware for server-to-server integrations (AWTOR sync, Google Apps Script bridges, help-desk intake).
  - Quality and delivery: Pest with 176 test files and about 1,500 test cases; GitHub Actions CI against MySQL 8, then a self-hosted runner deploys main to production and develop to staging; scheduled jobs drain the queue, back up the database weekly, run health checks every five minutes and enforce retention.

### ARIA — controlled-response AI assistant
- URL: https://rmbergonia.com/work/aria-controlled-response-ai/
- Role: Architect & Developer. Domain: research support. AI: Claude with retrieval-augmented generation (RAG) over keyword-scored retrieval (no vector database), Next.js and Laravel. Focus: controlled-response AI.
- What it is: an AI-assisted support platform that answers research inquiries from approved information sources, routes anything outside its scope to a human rather than guessing, and automatically creates tracked tickets for follow-up.
- Problem: research administration offices field a constant stream of inquiries, most answerable from existing policies, guidelines, and records. Answering by hand consumes staff time; leaving them unanswered erodes trust. A generic chatbot is the wrong fix: when an AI speaks for a university office, a confidently wrong answer is worse than no answer.
- Three rules of the controlled-response architecture: (1) Approved sources only, via RAG, not open-ended model knowledge. (2) Human handoff for anything outside scope. (3) Tracked follow-up: inquiries that need follow-up become tickets, nothing disappears into a chat log.
- The hard part was not the model; it was the refusal behaviour. It says it doesn't know rather than inventing an answer.
- Powered by Claude. Operates in the same ecosystem as SURI; TRACE, the research-team workspace, sits on the same API.
- Engineering notes (as of 2026; there are two ARIA surfaces):
  - Public assistant: on the office's Next.js 16 site, Anthropic SDK, Claude Haiku 4.5, streamed, low temperature, hard output cap; only the last six messages are sent, each trimmed; per-IP rate limit.
  - Retrieval: keyword-scored retrieval over the office's own content (one chunk per FAQ, downloadable file and page; length-normalised term frequency with a title boost; top six; each windowed around the query). No embeddings or vector database, by design: small controlled corpus and encrypted sensitive fields upstream.
  - Grounding: cached facts block plus per-query context block; the model may answer only from those. Reply links are checked against an allowlist built from the facts and retrieved chunks; others are stripped while streaming.
  - Handoff: when it cannot answer or the visitor asks for a person, the reply ends with a marker that opens a ticket form. The ticket is created in SURI's help desk with a year-numbered reference and the transcript attached, and an acknowledgement email with a reply token is sent. If SURI is unreachable it falls back to email with a local reference.
  - Privacy: conversations live only in the visitor's browser session; public and staff AI features sit behind environment flags that default to off.
  - Staff assistant inside SURI: Laravel service on Claude Sonnet 4.6 with seven read-only tools (worklist, documents, SURI records, analytics, bibliometrics, ranking, email drafting) returning totals, breakdowns and samples of at most 15 rows. Each tool maps to a permission; tools the user cannot run are not offered to the model; the tool loop is capped. Session context gives the model who is asking, where they are in the app and the office's current counts.
  - Audit and retention: one audit row per turn stores hashes and lengths of prompt and reply (not text), tokens, latency, tool calls, referenced records and a prompt-injection heuristic flag. Verbatim capture needs the feature on, per-turn consent and an identified user, and is purged after 30 days; rows kept two years. Reading the log is permission-gated and itself audited; retention and purge run as scheduled commands.

### TRACE — collaboration workspace for research teams (in development)
- URL: https://rmbergonia.com/work/race-platform-orchestration/
- Full name: Transformative Research Assistant for Collaboration and Engagement. Grew out of RACE (Research Assistant Coordination Engine), a project-management app for research assistants; renamed TRACE in October 2026 when the scope widened to the whole research team.
- Role: Systems Architect (he builds it alongside SURI). Users: research assistants and principal investigators of UP Manila research projects, with RGAO handlers overseeing. Status: in active development since July 2026, staging test build in use, no production deployment yet.
- What it is: a Vue 3 workspace for research teams that runs on the same Laravel API and the same research records as SURI. The office keeps its system of record in SURI; the team does its work in TRACE.
- Problem: SURI gave the office a system of record, but nothing in the data linked an assistant to a project ("my projects" was guesswork), and tasks, deadlines, deliverables and phase documents lived in chat threads, spreadsheets and inboxes.
- Provides: (1) Personal view: Today, my tasks, my projects, an inbox with read acknowledgements, and Learning (RGAO's orientation courses, TUKLAS, now live inside TRACE). (2) Project workspace: overview, tasks, timeline, deliverables, files, team, activity feed, shared notes with comments, metrics, scoped to project members. (3) Office files: research documents, line-item budget, procurement and monthly payroll submissions, the same records SURI handlers see, edited through the same rules.
- Phase sync: a project in TRACE is a SURI research record; when a project moves to a new phase in SURI, TRACE creates one task per document that phase requires.
- Design decisions: no second database (every TRACE table hangs off SURI's research record; budget lines, procurement stages, disbursements and payroll reuse SURI's own models and services); membership is the authorization primitive (an assignment row links a person to a project, every request checks membership, any member sees the whole team's work; writes blocked on projects the office does not manage); invite-only sign-in (admin or the project's handler issues an email-bound single-use link valid 14 days; Google sign-in returns a Sanctum bearer token scoped to TRACE, which can never act as a SURI role); safe concurrent edits (tasks carry an integer version; a write without one is rejected, a stale one is refused); one task model (tasks, milestones and deliverables are one table with a kind, dates and dependencies).
- Engineering notes: frontend Vue 3.5, Vite, TypeScript strict, Pinia, vue-router, Tailwind 4, no component library, three layers (pure TypeScript domain, stores that run on mock data or the live API, views), refreshes on window focus. Backend: Laravel routes under api/v1/race guarded by Sanctum plus a TRACE-only token ability; workspace tables for tasks, notes, comments, files, events and read state; budget, procurement, disbursement and payroll endpoints reuse SURI's services, the managed-project middleware and the shared audit log. Tests: 15 Vitest files (about 94 cases) and 4 Playwright specs against a mocked API, run on every push and pull request; backend 10 feature test files (about 106 cases). Deployment: a Cloudflare Worker serving the built static assets with single-page fallback, staging only. A mobile companion (Expo, React Native) is scaffolded with PKCE sign-in.
- Not yet built: email notifications, AI features, production deployment. Say so when asked.
- ARIA and TRACE are not integrated with each other; both sit on SURI's API.

### GO-ARAL — graduate application & ticketing portal (NGOHS, UP Manila)
- URL: https://rmbergonia.com/work/go-aral-graduate-support-platform/
- Role: Senior ICT Assistant. Client: NGOHS, UP Manila. Focus: portal / ticketing / RBAC. Period: 2021 — 2025. Stack: Laravel, Vue, MySQL.
- What it is: the application and ticketing portal at the National Graduate Office for the Health Sciences, built alongside DRMS (the admissions records system). Supports roughly 1,000 graduate applicants annually and around 200 support requests monthly.
- Problem: NGOHS coordinates graduate admissions for the health sciences; ~1,000 applicants per recurring cycle generating applications, records, and support questions. Without systems, records lived in ad-hoc files and support arrived through unstructured channels with no way to track what was answered, resolved, or dropped.
- Two systems: GO-ARAL (applicant-facing application and ticketing portal: applicants apply, support requests become tracked tickets instead of lost emails) and DRMS (internal records system, the office's source of truth for applicant records).
- He architected the APIs, database schemas, reporting systems, and role-based access control behind both, led deployment to a VPS, staff training, and post-deployment support.
- Outcome: ~1,000 applicants a year, ~200 tickets a month, admissions records, reporting, and applicant support running through structured, role-controlled software.

### Alamat
- An exam reviewer built with the same controlled-response AI approach as ARIA. Mentioned on the About page; no separate case study.

### Freelance projects (no public case study)
- SaaS platform, real property management, logs monitoring (ELK Stack ops dashboard for LMQ Tech), targeted advertisement (Crosshair). Server, database, and infrastructure management for these clients.

## Products

### Sprntr — websites + CRM + booking for Philippine service businesses
- Pages: https://rmbergonia.com/services/ and https://sprntr.dev/ · Email: hello@sprntr.dev
- Tagline: "Sprntr. Move business faster." His product for service businesses: a website built for you, connected to one workspace for inquiries, follow-up, and bookings. The preview is free.
- Pricing: one-time, no monthly fees. Hosting, SSL, and domain included for 2 years, then ₱3,000 a year. 50% deposit to start, the rest at launch. Pay by GCash, Maya, card, or QR Ph. Build your own package on sprntr.dev.
  - Website: ₱15,000 one-time. Up to 5 pages built for you, SEO setup and Search Console, inquiry form that emails you, hosting/SSL/domain for 2 years.
  - Website + CRM: ₱22,000 one-time. Everything in Website plus pipeline and customer records, online booking and shared calendar, reminders, Google Meet links, review requests.
  - Business System: ₱35,000 one-time. Everything in Website + CRM plus up to 10 pages, a planning call, staff training, competitor monitoring (Market Watch), priority support, and 3 months of the Care plan free.
  - Add-ons: extra pages ₱1,500 each; rush launch in 3 business days ₱3,000; Sprntr Premium ₱15,000 one-time with 11 growth features including lead recovery and AI reply drafts.
  - Sprntr Custom from ₱50,000 for inventory, multiple branches, payments, and similar.
- What it fixes: (1) They can't find you: no proper Google presence. (2) Bookings get lost across Messenger, Instagram, and text. (3) You look smaller than the shop with a real website and clear prices.
- What's included:
  - Website: custom site up to 5 pages, phone-first, SEO setup (titles, descriptions, sitemap, Search Console), hosting/SSL/domain for 2 years, your own domain registered in your business's name or connected, plus a free yourbusiness.sprntr.dev address.
  - Inquiries: every inquiry lands in one pipeline; team emailed the moment it arrives; website inquiries saved as leads; customer records with full history; reply by email from the lead's record; Messenger chats as leads (awaiting Meta approval); if an inquiry waits 30 minutes without a reply the team gets a nudge during opening hours.
  - Booking: customers book open slots based on hours, closed dates, and Philippine holidays; you confirm or decline; shared calendar; Google Meet links; reminder emails the day before; one review request after each visit; a results email on the 1st of every month (last month's leads, bookings, customers). Text reminders work using prepaid SMS credits.
  - Support: set up with you; free preview before paying; walkthrough call then changes then launch; up to 3 staff sign-ins with Google accounts; up to 10 content edits included (prices, photos, hours); you own your customer data and can export any time; a real person replies at hello@sprntr.dev usually within one business day.
- Process: (1) Tell us about your business via the preview form on sprntr.dev (two minutes). (2) Free preview built from your logo, photos, services, and prices, usually in about 5 business days, no cost or commitment. (3) Walkthrough call and your changes; pay the 50% deposit only when you decide to go ahead. (4) Live once you approve, or within 3 business days with rush launch; pay the balance, invite your team.
- Live client sites: Lamour Printing Services (print shop, Sampaloc, Manila; stickers, labels, standees, invitations; Sprntr's first pilot customer) https://lamour.sprntr.dev/ · Pampered Pets Club (pet grooming, hotel and daycare, Batangas City; "Book a visit" flow) https://pamperedpets.sprntr.dev/ · Pinky Lamasan Bridal Atelier (ready-to-wear and customized bridal gowns, General Trias, Cavite; editorial website plus a custom system for gown inventory, reservations, orders, and payments on its own domain) https://pqlamasan.com/
- FAQ:
  - Is the preview really free? Yes. You only pay if you decide to go live.
  - Is there a monthly fee? No. Pay once; hosting and domain included for 2 years, then ₱3,000 a year; up to 10 content edits included.
  - Can I keep my own domain? Yes. Connect one you own or register a new one in your business's name; it's yours and transferable any time; plus a free sprntr.dev address.
  - I already have a Facebook page, why do I need this? Keep it; they do different jobs. The website is what people find on Google, and inquiries land in an organized pipeline.
  - Does it connect to Messenger? Yes, pending Meta's approval for customer Pages. Text reminders already work.
  - Can you do more than this? Yes; inventory, multiple branches, payments, reporting are all doable, scoped and priced separately (Sprntr Custom).

### CNTXTQRY — AI practice tool for customer-service conversations
- URL: https://cntxtqry.com/ · Made in the Philippines.
- Headline: "Rehearse the hard conversations. Before they happen." Tagline: "A little practice. A different conversation."
- What it is: users rehearse chat, email, and voice customer-service interactions with an AI customer (for example "Dana", a customer charged twice for a $59.99 meal-kit subscription) and get scored feedback before a real interview, mock assessment, or client conversation.
- Who it's for: Filipino BPO applicants preparing for mock assessments, virtual assistants (VAs) preparing for client work, and agency teams.
- Features: chat, email, and voice practice scenarios (billing disputes, cancellations, damaged-item complaints); an AI judge scores five skills (empathy, discovery, accuracy, resolution, communication) on a 1 to 5 scale, weighted and converted to a score out of 100; feedback quotes the user's own words; coaching tips and printable reports; VAs can upload a client's SOP (Pro and Job-hunt pass) to generate practice scenarios; coach review in agency workspaces.
- Pricing: Free ₱0, 3 sessions a month, no card needed. Job-hunt pass ₱149 for 7 days, one-time, 10 sessions. Pro ₱499 per month or ₱4,990 per year, 30 sessions a month, up to 5 SOP uploads a month. Payment by QR Ph with receipt upload as an alternative. Plans do not auto-renew.
- Disclaimers: cannot promise job placement; AI scoring is coaching, not an official assessment, and can be wrong.

## Client work: Construction Estimating Academy
- URL: https://estimatingacademy.org/ · Made in the Philippines. A client project (Ruther built the platform).
- Headline: "Practical construction estimating training, online." Tagline: "Self-paced online courses. Live webinars. Verifiable certificates."
- What it is: an online training platform for construction estimating: self-paced courses, live Zoom webinars, a store of estimating templates and guides (takeoff, pricing, bid recap), and corporate training for teams. Includes a marketing site, webinar booking, a template store, and student sign-in.
- Audience: people starting out in estimating, working estimators who want to improve, and companies that want a shared estimating approach.
- Features: project-based lessons using real drawings and quantities; lessons stay open after enrollment; short quizzes; certificates of completion with numbers that can be verified online. Payment by bank transfer or e-wallet.
- Featured event at time of writing: a free beginner webinar on working as a construction VA and using PlanSwift.
- Course prices are not listed on the site; the webinar shown is free.

## Contact

- Email ruther.bergonia@gmail.com. Replies within one business day. Contact page: https://rmbergonia.com/contact/
- What to include in a first email: (1) what you're building or what's currently breaking; (2) rough timeline and, if you have one, a budget range; (3) any existing systems this needs to work with.
- For Sprntr (local business websites): hello@sprntr.dev or the free preview form at https://sprntr.dev/
- He'll tell you what he'd investigate first, and whether he's the right fit.

## This website

- rmbergonia.com is a static site on GitHub Pages behind Cloudflare, source at https://github.com/rockyru/rockyru.github.io. The homepage is a chat-style interface whose assistant is called Ru Bot; it answers as Ruther, only from the site's own content.
