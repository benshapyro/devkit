---
name: presentation-composer
description: Expert system for creating scientifically-optimized, strategically-structured presentations that drive decisions and action. Use when user needs to create, improve, or strategize any type of presentation including executive briefings, board decks, sales presentations, training materials, conference talks, monthly business reviews, or strategy consulting deliverables. Applies neuroscience-based frameworks (working memory limits, serial position effects), consulting methodologies (Pyramid Principle, SCR, McKinsey/BCG approaches), and proven story architectures to ensure maximum impact and retention.
tagline: "Beautiful decks fast"
roles:
  - Salesperson
  - Product Manager
  - Content Creator
tasks:
  - Create Presentations
favorite: true
outputType: document
examplePrompt: Create a board presentation for Q4 results
---

# Presentation Composer

Create presentations that transform audiences through strategic structure, cognitive science, and proven frameworks.

## Quick Workflow

Follow this 4-step process for any presentation:

1. **Analyze Context** → Understand audience, objective, constraints, success criteria
2. **Select Framework** → Choose story architecture based on objective and context
3. **Build Structure** → Use templates and components from assets/ with cognitive principles
4. **Validate Quality** → Run validation scripts and check against quality criteria

## Framework Selection

Use this decision tree to select the optimal framework:

```
PRIMARY OBJECTIVE?
├── DECISION NEEDED → Time Available?
│   ├── <30 min → Pyramid Principle
│   └── >30 min → SCR Framework
├── INSPIRATION NEEDED → Duarte's Resonate
├── EDUCATION NEEDED → Audience Expertise?
│   ├── Expert → NEURO Method
│   └── Mixed/Novice → TED 4-Step
└── ANALYSIS NEEDED → Stakeholder Type?
    ├── Board/Investors → Pyramid (McKinsey style)
    └── Market/Customers → SCR (BCG style)
```

**For complete framework details with examples**: `view references/frameworks.md`

### Quick Framework Reference

**Pyramid Principle** (Executive/Consulting)
- Start with conclusion/recommendation first
- Support with MECE arguments
- Action titles on every slide
- Best for: Board presentations, time-pressed executives

**SCR Framework** (Problem-Solving)
- **S**ituation → **C**omplication → **R**esolution
- Creates urgency through tension
- Best for: Business cases, project proposals, change initiatives

