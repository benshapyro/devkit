# Card Enhancements Implementation Plan

> **For Claude:** Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Make skill cards immediately understandable by adding output type icons, user favorites (starring), and example prompts

**Architecture:** Add two new frontmatter fields (outputType, examplePrompt), create localStorage-based favorites hook, add favorites filter toggle, update SkillCard with new visual elements

**Tech Stack:** Astro 5, React 18, TypeScript, Tailwind CSS v4, localStorage

---

## Task 1: Add Output Type Constants

**Files:**
- Modify: `site/src/lib/tags.ts`

**Implementation:**

Add output type constant with emoji mappings:

```typescript
// At end of file, add:

export const OUTPUT_TYPES = {
  document: { emoji: '📄', label: 'Document' },
  code: { emoji: '💻', label: 'Code' },
  visual: { emoji: '🎨', label: 'Visual' },
  guidance: { emoji: '💬', label: 'Guidance' },
} as const;

export type OutputType = keyof typeof OUTPUT_TYPES;
```

**Commit:**
```bash
git add site/src/lib/tags.ts
git commit -m "feat(site): add output type constants"
```

---

## Task 2: Update Skills Schema

**Files:**
- Modify: `site/src/content.config.ts`

**Implementation:**

Add `outputType` and `examplePrompt` to the skills schema:

```typescript
// In the schema: z.object({ ... }) around line 16-24, add after favorite:
schema: z.object({
  name: z.string(),
  description: z.string(),
  license: z.string().optional(),
  tagline: z.string().optional(),
  roles: z.array(z.string()).optional(),
  tasks: z.array(z.string()).optional(),
  favorite: z.boolean().optional(),
  outputType: z.enum(['document', 'code', 'visual', 'guidance']).optional(),
  examplePrompt: z.string().optional(),
}),
```

**Commit:**
```bash
git add site/src/content.config.ts
git commit -m "feat(site): add outputType and examplePrompt to skills schema"
```

---

## Task 3: Update Skill Type Interface

**Files:**
- Modify: `site/src/types/index.ts`

**Implementation:**

Add new fields to Skill interface:

```typescript
export interface Skill {
  name: string;
  description: string;
  group: string;
  slug: string;
  excerpt: string;
  license?: string;
  tagline?: string;
  roles?: string[];
  tasks?: string[];
  favorite?: boolean;
  outputType?: 'document' | 'code' | 'visual' | 'guidance';
  examplePrompt?: string;
}
```

**Commit:**
```bash
git add site/src/types/index.ts
git commit -m "feat(site): add outputType and examplePrompt to Skill type"
```

---

## Task 4: Update Index Page Data Mapping

**Files:**
- Modify: `site/src/pages/index.astro`

**Implementation:**

Update the skillData mapping (around line 11-25) to include new fields:

```typescript
const skillData = skills.map(s => {
  const { group, slug } = parseSkillId(s.id);
  return {
    name: s.data.name,
    description: s.data.description,
    group,
    slug,
    excerpt: createExcerpt(s.data.description),
    license: s.data.license,
    tagline: s.data.tagline,
    roles: s.data.roles,
    tasks: s.data.tasks,
    favorite: s.data.favorite,
    outputType: s.data.outputType,
    examplePrompt: s.data.examplePrompt,
  };
});
```

**Commit:**
```bash
git add site/src/pages/index.astro
git commit -m "feat(site): pass outputType and examplePrompt to gallery"
```

---

## Task 5: Create useFavorites Hook

**Files:**
- Create: `site/src/hooks/useFavorites.ts`

**Implementation:**

```typescript
import { useState, useEffect, useCallback } from 'react';

const STORAGE_KEY = 'devkit-favorites';

function loadFavorites(): string[] {
  if (typeof window === 'undefined') return [];
  try {
    const stored = localStorage.getItem(STORAGE_KEY);
    return stored ? JSON.parse(stored) : [];
  } catch {
    return [];
  }
}

function saveFavorites(favorites: string[]): void {
  if (typeof window === 'undefined') return;
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(favorites));
  } catch {
    // Silently fail if localStorage is full or unavailable
  }
}

export function useFavorites() {
  const [favorites, setFavorites] = useState<string[]>([]);

  // Load from localStorage on mount
  useEffect(() => {
    setFavorites(loadFavorites());
  }, []);

  const toggleFavorite = useCallback((slug: string) => {
    setFavorites(prev => {
      const next = prev.includes(slug)
        ? prev.filter(s => s !== slug)
        : [...prev, slug];
      saveFavorites(next);
      return next;
    });
  }, []);

  const isFavorite = useCallback((slug: string) => {
    return favorites.includes(slug);
  }, [favorites]);

  return { favorites, toggleFavorite, isFavorite };
}
```

