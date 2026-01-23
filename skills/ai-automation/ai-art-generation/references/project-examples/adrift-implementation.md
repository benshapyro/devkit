# Adrift Project Implementation

This file demonstrates how to apply the `ai-art-generation` skill to a specific project. Other projects can use this as a template for their own project-specific implementation.

---

## Project Overview

**Game:** Adrift (Cozy Apocalypse Roguelike)
**Engine:** Godot 4.5 with GDScript
**Art Style:** Polished pixel art (Blasphemous-adjacent)
**Core Loop:** Sanctuary management + turn-based roguelike exploration

---

## Style Fusion (LOCKED)

All Adrift assets share the same rendering style, regardless of color palette:

```
STYLE FUSION (applies to ALL game assets):
- EASTWARD warmth: HD pixel art, emotionally resonant, approachable
- WEATHERED REALISM: Worn, lived-in details that tell a story
- HADES ENERGY: Bold readable silhouette, dynamic presence
```

**What this means:**
- Eastward warmth = the *rendering quality* (not warm colors everywhere)
- Weathered realism = details tell stories (torn clothes, worn edges)
- Hades energy = bold silhouettes, readable at small scale

**Color palettes are separate from style fusion.**

---

## Temperature as Narrative

Color temperature communicates location and safety level:

| Context | Temperature | Meaning |
|---------|-------------|---------|
| Sanctuary | WARM | Safety, home, preservation |
| Veil (surface) | WARM | Above-ground, familiar |
| Marrow (dungeon) | COOL | Transformation, descent, alien |

**Design principle:** Players should feel the temperature shift when moving between areas.

---

## Regional Palettes

### Sanctuary Palette (Warm)

```
SANCTUARY PALETTE:
- Cream: #F4E4BC (primary light)
- Amber: #E8C170 (warm accent)
- Sage: #A8B35C (vegetation)
- Forest: #6B8E4E (deep vegetation)
- Wood: #5C4A3D (structural)
- Weathered: #6B6B5A (mid stone)
- Deep: #4A4A3D (dark shadow)
```

**Use for:** All Sanctuary locations, friendly NPCs, surface environments

### Marrow Palette (Cool)

```
MARROW/EXPEDITION PALETTE:
- Shadow: #2D3436 (darkest)
- Stone: #4A5568 (base)
- Dusk: #5C5470 (mid tone)
- Twilight: #6B5B7A (cool accent)
- Void: #1A1A2E (absolute dark)
```

**Use for:** Dungeon tiles, expedition environments, threat-adjacent elements

---

## Asset Specifications

### Native Resolutions (V3.0 Update)

| Asset Type | Size | Aspect Ratio | MJ Settings |
|------------|------|--------------|-------------|
| Character sprites | 128×192 | 2:3 | `--ar 2:3 --s 50 --q 2` |
| Tiles | 128×128 | 1:1 | `--ar 1:1 --tile` |
| Portraits | 128×128 | 1:1 | `--ar 1:1 --s 100-250` |
| Small enemies | 64×64 or 96×96 | 1:1 | `--ar 1:1 --s 25` |
| Large enemies/bosses | 192×256 or 256×256 | varies | `--ar 3:4 --s 50` |

**Why 128×192 native:** V7 naturally produces excellent polished pixel art at this size. Fighting it to make 32×48 chunky pixels was inefficient.

---

## Enemy Color Alignment

Enemy colors communicate alignment with game factions:

### Three Categories

| Alignment | Colors | Visual Message | Examples |
|-----------|--------|----------------|----------|
| **Neutral** | Greens, teals, grays, browns | Natural dungeon creature | Husk, Weeper, Skitter, Shard |
| **Veil-Aligned** | Gray + purple/violet accents | Guardian origin, preservation | Warden, threshold spirits |
| **Marrow-Aligned** | Dark + red/crimson accents | Deep corruption, transformation | Heart region creatures |

### Key Principle: Accents, Not Full Body

- Purple/red are **accent colors only** (eyes, veins, aura)
- Keep body colors **neutral** (gray, brown, bone)
- Player transformation uses **saturated** purple/red on equipment
- Enemy alignment uses **desaturated/muted** purple/red as undertones

This keeps player feedback readable while allowing thematic enemy coloring.

### Palette by Region

| Region | Floors | Default Palette | Alignment Notes |
|--------|--------|-----------------|-----------------|
| Threshold | 1-5 | Mossy greens, teal, gray-brown | Mostly neutral; Warden has purple |
| Sinew | 6-10 | Pale pink, sinew white, tension red | Red = muscle, not corruption |
| Hollow | 11-15 | Ashen gray, sickly green, void black | Neutral-dark; absence of color |
| Heart | 16-20 | Crimson, burgundy, pulsing red | Red IS the zone; Marrow expected |

---

## Character: Seren

### Visual Identity

```
SEREN SPECIFICATIONS:
- Aesthetic: "Blade wrapped in silk" — kind but keen
- Age: Ageless (not old, not young—eternal prime)
- Build: Defined, elegant, not frail
- Hair: Silver-white, long, flowing, catches light
- Face: Sharp intelligent eyes, high cheekbones
- Clothing: Layered robes in soft teals and cream
```

### Projection Quality (Visual Tells)

