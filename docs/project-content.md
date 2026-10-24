# Project content

The source for every project page. The page data (`PAGE` in `index.html`) is filled from here.
How we fill it: Claude asks Juan what's missing, one project at a time, then writes the text. Never invent clients, metrics or dates; anything unknown stays `[placeholder]`.

## The buckets (the same for every project)
- **Facts:** Year · (Industry) · (Capabilities) · (My role) · a link pill if it's live
- **Overview:** a one-line headline, then a short paragraph: what it is and for whom
- **(The goal):** why it exists, the problem or need. For Lab experiments, this is the "why"
- **(Approach):** what I did and how. For Lab experiments, this is "how I built it"
- **(Outcome):** what happened: results, reactions, what I learned. Real facts only
- **Media:** main video (or cover image), gallery images; (Links) last if there are extra links

Status key: ✅ written · 🟡 old site copy, word for word · ⬜ missing

---

## Lab

### Learn 2 Fly
- **Facts:** 2026 · Education, Games · Claude Code, Vibe Coding, 3D Game Design · Solo, from design to launch · learn2flygame.vercel.app
- **Known (from the site and the repo, wongui/LEARN2FLY):** a game for kids: fly through 3 worlds (Biology, Space, Art), collect stars and answer questions to level up. Spanish and English. One HTML file with Three.js, no build step; installs to the home screen (PWA). The repo can connect a Google Sheet that adds up stars across devices, but the live site doesn't use it yet. Repo created July 2026.
- Overview ✅ · The goal ✅ · Approach ✅ · Outcome ✅
- Media: cover = share image. Gallery: a kid playing it on a tablet (supplied by Juan). Gameplay video ⬜, more screenshots ⬜
- Note: the shared Google Sheet isn't connected on the live site (SHEET_URL is empty), so stars stay on each device. Don't mention it until it is.

**Headline:** Learning that feels like play

**Overview:** A 3D flying game for kids, and a personal project. Players fly through three worlds, Biology, Space and Art, collecting stars and answering questions to level up, in Spanish or English. It plays in the browser and installs to a phone's home screen.

**(The goal):** I made Learn 2 Fly for my nephews, and for kids in general, as a way to learn while playing. I'm interested in how games can add a layer of fun to everyday learning: the best way to get a young kid's attention is a game. So as they play, they're rewarded not only with stars but with knowledge, and learning stops feeling like a task. It was also an experiment, to understand what Claude Code can do with 3D and gamified experiences.

**(Approach):** I started from sketches and my own experience with games, then designed and built the whole thing with Claude Code in about a week and a half: the characters, the environments, the reward system and the questions. The hardest part was the flying. Getting it to feel right, turning my characters into good 3D versions, and tuning the difficulty, pacing, obstacles and stars so kids could understand the game and how to play it.

**(Outcome):** Learn 2 Fly was my first time mixing 3D, games and learning, and doing it all on my own was a real challenge. My nephews were really happy with it: they’ve been playing a lot, and so have their friends. It taught me how hard it is to teach through play. Kids already play very complex games, so a game for them has to be easy to pick up and still exciting, and the learning has to live inside the levels and the play, not on top of them. I keep refining it by watching kids play: testing, iterating and relaunching.

### Config 2026
- **Facts:** 2026 · Design · Claude Code, Vibe Coding, Web Design · Solo, from design to launch · config-2026-frog.vercel.app · (Links) LinkedIn post
- **Known:** a 19-screen scrolling recap for the frog team: Figma's big idea and six launches (Motion, Generative plugins, Weave tools, Figma agent, Shader fills, Code on the canvas), each with "In practice". Repo created July 2026. Source for the text: Juan, plus his LinkedIn post about it.
- Overview ✅ · The goal ✅ · Approach ✅ · Outcome ✅
- Media: cover = share image. Screen recording ⬜, screenshots for the gallery ⬜

**Headline:** A conference recap, built as a website

**Overview:** A 10-minute tour of what Figma shipped at Config 2026, and why it matters for how we design. I made it for my teammates at frog as my first fully vibe-coded website: a slide presentation, reimagined as an interactive site you scroll through.

**(The goal):** I wanted to share the highlights of Config with my frog teammates, and I gave myself a challenge: do it as my first fully vibe-coded website instead of a deck. Still a presentation, but more interactive, modern and interesting to go through.

