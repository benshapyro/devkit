# Devkit Site Improvements Plan

> **For Claude:** Use superpowers:subagent-driven-development to execute this plan task-by-task.

**Goal:** Expand the devkit site with all artifact types (hooks, commands, agents), add missing functionality (Cmd+K, mobile filters), and refine the design with hybrid typography.

**Architecture:** Extend existing Astro content collections for new artifact types, add React components for new features, enhance typography with display font pairing.

**Tech Stack:** Astro 5, React 18, Tailwind CSS v4, Google Fonts

---

## Current State

**Existing:**
- 122 skill pages with search, filters, downloads
- Skills organized by group with detail pages

**Missing:**
- 7 hooks not displayed
- 14 commands not displayed
- 11 agents not displayed
- Cmd+K keyboard shortcut (hint exists but doesn't work)
- Mobile filter access (hidden on mobile)
- Display font for headings

**Repository structure:**
```
devkit/
├── skills/           # 122 skills (currently displayed)
├── hooks/            # 7 hooks (not displayed)
├── commands/         # 14 commands (not displayed)
└── agents/           # 11 agents (not displayed)
```

---

## Task 1: Add Display Font for Headings

**Files:**
- Modify: `site/src/layouts/Layout.astro`
- Modify: `site/src/styles/global.css`

**Implementation:**

Add Plus Jakarta Sans (or similar distinctive display font) to Layout.astro:

```html
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

Update global.css @theme block:

```css
@theme {
  --font-display: 'Plus Jakarta Sans', ui-sans-serif, system-ui, sans-serif;
  --font-sans: 'Inter', ui-sans-serif, system-ui, sans-serif;
  --font-mono: 'JetBrains Mono', ui-monospace, monospace;
}
```

Update heading styles:

```css
h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-display);
  @apply tracking-tight;
  font-weight: 600;
}
```

**Commit:** `feat(site): add Plus Jakarta Sans display font for headings`

---

## Task 2: Implement Cmd+K Search Shortcut

**Files:**
- Modify: `site/src/components/SkillGallery.tsx`

**Implementation:**

Add keyboard event listener that focuses the search input on Cmd+K (Mac) or Ctrl+K (Windows/Linux):

```tsx
// Add ref to SearchInput
const searchInputRef = useRef<HTMLInputElement>(null);

// Add keyboard shortcut effect
useEffect(() => {
  const handleKeyDown = (e: KeyboardEvent) => {
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      searchInputRef.current?.focus();
    }
  };

  document.addEventListener('keydown', handleKeyDown);
  return () => document.removeEventListener('keydown', handleKeyDown);
}, []);
```

Update SearchInput to accept a ref:

```tsx
// SearchInput.tsx
import { forwardRef } from 'react';

export const SearchInput = forwardRef<HTMLInputElement, Props>(
  ({ value, onChange }, ref) => {
    return (
      <input
        ref={ref}
        type="search"
        // ... rest of props
      />
    );
  }
);
```

**Commit:** `feat(site): implement Cmd+K keyboard shortcut for search`

---

## Task 3: Add Mobile Filter Drawer

**Files:**
- Create: `site/src/components/MobileFilterDrawer.tsx`
- Modify: `site/src/components/SkillGallery.tsx`
- Modify: `site/src/components/FilterSidebar.tsx`

**Implementation:**

Create MobileFilterDrawer component:

```tsx
interface Props {
  isOpen: boolean;
  onClose: () => void;
  groups: [string, number][];
  selected: string[];
  onToggle: (group: string) => void;
  onClear: () => void;
}

