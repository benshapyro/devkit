# Discovery UX Redesign

> **For Claude:** Use superpowers:subagent-driven-development to implement this plan.

**Goal:** Make it easy and frictionless for non-technical users to discover, understand, and install skills

**Architecture:** Editorial/magazine visual refresh with curated Favorites section, two-dimensional filtering (role + task tags), and benefit-focused card copy

**Tech Stack:** Astro 5, React 18, Tailwind CSS v4

---

## Problem Statement

Current barriers for non-technical users:
1. **Too many choices** — 130 skills is overwhelming, no clear starting point
2. **Unclear value props** — Card descriptions are technical, users can't tell "will this help ME?"
3. **Don't know what skills ARE** — Concept is unfamiliar, need gentle onboarding

**Success metric:** Users find 2-3 skills that excite them and install something (spark excitement, drive adoption)

---

## Design Decisions

### Visual Direction: Editorial/Magazine

Chosen to create a distinctive, memorable experience that stands out from generic AI tool aesthetics.

**Typography:**
- Headlines: Plus Jakarta Sans (bold, dramatic sizing)
- Body: Inter (used sparingly)
- Size contrast: Hero text 4-5x larger than body

**Layout:**
- Break the grid intentionally for emphasis
- Generous whitespace
- Left-aligned content (editorial feel)
- Thin ruled lines to separate sections

**Color:**
- Emerald primary accent (keep existing)
- Warm secondary (cream/off-white) for contrast
- Mostly monochrome with emerald pops

**Details:**
- Subtle grain/noise texture (keep existing)
- Oversized stats as design elements
- Smooth, purposeful hover transitions

---

## Homepage Structure

### Hero Area
Keep existing hero, flows into Favorites section

### Favorites Section
Curated collection of 7 hand-picked skills displayed prominently

**Layout:**
```
┌─────────────────────────────────┬──────────┬──────────┐
│                                 │    ai-   │  brain-  │
│         CADRE-OS                │   art-   │ storming │
│      (large featured)           │generation│          │
│                                 │          │          │
├─────────────┬───────────────────┼──────────┼──────────┤
│  frontend-  │     prompt-       │presentat-│ product- │
│   design    │   engineering     │ion-compo-│ discovery│
│             │                   │   ser    │          │
└─────────────┴───────────────────┴──────────┴──────────┘
```

**Featured card (Cadre-OS):**
- 2x width, 2x height
- Larger typography, more detail
- Subtle gradient or glow

**Curated skills (6):**
| Skill | Appeal |
|-------|--------|
| ai-art-generation | Creative/visual |
| brainstorming | Planning/ideation |
| frontend-design | Designers & devs |
| prompt-engineering | AI fundamentals |
| presentation-composer | Everyone makes decks |
| product-discovery | Founders & PMs |

### Main Gallery Area
- Left sidebar: Two filter groups
- Main area: Skill cards with new design
- Progressive disclosure: Show ~20 initially, "Show all" button

---

## Filtering System

### Two Dimensions

**Role tags ("I am a..."):**
- Frontend Developer
- Backend Developer
- Full-Stack Developer
- AI/ML Engineer
- DevOps Engineer
- Digital Marketer
- Content Creator
- Salesperson
- Product Manager
- Designer
- Data Analyst

**Task tags ("I want to..."):**
- Write Code
- Debug Code
- Test Code
- Review Code
- Document
- Deploy
- Create Images
- Create Videos
- Create Presentations
- Write Emails
- Analyze Data
- Automate Tasks
- Learn & Research

### Filter Behavior
- Multiple roles selected = OR (match ANY)
- Multiple tasks selected = OR (match ANY)
- Role + Task combined = AND (must match at least one from each)
- Show count: "Showing 23 of 130 skills"

### Sidebar UI
- Collapsible sections for each dimension
- Clickable pill/chip for each tag
- Active filters shown as removable badges above gallery
- Clear all button

---

## Card Redesign

### Current Card
- Name
- Description (technical, 1-2 sentences)
- Group label

### New Card
- **Name** (largest, bold)
- **Tagline** (2-5 words, benefit-focused, slightly muted)
- **Role badges** (small pills)
- **Task badges** (small pills)
- Group label (smaller, secondary)

### Tagline Examples
| Skill | Tagline |
|-------|---------|
| test-driven-development | Write tests that pass |
| brainstorming | Ideas → actionable plans |
| systematic-debugging | Find bugs fast |
| ai-art-generation | Create stunning visuals |
| prompt-engineering | Master AI interactions |
| presentation-composer | Beautiful decks fast |
| product-discovery | Validate before you build |
| frontend-design | Distinctive, memorable UIs |

---

## Data Model Changes

### New SKILL.md Frontmatter Fields

```yaml
# Existing fields
name: skill-name
description: Full description...

# New fields
tagline: "2-5 word benefit statement"
roles:
  - Frontend Developer
  - Designer
tasks:
  - Create Images
  - Design UI
favorite: true  # Only for the 7 curated skills
```

### Migration Required
- Add `tagline` to all 121 skills
- Add `roles` (1-3) to all skills
- Add `tasks` (1-3) to all skills
- Mark 7 skills as `favorite: true`

---

## Implementation Tasks

### Phase 1: Data Layer
1. Update content.config.ts with new schema fields
2. Create role and task tag constants
3. Batch-tag all 121 skills (use Claude to assist)
4. Add taglines to all skills

### Phase 2: Visual Refresh
5. Update typography scale (dramatic hierarchy)
6. Add thin ruled lines component
7. Adjust spacing for generous whitespace
8. Create featured card variant

### Phase 3: Favorites Section
9. Create FavoritesSection component
10. Implement asymmetric grid layout
11. Style featured card (Cadre-OS)
12. Add section below hero

### Phase 4: Filtering System
13. Create role/task filter sidebar
14. Implement filter state management
15. Add active filter badges
16. Connect filters to gallery

### Phase 5: Card Redesign
17. Update SkillCard with tagline
18. Add role/task badge display
19. Adjust visual hierarchy

---

## Success Criteria

- [ ] Non-technical user can identify relevant skills within 30 seconds
- [ ] Favorites section creates immediate "spark" moment
- [ ] Filters reduce 130 skills to <20 for any role+task combo
- [ ] Cards communicate value without requiring click-through
- [ ] Design is memorable ("Would I remember this UI tomorrow?")

---

## References

- Frontend Design Skill: `/Users/bshap/.claude/skills/frontend-design/SKILL.md`
- Frontend UI Integration: `/Users/bshap/.claude/skills/frontend-ui-integration/SKILL.md`
- Current site: https://cadreai.github.io/devkit/
