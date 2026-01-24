# Devkit Site Redesign Implementation Plan

> **For Claude:** Use superpowers:subagent-driven-development to execute this plan task-by-task.

**Goal:** Transform the devkit skills gallery from functional-but-generic to a refined technical showcase that matches Linear/Vercel/Stripe quality.

**Architecture:** Progressive enhancement of existing Astro/React/Tailwind stack. Add custom typography via Google Fonts, enhance visual depth with textures and gradients, improve motion choreography, and refine component designs. No structural changes to data flow.

**Tech Stack:** Astro 5, React 18, Tailwind CSS v4, Google Fonts (Satoshi + JetBrains Mono)

---

## Current State

**Files in scope:**
- `site/src/styles/global.css` - Base styles, gradients, animations
- `site/src/components/Hero.tsx` - Landing hero section
- `site/src/components/SkillCard.tsx` - Individual skill cards
- `site/src/components/FilterSidebar.tsx` - Category filter
- `site/src/components/SearchInput.tsx` - Search box
- `site/src/components/SkillGallery.tsx` - Grid layout
- `site/src/pages/index.astro` - Homepage
- `site/src/pages/skills/[slug].astro` - Detail pages
- `site/src/layouts/Layout.astro` - Base layout

---

## Task 1: Add Custom Typography

**Files:**
- Modify: `site/src/layouts/Layout.astro` - Add font imports
- Modify: `site/src/styles/global.css` - Define font families

**Implementation:**

Add Google Fonts link in `site/src/layouts/Layout.astro` head section (after existing meta tags):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

Note: Using Inter here as it's available on Google Fonts. For true Satoshi, would need Fontshare. Inter is refined technical, widely used by Vercel/Linear.

Update `site/src/styles/global.css` to use the fonts:

```css
@theme {
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
  --gradient-hero: linear-gradient(135deg, #0a0a0c 0%, #0f0f14 50%, #0a0f18 100%);
  --gradient-glow: radial-gradient(ellipse at 50% -20%, rgba(16, 185, 129, 0.12) 0%, transparent 60%);
}

@layer base {
  body {
    @apply text-zinc-100 antialiased;
    font-family: var(--font-sans);
    background: var(--gradient-hero);
    background-attachment: fixed;
    min-height: 100vh;
  }

  code, pre, kbd {
    font-family: var(--font-mono);
  }
}
```

---

## Task 2: Enhance Hero Section

**Files:**
- Modify: `site/src/components/Hero.tsx`

**Implementation:**

Replace entire Hero.tsx with enhanced version:

```tsx
interface Props {
  skillCount: number;
}

export function Hero({ skillCount }: Props) {
  return (
    <section className="relative py-24 px-8 overflow-hidden">
      {/* Decorative grid pattern */}
      <div
        className="absolute inset-0 opacity-[0.02]"
        style={{
          backgroundImage: `linear-gradient(rgba(255,255,255,0.1) 1px, transparent 1px),
                           linear-gradient(90deg, rgba(255,255,255,0.1) 1px, transparent 1px)`,
          backgroundSize: '64px 64px',
        }}
      />

      {/* Gradient orb */}
      <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[600px] h-[600px] bg-emerald-500/10 rounded-full blur-[128px] pointer-events-none" />

      <div className="relative z-10 max-w-4xl mx-auto text-center">
        {/* Badge */}
        <div className="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-sm font-medium mb-8">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
          {skillCount} skills available
        </div>

        <h1 className="text-5xl md:text-7xl font-bold tracking-tight">
          <span className="bg-gradient-to-b from-white via-zinc-100 to-zinc-400 bg-clip-text text-transparent">
            Devkit Skills
          </span>
          <br />
          <span className="text-zinc-500">Gallery</span>
        </h1>

        <p className="mt-6 text-lg md:text-xl text-zinc-400 max-w-2xl mx-auto leading-relaxed">
          Portable skills for agentic CLI tools. Browse, search, and download
          production-ready capabilities for Claude Code and beyond.
        </p>

        {/* Keyboard shortcut hint */}
        <div className="mt-8 flex items-center justify-center gap-2 text-sm text-zinc-500">
          <kbd className="px-2 py-1 rounded bg-zinc-800/50 border border-zinc-700/50 font-mono text-xs">⌘</kbd>
          <kbd className="px-2 py-1 rounded bg-zinc-800/50 border border-zinc-700/50 font-mono text-xs">K</kbd>
          <span>to search</span>
        </div>
      </div>
    </section>
  );
}
```

---

## Task 3: Add Visual Texture and Depth

**Files:**
- Modify: `site/src/styles/global.css`

**Implementation:**

Add noise texture and enhanced visual layers:

