---
name: onboarding
description: Generate comprehensive onboarding documentation for multiple scenarios - (1) Client Engagement Onboarding for consultants joining existing client projects, (2) Employee-to-Client Onboarding for team members joining delivery teams, (3) Employee-to-Pod Onboarding for new Cadre hires joining internal teams. Analyzes contracts, intelligence, and context to create actionable handoff documentation. Use when someone needs to be onboarded to a client engagement, a delivery team, or a Cadre pod. Trigger phrases include "onboard [person] to [client/team]", "create onboarding for [scenario]", "handoff documentation for [context]", "what do I need to know about [client] engagement".
---

# Onboarding

Generate comprehensive onboarding documentation for consultants, team members, and new hires across multiple scenarios.

## Purpose

Create actionable handoff documentation that enables incoming team members to:
- Understand what they're responsible for (deliverables, commitments, timeline)
- Grasp business context (who the client/team is, what they need)
- Execute effectively (how to win, what to avoid, immediate priorities)
- Access quick reference data (key facts, contacts, systems)

## Supported Onboarding Types

### Type 1: Client Engagement Onboarding
**When:** Consultant or strategist joining existing client engagement mid-stream  
**Audience:** Incoming Cadre consultant taking over or co-leading engagement  
**Output:** 30-50 page strategic client brief (markdown format)  
**Content:** Full strategic context - contracts, discovery intelligence, stakeholder dynamics, execution playbook, risk assessment  
**Triggers:** "Onboard me to [Client]", "Strategic handoff for [Client]", "What do I need to know about [Client] engagement"

### Type 2: Employee-to-Client Onboarding
**When:** Team member (engineer, manager, etc.) joining active client delivery team  
**Audience:** Delivery team members who need operational context to execute  
**Output:** 15-25 page operational onboarding doc (markdown format)  
**Content:** Contract essentials, business context, stakeholders, tech landscape, priorities, immediate actions  
**Triggers:** "Onboard [person] to [Client] team", "Employee onboarding for [Client]", "New team member joining [Client]"

### Type 3: Employee-to-Pod Onboarding
**When:** New hire or contractor joining Cadre internal team/pod  
**Audience:** New Cadre team members joining specific practice areas or delivery pods  
**Output:** 10-20 page pod onboarding guide (markdown format)  
**Content:** Pod mission, projects, team structure, tools, workflows, culture, first week priorities  
**Triggers:** "Onboard [person] to [Pod] team", "New hire onboarding", "Pod onboarding for [team name]"  
**Status:** Future implementation (references not yet built)

## Onboarding Type Detection

Use this decision logic to determine which onboarding type:

**Detection Pattern:**
```
1. Analyze user request for context clues:
   - Mentions "engagement", "account", "strategic", "taking over" → Type 1
   - Mentions "employee", "delivery team", "engineer", "joining project" → Type 2
   - Mentions "pod", "internal team", "new hire", "contractor" → Type 3

2. Check requester role/context:
   - Strategist/consultant + client context → Type 1
   - Engineer/manager + active engagement → Type 2
   - New employee + Cadre team → Type 3

3. If ambiguous, ask clarifying question:
   "I can help with onboarding. Are you:
   (1) A consultant joining a client engagement (strategic handoff)
   (2) A team member joining a client delivery team (operational onboarding)
   (3) A new hire joining a Cadre pod (internal team onboarding)"
```

**Type 1 Trigger Examples:**
- "Onboard me to the Hyperion engagement"
- "Create strategic handoff for CES"
- "I'm taking over the Aileron account, what do I need to know?"
- "Generate engagement brief for Sunroad"

**Type 2 Trigger Examples:**
- "Onboard Mike to the Aileron delivery team"
- "Create employee onboarding doc for new engineer joining Hyperion"
- "Sarah is joining CES project next week, onboard her"
- "We hired an AI Manager for Sunroad, onboard them"

**Type 3 Trigger Examples:**
- "Onboard new hire to Strategy pod"
- "Create onboarding doc for contractor joining Delivery team"
- "New team member starting Monday, onboard them to our pod"

## Routing Instructions

Once onboarding type is determined, use the appropriate reference file for detailed methodology:

### For Type 1: Client Engagement Onboarding

**Primary Reference:** `references/client-onboarding.md`

