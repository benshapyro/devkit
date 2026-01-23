# Midjourney v7 for Game Assets

This reference covers Midjourney v7-specific techniques for generating game art assets. For universal principles, see the main SKILL.md file.

---

> ⚠️ **CRITICAL v7 CHANGES:**
> - **No `/imagine` prefix** — Enter prompts directly, the command is not needed
> - **No multi-prompt weights (`::`)** — This syntax was removed in v7
> - **Use `--oref` not `--cref`** — Character reference was replaced with Omni Reference

---

## Table of Contents

1. [v7 Key Changes](#v7-key-changes)
2. [Core Parameters](#core-parameters)
3. [Generation Modes](#generation-modes)
4. [Consistency System](#consistency-system)
5. [Workflows](#workflows)
6. [Pixel Art Settings](#pixel-art-settings)
7. [Troubleshooting](#troubleshooting)
8. [Parameter Quick Reference](#parameter-quick-reference)

---

## v7 Key Changes

### What's New from v6.1

| Feature | v6.1 | v7 | Impact |
|---------|------|----|----|
| Character Consistency | `--cref` | `--oref` (Omni Reference) | Works for objects AND characters |
| Speed | Standard only | Draft Mode (10x faster) | Rapid iteration |
| Tile Quality | Good | Better upscaling | Preserves seamlessness |
| Face/Hand Quality | Weak point | Significantly improved | Cleaner sprites |
| Text Rendering | Decent | Better (use quotes) | Readable UI elements |

### Deprecated Parameters

**DO NOT USE (replaced or removed in v7):**
- `--cref` → Use `--oref` instead
- `--cw` → Use `--ow` (Omni Weight) instead
- Old upscalers → Use v7 upscalers only
- **Multi-prompt weights (`::`)** → Removed in v7, use natural language instead
- `/imagine` prefix → Not needed, just enter the prompt directly

### New v7 Parameters

- `--oref` — Omni Reference (object/character consistency)
- `--ow` — Omni Weight (0-400, strictness of --oref)
- `--xexp` — Extra Experimental (0-25, cinematic effects)
- Draft Mode — 10x faster, ~60% quality

---

## Core Parameters

### Style Control

| Parameter | Range | Default | Purpose |
|-----------|-------|---------|---------|
| `--s` (stylize) | 0-1000 | 100 | Artistic interpretation |
| `--style raw` | flag | off | Literal prompt interpretation |
| `--q` (quality) | 0.5, 1, 2 | 1 | Detail level |

**For pixel art:**
- `--s 0-50` — Minimal AI interpretation, cleanest edges
- `--s 50-250` — Balanced (good for portraits)
- `--s 250+` — Heavy artistic style (NOT for game assets)

**--style raw (CRITICAL for pixel art):**
```
WITHOUT --style raw: MJ adds artistic flair, softens edges, adds gradients
WITH --style raw: Literal interpretation, cleaner edges, respects constraints
```

### Consistency Control

| Parameter | Purpose | GPU Cost |
|-----------|---------|----------|
| `--oref [URL]` | Lock object/character appearance | 2× normal |
| `--ow [0-400]` | Strictness of --oref | — |
| `--sref [URL/code]` | Lock style/palette/mood | Normal |
| `--sw [0-1000]` | Strictness of --sref | — |
| `--seed [int]` | Reproducibility (~15-20% consistency) | Normal |

**Omni Weight (--ow) guide:**

| Weight | Strictness | Use Case |
|--------|------------|----------|
| 50-75 | Moderate | Structure locked, lighting/angle vary |
| 76-150 | High | All elements consistent, light changes only |
| 151-300 | Very High | Face + body + most clothing locked |
| 300+ | Extreme | Exact match (rarely needed, risks distortion) |

**Style Weight (--sw) guide:**
- 0-100: Subtle influence
- 300-400: **Recommended** for palette/mood lock
- 500+: Very strict (may limit creativity)

### Aspect Ratio

| Asset Type | Aspect Ratio | Example Size |
|------------|--------------|--------------|
| Square tiles | 1:1 | 128×128 |
| Character sprites | 2:3 | 128×192 |
| Wide scenes | 16:9 | 1920×1080 |
| Sprite sheets | varies | 1:2 for 8-row sheets |

---

## Generation Modes

### Draft Mode

**Purpose:** Rapid exploration at lower quality (~60%)

| Aspect | Draft | Standard |
|--------|-------|----------|
| Speed | 10× faster | Normal |
| Cost | Half GPU | Full GPU |
| Quality | ~60% | 100% |
| Use Case | Exploration | Final assets |

**How to use:**
```
--draft [your prompt]
```

**Workflow:**
1. Draft Mode: Generate 20-50 concepts quickly
2. Choose best 3-5 directions
3. Standard Mode: Regenerate winners at full quality

### Standard Quality

**Use for:** All final assets, character consistency, detailed work

```
[prompt] --q 1  (default)
[prompt] --q 2  (higher detail, more GPU)
```

---

## Consistency System

### Three-Layer Approach

| Layer | Parameter | What It Locks | Cost | When to Use |
|-------|-----------|---------------|------|-------------|
| Style | `--sref` | Colors, textures, mood | Normal | All assets in a set |
| Object | `--oref` | Specific items/characters | **2× GPU** | Hero assets only |
| Seed | `--seed` | Minor variations | Normal | Animation frames |

**Recommendation:** Start with `--sref` for style. Add `--oref` only for hero assets.

### Creating Style References

**Method 1: From existing image**
1. Upload reference image to MJ
2. Copy image URL
3. Use: `--sref [URL] --sw 300`

**Method 2: Generate reference swatch**
1. Create 64×64 palette swatch in image editor
2. Upload to MJ
3. Use as `--sref`

### Omni Reference (--oref) Workflow

**Step 1: Generate base asset**
```
[detailed prompt for character/object]
--ar 2:3 --q 2 --s 50 --v 7
```

**Step 2: Choose best result, upscale, save URL**

**Step 3: Generate variants**
```
--oref [saved_URL] --ow 150
[character name] in [new pose/context]
[same style descriptors]
--ar 2:3 --q 2 --v 7
```

---

## Workflows

### Draft → Refine → Finalize

```
PHASE 1: DRAFT MODE (Exploration)
--draft [concept prompt]
Time: 15-30 seconds
Generate: 4-8 concepts
Choose: Best 2-3 directions

PHASE 2: STANDARD (Refinement)
[refined prompt based on learnings] --q 2
Time: 60-90 seconds
Iterate: Remix to adjust

PHASE 3: FINALIZE (Production)
Upscale using v7 upscaler
Validate quality
Export for game
```

### Character Sheet Workflow

```
1. Generate hero portrait (full quality)
   [detailed character description]
   --ar 2:3 --q 2 --s 50 --v 7

2. Save as --oref reference

3. Generate pose variants
   --oref [URL] --ow 150
   [character] in [pose 1], [pose 2], [pose 3]
   Same style, same lighting

4. Generate expression variants
   --oref [URL] --ow 180
   [character] with [expression 1], [expression 2]
   Same face, only expression changes
```

### Tileset Workflow

```
1. Create palette reference
   - 64×64 color swatch image
   - Upload to MJ for --sref code

2. Draft exploration
   --draft --tile [tileset concept]
   --sref [palette] --sw 300 --ar 1:1

3. Refine winner
   --tile [improved prompt]
   --sref [palette] --sw 400 --q 2 --ar 1:1

4. Validate tiling
   - Download PNG
   - Test 4×4 tile in image editor
   - Check for visible seams

5. Upscale (v7 upscaler preserves seams)
```

---

## Pixel Art Settings

### Recommended Parameters by Asset Type

| Asset | Settings |
|-------|----------|
| Character sprites | `--s 25-50 --style raw --q 2 --ar 2:3` |
| Tiles | `--s 50 --tile --ar 1:1` |
| Portraits | `--s 100-250 --q 2 --ar 1:1` |
| Small enemies | `--s 0-25 --style raw --ar 1:1` |
| Bosses | `--s 50 --q 2 --ar 1:1` |

### Comprehensive --no List for Pixel Art

```
--no anti-aliasing, smooth edges, gradients, blur,
photorealistic, 3D render, concept art style,
painterly, soft focus
```

### Prompt Structure

**DO: Front-load subject**
```
GOOD: "A pixel art enemy sprite, shambling humanoid..."
BAD:  "32x48, HD, pixel art, enemy..."
```

**DO: Natural language**
```
GOOD: "A warm HD pixel art character standing in idle pose"
BAD:  "character, idle pose, pixel art, HD, warm"
```

**DO: Describe image, not instructions**
```
GOOD: "Ancient temple stone with subtle moss growth"
BAD:  "Create a tileable texture that repeats seamlessly"
```

---

## Troubleshooting

### Architectural Bias

**Problem:** Requesting floor textures produces buildings instead.

**Solution 1: Orthographic keywords (most effective)**
```
weathered stone ground texture, orthographic top-down,
seamless pattern, flat 2D, no perspective
--tile --ar 1:1 --s 50 --style raw --v 7
```

**Solution 2: Material-first language**
```
GOOD: "cracked earth texture, seamless, top-down"
BAD:  "ground with cracks from above"
```

**Solution 3: Strong --no list**
```
[your texture prompt]
--tile --ar 1:1 --s 50 --style raw --v 7
--no buildings, walls, architecture, structures, perspective, 3D
```

> **Note:** Multi-prompt weights (`::`) do NOT work in v7. Use natural language emphasis and `--no` lists instead.

### Palette Drift

**Problem:** Colors shift from reference.

**Solutions:**
- Increase `--sw` to 300-400
- Provide explicit hex codes in prompt
- Use stronger `--sref` from color swatch
- Add unwanted colors to `--no` list

### Seam Issues in Tiles

**Problem:** Tiles show visible seams after generation.

**Solutions:**
1. Use v7 native upscaler (NOT Creative upscaler)
2. Add to prompt: "edges must match perfectly"
3. Regenerate with explicit seam instruction
4. Manual fix with clone stamp if persistent

### V6 Style Codes Breaking

**Problem:** Old `--sref` codes don't work in v7.

**Solutions:**
- Add `--sv 4` to use v6 codes in v7
- Or regenerate reference in v7 for new code

---

## Parameter Quick Reference

### Quality & Generation

| Parameter | Range | Purpose |
|-----------|-------|---------|
| `--q` | 0.5, 1, 2 | Detail level |
| `--s` | 0-1000 | Stylization (0-50 for pixel art) |
| `--style raw` | flag | Literal interpretation |
| `--v` | 4, 7 | Model version (7 for most uses) |
| `--draft` | flag | 10× faster, 60% quality |
| `--ar` | ratio | Aspect ratio |
| `--seed` | int | Reproducibility |
| `--stop` | 10-100 | Stop early for sketch effect |

### References & Consistency

| Parameter | Purpose |
|-----------|---------|
| `--oref [URL]` | Object/character reference |
| `--ow [0-400]` | Omni weight |
| `--sref [URL/code]` | Style reference |
| `--sw [0-1000]` | Style weight |
| `--iw [float]` | Image weight |
| `--xexp [0-25]` | Experimental effects |

### Special Features

| Parameter | Purpose |
|-----------|---------|
| `--tile` | Seamless repeating pattern |
| `--weird [0-3000]` | Unusual variations |
| `--no [content]` | Exclude elements |
| `--repeat [1-40]` | Batch variations |

### Mode Comparison

| Mode | Speed | Cost | Quality |
|------|-------|------|---------|
| Draft | 10× | Half | ~60% |
| Standard | 1× | Normal | 100% |
| Turbo | 3× | Same | High |
| Relax | Slow | Lower | High |

---

## MJ Editor for Background Removal

**Access:** midjourney.com/editor (requires subscription)

**Capabilities:**
- AI-powered background removal (cleaner than remove.bg for pixel art)
- Inpainting/outpainting for sprite extension
- Regional generation for asset modification

**When to use:** After generation, before game engine import

---

## Model Personalization

**Setup (5-10 minutes):**
1. Go to midjourney.com/personalize
2. Rate ~200 images (like/dislike)
3. Get personal style code
4. Use with `--p` parameter

**Impact:** Trained model better matches your aesthetic preferences.