```css
@theme {
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
  --gradient-hero: linear-gradient(135deg, #09090b 0%, #0c0c10 50%, #09090b 100%);
  --gradient-glow: radial-gradient(ellipse at 50% 0%, rgba(16, 185, 129, 0.08) 0%, transparent 50%);
}

@layer base {
  body {
    @apply text-zinc-100 antialiased;
    font-family: var(--font-sans);
    background: var(--gradient-hero);
    background-attachment: fixed;
    min-height: 100vh;
  }

  /* Subtle noise overlay */
  body::before {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
    opacity: 0.03;
    pointer-events: none;
    z-index: 0;
  }

  /* Emerald glow at top */
  body::after {
    content: '';
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 50vh;
    background: var(--gradient-glow);
    pointer-events: none;
    z-index: 0;
  }

  @media (prefers-reduced-motion: reduce) {
    body {
      background-attachment: scroll;
    }
  }

  code, pre, kbd {
    font-family: var(--font-mono);
  }

  h1, h2, h3, h4, h5, h6 {
    @apply tracking-tight;
    font-weight: 600;
  }

  h1 { @apply text-4xl md:text-5xl font-bold; }
  h2 { @apply text-2xl md:text-3xl; }
  h3 { @apply text-xl; }

  p {
    @apply leading-relaxed;
  }
}

@layer utilities {
  .text-balance {
    text-wrap: balance;
  }

  @keyframes fade-in-up {
    from {
      opacity: 0;
      transform: translateY(16px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes fade-in {
    from { opacity: 0; }
    to { opacity: 1; }
  }

  .animate-fade-in-up {
    animation: fade-in-up 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
  }

  .animate-fade-in {
    animation: fade-in 0.4s ease-out forwards;
  }

  @media (prefers-reduced-motion: reduce) {
    .animate-fade-in-up,
    .animate-fade-in {
      animation: none;
      opacity: 1;
      transform: none;
    }
  }
}
```

---

## Task 4: Redesign Skill Cards

**Files:**
- Modify: `site/src/components/SkillCard.tsx`

**Implementation:**

Replace SkillCard.tsx with enhanced design:

```tsx
import type { Skill } from '../types';
import { DownloadButton } from './DownloadButton';
import { hasDownload } from '../lib/downloads';

interface Props {
  skill: Skill;
  baseUrl: string;
}

// Group to icon mapping (using simple geometric shapes)
const groupIcons: Record<string, string> = {
  'ai-automation': '◈',
  'business-strategy': '◆',
  'communications': '◇',
  'content-marketing': '▣',
  'data-documents': '▤',
  'design-ui': '◐',
  'development-tools': '⬡',
  'infrastructure-ops': '⬢',
  'internal-specialty': '◎',
  'marketing': '◉',
};

export function SkillCard({ skill, baseUrl }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;
  const icon = groupIcons[skill.group] || '○';

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-gradient-to-b from-zinc-900/80 to-zinc-900/40
                 border border-zinc-800/60
                 hover:border-zinc-700/80
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-emerald-500/5"
      role="listitem"
    >
      {/* Download button overlay */}
      {hasDownload(skill.slug) && (
        <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 transition-opacity duration-200 z-10">
          <DownloadButton slug={skill.slug} baseUrl={baseUrl} variant="icon" />
        </div>
      )}

      <a
        href={skillUrl}
        className="block p-6 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:ring-inset rounded-2xl"
      >
        {/* Top accent line */}
        <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-zinc-700/50 to-transparent" />

        {/* Hover glow */}
        <div className="absolute inset-0 bg-gradient-to-b from-emerald-500/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div className="relative">
          {/* Icon and group */}
          <div className="flex items-center gap-3 mb-4">
            <span className="text-2xl text-emerald-500/70 group-hover:text-emerald-400 transition-colors">
              {icon}
            </span>
            <span className="text-xs font-medium text-zinc-500 uppercase tracking-wider">
              {skill.group}
            </span>
          </div>

          {/* Title */}
          <h3 className="text-lg font-semibold text-zinc-100 group-hover:text-white transition-colors leading-snug">
            {skill.name}
          </h3>

          {/* Description */}
          <p className="mt-3 text-sm text-zinc-400 line-clamp-2 leading-relaxed">
            {skill.excerpt}
          </p>

          {/* Bottom arrow indicator */}
          <div className="mt-4 flex items-center text-sm text-zinc-500 group-hover:text-emerald-400 transition-colors">
            <span className="opacity-0 -translate-x-2 group-hover:opacity-100 group-hover:translate-x-0 transition-all duration-200">
              View details →
            </span>
          </div>
        </div>
      </a>
    </div>
  );
}
```

---

## Task 5: Enhance Filter Sidebar

**Files:**
- Modify: `site/src/components/FilterSidebar.tsx`

