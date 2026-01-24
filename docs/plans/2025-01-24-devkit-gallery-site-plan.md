# Devkit Gallery Site Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build an interactive gallery site for browsing 121 skills with filtering, search, and GitHub Pages deployment.

**Architecture:** Astro 5 static site with React islands for interactivity. Content collections read SKILL.md files from parent directory. URL state for shareable filtered views.

**Tech Stack:** Astro 5, React 18, Tailwind CSS, @tailwindcss/typography, GitHub Pages

**Design Doc:** `docs/plans/2025-01-24-devkit-gallery-site-design.md`

---

## Task 1: Initialize Astro Project

**Files:**
- Create: `site/` directory with Astro scaffold

**Step 1: Create Astro project**

Run from devkit root:
```bash
npm create astro@latest site -- --template minimal --install --no-git --typescript strict
```

Expected: Astro project scaffolded in `site/`

**Step 2: Install dependencies**

```bash
cd site && npm install @astrojs/react @astrojs/tailwind react react-dom tailwindcss @tailwindcss/typography
```

Expected: Dependencies added to package.json

**Step 3: Verify project structure**

```bash
ls -la site/src/
```

Expected: `pages/`, `layouts/` (or similar) directories exist

**Step 4: Commit**

```bash
git add site/
git commit -m "chore: initialize Astro project for gallery site"
```

---

## Task 2: Configure Astro

**Files:**
- Modify: `site/astro.config.mjs`

**Step 1: Update Astro config**

Replace contents of `site/astro.config.mjs`:

```javascript
import { defineConfig } from 'astro/config';
import react from '@astrojs/react';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  site: 'https://bshap.github.io',
  base: '/devkit',
  integrations: [
    react(),
    tailwind({
      applyBaseStyles: false,
    }),
  ],
  markdown: {
    shikiConfig: {
      themes: {
        light: 'github-light',
        dark: 'github-dark',
      },
      wrap: true,
    },
  },
  trailingSlash: 'ignore',
});
```

**Step 2: Verify config is valid**

```bash
cd site && npm run build
```

Expected: Build succeeds (may have warnings about empty pages)

**Step 3: Commit**

```bash
git add site/astro.config.mjs
git commit -m "chore: configure Astro with React, Tailwind, and GitHub Pages"
```

---

## Task 3: Configure Tailwind

**Files:**
- Create: `site/tailwind.config.mjs`
- Create: `site/src/styles/global.css`

**Step 1: Create Tailwind config**

Create `site/tailwind.config.mjs`:

```javascript
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  darkMode: 'class',
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            maxWidth: '65ch',
          },
        },
        invert: {
          css: {
            '--tw-prose-body': 'var(--tw-prose-invert-body)',
            '--tw-prose-headings': 'var(--tw-prose-invert-headings)',
            '--tw-prose-links': 'var(--tw-prose-invert-links)',
            '--tw-prose-code': 'var(--tw-prose-invert-code)',
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
};
```

**Step 2: Create global styles**

Create directory and file `site/src/styles/global.css`:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  html {
    @apply bg-zinc-950 text-white antialiased;
  }
}

