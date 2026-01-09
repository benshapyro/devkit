# Insight Extraction Guide

How to identify and apply insight markers during debrief to surface high-value findings.

---

## Insight Markers

| Marker | Name | Meaning | Value |
|--------|------|---------|-------|
| ⚡ | Surprise | Contradicted an assumption we held | High learning value |
| 🔄 | Pattern | Theme mentioned 3+ times | Validates trend |
| ⚠️ | Contradiction | Conflicting statements | Needs clarification |
| 💡 | Opportunity | Unprompted solution idea from client | High buy-in potential |

---

## ⚡ Surprise Detection

### What Qualifies

A surprise is information that contradicts what we expected based on:
- Prior sessions with this client
- Industry norms
- Common assumptions
- Stated vs. actual behavior

### Detection Criteria

| Source of Assumption | Surprise Indicator |
|---------------------|-------------------|
| Prior session said X | This session reveals not-X |
| Industry typical is X | Client does Y instead |
| Stated goal was X | Actual priority is Y |
| Expected pain in X | Pain is actually in Y |
| Assumed they had X | They lack X |

### Examples

```
Prior session: "Our CRM is working great"
This session: "We've stopped using the CRM for forecasting"
→ ⚡ Surprise: CRM usage has degraded since last session

Industry norm: Sales teams prioritize pipeline
This session: "We focus more on customer retention than new sales"
→ ⚡ Surprise: Counter-typical sales strategy

Assumption: Executive sponsor is bought in
This session: "Leadership isn't sure this is the right timing"
→ ⚡ Surprise: Executive alignment weaker than assumed
```

### Application

Apply ⚡ to:
- Key findings that flip an assumption
- Information that requires strategy adjustment
- Facts that should inform future sessions

---

## 🔄 Pattern Detection

### What Qualifies

A pattern emerges when the same theme appears 3+ times:
- Within a single session (multiple mentions)
- Across sessions (different people say same thing)
- Across dimensions (shows up in process, technology, AND challenges)

### Detection Criteria

| Pattern Type | Threshold | Example |
|--------------|-----------|---------|
| Single session | 3+ mentions | "Approvals" mentioned 4 times |
| Cross-session | 2+ people | Sarah and Mike both cite "data quality" |
| Cross-dimension | 2+ dimensions | "Manual work" in Process AND Technology |

### Pattern Categories

| Category | What to Track |
|----------|---------------|
| Pain themes | Same problem repeatedly |
| System mentions | Same tool/system repeatedly |
| Department friction | Same handoff issue |
| Process bottlenecks | Same step causes delays |
| People dynamics | Same person/role mentioned |

### Examples

```
Session mentions:
- "The approval process takes forever" (minute 12)
- "We wait weeks for sign-off" (minute 28)
- "Getting VP approval is the bottleneck" (minute 41)
→ 🔄 Pattern: Approval delays (3 mentions)

Across sessions:
- CEO: "Data quality is our biggest issue"
- VP Ops: "We can't trust the numbers in our reports"
- Analyst: "I spend half my time cleaning data"
→ 🔄 Pattern: Data quality (3 stakeholders)
```

### Application

Apply 🔄 to:
- Challenges mentioned 3+ times (strong signal)
- Processes that multiple people cite as problematic
- Technology that comes up repeatedly
- Themes that span stakeholder levels

---

## ⚠️ Contradiction Detection

### What Qualifies

A contradiction occurs when:
- Same person says two conflicting things
- Different people give conflicting accounts
- Stated priority conflicts with behavior
- Official process differs from actual practice

### Detection Criteria

| Contradiction Type | Example |
|-------------------|---------|
| Self-contradiction | "We're customer-focused" but "We don't track NPS" |
| Cross-stakeholder | CEO says A, Manager says not-A |
| Say vs. Do | "Our top priority is X" but no resources on X |
| Policy vs. Practice | "Process is X" but "We actually do Y" |

### Examples