**Commit:**
```bash
git add site/src/hooks/useFavorites.ts
git commit -m "feat(site): create useFavorites hook for localStorage persistence"
```

---

## Task 6: Update FilterState Type

**Files:**
- Modify: `site/src/types/index.ts`

**Implementation:**

Add `favoritesOnly` to FilterState:

```typescript
export interface FilterState {
  search: string;
  groups: string[];
  roles: string[];
  tasks: string[];
  favoritesOnly: boolean;
}
```

**Commit:**
```bash
git add site/src/types/index.ts
git commit -m "feat(site): add favoritesOnly to FilterState"
```

---

## Task 7: Update useUrlFilters Hook

**Files:**
- Modify: `site/src/hooks/useUrlFilters.ts`

**Implementation:**

Update DEFAULT_FILTERS and parsing to include favoritesOnly:

```typescript
const DEFAULT_FILTERS: FilterState = {
  search: '',
  groups: [],
  roles: [],
  tasks: [],
  favoritesOnly: false,
};

// In the initial state function (around line 21-27):
return {
  search: params.get('q') || '',
  groups: parseArrayParam(params, 'groups'),
  roles: parseArrayParam(params, 'roles'),
  tasks: parseArrayParam(params, 'tasks'),
  favoritesOnly: params.get('favorites') === 'true',
};

// In the sync to URL effect (around line 31-36), add:
if (filters.favoritesOnly) params.set('favorites', 'true');

// In the popstate handler (around line 49-54):
setFiltersState({
  search: params.get('q') || '',
  groups: parseArrayParam(params, 'groups'),
  roles: parseArrayParam(params, 'roles'),
  tasks: parseArrayParam(params, 'tasks'),
  favoritesOnly: params.get('favorites') === 'true',
});
```

**Commit:**
```bash
git add site/src/hooks/useUrlFilters.ts
git commit -m "feat(site): add favoritesOnly to URL filter state"
```

---

## Task 8: Update FilterSidebar with Favorites Toggle

**Files:**
- Modify: `site/src/components/FilterSidebar.tsx`

**Implementation:**

Add new props and favorites toggle section at the top:

```typescript
interface Props {
  groups: [string, number][];
  selectedGroups: string[];
  selectedRoles: string[];
  selectedTasks: string[];
  favoritesOnly: boolean;
  favoritesCount: number;
  onToggleGroup: (group: string) => void;
  onToggleRole: (role: string) => void;
  onToggleTask: (task: string) => void;
  onToggleFavorites: () => void;
  onClear: () => void;
}

// Inside the component, add this section before the Roles section:
{/* Favorites toggle */}
{favoritesCount > 0 && (
  <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
    <button
      type="button"
      onClick={onToggleFavorites}
      className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm transition-all duration-150
        ${favoritesOnly
          ? 'bg-amber-500/10 text-amber-400'
          : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
        }`}
      aria-pressed={favoritesOnly}
    >
      <span className="flex items-center gap-2">
        <span>⭐</span>
        <span>My Favorites</span>
      </span>
      <span className={`text-xs tabular-nums ${favoritesOnly ? 'text-amber-500/70' : 'text-zinc-600'}`}>
        {favoritesCount}
      </span>
    </button>
  </div>
)}
```

Also update the hasFilters check:
```typescript
const hasFilters = selectedGroups.length > 0 || selectedRoles.length > 0 || selectedTasks.length > 0 || favoritesOnly;
```

**Commit:**
```bash
git add site/src/components/FilterSidebar.tsx
git commit -m "feat(site): add favorites toggle to FilterSidebar"
```

---

## Task 9: Update MobileFilterDrawer with Favorites Toggle

**Files:**
- Modify: `site/src/components/MobileFilterDrawer.tsx`

**Implementation:**

Add new props and favorites toggle (similar to FilterSidebar):

```typescript
interface Props {
  isOpen: boolean;
  onClose: () => void;
  groups: [string, number][];
  selectedGroups: string[];
  selectedRoles: string[];
  selectedTasks: string[];
  favoritesOnly: boolean;
  favoritesCount: number;
  onToggleGroup: (group: string) => void;
  onToggleRole: (role: string) => void;
  onToggleTask: (task: string) => void;
  onToggleFavorites: () => void;
  onClear: () => void;
}

