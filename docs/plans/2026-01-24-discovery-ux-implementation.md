# Discovery UX Implementation Plan

> **For Claude:** Use superpowers:subagent-driven-development to implement this plan task-by-task.

**Goal:** Transform the devkit site into an editorial-style experience with curated Favorites, two-dimensional filtering (roles + tasks), and benefit-focused card copy

**Architecture:** Update SKILL.md schema with tagline/roles/tasks/favorite fields, create tag constants, build FavoritesSection component with asymmetric grid, extend FilterSidebar with role/task dimensions, update SkillCard with new visual hierarchy

**Tech Stack:** Astro 5, React 18, TypeScript, Tailwind CSS v4, Zod schemas

---

## Task 1: Add New Fields to Skills Schema

**Files:**
- Modify: `site/src/content.config.ts:4-21`

**Step 1: Update the skills schema**

Add `tagline`, `roles`, `tasks`, and `favorite` fields to the Zod schema:

```typescript
const skills = defineCollection({
  loader: glob({
    pattern: ['**/SKILL.md', '!**/archive/**', '!**/.archive/**'],
    base: '../skills',
    generateId: ({ entry }) => {
      return entry.replace(/\/SKILL\.md$/, '');
    },
  }),
  schema: z.object({
    name: z.string(),
    description: z.string(),
    license: z.string().optional(),
    tagline: z.string().optional(),
    roles: z.array(z.string()).optional(),
    tasks: z.array(z.string()).optional(),
    favorite: z.boolean().optional(),
  }),
});
```

**Step 2: Run build to verify schema compiles**

Run: `cd site && npm run build`
Expected: Build succeeds (existing skills don't have new fields, but they're optional)

**Step 3: Commit**

```bash
git add site/src/content.config.ts
git commit -m "feat(site): add tagline, roles, tasks, favorite to skills schema"
```

---

## Task 2: Create Tag Constants

**Files:**
- Create: `site/src/lib/tags.ts`

**Step 1: Create the tags constants file**

```typescript
// Role tags - "I am a..."
export const ROLE_TAGS = [
  'Frontend Developer',
  'Backend Developer',
  'Full-Stack Developer',
  'AI/ML Engineer',
  'DevOps Engineer',
  'Digital Marketer',
  'Content Creator',
  'Salesperson',
  'Product Manager',
  'Designer',
  'Data Analyst',
] as const;

export type RoleTag = typeof ROLE_TAGS[number];

// Task tags - "I want to..."
export const TASK_TAGS = [
  'Write Code',
  'Debug Code',
  'Test Code',
  'Review Code',
  'Document',
  'Deploy',
  'Create Images',
  'Create Videos',
  'Create Presentations',
  'Write Emails',
  'Analyze Data',
  'Automate Tasks',
  'Learn & Research',
] as const;

export type TaskTag = typeof TASK_TAGS[number];

// Favorite skill slugs (for curation)
export const FAVORITE_SKILLS = [
  'cadre-os',
  'ai-art-generation',
  'brainstorming',
  'frontend-design',
  'prompt-engineering',
  'presentation-composer',
  'product-discovery',
] as const;
```

**Step 2: Verify TypeScript compiles**

Run: `cd site && npx tsc --noEmit`
Expected: No errors

**Step 3: Commit**

```bash
git add site/src/lib/tags.ts
git commit -m "feat(site): add role and task tag constants"
```

---

## Task 3: Update Skill Type Interface

**Files:**
- Modify: `site/src/types/index.ts:1-8`

**Step 1: Add new fields to Skill interface**

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
}
```

**Step 2: Verify TypeScript compiles**

Run: `cd site && npx tsc --noEmit`
Expected: No errors

**Step 3: Commit**

```bash
git add site/src/types/index.ts
git commit -m "feat(site): add tagline, roles, tasks, favorite to Skill type"
```

---

## Task 4: Update Index Page to Pass New Fields

**Files:**
- Modify: `site/src/pages/index.astro:9-20`

**Step 1: Update skillData mapping to include new fields**

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
  };
});
```

**Step 2: Run build to verify**

Run: `cd site && npm run build`
Expected: Build succeeds

**Step 3: Commit**

```bash
git add site/src/pages/index.astro
git commit -m "feat(site): pass tagline, roles, tasks, favorite to gallery"
```

---

## Task 5: Add Tags to the 7 Favorite Skills

