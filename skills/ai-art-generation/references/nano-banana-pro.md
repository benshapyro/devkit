# Nano Banana Pro (Gemini) for Game Assets

This reference covers Nano Banana Pro (NBP) / Gemini image generation techniques for game art. NBP excels at conversational refinement and precise control—use it when Midjourney exploration is complete and you need pixel-perfect finalization.

---

## Table of Contents

1. [NBP Strengths](#nbp-strengths)
2. [Golden Rules](#golden-rules)
3. [Workflows](#workflows)
4. [Asset Type Guides](#asset-type-guides)
5. [Iterative Refinement Patterns](#iterative-refinement-patterns)
6. [Godot Integration](#godot-integration)
7. [Model Configuration](#model-configuration)

---

## NBP Strengths

### When NBP Beats Midjourney

| Scenario | Why NBP Wins |
|----------|--------------|
| Precise refinement needed | Conversational editing, not regeneration |
| Specific palette requirements | Follows hex code constraints well |
| Iterative back-and-forth | Edit existing images, not start over |
| Constraint compliance | "Thinking" model understands intent |
| Final polish | Fine control over specific elements |

### When Midjourney Beats NBP

| Scenario | Why MJ Wins |
|----------|-------------|
| Rapid exploration | Draft Mode, 10× speed |
| Style variety | More diverse outputs |
| Complex compositions | Better at scenes/environments |
| Object/character consistency | --oref is powerful |

### Optimal Hybrid Workflow

```
1. EXPLORATION: Midjourney Draft Mode (quick concepts)
2. REFINEMENT: Midjourney Standard (select winners)
3. FINALIZATION: NBP (pixel-perfect polish)
```

---

## Golden Rules

### Rule 1: Sensory Grounding First, Pixels Second

Describe the **feeling** and atmosphere, not just objects.

```
BAD:  "pixel art dungeon floor"
GOOD: "cool-toned overgrown temple ruins, 32x32 tileable pixel art,
       mysterious atmosphere, purple-violet accent tints at depth boundaries"
```

**Include:**
- Temperature (warm/cool)
- Lighting mood (soft/harsh)
- Emotional quality (cozy/oppressive/mysterious)

### Rule 2: Grid Templates are Your Foundation

NBP excels when given grid structure references.

**Setup:**
1. Create template file: 8-pixel cell grid image
2. Upload to NBP to lock spatial consistency
3. Request: "Fill each cell with [element], maintaining grid structure exactly"

**Benefits:**
- Locks spatial consistency
- Prevents scale drift
- Ensures tile alignment

### Rule 3: Conversational Refinement Over Re-rolling

**Never regenerate from scratch twice. Edit instead.**

```
WORKFLOW:
1. First pass: Generate full asset
2. Analyze: "This is 85% correct, but X needs adjustment"
3. Edit: "Keep everything identical, change only [specific element]"
4. Iterate: Refine color, lighting, or detail

EXAMPLE:
"Perfect, but the moss is too saturated. Desaturate the green by 20%
while keeping all stone textures and lighting identical."
```

### Rule 4: Specify Every Constraint

NBP understands intent, but ambiguity leads to drift. Lock explicitly:

- **Aspect ratio** (1:1 for tiles, 2:3 for sprites)
- **Resolution** (32×32, 64×64, 128×192)
- **Color palette** (hex codes)
- **Transparent background** (critical for game assets)
- **Grid alignment** (pixel-perfect spacing)

**Template:**
```
TECHNICAL REQUIREMENTS:
- Dimensions: [WIDTH]×[HEIGHT] pixels
- Aspect ratio: [RATIO]
- Background: Transparent (PNG)
- Color palette: Locked to [list hex codes]
- Style: [HD pixel art / polished pixel art / retro]
```

---

## Workflows

### Palette Lock Workflow

**Problem:** Colors drift from intended palette.

**Solution:**
1. Define palette explicitly (hex codes)
2. Provide as text constraint in every prompt
3. Request validation after generation

```
COLOR PALETTE (EXACT - no other colors):
- Primary: #5C4A3D (warm brown)
- Secondary: #E8C170 (amber)
- Accent: #A8B35C (sage green)
- Shadow: #4A4A3D (dark)
- Highlight: #F4E4BC (cream)

After generation, verify all pixels use only these colors.
No interpolation. No new colors.
```

### Seamlessness Check Workflow

1. Generate with explicit tiling instruction
2. Download and test in tile preview tool
3. If seams visible, request fix conversationally:

```
"I'm going to tile this 4×4. The edges don't match.
- Left edge (pixels 0-31) must match right edge exactly
- Top edge must match bottom edge exactly
Regenerate with perfect edge matching. Keep all other elements identical."
```

### Animation Fluidity Workflow

1. Generate base pose
2. Request frame variations
3. Test timing in engine
4. Request adjustments conversationally

```
ANIMATION CHECK:
1. Does weight shift left-right (hip movement)?
2. Do legs fully extend/contract (not stiff)?
3. Does arm swing oppose leg motion?
4. Is motion smooth frame-to-frame (no pose jumps)?

FIX REQUEST:
"The walk feels stiff. Increase hip sway by 20% (weight should visibly
shift left-right). Leg extension more pronounced (full stride).
Keep same frame count and timing."
```

---

## Asset Type Guides

### Tilesets (32×32 Seamless)

```
NBP PROMPT TEMPLATE:

Generate a 2×2 tileset grid (each cell 32×32 pixels, total 64×64).
Seamlessly tileable pixel art floor tiles.

VISUAL SPECIFICATIONS:
- Style: HD pixel art (detailed, not 8-bit low-res)
- Tileable: Each tile blends seamlessly in all directions
- Theme: [DESCRIPTION]

COLOR PALETTE (EXACT):
- [List hex codes with purpose]

GRID LAYOUT (2×2):
- Top-left: [description]
- Top-right: [description]
- Bottom-left: [description]
- Bottom-right: [description]

MATERIAL DETAILS:
- [Surface material and texture]
- [Lighting direction and quality]
- [Shadow characteristics]

TRANSPARENCY:
- Transparent background (PNG)
- Solid tiles only (no floating objects)

VERIFICATION:
- Ensure seamless tiling when placed 4×4
- No visible grid lines at edges
```

### Character Sprites (32×48 or 128×192)

```
NBP PROMPT TEMPLATE:

Create a pixel art character sprite.

CHARACTER SPECIFICATIONS:
- Name: [NAME]
- Size: [WIDTH]×[HEIGHT] pixels
- Pose: [DESCRIPTION]
- View: [3/4 facing / side view / front]

VISUAL IDENTITY:
- Aesthetic: [key visual descriptors]
- Expression: [mood and facial expression]
- Clothing: [outfit description]

COLOR PALETTE:
- [List colors with hex codes]

LIGHTING & SHADING:
- Key light: Top-left (consistent with game)
- Shadow style: [soft/hard]

TRANSPARENCY:
- Transparent background
- Full character only (no environment)
- Pixel-perfect silhouette

QUALITY:
- Clean pixel edges
- Readable at game scale
- Consistent proportions
```

### Walk Cycles (8-Directional)

```
NBP PROMPT TEMPLATE:

Create 8-directional walk cycle sprite sheet.

ANIMATION SPECIFICATIONS:
- Directions: 8 (N, NE, E, SE, S, SW, W, NW)
- Frames per direction: 6 (smooth loop)
- Frame size: [WIDTH]×[HEIGHT] pixels
- Total output: 6 columns × 8 rows

LAYOUT:
- Rows: One per direction
- Row 1: North (away from camera)
- Row 2: Northeast
- [continue through Row 8: Northwest]
- Columns: 6 frames of walk cycle

ANIMATION QUALITY:
- Framerate: 8 FPS equivalent
- Gait: Natural walking (not running)
- Weight shift: Visible hip movement left-right
- Arm swing: Opposite-arm coordination
- Head: Minimal bob, stable neck

CHARACTER:
- [Description matching previous sprites]

COLOR PALETTE:
- [Same palette as character reference]

TRANSPARENCY:
- Transparent background
- Pixel-perfect edges
- No stray pixels or halos
```

### Portraits (128×128)

```
NBP PROMPT TEMPLATE:

Generate character portrait for dialogue UI.

PORTRAIT SPECIFICATIONS:
- Size: 128×128 pixels
- Framing: 3/4 facing camera
- Expression: [mood]

CHARACTER:
- [Character description]

CONTEXT VARIANTS (if needed):
Generate two versions with identical features but different color grading:

VARIANT A - WARM CONTEXT:
- Color grade: Warm amber highlights
- Lighting: Golden hour quality
- Mood: Safe, welcoming

VARIANT B - COOL CONTEXT:
- Color grade: Cool gray-green shadows
- Lighting: Desaturated, directional
- Mood: Ancient, mysterious

CONSISTENCY:
- Facial features IDENTICAL in both
- Only color temperature changes

TRANSPARENCY:
- Transparent background
- Character portrait only
```

---

## Iterative Refinement Patterns

### The "Palette Lock" Fix

**Issue:** Colors drifting outside locked palette.

```
CORRECTION PROMPT:
"Perfect, but I need strict color discipline. Regenerate using ONLY these hex codes:
- #XXXXXX (color name)
- #XXXXXX (color name)
[list all palette colors]

No interpolation between these colors. No new colors.
Only these [N] colors in the output."
```

### The "Seamlessness" Fix

**Issue:** Tile seams visible.

```
CORRECTION PROMPT:
"I'm tiling this 4×4 and see visible seams.
- Left edge pixels must match right edge pixels exactly
- Top edge must match bottom edge exactly
- All corners must connect seamlessly

Remake with perfect edge matching. Keep everything else identical."
```

### The "Animation Stiffness" Fix

**Issue:** Walk cycle feels robotic.

```
CORRECTION PROMPT:
"The walk cycle feels stiff.
- Increase weight shift (hips should swing left/right more visibly)
- Longer leg extension (more pronounced stride)
- Smoother arm swing (should counter-rotate with legs)

Keep same 6 frames and animation speed. Same character appearance."
```

### The "Edge Clarity" Fix

**Issue:** Sprite edges too fuzzy or too sharp.

```
CORRECTION PROMPT:
"Antialiasing should be subtle (soft edges, not harsh pixels).
BUT maintain pixel-perfect silhouette clarity at [SIZE] scale.
This is HD pixel art—selective softness, not blurry or jagged."
```

---

## Godot Integration

### Import Settings

```
Workflow after NBP generation:

1. Download PNG from NBP
2. Place in res://assets/sprites/
3. Click PNG → Import tab
4. Settings:
   - Texture Filter: Nearest (CRITICAL for pixels)
   - Mipmaps: OFF
   - Compression: Lossless
5. Reimport

For Tilesets:
1. Create TileSet resource (.tres)
2. Add tileset texture
3. Set Tile Size: (32, 32) or appropriate
4. Enable physics geometry if needed
5. Test in scene
```

### SpriteFrames Setup

```gdscript
# For animated sprites from NBP sprite sheets:

1. Use SpriteFrames Generator addon
2. Load sprite sheet PNG
3. Auto-slice by tile size (e.g., 32×48 for characters)
4. Set frame duration (0.125s = 8 FPS)
5. Export as .tres
6. Assign to AnimatedSprite2D.sprite_frames

# Code to set animation:
animated_sprite.animation = "walk_east"
animated_sprite.frame = 0
animated_sprite.play()
```

### Transformation Color Shader

```glsl
shader_type canvas_item;

uniform vec3 accent_color : hint_color = vec3(0.6, 0.47, 0.73);
uniform float accent_strength : hint_range(0.0, 1.0) = 0.3;

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    float bright = (tex_color.r + tex_color.g + tex_color.b) / 3.0;

    // Apply accent to equipment/bright areas only
    if (bright > 0.5 && tex_color.a > 0.5) {
        vec3 blended = mix(tex_color.rgb, accent_color, accent_strength);
        COLOR = vec4(blended, tex_color.a);
    } else {
        COLOR = tex_color;
    }
}
```

Update shader uniforms based on character state.

---

## Model Configuration

### AI Studio Setup

```
Model: Nano Banana Pro (Gemini 3 Pro Image)
Resolution: 1024×1024 (upscale for final assets)
Aspect Ratio: 1:1 (tiles) or 2:3 (sprites) or 6:8 (sheets)
Thinking Mode: ON (enables complex reasoning)
Safety Filters: OFF (pixel art is not inappropriate)
Generation Time: ~30-60 seconds per image
```

### API Integration (Python)

```python
import anthropic

client = anthropic.Anthropic(api_key="YOUR_KEY")

response = client.messages.create(
    model="nano-banana-pro",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "[Your NBP prompt]"
                }
            ]
        }
    ]
)

# Handle response
image_data = response.content[0].image
```

---

## Quality Checklist

Before exporting any NBP-generated asset:

| Aspect | Check | Pass |
|--------|-------|------|
| Color Palette | All colors within locked palette? | |
| Transparency | Clean edges, no halos? | |
| Seamlessness | Tiles match on all edges? | |
| Animation | Smooth framerate, natural motion? | |
| Silhouette | Readable at game scale? | |
| Lighting | Consistent key light direction? | |
| Resolution | Correct pixel dimensions? | |
| File Format | PNG, not JPEG? | |

---

## Common Issues

### Issue: Colors outside palette appearing

**Cause:** NBP interpolated between palette colors.

**Fix:** Explicit hex code list with "no interpolation" instruction.

### Issue: Sprite edges fuzzy or too sharp

**Cause:** Anti-aliasing mismatch.

**Fix:** Specify "subtle antialiasing for HD pixel art" with target scale.

### Issue: Animation feels jerky

**Cause:** Insufficient pose variation or weight shift.

**Fix:** Request more hip sway, leg extension, arm swing in refinement pass.

### Issue: Tiles have different brightness

**Cause:** Lighting inconsistency across tiles.

**Fix:** Specify "consistent top-left lighting across all tiles" and use same prompt for batch.
