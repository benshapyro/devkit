# Employee-to-Client Onboarding

**Purpose:** Generate operational onboarding documentation for team members joining active client delivery teams.

**Audience:** Engineers, managers, and other delivery team members who need operational context to execute effectively

**Output:** 15-25 page operational onboarding doc (markdown format)

---

## Overview

This methodology creates actionable onboarding documentation that enables delivery team members to:
- Understand what we're committed to deliver (contract essentials)
- Know who the client is and how they operate (business context)
- Identify key stakeholders and how to work with them (people & relationships)
- Navigate the client's technology landscape (systems they'll use)
- Focus on critical pain points they're helping solve (priorities)
- Execute immediately (logistics, meetings, first week actions)

**Key Difference from Strategic Onboarding:**
- **Strategic (Type 1):** Full discovery synthesis, risk assessment, patterns, strategic decisions → 30-50 pages
- **Operational (Type 2):** Essential context for execution, immediate priorities, practical guidance → 15-25 pages

---

## The 8-Step Onboarding Process

Follow these steps sequentially to create comprehensive operational onboarding documentation.

### Step 1: Contract Essentials (Streamlined)

**Goal:** Extract operational commitments - what they need to know to contribute, not full strategic analysis.

**Focus Areas:**
- Payment structure (monthly value, total value, timing)
- Delivery framework overview (pillars/phases at high level)
- Key deliverable counts (8 CustomGPTs, 25 prompts, etc.)
- Timeline (start/end dates, key milestones)
- Monthly obligations (business reviews, recurring commitments)

**What to Skip:**
- Detailed contract language analysis
- Legal provisions and termination clauses
- Renewal mechanics (unless relevant to their work)
- Pricing negotiation history

**Output Format:**
```markdown
## Contract Overview

### Payment Structure
- Monthly: $X/month for Y months
- Total: $Z
- Payment Terms: [Timing]
- Initial Payment: [If applicable]

### [Framework Name] (e.g., Four-Pillar Framework)

#### Pillar 1: [Name]
[1-2 sentence description]
- Key deliverable counts
- Timeline

[Repeat for all pillars/phases]

### Monthly Obligations
- [Business reviews, check-ins, etc.]
```

**Search Strategy:**
- "contract signed schedule A payment"
- "[Client] deliverables framework pillars"
- Focus on Schedule A or SOW sections

### Step 2: Client Business Context

**Goal:** Give team member enough business understanding to make good decisions and contribute intelligently.

**Extract:**
- **Organization Profile:** Legal structure, mission, location, team size, key metrics
- **Business Model:** How they make money (revenue streams, pricing, volumes)
- **Target Market:** Who they serve, geographic scope, company size
- **Strategic Transformation:** What's changing, why, where they're heading

**What Matters:**
- Numbers (revenue, team size, customers, etc.)
- How their business actually works (not just what they say they do)
- Strategic shifts in progress (affects our work)
- Cultural context (mission, values, operating principles)

**Output Format:**
```markdown
## Client Business Context

### Organization Profile
**Basic Facts:**
- Legal Structure: [Corp/LLC/Nonprofit]
- Mission: [One-liner]
- Location: [HQ city/state]
- Team Size: [Total with breakdown]
- Key Metrics: [Revenue, customers, etc.]

### Business Model & Revenue
**Revenue Streams:**
- [Stream 1]: $X ([Description])
- [Stream 2]: $Y ([Description])

**Target Market:**
- [Who they serve]
- [Geographic scope]
- [Company size range if B2B]

### Strategic Transformation
[2-3 sentences on major changes underway that affect our work]
```

**Search Strategy:**
- "[Client] business model revenue"
- "[Client] organization profile team"
- "[Client] strategic transformation vision"

### Step 3: Key Stakeholders

**Goal:** Help team member know who to talk to, what each person cares about, and how to interact effectively.

**For Each Key Stakeholder:**
- **Name & Role:** Title, decision authority, responsibilities
- **Status:** Champion/Skeptic/Neutral/Capacity-Constrained
- **Key Concerns:** What keeps them up at night related to our work
- **Key Quote:** Representative statement that captures their perspective
- **Your Interaction:** How to work with them (meeting style, communication preferences, sensitivities)

