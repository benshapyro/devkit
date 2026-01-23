# Client Engagement Onboarding

**Purpose:** Generate comprehensive strategic onboarding briefs for consultants joining client engagements.

**Audience:** Incoming Cadre consultant taking over or joining an engagement

**Output:** 30-50 page strategic onboarding brief (markdown format)

---

## Overview

This methodology creates actionable handoff documentation that enables incoming strategists to:
- Understand contractual obligations (what we're delivering)
- Grasp business context (who the client is, what they need)
- Execute strategically (how to win, what to avoid)
- Access quick reference data (key facts, contacts, deliverables)

## The 5-Step Onboarding Process

Follow these steps sequentially to create a comprehensive strategic onboarding brief.

### Step 1: Contract Analysis

**Goal:** Extract all contractual obligations, payment terms, and deliverables.

**Process:**

1. **Search for signed contract** using layered approach:
   - Broad: "contract signed agreement schedule A"
   - Specific: "payment monthly commencement deliverables"
   - Client name + "MSA" or "SOW" or "Schedule A"

2. **Extract from contract:**
   - **Payment structure**: Total value, monthly amount, payment timing, special terms
   - **Deliverables framework**: How services are organized (pillars, phases, workstreams)
   - **Specific deliverables**: Exact counts (e.g., "8 CustomGPTs", "7 training sessions")
   - **Timeline**: Start/end dates, key milestones, renewal terms
   - **Monthly obligations**: Recurring commitments like business reviews
   - **Special provisions**: Auto-renewal, termination clauses, scope boundaries

3. **Use pdf skill** for structured extraction from PDF contracts

4. **Organize by delivery framework** (pillars/phases/workstreams)

**Output Quality Standards:**
- Quantified deliverables (not "several" but "7 training sessions")
- Month-by-month breakdown when contract specifies timing
- Payment terms exact (not "around $80K" but "$81,000 over 6 months")

**Reference:** See `references/client-contract-extraction.md` for advanced contract analysis techniques

### Step 2: Discovery Synthesis

**Goal:** Synthesize all discovery intelligence into actionable context.

**Process:**

1. **Search for discovery materials:**
   - "discovery transcript interview stakeholder"
   - "intelligence findings session notes"
   - Client name + specific stakeholder names
   - "business model revenue pricing"

2. **Extract and synthesize:**
   - **Business Model & Revenue**: How they make money, pricing structure, key metrics, volumes
   - **Technology Stack**: Current systems, integration landscape, pain points, replacement candidates
   - **Key Stakeholders**: Name, title, role (Champion/Skeptic/etc), concerns, decision authority, key quotes
   - **Critical Pain Points**: Prioritized by evidence frequency, quantified impact when possible
   - **Strategic Opportunities**: Client-originated (💡) vs consultant-identified (🔧), DVF scoring when available
   - **Cross-Cutting Patterns**: ⚡ Surprises, 🔄 Themes (3+ mentions), ⚠️ Contradictions
   - **Timeline Constraints**: Blocked dates, weekly cadences, capacity windows

3. **Use cadre-os-synthesis** for pattern analysis across multiple sessions

4. **Query cadre-os-context** for existing Brain/Catalog data when available

5. **Apply stakeholder archetypes** from cadre-os-knowledge

**Evidence Standards:**
- Cite sources: "Quote: '...' — Source: Chuck unprompted in Nov 22 session"
- Count evidence: "Evidence: 3+ sessions", "Mentioned by 4 different stakeholders"
- Flag confidence: HIGH (verified multiple sources), MEDIUM (single source), LOW (inferred)
- Use insight markers: ⚡💡🔄⚠️🔧

**Cross-Reference Pattern:**
Search same topic across multiple transcripts to identify:
- Evolution in thinking (pricing changed from $48K to $60K)
- Contradictions that need clarification
- Patterns that strengthen from 1 mention → 3+ mentions
- Client-originated ideas (built-in buy-in opportunities)

### Step 3: Execution Planning

**Goal:** Create actionable month-by-month execution roadmap.

**Process:**

1. **Map contract deliverables to timeline**

2. **Identify Month 1 critical path** (sets tone for entire engagement)

3. **Define success metrics:**
   - Phase 1 success criteria (how we'll be judged)
   - Quick win targets (visible progress early)
   - Expansion indicators (Phase 2 conversion signals)

4. **Generate immediate actions:**
   - Strategist's priority actions (this week)
   - Team priority actions
   - Checkboxes for accountability

**Timeline Construction:**
- Week-by-week breakdown for Month 1 (most critical)
- Month-by-month for remaining engagement
- Flag blocked dates and scheduling constraints
- Note capacity commitments (e.g., "client commits 3-5 hours/week")

**Reference:** See `references/client-execution-planning.md` for detailed success metrics and risk assessment frameworks

### Step 4: Risk Assessment

**Goal:** Identify success factors and failure modes proactively.

**Process:**

1. **Generate "Do These Well" list (6-8 items):**
   - What will make this engagement succeed?
   - What does client value most?
   - What are the high-leverage activities?
   - Include rationale for each

2. **Generate "Avoid These Risks" list (6-8 items):**
   - What could cause engagement to fail?
   - What has gone wrong in similar engagements?
   - What are the scope creep dangers?
   - Include mitigation strategies

3. **Identify critical success factors:**
   - Deal-breaker issues ("Month 1 is make-or-break")
   - Relationship dynamics to preserve
   - Technical constraints to respect
   - Cultural sensitivities to honor

**Pattern Recognition:**
Look for patterns from discovery that signal risks:
- ⚠️ Contradictions → Need alignment conversations
- Implementation expectations > strategy scope → Scope management risk
- Past vendor failures → Need to differentiate our approach
- Capacity constraints → Resource allocation risk

**Reference:** See `references/client-execution-planning.md` for risk assessment methodology

### Step 5: Brief Generation

**Goal:** Synthesize all intelligence into structured, scannable document.

**Structure:** Use 4-part template from `references/client-onboarding-template.md`

#### Part 1: Contract Commitments (What We're Delivering)
- Payment structure
- Delivery framework (pillars/phases)
- Month-by-month deliverables
- Monthly/recurring obligations

#### Part 2: Discovery Intelligence (What We've Learned)
- Business model & revenue
- Technology stack
- Key stakeholders
- Critical pain points (prioritized)
- Strategic opportunities
- Cross-cutting patterns
- Timeline constraints

#### Part 3: Strategic Execution Plan (The Playbook)
- Month 1 critical path
- Success metrics
- Critical success factors (do/avoid)
- Immediate actions

#### Part 4: Quick Reference (The Cheat Sheet)
- Key numbers (revenue, team size, metrics)
- Key deliverables count
- Key contacts
- Tech stack inventory
- Cultural attributes

**Formatting Standards:**
- Use tables for structured comparisons
- Use checkboxes [ ] for action items
- Use bold for key terms and section headers
- Use insight markers (⚡💡🔄⚠️🔧) for visual scanning
- Include evidence citations in italics
- Quantify everything possible

**Document Metadata:**
```markdown
# [Client] Engagement Onboarding Brief
**Prepared by:** [Your name]
**Date:** [Current date]
**Contract Status:** [Signed/In negotiation/etc]
**Contract Value:** [Total $ amount]
**Engagement Duration:** [Timeline]
```

**Reference:** See `references/client-onboarding-template.md` for complete structure with examples

## Layered Search Strategy

Use this progressive search approach for comprehensive context gathering:

### Contract Materials
```
1. "[Client] contract signed agreement schedule A"
2. "[Client] payment monthly commencement deliverables services"
3. "MSA master services agreement [Client] effective date"
4. "schedule A scope work deliverables [specific terms from initial search]"
```

### Discovery Materials
```
1. "[Client] discovery transcript interview"
2. "[Client] intelligence findings session"
3. "[Stakeholder name] [Client]" (for specific people)
4. "[Client] business model revenue pricing"
5. "[Client] technology stack systems tools"
6. "[Client] pain points challenges problems"
```

**Pattern:**
- Start broad to understand scope
- Drill into specifics (deliverables, pricing, timeline)
- Search by stakeholder names for targeted intelligence
- Cross-reference same topics across multiple sources

### Search Quality Indicators

**Strong Results:**
- Multiple documents per query
- Specific matches to contract language
- Recent dates (signed contracts, latest transcripts)
- Stakeholder names appear

**Weak Results (adjust strategy):**
- Zero results → Try synonyms ("agreement" vs "contract", "CustomGPT" vs "AI tools")
- Too many results → Add client name, narrow date range
- Wrong document type → Add "signed" or "final" or "v2"

## Quality Standards

Every onboarding brief must meet these standards:

### Quantification
- ❌ "significant revenue" 
- ✅ "~$3.6M annual revenue"
- ❌ "many visitors"
- ✅ "15,000 annual visitors"
- ❌ "several coaches"
- ✅ "7 business coaches, 7 leadership coaches"

### Evidence
- ✅ "Evidence: 3+ sessions"
- ✅ "Quote: '...' — Chuck, unprompted"
- ✅ "Source: Contract Section 2.3"
- ✅ "Confidence: HIGH (verified by finance team)"

### Actionability
- ✅ Checkbox lists for actions
- ✅ Specific recommendations with rationale
- ✅ Risk/mitigation pairs
- ✅ "Do this / Avoid that" format

### Scannability
- ✅ Clear hierarchy with ### and #### levels
- ✅ Bold for emphasis on key terms
- ✅ Tables for structured data
- ✅ Emoji markers for visual scanning
- ✅ Short paragraphs (3-5 sentences max)

## Advanced Techniques

### Multi-Source Triangulation

When you find contradictory information:

1. Note the contradiction explicitly: ⚠️
2. List all sources with dates
3. Identify which is most recent or authoritative
4. Flag for clarification in immediate actions

**Example:**
```
⚠️ **Bundle pricing contradiction:**
- Oct 29 session: "$48K/year at $4K/month"
- Nov 22 session: "$60K/year at $5K/month" 
- Contract: References "$5K/month" in payment schedule

**Resolution:** $60K/year is current (contract matches Nov update)
**Flag:** Understand what drove pricing change from $48K → $60K
```

### Insight Marker Usage

- ⚡ **Surprise**: Information that contradicts expectations or assumptions
- 💡 **Client-Originated Opportunity**: Ideas the client specifically requested or suggested
- 🔄 **Pattern**: Themes that appear 3+ times across sources
- ⚠️ **Contradiction**: Information that conflicts and needs clarification
- 🔧 **Consultant-Identified Opportunity**: Solutions we're proposing

### Cultural Intelligence Extraction

Look for phrases that reveal organizational culture:
- "We want to be challenged, not validated" → Growth mindset
- "As much as we can do off the shelf" → Custom code trauma
- "Human-centered organization supported by AI" → Values preservation
- "Ready for it to be blown up" → Transformation willingness

These become "Cultural Attributes" in Quick Reference section.

## Workflow Example

**User Request:** "Onboard me to the Aileron engagement"

**Skill Execution:**

1. **Search contracts:**
   - "Aileron contract signed schedule A"
   - Extract: $81K/6 months, 4-pillar framework, 8 GPTs, 25 prompts, etc.

2. **Search discovery:**
   - "Aileron discovery transcript"
   - "Aileron Joni Chuck Michael"
   - Synthesize: Business model, tech stack, pain points, opportunities

3. **Analyze patterns** (use cadre-os-synthesis):
   - Cross-session themes
   - Prioritized challenges
   - Risk indicators

4. **Generate brief:**
   - Part 1: Contract obligations
   - Part 2: Discovery context
   - Part 3: Execution playbook
   - Part 4: Quick reference

5. **Output:**
   ```markdown
   # Aileron Engagement Onboarding Brief
   [40-page strategic document with all synthesis]
   ```

**Deliverable:** `/mnt/user-data/outputs/[client]_strategic_onboarding_[date].md`

## Tools & Composition

### Primary Tools
- **project_knowledge_search**: Finding contracts, transcripts, intelligence documents
- **pdf skill**: Extracting structured data from signed contracts

### Composing with Other Skills
- **cadre-os-synthesis**: Pattern detection, prioritization, gap analysis
- **cadre-os-context**: Client data from Brain and Discovery Catalog (when available)
- **cadre-os-knowledge**: Stakeholder archetypes, methodology framing
- **docx skill**: Generating final brief document (if Word format requested)

## References

- **Template:** [client-onboarding-template.md](client-onboarding-template.md) - Complete 4-part structure with examples
- **Execution Framework:** [client-execution-planning.md](client-execution-planning.md) - Success metrics, risk assessment methodology
- **Contract Playbook:** [client-contract-extraction.md](client-contract-extraction.md) - Advanced contract analysis techniques
