# Portrait Prompt Template

Copy-paste ready prompts for dialogue portraits and character portraits.

---

## Midjourney v7 Template

```
/imagine character portrait, [COLOR_GRADE] color grading, [CONTEXT] context:

PORTRAIT SPECIFICATIONS:
- Size: [SIZE] pixels (game UI standard)
- Framing: 3/4 facing camera
- Expression: [MOOD]
- Character: [NAME]

CHARACTER DETAILS:
[Face description, distinguishing features]
[Hair and clothing visible in frame]
[Personality conveyed through expression]

COLOR GRADING:
[Warm: amber highlights, soft shadows, saturated colors]
[Cool: gray-green shadows, desaturated, blue-tinted]

LIGHTING:
- Key light: Top-left, [warm/cool] tinted
- Fill: [soft warm / gray shadows]
- Overall mood: [safe/intimate OR ancient/mysterious]

STYLE:
Painterly illustration (concept art quality)
Soft edges, atmospheric depth
[HD pixel art / detailed illustration]

TECHNICAL:
- Transparent background
- Character portrait only
- v7 face quality (exceptional coherence)

--ar 1:1 --q 2 --s [100-250] --v 7
```

---

## NBP Template

```
Generate character portrait for dialogue UI.

PORTRAIT SPECIFICATIONS:
- Size: [WIDTH]×[HEIGHT] pixels
- Framing: 3/4 facing camera
- Expression: [mood/emotion]

CHARACTER:
[Detailed description of face, hair, visible clothing]

COLOR GRADING ([CONTEXT]):
[For warm: "Warm amber highlights, soft shadows, rich saturated colors"]
[For cool: "Cool gray-green shadows, desaturated, blue-tinted highlights"]

LIGHTING:
- Key light: Top-left
- Color temperature: [warm white / cool white]
- Shadow bias: [warm / blue]

MOOD:
[Safe and welcoming / Ancient and mysterious / etc.]

TECHNICAL:
- Transparent background (PNG)
- [SIZE] dimensions
- Character portrait only
- Clean edges
```

---

## Context Variants (Using --oref)

Generate warm version first, then cool variant:

```
/imagine --oref [WARM_PORTRAIT_URL] --ow 200
Same character portrait, cool color grading:

COLOR GRADING (COOL):
- Cool gray-green shadows
- Desaturated, muted colors
- Blue-tinted highlights
- No warm undertones

CONSISTENCY (locked by --oref at 200):
- Facial features: IDENTICAL
- Clothing: IDENTICAL (color-graded only)
- Proportions: IDENTICAL
- Expression: IDENTICAL
Only color temperature changes

--oref [URL] --ow 200 --ar 1:1 --q 2 --v 7
```

---

## Expression Variants

For dialogue systems needing multiple expressions:

```
/imagine --oref [BASE_PORTRAIT_URL] --ow 180
[CHARACTER] portrait with [EXPRESSION]:

EXPRESSION:
[Happy: warm smile, soft eyes]
[Concerned: furrowed brow, slight frown]
[Angry: intense eyes, tight jaw]
[Sad: downcast eyes, subtle melancholy]
[Surprised: wide eyes, raised brows]

CONSISTENCY:
Same face, lighting, framing
Only expression changes

--oref [URL] --ow 180 --ar 1:1 --q 2 --v 7
```

---

## Common Sizes

| Use Case | Size | Notes |
|----------|------|-------|
| Small UI | 64×64 | Minimal detail |
| Standard dialogue | 128×128 | Good detail |
| Large dialogue | 256×256 | High detail |
| Full illustration | 512×512+ | Concept art quality |

---

## Stylize Settings for Portraits

| Goal | --s Value |
|------|-----------|
| Pixel art portrait | 50-100 |
| Painterly/illustrated | 100-250 |
| Photorealistic | 250-500 |

Portraits benefit from higher --s than sprites since v7 face rendering is exceptional.

---

## Checklist

- [ ] Expression matches character personality
- [ ] Readable at target UI size
- [ ] Color grading matches context (warm/cool)
- [ ] Consistent with other character portraits
- [ ] Transparent background, clean edges
- [ ] If variants: facial features identical across all