**Implementation:**

Replace FilterSidebar.tsx with refined design:

```tsx
interface Props {
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function FilterSidebar({ groups, selected, onToggle, onClear }: Props) {
  return (
    <aside className="w-64 shrink-0 hidden md:block">
      <div className="sticky top-24">
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <div className="flex items-center justify-between mb-4 pb-3 border-b border-zinc-800/50">
            <h2 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider">
              Categories
            </h2>
            {selected.length > 0 && (
              <button
                type="button"
                onClick={onClear}
                className="text-xs text-zinc-500 hover:text-white transition-colors"
              >
                Clear
              </button>
            )}
          </div>

          <div className="space-y-1" role="group" aria-label="Filter by category">
            {groups.map(([group, count]) => {
              const isChecked = selected.includes(group);
              return (
                <button
                  type="button"
                  key={group}
                  onClick={() => onToggle(group)}
                  className={`w-full flex items-center justify-between px-3 py-2.5 rounded-lg text-sm transition-all duration-150
                    ${isChecked
                      ? 'bg-emerald-500/10 text-emerald-400'
                      : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
                    }`}
                  aria-pressed={isChecked}
                >
                  <span className="truncate">{group}</span>
                  <span className={`ml-2 text-xs tabular-nums ${isChecked ? 'text-emerald-500/70' : 'text-zinc-600'}`}>
                    {count}
                  </span>
                </button>
              );
            })}
          </div>
        </div>
      </div>
    </aside>
  );
}
```

---

## Task 6: Enhance Search Input

**Files:**
- Modify: `site/src/components/SearchInput.tsx`

**Implementation:**

First, read current SearchInput to understand structure, then enhance:

```tsx
interface Props {
  value: string;
  onChange: (value: string) => void;
}

export function SearchInput({ value, onChange }: Props) {
  return (
    <div className="relative mb-6">
      <div className="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
        <svg
          className="w-5 h-5 text-zinc-500"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={1.5}
            d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
          />
        </svg>
      </div>
      <input
        type="search"
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder="Search skills..."
        className="w-full pl-12 pr-4 py-3
                   bg-zinc-900/50 border border-zinc-800/60
                   rounded-xl text-zinc-100 placeholder-zinc-500
                   focus:outline-none focus:ring-2 focus:ring-emerald-500/30 focus:border-emerald-500/30
                   transition-all duration-200"
        aria-label="Search skills"
      />
      {value && (
        <button
          type="button"
          onClick={() => onChange('')}
          className="absolute inset-y-0 right-0 pr-4 flex items-center text-zinc-500 hover:text-zinc-300 transition-colors"
          aria-label="Clear search"
        >
          <svg className="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
          </svg>
        </button>
      )}
    </div>
  );
}
```

---

## Task 7: Update Header Navigation

**Files:**
- Modify: `site/src/pages/index.astro`

**Implementation:**

Update the header section in index.astro:

```astro
<header class="sticky top-0 z-40 border-b border-zinc-800/40 bg-zinc-950/90 backdrop-blur-xl">
  <nav aria-label="Site navigation" class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
    <a href={baseUrl || '/'} class="flex items-center gap-3 group">
      <div class="w-8 h-8 rounded-lg bg-gradient-to-br from-emerald-400 to-emerald-600 flex items-center justify-center text-white font-bold text-sm">
        D
      </div>
      <span class="text-lg font-semibold text-zinc-100 group-hover:text-white transition-colors">
        Devkit
      </span>
    </a>
    <div class="flex items-center gap-6">
      <a
        href="https://github.com/CadreAI/devkit"
        target="_blank"
        rel="noopener noreferrer"
        class="text-sm text-zinc-400 hover:text-white transition-colors flex items-center gap-2"
      >
        <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
          <path fill-rule="evenodd" clip-rule="evenodd" d="M12 2C6.477 2 2 6.477 2 12c0 4.42 2.865 8.17 6.839 9.49.5.092.682-.217.682-.482 0-.237-.008-.866-.013-1.7-2.782.604-3.369-1.34-3.369-1.34-.454-1.156-1.11-1.464-1.11-1.464-.908-.62.069-.608.069-.608 1.003.07 1.531 1.03 1.531 1.03.892 1.529 2.341 1.087 2.91.831.092-.646.35-1.086.636-1.336-2.22-.253-4.555-1.11-4.555-4.943 0-1.091.39-1.984 1.029-2.683-.103-.253-.446-1.27.098-2.647 0 0 .84-.269 2.75 1.025A9.578 9.578 0 0112 6.836c.85.004 1.705.114 2.504.336 1.909-1.294 2.747-1.025 2.747-1.025.546 1.377.203 2.394.1 2.647.64.699 1.028 1.592 1.028 2.683 0 3.842-2.339 4.687-4.566 4.935.359.309.678.919.678 1.852 0 1.336-.012 2.415-.012 2.743 0 .267.18.578.688.48C19.138 20.167 22 16.418 22 12c0-5.523-4.477-10-10-10z" />
        </svg>
        GitHub
      </a>
      <span class="text-sm text-zinc-600">{skillData.length} skills</span>
    </div>
  </nav>
</header>
```