```
Same person:
- Minute 8: "Our team works well together"
- Minute 34: "There's constant friction between sales and ops"
→ ⚠️ Contradiction: Team cohesion — needs clarification

Different people:
- VP (last week): "Budget is approved and ready"
- Manager (today): "We're still waiting on budget confirmation"
→ ⚠️ Contradiction: Budget status unclear

Say vs. Do:
- Stated: "AI is our strategic priority"
- Reality: No AI budget, no AI hires, no AI projects
→ ⚠️ Contradiction: AI priority stated but not resourced
```

### Application

Apply ⚠️ to:
- Findings that require follow-up clarification
- Information that affects scope or approach
- Statements that warrant validation
- Areas where we need to dig deeper

**Action Required:** Every ⚠️ needs a follow-up plan

---

## 💡 Opportunity Detection

### What Qualifies

An opportunity is when the client unprompted:
- Suggests a solution idea
- Describes their ideal future state
- Identifies a specific change they want
- Proposes an approach or tool

### Why It Matters

Client-originated ideas have:
- Built-in buy-in (it's their idea)
- Validation of need (they've thought about it)
- Direction for solutions (they know what they want)
- Potential quick wins (they're ready to act)

### Detection Criteria

| Signal | Example Phrase |
|--------|---------------|
| Solution suggestion | "What if we could..." |
| Ideal state | "In a perfect world..." |
| Wish | "I wish we had..." |
| Specific ask | "We need something that..." |
| Vision | "Imagine if..." |

### Examples

```
"What if we could automatically route approvals based on deal size?"
→ 💡 Opportunity: Client suggests approval automation with tiered routing

"I wish we had a single view of the customer across all our systems"
→ 💡 Opportunity: Client wants unified customer view (360 dashboard)

"In a perfect world, the sales team wouldn't have to enter data twice"
→ 💡 Opportunity: Client identifies duplicate entry as target for automation
```

### Application

Apply 💡 to:
- Any unprompted solution idea from client
- Specific feature requests or wishes
- Described ideal future states
- Areas where client has clear vision

**Capture exactly:** Quote the client's words — their language matters for buy-in

---

## Marker Application Rules

### When Extracting

1. **Read through transcript/notes** looking for marker signals
2. **Tag as you go** — don't wait until the end
3. **One marker per insight** — choose the most relevant
4. **Include context** — what makes this significant

### Marker Priority

If an insight could have multiple markers, prioritize:

1. 💡 Opportunity (highest — actionable, client-owned)
2. ⚠️ Contradiction (needs resolution)
3. ⚡ Surprise (high learning value)
4. 🔄 Pattern (validation of known theme)

### Minimum Counts

For a typical 60-minute session, expect:
- ⚡ Surprises: 1-3
- 🔄 Patterns: 2-4
- ⚠️ Contradictions: 0-2
- 💡 Opportunities: 1-3

If you find none, dig deeper or flag as a thin session.

---

## Output Format

When reporting insights:

```markdown
## Key Insights

### ⚡ Surprises
- **CRM abandonment**: Team has stopped using CRM for forecasting despite prior positive feedback

### 🔄 Patterns
- **Approval delays**: Mentioned 4x — consistent theme across discussion
- **Data quality**: Third stakeholder to cite this as top issue

### ⚠️ Contradictions (Follow-up Needed)
- **Budget status**: VP says approved, Manager says pending — clarify with CFO
- **Team alignment**: Mixed signals on cross-functional collaboration

### 💡 Opportunities (Client Ideas)
- **Tiered approval routing**: "What if approvals auto-routed by deal size?"
- **Customer 360 view**: "I wish we had a single view across all systems"
```

---

## Linking Insights to Catalog

When creating Discovery Catalog records:

| Marker | Primary Table | Notes Field |
|--------|---------------|-------------|
| ⚡ | Challenges or appropriate dimension | Add "⚡ SURPRISE:" prefix in notes |
| 🔄 | Challenges (usually) | Add "🔄 PATTERN:" prefix in notes |
| ⚠️ | Challenges | Add "⚠️ CONTRADICTION:" prefix, create follow-up |
| 💡 | Solutions | Add "💡 CLIENT IDEA:" prefix |

This ensures insights are preserved and searchable in the Catalog.
