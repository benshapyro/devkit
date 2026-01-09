# Walk Cycle Prompt Template

Copy-paste ready prompts for generating 8-directional walk cycle sprite sheets.

---

## Midjourney v7 Template

```
/imagine 8-directional walk cycle sprite sheet, [CHARACTER], [FRAME_COUNT] frames per direction:

CHARACTER:
[Description matching your established character]
[Clothing, build, distinguishing features]

ANIMATION SPECIFICATIONS:
Directions: 8 (North, NE, East, SE, South, SW, West, NW)
Frames per direction: [4/6/8]
Total frames: [DIRECTIONS × FRAMES]
Frame size: [WIDTH]×[HEIGHT] pixels
Canvas: [COLUMNS × WIDTH]×[ROWS × HEIGHT] pixels

LAYOUT:
- Rows: One per direction (top = North, clockwise)
  - Row 1: North (walking away)
  - Row 2: Northeast
  - Row 3: East (walking right)
  - Row 4: Southeast
  - Row 5: South (walking toward)
  - Row 6: Southwest
  - Row 7: West (walking left)
  - Row 8: Northwest
- Columns: Walk cycle frames

ANIMATION QUALITY:
- Gait: Natural walking (not running)
- Weight distribution: Visible hip shift left-right
- Arm swing: Opposite-arm coordination
- Leg extension: Full knee bend and extension
- Head: Minimal bob, stable neck

LIGHTING:
- Top-left key light (consistent across all frames)
- Soft shadows suggesting ground plane

COLOR PALETTE:
[Same palette as character reference]

STYLE:
[HD pixel art / polished pixel art]
Transparent background
Pixel-perfect edges
No halos or stray pixels

--ar [COLUMNS:ROWS] --q 2 --s 50 --v 7
```

---

## NBP Template

```
Create 8-directional walk cycle sprite sheet.

ANIMATION SPECIFICATIONS:
- Directions: 8 (N, NE, E, SE, S, SW, W, NW)
- Frames per direction: [4/6/8]
- Frame size: [WIDTH]×[HEIGHT] pixels
- Total output: [COLUMNS] columns × 8 rows

LAYOUT:
- Rows: One per direction
  - Row 1: North (away)
  - Row 2: Northeast
  - Row 3: East (right)
  - Row 4: Southeast
  - Row 5: South (toward)
  - Row 6: Southwest
  - Row 7: West (left)
  - Row 8: Northwest
- Columns: [FRAME_COUNT] frames of walk cycle

CHARACTER:
[Match established character exactly]

ANIMATION QUALITY:
- Framerate: 8 FPS equivalent
- Gait: Natural walking
- Weight shift: Hip movement visible
- Arm swing: Opposes leg motion
- Legs: Full extension and contraction
- Head: Stable with minimal bob

COLOR PALETTE:
[List hex codes matching character]

TECHNICAL:
- Transparent background
- Pixel-perfect edges
- No aliasing artifacts
- Consistent lighting all frames
```

---

## Frame Count Guide

| Frames | Feel | Best For |
|--------|------|----------|
| 4 | Snappy, retro | Small sprites, NES style |
| 6 | Smooth, natural | Standard games |
| 8 | Very smooth | Detailed characters |

---

## Common Configurations

| Character Size | Frame Count | Sheet Size |
|----------------|-------------|------------|
| 16×24 | 4 | 64×192 |
| 32×48 | 6 | 192×384 |
| 64×96 | 6 | 384×768 |
| 128×192 | 6 | 768×1536 |

---

## Animation Quality Checklist

- [ ] Weight shifts left-right (hip movement)
- [ ] Arms swing opposite to legs
- [ ] Legs fully extend and contract
- [ ] Head stable, minimal vertical bob
- [ ] Smooth transitions between frames
- [ ] All directions look natural
- [ ] Silhouette consistent across directions
- [ ] Colors match character reference

---

## Transformation Variant (Using --oref)

After base walk cycle is complete:

```
/imagine --oref [BASE_WALK_URL] --ow 120
Walk cycle with [TRANSFORMATION_TYPE] transformation:

MODIFICATIONS:
- Equipment accent: [description of visual change]
- Ability visual: [glow, particles, etc.]
- Overall: [subtle transformation effect]

CONSISTENT (locked by --oref):
- Exact same animation poses
- Same proportions and silhouette
- Same frame timing

TRANSFORMATION QUALITY:
- Subtle, discoverable on close inspection
- Accents only, no full-body color change
- Animation remains smooth

--oref [URL] --ow 120 --ar [RATIO] --q 2 --v 7
```
