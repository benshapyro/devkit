# New Skill Ideas

Research findings from January 2026 analysis of current inventory, AI agent trends, developer tools, and the broader agent skills ecosystem.

---

## Executive Summary

Your skills library has **36 skills** with excellent coverage in **frontend development** (7 skills), **document processing** (5 skills), and **code quality** (4 skills). However, there are critical gaps in **DevOps/Infrastructure**, **security**, **database operations**, and **observability** that represent high-value opportunities.

The agent skills ecosystem is exploding—Anthropic's spec has been adopted by Microsoft, OpenAI, Cursor, and others. Community collections like **obra/superpowers** (20+ battle-tested skills) and **wshobson/agents** (107 skills) demonstrate proven patterns worth adopting.

---

## Current Inventory Analysis

### Well-Covered Domains (Strong)

| Domain | Skills | Coverage |
|--------|--------|----------|
| Frontend/UI | 7 | react-patterns, tailwind-conventions, frontend-design, vibe-coding, web-artifacts-builder, canvas-design, algorithmic-art |
| Documents | 5 | pdf, docx, pptx, xlsx, doc-coauthoring |
| Code Quality | 4 | test-generator, error-handler, code-formatter, webapp-testing |
| Backend/API | 4 | api-design-patterns, service-integration, internal-tools, data-querying |
| LLM Integration | 3 | anthropic-messages-api, openai-responses-api, mcp-builder |

### Critical Gaps

| Domain | Current Skills | Gap Level |
|--------|---------------|-----------|
| DevOps/Infrastructure | 0 | 🔴 Critical |
| Security | 0 | 🔴 Critical |
| Database Operations | 0 | 🔴 Critical |
| Observability/Debugging | 0 | 🟡 High |
| Git Workflows | 0 | 🟡 High |
| Mobile Development | 0 | 🟡 Medium |
| Performance Profiling | 0 | 🟡 Medium |

---

## Recommended New Skills

### Tier 1: Build Immediately (Highest Impact)

These address critical gaps with strong market validation.

#### 1. `git-workflow-automator`
**Why:** Universal pain point, high daily usage. 43M PRs/month on GitHub.
**What it does:**
- Conventional commit message generation
- Branch naming conventions
- PR description generation from diff
- Changelog generation
- Interactive rebase guidance
- Git worktree management (from obra/superpowers)

**Pattern source:** obra/superpowers `finishing-a-development-branch`, `using-git-worktrees`

---

#### 2. `systematic-debugging`
**Why:** No competing skill in repo; debugging non-deterministic AI behavior is hard.
**What it does:**
- 4-phase root cause analysis process
- Log analysis and pattern detection
- Trace visualization
- Hypothesis-driven debugging workflow
- Defense-in-depth validation

**Pattern source:** obra/superpowers `systematic-debugging`, `root-cause-tracing`

---

#### 3. `database-operations`
**Why:** Schema changes are risky; 80% of production issues involve databases.
**What it does:**
- Migration script generation (Flyway, Liquibase, Atlas patterns)
- Schema diff and drift detection
- Safe query generation with read-only modes
- Seed data management
- Rollback procedures

**Pattern source:** DBHub MCP, Execute Automation MCP patterns

---

#### 4. `ci-cd-pipelines`
**Why:** Every project needs CI/CD; $44.5B wasted on cloud misconfigurations.
**What it does:**
- GitHub Actions workflow generation
- GitLab CI, CircleCI templates
- Common patterns (test → build → deploy)
- Security scanning integration
- Deployment checklist workflows

**Tools referenced:** GitHub Actions, ArgoCD, Jenkins X

---

#### 5. `security-scanner`
**Why:** 34% increase in vulnerability exploitation; 80-90% of code is dependencies.
**What it does:**
- Secrets scanning (committed credentials)
- Dependency vulnerability audit
- OWASP top 10 checklist
- License compliance checking
- Security policy generation (SECURITY.md, dependabot.yml)