**Files:**
- Modify: `skills/internal-specialty/cadre-os/SKILL.md` (frontmatter only)
- Modify: `skills/ai-automation/ai-art-generation/SKILL.md` (frontmatter only)
- Modify: `skills/business-strategy/product-discovery/SKILL.md` (frontmatter only)
- Modify: `skills/ai-automation/prompt-engineering/SKILL.md` (frontmatter only)
- Modify: `skills/design-ui/frontend-design/SKILL.md` (frontmatter only)
- Modify: `skills/communications/presentation-composer/SKILL.md` (frontmatter only)

Note: `brainstorming` needs to be located first.

**Step 1: Find brainstorming skill location**

Run: `find skills -name "SKILL.md" -path "*brainstorm*" | head -5`

**Step 2: Add frontmatter to each favorite skill**

For each skill, add these fields after existing frontmatter:

**cadre-os:**
```yaml
tagline: "Your AI operating system"
roles:
  - Full-Stack Developer
  - AI/ML Engineer
tasks:
  - Automate Tasks
  - Write Code
favorite: true
```

**ai-art-generation:**
```yaml
tagline: "Create stunning visuals"
roles:
  - Designer
  - Content Creator
  - Digital Marketer
tasks:
  - Create Images
favorite: true
```

**brainstorming:**
```yaml
tagline: "Ideas → actionable plans"
roles:
  - Product Manager
  - Full-Stack Developer
  - Designer
tasks:
  - Learn & Research
favorite: true
```

**frontend-design:**
```yaml
tagline: "Distinctive, memorable UIs"
roles:
  - Frontend Developer
  - Designer
tasks:
  - Write Code
  - Create Images
favorite: true
```

**prompt-engineering:**
```yaml
tagline: "Master AI interactions"
roles:
  - AI/ML Engineer
  - Content Creator
  - Full-Stack Developer
tasks:
  - Write Code
  - Automate Tasks
favorite: true
```

**presentation-composer:**
```yaml
tagline: "Beautiful decks fast"
roles:
  - Salesperson
  - Product Manager
  - Content Creator
tasks:
  - Create Presentations
favorite: true
```

**product-discovery:**
```yaml
tagline: "Validate before you build"
roles:
  - Product Manager
  - Full-Stack Developer
tasks:
  - Learn & Research
favorite: true
```

**Step 3: Run build to verify frontmatter parses**

Run: `cd site && npm run build`
Expected: Build succeeds

**Step 4: Commit**

```bash
git add skills/
git commit -m "feat(skills): add tagline, roles, tasks to 7 favorite skills"
```

---

## Task 6: Create FeaturedSkillCard Component

**Files:**
- Create: `site/src/components/FeaturedSkillCard.tsx`

**Step 1: Create the component**

```typescript
import type { Skill } from '../types';

interface Props {
  skill: Skill;
  baseUrl: string;
  featured?: boolean;
}

export function FeaturedSkillCard({ skill, baseUrl, featured = false }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;

  return (
    <a
      href={skillUrl}
      className={`group relative block overflow-hidden rounded-2xl
                  bg-gradient-to-br from-zinc-900 to-zinc-900/80
                  border border-zinc-800/60 hover:border-emerald-500/30
                  transition-all duration-300
                  ${featured ? 'row-span-2 col-span-2' : ''}`}
    >
      {/* Glow effect for featured */}
      {featured && (
        <div className="absolute inset-0 bg-gradient-to-br from-emerald-500/10 via-transparent to-transparent opacity-50" />
      )}

      <div className={`relative p-6 ${featured ? 'p-8' : 'p-6'} h-full flex flex-col`}>
        {/* Tagline */}
        {skill.tagline && (
          <span className={`text-emerald-400 font-medium mb-2 ${featured ? 'text-lg' : 'text-sm'}`}>
            {skill.tagline}
          </span>
        )}

        {/* Name */}
        <h3 className={`font-display font-bold text-white group-hover:text-emerald-50 transition-colors
                        ${featured ? 'text-3xl md:text-4xl' : 'text-xl'}`}>
          {skill.name}
        </h3>

        {/* Description - only on featured */}
        {featured && (
          <p className="mt-4 text-zinc-400 text-lg leading-relaxed line-clamp-3">
            {skill.excerpt}
          </p>
        )}

        {/* Role badges */}
        {skill.roles && skill.roles.length > 0 && (
          <div className={`flex flex-wrap gap-2 ${featured ? 'mt-6' : 'mt-4'}`}>
            {skill.roles.slice(0, featured ? 3 : 2).map(role => (
              <span
                key={role}
                className="px-2 py-1 text-xs bg-zinc-800/80 text-zinc-400 rounded-full"
              >
                {role}
              </span>
            ))}
          </div>
        )}

        {/* Arrow indicator */}
        <div className="mt-auto pt-4 flex items-center text-zinc-500 group-hover:text-emerald-400 transition-colors">
          <span className={`${featured ? 'text-base' : 'text-sm'}`}>
            Explore →
          </span>
        </div>
      </div>
    </a>
  );
}
```

