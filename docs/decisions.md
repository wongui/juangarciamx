# Decision log

Newest last. Each line: decision, then the reason in brackets.

## Brand & content
- Brand stays **Juangarcia(mx)**, domain **juangarcia.mx**. "From Mexico, based in San Francisco." [Mexico is core to the brand; SF is location, not identity]
- Concept: exciting, future-oriented, but useful and grounded in user needs. Visual craft first, 3D as signature, vibe coding as method. [Juan's positioning]
- Keep the parenthetical voice: "(Lab) (Work) (Art) (About)", "(Move) (Drag)". [Carry-over signature from current site]
- About opens as an overlay on top of the live scene. [Brief requirement]

## Landing scene (prototype v2)
- Scene: giant white glowing sculpture (`pintura final.glb`), ~15 m tall, buried to the chest; starting view is 3/4, face turned to frame-right. [Matches Juan's renders]
- Two modes, toggle (Sun) / (Moon); default follows visitor's local time (night 19:00–06:00). `#day` / `#night` in the URL force a mode.
- Day: vibrant blue sky, soft wispy clouds (the first procedural version; volumetric clouds were rejected as fake-looking), visible sun disc, chrome dragonflies that dart toward the cursor at the depth you point.
- Night: **after-sunset / blue hour** (indigo zenith → dusty rose → amber horizon glow behind the sculpture, cool fill, warm rim light), waning crescent moon (sun disc morphs into it), fireflies that follow the cursor. Purple dusk kept as alternative in `v2-alt-purple-night.html`.
- Camera: very slow, subtle automatic drift; drag to orbit; gentle eased parallax. [Reduce motion]
- Grass: dense interactive field around the sculpture (wind + cursor parting), extra-dense strip near the camera, distant blades blend to turf tone to avoid sparkle.
- Grass meets the sculpture with the original soft cut-off. Precise footprint masks / stencil cut-outs were tried and rejected: they made the sculpture look pasted on.
- Distant hills: **live grass all the way up**. The valley was reshaped so the hills rise 16–44 m from the sculpture and their crest hides everything beyond; a second, world-fixed grass layer covers the hills, thinning with distance while blades widen so on-screen density matches the field. Same wind, colour and lighting as the field. (Replaced the baked panorama, which looked different from up close; kept in `v2-alt-baked-hills.html`.)
- Mode toggle is icon-only (sun / crescent), no "(Sun)" "(Moon)" words; labels kept for screen readers via aria-label. [Icons are enough]
- Third mode **Ocean** (wave icon): the field becomes open ocean at sunrise. Low warm sun on the horizon with a glitter path toward the camera, peach/rose/violet sky, glowing reflection of the sculpture, foam at its waterline, cursor ripples, golden water droplets instead of dragonflies. Land ↔ ocean switches with a short fade; `#ocean` forces it. Pre-ocean version kept in `v2-alt-before-ocean.html`.
- Ocean refinements: the sculpture glows brighter at sunrise (stronger emission, lower bloom threshold). Particles are **floating water beads**: ~40 small wobbling spheres (4–13 cm), highly reflective (sky, sun glints, the sculpture's glow) with a clear, slightly refracted core. They drift slowly like the fireflies and all of them ease toward the cursor (spread in loose layers so they don't clump). Earlier versions kept: tiny glow droplets `v2-alt-ocean-droplets.html`, big blobs `v2-alt-ocean-big-blobs.html` (too big, moved too much).
- Dragonflies, fireflies and water beads follow the cursor everywhere: over ground/sea they go to the point you hover; over the sky they rise to a point ~16 m along your line of sight. Grass parting and water ripples only react when the cursor is over the ground or sea.
- Sculpture glow is identical in every mode (emission and bloom set relative to each mode's exposure). Hover: it glows brighter and lights its surroundings more, cursor becomes a pointer. Click (not drag): a bright pulse, then the About overlay opens.
- Same camera framing on every screen size (the mobile framing: 15 m out, 1.0 rad view), so resizing no longer zooms in.
- About = **face focus**: clicking the sculpture (or (About)) pulses the glow, then the camera swoops in on a slight arc and orbit to a **true side profile** of the head, face looking toward the text (3/4 version kept in `v2-alt-about-three-quarter.html`). Desktop: head on the left, text on the right. Mobile/portrait: head low, text above it. The interface fades out, the glow softens so the face reads; (Close), Esc or clicking the scene flies back. `#about` opens it directly. Pre-focus version kept in `v2-alt-before-face-focus.html`.
- Grass layers hand off by thinning (blades drop out gradually) instead of shrinking, and the ground uses smooth per-vertex normals. [Removed the ring/stripe lines across the field]
- UI glass is drawn by the renderer itself (not CSS backdrop-filter or a library): the mode toggle, nav and About panel get a frosted blur of the live scene, lens-like refraction and a slight colour fringe at the edges, a specular rim lit from top-left and a soft shadow. Positions are read from the DOM every frame, so CSS animations still drive it. Light glass by day/ocean, dark glass at night. [Works the same in Chrome, Safari and Firefox; CSS-filter libraries only refract in Chromium.] CSS-glass version kept in `v2-alt-css-glass.html`.

## Rejected
- Inflatable playground as *the* concept (kept only as an idea). Real-time soft-body physics. 3D scan of Juan.
- Volumetric clouds; footprint mask clearing ring; stencil "grass never over sculpture".
