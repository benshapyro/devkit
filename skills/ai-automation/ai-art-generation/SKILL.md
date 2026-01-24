---
name: ai-art-generation
description: Guides AI image generation for game assets and creative projects. Use when prompting Midjourney, Nano Banana Pro, DALL-E, Stable Diffusion, or other AI image tools. Covers iterative refinement, style consistency, quality validation, and game engine integration. v1 focuses on pixel art; structure supports future expansion to concept art, 3D, and UI mockups.
tagline: "Create stunning visuals"
roles:
  - Designer
  - Content Creator
  - Digital Marketer
tasks:
  - Create Images
favorite: true
---

# AI Art Generation

## Overview

This skill teaches the **discipline** of AI art generation—principles that apply regardless of which tool you use. The goal is production-ready game assets, not just pretty pictures.

**v1 Focus:** Pixel art for 2D games (HD pixel art, polished pixel art, retro pixel art)

**Core insight:** AI art generation is 40% prompting, 60% iteration and refinement. Budget accordingly.

## Universal Principles

### 1. Iterative Refinement Over Re-Rolling

Never regenerate from scratch. Edit instead.

```
WORKFLOW:
1. First pass → Generate initial concept
2. Analyze → "This is 85% correct, but X needs adjustment"
3. Edit → "Keep everything, change only [specific element]"
4. Iterate → Refine color, lighting, or detail
5. Finalize → Export when 95%+ correct
```

**Industry standard:** Budget 3-5 refinement cycles per concept. Professional studios report **40:1 generation ratio** (40 prompts for 1 keeper).

### 2. Constraint Specification

Lock what needs consistency. Ambiguity leads to drift.

**Always specify:**
- Exact dimensions (pixels, not "small" or "large")
- Aspect ratio
- Color palette (hex codes when critical)
- Transparency requirements
- Grid alignment for game assets

**Example:**
```
BAD:  "pixel art character"
GOOD: "128x192 pixel art character sprite, transparent background,
       top-left lighting, earth tone palette (#5C4A3D, #E8C170, #A8B35C)"
```

### 3. Exploration → Refinement → Finalization Pipeline

Separate the phases. Different goals require different settings.

| Phase | Goal | Speed | Quality | Cost |
|-------|------|-------|---------|------|
| **Exploration** | Generate many variants | Fast | ~60% | Low |
| **Refinement** | Perfect top 3-5 concepts | Standard | 100% | Normal |
| **Finalization** | Production-ready export | Standard | 100% | Normal |

**Time allocation:** Exploration (20%) → Refinement (50%) → Finalization (30%)

### 4. Reference Images for Consistency

Two types of references serve different purposes:

| Reference Type | Locks | Use For |
|---------------|-------|---------|
| **Style reference** | Aesthetic, colors, textures, lighting | Maintaining visual cohesion across asset batches |
| **Object reference** | Specific items, characters, architecture | Consistent characters, recurring props |

**Principle:** Create hero assets first, use as references for variants.

### 5. Quality Validation Before Export

Never import directly to game engine. Always validate.

**Universal Checklist:**
- [ ] Transparency edges clean (no white fringing/halos)
- [ ] Dimensions match target exactly (not "close enough")
- [ ] Palette within bounds (no unexpected colors)
- [ ] Seamless if tileable (test with 4x4 tile preview)
- [ ] Animation smooth if animated (frame timing, weight shift)
- [ ] Silhouette readable at game scale

## Tool Selection Matrix

| Need | Best Tool | Why |
|------|-----------|-----|
| Rapid exploration | MJ v7 Draft Mode | 10x speed, low cost |
| Precise refinement | NBP / Gemini | Conversational editing |
| Style consistency | MJ v7 --sref | Palette/mood lock |
| Character consistency | MJ v7 --oref | Object appearance lock |
| Pixel-perfect control | Aseprite (manual) | Frame-by-frame precision |
| Photorealistic | MJ v7 / DALL-E | Trained for realism |
| Custom model training | Scenario.gg | Your exact style |

**Reality check:** No AI tool produces production-ready assets. Budget 20-50% time for post-generation cleanup.

