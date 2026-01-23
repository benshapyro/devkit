# Character Sheet Prompt Template

Copy-paste ready prompts for generating multi-pose character sheets.

---

## Midjourney v7 Template (Base Character)

```
/imagine [SIZE] pixel art character sprite of [NAME], [BRIEF DESCRIPTION] in [POSE].

CHARACTER:
[2-3 sentences describing the subject - appearance, role, personality]

CLOTHING/SURFACE:
[What they wear, armor, skin texture, defining visual elements]

KEY VISUAL ELEMENT:
[The one recognizable feature that defines this character]

MOOD:
[Emotional quality - confident, weary, mysterious, welcoming]

COLOR PALETTE:
- Primary: #[HEX] ([description])
- Secondary: #[HEX] ([description])
- Accent: #[HEX] ([description])
- Skin: #[HEX]
- Shadow: #[HEX]

STYLE:
[HD pixel art / polished pixel art]
Transparent background
Top-left lighting
3/4 view facing camera

--ar 2:3 --s 25 --style raw --v 7
--no anti-aliasing, smooth edges, gradients, blur, 3D render
```

---

## Pose Variants (Using --oref)

After generating and saving base character:

```
/imagine --oref [BASE_CHARACTER_URL] --ow 150
[CHARACTER NAME] in three action poses:

POSE 1 - Idle:
Standing naturally, weight on one leg, relaxed arms

POSE 2 - Dialogue:
Facing camera, engaging expression, hands gesturing

POSE 3 - Action:
[Attack / casting / working / etc.], active pose, clear action

CONSISTENCY:
Same character (locked by --oref at 150)
Same clothing, proportions, face
Different poses and expressions only

STYLE:
[SIZE] pixels per character
Same lighting as reference
Transparent background

--oref [URL] --ow 150 --ar 1:1 --q 2 --v 7
```

---

## NBP Template

```
Create a pixel art character sprite.

CHARACTER SPECIFICATIONS:
- Name: [NAME]
- Size: [WIDTH]×[HEIGHT] pixels
- Pose: [neutral standing / action / dialogue]
- View: 3/4 facing camera

VISUAL IDENTITY:
[Detailed description of appearance, role, personality]

EXPRESSION:
[Mood and facial expression]

CLOTHING:
[Outfit description with materials]

COLOR PALETTE:
- #[HEX]: [body part/element]
- #[HEX]: [body part/element]
- #[HEX]: [body part/element]

LIGHTING:
- Key light: Top-left
- Shadows: [soft/hard]

TECHNICAL:
- Transparent background (PNG)
- Pixel-perfect silhouette
- Readable at game scale
```

---

## Common Sizes

| Style | Size | Aspect Ratio |
|-------|------|--------------|
| Retro | 16×24 | 2:3 |
| Standard | 32×48 | 2:3 |
| HD | 64×96 | 2:3 |
| Large | 128×192 | 2:3 |
| Square | 64×64 | 1:1 |

---

## --ow Weight Guide

| Weight | Effect | Use For |
|--------|--------|---------|
| 50-75 | Loose match | Different angles |
| 100-150 | Strong match | Pose variants |
| 150-200 | Very strong | Expression variants |
| 200+ | Near-exact | Color grading only |

---

## Checklist

- [ ] Base character reads clearly at game scale
- [ ] Silhouette is distinctive
- [ ] Colors match palette exactly
- [ ] Proportions consistent across poses
- [ ] Lighting direction consistent
- [ ] Transparent background, no halos
