# Project: Juangarcia(mx) — Portfolio 2027

## Who I am
Juan Garcia, Senior Visual Designer at frog, from Mexico, based in San Francisco. Brand **Juangarcia(mx)**, domain **juangarcia.mx**.
10+ years in visual design, UX/UI, branding, 3D and motion across health, music, real estate, retail, finance and consultancy work.
I now build what I design with vibe coding. Talk to me in designer language and explain technical things plainly.

## The concept
A portrait of how I design: **exciting, innovative, future-oriented, but useful and grounded in what people need.**
Visual craft is the loudest signal; 3D is my signature; vibe coding is the method; the user stays at the centre.
Keep my parenthetical voice ("(Lab) (Work) (Art) (About)", "(Move) (Drag)", "(& get a coffee)").

## Site structure
- **Landing:** the Sun & Moon field (see below). Text nav to Lab, Work, Art. About opens as an overlay on the live scene.
- **Lab (primary):** usable interaction experiments, each with a short "why" and "how I built it".
- **Work / Art (secondary):** case studies and Brutalist Daddy 3D work, one click away.

## Landing (decided, prototype: `prototypes/v2-sun-moon-field.html`)
**Current main file: `index.html` (repo root) is the v3 scroll story and the home page. Edit it there; `prototypes/v3-scroll-story-greybox.html` only forwards to it. Keep backups in `prototypes/` as `v3-scroll-story-greybox-alt-*.html`.**
Giant glowing sculpture buried to the chest in a dense grass field with rolling grass hills.
(Sun) = vibrant blue sky, sun, dragonflies. (Moon) = after-sunset blue hour, crescent moon, fireflies.
Read `docs/decisions.md` before changing the look. It records what was tried and rejected.

## Tech
- Prototypes: single-file WebGL2 (no libraries), so they open anywhere.
- Production (`site/`): Next.js (App Router) + TypeScript, React Three Fiber + drei, Tailwind + CSS tokens, MDX content, Vercel.
- Assets: originals in `assets/source/` (never overwrite); derived data in `assets/data/` via `tools/`.

## Quality bar
- 60 fps target on a mid-range laptop; lighter path on phones; poster/fade-in while loading.
- prefers-reduced-motion respected; visible text nav; keyboard access; WCAG 2.2 AA on non-3D UI.
- 301 redirects from old Framer URLs.

## How to work with me
- Recommendation first, reasoning second. Be direct.
- Show a quick visual before big builds; give 2–3 distinct options when exploring.
- Name one thing you wouldn't do, and why.
- Before replacing something I liked, keep a copy (e.g. `prototypes/*-alt-*.html`) so we can go back.
- Ask before changing brand, copy or structure. Never invent clients, metrics or dates; use [placeholder].
- Log every look/feel decision in `docs/decisions.md`.