Seren is a projection, not fully physical. Subtle visual tells:
- Edges slightly soft (not sharp pixel edges everywhere)
- Shadow is wrong (too faint, wrong angle)
- Light interaction slightly off (doesn't cast completely)
- Stillness quality (no breath motion)

---

## Character: Kael (Player)

### Visual Identity

```
KAEL SPECIFICATIONS:
- Role: Weary survivor, practical adventurer
- Build: Average, functional
- Clothing: Earth tones (brown, cream, sage)
- Equipment: Practical, worn, lived-in
- Expression: Determined but tired
```

### Transformation Stages

Player equipment shows transformation via accent colors:

| Stage | Transform % | Veil Accent | Marrow Accent |
|-------|-------------|-------------|---------------|
| Untuned | 0-10% | None | None |
| Touched | 11-30% | Soft Lavender #9B7BB8 | Warm Coral #E85C5C |
| Attuned | 31-50% | Medium Violet #7B5BA8 | Deep Salmon #D64545 |
| Resonant | 51-70% | Deep Purple #5B3B8C | Rich Crimson #C42B2B |
| Saturated | 71-90% | Vivid Violet #4A1A6B | Blood Red #A01515 |
| Crystallized | 91-100% | Void Purple #3A0A4A | Heart Crimson #800000 |

Apply via shader, not separate sprite sets.

---

## Sanctuary Locations

### The Hold (6 Stations)

| Station | Theme | Key Visual Elements |
|---------|-------|---------------------|
| The Foundry | Warm, industrial | Orange-amber glow, blackened metal, active forge |
| The Hall | Grand, ancient | High ceilings, storage, loadout display |
| The Pool | Contemplative | Circular pool, teal-silver water, ancient stone |
| The Mirror | Mysterious | Reflective surface, transformation feedback |
| The Athanor | Alchemical | Glowing vessels, material transmutation |
| The Line | Travel hub | Portal/waypoint aesthetic |

### Open Areas

| Location | Theme | Key Visual Elements |
|---------|-------|---------------------|
| Seren's Fire | Communal center | Central fire, warm gathering space |
| The Grove | Growing station | Vegetation, planters, growth |
| The Cookfire | Food preparation | Cooking implements, warm light |
| The Bower | Rest/sleep | Woven canopy, intimate shelter |

---

## Prompt Templates (Adrift-Specific)

### Sanctuary Floor Tile (LOCKED)

```
Pixel art stone texture, seamless tileable pattern, flat 2D orthographic,
cream limestone blocks, warm gray-beige, weathered surface,
material sample, no depth, no perspective, no objects,
polished pixel art, 128x128 pixels, clean pixel edges,
warm neutral palette: cream #E8DDD0, warm beige #C4B8A8, soft brown #9B8B7A, shadow #6B5F52

--tile --ar 1:1 --s 25 --style raw --v 7
--no architecture, building, walls, columns, ruins, isometric, 3D, scene, room, perspective, objects
```

**Note:** Fighting MJ architectural bias requires explicit "material sample, no depth, no perspective" language and extensive --no list. Lower stylize (25) keeps it literal.

### Threshold Floor Tile (LOCKED)

```
Pixel art floor tile, seamless tileable texture, top-down overhead view,
ancient temple stone floor, weathered ceremonial blocks, subtle cracks and worn edges,
cooling violet undertones in shadows, faded cream stone transitioning to cool gray,
sparse moss in crevices, 128x128 pixels, HD pixel art style like Dead Cells and Blasphemous,
clean pixel edges, bone white #F0EBE0, cool gray #8B8A90, faded violet shadow #7A7080,
simple pattern for tactical readability

--v 7 --s 50 --tile --ar 1:1
```

**Note:** "Cooling violet shadows" + "faded cream transitioning to cool gray" creates the "warmth fading" feel at dungeon entrance.

### Neutral Enemy — Husk (LOCKED)

```
Pixel art enemy sprite, full body head to toe, top-down RPG game,
shambling undead humanoid, hollow empty chest cavity visible, thin emaciated limbs,
reaching arms, hunched posture, tattered remnants of clothing,
pathetic and sad not terrifying, slow shambling creature,
128x192 pixels, HD pixel art style like Dead Cells and Blasphemous,
clean pixel edges, pale gray-green skin #7A9B8A, bone white #E8DDD4,
decay brown #6B6B5A, tattered cloth gray, transparent background

--v 7 --s 50 --ar 2:3
```

**Note:** "Pathetic and sad not terrifying" is key — you fight corpses, not monsters. Neutral colors (no purple/red) keep player transformation feedback clear.

---

## Godot Integration

### Import Settings

```
All Adrift pixel art:
- Texture Filter: Nearest (CRITICAL)
- Mipmaps: OFF
- Compression: Lossless (PNG)
```

### Transformation Shader

```glsl
shader_type canvas_item;

uniform vec3 accent_color : hint_color = vec3(1.0, 1.0, 1.0);
uniform float accent_strength : hint_range(0.0, 1.0) = 0.0;

void fragment() {
    vec4 tex_color = texture(TEXTURE, UV);
    float brightness = (tex_color.r + tex_color.g + tex_color.b) / 3.0;

    // Apply to equipment only (bright areas)
    if (brightness > 0.6 && tex_color.a > 0.5) {
        vec3 blended = mix(tex_color.rgb, accent_color, accent_strength);
        COLOR = vec4(blended, tex_color.a);
    } else {
        COLOR = tex_color;
    }
}
```

Update uniforms based on player resonance stage.

---

## Cross-References

| Topic | Reference |
|-------|-----------|
| Full art direction | `adrift-docs/1-bibles/sensory-bible.md` |
| Enemy specifications | `adrift-docs/1-bibles/bestiary-bible.md` |
| Character details | `adrift-docs/1-bibles/character-bible.md` |
| MJ prompts | `adrift-dev/workstreams/midjourney-v7-adrift-guide.md` |
| NBP prompts | `adrift-dev/workstreams/nano-banana-pro-adrift-guide.md` |
| Asset prompt templates | `adrift-dev/asset-prompts-v2.md` |