/* Screen reader only utility */
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.sr-only:focus {
  position: absolute;
  width: auto;
  height: auto;
  padding: 0.5rem 1rem;
  margin: 0;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
```

**Step 3: Commit**

```bash
git add site/tailwind.config.mjs site/src/styles/
git commit -m "chore: configure Tailwind with typography plugin and dark theme"
```

---

## Task 4: Create Content Collection

**Files:**
- Create: `site/src/content.config.ts`

**Step 1: Create content collection config**

Create `site/src/content.config.ts`:

```typescript
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const skills = defineCollection({
  loader: glob({
    pattern: '**/SKILL.md',
    base: '../skills',
  }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    license: z.string().optional(),
  }).transform((data, ctx) => {
    // ctx.id = "marketing/copywriting/SKILL.md"
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

**Step 2: Verify content collection loads**

```bash
cd site && npm run build 2>&1 | head -20
```

Expected: Build starts processing skills (may fail on missing pages, that's OK)

**Step 3: Commit**

```bash
git add site/src/content.config.ts
git commit -m "feat: add content collection for skills from parent directory"
```

---

## Task 5: Create TypeScript Types

**Files:**
- Create: `site/src/types/index.ts`

**Step 1: Create types file**

Create directory and file `site/src/types/index.ts`:

```typescript
export interface Skill {
  name: string;
  description: string;
  group: string;
  slug: string;
  excerpt: string;
  license?: string;
}

export interface FilterState {
  search: string;
  groups: string[];
}
```

**Step 2: Commit**

```bash
git add site/src/types/
git commit -m "feat: add TypeScript types for skills and filters"
```

---

## Task 6: Create Custom Hooks

**Files:**
- Create: `site/src/hooks/useDebouncedValue.ts`
- Create: `site/src/hooks/useUrlFilters.ts`

**Step 1: Create debounce hook**

Create directory and file `site/src/hooks/useDebouncedValue.ts`:

```typescript
import { useState, useEffect } from 'react';

export function useDebouncedValue<T>(value: T, delay: number = 300): T {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
}
```

**Step 2: Create URL filters hook**

Create `site/src/hooks/useUrlFilters.ts`:

```typescript
import { useState, useEffect, useCallback } from 'react';
import type { FilterState } from '../types';

export function useUrlFilters() {
  const [filters, setFiltersState] = useState<FilterState>(() => {
    if (typeof window === 'undefined') {
      return { search: '', groups: [] };
    }

    const params = new URLSearchParams(window.location.search);
    return {
      search: params.get('q') || '',
      groups: params.get('groups')?.split(',').filter(Boolean) || [],
    };
  });

  // Sync to URL
  useEffect(() => {
    const params = new URLSearchParams();
    if (filters.search) params.set('q', filters.search);
    if (filters.groups.length) params.set('groups', filters.groups.join(','));

    const url = params.toString()
      ? `${window.location.pathname}?${params}`
      : window.location.pathname;

    window.history.replaceState({}, '', url);
  }, [filters]);

  // Handle back/forward
  useEffect(() => {
    const onPopState = () => {
      const params = new URLSearchParams(window.location.search);
      setFiltersState({
        search: params.get('q') || '',
        groups: params.get('groups')?.split(',').filter(Boolean) || [],
      });
    };
    window.addEventListener('popstate', onPopState);
    return () => window.removeEventListener('popstate', onPopState);
  }, []);

  const setFilters = useCallback((updates: Partial<FilterState>) => {
    setFiltersState(prev => ({ ...prev, ...updates }));
  }, []);

  return { filters, setFilters };
}
```

**Step 3: Commit**

```bash
git add site/src/hooks/
git commit -m "feat: add custom hooks for debounce and URL filter state"
```

---

## Task 7: Create Base Layout

**Files:**
- Create: `site/src/layouts/Layout.astro`

**Step 1: Create Layout component**

Create directory and file `site/src/layouts/Layout.astro`:

```astro
---
import '../styles/global.css';

interface Props {
  title: string;
  description?: string;
}

const { title, description = 'Skills library for agentic CLI tools' } = Astro.props;
const canonicalURL = new URL(Astro.url.pathname, Astro.site);
---

<!DOCTYPE html>
<html lang="en" class="dark">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content={description} />
  <link rel="canonical" href={canonicalURL} />

  <meta property="og:type" content="website" />
  <meta property="og:url" content={canonicalURL} />
  <meta property="og:title" content={title} />
  <meta property="og:description" content={description} />

  <slot name="head" />
</head>
<body class="min-h-screen bg-zinc-950 text-white">
  <slot />
</body>
</html>
```

**Step 2: Commit**

```bash
git add site/src/layouts/
git commit -m "feat: add base Layout component with SEO meta tags"
```

---

## Task 8: Create SearchInput Component

**Files:**
- Create: `site/src/components/SearchInput.tsx`

**Step 1: Create SearchInput**

Create directory and file `site/src/components/SearchInput.tsx`:

```tsx
interface Props {
  value: string;
  onChange: (value: string) => void;
}

export function SearchInput({ value, onChange }: Props) {
  return (
    <div className="mb-6">
      <label htmlFor="skill-search" className="sr-only">
        Search skills by name or description
      </label>
      <input
        type="search"
        id="skill-search"
        placeholder="Search skills..."
        value={value}
        onChange={(e) => onChange(e.target.value)}
        className="w-full px-4 py-3 bg-zinc-900 border border-zinc-800 rounded-lg
                   text-white placeholder-zinc-500
                   focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-transparent
                   transition-colors"
        aria-label="Search skills by name or description"
      />
    </div>
  );
}
```

**Step 2: Commit**

```bash
git add site/src/components/SearchInput.tsx
git commit -m "feat: add SearchInput component with accessibility"
```

---

## Task 9: Create FilterSidebar Component

**Files:**
- Create: `site/src/components/FilterSidebar.tsx`

**Step 1: Create FilterSidebar**

Create `site/src/components/FilterSidebar.tsx`:

```tsx
interface Props {
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function FilterSidebar({ groups, selected, onToggle, onClear }: Props) {
  return (
    <aside className="w-56 shrink-0">
      <fieldset className="border-0 p-0 m-0">
        <legend className="text-sm font-semibold text-zinc-300 uppercase tracking-wide mb-3">
          Groups
        </legend>

        <button
          onClick={onClear}
          className="text-sm text-zinc-500 hover:text-zinc-300 mb-4 transition-colors"
          type="button"
        >
          Clear filters
        </button>

        <div className="space-y-2" role="group" aria-label="Filter by group">
          {groups.map(([group, count]) => {
            const id = `filter-${group.replace(/\s+/g, '-').toLowerCase()}`;
            const isChecked = selected.includes(group);

            return (
              <label
                key={group}
                htmlFor={id}
                className="flex items-center gap-2 cursor-pointer text-sm group/item"
              >
                <input
                  type="checkbox"
                  id={id}
                  checked={isChecked}
                  onChange={() => onToggle(group)}
                  className="w-4 h-4 rounded border-zinc-600 bg-zinc-800
                           text-emerald-500 focus:ring-emerald-500 focus:ring-offset-zinc-900
                           cursor-pointer"
                />
                <span className={`transition-colors ${isChecked ? 'text-white' : 'text-zinc-400 group-hover/item:text-zinc-300'}`}>
                  {group}
                </span>
                <span className="text-zinc-600 ml-auto">{count}</span>
              </label>
            );
          })}
        </div>
      </fieldset>
    </aside>
  );
}
```

**Step 2: Commit**

```bash
git add site/src/components/FilterSidebar.tsx
git commit -m "feat: add FilterSidebar component with accessible checkboxes"
```

---

## Task 10: Create SkillCard Component

**Files:**
- Create: `site/src/components/SkillCard.tsx`

**Step 1: Create SkillCard**

Create `site/src/components/SkillCard.tsx`:

```tsx
import type { Skill } from '../types';

interface Props {
  skill: Skill;
  baseUrl: string;
}

export function SkillCard({ skill, baseUrl }: Props) {
  return (
    <a
      href={`${baseUrl}/skills/${skill.slug}`}
      className="block rounded-lg border border-zinc-800 bg-zinc-900 p-4
                 hover:border-zinc-600 hover:bg-zinc-800/50
                 transition-all duration-200
                 focus:outline-none focus:ring-2 focus:ring-emerald-500"
      role="listitem"
    >
      <span className="text-xs text-emerald-400 uppercase tracking-wide font-medium">
        {skill.group}
      </span>
      <h3 className="text-white font-medium mt-1 text-lg">
        {skill.name}
      </h3>
      <p className="text-zinc-400 text-sm mt-2 line-clamp-2">
        {skill.excerpt}
      </p>
    </a>
  );
}
```

**Step 2: Commit**

```bash
git add site/src/components/SkillCard.tsx
git commit -m "feat: add SkillCard component with hover states"
```

---

## Task 11: Create ErrorBoundary Component

**Files:**
- Create: `site/src/components/ErrorBoundary.tsx`

**Step 1: Create ErrorBoundary**

Create `site/src/components/ErrorBoundary.tsx`:

```tsx
import { Component, type ReactNode, type ErrorInfo } from 'react';

interface Props {
  children: ReactNode;
  fallback?: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('SkillGallery error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || (
        <div className="p-6 border border-red-800 rounded-lg bg-red-900/20 text-center">
          <h2 className="text-lg font-semibold text-red-200">
            Something went wrong loading the gallery
          </h2>
          <p className="text-sm text-red-300 mt-2">
            Please refresh the page to try again.
          </p>
        </div>
      );
    }

    return this.props.children;
  }
}
```

**Step 2: Commit**

```bash
git add site/src/components/ErrorBoundary.tsx
git commit -m "feat: add ErrorBoundary for graceful failure handling"
```

---

## Task 12: Create SkillGallery Component

**Files:**
- Create: `site/src/components/SkillGallery.tsx`

**Step 1: Create SkillGallery**

Create `site/src/components/SkillGallery.tsx`:

```tsx
import { useState, useMemo, useEffect } from 'react';
import type { Skill } from '../types';
import { useUrlFilters } from '../hooks/useUrlFilters';
import { useDebouncedValue } from '../hooks/useDebouncedValue';
import { SearchInput } from './SearchInput';
import { FilterSidebar } from './FilterSidebar';
import { SkillCard } from './SkillCard';
import { ErrorBoundary } from './ErrorBoundary';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

function SkillGalleryInner({ skills, baseUrl }: Props) {
  const { filters, setFilters } = useUrlFilters();
  const [searchInput, setSearchInput] = useState(filters.search);
  const debouncedSearch = useDebouncedValue(searchInput, 300);

  // Sync debounced search to URL
  useEffect(() => {
    setFilters({ search: debouncedSearch });
  }, [debouncedSearch, setFilters]);

  // Extract groups with counts
  const groups = useMemo(() => {
    const counts = new Map<string, number>();
    skills.forEach(s => counts.set(s.group, (counts.get(s.group) || 0) + 1));
    return Array.from(counts.entries()).sort((a, b) => a[0].localeCompare(b[0]));
  }, [skills]);

  // Filter skills
  const filteredSkills = useMemo(() => {
    return skills.filter(skill => {
      const searchLower = filters.search.toLowerCase();
      const matchesSearch = !filters.search ||
        skill.name.toLowerCase().includes(searchLower) ||
        skill.description.toLowerCase().includes(searchLower);

      const matchesGroup = filters.groups.length === 0 ||
        filters.groups.includes(skill.group);

      return matchesSearch && matchesGroup;
    });
  }, [skills, filters]);

  const toggleGroup = (group: string) => {
    setFilters({
      groups: filters.groups.includes(group)
        ? filters.groups.filter(g => g !== group)
        : [...filters.groups, group],
    });
  };

  const clearFilters = () => {
    setSearchInput('');
    setFilters({ groups: [], search: '' });
  };

  return (
    <div className="flex gap-8">
      <FilterSidebar
        groups={groups}
        selected={filters.groups}
        onToggle={toggleGroup}
        onClear={clearFilters}
      />

      <div className="flex-1">
        <SearchInput value={searchInput} onChange={setSearchInput} />

        {/* Screen reader announcement */}
        <div role="status" aria-live="polite" aria-atomic="true" className="sr-only">
          {filteredSkills.length} skill{filteredSkills.length !== 1 ? 's' : ''} found
        </div>

        {filteredSkills.length === 0 ? (
          <p className="text-zinc-400 text-center py-12">
            No skills match your filters.
          </p>
        ) : (
          <div
            role="list"
            aria-label="Skills"
            className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 gap-4"
          >
            {filteredSkills.map(skill => (
              <SkillCard key={skill.slug} skill={skill} baseUrl={baseUrl} />
            ))}
          </div>
        )}
      </div>
    </div>
  );
}

export function SkillGallery(props: Props) {
  return (
    <ErrorBoundary>
      <SkillGalleryInner {...props} />
    </ErrorBoundary>
  );
}
```

**Step 2: Commit**

```bash
git add site/src/components/SkillGallery.tsx
git commit -m "feat: add SkillGallery component with filtering and search"
```

---

## Task 13: Create Gallery Page (Homepage)

**Files:**
- Create: `site/src/pages/index.astro`

**Step 1: Create homepage**

Create `site/src/pages/index.astro`:

```astro
---
import { getCollection } from 'astro:content';
import Layout from '../layouts/Layout.astro';
import { SkillGallery } from '../components/SkillGallery';

const skills = await getCollection('skills');
const skillData = skills.map(s => ({
  name: s.data.name,
  description: s.data.description,
  group: s.data.group,
  slug: s.data.slug,
  excerpt: s.data.excerpt,
}));

// Sort alphabetically by name
skillData.sort((a, b) => a.name.localeCompare(b.name));

const baseUrl = import.meta.env.BASE_URL.replace(/\/$/, '');
---

<Layout title="Devkit | Skills Gallery">
  <a
    href="#main-content"
    class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4
           focus:z-50 focus:px-4 focus:py-2 focus:bg-white focus:text-zinc-900
           focus:rounded focus:outline-none"
  >
    Skip to main content
  </a>

  <header class="border-b border-zinc-800 px-8 py-6">
    <h1 class="text-2xl font-bold">Devkit</h1>
    <p class="text-zinc-400 mt-1">{skillData.length} skills for agentic CLI tools</p>
  </header>

  <main id="main-content" class="px-8 py-8">
    <SkillGallery skills={skillData} baseUrl={baseUrl} client:visible />
  </main>
</Layout>
```

**Step 2: Test local build**

```bash
cd site && npm run build
```

Expected: Build succeeds

**Step 3: Commit**

```bash
git add site/src/pages/index.astro
git commit -m "feat: add gallery homepage with skill listing"
```

---

## Task 14: Create Skill Detail Page

**Files:**
- Create: `site/src/pages/skills/[slug].astro`

**Step 1: Create skill detail page**

Create directory and file `site/src/pages/skills/[slug].astro`:

```astro
---
import { getCollection, render } from 'astro:content';
import Layout from '../../layouts/Layout.astro';

export const prerender = true;

export async function getStaticPaths() {
  const skills = await getCollection('skills');
  return skills.map(skill => ({
    params: { slug: skill.data.slug },
    props: { skill },
  }));
}

const { skill } = Astro.props;
const { Content, headings } = await render(skill);

const tocHeadings = headings.filter(h => h.depth >= 2 && h.depth <= 3);
const baseUrl = import.meta.env.BASE_URL.replace(/\/$/, '');
const canonicalURL = new URL(Astro.url.pathname, Astro.site);
---

<Layout
  title={`${skill.data.name} | Devkit`}
  description={skill.data.description}
>
  <head slot="head">
    <meta property="og:type" content="article" />
    <script type="application/ld+json" set:html={JSON.stringify({
      "@context": "https://schema.org",
      "@type": "TechArticle",
      "headline": skill.data.name,
      "description": skill.data.description,
      "url": canonicalURL.href,
    })} />
  </head>

  <a
    href="#main-content"
    class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4
           focus:z-50 focus:px-4 focus:py-2 focus:bg-white focus:text-zinc-900
           focus:rounded focus:outline-none"
  >
    Skip to main content
  </a>

  <main id="main-content" class="min-h-screen">
    <div class="max-w-3xl mx-auto px-6 py-12">

      <nav class="mb-8">
        <a
          href={baseUrl || '/'}
          class="inline-flex items-center text-zinc-400 hover:text-white transition-colors"
        >
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7" />
          </svg>
          Back to Gallery
        </a>
      </nav>

      <header class="bg-zinc-900 border border-zinc-800 rounded-lg p-6 mb-8">
        <span class="text-xs text-emerald-400 uppercase tracking-wide font-medium">
          {skill.data.group}
        </span>
        <h1 id="article-title" class="text-3xl font-bold mt-2">
          {skill.data.name}
        </h1>
        <p class="text-zinc-400 mt-3 text-lg">
          {skill.data.description}
        </p>
      </header>

      {tocHeadings.length >= 3 && (
        <nav aria-label="Table of contents" class="mb-8 p-4 bg-zinc-900/50 rounded-lg border border-zinc-800">
          <h2 class="text-sm font-semibold text-zinc-300 uppercase tracking-wide mb-3">
            On this page
          </h2>
          <ul class="space-y-2">
            {tocHeadings.map(({ depth, slug, text }) => (
              <li style={`padding-left: ${(depth - 2) * 1}rem`}>
                <a
                  href={`#${slug}`}
                  class="text-sm text-zinc-400 hover:text-white transition-colors"
                >
                  {text}
                </a>
              </li>
            ))}
          </ul>
        </nav>
      )}

      <article
        class="prose prose-zinc prose-invert max-w-none
               prose-headings:text-white
               prose-a:text-emerald-400 prose-a:no-underline hover:prose-a:underline
               prose-code:text-emerald-300 prose-code:bg-zinc-800 prose-code:px-1 prose-code:rounded
               prose-pre:bg-zinc-900 prose-pre:border prose-pre:border-zinc-800"
        aria-labelledby="article-title"
      >
        <Content />
      </article>

    </div>
  </main>
