# Step 2: Grey-box animatic (stage gate)

Goal: feel the whole camera path and timing before any polish. Grey cards, plain spheres, placeholder text. Juan reviews it before Step 3.

File: `prototypes/v3-scroll-story-greybox.html` (a new file, so the current landing `v2-sun-moon-field.html` stays untouched and no backup copy is needed).

- [x] New scroll timeline: field, About, Lab, Work, Art, footer, measured in screens of scrolling
- [x] Camera path: field, then About close-up, then around to a spot beside the sculpture facing the hills, then a continuous turn to the right through Lab and Work, then a slow stop for Art
- [x] About text rises out of the open skull on a tilted plane, as real HTML text
- [x] Cards drop in as the camera turns toward them and rise back up if you scroll back
- [x] Bubbles fall with real gravity (recorded once at load, so the pile is the same every visit and rewinds when you scroll back)
- [x] Art holds the camera while the drop plays
- [x] Footer panel slides up, the 3D stops drawing once it covers the screen
- [x] Debug overlay showing the scroll position and chapter (`?debug`)
- [x] Nav buttons and `#about`, `#lab`, `#work`, `#art`, `#footer` jump to chapters
- [ ] Juan’s review: pacing, turn direction, how far the camera is from the sculpture, how many cards are visible at once
