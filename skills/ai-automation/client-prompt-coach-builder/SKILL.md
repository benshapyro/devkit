---
name: client-prompt-coach-builder
description: Generates customized Prompt Engineering Coach instructions and user guides for any client by analyzing their project knowledge base, extracting context about industry/personas/tasks, and filling production-ready templates. Use when deploying prompt coaching to new clients or updating existing coaches.
---

# Client Prompt Coach Builder

Automates creation of client-specific Prompt Engineering Coach CustomGPTs by analyzing project KB and generating deployment-ready instructions + user guides.

## When to Use This Skill

| User Says | What to Do |
|-----------|------------|
| "Build a prompt coach for [Client]" | Full generation workflow |
| "Create prompt coach instructions for [Client]" | Generate CustomGPT instructions only |
| "Generate prompt coach guide for [Client]" | Generate user guide only |
| "Update [Client]'s prompt coach" | Analyze KB, ask what changed, regenerate |
| "What do I need to build a prompt coach?" | Show questionnaire, explain process |

## Process Overview

```
1. Analyze Client KB
   ↓
2. Extract Context (industry, personas, tasks, pain points)
   ↓
3. Ask Clarifying Questions (fill gaps)
   ↓
4. Generate CustomGPT Instructions (<8,000 chars)
   ↓
5. Generate User Guide (team documentation)
   ↓
6. Provide Deployment Checklist
```

**Time to complete**: 5-10 minutes with good KB, 10-15 minutes if sparse KB

## Step 1: Analyze Client KB

Search project knowledge for:

**Company Basics**:
- Company name (full legal name)
- Industry/sector
- Primary business description
- Company size (if mentioned)
- Key products/services

**Team & Personas**:
- Names and roles mentioned in documents
- Responsibilities and pain points
- Technical sophistication level
- Communication patterns (formal/casual)

**Common Tasks**:
- What work do they do with AI?
- Mentioned in transcripts, meeting notes, emails
- Proposal writing, analysis, communications, reporting, etc.
- Frequency and pain points

**Values & Culture**:
- What do they prioritize? (speed, quality, precision, simplicity)
- Communication style (professional, direct, friendly, casual)
- Technical vs traditional industry
- Change readiness (early adopters vs cautious)

**Pain Points**:
- Specific problems mentioned
- Time-consuming tasks
- Quality/consistency issues
- Workflow bottlenecks

## Step 2: Extract & Structure Context

Organize findings into:

```markdown
## Client Context Summary

**Company**: [Name]
**Industry**: [Industry]
**Business**: [1-2 sentence description]

**Key Personas** (3-4):
1. Name/Role | Primary Tasks | Pain Points
2. Name/Role | Primary Tasks | Pain Points
3. Name/Role | Primary Tasks | Pain Points

**Common Tasks** (5-7):
- Task 1
- Task 2
- Task 3...

**Technical Level**: [High-tech / Mixed / Low-tech]
**Communication Style**: [Professional / Friendly / Direct / Casual]
**Top Values**: [Speed, Quality, Precision, Simplicity]
**Confidence**: [High/Medium/Low based on KB completeness]
```

## Step 3: Ask Clarifying Questions

If confidence is MEDIUM or LOW, ask:

**For Company Basics**:
- "I found [X] about the company. Is this accurate?"
- "What's the best 1-2 sentence description of what they do?"

**For Personas** (critical):
- "I found mentions of [Names]. Are these key users? What are their roles?"
- "What are the top 3-4 user types I should optimize for?"
- "What specific pain points do [Name] and [Name] face?"

**For Tasks**:
- "I found these common tasks: [list]. Are there others I should include?"
- "Which of these is most frequent/highest priority?"

**For Culture**:
- "What's their communication style? (professional/friendly/direct)"
- "Technical team or more traditional industry?"
- "What do they value most: speed, quality, simplicity, or precision?"

**Pro tip**: For sparse KB, show what you found and ask "What am I missing?"

## Step 4: Generate CustomGPT Instructions

→ Read `templates/coach-instructions-template.md`
→ Read `references/industry-patterns.md` for domain-specific guidance
→ Read `references/tone-examples.md` for communication style matching

**Fill template with**:
- [CLIENT_NAME] → Full company name
- [INDUSTRY/BUSINESS] → Industry + what they do
- [5-7 COMMON TASKS] → From KB analysis
- [TECH LEVEL] → From culture analysis
- [VALUES] → Top 2 priorities
- [3-5 PAIN POINTS] → Specific issues with names
- [TONE] → Communication style
- [EXAMPLE PROMPT] → Domain-specific example
- [IMPROVED PROMPT] → Complete rewrite for their domain

**Character count check**: Must be under 8,000 characters for ChatGPT

**Quality checks**:
→ Read `references/validation-checklist.md`
- [ ] Company name appears throughout
- [ ] Industry context is specific
- [ ] 3+ real persona names included
- [ ] 5+ domain-specific tasks listed
- [ ] Example is from their actual work
- [ ] Tone matches their culture
- [ ] Under 8,000 characters

## Step 5: Generate User Guide

→ Read `templates/user-guide-template.md`

