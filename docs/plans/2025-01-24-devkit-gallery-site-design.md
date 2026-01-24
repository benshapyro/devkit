# Devkit Gallery Site Design

**Date:** 2025-01-24
**Status:** Approved
**Tech Stack:** Astro 5 + React + Tailwind + GitHub Pages

## Overview

An interactive gallery site for browsing the devkit's 121 skills, with future support for hooks, commands, and agents. Hosted on GitHub Pages with auto-deployment.

**Live URL:** `https://bshap.github.io/devkit/`

## Requirements

- **Audience:** Team/collaborators
- **Primary use:** Browse & discover skills
- **Interactivity:** Filtering by group, search, sorting
- **Style:** Modern dark theme (Vercel/Linear aesthetic)

## Architecture

```
devkit/
├── site/                          # Astro project
│   ├── src/
│   │   ├── components/
│   │   │   ├── SkillGallery.tsx   # Main gallery (React island)
│   │   │   ├── SkillCard.tsx      # Individual card
│   │   │   ├── FilterSidebar.tsx  # Group checkboxes
│   │   │   ├── SearchInput.tsx    # Debounced search
│   │   │   └── ErrorBoundary.tsx  # Graceful failures
│   │   ├── hooks/
│   │   │   ├── useUrlFilters.ts   # URL state sync
│   │   │   └── useDebouncedValue.ts
│   │   ├── layouts/
│   │   │   └── Layout.astro       # Base layout
│   │   ├── pages/
│   │   │   ├── index.astro        # Gallery homepage
│   │   │   └── skills/
│   │   │       └── [slug].astro   # Skill detail
│   │   ├── content.config.ts      # Astro content collections
│   │   └── styles/
│   │       └── global.css
│   ├── astro.config.mjs
│   ├── tailwind.config.mjs
│   └── package.json
├── skills/                        # Source of truth (unchanged)
└── .github/
    └── workflows/
        └── deploy-site.yml        # Auto-deploy
```

## Data Flow

```
skills/marketing/copywriting/SKILL.md
              ↓
    glob() loader with base: "../skills"
              ↓
    Entry ID: "marketing/copywriting/SKILL.md"
              ↓
    Zod transform extracts: group="marketing", slug="copywriting"
              ↓
    SkillGallery.tsx renders cards
```

### Content Collection Config

```typescript
// site/src/content.config.ts
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const skills = defineCollection({
  loader: glob({
    pattern: "**/SKILL.md",
    base: "../skills"
  }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    license: z.string().optional(),
  }).transform((data, ctx) => {
    const parts = ctx.id.split('/');
    const group = parts[0];
    const slug = parts.length > 2 ? parts[1] : parts[0];

    return {
      ...data,
      group,
      slug,
      excerpt: data.description.length > 120
        ? data.description.slice(0, 117) + '...'
        : data.description,
    };
  }),
});

export const collections = { skills };
```

## Gallery Component

### Features
- **Filter sidebar:** Multi-select group checkboxes with counts
- **Search:** 300ms debounced, searches name + description
- **URL state:** `?groups=marketing&q=seo` - shareable filtered views
- **Sorting:** Alphabetical (default), by group

### Accessibility
- ARIA live region announces result count changes
- Fieldset/legend for filter groups
- Keyboard navigable

### Hydration
- `client:visible` - loads when scrolled into view

## Skill Detail Page

### Features
- Static generation (`export const prerender = true`)
- Auto-generated TOC for skills with 3+ headings
- Skip link for accessibility
- Full SKILL.md rendered with syntax highlighting

### SEO
- Meta description from skill description
- Open Graph tags
- JSON-LD structured data (TechArticle schema)

### Typography
- `prose-zinc prose-invert` for dark theme
- Shiki dual themes (github-light/dark)

## Deployment

### GitHub Actions Workflow

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [main]
    paths:
      - 'skills/**'
      - 'site/**'
      - '.github/workflows/deploy-site.yml'
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: pages
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v5
      - uses: withastro/action@v5
        with:
          path: ./site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - uses: actions/deploy-pages@v4
        id: deployment
```

### Astro Config

```javascript
export default defineConfig({
  site: 'https://bshap.github.io',
  base: '/devkit',
  integrations: [tailwind(), react()],
  markdown: {
    shikiConfig: {
      themes: { light: 'github-light', dark: 'github-dark' },
      wrap: true,
    },
  },
  trailingSlash: 'ignore',
});
```

## URL Structure

| Page | URL |
|------|-----|
| Gallery | `https://bshap.github.io/devkit/` |
| Skill detail | `https://bshap.github.io/devkit/skills/copywriting` |
| Filtered view | `https://bshap.github.io/devkit/?groups=marketing&q=seo` |

## Future Extensions

1. **Hooks catalog** - `/hooks` route with similar gallery
2. **Commands catalog** - `/commands` route
3. **Agents catalog** - `/agents` route
4. **Skill analytics** - Usage stats, popular skills
5. **Dark/light toggle** - Currently dark-only

## Implementation Checklist

- [ ] Initialize Astro project in `/site`
- [ ] Configure content collections
- [ ] Build Layout component
- [ ] Build SkillCard component
- [ ] Build FilterSidebar component
- [ ] Build SearchInput with debounce
- [ ] Build SkillGallery (main React island)
- [ ] Build skill detail page
- [ ] Configure Tailwind with typography
- [ ] Set up GitHub Actions workflow
- [ ] Enable GitHub Pages
- [ ] Test deployment
- [ ] Verify all 121 skills render
