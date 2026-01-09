# Pixel Art Patterns for AI Generation

This reference covers pixel art-specific techniques for AI image generation. These patterns apply to any tool (Midjourney, NBP, DALL-E, Stable Diffusion).

---

## Grid Alignment

AI tools don't naturally respect pixel grids. Force alignment through explicit constraints.

### Grid Templates

Create reference grids before generation sessions:
- 8-pixel cell grids for small assets
- 16-pixel cell grids for standard tiles
- Upload grid overlay to lock spatial consistency

**Prompt pattern:**
```
"Fill each cell with [element], maintaining the grid structure exactly"
```

### Resolution Discipline

**Always specify exact dimensions:**

| Asset Type | Common Sizes | Aspect Ratio |
|------------|--------------|--------------|
| Small tiles | 16×16, 32×32 | 1:1 |
| Large tiles | 64×64, 128×128 | 1:1 |
| Character sprites | 32×48, 64×64, 128×192 | 2:3 or 1:1 |
| Portraits | 64×64, 128×128, 256×256 | 1:1 |
| Small enemies | 32×32, 64×64 | 1:1 |
| Large enemies/bosses | 96×96, 128×128, 192×256 | varies |

**Prompt pattern:**
```
"[SIZE] pixel art [asset], transparent background"
e.g., "128x192 pixel art character sprite, transparent background"
```

---

## Limited Palettes

Color discipline is essential for cohesive game art.

### Define Palette Upfront

Before generating, establish:
- Primary colors (2-3)
- Secondary colors (2-3)
- Accent colors (1-2)
- Shadow/highlight variants

**Provide hex codes explicitly:**
```
COLOR PALETTE (EXACT):
- Primary: #5C4A3D (warm brown)
- Secondary: #E8C170 (amber)
- Accent: #A8B35C (sage green)
- Shadow: #4A4A3D (dark)
- Highlight: #F4E4BC (cream)
```

### Palette Lock Workflow

1. Generate first asset with explicit palette
2. Save as style reference
3. Apply `--sref` with high weight (300-400) for subsequent assets
4. Validate colors match after generation

### Avoiding Palette Drift

**Common causes:**
- Ambient color in prompt ("sunset lighting" adds orange)
- Vague color terms ("blue" is ambiguous)
- Low style weight on references

**Solutions:**
- Use hex codes, not color names
- Increase style reference weight
- Add explicit `--no [unwanted colors]`
- Post-process in image editor if needed

---

## Seamless Tiling

Tilesets must repeat without visible seams.

### Generation Parameters

**Midjourney:** Add `--tile` parameter
**NBP:** Explicitly state "seamlessly tileable, edges must match"

### Validation Workflow

1. Generate tileset
2. Download PNG
3. Test with online tile checker (imgonline.com.ua/eng/check-texture-tiling.php)
4. Create 4×4 preview in image editor
5. Check for:
   - Visible seams at edges
   - Color mismatches
   - Texture discontinuities
   - Obvious repeat patterns

### Fixing Seam Issues

**Prompt refinement:**
```
"The edges don't match perfectly:
- Left edge must pixel-perfectly match right edge
- Top edge must pixel-perfectly match bottom edge
Regenerate with perfect edge matching."
```

**Manual fix:** Clone stamp/healing brush in image editor

---

## Asset Types

### Tilesets

**Standard configurations:**
- 2×2 grid (4 tiles) for variety
- Seamless within each tile AND between tiles
- Consistent lighting direction

**Tile layout pattern:**
```
Top-left: Base clean
Top-right: Base + variation A
Bottom-left: Base + variation B
Bottom-right: Mixed variations
```

**Prompt structure:**
```
"2x2 tileset grid, each tile [SIZE], seamlessly tileable,
[THEME] with [VARIATIONS].
Top-left: [description]
Top-right: [description]
Bottom-left: [description]
Bottom-right: [description]
--tile --ar 1:1"
```

### Character Sprites

**Key requirements:**
- Clear silhouette at game scale
- Consistent proportions (head 1/5, body 3/5, legs 1/5)
- Transparent background
- Top-left lighting (game standard)

**Prompt structure:**
```
"[SIZE] pixel art character sprite of [NAME],
[DESCRIPTION] in [POSE].
[CLOTHING/SURFACE DETAILS].
[KEY VISUAL ELEMENT].
Transparent background, top-left lighting."
```

**For animation sheets:**
- 8 directions × N frames
- Layout: rows = directions, columns = frames
- Specify frame count and direction order

### Walk Cycles

**Standard frame counts:**
- 4 frames: Basic (retro feel)
- 6 frames: Smooth (recommended)
- 8 frames: Very smooth (high detail)

**8-directional layout:**
```
Row 1: North (away)
Row 2: Northeast
Row 3: East (right)
Row 4: Southeast
Row 5: South (toward)
Row 6: Southwest
Row 7: West (left)
Row 8: Northwest
```