**Tools referenced:** Snyk, OWASP Dependency-Check, GitHub Dependabot

---

### Tier 2: Build Next (Strong Value)

#### 6. `test-driven-development`
**Why:** TDD discipline prevents bugs; obra/superpowers proves this pattern works.
**What it does:**
- RED-GREEN-REFACTOR workflow enforcement
- Test-first scaffolding
- Async testing patterns
- Testing anti-patterns reference
- Coverage gap identification

**Pattern source:** obra/superpowers `test-driven-development`, `testing-anti-patterns`

---

#### 7. `cloud-cost-optimizer`
**Why:** 21% ($44.5B) of cloud spending is wasted; FinOps is now strategic.
**What it does:**
- Terraform/IaC cost estimation before deployment
- Resource rightsizing recommendations
- Unused resource detection
- Cost allocation tagging
- Multi-cloud comparison

**Tools referenced:** Finout, Infracost, AWS Cost Explorer

---

#### 8. `api-documentation-generator`
**Why:** 80% say API docs more important than 5 years ago; 50%+ struggle to keep in sync.
**What it does:**
- OpenAPI spec generation from code
- Interactive documentation (Swagger UI)
- Multi-language SDK generation
- API changelog with breaking change detection
- Postman collection sync

**Tools referenced:** Fern, Mintlify, Bump.sh, Theneo

---

#### 9. `kubernetes-helper`
**Why:** K8s complexity is overwhelming; troubleshooting is painful.
**What it does:**
- Manifest validation and best practices
- Common issue diagnosis (pod crashes, network, storage)
- Helm chart generation
- Service mesh configuration (Istio/Linkerd patterns)
- Resource quota planning

**Tools referenced:** kubectl, Helm, ArgoCD

---

#### 10. `terraform-validator`
**Why:** Infrastructure drift causes production issues; IaC security is critical.
**What it does:**
- Terraform file validation
- Security misconfiguration detection
- Drift detection (IaC vs actual)
- Module best practices
- State management guidance

**Tools referenced:** Terraform, OpenTofu, Spacelift

---

### Tier 3: Specialized Value

#### 11. `agent-orchestrator`
**Why:** Multi-agent systems are the future (1,445% inquiry surge); foundational capability.
**What it does:**
- Task decomposition into sub-agent work
- Parallel agent dispatch
- Result synthesis and coordination
- Error recovery patterns
- Agent communication protocols

**Pattern source:** obra/superpowers `dispatching-parallel-agents`, wshobson/agents orchestration

---

#### 12. `context-optimizer`
**Why:** Context engineering is emerging discipline; naive patterns cause cost spirals.
**What it does:**
- Token usage analysis
- Redundancy detection
- Compression strategies
- Hierarchical summarization
- Budget management with quality metrics

**Pattern source:** muratcankoylan/Agent-Skills-for-Context-Engineering

---

#### 13. `log-analyzer`
**Why:** Teams drowning in logs without actionable insights; debugging production is hard.
**What it does:**
- Pattern detection in log files
- Error clustering and deduplication
- Anomaly detection
- Correlation across services
- Alert rule generation

**Tools referenced:** Datadog, Grafana Loki, OpenTelemetry

---

#### 14. `performance-profiler`
**Why:** Performance issues are expensive; shift-left testing is trend.
**What it does:**
- Load test generation from API specs
- Bundle size analysis
- Core Web Vitals optimization
- Benchmark comparison across changes
- APM integration patterns

**Tools referenced:** k6, Lighthouse, webpack-bundle-analyzer

---

#### 15. `dev-environment-setup`
**Why:** "Works on my machine" costs hours/days per new team member.
**What it does:**
- One-command project setup
- Tool version verification
- Docker Compose generation
- Environment health checks
- Dotfiles management

**Tools referenced:** Devbox, Docker, asdf

---

### Tier 4: Niche But Valuable