**Step 2: Verify TypeScript compiles**

Run: `cd site && npx tsc --noEmit`
Expected: No errors

**Step 3: Commit**

```bash
git add site/src/components/FeaturedSkillCard.tsx
git commit -m "feat(site): create FeaturedSkillCard component"
```

---

## Task 7: Create FavoritesSection Component

**Files:**
- Create: `site/src/components/FavoritesSection.tsx`

**Step 1: Create the component**

```typescript
import type { Skill } from '../types';
import { FeaturedSkillCard } from './FeaturedSkillCard';
import { FAVORITE_SKILLS } from '../lib/tags';

interface Props {
  skills: Skill[];
  baseUrl: string;
}

export function FavoritesSection({ skills, baseUrl }: Props) {
  // Get favorites in the specified order
  const favorites = FAVORITE_SKILLS
    .map(slug => skills.find(s => s.slug === slug))
    .filter((s): s is Skill => s !== undefined);

  if (favorites.length === 0) return null;

  const [featured, ...rest] = favorites;

  return (
    <section className="mb-16">
      {/* Section header with editorial styling */}
      <div className="flex items-center gap-4 mb-8">
        <h2 className="font-display text-2xl md:text-3xl font-bold text-white">
          Staff Picks
        </h2>
        <div className="flex-1 h-px bg-zinc-800" />
      </div>

      {/* Asymmetric grid */}
      <div className="grid grid-cols-2 md:grid-cols-4 gap-4 md:gap-6">
        {/* Featured card (2x2) */}
        <FeaturedSkillCard
          skill={featured}
          baseUrl={baseUrl}
          featured={true}
        />

        {/* Remaining cards */}
        {rest.map(skill => (
          <FeaturedSkillCard
            key={skill.slug}
            skill={skill}
            baseUrl={baseUrl}
          />
        ))}
      </div>
    </section>
  );
}
```

**Step 2: Verify TypeScript compiles**

Run: `cd site && npx tsc --noEmit`
Expected: No errors

**Step 3: Commit**

```bash
git add site/src/components/FavoritesSection.tsx
git commit -m "feat(site): create FavoritesSection with asymmetric grid"
```

---

## Task 8: Add FavoritesSection to Index Page

**Files:**
- Modify: `site/src/pages/index.astro`

**Step 1: Import FavoritesSection**

Add import at top of frontmatter:
```typescript
import { FavoritesSection } from '../components/FavoritesSection';
```

**Step 2: Add FavoritesSection after Hero**

After `<Hero skillCount={skillData.length} />` and before `<main>`, add:

```astro
<section class="max-w-7xl mx-auto px-8 pt-8">
  <FavoritesSection skills={skillData} baseUrl={baseUrl} client:visible />
</section>
```

**Step 3: Run dev server and visually verify**

Run: `cd site && npm run dev`
Expected: Favorites section appears below hero with cadre-os as large featured card

**Step 4: Commit**

```bash
git add site/src/pages/index.astro
git commit -m "feat(site): add FavoritesSection to homepage"
```

---

## Task 9: Update FilterSidebar with Role/Task Sections

**Files:**
- Modify: `site/src/components/FilterSidebar.tsx`

**Step 1: Update Props interface and component**