## When to Read Reference Files

| Reference | Read When |
|-----------|-----------|
| `references/pixel-art-patterns.md` | Working on pixel art game assets |
| `references/midjourney-v7.md` | Using Midjourney v7 specifically |
| `references/nano-banana-pro.md` | Using NBP / Gemini image generation |
| `references/templates/*.md` | Need copy-paste prompt structure |
| `references/project-examples/*.md` | Working on specific projects |

## Pixel Art Quick Start

**For detailed patterns, see:** `references/pixel-art-patterns.md`

**Key settings for pixel art (MJ v7):**
```
--s 0-50      Low stylize (cleaner edges)
--style raw   Literal interpretation
--tile        Seamless for tilesets
--ar X:Y      Match your target dimensions
```

**Common sizes:**
- Characters: 32×48, 64×64, 128×192 pixels
- Tiles: 16×16, 32×32, 64×64, 128×128 pixels
- Portraits: 64×64, 128×128 pixels

## Godot Integration (Universal)

**Import settings for pixel art:**
```
Texture Filter: Nearest (CRITICAL - preserves pixels)
Mipmaps: OFF
Compression: Lossless (PNG)
```

**SpriteFrames setup:**
1. Place sprite sheet in `res://assets/sprites/`
2. Create SpriteFrames resource
3. Set frame dimensions and FPS
4. Assign to AnimatedSprite2D

**Basic color-shift shader (for variants):**
```glsl
shader_type canvas_item;
uniform vec3 accent_color : hint_color = vec3(1.0, 1.0, 1.0);
uniform float accent_strength : hint_range(0.0, 1.0) = 0.3;

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    float brightness = (tex_color.r + tex_color.g + tex_color.b) / 3.0;
    if (brightness > 0.5 && tex_color.a > 0.5) {
        COLOR = vec4(mix(tex_color.rgb, accent_color, accent_strength), tex_color.a);
    } else {
        COLOR = tex_color;
    }
}
```

## When to Use Manual Creation Instead

**Switch to manual tools if:**
- Same issue after 3 different prompt strategies
- Generation time exceeds 30 minutes for single asset
- Results getting worse with iteration
- Asset requires pixel-perfect precision (UI, animation frames)

**Manual tools:**
- **Aseprite:** Pixel art (industry standard)
- **Piskel:** Pixel animation (free)
- **Pyxel Edit:** Tilesets
- **Photoshop/GIMP:** General editing

**Hybrid approach:** Use AI for inspiration/base → manual refinement in Aseprite

## Legal Considerations (2025-2026)

- **Steam disclosure:** Must disclose AI-generated content
- **Copyright:** AI + significant human input = stronger claim
- **Training data:** May need to prove licensing/ownership
- **Public by default:** Midjourney images are public (potential IP leak)

## Production Pipeline Summary

```
1. EXPLORATION (MJ v7 Draft Mode)
   - Generate 10-20 concepts quickly
   - Test color palettes with --sref
   - Time: 15-20 minutes

2. REFINEMENT (Standard Quality)
   - Regenerate winning concepts at full quality
   - Use --oref for character/object consistency
   - Fine-tune with Remix or conversational editing
   - Time: 20-30 minutes

3. FINALIZATION (NBP or Manual)
   - Lock exact hex codes
   - Fix seams for tilesets
   - Add project-specific details
   - Validate against checklist
   - Time: 10-20 minutes

4. ENGINE INTEGRATION
   - Import with correct settings
   - Test in actual game context
   - Apply shaders if needed
   - Time: 5-10 minutes

Total per asset batch: 50-80 minutes
```

## Common Pitfalls

| Pitfall | Solution |
|---------|----------|
| Colors outside palette | Provide exact hex codes, use style reference |
| Tile seams visible | Validate with 4x4 preview before importing |
| Animation feels stiff | Increase hip sway, arm swing; check weight shift |
| Edges too fuzzy/sharp | Adjust anti-aliasing settings per tool |
| Fighting tool limitations | Switch tools or use manual cleanup |
| Infinite iteration | Set time limit, accept "good enough" |