---

## Task 8: Enhance Detail Page Header

**Files:**
- Modify: `site/src/pages/skills/[slug].astro`

**Implementation:**

Update the header section in the detail page (lines 70-88):

```astro
<header class="relative overflow-hidden bg-gradient-to-br from-zinc-900 to-zinc-950 border border-zinc-800/60 rounded-2xl p-8 mb-10">
  {/* Subtle pattern */}
  <div
    class="absolute inset-0 opacity-[0.015]"
    style="background-image: radial-gradient(circle at 1px 1px, white 1px, transparent 0); background-size: 24px 24px;"
  />

  {/* Glow */}
  <div class="absolute -top-24 -right-24 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

  <div class="relative">
    <div class="flex items-center gap-3 mb-4">
      <span class="inline-flex items-center px-3 py-1 rounded-full text-xs font-medium bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
        {group}
      </span>
    </div>

    <h1 id="article-title" class="text-4xl md:text-5xl font-bold tracking-tight text-white">
      {skill.data.name}
    </h1>

    <p class="text-zinc-400 mt-4 text-lg leading-relaxed max-w-2xl">
      {skill.data.description}
    </p>

    {hasDownload(slug) && (
      <div class="mt-6">
        <DownloadButton slug={slug} baseUrl={baseUrl} variant="full" />
      </div>
    )}
  </div>
</header>
```

---

## Task 9: Add Footer

**Files:**
- Create: `site/src/components/Footer.astro`
- Modify: `site/src/pages/index.astro`

**Implementation:**

Create `site/src/components/Footer.astro`:

```astro
---
const currentYear = new Date().getFullYear();
---

<footer class="border-t border-zinc-800/40 mt-16">
  <div class="max-w-7xl mx-auto px-6 py-12">
    <div class="flex flex-col md:flex-row items-center justify-between gap-4">
      <div class="flex items-center gap-3">
        <div class="w-6 h-6 rounded bg-gradient-to-br from-emerald-400 to-emerald-600 flex items-center justify-center text-white font-bold text-xs">
          D
        </div>
        <span class="text-sm text-zinc-500">
          Devkit Skills Gallery
        </span>
      </div>

      <div class="flex items-center gap-6 text-sm text-zinc-500">
        <a
          href="https://github.com/CadreAI/devkit"
          target="_blank"
          rel="noopener noreferrer"
          class="hover:text-white transition-colors"
        >
          GitHub
        </a>
        <a
          href="https://agentskills.io"
          target="_blank"
          rel="noopener noreferrer"
          class="hover:text-white transition-colors"
        >
          Agent Skills Spec
        </a>
        <span class="text-zinc-600">
          © {currentYear} Cadre
        </span>
      </div>
    </div>
  </div>
</footer>
```

Add to `site/src/pages/index.astro` after the main content:

```astro
import Footer from '../components/Footer.astro';

<!-- Add before closing Layout tag -->
<Footer />
```

---

## Verification Checklist

After completing all tasks:

1. **Build Check:**
   ```bash
   cd site && npm run build
   ```
   - [ ] No TypeScript errors
   - [ ] Build succeeds
   - [ ] 122+ pages generated

2. **Visual Check (run preview):**
   ```bash
   npm run preview
   ```
   - [ ] Custom fonts loading (Inter, JetBrains Mono)
   - [ ] Hero has badge, gradient text, keyboard hint
   - [ ] Cards have icons, refined hover states
   - [ ] Noise texture visible (subtle)
   - [ ] Filter sidebar in container
   - [ ] Search has clear button
   - [ ] Header has logo and GitHub link
   - [ ] Footer displays at bottom
   - [ ] Detail pages have enhanced header

3. **Accessibility Check:**
   - [ ] Focus states visible on all interactive elements
   - [ ] Skip link works
   - [ ] Screen reader can navigate structure

---

## Summary

| Task | Component | Est. Time |
|------|-----------|-----------|
| 1 | Typography | 15 min |
| 2 | Hero | 20 min |
| 3 | Visual texture | 15 min |
| 4 | Skill cards | 20 min |
| 5 | Filter sidebar | 15 min |
| 6 | Search input | 10 min |
| 7 | Header nav | 15 min |
| 8 | Detail header | 15 min |
| 9 | Footer | 15 min |

**Total estimated time:** ~2.5 hours
