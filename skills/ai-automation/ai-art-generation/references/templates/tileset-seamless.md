# Tileset (Seamless) Prompt Template

Copy-paste ready prompts for generating seamless tileable textures.

---

## Midjourney v7 Template

```
/imagine --tile seamless [SIZE]x[SIZE] pixel art floor tileset, [THEME]:

THEME:
[Describe material, atmosphere, and visual identity]

MATERIAL:
- [Primary surface: stone/wood/grass/etc.]
- [Secondary elements: moss/cracks/debris]
- [Lighting: warm diffuse / cool directional / etc.]
- [Shadows: soft / angular / minimal]

TILE LAYOUT (2×2):
- Top-left: Base clean variant
- Top-right: Base + [variation A]
- Bottom-left: Base + [variation B]
- Bottom-right: Mixed [A + B]

COLOR PALETTE (EXACT):
- Primary: #[HEX] ([description])
- Secondary: #[HEX] ([description])
- Accent: #[HEX] ([description])
- Shadow: #[HEX] ([description])
- Highlight: #[HEX] ([description])

STYLE:
[HD pixel art / polished pixel art / retro 8-bit]
Seamlessly tileable in all directions
Transparent background
Top-left lighting

--tile --ar 1:1 --s 50 --style raw --v 7
--no anti-aliasing, smooth edges, gradients, blur, 3D render
```

---

## NBP Template

```
Generate a 2×2 tileset grid (each cell [SIZE]×[SIZE] pixels, total output [SIZE*2]×[SIZE*2]).
Seamlessly tileable pixel art floor tiles.

VISUAL SPECIFICATIONS:
- Style: [HD pixel art / polished pixel art]
- Tileable: Each tile blends seamlessly in all directions
- Theme: [DESCRIPTION]

COLOR PALETTE (EXACT - use only these colors):
- #[HEX]: [purpose]
- #[HEX]: [purpose]
- #[HEX]: [purpose]
- #[HEX]: [purpose]
- #[HEX]: [purpose]

GRID LAYOUT (2×2):
- Top-left: [base clean]
- Top-right: [base + variation A]
- Bottom-left: [base + variation B]
- Bottom-right: [mixed variations]

MATERIAL DETAILS:
- Surface: [material and texture description]
- Details: [secondary elements]
- Lighting: [direction and quality]
- Shadows: [style]

TRANSPARENCY:
- Transparent background (PNG)
- Solid tiles only

OUTPUT VERIFICATION:
- Must tile seamlessly when placed 4×4
- No visible seams at edges
- All colors within locked palette
```

---

## Common Sizes

| Use Case | Tile Size | Grid Output |
|----------|-----------|-------------|
| Retro games | 16×16 | 32×32 (2×2) |
| Standard | 32×32 | 64×64 (2×2) |
| HD | 64×64 | 128×128 (2×2) |
| Large format | 128×128 | 256×256 (2×2) |

---

## Validation Checklist

After generation:

- [ ] Download PNG
- [ ] Test 4×4 tiling in image editor or online tool
- [ ] Check for visible seams
- [ ] Verify all colors match palette
- [ ] Test at game scale
- [ ] Import to engine with Nearest filter
