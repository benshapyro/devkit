# Opportunity Categories Reference

Detailed signals and patterns for each MECE category.

## 1. Knowledge Retrieval

**What it solves:** Finding and synthesizing information from existing sources.

**Signals in discovery:**
- "Where do I find..."
- "Who knows about..."
- "I always have to ask [person] about..."
- "New hires take months to learn where things are"
- "The information exists but it's buried in..."
- "People keep asking the same questions"
- "Tribal knowledge" mentions
- Policy/procedure lookup friction

**Typical GPT solution:** Q&A bot with curated knowledge base, internal wiki assistant, policy lookup tool.

**Example opportunities:**
- Employee policy FAQ bot
- Product knowledge assistant
- Procedure lookup tool
- Onboarding knowledge guide

**Key success factors:**
- Quality of knowledge base curation
- Clear scope boundaries
- Confidence indicators on answers
- Escalation path when unsure

---

## 2. Content Generation

**What it solves:** Creating documents, communications, and materials that follow patterns.

**Signals in discovery:**
- "I write the same email every..."
- "Reports follow a standard template"
- "Copy-paste from previous versions"
- "Formatting takes forever"
- "Draft, review, revise cycle"
- "Everyone writes it differently"
- Mentions of templates, boilerplate, standard language

**Typical GPT solution:** Draft generator with templates, communication assistant, report builder.

**Example opportunities:**
- Meeting summary generator
- Proposal draft assistant
- Email template tool
- Status report builder
- Job description writer

**Key success factors:**
- Good examples/templates in knowledge base
- Clear tone and style guidelines
- Output format specification
- Human review expectation set

---

## 3. Analysis & Decision Support

**What it solves:** Processing information to generate insights or recommendations.

**Signals in discovery:**
- "I have to compare..."
- "Evaluating options takes..."
- "Need to weigh pros and cons"
- "Data is there but insights aren't obvious"
- "Decision criteria are complex"
- "Scoring/rating things manually"
- Mentions of analysis frameworks, rubrics, matrices

**Typical GPT solution:** Analysis assistant, decision framework tool, evaluation helper.

**Example opportunities:**
- Vendor comparison tool
- Risk assessment assistant
- Investment screening helper
- Candidate evaluation tool
- Market analysis assistant

**Key success factors:**
- Clear analysis framework
- Explicit criteria and weights
- Confidence levels on outputs
- Supporting evidence cited

---

## 4. Document Processing

**What it solves:** Extracting, summarizing, or transforming information from documents.

**Signals in discovery:**
- "Reading through documents to find..."
- "Extracting data from PDFs"
- "Summarizing long reports"
- "Comparing contract terms"
- "Pulling key points from..."
- "Manual data entry from documents"
- Mentions of review, extraction, abstraction

**Typical GPT solution:** Document summarizer, extraction tool, review assistant.

**Example opportunities:**
- Contract abstraction tool
- Meeting transcript summarizer
- Research paper digest
- Invoice data extractor
- Resume screening assistant

**Key success factors:**
- Code Interpreter enabled (mandatory)
- Clear extraction schema
- Output format specified
- Handling of edge cases

---

## 5. Process Guidance

**What it solves:** Walking users through multi-step workflows or procedures.

**Signals in discovery:**
- "The process has many steps"
- "People skip steps or do them wrong"
- "Checklist compliance is inconsistent"
- "How do I do X" questions
- "Depends on the situation"
- SOPs that aren't followed
- Training on procedures takes long

**Typical GPT solution:** Workflow guide, procedure assistant, checklist companion.

**Example opportunities:**
- New hire onboarding guide
- Incident response assistant
- Compliance checklist tool
- Project setup wizard
- Quality control guide

**Key success factors:**
- Complete process documentation
- Conditional logic handling
- Progress tracking capability
- Clear handoff points

---

## 6. Training & Enablement

**What it solves:** Teaching skills, explaining concepts, providing coaching.

**Signals in discovery:**
- "Training new people takes..."
- "Wish I had a coach for..."
- "Learning curve is steep"
- "Need to practice [skill]"
- "Explaining [concept] repeatedly"
- Onboarding duration concerns
- Skill gap mentions

**Typical GPT solution:** Training assistant, skill coach, concept explainer.

**Example opportunities:**
- Sales pitch practice coach
- Product training assistant
- Interview prep tool
- Skill development guide
- Concept explainer for [domain]

**Key success factors:**
- Good examples and scenarios
- Adaptive difficulty
- Feedback mechanisms
- Progress indicators

---

## Cross-Category Patterns

Some opportunities span categories. When this happens:
- Identify the **primary** category (where most value comes from)
- Note secondary benefits
- Consider if should be split into separate GPTs

**Common combinations:**
- Knowledge Retrieval + Process Guidance (FAQ that walks through steps)
- Document Processing + Analysis (Extract then analyze)
- Content Generation + Knowledge Retrieval (Generate using internal sources)

---

## Red Flags (Probably Not a Good GPT Opportunity)

- Requires real-time external data (consider API/Actions complexity)
- Needs to write back to systems (GPTs can't edit external files)
- Highly regulated output requiring human sign-off anyway
- Process changes frequently (maintenance burden)
- Edge cases dominate (hard to handle reliably)
- Success requires 99.9%+ accuracy (GPTs have error rates)
- No clear user who would adopt it