This contains the full 5-step strategic onboarding process:
1. Contract Analysis - Extract obligations, payment, deliverables
2. Discovery Synthesis - Business model, stakeholders, pain points, opportunities
3. Execution Planning - Month-by-month roadmap, success metrics
4. Risk Assessment - Critical success factors, failure modes, mitigation
5. Brief Generation - Comprehensive 4-part strategic document

**Supporting References:**
- `references/client-onboarding-template.md` - 4-part structure template
- `references/client-contract-extraction.md` - Advanced contract analysis
- `references/client-execution-planning.md` - Success metrics & risk frameworks

**Tools/Skills to Use:**
- project_knowledge_search (contracts, transcripts, intelligence)
- pdf skill (contract extraction)
- cadre-os-synthesis (pattern detection, prioritization)
- cadre-os-context (Client Brain, Discovery Catalog data)
- cadre-os-knowledge (stakeholder archetypes)

### For Type 2: Employee-to-Client Onboarding

**Primary Reference:** `references/employee-to-client-onboarding.md`

This contains the 8-step operational onboarding process:
1. Contract Essentials - Payment, deliverables, timeline (streamlined)
2. Client Business Context - Model, mission, key metrics
3. Key Stakeholders - Names, roles, contact preferences, working styles
4. Technology Landscape - Current systems, pain points, tools they'll use
5. Critical Pain Points - Prioritized challenges they'll help solve
6. Strategic Priorities - Client-stated goals and success metrics
7. Engagement Logistics - Meetings, cadence, blocked dates, capacity
8. Immediate Action Items - First week/month priorities

**Supporting Reference:**
- `references/employee-to-client-template.md` - Operational onboarding structure

**Tools/Skills to Use:**
- project_knowledge_search (contracts, transcripts, stakeholder profiles)
- pdf skill (contract extraction for essentials)
- Focus on actionable, operational content vs strategic analysis

### For Type 3: Employee-to-Pod Onboarding

**Status:** Not yet implemented. Ask user if this is needed urgently or can be deferred.

If needed, would include:
- Pod mission & charter
- Current projects & client portfolio
- Team structure, roles, strengths
- Tools & systems (Cadre tech stack)
- Workflows & processes
- Communication norms & meeting cadence
- First week priorities

## Shared Onboarding Principles

These principles apply to ALL onboarding types:

### Evidence Standards

**Quantification:**
- ❌ "significant revenue" → ✅ "~$3.6M annual revenue"
- ❌ "many visitors" → ✅ "15,000 annual visitors"
- ❌ "several coaches" → ✅ "7 business coaches, 7 leadership coaches"

**Citation:**
- ✅ "Quote: '...' — Chuck, Nov 22 session"
- ✅ "Evidence: 3+ sessions"
- ✅ "Source: Contract Section 2.3"
- ✅ "Confidence: HIGH (verified multiple sources)"

**Confidence Scoring:**
- HIGH: Verified by multiple sources or authoritative document (contract)
- MEDIUM: Single credible source, internally consistent
- LOW: Inferred, unverified, or contradictory evidence

### Quality Standards

**Actionability:**
- Use checkboxes [ ] for all action items
- Specific recommendations with rationale
- Risk/mitigation pairs ("Do this / Avoid that")
- Clear ownership ("Strategist priority" vs "Team priority")