export function MobileFilterDrawer({ isOpen, onClose, groups, selected, onToggle, onClear }: Props) {
  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 z-50 md:hidden">
      {/* Backdrop */}
      <div className="absolute inset-0 bg-black/60" onClick={onClose} />

      {/* Drawer */}
      <div className="absolute bottom-0 left-0 right-0 bg-zinc-900 rounded-t-2xl max-h-[70vh] overflow-y-auto">
        <div className="sticky top-0 bg-zinc-900 p-4 border-b border-zinc-800 flex items-center justify-between">
          <h2 className="font-semibold">Filters</h2>
          <button onClick={onClose} className="p-2 text-zinc-400 hover:text-white">
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        <div className="p-4">
          {/* Reuse filter content from FilterSidebar */}
          {/* ... filter buttons ... */}
        </div>

        <div className="sticky bottom-0 bg-zinc-900 p-4 border-t border-zinc-800">
          <button
            onClick={onClose}
            className="w-full py-3 bg-emerald-500 hover:bg-emerald-400 text-white font-medium rounded-xl"
          >
            Show Results
          </button>
        </div>
      </div>
    </div>
  );
}
```

Add filter button to SkillGallery for mobile:

```tsx
<button
  className="md:hidden flex items-center gap-2 px-4 py-2 bg-zinc-800 rounded-lg text-sm"
  onClick={() => setFilterDrawerOpen(true)}
>
  <svg className="w-4 h-4" /* filter icon */ />
  Filters
  {selectedGroups.length > 0 && (
    <span className="bg-emerald-500 text-white text-xs px-1.5 rounded-full">
      {selectedGroups.length}
    </span>
  )}
</button>
```

**Commit:** `feat(site): add mobile filter drawer`

---

## Task 4: Create Content Collections for Hooks, Commands, Agents

**Files:**
- Modify: `site/src/content.config.ts`
- Create: `site/src/content/hooks/` (symlink or copy)
- Create: `site/src/content/commands/` (symlink or copy)
- Create: `site/src/content/agents/` (symlink or copy)

**Implementation:**

Update content.config.ts to add new collections:

```typescript
const hooks = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../../hooks' }),
  schema: z.object({
    name: z.string().optional(),
    description: z.string().optional(),
    event: z.string().optional(),
    // ... other hook frontmatter fields
  }),
});

const commands = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../../commands' }),
  schema: z.object({
    // command frontmatter fields
  }),
});

const agents = defineCollection({
  loader: glob({ pattern: '**/*.md', base: '../../agents' }),
  schema: z.object({
    name: z.string().optional(),
    description: z.string().optional(),
    // ... other agent frontmatter fields
  }),
});

export const collections = { skills, hooks, commands, agents };
```

**Note:** Exclude README.md and CLAUDE.md from collections.

**Commit:** `feat(site): add content collections for hooks, commands, agents`

---

## Task 5: Create Hooks Gallery Page

**Files:**
- Create: `site/src/pages/hooks/index.astro`
- Create: `site/src/pages/hooks/[slug].astro`
- Create: `site/src/components/HookCard.tsx`

**Implementation:**

Similar structure to skills but simpler (no groups/filters for now):

```astro
---
// hooks/index.astro
import { getCollection } from 'astro:content';
import Layout from '../../layouts/Layout.astro';
import { HookCard } from '../../components/HookCard';

const hooks = await getCollection('hooks', ({ id }) =>
  !id.includes('README') && !id.includes('CLAUDE')
);
---

<Layout title="Hooks | Devkit">
  <main class="max-w-6xl mx-auto px-6 py-12">
    <h1 class="text-4xl font-bold mb-4">Hooks</h1>
    <p class="text-zinc-400 mb-8">Event-driven automation for Claude Code</p>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {hooks.map(hook => (
        <HookCard hook={hook} />
      ))}
    </div>
  </main>
