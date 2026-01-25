# Cadre AI Brand Rebrand Plan

> **For Claude:** Use superpowers:subagent-driven-development to execute this plan.

**Goal:** Rebrand the devkit site from dark theme with emerald accents to Cadre AI's light theme with coral red accents

**Architecture:** Update CSS theme variables first, then systematically update each component to use the new brand palette

**Tech Stack:** Astro 5, React 18, Tailwind CSS v4

---

## Brand Color Reference

From `skills/internal-specialty/cadre-os/references/brand.md`:

| Token | Hex | Usage |
|-------|-----|-------|
| `--color-warm-black` | `#0C0407` | Primary text, headlines |
| `--color-coral` | `#DB4545` | Primary accent, CTAs |
| `--color-blue` | `#08749B` | Links, secondary accent |
| `--color-body` | `#6E7191` | Body text |
| `--color-muted` | `#A1A1A1` | Muted text, captions |
| `--color-warm-white` | `#FAF9F6` | Primary background |
| `--color-cream` | `#F2EFE4` | Hero sections, features |
| `--color-white` | `#FFFFFF` | Cards, surfaces |
| `--color-dark` | `#242424` | Footer, dark sections |
| `--color-border` | `#E5E2D8` | Standard borders |
| `--color-border-subtle` | `rgba(0,0,0,0.10)` | Subtle borders |

---

## Color Mapping

