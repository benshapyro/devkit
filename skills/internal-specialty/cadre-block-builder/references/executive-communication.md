# Executive Communication Patterns

Language patterns and frameworks for client-facing block documentation.

---

## Core Principles

**Outcome-Focused**: "What you'll get" not "What we'll do"
**Business Impact**: Revenue, efficiency, risk reduction
**Plain English**: No jargon, no technical details
**Conservative Promises**: Under-promise, over-deliver
**Flexibility Built In**: "Typically ranges" not hard commitments

---

## Framing Outcomes

### ❌ Activity-Focused (Internal)
"We'll conduct stakeholder interviews, map current processes, and create requirements documentation."

### ✅ Outcome-Focused (Client)
"You'll get validated requirements signed off by all key stakeholders, giving you confidence we're building the right solution."

---

### ❌ Technical Detail (Internal)
"Configure OAuth 2.0 authentication, implement API rate limiting logic, and build data transformation pipeline."

### ✅ Business Value (Client)
"Your Salesforce and HubSpot will sync automatically in real-time, eliminating manual data entry and ensuring your sales team always has current information."

---

## Outcome Verbs

**Use these**: Get, Achieve, Gain, Reduce, Eliminate, Enable, Unlock, Improve
**Avoid these**: Implement, Configure, Build, Develop, Code, Deploy

### Strong Outcome Statements
- "Reduce manual data entry by 80%"
- "Enable real-time visibility into customer status"
- "Eliminate sync errors between systems"
- "Gain confidence in data accuracy"
- "Unlock insights from previously siloed data"

---

## Flexibility Language

### When Discussing Timeline

**❌ Hard Commitment**: "This will take exactly 8 weeks"
**✅ Flexible Range**: "Typically ranges from 6-10 weeks depending on data complexity"

**❌ Absolute**: "We'll deliver on March 15"
**✅ Conditional**: "Target completion in mid-March, with exact date confirmed after discovery phase"

### When Discussing Scope

**❌ Fixed Feature List**: "You'll get features X, Y, and Z"
**✅ Outcome-Based**: "You'll be able to automate your lead routing, with specific rules we'll define together in discovery"

**❌ Technical Spec**: "RESTful API with JSON responses"
**✅ Business Capability**: "Your systems will communicate automatically, no manual data transfer needed"

### When Discussing ROI

**❌ Optimistic**: "This will save you 20 hours per week"
**✅ Conservative**: "Based on similar clients, teams typically save 12-16 hours per week"

**❌ Definitive**: "You'll see 300% ROI"
**✅ Range-Based**: "Similar implementations have delivered 200-350% ROI within 6 months"

---

## Handling Unknowns

### Discovery Needed

**Template**: "We'll evaluate [options] during discovery and recommend the best approach based on your specific [constraints/needs]."

**Example**: "We'll evaluate whether to build custom or use a pre-built connector during discovery and recommend the best approach based on your data volume and budget."

### Dependency on Client

**Template**: "Timeline depends on [specific client input/resource], which we'll coordinate during kickoff."

**Example**: "Timeline depends on how quickly we can get staging environment access from your IT team, which we'll coordinate during kickoff."

### Risk Disclosure

**Template**: "In our experience, [potential issue] can occur. We'll [mitigation] to minimize impact."

**Example**: "In our experience, legacy system APIs can be poorly documented. We'll start with an API audit to validate feasibility before committing to real-time sync."

---

## Resource Request Framing

### ❌ Demanding Tone
"We need VP Sales to commit 5 hours per week."

### ✅ Collaborative Tone
"To ensure we build exactly what your team needs, we'd love VP Sales to spend about 1 hour weekly reviewing progress with us."

---

### ❌ Technical Requirements
"Must provide database credentials and API keys by Week 1."

### ✅ Business Context
"To get started quickly, we'll need access to your systems. We'll work with your IT team during kickoff to coordinate the right level of access."

---

## Success Indicator Language

### ❌ Internal Metric
"Unit test coverage >80%"

### ✅ Business Outcome
"All features tested and validated by your team before launch"

---

### ❌ Technical Measure
"API response time <200ms"

### ✅ User Experience
"System responds instantly to user actions, no noticeable delays"

---

### ❌ Vague
"Users are happy with the system"

### ✅ Measurable
"80% of users complete training and log in within first week"

---

## Decision Gate Phrasing

### Template (Client Version)
"**Decision Point**: We'll review [deliverable] together and decide whether to [proceed/adjust/pause]."

### Examples

**After Discovery**:
"**Decision Point**: We'll present our findings and recommended approach. You'll decide whether to move forward with the full build or start with a simpler pilot."

