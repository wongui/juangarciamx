# Scroll story v2: the sculpture steps aside

Based on Juan’s sketches from 2026-10-20. The first pass kept the camera on the sculpture the whole way down. This version starts on the sculpture, then turns away from it toward the landscape and lets the work take over.

## The sequence

| # | Chapter | Camera | What happens |
|---|---|---|---|
| 0 | Field | As today | Sculpture is the hero. Brand top left, nav, mode toggle. |
| 1 | About | Close-up on the open head, looking slightly up | The heads lift apart and the About text rises out of the skull, moving up as you scroll down, with a gentle Star Wars tilt. |
| 2 | Lab | Stays near the sculpture, turns to face the hills, then keeps turning (yaw only) as you scroll | Glowing rounded cards with project images drop from the sky and hover just above the grass. A big “LAB” title is anchored in the world. |
| 3 | Work | Keeps turning in the same direction | Same card behaviour, “WORK” title, a “(See more)” pill under the group. LAB slides out of frame on the left. |
| 4 | Art | Stops turning. Scroll is held for a beat | Glowing bubbles fall from the top and pile up in the grass with real gravity. Each one holds an art piece. |
| 5 | Footer | No 3D | A white panel that fills the screen with a small margin, text at the top. The 3D stops rendering behind it to save battery. |

## The idea that ties it together

The heads already “surface ideas” on hover. In About, the heads lift and the words come out of the gap. In Lab and Work, the ideas have left the head and landed in the field as cards. In Art, they fall as bubbles. So the story is: one mind, then everything that came out of it. That gives the turn away from the sculpture a reason, and it isn’t only for variety.

## Tech choices

- **Stay in the single-file WebGL2 prototype, no libraries.** Everything here fits in the existing renderer. Bringing in three.js or Rapier now would mean rebuilding the scene twice, once now and again in the Next.js port.
- **Bubble physics: a small custom solver** (spheres against spheres and the ground, about 100 lines). It runs once when the page loads and records the fall, then plays it back. Every visit gets the same nicely composed pile, the pile can rewind when you scroll back up, and nothing is simulated during scrolling.
- **Cards: a new shader.** A rounded-rectangle panel with the project image inside, the sculpture’s glow on the edges, a fresnel rim, and the glow fading toward the centre so the image stays readable. The cards light the grass under them, the same way the sculpture does.
- **About text: real HTML, not WebGL text.** A CSS 3D perspective layer, positioned every frame from the head’s on-screen position and masked so the words look like they come out of the skull. It stays selectable, translatable and readable by screen readers.
- **Section titles (LAB / WORK / ART):** HTML type pinned to a point in the 3D world, so they move with the camera turn.
- **Images:** files next to the page (`assets/projects/*.webp`, about 1600 px wide), loaded just before their chapter. A new `tools/prep_project_images.py` script makes them from the originals in `assets/source/projects/`.
- **Accessibility:** every card and bubble also exists as a real link in an HTML list, so Tab moves through them and the camera follows focus. With reduced motion, cards fade in where they land, bubbles start already settled, and the crawl is flat text.

## What I wouldn’t do

- **A real Star Wars crawl.** A steep tilt toward a vanishing point is fun for three lines and tiring to read after that. I’d use about 20° of tilt and keep the About text to 4 or 5 short lines.
- **A glass footer.** Glass needs a live scene behind it, and the footer’s job is to let the 3D rest. White, or a solid tone tinted per mode, ends the page cleanly and costs nothing.

## Steps

- [ ] [[Step 1]] Decisions and content from Juan
- [ ] [[Step 2]] Grey-box animatic (stage gate)
- [ ] [[Step 3]] About: text out of the head
- [ ] [[Step 4]] Lab and Work cards
- [ ] [[Step 5]] Art bubbles
- [ ] [[Step 6]] Footer
- [ ] [[Step 7]] Modes, phones, accessibility, performance, ship