**Customize sections**:
1. **What is the Coach** (universal - no changes)
2. **When to Use** → Fill with their common tasks
3. **How to Use** (universal - no changes)
4. **Real [Client] Use Cases** → 3-4 persona examples with before/after
5. **Quick Reference** → 3 before/after for common tasks
6. **Getting Help** → Add contact name and channel

**Critical**: Persona use cases must include:
- Real name and role
- Specific pain point
- Vague prompt they might use
- Improved prompt with their terminology
- Quantified result (time/quality improvement)

## Step 6: Provide Deployment Checklist

Output:

```markdown
## Deployment Ready!

### Files Created:
1. **[Client]_PromptCoach_Instructions.md** (Ready for CustomGPT)
2. **[Client]_PromptCoach_UserGuide.md** (Share with team)

### Next Steps:
1. [ ] Review instructions for accuracy (2 min)
2. [ ] Test with 2-3 domain examples (5 min)
3. [ ] Deploy to ChatGPT workspace (2 min)
4. [ ] Share user guide with team (1 min)
5. [ ] Schedule 15-min demo with 2-3 power users
6. [ ] Set 2-week check-in for feedback

### Quick Deploy:
- CustomGPT: Settings → Create GPT → Paste instructions
- Name: "Prompt Engineering Coach"
- Share: [Client] workspace only

### Success Metrics (track after 2 weeks):
- 50-70% of team tries it
- 20-30% daily active users
- 2-3 Custom GPTs created
- 80%+ first-draft usability
```

## Common Patterns by Industry

→ Read `references/industry-patterns.md` for full details

Quick reference:

| Industry | Common Tasks | Values | Tone | Example Prompts |
|----------|--------------|--------|------|-----------------|
| Professional Services | Memos, reports, client comms | Quality, precision | Professional | Investment memos, legal briefs |
| Manufacturing | SOPs, quality reports, logs | Reliability, safety | Clear, direct | Procedures, incident reports |
| Healthcare | Documentation, care plans | Accuracy, compliance | Professional, compassionate | Visit notes, treatment plans |
| Technology | Docs, code, specs | Speed, innovation | Casual, collaborative | Technical docs, user stories |
| Real Estate | Analysis, valuations, reports | Precision, speed | Professional | Property analysis, LP updates |
| Sales/Marketing | Emails, content, campaigns | Speed, creativity | Friendly, energetic | Outreach, case studies |

## Examples Available

→ `examples/ces-example.md` — LED lighting company (CES)
→ `examples/hyperion-example.md` — Commercial real estate (Hyperion)

Use these as reference for:
- What level of detail to include
- How to write persona use cases
- Tone matching examples
- Before/after prompt examples

## Troubleshooting

### "KB is too sparse - not enough info"
1. Show what you found
2. Ask targeted questions (use Step 3 framework)
3. Prioritize persona/task info over company basics
4. Better to ask 5 good questions than generate generic output

### "Not sure about communication tone"
1. Read a few client emails/transcripts
2. Look for: formal language, jargon, sentence structure
3. Default to "Professional and practical" if unclear
4. Can always adjust after deployment

### "Client has multiple departments with different needs"
1. Start with most common use case
2. Note in deployment plan: "Consider department-specific variations"
3. Can generate multiple coaches later (Sales Coach, Ops Coach, etc.)

### "Generated instructions are over 8,000 chars"
1. Shorten example section (biggest culprit)
2. Combine similar pain points
3. Reduce persona descriptions to bullets
4. Keep all core methodology intact

## Anti-Patterns (What NOT to Do)

| Don't | Do Instead |
|-------|------------|
| Generate without KB search | Always search first, ask questions second |
| Use generic examples | Pull from their actual domain/work |
| Skip persona names | Real names = higher relevance = better adoption |
| Make up pain points | Use actual issues from KB or ask |
| Default to friendly tone for all | Match their culture (finance ≠ tech startup) |
| Over-customize methodology | Keep core coaching unchanged, customize context only |

## Quality Standards

**Good output has**:
✅ 3-4 real persona names with roles and pain points
✅ 5-7 specific tasks from their actual work
✅ Domain-specific example (not generic "write an email")
✅ Tone that matches their communication style
✅ Quantified results in use cases ("4 hours → 90 minutes")
✅ Under 8,000 characters for instructions

**Great output also has**:
✅ Industry-specific terminology in examples
✅ Reference to real tools/systems they use
✅ Before/after examples that feel authentic
✅ Clear connection between pain points and solutions

## Reference Files

| File | Purpose |
|------|---------|
| `templates/coach-instructions-template.md` | CustomGPT instructions template |
| `templates/user-guide-template.md` | Team documentation template |
| `templates/questionnaire-template.md` | What to ask if KB incomplete |
| `references/industry-patterns.md` | Common patterns by sector |
| `references/tone-examples.md` | Communication style matching |
| `references/validation-checklist.md` | Quality control checks |
| `examples/ces-example.md` | Full CES deployment reference |
| `examples/hyperion-example.md` | Full Hyperion deployment reference |

## Remember

**Goal**: Generate deployment-ready prompt coaches that feel custom-built, not templated.

**Success criteria**: Client team says "This gets our work" not "This is generic AI coaching."

**Time investment**: 5-10 min generation saves 4-6 hours of manual customization.