```typescript
import { ROLE_TAGS, TASK_TAGS } from '../lib/tags';

interface Props {
  groups: [string, number][];
  selectedGroups: string[];
  selectedRoles: string[];
  selectedTasks: string[];
  onToggleGroup: (group: string) => void;
  onToggleRole: (role: string) => void;
  onToggleTask: (task: string) => void;
  onClear: () => void;
}

export function FilterSidebar({
  groups,
  selectedGroups,
  selectedRoles,
  selectedTasks,
  onToggleGroup,
  onToggleRole,
  onToggleTask,
  onClear,
}: Props) {
  const hasFilters = selectedGroups.length > 0 || selectedRoles.length > 0 || selectedTasks.length > 0;

  return (
    <aside className="w-64 shrink-0 hidden md:block">
      <div className="sticky top-24 space-y-6">
        {/* Roles section */}
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <h2 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider mb-4 pb-3 border-b border-zinc-800/50">
            I am a...
          </h2>
          <div className="space-y-1" role="group" aria-label="Filter by role">
            {ROLE_TAGS.map(role => {
              const isChecked = selectedRoles.includes(role);
              return (
                <button
                  type="button"
                  key={role}
                  onClick={() => onToggleRole(role)}
                  className={`w-full flex items-center px-3 py-2 rounded-lg text-sm transition-all duration-150
                    ${isChecked
                      ? 'bg-emerald-500/10 text-emerald-400'
                      : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
                    }`}
                  aria-pressed={isChecked}
                >
                  <span className="truncate">{role}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Tasks section */}
        <div className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <h2 className="text-xs font-semibold text-zinc-400 uppercase tracking-wider mb-4 pb-3 border-b border-zinc-800/50">
            I want to...
          </h2>
          <div className="space-y-1" role="group" aria-label="Filter by task">
            {TASK_TAGS.map(task => {
              const isChecked = selectedTasks.includes(task);
              return (
                <button
                  type="button"
                  key={task}
                  onClick={() => onToggleTask(task)}
                  className={`w-full flex items-center px-3 py-2 rounded-lg text-sm transition-all duration-150
                    ${isChecked
                      ? 'bg-emerald-500/10 text-emerald-400'
                      : 'text-zinc-400 hover:bg-zinc-800/50 hover:text-zinc-200'
                    }`}
                  aria-pressed={isChecked}
                >
                  <span className="truncate">{task}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Categories section (collapsed by default) */}
        <details className="p-4 rounded-xl bg-zinc-900/50 border border-zinc-800/50">
          <summary className="text-xs font-semibold text-zinc-400 uppercase tracking-wider cursor-pointer">
            Categories ({groups.length})
          </summary>
          <div className="mt-4 space-y-1" role="group" aria-label="Filter by category">
            {groups.map(([group, count]) => {
              const isChecked = selectedGroups.includes(group);
              return (
                <button
                  type="button"
                  key={group}
                  onClick={() => onToggleGroup(group)}
                  className={`w-full flex items-center justify-between px-3 py-2 rounded-lg text-sm transition-all duration-150
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
        </details>

        {/* Clear all button */}
        {hasFilters && (
          <button
            type="button"
            onClick={onClear}
            className="w-full px-4 py-2 text-sm text-zinc-500 hover:text-white transition-colors"
          >
            Clear all filters
          </button>
        )}
      </div>
    </aside>
  );
}
```

**Step 2: Verify TypeScript compiles**

Run: `cd site && npx tsc --noEmit`
Expected: Errors in SkillGallery (expected - we'll fix next)

**Step 3: Commit**

```bash
git add site/src/components/FilterSidebar.tsx
git commit -m "feat(site): add role and task filter sections to sidebar"
```

---

## Task 10: Update Filter State and SkillGallery

**Files:**
- Modify: `site/src/types/index.ts` (FilterState)
- Modify: `site/src/hooks/useUrlFilters.ts`
- Modify: `site/src/components/SkillGallery.tsx`

**Step 1: Update FilterState type**

In `site/src/types/index.ts`, update FilterState:

```typescript
export interface FilterState {
  search: string;
  groups: string[];
  roles: string[];
  tasks: string[];
}
```

**Step 2: Update useUrlFilters hook**

Read the current hook first, then update to handle roles and tasks URL params.

**Step 3: Update SkillGallery to use new filter dimensions**

Update the filtering logic:

```typescript
// Filter skills
const filteredSkills = useMemo(() => {
  return skills.filter(skill => {
    // Search filter
    const searchLower = filters.search.toLowerCase();
    const matchesSearch = !filters.search ||
      skill.name.toLowerCase().includes(searchLower) ||
      skill.description.toLowerCase().includes(searchLower) ||
      (skill.tagline && skill.tagline.toLowerCase().includes(searchLower));

    // Group filter (OR within groups)
    const matchesGroup = filters.groups.length === 0 ||
      filters.groups.includes(skill.group);

    // Role filter (OR within roles)
    const matchesRole = filters.roles.length === 0 ||
      (skill.roles && skill.roles.some(r => filters.roles.includes(r)));

    // Task filter (OR within tasks)
    const matchesTask = filters.tasks.length === 0 ||
      (skill.tasks && skill.tasks.some(t => filters.tasks.includes(t)));

    // AND between dimensions
    return matchesSearch && matchesGroup && matchesRole && matchesTask;
  });
}, [skills, filters]);
```

**Step 4: Update FilterSidebar props in SkillGallery**

```typescript
<FilterSidebar
  groups={groups}
  selectedGroups={filters.groups}
  selectedRoles={filters.roles}
  selectedTasks={filters.tasks}
  onToggleGroup={toggleGroup}
  onToggleRole={toggleRole}
  onToggleTask={toggleTask}
  onClear={clearFilters}
