# Enemy Sprite Prompt Template

Copy-paste ready prompts for generating enemy sprites by threat level.

---

## Midjourney v7 Template

```
/imagine A [SIZE] pixel art enemy sprite showing [NAME], [BRIEF DESCRIPTION] in [POSE].

ENEMY SPECIFICATIONS:
- Name: [NAME]
- Threat Level: [Low/Medium/High/Boss]
- Size: [WIDTH]×[HEIGHT] pixels
- Alignment: [Neutral/Faction-aligned]

VISUAL CHARACTER:
[2-3 sentences describing form, surface, movement quality, presence]

KEY VISUAL ELEMENT:
[The defining recognizable feature]

THREAT COMMUNICATION:
[How the design telegraphs danger level]

COLOR PALETTE ([ALIGNMENT]):
- Primary: #[HEX] ([description])
- Secondary: #[HEX] ([description])
- Accent: #[HEX] ([description])
- Shadow: #[HEX]

STYLE:
[HD pixel art / polished pixel art]
Clear silhouette, readable at game scale
Top-left lighting
Transparent background

--ar [RATIO] --s [0-50] --style raw --v 7
--no anti-aliasing, smooth edges, gradients, blur, 3D render
```

---

## NBP Template

```
Design a [THREAT_LEVEL] enemy sprite.

ENEMY SPECIFICATIONS:
- Name: [NAME]
- Size: [WIDTH]×[HEIGHT] pixels
- Threat Level: [Low/Medium/High/Boss]
- Alignment: [Neutral/specific faction]

VISUAL CHARACTER:
- Form: [body shape and structure]
- Surface: [texture and material]
- Movement: [implied motion quality]
- Presence: [emotional impression]

COLOR PALETTE:
- #[HEX]: [body part/element]
- #[HEX]: [body part/element]
- #[HEX]: [body part/element]

[If aligned, note: "[COLOR] as ACCENT ONLY, not full body"]

TECHNICAL:
- Transparent background (PNG)
- Clean silhouette
- Readable at game scale

OUTPUT:
- Dimensions: [WIDTH]×[HEIGHT] pixels
- Label: [enemy_name]_idle.png
```

---

## Size by Threat Level

| Threat | Size | Silhouette |
|--------|------|------------|
| Fodder/Swarm | 16×16, 32×32 | Simple, small |
| Low | 32×48 | Basic humanoid |
| Medium | 48×48, 64×64 | Complex |
| High | 64×64, 96×96 | Distinctive |
| Boss | 96×96, 128×128+ | Imposing |

---

## Color Alignment Strategy

### Neutral Enemies (Default)

```
COLOR PALETTE (Neutral):
- Use zone-appropriate colors (greens, tans, grays, browns)
- No purple or red alignment colors
- Keeps player feedback clear
```

### Faction-Aligned Enemies

```
COLOR PALETTE ([Faction]-aligned):
- Primary body: [neutral color] (gray, brown, bone)
- Faction accent: #[HEX] (as ACCENT ONLY - eyes, veins, aura)
- Keep body neutral so accent pops
- Player uses saturated colors; enemies use muted/desaturated
```

---

## Animation States

For full enemy sprite set, generate each state:

1. **Idle** - Default standing/floating
2. **Alert** - Noticed player, preparing
3. **Attack** - Wind-up or strike pose
4. **Damaged** - Recoil, pain expression
5. **Death** - Collapse or dissolve

Use --oref with moderate weight (100-150) between states for consistency.

---

## Stylize Settings by Size

| Size | --s Value | Reason |
|------|-----------|--------|
| 16×16 | 0 | Minimal style, crisp pixels |
| 32×48 | 25 | Light styling |
| 64×64 | 50 | Balanced detail |
| 96×96+ | 50-100 | Room for detail |

---

## Checklist

- [ ] Threat level readable from silhouette
- [ ] Colors communicate alignment correctly
- [ ] Readable at actual game scale
- [ ] Clear differentiation from other enemies
- [ ] Attack tells visible in design (if applicable)
- [ ] Transparent background, clean edges