**(Approach):** I built it in a weekend, my first time using Claude Code. Figma and Config have a very established brand, so I started by bringing assets in from Figma and building a set of starting slides, so Claude could understand the brand and the kind of presentation I had in mind. I still created a lot of the assets myself, or brought them over from Figma, to make it feel real and dynamic. There was a lot of iteration: the skill wasn’t getting something done, but recognizing when an idea was finally pointing in the right direction. I tried several tools before landing on Claude, Figma and Vercel; Figma Make and Figma Agent weren’t quite there for me yet.

**(Outcome):** My teammates were impressed by the format, and a vibe-coded site has become the standard way many of them share things now; some have reused it to build their own shareouts. For me, it confirmed that AI doesn’t replace design thinking, it rewards it. The tools move fast but have no taste, so the job is showing them what good design looks like from the first prompt, and treating every decision like a brief.

## Work

### Atelier West
- **Facts:** 2026 · Physical AI, Robotics, Venture & Startup Innovation · Brand Strategy & Visual Identity, Art Direction, UX/UI Design, Web Design, Prototyping, AI-Assisted Development / Vibe Coding, Front-End Implementation, Responsive Design, SEO · Senior Visual Designer · atelierwest.ai
- **Known:** Next.js site, repo wongui/atelier-west (Sep 4 to Oct 20, 2026, 99 commits; a second contributor, lonniedesign). Partners on the posters: frog, Capgemini, Applied Innovation Exchange, Synapse, NVIDIA, HSBC, AWS Startups. Application windows on the posters: 9/21/26 to 10/11/26 and 10/5/26 to 10/21/26.
- Overview ✅ · The goal ✅ · Approach ✅ · Outcome 🟡 (launch only; results ⬜)
- Media: cover supplied by Juan. Gallery ✅ (brand board, two posters, in assets/source/work/atelierwest). Brand video ⬜ (Juan made one with AI: it should be the main media). The "Second Nature" moodboard is reference only, never on the site.
- ⬜ The two posters give different cohort dates (October 2026 vs November 2026 to January 2027). Which is right, if it goes in the copy?

**Headline:** A brand that makes Physical AI feel natural

**Overview:** Atelier West is a 12-week, equity-free residency for Physical AI startups at Capgemini’s Mission Rock labs in San Francisco. It brings founders into a hands-on environment, with prototyping facilities, engineering and design expertise from frog, Synapse and Capgemini, and access to enterprise partners, to help move Physical AI concepts toward real-world deployment.

**(The goal):** Atelier West started as an emerging program concept that needed a public face. The site had to make it a credible, compelling destination for Physical AI founders: what the residency is, who it’s for, the resources and expertise behind it, and above all, a reason to apply. The launch was tied directly to recruiting startups, while positioning Atelier West within San Francisco’s Physical AI ecosystem.

**(Approach):** I took it from brand to launch, so I could hold the direction all the way through: visual identity, art direction, assets, UX/UI, the website and its build. I explored directions around human creativity, engineering, robotics and AI, such as Neo-Renaissance, North Light, Alchemy, and organic and mechanical systems. The selected one became the brand’s core image: robotic animals with soft, organic exteriors. Physical AI is complex, high technology, but in the end it has to feel natural, pleasant and easy to interact with. I created these visuals with the help of AI and turned them into video, then designed the site in Figma over several iterations and built it with Claude Code, from a working site on GitHub through mobile behavior and production refinements. I also handled the technical launch and discoverability: SEO titles and descriptions, sitemap and robots, AI-readable content, Google Search Console, and analytics and privacy requirements.

**(Outcome):** The site launched with the call for applications to the inaugural cohort, alongside posters and social assets built from the same visuals. [Results: applications received, the cohort, reactions from the team or partners]

### Embroker
- **Facts:** 2024 (June to August) · Insurtech, Commercial Insurance · UX/UI Design, Visual Design, Art Direction, Prototyping, Design Systems, Web Design · Senior Visual Designer · frog client project · embroker.com
- **Source:** Juan, and his frog case-study deck ("A Best-in-Class Insurance Buying Experience for Small Businesses"). Slides with text or confidential footers stay off the site; only clean visuals and the image halves of two slides are used.
- Overview ✅ · The goal ✅ · Approach ✅ · Outcome ✅
- Media: cover supplied by Juan. Gallery ✅ (6, in assets/source/work/embroker). Video ⬜

**Headline:** A best-in-class insurance buying experience for small businesses

**Overview:** Embroker is a digital insurance company simplifying commercial insurance for businesses. frog partnered with Embroker to reimagine its website and evolve its visual language: a clearer, more intuitive journey that communicates its offering, sets it apart from traditional insurers, and increases conversion.