/>
```

**Step 5: Add toggle functions**

```typescript
const toggleRole = (role: string) => {
  setFilters({
    roles: filters.roles.includes(role)
      ? filters.roles.filter(r => r !== role)
      : [...filters.roles, role],
  });
};

const toggleTask = (task: string) => {
  setFilters({
    tasks: filters.tasks.includes(task)
      ? filters.tasks.filter(t => t !== task)
      : [...filters.tasks, task],
  });
};

const clearFilters = () => {
  setSearchInput('');
  setFilters({ groups: [], roles: [], tasks: [], search: '' });
};
```

**Step 6: Run build to verify**

Run: `cd site && npm run build`
Expected: Build succeeds

**Step 7: Commit**

```bash
git add site/src/types/index.ts site/src/hooks/useUrlFilters.ts site/src/components/SkillGallery.tsx
git commit -m "feat(site): implement role and task filtering"
```

---

## Task 11: Update SkillCard with Tagline and Badges

**Files:**
- Modify: `site/src/components/SkillCard.tsx`

**Step 1: Update the component to show tagline and role badges**

```typescript
import type { Skill } from '../types';
import { DownloadButton } from './DownloadButton';
import { hasDownload } from '../lib/downloads';

interface Props {
  skill: Skill;
  baseUrl: string;
}