| Skill | Use Case |
|-------|----------|
| `mobile-react-native` | React Native development patterns |
| `graphql-patterns` | GraphQL schema design and resolvers |
| `websocket-realtime` | Real-time communication patterns |
| `i18n-localization` | Internationalization workflows |
| `data-pipeline-etl` | ETL pattern scaffolding |
| `ai-code-reviewer` | Multi-agent PR review system |
| `load-test-generator` | k6/JMeter script generation |
| `helm-chart-generator` | Kubernetes Helm chart creation |
| `openapi-client-generator` | Type-safe API client generation |
| `playwright-automation` | Browser automation beyond testing |

---

## Patterns to Adopt

### From obra/superpowers

**Feedback Loop Pattern** (validation-driven):
```
1. Execute action
2. Run validator
3. If errors → fix and return to step 2
4. Proceed only when validation passes
```

**Plan-Validate-Execute Pattern** (for high-stakes):
```
analyze → create plan file → validate plan → execute → verify
```

**Checklist Workflow** (for complex multi-step):
```markdown
Copy this checklist:
- [ ] Step 1: Action
- [ ] Step 2: Action
- [ ] Step 3: Action
```

### From Anthropic's Official Skills

**Reconnaissance-Then-Action** (webapp-testing):
```
1. Navigate and wait for networkidle
2. Take screenshot/inspect DOM
3. Identify selectors from rendered state
4. Execute actions with discovered selectors
```

**Four-Phase Development** (mcp-builder):
```
Phase 1: Deep research and planning
Phase 2: Implementation
Phase 3: Review and test
Phase 4: Create evaluations
```

### From Community Best Practices

**Rigid vs. Flexible Skills:**
- **Rigid skills**: Enforce discipline (TDD, commit conventions)
- **Flexible skills**: Provide guidance (design patterns, best practices)

**Domain-Specific Organization:**
```
skill/
├── SKILL.md (overview + routing)
└── references/
    ├── aws.md (loaded for AWS)
    ├── gcp.md (loaded for GCP)
    └── azure.md (loaded for Azure)
```

---

## Priority Matrix

| Impact | Effort | Skills |
|--------|--------|--------|
| 🔴 High | 🟢 Low | git-workflow-automator, security-scanner |
| 🔴 High | 🟡 Medium | systematic-debugging, ci-cd-pipelines, database-operations |
| 🔴 High | 🔴 High | agent-orchestrator, kubernetes-helper |
| 🟡 Medium | 🟢 Low | test-driven-development, dev-environment-setup |
| 🟡 Medium | 🟡 Medium | api-documentation-generator, terraform-validator |
| 🟡 Medium | 🔴 High | context-optimizer, ai-code-reviewer |

---

## Market Validation

**Why These Skills Matter:**

- **1,200+ MCP servers** created in 12 months (explosive growth)
- **41% of code is AI-generated** (GitHub 2025), creating review bottleneck
- **85% of developers** use AI tools regularly
- **$750M AI code review market** in 2025
- **21% ($44.5B) cloud spending wasted** on underutilized resources
- **1,445% surge** in multi-agent system inquiries (Q1 2024 → Q2 2025)

**Ecosystem Adoption:**
- Microsoft (VS Code, GitHub Copilot) adopted Agent Skills spec
- OpenAI (Codex CLI, ChatGPT) adopted Agent Skills spec
- 35.3k+ stars on Anthropic's skills repository
- "Tens of thousands" of community-created skills

---

## Sources