**Animation quality checklist:**
- [ ] Weight shifts left-right (hip movement visible)
- [ ] Arm swing opposes leg motion
- [ ] Legs fully extend and contract
- [ ] Head stable with minimal bob
- [ ] Smooth frame-to-frame transitions

### Portraits

**Common uses:**
- Dialogue boxes
- Character selection
- Inventory/status screens

**Key requirements:**
- 3/4 facing camera (most expressive)
- Clear facial features at target size
- Expression matches character personality
- Consider warm/cool variants for context

**Variant workflow:**
1. Generate base portrait
2. Use as object reference
3. Generate expression variants (happy, concerned, angry)
4. Generate lighting variants (warm Sanctuary, cool dungeon)

### Enemies

**Size communicates threat:**
| Threat Level | Typical Size | Silhouette |
|--------------|--------------|------------|
| Low (fodder) | 16×16, 32×32 | Simple |
| Medium | 32×48, 48×48 | Moderate complexity |
| High | 64×64 | Complex, distinctive |
| Boss | 96×96+ | Imposing, detailed |

**Color alignment strategy:**
- Neutral enemies: Zone-appropriate colors (greens, tans, grays)
- Aligned enemies: Faction colors as ACCENTS only (not full body)

**Telegraphing visual cues:**
- Attack wind-up poses
- Glow effects for charging
- Clear differentiation between idle/attack/damaged states

---

## AI-Specific Parameters for Pixel Art

### Midjourney v7

| Parameter | Value | Purpose |
|-----------|-------|---------|
| `--s` | 0-50 | Low stylize for clean pixels |
| `--style raw` | flag | Literal interpretation |
| `--tile` | flag | Seamless tiling |
| `--ar` | varies | Match target dimensions |
| `--no` | list | Exclude anti-aliasing, gradients, blur |

**Recommended --no list:**
```
--no anti-aliasing, smooth edges, gradients, blur, photorealistic,
3D render, concept art style, painterly, soft focus
```

### Nano Banana Pro (Gemini)

- Provide grid templates as reference images
- Use explicit dimensional constraints
- Specify "pixel art" style explicitly
- Request validation after generation

### General Prompting

**DO: Front-load the subject**
```
GOOD: "A pixel art enemy sprite, shambling humanoid..."
BAD:  "32x48, HD, pixel art, enemy, shambling..."
```

**DO: Use natural language**
```
GOOD: "A warm HD pixel art character standing in idle pose"
BAD:  "character, idle pose, pixel art, HD, warm palette"
```

**DO: Describe the image, not instructions**
```
GOOD: "Ancient temple stone with subtle moss growth"
BAD:  "Create a tileable texture that can repeat"
```

---

## Style Spectrum

### Retro/Chunky (8-bit/16-bit)

- Very limited palettes (4-16 colors)
- Visible individual pixels
- Minimal anti-aliasing
- Nostalgic aesthetic

**MJ settings:** `--v 4 --s 0-25`
**Keywords:** "8-bit", "16-bit", "retro", "NES style", "SNES style"

### HD Pixel Art (Modern)

- Larger palettes (32-64 colors)
- Clean but visible pixels
- Selective anti-aliasing
- High detail at larger sizes

**MJ settings:** `--v 7 --s 25-50 --style raw`
**Keywords:** "HD pixel art", "Eastward style", "modern pixel art"

### Polished Pixel Art

- Smooth anti-aliased edges where appropriate
- Rich detail and textures
- Approaches illustration quality
- Best for larger sprites (128px+)

**MJ settings:** `--v 7 --s 50-100`
**Keywords:** "polished pixel art", "Blasphemous style", "detailed pixel art"

---

## Common Issues and Solutions

### Architectural Bias

**Problem:** Requesting floor textures produces buildings/rooms instead.

**Solutions:**
1. **Multi-prompt weights:**
   ```
   stone floor texture::3 weathered blocks::2
   temple architecture::-2 buildings::-2 walls::-2
   ```
2. **Orthographic keywords:** "orthographic top-down, flat 2D, no perspective"
3. **Material-first language:** Describe surface, not context

### Color Bleeding

**Problem:** Requested color appears in unexpected areas.

**Solutions:**
- More specific color placement: "blue robe, NOT blue skin"
- Use reference images for color distribution
- Post-process in image editor

### Inconsistent Lighting

**Problem:** Lighting direction varies across assets.

**Solutions:**
- Always specify: "top-left lighting"
- Use style reference from first successful asset
- Batch generate related assets in same session

### Loss of Detail at Small Scale

**Problem:** Details disappear when viewed at game size.

**Solutions:**
- Generate larger, test at target scale
- Prioritize silhouette over internal detail
- Use higher contrast for important features
- Test in actual game context before finalizing