// Add favorites section at top of filter content (inside <div className="p-4 space-y-6">):
{/* Favorites toggle */}
{favoritesCount > 0 && (
  <section>
    <button
      type="button"
      onClick={onToggleFavorites}
      className={`w-full flex items-center justify-between px-4 py-3 rounded-xl text-sm transition-all
        ${favoritesOnly
          ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
          : 'bg-zinc-800/50 text-zinc-400 border border-zinc-700/50'
        }`}
      aria-pressed={favoritesOnly}
    >
      <span className="flex items-center gap-2">
        <span>⭐</span>
        <span>My Favorites</span>
      </span>
      <span className="text-xs tabular-nums">
        {favoritesCount}
      </span>
    </button>
  </section>
)}
```

Update totalSelected calculation:
```typescript
const totalSelected = selectedGroups.length + selectedRoles.length + selectedTasks.length + (favoritesOnly ? 1 : 0);
```

**Commit:**
```bash
git add site/src/components/MobileFilterDrawer.tsx
git commit -m "feat(site): add favorites toggle to MobileFilterDrawer"
```

---

## Task 10: Update SkillGallery with Favorites Integration

**Files:**
- Modify: `site/src/components/SkillGallery.tsx`

**Implementation:**

Import and use the favorites hook, update filter logic and pass props:

```typescript
// Add import at top:
import { useFavorites } from '../hooks/useFavorites';

// Inside SkillGalleryInner, add after useUrlFilters:
const { favorites, toggleFavorite, isFavorite } = useFavorites();

// Update filteredSkills useMemo to include favorites filter:
const filteredSkills = useMemo(() => {
  return skills.filter(skill => {
    // Favorites filter (if enabled, only show favorites)
    if (filters.favoritesOnly && !favorites.includes(skill.slug)) {
      return false;
    }

    const searchLower = filters.search.toLowerCase();
    const matchesSearch = !filters.search ||
      skill.name.toLowerCase().includes(searchLower) ||
      skill.description.toLowerCase().includes(searchLower) ||
      (skill.tagline && skill.tagline.toLowerCase().includes(searchLower));

    const matchesGroup = filters.groups.length === 0 ||
      filters.groups.includes(skill.group);

    const matchesRole = filters.roles.length === 0 ||
      (skill.roles && skill.roles.some(r => filters.roles.includes(r)));

    const matchesTask = filters.tasks.length === 0 ||
      (skill.tasks && skill.tasks.some(t => filters.tasks.includes(t)));

    return matchesSearch && matchesGroup && matchesRole && matchesTask;
  });
}, [skills, filters, favorites]);

// Add toggle function:
const toggleFavoritesFilter = () => {
  setFilters({ favoritesOnly: !filters.favoritesOnly });
};

// Update clearFilters:
const clearFilters = () => {
  setSearchInput('');
  setFilters({ groups: [], roles: [], tasks: [], search: '', favoritesOnly: false });
};

// Update activeFilterCount:
const activeFilterCount = filters.groups.length + filters.roles.length + filters.tasks.length + (filters.favoritesOnly ? 1 : 0);

// Update FilterSidebar props:
<FilterSidebar
  groups={groups}
  selectedGroups={filters.groups}
  selectedRoles={filters.roles}
  selectedTasks={filters.tasks}
  favoritesOnly={filters.favoritesOnly}
  favoritesCount={favorites.length}
  onToggleGroup={toggleGroup}
  onToggleRole={toggleRole}
  onToggleTask={toggleTask}
  onToggleFavorites={toggleFavoritesFilter}
  onClear={clearFilters}
/>

// Update MobileFilterDrawer props:
<MobileFilterDrawer
  isOpen={isFilterDrawerOpen}
  onClose={() => setIsFilterDrawerOpen(false)}
  groups={groups}
  selectedGroups={filters.groups}
  selectedRoles={filters.roles}
  selectedTasks={filters.tasks}
  favoritesOnly={filters.favoritesOnly}
  favoritesCount={favorites.length}
  onToggleGroup={toggleGroup}
  onToggleRole={toggleRole}
  onToggleTask={toggleTask}
  onToggleFavorites={toggleFavoritesFilter}
  onClear={clearFilters}
/>

