# Juangarcia(mx) — Portfolio 2027

Personal site for Juan Garcia, Senior Visual Designer (from Mexico, based in San Francisco).
Replaces the Framer site at juangarcia.mx. Lab first, portfolio second.

## Status
- **Landing direction chosen:** the *Sun & Moon field*: a giant glowing sculpture buried to the chest in a grass field,
  rolling grass hills, day (sun, blue sky, dragonflies) ↔ after-sunset (crescent moon, blue-hour sky, fireflies).
- **Current prototype:** `prototypes/v2-sun-moon-field.html` (open in Chrome/Safari, no server needed).
- **Next:** port the prototype into the real site in `site/` (Next.js + React Three Fiber), swap placeholder dragonflies for Juan's model.

## Folder map
| Folder | What's inside |
|---|---|
| `prototypes/` | Single-file WebGL prototypes. `v2-sun-moon-field.html` is current; `v2-alt-purple-night.html` keeps the earlier purple night; v0/v1 are history. |
| `assets/source/` | Original 3D files from Juan (`websitebackground.blend`, `pintura final.glb`). Never edit; export new versions next to them. |
| `assets/data/` | Data extracted from the sources (sculpture mesh, ground-level footprint). Regenerate with `tools/`. |
| `docs/` | Brief, Claude project instructions, decision log, visual references. |
| `tools/` | Scripts used to prepare assets. |
| `site/` | The production site (to be scaffolded). |

## Key files
- `CLAUDE.md`: instructions for Claude when working in this project.
- `docs/decisions.md`: what we decided and why (read before changing the look).
- `docs/brief/`: original brief. **Outdated** on landing concept and "(sf)" naming; see decisions log.

## Still needed from Juan
- Dragonfly model with animated wings (`.glb`, Animation on).
- Firefly model, if a custom one is wanted (currently procedural glow).
- Project shortlist + any 2025–26 work; Framer asset export.