| Current | New |
|---------|-----|
| `zinc-950`, `zinc-900` (backgrounds) | `warm-white`, `cream`, `white` |
| `zinc-800` (borders) | `border` (#E5E2D8) |
| `zinc-100`, `white` (text) | `warm-black` (#0C0407) |
| `zinc-400`, `zinc-500` (body text) | `body` (#6E7191), `muted` (#A1A1A1) |
| `emerald-*` (accent) | `coral` (#DB4545) |
| `amber-*` (favorites) | Keep amber for favorites (⭐ is yellow) |
| `violet-*` (commands) | `coral` (unified brand) |
| `cyan-*` (agents) | `blue` (#08749B) |

---

## Task 1: Update Global CSS Theme

**Files:**
- Modify: `site/src/styles/global.css`

**Changes:**
1. Replace theme variables with brand colors
2. Change hero gradient from dark to light (cream → white)
3. Change glow from emerald to coral
4. Update base body styles for light theme
5. Update text colors for light backgrounds
6. Update utility classes (ruled-line, section-heading)

**Implementation:**
```css
@theme {
  --font-display: 'Plus Jakarta Sans', ui-sans-serif, system-ui, sans-serif;
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;

  /* Brand colors */
  --color-warm-black: #0C0407;
  --color-coral: #DB4545;
  --color-blue: #08749B;
  --color-body: #6E7191;
  --color-muted: #A1A1A1;
  --color-warm-white: #FAF9F6;
  --color-cream: #F2EFE4;
  --color-dark: #242424;
  --color-border: #E5E2D8;

  --gradient-hero: linear-gradient(180deg, #F2EFE4 0%, #FFFFFF 100%);
  --gradient-glow: radial-gradient(ellipse at 50% 0%, rgba(219, 69, 69, 0.08) 0%, transparent 50%);
}
```

---

## Task 2: Update Layout Base Styles

**Files:**
- Modify: `site/src/layouts/Layout.astro`

**Changes:**
1. Remove `dark` class from root
2. Change body background from `bg-zinc-950` to `bg-[#FAF9F6]`
3. Change text from `text-white` to `text-[#0C0407]`

---

## Task 3: Update Hero Component

**Files:**
- Modify: `site/src/components/Hero.tsx`

**Changes:**
1. Badge: emerald → coral palette
2. Title gradient: adjust for light background
3. Subtitle: zinc-500 → body color
4. Gradient orb: emerald → coral
5. Keyboard hint: zinc-800 → light surface with border

---

## Task 4: Update SkillCard Component

**Files:**
- Modify: `site/src/components/SkillCard.tsx`

**Changes:**
1. Card background: zinc-900 → white with subtle shadow
2. Card border: zinc-800 → border color
3. Hover shadow: emerald → coral tint
4. Icon color: emerald → coral
5. Title: zinc-100 → warm-black
6. Description: zinc-400 → body color
7. Role badges: zinc-800 → light gray surface
8. Task badges: emerald → coral palette
9. Arrow and links: emerald → coral
10. Keep amber for favorites (star icon)

---

## Task 5: Update FeaturedSkillCard Component

**Files:**
- Modify: `site/src/components/FeaturedSkillCard.tsx`

**Changes:**
- Same treatment as SkillCard
- Featured glow: emerald → coral
- Tagline: emerald → coral

---

## Task 6: Update FilterSidebar Component

**Files:**
- Modify: `site/src/components/FilterSidebar.tsx`

**Changes:**
1. Section background: zinc-900 → white/cream
2. Section border: zinc-800 → border color
3. Headings: zinc-400 → body color
4. Active filters: emerald → coral
5. Inactive filters: adjust for light background
6. Keep amber for favorites toggle

---

## Task 7: Update MobileFilterDrawer Component

**Files:**
- Modify: `site/src/components/MobileFilterDrawer.tsx`

**Changes:**
1. Drawer background: zinc-900 → white
2. All borders: zinc-800 → border color
3. Filter buttons: emerald → coral
4. Show Results button: emerald → coral
5. Keep amber for favorites

---

## Task 8: Update SearchInput Component

**Files:**
- Modify: `site/src/components/SearchInput.tsx`

**Changes:**
1. Input background: zinc-900 → white
2. Input border: zinc-800 → border color
3. Input text: zinc-100 → warm-black
4. Placeholder: zinc-500 → muted
5. Focus ring: emerald → coral

---

## Task 9: Update DownloadButton Component

**Files:**
- Modify: `site/src/components/DownloadButton.tsx`

**Changes:**
1. Icon button: emerald → coral
2. Full button: emerald → coral palette

---

## Task 10: Update CopyInstallButton Component

**Files:**
- Modify: `site/src/components/CopyInstallButton.tsx`

**Changes:**
1. Button background: zinc-800 → light surface
2. Button border: zinc-700 → border color
3. Button text: zinc-300 → body color
4. Check icon: emerald → coral

---

## Task 11: Update CommandCard Component

**Files:**
- Modify: `site/src/components/CommandCard.tsx`

**Changes:**
1. Card: same light treatment as SkillCard
2. Icon accent: violet → coral (unified brand)
3. Arrow: violet → coral

---

## Task 12: Update AgentCard Component

**Files:**
- Modify: `site/src/components/AgentCard.tsx`

**Changes:**
1. Card: same light treatment as SkillCard
2. Icon accent: cyan → blue (secondary brand color)
3. Arrow: cyan → blue

---

## Task 13: Update HookCard Component

**Files:**
- Modify: `site/src/components/HookCard.tsx`

**Changes:**
1. Card: same light treatment as SkillCard
2. Icon accent: amber → coral
3. Arrow: amber → coral

---

## Task 14: Update SkillGallery Component

**Files:**
- Modify: `site/src/components/SkillGallery.tsx`

**Changes:**
1. Mobile filter button: zinc → light surface
2. Badge count: emerald → coral
3. Results text: white → warm-black
4. Reset link: emerald → coral
5. Separator: zinc-800 → border color

---

## Task 15: Update Compare Components

**Files:**
- Modify: `site/src/components/CompareView.tsx`
- Modify: `site/src/components/CompareSelector.tsx`

**Changes:**
1. Card backgrounds: zinc-900 → white
2. All borders: zinc-800 → border color
3. Text colors: adjust for light background
4. Links and accents: emerald → coral
5. Selected pills: emerald → coral

---

## Task 16: Update Footer Component

**Files:**
- Modify: `site/src/components/Footer.astro`

**Changes:**
1. Keep dark background (#242424 from brand)
2. Logo gradient: emerald → coral
3. Links: zinc-500 → lighter gray for contrast
4. Border: zinc-800 → subtle dark border

---

## Task 17: Update Index Page Header

**Files:**
- Modify: `site/src/pages/index.astro`

**Changes:**
1. Header background: zinc-950 → warm-white with blur
2. Header border: zinc-800 → border color
3. Logo gradient: emerald → coral
4. Nav links: zinc-400 → body color, hover → coral

---

## Task 18: Update Skill Detail Page

**Files:**
- Modify: `site/src/pages/skills/[slug].astro`

**Changes:**
1. Header gradient: zinc-900/950 → cream/white
2. Glow: emerald → coral
3. Badge: emerald → coral
4. Prose links: emerald → coral
5. Prose code: emerald → coral
6. All text colors for light background

---

## Task 19: Update Other Detail Pages

**Files:**
- Modify: `site/src/pages/hooks/[slug].astro`
- Modify: `site/src/pages/commands/[slug].astro` (if exists)
- Modify: `site/src/pages/agents/[slug].astro` (if exists)

**Changes:**
- Same light theme treatment as skill detail
- Hooks: amber → coral
- Commands: violet → coral
- Agents: cyan → blue

---

## Task 20: Update Index Pages for Hooks/Commands/Agents

**Files:**
- Modify: `site/src/pages/hooks/index.astro`
- Modify: `site/src/pages/commands/index.astro`
- Modify: `site/src/pages/agents/index.astro`

**Changes:**
- Hero glow radials: adjust for light theme with brand colors
- All other page elements for light theme

---

## Task 21: Update Remaining Components

**Files:**
- Modify: `site/src/components/FavoritesSection.tsx`
- Modify: `site/src/components/ResultsSummary.tsx` (if has colors)

**Changes:**
- Divider: zinc-800 → border color
- Any other dark theme remnants

---

## Task 22: Final Review and Build Verification

**Actions:**
1. Run `npm run build` to check for errors
2. Run `npm run preview` and visually verify all pages
3. Check for any remaining dark theme colors
4. Verify color contrast meets accessibility standards
5. Test responsive behavior on mobile

---

## Verification Checklist

1. **Build Check:**
   ```bash
   cd site && npm run build
   ```
   - [ ] No TypeScript errors
   - [ ] No build warnings about colors
   - [ ] Build succeeds

2. **Visual Check (each page):**
   - [ ] Skills index - light background, coral accents
   - [ ] Skill detail - light theme, readable prose
   - [ ] Hooks index - coral accents
   - [ ] Commands index - coral accents
   - [ ] Agents index - blue accents
   - [ ] Footer - dark section with coral logo
   - [ ] Mobile drawer - light theme

3. **Interaction Check:**
   - [ ] Hover states visible on light background
   - [ ] Focus states visible
   - [ ] Favorites star still amber (intentional)
   - [ ] Search input readable
   - [ ] Filter buttons show active state

4. **Accessibility:**
   - [ ] Text contrast ratio ≥ 4.5:1
   - [ ] Interactive elements have visible focus
   - [ ] No pure white on cream (needs contrast)