**(The goal):** Embroker is a startup in a highly competitive market, where most insurers offer the same digital flows, quick quotes and tailored coverage, and where customers often see business insurance as a necessary evil that distracts them from running their business. Its website was holding back customer acquisition and conversion. The goal was a simpler, more trustworthy, conversion-focused experience that helps businesses understand their options and find the right coverage without being overwhelmed, and a more distinctive digital presence, with a visual foundation that could support the brand beyond the website.

**(Approach):** As Senior Visual Designer, I worked across both the UX and the visual expression. Our immersion research showed where Embroker could stand apart from its competitors, and we explored the user experience and the visual direction at the same time, mapping guided and unguided buying paths for the home page in weekly working sessions with Embroker’s design, product and marketing teams. I then translated the selected direction across the homepage, navigation, industry and coverage pages, search, content templates and core UI components, and helped establish a refreshed visual system: typography, color, imagery, iconography, elevation and reusable components, built within their existing design system so development stayed seamless.

**(Outcome):** Within six weeks of frog delivering the key screens and the design system, Embroker’s development team launched the new site, and it closely reflected our UX, conversion flows, brand and design system work. The client was especially happy with my approach to the brand, the visual design and the assets for the site, and the new look and feel reached both the website and the brand within months, which is rare. I’m very happy with how they received it.

### AIDO
- **Facts:** 2024 · Design · Web Design · Visual Designer, UX/UI · aido.studio
- Overview 🟡 · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅, gallery ✅ (4)

### Jiviniti
- **Facts:** 2024 · Nonprofit, Research · Web Design · Visual Designer, UX/UI · jiviniti.org
- Overview 🟡 · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅, gallery ✅ (3)

### Around
- **Facts:** 2019 — 2023 (Full Work page says 2020—2023 ⬜ which one?) · Office rental · Web Design, Web App Design · UX/UI Design Consultant, Freelance visual Designer · around.to
- Overview 🟡 · The goal 🟡 · Approach 🟡 · Outcome 🟡
- Media: video ✅, gallery ✅ (12)

### Chief Challenges
- **Facts:** 2021 · Design · Web Design, DLS · Visual Designer, UX/UI · frog.co/insights/chief-challenges
- Overview 🟡 · The goal 🟡 · Approach 🟡 · Outcome 🟡 · (Links) six episodes (03 and 04 share a URL ⬜)
- Media: video ✅, gallery ✅ (6)

### Coltrane
- **Facts:** 2021 · NDA. Shows the old site's line: "Please contact me to see NDA protected projects…"
- ⬜ Public page or not? If yes: facts, text, which images are safe to show, can "Coppel" appear

## Art

### Hule
- **Facts:** [Year] ⬜ · Galería · Branding, 3D Art, Animation · [My role] ⬜ · Instagram @hulegaleria
- Overview 🟡 (Spanish) · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅ (a second one exists), gallery ✅ (6)

### Luum
- **Facts:** 2023 · Tiles · 3D animation · [My role] ⬜
- Overview 🟡 · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅, gallery ✅ (4)

### Nocturna
- **Facts:** 2023 · Music · 3D Animation · [My role] ⬜
- Overview 🟡 · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅, gallery ✅ (3)

### Sūraja
- **Facts:** 2022 · Music · 3D Art, Cover Art · [My role] ⬜
- Overview 🟡 (two paragraphs) · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: cover = the deep affection EP cover (700 px; bigger export ⬜), gallery ✅ (3)

### Surreal Elfs
- **Facts:** 2022 · Conceptual · 3D Animation · [My role] ⬜
- Overview 🟡 · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅ (two more exist), gallery ✅ (8)

### Rhythmic Music Conservatory
- **Facts:** 2020—2022 · Music · 3D Animation, Poster Design · [My role] ⬜
- Overview 🟡 (two paragraphs) · The goal ⬜ · Approach ⬜ · Outcome ⬜
- Media: video ✅, gallery ✅ (3)

### Genesis (old site: Génesis ⬜ which spelling?)
- **Facts:** [Year] ⬜ · Series: Obra I · [Capabilities / medium] ⬜ · [My role] ⬜
- Overview 🟡 (poem, Spanish). A poem may not need goal / approach / outcome ⬜ decide
- Media: cover, gallery ✅ (3)

### Trascender
- **Facts:** [Year] ⬜ · Series: Obra VIII · [Capabilities / medium] ⬜ · [My role] ⬜
- Overview 🟡 (poem, Spanish). Same question as Genesis ⬜
- Media: video ✅, gallery ✅ (3)

---

## Copy notes
- Typos kept from the old site until rewritten: "brand form Mexico City", "lead by", "they where", "team cloud", "Going beyong sustaintability".