</Layout>
```

**Commit:** `feat(site): add hooks gallery and detail pages`

---

## Task 6: Create Commands Gallery Page

**Files:**
- Create: `site/src/pages/commands/index.astro`
- Create: `site/src/pages/commands/[slug].astro`
- Create: `site/src/components/CommandCard.tsx`

**Implementation:**

Similar to hooks. Commands are user-invoked slash commands.

**Commit:** `feat(site): add commands gallery and detail pages`

---

## Task 7: Create Agents Gallery Page

**Files:**
- Create: `site/src/pages/agents/index.astro`
- Create: `site/src/pages/agents/[slug].astro`
- Create: `site/src/components/AgentCard.tsx`

**Implementation:**

Similar to hooks. Agents are specialized sub-agents.

**Commit:** `feat(site): add agents gallery and detail pages`

---

## Task 8: Add Navigation for All Artifact Types

**Files:**
- Modify: `site/src/pages/index.astro` (header)
- Modify: `site/src/components/Footer.astro`

**Implementation:**

Update header navigation to include links to all sections:

```astro
<nav class="flex items-center gap-6">
  <a href={`${baseUrl}/`} class="text-sm text-zinc-400 hover:text-white">Skills</a>
  <a href={`${baseUrl}/hooks`} class="text-sm text-zinc-400 hover:text-white">Hooks</a>
  <a href={`${baseUrl}/commands`} class="text-sm text-zinc-400 hover:text-white">Commands</a>
  <a href={`${baseUrl}/agents`} class="text-sm text-zinc-400 hover:text-white">Agents</a>
</nav>
```

Update Hero to show counts for all types, or create a unified landing page.

**Commit:** `feat(site): add navigation for all artifact types`

---

## Task 9: Add Quick Copy Install Command

**Files:**
- Create: `site/src/components/CopyInstallButton.tsx`
- Modify: `site/src/components/SkillCard.tsx`
- Modify: `site/src/pages/skills/[slug].astro`

**Implementation:**

Create a copy button that copies the install/deploy command:

```tsx
interface Props {
  skillPath: string; // e.g., "development-tools/mcp-builder"
}

export function CopyInstallButton({ skillPath }: Props) {
  const [copied, setCopied] = useState(false);

  const command = `cp -r skills/${skillPath} ~/.claude/skills/`;

  const handleCopy = async () => {
    await navigator.clipboard.writeText(command);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <button
      onClick={handleCopy}
      className="inline-flex items-center gap-2 px-3 py-1.5 text-sm bg-zinc-800 hover:bg-zinc-700 rounded-lg transition-colors"
      aria-label="Copy install command"
    >
      {copied ? (
        <>
          <CheckIcon className="w-4 h-4 text-emerald-400" />
          Copied!
        </>
      ) : (
        <>
          <ClipboardIcon className="w-4 h-4" />
          Copy install
        </>
      )}
    </button>
  );
}
```

**Commit:** `feat(site): add quick copy install command button`

---

## Task 10: Add Skill Comparison View (P3)

**Files:**
- Create: `site/src/pages/compare.astro`
- Create: `site/src/components/CompareSelector.tsx`
- Create: `site/src/components/CompareView.tsx`

**Implementation:**

This is a more complex feature. Create a page where users can:
1. Search/select 2-3 skills
2. See them side-by-side with key attributes compared

Can be URL-based: `/compare?skills=mcp-builder,api-design-patterns`

**Commit:** `feat(site): add skill comparison view`

---

## Verification Checklist

1. **Build Check:**
   ```bash
   cd site && npm run build
   ```
   - [ ] No TypeScript errors
   - [ ] All pages build successfully
   - [ ] New artifact pages generate

2. **Functionality Check:**
   - [ ] Cmd+K focuses search input
   - [ ] Mobile filter drawer opens/closes
   - [ ] Hooks/commands/agents pages render
   - [ ] Navigation works between sections
   - [ ] Copy install button works

3. **Visual Check:**
   - [ ] Display font renders on headings
   - [ ] Mobile drawer looks good
   - [ ] New cards match existing style

---

## Summary

| Task | Component | Priority |
|------|-----------|----------|
| 1 | Display font for headings | P2 |
| 2 | Cmd+K search shortcut | P1 |
| 3 | Mobile filter drawer | P2 |
| 4 | Content collections for hooks/commands/agents | P1 |
| 5 | Hooks gallery page | P1 |
| 6 | Commands gallery page | P1 |
| 7 | Agents gallery page | P1 |
| 8 | Navigation for all artifact types | P1 |
| 9 | Quick copy install command | P2 |
| 10 | Skill comparison view | P3 |

**Recommended execution order:** 4 → 5 → 6 → 7 → 8 → 2 → 3 → 1 → 9 → 10

Start with content infrastructure (Task 4) since Tasks 5-8 depend on it.
