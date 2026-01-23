---
name: ai-maturity-assessor
description: Conducts structured diagnostic assessments to evaluate an organization's AI transformation maturity across governance, fluency, prioritization, and production capabilities. Use when clients ask to "assess our AI readiness," "evaluate where we are in our AI journey," "create a transformation roadmap," "determine our AI maturity level," or need gap analysis before planning AI initiatives. Generates quantitative scores, identifies capability gaps, and produces customized 12-18 month transformation roadmaps with investment estimates and ROI projections.
---

# AI Maturity Assessor

This skill conducts comprehensive AI transformation maturity assessments based on OpenAI's four-phase deployment framework and industry research from McKinsey, Gartner, and Stanford HAI. It evaluates organizations across governance, fluency, prioritization, and production capabilities to identify the critical gaps preventing progression from experimentation (78% of organizations) to maturity (only 1% of organizations).

## Assessment Framework

The assessment evaluates four interconnected phases:

**Phase 1: Foundations** (Governance, Data Access, Executive Alignment)
- Executive sponsorship and strategic alignment
- Data infrastructure and access policies
- Governance frameworks and decision rights
- Risk management and compliance readiness

**Phase 2: AI Fluency** (Literacy, Champions, Learning Networks)
- Workforce AI literacy and skill levels
- Champion networks and knowledge sharing
- Training programs and learning infrastructure
- Cultural readiness for experimentation

**Phase 3: Scope & Prioritize** (Capture Ideas, Systematic Evaluation)
- Use case identification and intake processes
- Prioritization frameworks and decision criteria
- Backlog management and resource allocation
- Reusability pattern recognition

**Phase 4: Build & Scale** (Iterative Development, Continuous Evaluation)
- Cross-functional team effectiveness
- Evaluation and measurement discipline
- Production deployment capabilities
- Continuous improvement practices

## Workflow

### 1. Conduct Assessment Interview

Use the structured questionnaire from `references/assessment_framework.md`:
- Ask questions systematically across all four phases
- Capture evidence and examples for each capability area
- Probe for specific artifacts, processes, and metrics
- Note organizational context (size, industry, budget, urgency)

**Interview Tips:**
- Request concrete evidence (documentation, screenshots, process diagrams)
- Ask "show me" not just "do you have"
- Explore both stated capabilities and actual practices
- Identify cultural blockers and political dynamics

### 2. Generate Maturity Scores

Run `scripts/maturity_scorecard.py` with collected responses:

```bash
python scripts/maturity_scorecard.py --responses responses.json --org-context context.json
```

The script:
- Calculates weighted scores for each phase (0-100 scale)
- Generates subsection scores for detailed gap analysis
- Compares against industry benchmarks from `references/benchmark_data.md`
- Identifies specific capability gaps and strengths
- Produces JSON output with scores and recommendations

### 3. Create Transformation Roadmap

Run `scripts/generate_roadmap.py` with maturity scores and context:

```bash
python scripts/generate_roadmap.py --scores maturity_scores.json --context context.json
```

The script:
- Sequences initiatives based on dependencies and maturity level
- Identifies quick wins (30-90 days) vs. strategic builds (6-18 months)
- Estimates investments (time, budget, resources) for each phase
- Projects ROI timeline based on benchmark data
- Generates milestone timeline with decision gates

### 4. Produce Assessment Deliverable

Create comprehensive assessment document:
- Start with `assets/assessment_template.docx` as base structure
- Include executive summary with key findings and recommendations
- Add detailed scores with radar charts and gap analysis
- Embed benchmark comparisons and peer positioning
- Insert roadmap visuals from `assets/roadmap_visuals/`
- Provide specific next steps with success criteria and investment estimates

## Key Principles

**Evidence-Based Assessment**: Require concrete examples and artifacts. Don't accept "we have governance" without seeing actual governance documentation, decision logs, or approval processes.

**Benchmark Contextualization**: Compare scores against industry and size-appropriate benchmarks. A 500-person company shouldn't be judged against Fortune 500 standards.

**Actionable Gaps**: Every identified gap should have a specific recommendation. "Low fluency" becomes "Implement role-specific training program starting with Product and Engineering teams."

**Realistic Timelines**: Resist compression. Enterprise transformation takes 12-18 months minimum. Quick wins can happen in 30-90 days but systematic maturity requires sustained investment.

**Investment Transparency**: Provide specific cost ranges for each roadmap phase including technology, talent, training, and change management. Typical range: $500K-$2M for mid-size enterprise over 18 months.

## Interpretation Guidelines

### Maturity Levels (By Phase Score)

**Level 1 - Initial (0-25)**: Ad hoc activities, no systematic approach, minimal foundation
**Level 2 - Developing (26-50)**: Some structure emerging, pilots underway, gaps in execution
**Level 3 - Defined (51-75)**: Systematic processes, measurable progress, scaling challenges
**Level 4 - Managed (76-90)**: Mature practices, continuous improvement, measurable business impact
**Level 5 - Optimizing (91-100)**: Industry leadership, innovation engine, sustained competitive advantage

### Common Patterns

**Stuck in Pilots** (High Phase 1 & 2, Low Phase 3 & 4): Strong foundation and excitement but no systematic prioritization or production discipline. Recommendation: Implement formal use case intake and build first 3-5 production use cases.

**Tool-Focused** (High Phase 2, Low Phase 1 & 3): High adoption and usage but weak governance and no prioritization. Recommendation: Establish AI Center of Excellence and formalize decision rights before expanding further.

**Engineering-Only** (High Phase 4, Low Phase 2 & 3): Technical teams can build but business isn't engaged. Recommendation: Expand fluency programs and create business-led use case discovery process.

## Output Format

The assessment produces three primary deliverables:

1. **Executive Presentation** (15-20 slides)
   - Current state assessment with scores
   - Gap analysis and benchmarking
   - Strategic recommendations
   - Investment roadmap with ROI projections

2. **Detailed Report** (25-40 pages)
   - Methodology and assessment approach
   - Phase-by-phase findings with evidence
   - Comprehensive gap analysis
   - Detailed implementation roadmap
   - Risk analysis and mitigation strategies

3. **Roadmap Artifacts**
   - 12-18 month timeline with milestones
   - Resource allocation plan
   - Investment schedule
   - Success metrics and KPIs
   - Decision gates and review cadence