**Priority Stakeholders:**
1. Executive sponsor/decision maker (always include)
2. Day-to-day contact (primary liaison)
3. Technical lead (IT/engineering contact)
4. End users (if they'll be heavily involved)

**Output Format:**
```markdown
## Key Stakeholders

### [Name] - [Title]

**Role:** [What they do, decision authority]  
**Authority:** [Budget, technical, strategic decisions]  
**Status:** [CHAMPION/SKEPTIC/etc] - [Brief explanation]

**Key Concerns:**
- [Concern 1]
- [Concern 2]

**Key Quote:**  
*"[Representative quote]"*

**Your Interaction:**
- [Communication preferences]
- [Meeting style]
- [Sensitivities to be aware of]
- [Best practices for working with them]

---
```

**What to Include:**
- 3-6 key stakeholders (executives, primary contacts, technical leads)
- Contributors/end users as a group if relevant (not individually)

**What to Skip:**
- Full org chart
- Stakeholders not relevant to delivery work
- Detailed psychological profiles (keep practical)

**Search Strategy:**
- "[Client] [Stakeholder name]"
- "[Client] decision maker sponsor"
- "[Client] technical contact IT"

### Step 4: Technology Landscape

**Goal:** Help team member understand what systems exist, what works/doesn't, and what they'll actually interact with.

**Extract:**
- **Current Systems:** Inventory with purpose, pain level, status
- **Technical Constraints:** Budget, preferences (off-the-shelf vs custom), past failures
- **Integration Landscape:** What connects to what (or doesn't)
- **Replacement Candidates:** Systems being considered for replacement
- **Tools They'll Use:** Systems the team member will directly interact with

**Output Format:**
```markdown
## Technology Landscape

### Current Systems

| System | Purpose | Pain Level | Status | Notes |
|--------|---------|------------|--------|-------|
| [System 1] | [Purpose] | [HIGH/MEDIUM/LOW] | [Status] | [Key context] |
| [System 2] | [Purpose] | [HIGH/MEDIUM/LOW] | [Status] | [Key context] |

### Technical Constraints & Preferences
**[Constraint Category]:**
- [Specific constraint or preference]
- [Impact on our work]

### Integration Landscape
[Brief description of how systems connect or don't]

### Tools You'll Use
- **[System Name]:** [What you'll do with it]
- **[System Name]:** [What you'll do with it]
```

**What Matters:**
- Pain points (helps prioritize our work)
- Integration gaps (affects solution design)
- Budget constraints (affects tool selection)
- Past failures (explains current preferences)

**Search Strategy:**
- "[Client] technology stack systems"
- "[Client] tech pain points integration"
- "[Client] IT infrastructure tools"

### Step 5: Critical Pain Points

**Goal:** Help team member understand what problems they're helping solve and why it matters.

**Prioritization:**
- Lead with client's #1 stated priority
- Follow with evidence-based ranking (frequency in discovery, impact mentioned)
- 3-5 pain points maximum (operational focus, not exhaustive)

**For Each Pain Point:**
- **Evidence:** What proves this is a problem (quotes, data, frequency)
- **Impact:** What happens if not solved (business consequences)
- **Our Response:** What we're doing about it (our deliverables that address it)

**Output Format:**
```markdown
## Critical Pain Points

### 1. [Pain Point Name] (PRIORITY LEVEL)

**Evidence:**
- [Specific example or quote]
- [Data point or observation]
- [Frequency: mentioned in X sessions]

**Impact:**
- [Business consequence 1]
- [Business consequence 2]

**Client Quote:**  
*"[Supporting quote]"* - [Who said it]

**Our Response:**
- [What we're doing to help]
- [Deliverables that address this]
- [Quick wins or Phase 2 opportunities]

---
```

**What to Include:**
- Top 3-5 pain points relevant to our deliverables
- Clear connection between pain → our work → outcomes

**What to Skip:**
- Pain points outside our scope
- Theoretical issues without evidence
- Problems the client isn't concerned about

**Search Strategy:**
- "[Client] pain points challenges"
- "[Client] problems frustrations"
- "[Client] needs priorities"

### Step 6: Strategic Priorities & Opportunities

**Goal:** Help team member understand client goals and where high-value opportunities exist.

**Extract:**
- **Client-Stated Priorities:** What they told us matters most (ordered list)
- **Quick Wins:** Month 1-2 opportunities for early visible wins
- **Transformational Work:** Months 3-6 major deliverables
- **Phase 2 Indicators:** Signals of expansion opportunity

**Output Format:**
```markdown
## Strategic Priorities & Opportunities

### Client-Stated Priorities (In Order)
1. **[Priority 1]** - [Brief description]
2. **[Priority 2]** - [Brief description]
3. **[Priority 3]** - [Brief description]

### High-Value Opportunities Identified

**Quick Wins (Month 1-2):**
- [Opportunity with brief explanation]
- [Connection to client priorities]

**Transformational (Months 3-6):**
- [Major deliverable or initiative]
- [Expected impact]

**Phase 2 Expansion Indicators:**
- [Signal of potential expansion]
- [Estimated value range]
- [Client quote supporting expansion potential]
```

**What Matters:**
- Clear prioritization (helps team allocate effort)
- Connection to contract deliverables
- Phase 2 awareness (shapes how we approach work)

**Search Strategy:**
- "[Client] priorities goals objectives"
- "[Client] opportunities quick wins"
- "[Client] expansion Phase 2"

### Step 7: Engagement Logistics & Timeline

**Goal:** Ensure team member knows when things happen, who attends what, and when they're expected to contribute.

**Extract:**
- **Key Dates:** Contract milestones, major deliverables, blocked dates
- **Meeting Cadence:** Weekly, bi-weekly, monthly rhythms with attendees
- **Blocked Dates:** Client unavailability, holidays, events
- **Capacity Commitments:** How much time client committed per week
- **Deliverable Schedule:** Month-by-month what's due

**Output Format:**
```markdown
## Engagement Logistics & Timeline

### Key Dates & Milestones
**Contract Dates:**
- Start: [Date]
- Signed: [Date]
- End: [Date]

**[Month] Critical Dates:**
- **[Date]:** [Event/Milestone]
- **[Date]:** [Event/Milestone]
- **Blocked Dates:** [Unavailability]

### Meeting Cadence
**Weekly:** [Meeting name]
- Day/Time: [When]
- Duration: [How long]
- Attendees: [Who]
- Purpose: [What for]

**Bi-Weekly/Monthly:** [Repeat structure]

### Deliverable Schedule

**Month 1:**
- [ ] [Deliverable]
- [ ] [Deliverable]

**Month 2:**
- [ ] [Deliverable]

[Continue for engagement duration]

### Client Capacity
- Committed time: [X hours/week]
- Primary availability: [Days/times]
- Response expectations: [Typical turnaround]
```

**What Matters:**
- When team member needs to show up
- When deliverables are due
- When client is unavailable (plan around it)

**Search Strategy:**
- "[Client] schedule calendar meetings"
- "[Client] timeline deliverables"
- "[Client] availability capacity"

### Step 8: Immediate Action Items

**Goal:** Give team member clear first-week priorities so they can contribute immediately.

**Create Two Lists:**
1. **Your Priority Actions (This Week):** Individual's first tasks
2. **Team Priority Actions (This Week):** Shared team priorities they should be aware of

**Format:**
```markdown
## Immediate Action Items

### Your Priority Actions (This Week)
- [ ] [Specific action with clear outcome]
- [ ] [Specific action with clear outcome]
- [ ] [Specific action with clear outcome]

### Team Priority Actions (This Week)
- [ ] [Team action you should be aware of]
- [ ] [Team action you might support]
- [ ] [Team action affecting your work]

### First Month Focus
**Week 1-2:**
- [Focus area or deliverable]

**Week 3-4:**
- [Focus area or deliverable]
```

**Action Item Quality:**
- Specific (not "get familiar with client")
- Actionable (clear verb)
- Outcome-oriented (what's produced)
- Time-bound (this week, by Friday, etc.)

**Examples:**
- ✅ "Review Aileron contract Schedule A and identify all CustomGPT deliverables by Friday"
- ❌ "Learn about the client"
- ✅ "Attend Thursday 1pm check-in with Joni to understand Q1 priorities"
- ❌ "Meet with stakeholders"

---

## Quality Standards for Employee Onboarding

### Scannability (Critical for Operational Docs)

**Heading Hierarchy:**
- `##` for major sections (Parts 1-8)
- `###` for subsections (individual stakeholders, pain points)
- `####` for details (if needed)

**Visual Elements:**
- Tables for system inventories, deliverable schedules
- Checkboxes `[ ]` for all action items
- Bold for key terms and names
- Quotes in italics with attribution
- Short paragraphs (2-4 sentences)

### Quantification

Everything quantifiable should be quantified:
- ❌ "Large team" → ✅ "30-person team (17 FT, 13 contractors)"
- ❌ "Significant revenue" → ✅ "~$3.6M annual revenue"
- ❌ "Multiple deliverables" → ✅ "8 CustomGPTs, 25 prompts, 7 training sessions"

### Actionability

Every section should enable action:
- Contract Essentials → Know what we're delivering
- Stakeholders → Know how to communicate
- Pain Points → Know what problems to prioritize
- Logistics → Know when to show up
- Action Items → Know what to do first

### Completeness (No TBDs in Critical Sections)

**Must have complete information:**
- Contract deliverable counts
- Key stakeholder contact info
- Meeting schedule
- First week action items

**Can mark as TBD:**
- Optional reference materials
- Non-critical background
- Phase 2 speculation

---

## Template Structure

Use the template from `references/employee-to-client-template.md` which includes:

**Part 1: Contract Overview**
- Payment structure
- Delivery framework with key deliverable counts
- Monthly obligations

**Part 2: Client Business Context**
- Organization profile
- Business model & revenue
- Strategic transformation in progress

**Part 3: Key Stakeholders**
- 3-6 key people with interaction guidance
- Contributors as a group (if relevant)

**Part 4: Technology Landscape**
- Current systems inventory
- Technical constraints & preferences
- Tools the team member will use

**Part 5: Critical Pain Points**
- Top 3-5 pain points with evidence
- Impact and our response
- Connection to deliverables

**Part 6: Strategic Priorities & Opportunities**
- Client-stated priorities
- Quick wins and transformational work
- Phase 2 expansion indicators

**Part 7: Engagement Logistics & Timeline**
- Key dates and milestones
- Meeting cadence
- Deliverable schedule

**Part 8: Critical Success Factors**
- Do These Well (6-8 items)
- Avoid These Risks (6-8 items)

**Part 9: Immediate Action Items**
- Your priority actions (this week)
- Team priority actions (awareness)
- First month focus

**Part 10: Quick Reference**
- Key numbers table
- Deliverables count table
- Primary contacts
- Cultural keywords

---

## Search Strategy

### Contract & Deliverables
```
"[Client] contract signed schedule A"
"[Client] deliverables framework"
"[Client] payment monthly"
```

### Business Context
```
"[Client] business model revenue"
"[Client] organization team structure"
"[Client] strategic vision transformation"
```

### Stakeholders
```
"[Client] [Name of key person]"
"[Client] decision maker sponsor"
"[Client] primary contact"
```

### Technology & Pain Points
```
"[Client] technology stack systems"
"[Client] pain points challenges"
"[Client] priorities goals"
```

### Logistics
```
"[Client] schedule meetings cadence"
"[Client] timeline deliverables"
"[Client] availability blocked dates"
```

---

## Workflow Example

**User Request:** "Onboard Mike to the Aileron delivery team"

**Execution:**

1. **Detect Type 2:** Employee joining delivery team

2. **Search & Extract:**
   - Contract: Deliverable counts, timeline, framework
   - Discovery: Business model, stakeholders, tech stack
   - Intelligence: Pain points, priorities, logistics

3. **Synthesize (Operational Focus):**
   - Streamline contract to essentials
   - Profile 4-6 key stakeholders with interaction guidance
   - Identify 3-5 critical pain points
   - Extract top priorities and quick wins
   - Build meeting schedule and action items

4. **Generate Document:**
   - Use employee-to-client-template.md structure
   - 15-25 pages (leaner than strategic onboarding)
   - Heavy emphasis on logistics and actions
   - Scannable with tables, checkboxes, quotes

5. **Output:**
   ```markdown
   # [Client] - Employee Onboarding
   [15-25 page operational guide]
   ```

**Deliverable:** `/mnt/user-data/outputs/[client]_employee_onboarding_[date].md`

---

## Tools & Composition

### Primary Tools
- **project_knowledge_search:** Finding contracts, transcripts, stakeholder profiles, logistics
- **pdf skill:** Extracting deliverable counts and payment terms from contracts (quick extraction only)

### Different from Strategic Onboarding
- **Don't use:** Extensive cadre-os-synthesis (pattern analysis not needed for operational onboarding)
- **Don't use:** Deep risk assessment frameworks (keep to practical "do/avoid" lists)
- **Do use:** Practical extraction and clear presentation
- **Do use:** Stakeholder interaction guidance (this is critical for delivery teams)

---

## Common Mistakes to Avoid

### ❌ Too Strategic
Don't create a mini-version of strategic onboarding with:
- Full discovery synthesis
- Extensive pattern analysis
- Deep risk assessment matrices
- Theoretical frameworks

### ❌ Too Vague
Avoid generic guidance like:
- "Learn about the client"
- "Familiarize yourself with stakeholders"
- "Review project materials"

### ✅ Just Right - Operational & Actionable
Provide specific, actionable content:
- "8 CustomGPTs due, 2 per department, Months 2-6"
- "Joni prefers weekly written updates + meetings, not verbal-only"
- "Review Configio replacement options by Friday for Monday discussion"

---

## Key Differences: Strategic vs Employee Onboarding

| Aspect | Strategic (Type 1) | Employee (Type 2) |
|--------|-------------------|-------------------|
| **Audience** | Consultants owning strategy | Delivery team executing |
| **Length** | 30-50 pages | 15-25 pages |
| **Contract** | Full analysis, payment terms, provisions | Essentials only: deliverables, timeline |
| **Discovery** | Full synthesis, patterns, contradictions | Key facts, operational context |
| **Stakeholders** | Deep profiles, archetypes, politics | Interaction guidance, communication style |
| **Pain Points** | Prioritized analysis, evidence scoring | Top 3-5 with clear connection to work |
| **Risk** | Comprehensive assessment framework | Practical do/avoid lists |
| **Actions** | Strategic priorities, execution playbook | First week action items, meeting schedule |
| **Style** | Analysis + strategy + execution | Execution-focused, immediately useful |

---

**Last Updated:** December 9, 2025