**Duarte's Resonate** (Inspirational)
- Oscillate between "what is" and "what could be"
- Include STAR moments (Something They'll Always Remember)
- Best for: Keynotes, vision presentations, transformation

**TED 4-Step** (Educational)
- Hook → Promise → Proof → Push
- Pattern interrupt in first 30 seconds
- Best for: Conference talks, thought leadership

**NEURO Method** (Science-Based)
- Numbers (3-4 max), Eye path (F/Z), Unity, Repetition, Order
- Leverages primacy/recency effects
- Best for: Complex information, data-heavy content

## Building Presentations

### Core Cognitive Principles (Always Apply)

These are non-negotiable neuroscience-based limits:

1. **Working Memory Limit**: 3-4 chunks maximum per slide
2. **Word Limit**: 30 words or less per slide (40% retention drop beyond this)
3. **Serial Position**: Critical messages in first 20% (primacy) or last 20% (recency)
4. **Cognitive Breaks**: Every 10-20 minutes to reset attention
5. **Channel Synchronization**: Visual and verbal must align (no reading different text)

**For detailed cognitive science principles**: `view references/cognitive-science.md`

### Using Slide Templates

Templates in `assets/slide-templates/` are pre-optimized for cognitive load:

**executive-summary.html**
- Optimized for primacy zone (first 20% of presentation)
- Maximum 3-4 key points (working memory limit)
- Action-oriented headline
- Copy: `cp assets/slide-templates/executive-summary.html working_dir/`

**data-slide.html**
- F-pattern layout for text-heavy content
- Single dominant visualization
- Annotation guides for key findings
- Source attribution in footer
- Copy: `cp assets/slide-templates/data-slide.html working_dir/`

**framework-slide.html**
- Z-pattern layout for visual flow
- Progressive disclosure support (build animations)
- 3-4 components maximum
- Conceptual framework focus
- Copy: `cp assets/slide-templates/framework-slide.html working_dir/`

**cta-slide.html**
- Optimized for recency zone (final 20% of presentation)
- Single specific ask
- 3-4 numbered next steps
- Timeline with ownership
- Copy: `cp assets/slide-templates/cta-slide.html working_dir/`

### Using Reusable Components

Components in `assets/components/` can be embedded into any slide:

**timeline.html**
- Horizontal timeline visualization
- 3-5 milestones maximum
- Progress indicators
- Customizable colors and labels

**comparison-table.html**
- Side-by-side comparison (2-3 items max)
- Visual hierarchy with icons
- Highlight recommendations
- Mobile-responsive

**metric-card.html**
- Single key metric display
- Trend indicator (up/down/stable)
- Context label and timeframe
- Color-coded for sentiment

**Usage pattern**: Copy component HTML into your slide template where needed, customize data values.

### Assembly Process

1. **Copy relevant template** to working directory
2. **Customize content** while maintaining constraints:
   - ≤30 words per slide
   - ≤4 key points
   - Headlines that tell story alone
3. **Apply visual design** principles (see references/visual-design.md)
4. **Embed components** as needed for data visualization
5. **Validate** with scripts before finalizing

## Visual Design System

### Layout Patterns

**F-Pattern** (Text-Heavy Slides)
- Users spend 69% of time on left side
- Place critical info top-left
- Use for: Lists, frameworks, analytical content
- See: references/visual-design.md section "F-Pattern"

**Z-Pattern** (Visual-Dominant Slides)
- Eyes follow: top-left → top-right → diagonal → bottom
- Position elements along this path
- Use for: Data visualizations, image-led slides
- See: references/visual-design.md section "Z-Pattern"

**For complete design system**: `view references/visual-design.md`

### Color Psychology (Quick Reference)

| Purpose | Color | Effect | Use Case |
|---------|-------|--------|----------|
| Detail/Analysis | Red accents | Heightened attention | Financial data, warnings |
| Creative/Strategic | Blue dominant | Enhanced creativity | Strategy, planning |
| Learning/Memory | Yellow highlights | 55-78% retention boost | Key concepts |
| Growth/Positive | Green elements | Positive association | Success metrics |
| Authority/Premium | Black/dark blue | Executive confidence | Board presentations |

**Rule**: 3-4 colors maximum, 60-30-10 ratio (60% dominant, 30% secondary, 10% accent)

## Context Adaptations

Different presentation contexts require specific optimizations:

**Virtual Presentations**
- Increase slide count 20% (faster pacing)
- Engagement element every 3-4 slides
- Larger fonts (assume small screens)
- More annotations (no laser pointer)
- Progress indicators throughout

**High-Stakes Presentations**
- Send pre-read 48 hours ahead
- Lead with recommendation (primacy)
- Prepare 3x backup slides
- Authority colors (black/dark blue)
- Practice with similar audience

**Time-Compressed Situations**
- Pyramid structure mandatory
- Maximum 3 key points total
- Visual-only support slides
- Details in leave-behind
- Skip middle if needed

**For complete adaptation guides**: `view references/context-adaptations.md`

## Quality Validation

### Automated Validation

Before finalizing, run the validation script:

```bash
python scripts/validate_presentation.py path/to/presentation.html
```

**Checks performed**:
- Word count per slide (≤30 words)
- Points per slide (≤4 points)
- Whitespace ratio (30-40% target)
- Color count (≤4 colors)
- Primacy/recency message placement
- F/Z pattern adherence
- Chart annotation presence

**Also run cognitive load check**:

```bash
python scripts/check_cognitive_load.py path/to/presentation.html
```

**Analyzes**:
- Information density per slide
- Cognitive break scheduling
- Channel conflict detection
- Working memory load per section

### Manual Quality Checklist

Before delivering any presentation, verify:

**Structure & Content**
- [ ] One big idea clearly defined and stated upfront
- [ ] Headlines tell complete story when read alone
- [ ] Key messages repeated 3x across presentation
- [ ] Most critical content in primacy zone (first 20%)
- [ ] Call-to-action in recency zone (final 20%)

**Cognitive Load**
- [ ] ≤30 words per slide
- [ ] ≤4 points per slide  
- [ ] ≤4 colors used consistently
- [ ] 30-40% whitespace maintained
- [ ] Cognitive breaks planned (every 10-20 min)

**Visual Design**
- [ ] F or Z pattern layouts applied
- [ ] Visual and verbal channels synchronized
- [ ] Color psychology applied appropriately
- [ ] Charts directly labeled (no legends)
- [ ] One message per chart/visual

**Story & Flow**
- [ ] Framework consistently applied
- [ ] Transitions between sections clear
- [ ] Examples support key messages
- [ ] Technical details in appendix/backup
- [ ] Success metrics defined

## Common Presentation Types

### Executive Summary (First Slide)

**Structure**:
- Compelling headline (not just topic name)
- 3-4 key findings/recommendations
- Most critical point first (primacy) or last (recency)
- Visual hook or metric
- Can exceed 30-word rule for this slide only

**Template**: Use `assets/slide-templates/executive-summary.html`

### Monthly Business Review

**Framework**: SCR or Pyramid Principle
**Key slides**:
1. Executive summary
2. Performance vs. targets (data-slide.html)
3. Key wins and challenges
4. Strategic initiatives update
5. Next month priorities (cta-slide.html)

**Length**: 10-15 core slides, 5-10 backup

### Sales Presentation

**Framework**: Problem → Solution → ROI → CTA
**Structure**: 
- Problem (red accents for urgency)
- Solution (green for positive)
- ROI (blue for trust)
- CTA (recency zone)
- Customer proof points spaced throughout

**Length**: 10-14 core slides, up to 30 with appendix

### Strategy Consulting Deck

**Framework**: Pyramid Principle
**Visual Style**: McKinsey (text/logic-driven) or BCG (visual-driven)
**Structure**:
- Recommendation upfront
- MECE supporting arguments
- Data-driven evidence
- Implementation roadmap
- Detailed backup slides (2-3x main deck)

**Length**: 15-25 core slides, 30-60 backup

## Advanced Techniques

### Progressive Disclosure

For complex concepts, build information incrementally:

1. Show framework empty
2. Add first component, explain
3. Add second component, show relationship
4. Complete framework
5. Show implications

**Implementation**: Use framework-slide.html with CSS animation classes

### Cognitive Break Strategies

**Every 10 minutes**: 30-second story or visual break
- Customer anecdote
- Relevant analogy
- Striking image
- Brief video clip

**Every 20 minutes**: 2-minute interactive element
- Poll or question
- Think-pair-share
- Quick discussion
- Hands-on demo

### Handling Q&A

**Preparation**:
- Create 3x more backup slides than main deck
- Number backup slides for reference
- Group by topic in appendix
- Practice likely questions

**During Q&A**:
- Park complex questions (prevent cognitive overload)
- Bridge back to key messages
- Use specific backup slide numbers
- Time-box to prevent fatigue

## Troubleshooting

### Issue: Presentation feels too long
**Solution**: 
- Check cognitive breaks (every 10-20 min)
- Move details to appendix
- Combine related slides
- Verify ≤4 points per slide

### Issue: Audience not engaging
**Solution**:
- Add interactive elements (every 3-4 slides for virtual)
- Strengthen primacy zone hook
- Add cognitive breaks
- Check channel synchronization (visual vs. verbal)

### Issue: Key messages not landing
**Solution**:
- Verify 3x repetition pattern
- Check primacy/recency placement
- Simplify language (≤30 words)
- Add concrete examples
- Use yellow highlights for key concepts

### Issue: Too complex/overwhelming
**Solution**:
- Run check_cognitive_load.py
- Break into multiple slides with progressive disclosure
- Reduce to 3-4 chunks per slide
- Add more whitespace (30-40% target)
- Remove extraneous information

## Resources Included

**references/**
- `frameworks.md` - Complete details on all 5 story frameworks with examples
- `cognitive-science.md` - Working memory, attention, serial position effects
- `visual-design.md` - F/Z patterns, color psychology, typography, chart selection
- `context-adaptations.md` - Virtual, high-stakes, time-compressed optimizations

**assets/slide-templates/**
- `executive-summary.html` - Primacy-optimized opening slide
- `data-slide.html` - F-pattern layout with visualization support
- `framework-slide.html` - Z-pattern layout for conceptual content
- `cta-slide.html` - Recency-optimized closing with next steps

**assets/components/**
- `timeline.html` - Horizontal timeline visualization (3-5 milestones)
- `comparison-table.html` - Side-by-side comparison (2-3 items)
- `metric-card.html` - Single metric with trend and context

**scripts/**
- `validate_presentation.py` - Automated quality checks (words, points, colors, layout)
- `check_cognitive_load.py` - Cognitive load analysis per slide and section

## Getting Started

**For a new presentation**:

1. Define objective and audience
2. Select framework using decision tree above
3. Read relevant framework details: `view references/frameworks.md`
4. Copy relevant templates from `assets/slide-templates/`
5. Build slides maintaining cognitive constraints
6. Validate with `python scripts/validate_presentation.py`
7. Review manual checklist before delivery

**For improving an existing presentation**:

1. Run `python scripts/validate_presentation.py existing.html`
2. Check violations and warnings
3. Apply fixes based on cognitive principles
4. Re-validate until passing all checks

**For learning the system**:

1. Read `references/cognitive-science.md` for foundation
2. Study `references/frameworks.md` for story structures  
3. Explore `references/visual-design.md` for design system
4. Review template code for implementation patterns