**Scannability:**
- Clear heading hierarchy (## for major sections, ### for subsections)
- Bold for key terms and emphasis
- Tables for structured comparisons
- Short paragraphs (3-5 sentences max)
- Bullet points for lists of discrete items

**Completeness:**
- No TBD sections in critical areas (can mark non-critical as TBD)
- All key stakeholders profiled
- All contract deliverables accounted for
- Immediate actions defined for first week/month

### Layered Search Strategy

Use progressive search approach for comprehensive context gathering:

**Contract Materials:**
```
1. "[Client/Project] contract signed agreement schedule A"
2. "[Client] payment monthly deliverables services"
3. "MSA master services agreement [Client]"
4. Specific terms from initial search results
```

**Discovery & Intelligence:**
```
1. "[Client/Project] discovery transcript interview"
2. "[Client] intelligence findings session"
3. "[Stakeholder name] [Client]" (for specific people)
4. "[Client] business model revenue"
5. "[Client] technology stack systems"
6. "[Client] pain points challenges"
```

**Search Pattern:**
- Start broad to understand scope
- Drill into specifics (deliverables, pricing, timeline, people)
- Search by stakeholder names for targeted intelligence
- Cross-reference same topics across multiple sources

**Search Quality Indicators:**

Strong Results:
- Multiple documents per query
- Specific matches to contract language or stakeholder names
- Recent dates (signed contracts, latest transcripts)

Weak Results (adjust strategy):
- Zero results → Try synonyms ("agreement" vs "contract")
- Too many results → Add client name, narrow scope
- Wrong document type → Add "signed" or "final"

### Output Formatting

**Markdown Standards:**
- Use tables for structured comparisons (payment terms, tech stack)
- Use checkboxes [ ] for action items
- Use bold for key terms, not entire sentences
- Use heading levels consistently (no skipping levels)
- Include document metadata at top

**Insight Markers (for strategic context):**
- ⚡ **Surprise** - Information contradicting expectations
- 💡 **Client-Originated Opportunity** - Ideas client requested
- 🔄 **Pattern** - Themes appearing 3+ times across sources
- ⚠️ **Contradiction** - Conflicting information needing clarification
- 🔧 **Consultant-Identified Opportunity** - Solutions we're proposing

## Common Tools & Composition

### Primary Tools

**project_knowledge_search:**
- First tool to use for all onboarding types
- Search for contracts, transcripts, intelligence, stakeholder profiles
- Use layered search strategy above

**pdf skill:**
- Extract structured data from signed contracts
- Get exact payment terms, deliverable counts, dates
- Parse complex contract language into actionable commitments

### Composing with Other Skills

**cadre-os-synthesis:**
- Pattern detection across multiple discovery sessions
- Prioritization of pain points and opportunities
- Gap analysis in discovery coverage
- Use for Type 1 (strategic) onboarding

**cadre-os-context:**
- Access Client Brain (Google Docs narrative context)
- Query Discovery Catalog (Airtable structured findings)
- Pull existing stakeholder intelligence
- Use when available for all types

**cadre-os-knowledge:**
- Stakeholder archetype patterns (Champion, Skeptic, etc.)
- Consulting methodology framing
- Discovery dimension frameworks
- Use for Type 1 strategic analysis

**docx skill:**
- Generate Word document format if requested
- Preserve formatting and structure
- Optional enhancement to markdown output

## Workflow Summary

**User Request:**
"Onboard [person/me] to [client/team/pod]"

**Step 1: Detect Type** (use decision logic above)

**Step 2: Load Appropriate Reference**
- Type 1 → references/client-onboarding.md
- Type 2 → references/employee-to-client-onboarding.md
- Type 3 → references/employee-to-pod-onboarding.md

**Step 3: Execute Methodology** (from reference file)
- Follow step-by-step process for that onboarding type
- Use appropriate tools and searches
- Apply shared principles (evidence, quality, formatting)

**Step 4: Generate Output**
- Use template structure from corresponding template file
- Create comprehensive onboarding document
- Save to /mnt/user-data/outputs/[name]_onboarding_[type]_[date].md

**Step 5: Deliver**
- Present document link to user
- Highlight key sections or urgent items
- Offer to clarify or expand any section

## When NOT to Use This Skill

Don't use this skill for:
- **New client setup** (no contract or discovery yet) → Use cadre-os "New Client Setup" workflow
- **Quick status check** (brief update only) → Use cadre-os "Quick Client Brief" workflow
- **Client-facing deliverables** (strategy decks, reports) → Use cadre-os-deliverables
- **Discovery session prep** (preparing for upcoming call) → Use cadre-os-discovery

Use this skill specifically for **comprehensive handoff documentation** when someone needs complete context to join a team, take over work, or start executing.

## References

For detailed type-specific methodologies, see:
- **Client Engagement:** [references/client-onboarding.md](references/client-onboarding.md) - Full strategic onboarding process
- **Client Engagement Template:** [references/client-onboarding-template.md](references/client-onboarding-template.md) - 4-part structure
- **Contract Extraction:** [references/client-contract-extraction.md](references/client-contract-extraction.md) - Advanced contract analysis
- **Execution Planning:** [references/client-execution-planning.md](references/client-execution-planning.md) - Success metrics & risk frameworks
- **Employee-to-Client:** [references/employee-to-client-onboarding.md](references/employee-to-client-onboarding.md) - Operational onboarding (future)
- **Employee-to-Client Template:** [references/employee-to-client-template.md](references/employee-to-client-template.md) - Operational structure (future)