**Mid-Build**:
"**Decision Point**: We'll demo the work-in-progress. If you're happy with the direction, we'll continue. If you want changes, we'll adjust the plan together."

**Before Launch**:
"**Decision Point**: Your team will test everything in a safe environment. We'll only launch to production once you're confident it's ready."

---

## Phase/Month Naming

### ❌ Technical Names
- "Infrastructure Setup Phase"
- "API Development Sprint"
- "Database Migration"

### ✅ Outcome-Focused Names
- "Foundation & Setup"
- "Build & Integrate"
- "Test & Refine"
- "Launch & Enable"
- "Optimize & Scale"

---

## Common Phrases to Avoid

**Avoid**: "Technical debt," "Refactoring," "Schema," "Endpoint," "Middleware"
**Use**: Plain English equivalents or business outcomes

**Avoid**: Absolute guarantees ("will," "definitely," "guaranteed")
**Use**: Confidence-appropriate language ("typically," "expect to," "based on similar projects")

**Avoid**: Blaming client ("Your team didn't provide...")
**Use**: Collaborative framing ("We'll work together to...")

---

## Block Overview Templates

### Integration Project
```
## Overview
We'll connect your [System A] and [System B] so data flows automatically 
between them. This eliminates manual data entry, reduces errors, and ensures 
your teams always have current information. Based on similar integrations, 
clients typically save 10-15 hours per week.
```

### Custom Application
```
## Overview
We'll build a custom [tool/portal/dashboard] that enables your team to 
[key capability]. This streamlines [current manual process] and provides 
[business value]. Similar applications have delivered [conservative ROI range] 
within [timeframe].
```

### Strategy Engagement
```
## Overview
We'll work with your team to evaluate [problem/opportunity] and recommend 
the best path forward. You'll get a clear strategy document with specific 
recommendations, ROI projections, and an implementation roadmap. This gives 
you confidence in making the right investment decisions.
```

---

## Deliverable Descriptions

### ❌ Technical Artifact
"API integration code with error handling"

### ✅ Business Value
"Working integration with automatic error notifications so issues get resolved quickly"

---

### ❌ Document-Focused
"Requirements specification document"

### ✅ Outcome-Focused
"Validated requirements signed off by all stakeholders, ensuring we build what you need"

---

### ❌ Technical Deliverable
"Test suite with 95% code coverage"

### ✅ Client Benefit
"Comprehensive testing completed, giving you confidence everything works correctly"

---

## Tone & Voice

**Professional but Accessible**: Like talking to a smart colleague, not a textbook

**Confident but Humble**: We know what we're doing, but acknowledge unknowns

**Collaborative not Prescriptive**: "We'll work together to..." not "We'll do X and you'll do Y"

**Transparent about Risks**: Surface issues early, don't hide complexity

**Conservative on Promises**: Under-promise so we can over-deliver

---

## Examples: Before & After

### Example 1: Integration Block

**Before (Internal Style)**:
```
Month 1: Technical Discovery
- API documentation review
- Authentication mechanism analysis  
- Data schema mapping
- Rate limit testing
Deliverable: Technical specifications document
```

**After (Client Style)**:
```
Month 1: Foundation & Planning
**What You'll Get**: Clear plan for connecting your systems with all 
technical questions answered.

**Key Activities**:
- We'll map exactly how data should flow between systems
- Your team confirms what data fields matter most
- We'll validate technical feasibility

**Deliverables**: Integration plan document you can review with your IT team

**What We Need From You**: IT Lead available 2-3 hours for technical questions
```

---

### Example 2: Custom Development Block

**Before (Internal Style)**:
```
Month 2-3: Feature Development
- Build user authentication module
- Implement CRUD operations for entities
- Create responsive UI components
- Set up CI/CD pipeline
```

**After (Client Style)**:
```
Month 2-3: Build Core Features
**What You'll Get**: Working application with your top-priority features, 
tested and ready for your team to review.

**Key Activities**:
- Build the features we prioritized together in discovery
- Your team provides feedback on early versions
- We refine based on your input

**Deliverables**: Demo-able application you can test with real users

**What We Need From You**: Product Owner available 1 hour weekly to review 
progress and provide direction
```

---

## Using This Guide

1. **Write internal version first** with technical details
2. **Transform to client version** using these patterns
3. **Read it aloud** - if it sounds like jargon, simplify
4. **Test with non-technical person** - can they understand value?
5. **Check for flexibility language** - no absolute commitments

Remember: Clients care about outcomes, not activities. Frame everything in terms of business value they'll receive.