### Official Documentation
- [Agent Skills Specification](https://agentskills.io)
- [Anthropic Skills Repository](https://github.com/anthropics/skills)
- [OpenAI Skills Catalog](https://github.com/openai/skills)

### Community Collections
- [obra/superpowers](https://github.com/obra/superpowers) - Production software development workflow
- [wshobson/agents](https://github.com/wshobson/agents) - 107 agent skills + orchestrators
- [skillmatic-ai/awesome-agent-skills](https://github.com/skillmatic-ai/awesome-agent-skills)
- [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)

### Tool References
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers)
- [SkillsMP Marketplace](https://skillsmp.com/)

### Trend Analysis
- [AI Coding Assistant Trends (Faros AI)](https://www.faros.ai/blog/best-ai-coding-agents-2026/)
- [Developer Productivity Pain Points (Jellyfish)](https://jellyfish.co/library/developer-productivity/pain-points/)
- [State of Developer Ecosystem 2025 (JetBrains)](https://blog.jetbrains.com/research/2025/10/state-of-developer-ecosystem-2025/)
- [Cloud Cost Optimization 2025 (nOps)](https://www.nops.io/blog/cloud-cost-optimization/)

---

## Non-Developer Skills

Beyond code, AI agents excel at business operations, creative workflows, research, and personal productivity. These represent high-value opportunities for broader adoption.

### Business & Operations

#### Sales & CRM

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `lead-scoring` | Analyzes CRM data, engagement signals, firmographics to score and prioritize leads | 30% higher conversion rates; 60% less follow-up time | Clay ($3.1B valuation), HubSpot AI, Monday CRM |
| `sales-proposal-generator` | Creates personalized proposals from CRM data, past wins, product info | Days → hours for proposal creation | Salesforce Einstein, PandaDoc AI |
| `pipeline-health-monitor` | Flags at-risk deals based on velocity, engagement patterns | Prevents stalled deals | Gong, Clari, HubSpot forecasting |

#### Marketing

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `content-calendar-planner` | Generates multi-channel calendars from goals, audience data, seasonal trends | Planning from 6 weeks → 5 days | Relevance AI, Wayfair case study, StoryChief |
| `seo-content-optimizer` | Analyzes content, suggests keywords, generates SEO outlines and meta descriptions | 60% boost in content personalization | Semrush, Surfer SEO, Clearscope |
| `campaign-brief-generator` | Creates comprehensive briefs with audience segments, messaging, channel strategy | Strategic alignment from day one | Acquia Source Site Builder, Sitecore AI |

#### HR & Recruiting

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `resume-screener` | Extracts info, scores against requirements, generates candidate summaries | 80% reduction in screening time | hireEZ Agent Mode, Glide AI, Paradox |
| `job-description-writer` | Creates inclusive, optimized JDs based on role requirements and DEI best practices | Consistency + improved candidate quality | Textio, LinkedIn AI, Datapeople |
| `interview-scheduler` | Coordinates availability across interviewers/candidates, manages rescheduling | 7-Eleven saved 40,000 hours/week | Paradox (Compass Group case), Calendly AI |
| `onboarding-checklist` | Creates personalized onboarding plans by role, department, policies | Consistent new hire experience | BambooHR, Rippling, Workday |

#### Finance & Accounting

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `invoice-processor` | Extracts data via OCR, validates against POs, flags discrepancies, routes for approval | Ramp gets 85% accuracy first pass; detects fraud | Ramp AI Agents, Vic.ai, Phacet |
| `expense-categorizer` | Auto-categorizes expenses, applies tax rules, flags policy violations | Compliance + reduced data entry | Expensify, Brex, Ramp |
| `financial-report-generator` | Pulls from accounting systems, generates P&L, balance sheets with visualizations | 40% more time for forecasting | QuickBooks AI, Xero, Sage Intacct |
| `budget-variance-analyzer` | Compares actual vs budget, identifies trends, generates variance explanations | Proactive budget management | Anaplan, Adaptive Planning, Pigment |

#### Legal & Compliance

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `contract-analyzer` | Extracts key terms, compares against playbook, flags non-standard language | 85% faster contract review | Sirion AI, Spellbook, ContractPod AI |
| `nda-generator` | Creates customized NDAs based on party types, jurisdiction, specific terms | Days → minutes turnaround | Ironclad, DocuSign CLM, Juro |
| `compliance-checklist` | Generates checklists for GDPR, SOC 2, HIPAA based on business type | Comprehensive coverage | Vanta, Drata, Secureframe |
| `policy-updater` | Monitors regulatory changes, identifies affected policies, suggests updates | Automated "repapering" | Thomson Reuters, LexisNexis, V7 Go |

#### Operations & Project Management

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `meeting-to-actions` | Transcribes meetings, extracts decisions/action items/owners, creates tasks | Nothing overlooked; accountability | Fellow AI, Sembly AI, Otter.ai, Fireflies |
| `status-report-generator` | Aggregates PM tool data, generates weekly reports with progress/blockers | Hours of compilation saved | ClickUp Brain, Monday AI, Notion AI |
| `resource-capacity-planner` | Analyzes workload, identifies bottlenecks, predicts capacity constraints | Prevents burnout | Smartsheet, Float, Resource Guru |
| `rfp-response-generator` | Searches past proposals, generates draft responses with citations | 70%+ time savings; 50% higher win rates | DeepRFP, Inventive AI, Responsive, Arphie |

#### Customer Success

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `ticket-triage` | Analyzes tickets, detects urgency/sentiment, routes to appropriate team | 30% time savings; 45 seconds per ticket | Zendesk AI, Forethought, zofiQ |
| `response-suggester` | Suggests relevant KB articles and response templates | Consistent quality; helps new agents | Intercom Fin, Freshdesk AI, Help Scout |
| `customer-health-score` | Aggregates usage, support, billing data to calculate health and predict churn | ZapScale achieves 94% accuracy | Gainsight, ChurnZero, Totango, ZapScale |

---

### Creative & Content

#### Writing & Copywriting

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `copywriting-templates` | Structured workflows for emails, landing pages, ad copy with brand voice | Addresses tool fragmentation | Jasper, Copy.ai, Writesonic |
| `style-guide-enforcer` | Extracts style patterns, validates new content against rules | Brand consistency | Writer.com, Acrolinx, Frontify |

#### Video & Audio

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `video-script-formatter` | Transforms scripts into production formats with shot lists, timing, b-roll suggestions | Bridges writing → production | Descript, Visla, Pictory |
| `subtitle-workflow` | Batch subtitle generation, translation, styling, export (VTT/SRT) | 15% more shares; accessibility compliance | VSub.io, Kapwing, LOVO AI |
| `podcast-production` | Transcription, show notes, timestamps, quote extraction, social posts | 5+ hours saved per episode | Castmagic, Podium, Descript, Riverside |
| `content-repurposer` | Converts content to multiple formats (blog → social → newsletter → video) | 76% more traffic from repurposing | Repurpose.io, Lately AI, Automata |

#### Social Media

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `social-scheduler` | Multi-platform scheduling with optimal timing, hashtag research, content recycling | 24/7 channel management | Buffer, FeedHive, Postiz, ContentStudio |
| `engagement-analyzer` | Performance metrics, content pattern analysis, competitor monitoring | Data-driven optimization | Sprout Social, Hootsuite, Brandwatch |

#### Content Strategy

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `editorial-calendar` | AI content calendar with SEO keywords, gap analysis, distribution planning | 80% reduction in planning time | StoryChief, CoSchedule, HubSpot |
| `content-audit` | Batch analysis of titles, meta, headings, internal links with fix recommendations | 32% traffic increases proven | Semrush, Ahrefs, Screaming Frog + AI |

#### Publishing & Editing

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `proofreading-workflow` | Multi-pass editing: grammar, style, fact-checking, readability, plagiarism | 45% of legal professionals use daily | Grammarly, ProWritingAid, Paperpal |
| `citation-formatter` | Auto-formatting for APA, MLA, Chicago, Bluebook; reference validation | Tedious work eliminated | MyBib, Scite.ai, Zotero, Mendeley |

---

### Research & Analysis

#### Market Research

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `competitive-intelligence` | Monitors competitor websites, pricing, messaging; generates battle cards | Real-time alerts on changes | Crayon, Klue, Competely |
| `market-research-agent` | Multi-source aggregation for SWOT, market sizing, trend identification | Weeks → days for research | Datagrid, AlphaSense, Gartner |
| `porter-five-forces` | Applies framework with AI-enhanced data collection | Structured industry analysis | McKinsey frameworks, BCG Gamma |

#### Academic Research

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `literature-review` | Multi-database search, citation networks, thematic clustering, gap analysis | 80% time savings proven | ResearchRabbit, Semantic Scholar, Elicit |
| `systematic-review` | PRISMA protocol compliance, data extraction, quality assessment | 99.4% accuracy (Elicit) | Elicit, Covidence, Rayyan |
| `citation-analysis` | Bibliometric analysis, co-authorship mapping, sentiment of citations | Research impact assessment | Scite.ai, VOSviewer, Dimensions |

#### Due Diligence

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `due-diligence` | Document processing, cross-doc inconsistency detection, red flag identification | 90% reduction in processing; 30% more risks found | Vantager, V7 Go, Deep Insight Labs |
| `investment-memo` | Market assessment, competitive landscape, financial validation, risk factors | Standardized analysis | AlphaSense, Tegus, PitchBook |
| `company-research` | SEC filings, news, management background, product catalog, financial health | Hours vs. weeks | Grata, Crunchbase, PrivCo, SEC EDGAR |

#### Consulting Frameworks

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `strategy-frameworks` | Porter's Five Forces, BCG Matrix, SWOT, 7S with AI-enhanced analysis | 70% time reduction | BCG Gamma, CaseLane.ai, Miro AI |
| `swot-analysis` | Data-driven SWOT with competitive benchmarking and trend prediction | Predictive insights | JEDA.AI, Airtable + AI, Notion AI |

#### User Research

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `user-research-synthesis` | Analyzes transcripts, surveys, feedback to identify patterns | Weeks → days for synthesis | Dovetail, Notably.ai, Condens |
| `persona-generator` | Data-driven personas from research inputs | Evidence-based vs. assumption-based | Miro AI Persona Generator, Synthetic Users |
| `survey-design` | Question optimization, bias detection, sample size calculation | Improved response quality | Typeform AI, SurveyMonkey Genius, Qualtrics |

---

### Personal Productivity

#### Email & Communication

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `newsletter-digest` | Reads subscribed newsletters, extracts key insights, sends structured summaries | Cross-newsletter pattern detection | Superhuman, SaneBox, Shortwave |
| `email-triage` | Priority scoring, intent detection, time-sensitive flagging | Hours of manual scanning saved | Gmail Priority Inbox, Spike, Newton Mail |
| `follow-up-tracker` | Monitors threads, tracks pending replies, context-aware reminders | Prevents dropped conversations | Boomerang, Mixmax, HubSpot Sequences |

#### Calendar & Scheduling

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `meeting-briefing` | Compiles attendee bios, email history, meeting notes into one-page brief | Eliminates morning prep | Tactiq, Read.ai, Circleback |
| `time-blocking` | Analyzes workload, energy patterns; auto-schedules focus time | Defends deep work | Reclaim.ai, Clockwise, Motion |
| `agenda-builder` | Pulls context from emails, docs to auto-generate structured agendas | Ensures productive meetings | Fellow, Hypercontext, Hugo |

#### Travel

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `itinerary-builder` | Complete trip plans with real-time adaptation to weather/delays | Hours → minutes planning | Layla AI, Mindtrip, Roam Around, TripIt |
| `packing-list` | Customized lists based on destination, weather, activities, duration | Prevents forgotten items | PackPoint, TripIt Pro, Packr |
| `travel-expense-tracker` | Auto-categorizes expenses, tracks against budget, generates reports | Accurate reimbursement | Expensify, Ramp, SAP Concur |

#### Personal Finance

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `subscription-audit` | Identifies unused subscriptions, calculates annual cost, suggests cancellations | Hundreds of dollars recovered | Rocket Money (Truebill), Trim, Bobby |
| `budget-anomaly-detector` | Learns spending patterns, flags unusual transactions, spots billing errors | Early warning system | Copilot, Monarch Money, YNAB |
| `cash-flow-optimizer` | Analyzes timing, identifies idle cash, suggests automated savings | Painless savings building | Qapital, Digit, Wealthfront Cash |

#### Health & Wellness

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `workout-planner` | Personalized workouts adjusted for recovery, sleep, stress | Prevents injuries; sustainable fitness | WHOOP, TrainFitness AI, Juggernaut AI, Fitbod |
| `meal-planner` | Weekly plans matching goals, activity, preferences; shopping lists | Decision fatigue eliminated | Mealime, Eat This Much, Whisk (Samsung) |
| `health-data-synthesizer` | Aggregates wearable/app data, identifies patterns, predicts risks | Proactive health management | Apple Health, Google Fit, Gyroscope, Welltory |

#### Learning

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `study-material-generator` | Converts courses to flashcards, quizzes, summaries with spaced repetition | 50% study time reduction | Anki + AI plugins, Quizlet, RemNote, Brainscape |
| `learning-path-builder` | Personalized skill roadmaps based on goals, knowledge, time | Clear path to competency | Coursera, Pluralsight Skill IQ, roadmap.sh |

#### Home & Life Admin

| Skill | What It Does | Value | Source/Inspiration |
|-------|--------------|-------|-------------------|
| `home-maintenance` | Tracks schedules, predicts failures, sends reminders | Prevents costly breakdowns | Centriq, HomeZada, Thumbtack |
| `contractor-research` | Researches qualified contractors, compares reviews/pricing | Hours of research saved | Angi (HomeAdvisor), Thumbtack, Yelp, Houzz |
| `moving-checklist` | Comprehensive checklists, utility transfers, address changes | Reduces moving stress | Updater, MoveAdvisor, Moved |
| `event-planner` | Guest lists, invitations, RSVPs, vendors, timelines, budget | Professional-level organization | Partiful, The Knot, Aisle Planner, Joy |

---

### Non-Developer Priority Recommendations

#### Tier 1: Broadest Appeal, Highest Impact
1. **`meeting-to-actions`** - Universal need; clear ROI; proven tools exist
2. **`content-repurposer`** - #1 cited AI content use case; 76% traffic gains
3. **`invoice-processor`** - $6.68B market; fraud detection; massive time savings
4. **`resume-screener`** - 87% of companies use AI hiring; 80% time reduction
5. **`competitive-intelligence`** - Real-time market awareness; sales enablement

#### Tier 2: Strong Departmental Value
6. **`editorial-calendar`** - 80% planning time savings; marketing teams
7. **`contract-analyzer`** - 85% faster review; legal teams
8. **`customer-health-score`** - 94% churn prediction accuracy; CS teams
9. **`rfp-response-generator`** - 70% time savings; 50% higher win rates
10. **`literature-review`** - 80% time savings; research teams

#### Tier 3: Personal Productivity Winners
11. **`newsletter-digest`** - Universal need; daily value
12. **`meeting-briefing`** - Professional credibility; time savings
13. **`subscription-audit`** - Immediate financial ROI
14. **`study-material-generator`** - Large student market

---

## Next Steps

1. **Start with Tier 1** - These have highest impact and strong market validation
2. **Adopt workflow patterns** - Add feedback loops and checklists to existing skills
3. **Reference community skills** - Study obra/superpowers for proven patterns
4. **Track ecosystem** - Monitor SkillsMP and awesome lists for new ideas
5. **Expand beyond dev** - Non-developer skills have massive untapped market