</Layout>
```

**Step 2: Test build**

```bash
cd site && npm run build
```

Expected: Build succeeds with all skill pages generated

**Step 3: Commit**

```bash
git add site/src/pages/skills/
git commit -m "feat: add skill detail page with TOC and syntax highlighting"
```

---

## Task 15: Create GitHub Actions Workflow

**Files:**
- Create: `.github/workflows/deploy-site.yml`

**Step 1: Create workflow file**

Create `.github/workflows/deploy-site.yml`:

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
      - name: Checkout
        uses: actions/checkout@v5

      - name: Build Astro site
        uses: withastro/action@v5
        with:
          path: ./site

  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**Step 2: Commit**

```bash
git add .github/workflows/deploy-site.yml
git commit -m "ci: add GitHub Actions workflow for auto-deploy to Pages"
```

---

## Task 16: Test Full Local Build

**Files:**
- None (verification only)

**Step 1: Run full build**

```bash
cd site && npm run build
```

Expected: Build succeeds, shows number of pages generated

**Step 2: Preview locally**

```bash
cd site && npm run preview
```

Expected: Site loads at http://localhost:4321/devkit/

**Step 3: Verify functionality**

- [ ] Gallery loads with all skills
- [ ] Search filters skills
- [ ] Group checkboxes filter skills
- [ ] Skill cards link to detail pages
- [ ] Detail pages render markdown
- [ ] Back link returns to gallery

**Step 4: Stop preview**

Press Ctrl+C

---

## Task 17: Push and Deploy

**Files:**
- None (deployment)

**Step 1: Push to GitHub**

```bash
git push origin main
```

Expected: Push succeeds

**Step 2: Enable GitHub Pages**

1. Go to repository Settings → Pages
2. Set Source to "GitHub Actions"
3. Save

**Step 3: Monitor deployment**

1. Go to repository Actions tab
2. Watch "Deploy to GitHub Pages" workflow
3. Wait for completion (~2 minutes)

Expected: Workflow succeeds with green checkmark

**Step 4: Verify live site**

Visit: `https://bshap.github.io/devkit/`

Expected: Gallery loads with all 121 skills

**Step 5: Final commit (if any fixes needed)**

```bash
git add -A && git commit -m "fix: deployment adjustments" && git push
```

---

## Verification Checklist

- [ ] Homepage loads at `/devkit/`
- [ ] All 121 skills display in gallery
- [ ] Search filters by name and description
- [ ] Group filters work (multi-select)
- [ ] URL updates with filter state
- [ ] Filtered URLs are shareable
- [ ] Skill detail pages load
- [ ] Markdown renders correctly
- [ ] Code blocks have syntax highlighting
- [ ] TOC appears on longer skills
- [ ] Back link works
- [ ] Skip link visible on focus
- [ ] Mobile responsive