export function SkillCard({ skill, baseUrl }: Props) {
  const skillUrl = `${baseUrl}/skills/${skill.slug}`;

  return (
    <div
      className="group relative rounded-2xl overflow-hidden
                 bg-gradient-to-b from-zinc-900/80 to-zinc-900/40
                 border border-zinc-800/60
                 hover:border-zinc-700/80
                 transition-all duration-300 ease-out
                 hover:shadow-2xl hover:shadow-emerald-500/5"
    >
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
          {/* Tagline - NEW */}
          {skill.tagline && (
            <p className="text-sm text-emerald-400 font-medium mb-2">
              {skill.tagline}
            </p>
          )}

          {/* Title - larger */}
          <h3 className="text-xl font-display font-bold text-zinc-100 group-hover:text-white transition-colors leading-snug">
            {skill.name}
          </h3>

          {/* Role badges - NEW */}
          {skill.roles && skill.roles.length > 0 && (
            <div className="flex flex-wrap gap-1.5 mt-3">
              {skill.roles.slice(0, 2).map(role => (
                <span
                  key={role}
                  className="px-2 py-0.5 text-xs bg-zinc-800/80 text-zinc-500 rounded-full"
                >
                  {role}
                </span>
              ))}
            </div>
          )}

          {/* Group label - smaller, secondary */}
          <p className="mt-3 text-xs text-zinc-600 uppercase tracking-wider">
            {skill.group}
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

**Step 2: Run dev server and verify cards display correctly**

Run: `cd site && npm run dev`
Expected: Cards show tagline (if present), name, role badges, and group label

**Step 3: Commit**

```bash
git add site/src/components/SkillCard.tsx
git commit -m "feat(site): update SkillCard with tagline and role badges"
```

---

## Task 12: Update MobileFilterDrawer with Roles/Tasks

**Files:**
- Modify: `site/src/components/MobileFilterDrawer.tsx`

**Step 1: Read current implementation**

Read the file to understand current structure.

**Step 2: Add role and task filter sections**

Mirror the FilterSidebar structure but in mobile drawer format.

**Step 3: Update props to match FilterSidebar**

```typescript
interface Props {
  isOpen: boolean;
  onClose: () => void;
  groups: [string, number][];
  selectedGroups: string[];
  selectedRoles: string[];
  selectedTasks: string[];
  onToggleGroup: (group: string) => void;
  onToggleRole: (role: string) => void;
  onToggleTask: (task: string) => void;
  onClear: () => void;
}
```

**Step 4: Verify on mobile viewport**

Run: `cd site && npm run dev`
Open dev tools, set mobile viewport, test filter drawer

**Step 5: Commit**

```bash
git add site/src/components/MobileFilterDrawer.tsx
git commit -m "feat(site): add role and task filters to mobile drawer"
```

---

## Task 13: Add Editorial Visual Refinements

**Files:**
- Modify: `site/src/styles/global.css`

**Step 1: Add ruled line utility class**

```css
@layer utilities {
  .ruled-line {
    @apply relative;
  }

  .ruled-line::after {
    content: '';
    @apply absolute bottom-0 left-0 right-0 h-px bg-zinc-800;
  }
}
```

**Step 2: Enhance typography scale**

Verify `h1` is dramatically larger than body text. Update if needed:

```css
h1 { @apply text-5xl md:text-6xl font-bold; }
h2 { @apply text-3xl md:text-4xl; }
```

**Step 3: Commit**

```bash
git add site/src/styles/global.css
git commit -m "style(site): add editorial ruled-line utility and typography refinements"
```

---

## Task 14: Final Build and Visual Verification

**Files:**
- None (verification only)

**Step 1: Run full build**

Run: `cd site && npm run build`
Expected: Build succeeds with no errors

**Step 2: Run preview**

Run: `cd site && npm run preview`
Expected: Site runs at localhost:4321

**Step 3: Visual checklist**

- [ ] Favorites section shows below hero
- [ ] Cadre-OS is large featured card (2x2)
- [ ] 6 smaller cards in asymmetric grid
- [ ] Role filters appear in sidebar ("I am a...")
- [ ] Task filters appear in sidebar ("I want to...")
- [ ] Categories collapsed by default
- [ ] Filtering works (selecting role reduces results)
- [ ] Cards show tagline, name, role badges
- [ ] Mobile filter drawer has role/task sections

**Step 4: Commit any fixes**

If visual issues found, fix and commit.

---

## Task 15: Batch-Tag Remaining Skills (Optional - Large Task)

**Files:**
- Modify: All SKILL.md files in `skills/` directory

**Note:** This task involves adding `tagline`, `roles`, and `tasks` to all 114 remaining skills (121 total - 7 favorites already tagged). This can be done incrementally or with Claude's assistance in a separate session.

**Approach:**
1. Group skills by their directory (ai-automation, business-strategy, etc.)
2. For each group, determine appropriate roles and tasks
3. Generate taglines that are benefit-focused (2-5 words)
4. Update frontmatter in batches

**Example batch for ai-automation skills:**

```yaml
# prompt-engineering (already done)
# ai-art-generation (already done)

# anthropic-messages-api
tagline: "Claude API mastery"
roles:
  - AI/ML Engineer
  - Backend Developer
tasks:
  - Write Code
  - Automate Tasks

# openai-responses-api
tagline: "OpenAI API mastery"
roles:
  - AI/ML Engineer
  - Backend Developer
tasks:
  - Write Code
  - Automate Tasks
```

**This task is intentionally left as guidance** — it's too large for a single implementation pass. Execute in batches of 10-15 skills at a time.

---

## Verification Checklist

- [ ] Skills schema includes tagline, roles, tasks, favorite fields
- [ ] Tag constants defined in `lib/tags.ts`
- [ ] 7 favorite skills have frontmatter with new fields
- [ ] FavoritesSection renders with asymmetric grid
- [ ] Cadre-OS is featured (large) card
- [ ] FilterSidebar shows "I am a..." and "I want to..." sections
- [ ] Role/task filtering works correctly (OR within, AND between)
- [ ] SkillCard displays tagline and role badges
- [ ] MobileFilterDrawer has role/task sections
- [ ] Build passes with no TypeScript errors
- [ ] Visual design matches editorial/magazine aesthetic