// Update SkillCard usage to pass favorite props:
<SkillCard
  skill={skill}
  baseUrl={baseUrl}
  isFavorite={isFavorite(skill.slug)}
  onToggleFavorite={() => toggleFavorite(skill.slug)}
/>
```

**Commit:**
```bash
git add site/src/components/SkillGallery.tsx
git commit -m "feat(site): integrate favorites into SkillGallery"
```

---

## Task 11: Update SkillCard with Star Button, Output Icon, and Example Prompt

**Files:**
- Modify: `site/src/components/SkillCard.tsx`

**Implementation:**

Add new imports, props, and visual elements:

```typescript
import type { Skill } from '../types';
import { DownloadButton } from './DownloadButton';
import { hasDownload } from '../lib/downloads';
import { OUTPUT_TYPES } from '../lib/tags';

interface Props {
  skill: Skill;
  baseUrl: string;
  isFavorite: boolean;
  onToggleFavorite: () => void;
}

// ... keep groupIcons as is ...

export function SkillCard({ skill, baseUrl, isFavorite, onToggleFavorite }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;
  const icon = groupIcons[skill.group] || '○';
  const displayRoles = skill.roles?.slice(0, 2) || [];
  const displayTasks = skill.tasks?.slice(0, 2) || [];
  const outputType = skill.outputType ? OUTPUT_TYPES[skill.outputType] : null;

  const handleStarClick = (e: React.MouseEvent) => {
    e.preventDefault();
    e.stopPropagation();
    onToggleFavorite();
  };

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-gradient-to-b from-zinc-900/80 to-zinc-900/40
                 border border-zinc-800/60
                 hover:border-zinc-700/80
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-emerald-500/5"
    >
      {/* Star button - always visible when favorited, visible on hover otherwise */}
      <button
        type="button"
        onClick={handleStarClick}
        className={`absolute top-4 left-4 z-10 p-1.5 rounded-lg transition-all duration-200
          ${isFavorite
            ? 'text-amber-400 bg-amber-500/10'
            : 'text-zinc-600 opacity-0 group-hover:opacity-100 hover:text-amber-400 hover:bg-amber-500/10'
          }`}
        aria-label={isFavorite ? 'Remove from favorites' : 'Add to favorites'}
        aria-pressed={isFavorite}
      >
        <svg className="w-4 h-4" fill={isFavorite ? 'currentColor' : 'none'} stroke="currentColor" viewBox="0 0 24 24">
          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M11.049 2.927c.3-.921 1.603-.921 1.902 0l1.519 4.674a1 1 0 00.95.69h4.915c.969 0 1.371 1.24.588 1.81l-3.976 2.888a1 1 0 00-.363 1.118l1.518 4.674c.3.922-.755 1.688-1.538 1.118l-3.976-2.888a1 1 0 00-1.176 0l-3.976 2.888c-.783.57-1.838-.197-1.538-1.118l1.518-4.674a1 1 0 00-.363-1.118l-3.976-2.888c-.784-.57-.38-1.81.588-1.81h4.914a1 1 0 00.951-.69l1.519-4.674z" />
        </svg>
      </button>

      {/* Download button overlay */}
      {hasDownload(skill.slug) && (
        <div className="absolute top-4 right-4 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 transition-opacity duration-200 z-10">
          <DownloadButton slug={skill.slug} baseUrl={baseUrl} variant="icon" />
        </div>
      )}

      <a
        href={skillUrl}
        aria-label={`View details for ${skill.name}`}
        className="block p-6 focus:outline-none focus:ring-2 focus:ring-emerald-500/50 focus:ring-inset rounded-2xl"
      >
        {/* Top accent line */}
        <div className="absolute top-0 inset-x-0 h-px bg-gradient-to-r from-transparent via-zinc-700/50 to-transparent" />

        {/* Hover glow */}
        <div className="absolute inset-0 bg-gradient-to-b from-emerald-500/[0.03] to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />

        <div className="relative">
          {/* Icon, output type, and group */}
          <div className="flex items-center gap-3 mb-3">
            <span className="text-2xl text-emerald-500/70 group-hover:text-emerald-400 transition-colors">
              {icon}
            </span>
            {outputType && (
              <span className="text-sm" title={outputType.label}>
                {outputType.emoji}
              </span>
            )}
            <span className="text-xs font-medium text-zinc-500 uppercase tracking-wider">
              {skill.group}
            </span>
          </div>

          {/* Title */}
          <h3 className="text-lg font-semibold text-zinc-100 group-hover:text-white transition-colors leading-snug">
            {skill.name}
          </h3>

          {/* Tagline (primary) or fallback to excerpt */}
          {skill.tagline ? (
            <p className="mt-2 text-sm text-zinc-400 font-medium">
              {skill.tagline}
            </p>
          ) : (
            <p className="mt-2 text-sm text-zinc-400 line-clamp-2 leading-relaxed">
              {skill.excerpt}
            </p>
          )}

          {/* Role and task badges */}
          {(displayRoles.length > 0 || displayTasks.length > 0) && (
            <div className="mt-4 flex flex-wrap gap-1.5">
              {displayRoles.map(role => (
                <span
                  key={role}
                  className="px-2 py-0.5 text-xs bg-zinc-800/70 text-zinc-400 rounded-full"
                >
                  {role}
                </span>
              ))}
              {displayTasks.map(task => (
                <span
                  key={task}
                  className="px-2 py-0.5 text-xs bg-emerald-500/10 text-emerald-400/80 rounded-full"
                >
                  {task}
                </span>
              ))}
            </div>
          )}

          {/* Example prompt */}
          {skill.examplePrompt && (
            <p className="mt-4 text-xs text-zinc-500 italic">
              Try: "{skill.examplePrompt}"
            </p>
          )}

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

**Commit:**
```bash
git add site/src/components/SkillCard.tsx
git commit -m "feat(site): add star button, output icon, and example prompt to SkillCard"
```

---

## Task 12: Add Sample Data to Favorite Skills

**Files:**
- Modify: `skills/internal-specialty/cadre-os/SKILL.md`
- Modify: `skills/ai-automation/ai-art-generation/SKILL.md`
- Modify: `skills/development-tools/brainstorming/SKILL.md`
- Modify: `skills/design-ui/frontend-design/SKILL.md`
- Modify: `skills/ai-automation/prompt-engineering/SKILL.md`
- Modify: `skills/data-documents/presentation-composer/SKILL.md`
- Modify: `skills/business-strategy/product-discovery/SKILL.md`

**Implementation:**

Add `outputType` and `examplePrompt` to each skill's frontmatter. Example for cadre-os:

```yaml
---
name: Cadre OS
description: ...
tagline: Your AI consulting partner
roles:
  - Product Manager
  - Designer
tasks:
  - Learn & Research
  - Document
favorite: true
outputType: guidance
examplePrompt: Help me run a discovery workshop
---
```

Suggested values:
| Skill | outputType | examplePrompt |
|-------|------------|---------------|
| cadre-os | guidance | Help me run a discovery workshop |
| ai-art-generation | visual | Create a hero image for my landing page |
| brainstorming | guidance | Help me explore solutions for user onboarding |
| frontend-design | code | Build a pricing page with dark mode |
| prompt-engineering | guidance | Improve my chatbot's system prompt |
| presentation-composer | document | Create a pitch deck for investors |
| product-discovery | document | Write a PRD for a new feature |

**Commit:**
```bash
git add skills/
git commit -m "feat(skills): add outputType and examplePrompt to favorite skills"
```

---

## Task 13: Final Build and Verification

**Steps:**

1. Run build:
```bash
cd site && npm run build
```
Expected: Build succeeds with no TypeScript errors

2. Run preview:
```bash
npm run preview
```

3. Verify manually:
- [ ] Output type emoji appears next to group icon on cards with outputType
- [ ] Star button appears on hover (top-left of card)
- [ ] Clicking star adds/removes from favorites (persists on reload)
- [ ] "My Favorites" toggle appears in sidebar when favorites exist
- [ ] Favorites filter works correctly
- [ ] Example prompt appears at bottom of cards with examplePrompt
- [ ] Mobile drawer has favorites toggle

**Commit:**
```bash
git add -A
git commit -m "feat(site): card enhancements complete - output types, favorites, example prompts"
```

---

## Summary

| Feature | Location | Behavior |
|---------|----------|----------|
| Output type icon | Card header row | Shows emoji (📄💻🎨💬) indicating what skill produces |
| Star button | Card top-left | Click to favorite, persists in localStorage |
| Favorites filter | Sidebar/drawer | Toggle to show only starred skills |
| Example prompt | Card bottom | Italic text showing sample usage |

All features degrade gracefully - cards without outputType or examplePrompt simply don't show those elements.
