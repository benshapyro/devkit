# Brand UI Reference

Detailed UI component specifications and examples based on official Cadre AI Brand Guidelines v1.0.

## Contents

1. [Color Palette](#color-palette-official)
2. [Buttons](#buttons)
3. [Cards](#cards)
4. [Forms](#forms)
5. [Navigation](#navigation)
6. [Tags & Badges](#tags--badges)
7. [Section Patterns](#section-patterns)
8. [Writing Examples](#writing-examples)
9. [Design Examples](#design-examples)
10. [Decision Trees](#decision-trees)
11. [Common Mistakes](#common-mistakes)

## Color Palette (Official)

**Primary:**
- Warm Black: `#0C0407` — Primary text, buttons, headlines
- Coral Red: `#DB4545` — Primary accent, CTAs, highlights, badges

**Secondary:**
- Secondary Blue: `#08749B` — Supporting CTAs, links, accents
- Strong Blue: `#034377` — Professional contexts, trust elements

**Text:**
- Body Text: `#6E7191`
- Muted Text: `#A1A1A1`

**Backgrounds:**
- Warm White: `#FAF9F6` — Primary background
- Cream: `#F2EFE4` — Hero sections, features
- White: `#FFFFFF` — Cards, surfaces
- Dark: `#242424` — Footer, dark sections

**Borders:**
- Standard: `#E5E2D8`
- Subtle: `rgba(0, 0, 0, 0.10)`

---

## Buttons

### Primary Button (Black)

```css
.button-primary {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 16px;
  
  background-color: #0C0407;
  color: #FFFFFF;
  border: none;
  border-radius: 52px;
  
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 500;
  line-height: 1;
  
  cursor: pointer;
  transition: all 350ms ease;
}

.button-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.button-primary:disabled {
  background-color: #A1A1A1;
  cursor: not-allowed;
}
```

**Variants:**
- Large CTA: `padding: 26px 38px; border-radius: 48px;`
- Small: `padding: 8px 12px; font-size: 14px;`

### Primary Button (White)

```css
.button-white {
  padding: 10px 16px;
  background-color: #FFFFFF;
  color: #000000;
  border: 1px solid rgba(0, 0, 0, 0.10);
  border-radius: 52px;
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.10);
  
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 500;
}
```

### Accent Button (Red)

Use sparingly for high-visibility CTAs:

```css
.button-accent {
  background-color: #DB4545;
  color: #FFFFFF;
  /* Same structure as primary */
}

.button-accent:hover {
  background-color: #c43d3d;
  transform: translateY(-2px);
}
```

### Text Button

```css
.button-text {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 0;
  background: none;
  border: none;
  color: #0C0407;
  font-size: 16px;
  font-weight: 500;
  transition: color 200ms ease;
}

.button-text:hover {
  color: #DB4545;
}

/* Arrow icon moves on hover */
.button-text:hover .icon {
  transform: translateX(4px);
}
```

### Button Rules
- One primary button per view maximum
- Never two accent buttons adjacent
- Border radius: 36px - 52px (pill shape)
- Transition: 350ms ease

---

## Cards

### Standard Card

```css
.card {
  display: flex;
  flex-direction: column;
  max-width: 386px;
  padding: 20px - 30px;
  
  background-color: #FAF9F6;
  border: 1px solid rgba(0, 0, 0, 0.10);
  border-radius: 16px;
  box-shadow: 0 28px 32px rgba(0, 0, 0, 0.03);
  
  transition: all 350ms ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.08);
}
```

**Structure:**
```html
<article class="card">
  <div class="card-image">
    <img src="..." alt="..." />
    <span class="card-badge">Category</span>
  </div>
  <div class="card-content">
    <h3 class="card-title">Title</h3>
    <p class="card-description">Description...</p>
    <div class="card-meta">Author • Date</div>
  </div>
</article>
```

**Sub-elements:**
```css
.card-image {
  margin: -20px -20px 16px -20px;
  border-radius: 16px 16px 0 0;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 256px;
  object-fit: cover;
}

.card-badge {
  position: absolute;
  top: 12px;
  left: 12px;
  padding: 5px 20px;
  background: #DB4545;
  color: #FFFFFF;
  font-size: 12px;
  font-weight: 500;
  border-radius: 6px;
}

.card-title {
  font-size: 24px;
  font-weight: 600;
  color: #0C0407;
  margin-bottom: 12px;
  line-height: 1.2;
  /* Max 2 lines */
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-description {
  font-size: 14px;
  color: #6E7191;
  line-height: 1.5;
  /* Max 3 lines */
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.card-meta {
  font-size: 14px;
  color: #A1A1A1;
}
```

### Stats/Number Card

```css
.card-stats {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  max-width: 368px;
  padding: 30px;
  
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.10);
  border-radius: 24px;
}

.card-stats-value {
  font-size: 48px;
  font-weight: 600;
  color: #0C0407;
  letter-spacing: -0.03em;
  line-height: 1.1;
  margin-bottom: 8px;
}

.card-stats-value .accent {
  color: #DB4545;
}

.card-stats-label {
  font-size: 16px;
  color: #6E7191;
  line-height: 1.5;
}
```

### Feature Card

```css
.card-feature {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 30px;
  
  background-color: #FAF9F6;
  border: 1px solid rgba(0, 0, 0, 0.10);
  border-radius: 16px;
}

.card-feature-icon {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #FFFFFF;
  border-radius: 16px;
  margin-bottom: 16px;
}

.card-feature-title {
  font-size: 20px;
  font-weight: 600;
  color: #0C0407;
  margin-bottom: 12px;
}

.card-feature-description {
  font-size: 16px;
  color: #6E7191;
  line-height: 1.75;
}
```

---

## Forms

### Text Input

```css
.form-group {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 24px;
}

.form-label {
  font-size: 16px;
  font-weight: 500;
  color: #0C0407;
}

.form-label .required {
  color: #DB4545;
}

.form-input {
  width: 100%;
  height: 54px;
  padding: 15px 20px;
  
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.13);
  border-radius: 8px;
  
  font-family: 'Inter', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #0C0407;
  
  transition: border-color 200ms ease;
}

.form-input::placeholder {
  color: #A1A1A1;
}

.form-input:focus {
  outline: none;
  border-color: rgba(0, 0, 0, 0.3);
}

.form-input:disabled {
  background: #F8F8F8;
  color: #A1A1A1;
  cursor: not-allowed;
}
```

**Error state:**
```css
.form-input.error {
  border-color: #DB4545;
}

.form-error {
  font-size: 14px;
  color: #DB4545;
  display: flex;
  align-items: center;
  gap: 6px;
}
```

### Textarea

```css
.form-textarea {
  /* Same as input plus: */
  min-height: 130px;
  padding: 15px 20px;
  resize: vertical;
  line-height: 1.5;
}
```

---

## Navigation

### Header

```css
.header {
  position: sticky;
  top: 0;
  z-index: 100;
  
  display: flex;
  align-items: center;
  justify-content: space-between;
  
  height: 72px;
  padding: 32px 24px;
  max-width: 1200px;
  margin: 0 auto;
  
  background: #FFFFFF;
  border-bottom: 1px solid rgba(0, 0, 0, 0.10);
}

.header-logo {
  width: 131px;
  height: auto;
}

.header-nav {
  display: flex;
  align-items: center;
  gap: 32px;
}

.header-nav-link {
  font-size: 16px;
  font-weight: 500;
  color: #0C0407;
  text-decoration: none;
  transition: color 200ms ease;
}

.header-nav-link:hover,
.header-nav-link.active {
  color: #DB4545;
}
```

### Footer

```css
.footer {
  background: #000000;
  padding: 64px 24px 28px;
  color: #FFFFFF;
}

.footer-grid {
  display: grid;
  grid-template-columns: 2fr repeat(3, 1fr);
  gap: 48px;
  max-width: 1200px;
  margin: 0 auto 48px;
}

.footer-logo {
  width: 131px;
  height: auto;
  margin-bottom: 16px;
}

.footer-description {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
  line-height: 1.6;
  max-width: 280px;
}

.footer-nav-title {
  font-size: 14px;
  font-weight: 600;
  color: #FFFFFF;
  margin-bottom: 16px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.footer-nav-link {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: color 150ms ease;
}

.footer-nav-link:hover {
  color: #FFFFFF;
}

.footer-bottom {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 28px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  max-width: 1200px;
  margin: 0 auto;
}

.footer-copyright {
  font-size: 14px;
  color: rgba(255, 255, 255, 0.5);
}
```

### Dropdown Menu

```css
.dropdown-menu {
  position: absolute;
  top: calc(100% + 12px);
  left: 50%;
  transform: translateX(-50%);
  
  min-width: 200px;
  padding: 8px;
  
  background: #FFFFFF;
  border: 1px solid rgba(0, 0, 0, 0.10);
  border-radius: 12px;
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.10);
}

.dropdown-item {
  display: block;
  padding: 12px 16px;
  border-radius: 8px;
  font-size: 14px;
  color: #6E7191;
  text-decoration: none;
}

.dropdown-item:hover {
  background: rgba(0, 0, 0, 0.04);
  color: #0C0407;
}
```

---

## Tags & Badges

### Category Badge

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: 5px 20px;
  
  background: #DB4545;
  color: #FFFFFF;
  border-radius: 6px;
  
  font-size: 12px;
  font-weight: 500;
}
```

### General Tag

```css
.tag {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  
  background: rgba(0, 0, 0, 0.05);
  border-radius: 6px;
  
  font-size: 12px;
  font-weight: 500;
  color: #0C0407;
}
```

### Hero Tag (Pill)

```css
.tag-pill {
  padding: 4px 12px;
  background: #FFFFFF;
  border-radius: 100px;
  font-size: 12px;
  font-weight: 500;
}
```

---

## Section Patterns

### Hero Section

```css
.hero {
  padding: 96px 24px;
  background: linear-gradient(180deg, #F2EFE4 0%, #FFFFFF 100%);
  text-align: center;
}

.hero-container {
  max-width: 840px;
  margin: 0 auto;
}

.hero-subtitle {
  font-size: 14px;
  font-weight: 500;
  color: #0C0407;
  margin-bottom: 16px;
}

.hero-title {
  font-size: 60px;
  font-weight: 400;
  letter-spacing: -1.8px;
  line-height: 110%;
  color: #0C0407;
  max-width: 712px;
  margin: 0 auto 24px;
}

.hero-title .accent {
  color: #DB4545;
}

.hero-description {
  font-size: 16px;
  color: #6E7191;
  line-height: 175%;
  max-width: 535px;
  margin: 0 auto 32px;
}

.hero-actions {
  display: flex;
  gap: 18px;
  justify-content: center;
}

/* Hero image container */
.hero-image {
  margin-top: 60px;
  padding: 12px;
  background: #FFFFFF;
  border: 1px solid #DEDEDE;
  border-radius: 28px;
  box-shadow: 0 16px 16px rgba(0, 0, 0, 0.07);
}

.hero-image img {
  width: 100%;
  border-radius: 16px;
}
```

### Content Section

```css
.section {
  padding: 96px 24px;
  margin-bottom: 96px;
}

.section-container {
  max-width: 1200px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  max-width: 712px;
  margin: 0 auto 50px;
}

.section-label {
  font-size: 16px;
  font-weight: 500;
  color: #0C0407;
  margin-bottom: 20px;
}

.section-title {
  font-size: 48px;
  font-weight: 400;
  letter-spacing: -1.44px;
  line-height: 120%;
  color: #0C0407;
  margin-bottom: 16px;
}

.section-title .accent {
  color: #DB4545;
}

.section-description {
  font-size: 16px;
  color: #6E7191;
  line-height: 175%;
  max-width: 628px;
  margin: 0 auto;
}
```

### Two-Column Layout

```css
.two-col {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 64px;
  align-items: center;
}

.two-col-text {
  max-width: 550px;
}

.two-col-image {
  max-width: 585px;
}

.two-col-image img {
  width: 100%;
  border-radius: 20px;
  border: 1px solid rgba(0, 0, 0, 0.10);
}
```

### Card Grids

```css
.grid-2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 28px;
}

.grid-3 {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 24px;
}

.grid-4 {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 28px;
}
```

---

## Quick Reference

### Most-Used Values

| Element | Value |
|---------|-------|
| Primary text | `#0C0407` |
| Body text | `#6E7191` |
| Accent | `#DB4545` |
| Background | `#FAF9F6` |
| Card bg | `#FFFFFF` or `#FAF9F6` |
| Border | `rgba(0, 0, 0, 0.10)` |
| Card radius | 16px - 20px |
| Button radius | 36px - 52px (pill) |
| Tag radius | 6px |
| Shadow (default) | `0 28px 32px rgba(0, 0, 0, 0.03)` |
| Shadow (hover) | `0 12px 36px rgba(0, 0, 0, 0.08)` |
| Hover transform | `translateY(-4px)` |
| Transition | 350ms ease |

### Typography Quick Reference

| Element | Size | Weight | Color |
|---------|------|--------|-------|
| H1 | 72px | 400 | `#0C0407` |
| H2 | 60px | 400 | `#0C0407` |
| H3 | 48px | 400 | `#0C0407` |
| H4 | 36px | 400 | `#0C0407` |
| Body | 16px | 400 | `#6E7191` |
| Body Small | 14px | 400 | `#6E7191` |
| Caption | 12px | 400 | `#A1A1A1` |

### Spacing Scale

```
4px   8px   12px   16px   20px   24px   32px   48px   64px   96px
```

### Responsive Breakpoints

```
Mobile: < 479px
Tablet: 768px - 991px
Desktop: 992px+

Mobile adjustments:
- H1: 72px → 32px
- H2: 60px → 28px
- H3: 48px → 24px
- Grids: collapse to 1 column
- Section padding: 96px → 64px
```
# Examples Reference

Do/don't patterns within the Cadre brand. Use when unsure if something is on-brand.

## Table of Contents
1. [Writing Examples](#writing-examples)
2. [Design Examples](#design-examples)
3. [Decision Trees](#decision-trees)
4. [Common Mistakes](#common-mistakes)

---

## Writing Examples

### Headlines

✓ **Good:**
```
Close your books in days, not weeks.
Win more bids with better margins.
Stop drowning in spreadsheets.
```

❌ **Bad:**
```
Unlock Your Business Potential with AI
The Future of Work is Here
Transformative Digital Solutions
```

**Why:** Good headlines lead with specific outcomes. Bad headlines are generic buzzwords.

---

### Service Descriptions

✓ **Good:**
```
The problem: You're spending 40+ hours per month on invoice 
reconciliation and still missing things.

What we do: We build automated reconciliation that matches 
invoices against POs in real-time and flags exceptions instantly.

Timeline: 8-12 weeks
Investment: $150-200K
```

❌ **Bad:**
```
Cadre AI offers best-in-class AI discovery services that 
leverage our proprietary methodology to unlock transformative 
opportunities across your organization.

Contact us to learn more.
```

**Why:** Good descriptions are specific about problem, solution, timeline, and cost. Bad descriptions are vague buzzwords with no useful information.

---

### Email Subject Lines

✓ **Good:**
```
Your invoice process (saw the CFO roundtable comment)
Week 3 update: reconciliation system in staging
Quick question about the NetSuite integration
```

❌ **Bad:**
```
Partnership Opportunity 🚀
Touching Base
Quick Question
```

**Why:** Good subjects are specific and give context. Bad subjects are generic or salesy.

---

### Email Openings

✓ **Good:**
```
Sarah,

Saw your post about month-end close taking too long.
```

```
Quick update on where we are:
```

❌ **Bad:**
```
Hi there!

I hope this email finds you well! My name is Ben and I'm 
reaching out from Cadre AI, a leading AI strategy firm.
```

```
I wanted to take a moment to provide you with an update 
on our ongoing engagement.
```

**Why:** Good openings are direct and get to the point. Bad openings are filler.

---

### LinkedIn Posts

✓ **Good:**
```
Most AI "strategy" is really just a list of places AI 
could theoretically go.

That's not strategy. That's a shopping list.

[Useful framework follows]
```

❌ **Bad:**
```
🚀 Excited to announce that Cadre AI has been named an 
Official OpenAI Service Partner! 🎉

This incredible milestone reflects our team's dedication 
to excellence!

#AI #OpenAI #DigitalTransformation #Innovation #Grateful
```

**Why:** Good posts offer useful insight. Bad posts are self-congratulatory with hashtag spam.

---

### Proposal Executive Summaries

✓ **Good:**
```
You're spending 40+ hours per month on invoice reconciliation. 
Your month-end close takes 12 days.

We'll fix this.

Expected outcomes:
• Month-end close: 12 days → 5 days
• Manual reconciliation: 40 hrs → 8 hrs/month

Investment: $180,000
Timeline: 12 weeks
```

❌ **Bad:**
```
Cadre AI is pleased to submit this proposal for AI-enabled 
process optimization services. As a leading AI strategy firm, 
we bring deep expertise in leveraging cutting-edge technologies 
to drive transformative business outcomes.

We look forward to the opportunity to partner with you on 
this exciting initiative.
```

**Why:** Good summaries lead with client pain and specific outcomes. Bad summaries lead with self-promotion and vague promises.

---

## Design Examples

### Button Pairing

✓ **Good:**
```
[Get started]  [Learn more →]
   primary        text link

[Get started]  [See pricing]
   primary       tertiary
```

❌ **Bad:**
```
[Get started]  [Contact us]
   primary        primary     ← Two primaries, no hierarchy

[Get started]  [Learn more]
    accent         accent     ← Two accents, overwhelming

[Start] [Learn] [Watch] [Read]
                              ← Too many options
```

---

### Color Usage

✓ **Good:** 60% neutrals / 30% text / 10% accent
```
┌──────────────────────────────────────┐
│  [Warm white background]             │
│                                      │
│  Section Title                       │ ← Black
│                                      │
│  Body text explaining something      │ ← Gray
│  important about this topic.         │
│                                      │
│  [Get started]                       │ ← Red accent (sparingly)
│                                      │
└──────────────────────────────────────┘
```

❌ **Bad:** Red everywhere
```
┌──────────────────────────────────────┐
│  [RED BACKGROUND]                    │
│                                      │
│  SECTION TITLE                       │
│                                      │
│  [RED BUTTON]  [RED BUTTON]          │
│                                      │
└──────────────────────────────────────┘
```

---

### Card Layout

✓ **Good:**
```
┌────────────────────────────┐
│ [Image - 16:9]             │
│ ┌────────┐                 │
│ │Category│                 │ ← Badge top-left
│ └────────┘                 │
├────────────────────────────┤
│ Card Title                 │ ← 20px semibold
│                            │
│ Brief description that     │ ← 14px gray
│ gives context. Max 3 lines.│
│                            │
│ Author • Dec 17, 2024      │ ← 14px light gray
└────────────────────────────┘
```

❌ **Bad:**
```
┌────────────────────────────┐
│ ⭐ FEATURED ⭐              │ ← Cheesy
│ TITLE IN ALL CAPS          │ ← Hard to read
│ Dec 17, 2024 | Author      │ ← Metadata before content
│ Very long description that │
│ goes on forever without    │
│ any constraint...          │ ← Too long
│ [Image at bottom]          │ ← Wrong position
│ [CTA] [CTA] [CTA]          │ ← Too many CTAs
└────────────────────────────┘
```

---

## Decision Trees

### What button style should I use?

```
Is this the main action?
├─ Yes → Primary (black)
│        On dark background?
│        ├─ Yes → Primary (white) or Accent (red)
│        └─ No → Primary (black)
│
└─ No → Alternative to main action?
        ├─ Yes → Tertiary (outline)
        └─ No → Minor/supporting?
                ├─ Yes → Text link
                └─ No → Reconsider if needed
```

### Should I use a bullet list?

```
How many items?
├─ 1-2 → Write as prose, no list
├─ 3-5 → Maybe
│        Items parallel in structure?
│        ├─ Yes → List okay
│        └─ No → Rewrite or use prose
└─ 6+ → Group into categories with shorter lists
```

### What text color?

```
Headline or primary content?
├─ Yes → #0C0407 (black)
└─ No → Explanatory/supporting?
        ├─ Yes → #6E7191 (gray)
        └─ No → Metadata/caption?
                ├─ Yes → #A1A1A1 (light gray)
                │        Essential info?
                │        ├─ Yes → Use #6E7191 instead
                │        └─ No → #A1A1A1 okay
                └─ No → Needs emphasis?
                        ├─ Yes → #0C0407 or #DB4545 (sparingly)
                        └─ No → #6E7191
```

### Which content pattern?

```
What are you creating?
├─ Hero section → Outcome headline + how subheadline + single CTA
├─ Service description → Problem + what we do + deliverables + investment
├─ Case study → Metric headline + situation + actions + results + quote
├─ Email (sales) → Specific subject + why reaching out + one insight + low-commit CTA
├─ Email (update) → Milestone subject + done + next + needs + timeline
├─ LinkedIn → Contrarian insight or useful framework, no hashtag spam
└─ Proposal summary → Their pain + recommendation + outcomes + investment
```

---

## Common Mistakes

### Writing Mistakes

| Mistake | Example | Fix |
|---------|---------|-----|
| Leading with "we" | "We help companies..." | "You get..." |
| Empty superlatives | "Best-in-class solution" | Describe what makes it good |
| Passive voice | "Results were achieved" | "We achieved results" |
| Jargon stacking | "Leverage synergies to optimize" | "Use X to improve Y" |
| Missing specifics | "Significant improvements" | "40% reduction" |
| Hedging | "We might be able to help" | "We can help. Here's how." |
| Filler openings | "I hope this finds you well" | [Delete, start with purpose] |
| Generic CTAs | "Learn more", "Click here" | "See how it works", "Get started" |

### Design Mistakes

| Mistake | Fix |
|---------|-----|
| Multiple focal points | One primary focus per view |
| Random spacing | Use 8px grid consistently |
| Red everywhere | Max 10% accent color |
| Too many type sizes | Max 3 hierarchy levels per view |
| No white space | Let content breathe |
| Decoration without purpose | Every element serves a function |
| Two primary buttons | One primary, others tertiary or text |

### Voice Mistakes

| Sounds Like | Should Sound Like |
|-------------|-------------------|
| "We are pleased to inform you..." | "Here's what happened." |
| "Hey! Super excited to..." | "Good news:" |
| "This AMAZING opportunity..." | "This could help because..." |
| "We deliver value." | "We cut your close time by 60%." |
| "We think we might be able to..." | "We can do this. Here's proof." |
| "Leverage cutting-edge AI..." | "Use AI to..." |
| "Partner with you on this journey..." | "Work with you on this project." |

---

## Quick Checklist

### Before Publishing Writing
- [ ] Leads with outcome, not feature?
- [ ] Specific numbers/timeframes?
- [ ] No forbidden terminology?
- [ ] "You/your" more than "we/our"?
- [ ] 30-second comprehension test?

### Before Publishing Design
- [ ] One clear focal point?
- [ ] 60/30/10 color ratio?
- [ ] 8px grid spacing?
- [ ] Max one primary button?
- [ ] Text contrast passes?

### Brand Gut Check
- [ ] Sounds direct, rigorous, warm, confident?
- [ ] Would show to prospective client?
- [ ] Differentiates from generic consulting?
- [ ] Honest (no exaggeration)?
