# Skills Catalog

A curated collection of 66 skills that extend Claude's capabilities for specific tasks and workflows. Skills auto-activate based on context, or you can invoke them explicitly.

**How skills work:** When you start a task that matches a skill's triggers, it automatically loads specialized knowledge and workflows. Think of skills as expert assistants for specific domains.

## Quick Navigation

- [Content & Marketing](#content--marketing) — Writing, editing, repurposing content
- [Development Tools](#development-tools) — APIs, testing, code patterns
- [Data & Documents](#data--documents) — Spreadsheets, PDFs, analysis
- [Design & UI](#design--ui) — Frontend, themes, visual design
- [Infrastructure & Ops](#infrastructure--ops) — Security, monitoring, reliability
- [Business & Strategy](#business--strategy) — Product, competitive analysis, frameworks
- [AI & Automation](#ai--automation) — AI APIs, prompts, image generation
- [Internal & Specialty](#internal--specialty) — Niche tools and meta-skills

---

## Quick Reference

### Content & Marketing

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| content-repurposer | Transform one piece of content into multiple platform-specific formats | "Turn this blog post into 5 tweets, a LinkedIn post, and newsletter intro" |
| editorial-calendar | Plan content calendars with SEO integration and multi-channel coordination | "Create a 3-month editorial calendar for our B2B blog with social tie-ins" |
| ace-content-engine | Generate blog content with brand voice using Workshop or YOLO modes | "Write a blog post about AI tools using Workshop Mode with citations" |
| internal-comms | Create internal communications like all-hands announcements and policy updates | "Write an all-hands announcement about our office relocation" |
| doc-coauthoring | Co-author documents through Context → Refinement → Reader Testing stages | "Help me co-author a technical guide, starting with context gathering" |
| brand-guidelines | Apply Anthropic brand colors and typography to artifacts | "Apply Anthropic brand styling to this HTML artifact" |
| presentation-composer | Create scientifically-optimized presentations with cognitive science principles | "Create an executive briefing deck using Pyramid Principle structure" |

### Development Tools

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| api-design-patterns | Design REST and GraphQL APIs with proper patterns for Node.js, Flask, FastAPI | "Design a REST API for user management with pagination and RBAC" |
| test-generator | Generate Jest or Pytest tests with proper coverage and mocking | "Generate Jest tests for this UserService including error cases" |
| react-patterns | Implement modern React patterns with hooks, state management, optimization | "Create a custom hook for form state with validation and error handling" |
| mcp-builder | Build Model Context Protocol servers to extend Claude's capabilities | "Build an MCP server that exposes our internal API as tools" |
| code-formatter | Apply consistent code style with naming conventions and formatting rules | "Format this TypeScript file according to our style guide" |
| error-handler | Implement robust error handling patterns for TypeScript and Python | "Add comprehensive error handling to this API endpoint" |

### Data & Documents

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| pdf | Extract, merge, split, fill forms, and manipulate PDF documents | "Extract all table data from this PDF invoice" |
| docx | Create Word docs with docx-js or edit existing docs with Python OOXML | "Create a professional report with cover page and table of contents" |
| pptx | Create presentations from scratch, templates, or edit existing slides | "Create a 10-slide investor pitch deck from this company overview" |
| xlsx | Create Excel files with formulas (never hardcoded), charts, and formatting | "Create an Excel budget template with formulas and conditional formatting" |
| ai-data-analyst | Perform data analysis, statistical modeling, and visualization with Python | "Analyze this sales dataset: identify trends and create visualizations" |
| data-querying | Query internal data warehouses while respecting governance and PII policies | "Query our data warehouse for monthly active users by region" |

### Design & UI

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| frontend-design | Create distinctive UIs with intentional aesthetic direction, not generic AI look | "Design a modern dashboard with a unique brutalist visual style" |
| canvas-design | Create museum-quality visual art through design philosophy workflow | "Create a visual piece inspired by brutalist architecture as a poster" |
| theme-factory | Apply 10 professional themes (Ocean Depths, etc.) to slides and documents | "Show me available themes, then apply Ocean Depths to my deck" |
| algorithmic-art | Create generative art with p5.js, seeded reproducibility, and interactivity | "Create generative art with flow fields and Perlin noise with seed controls" |
| web-artifacts-builder | Build complex React/shadcn/ui artifacts that bundle to single HTML | "Build a project management app with React, Tailwind, and drag-and-drop" |
| tailwind-conventions | Apply consistent Tailwind CSS patterns for React/Next.js apps | "Style this component with Tailwind including responsive and dark mode" |

### Infrastructure & Ops

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| security-guardian | Security patterns for authentication, authorization, and OWASP remediation | "Review this auth module for vulnerabilities and provide fixes" |
| observability-engineering | Implement metrics, logging, tracing, and alerting with OpenTelemetry | "Add OpenTelemetry instrumentation to this Node.js service" |
| sre-runbook-generator | Generate operational runbooks for incidents and maintenance procedures | "Create a runbook for database connection pool exhaustion alerts" |
| database-migration | Plan and execute zero-downtime database schema migrations | "Create a migration plan to add a column with zero downtime" |
| web-accessibility-auditor | Audit for WCAG 2.2 compliance and fix accessibility issues | "Audit this page for WCAG 2.2 AA compliance and provide fixes" |
| webapp-testing | Test web applications with Playwright for E2E and UI verification | "Write Playwright tests for our checkout flow" |

### Business & Strategy

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| product-discovery | Discover products using Five Whys, MECE; outputs SPEC.md, DESIGN.md, PLAN.md | "Help me discover a new onboarding feature, start with problem exploration" |
| product-management | PRD writing, feature analysis, research synthesis, stakeholder communication | "Write a PRD for team collaboration features based on user research" |
| strategy-frameworks | Apply Porter's Five Forces, BCG Matrix, SWOT, McKinsey 7S frameworks | "Conduct a Porter's Five Forces analysis for EV charging market" |
| competitive-intelligence | Create battle cards, competitive matrices, and win/loss analysis | "Create a battle card for competing against [Competitor]" |
| expense-categorizer | Categorize expenses with tax treatment, GL codes, and policy compliance | "Categorize these expenses and flag policy violations" |
| ai-maturity-assessor | Assess AI transformation maturity across governance, fluency, and production | "Assess our organization's AI readiness and create a transformation roadmap" |
| software-research-analyst | Strategic software research for $50K+ purchases with TCO analysis | "Evaluate HubSpot vs Salesforce vs Pipedrive for our 50-person sales team" |
| tool-research-architect | Tool research with Jobs-to-be-Done framework and LLM integration analysis | "Research these 10 GTM tools focusing on AI/LLM integration capabilities" |

### AI & Automation

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| anthropic-messages-api | Implement Claude API with tool use, streaming, caching, and batches | "Implement Claude API integration with tool use for a support bot" |
| openai-responses-api | Implement OpenAI Responses API with built-in tools and migration guidance | "Migrate our Chat Completions to Responses API with web search" |
| ai-art-generation | Guide AI image generation with Midjourney, DALL-E, Stable Diffusion | "Create prompts for consistent fantasy character portraits in pixel art" |
| clay-mastery | Build Clay.com data enrichment workflows with waterfall enrichment and Claygent | "Build a prospect list workflow with email waterfall and AI personalization" |
| prompt-engineering | Comprehensive prompt patterns for Claude, GPT, and Gemini with model-specific optimization | "Optimize this prompt for Claude 4.5 with tool use" |
| client-prompt-coach-builder | Generate customized prompt coaching CustomGPTs for clients | "Build a prompt coach for our client in the real estate industry" |
| n8n-workflow-patterns | 5 core workflow architectures (webhook, API, database, AI agent, scheduled) | "What pattern should I use for a Slack bot that queries our database?" |
| n8n-mcp-tools-expert | Master guide for n8n MCP tools (search_nodes, get_node, validate, create) | "How do I use get_node to understand Slack node configuration?" |
| n8n-node-configuration | Operation-aware configuration with property dependencies | "Why does my HTTP Request node require sendBody for POST?" |
| n8n-validation-expert | Interpret validation errors and fix them with iterative workflow | "I'm getting a missing_required error on my Slack node" |
| n8n-expression-syntax | Write correct n8n expressions with {{}} syntax and webhook data access | "Why is my webhook data coming back undefined?" |
| n8n-code-javascript | Write JavaScript in n8n Code nodes with $input, $json, $helpers | "Write a Code node that aggregates data from multiple items" |
| n8n-code-python | Write Python in n8n Code nodes (standard library only, no pandas/requests) | "When should I use Python instead of JavaScript in n8n?" |

### Internal & Specialty

| Skill | Description | Example Prompt |
|-------|-------------|----------------|
| skill-creator | Create new skills with proper SKILL.md structure and best practices | "Help me create a new skill for [domain]" |
| vibe-coding | Rapidly prototype web apps; local alternative to Lovable, Bolt, v0 | "Build a task management app with drag-and-drop and local storage" |
| browser | Automate Chrome with DevTools Protocol for navigation and scraping | "Navigate to this page, fill the form, and capture a screenshot" |
| slack-gif-creator | Create animated GIFs for Slack using programmatic graphics (PIL) | "Create a GIF showing the new feature, optimized for Slack" |
| cadre-os | Cadre AI consulting OS for discovery, synthesis, and deliverables | "/prep [Client Name] — Prepare for upcoming discovery session" |
| documentation-templates | Generate READMEs, API docs, and code comments following best practices | "Generate a comprehensive README with setup, usage, and API docs" |
| frontend-ui-integration | Build frontend features that integrate with existing backend APIs | "Build a user settings page integrating with our user API" |
| service-integration | Integrate services in monorepos while preserving ownership boundaries | "Add a notification service that integrates with user service" |
| internal-tools | Build internal operational tools with access controls and audit logging | "Build an internal tool for support to manage subscriptions" |
| cadre-block-builder | Create implementation blocks for client SOWs with dual internal/client versions | "Create a 3-month implementation block for this Salesforce integration project" |
| clickup-automation-architect | Design and optimize ClickUp automations for consulting workflows | "Build a client onboarding automation that triggers on task creation" |
| clickup-guide | ClickUp structure, permissions, and features optimized for consulting firms | "How should I organize client projects in ClickUp with proper permissions?" |
| onboarding | Generate comprehensive onboarding docs for engagements, teams, and pods | "Onboard me to the Hyperion client engagement with strategic context" |
| project-resource-planner | Convert SOWs to week-by-week ClickUp resource plans with SMART goals | "Convert this SOW into a resource allocation plan with hour estimates" |

---

## Content & Marketing

Skills for writing, editing, and content strategy.

<details>
<summary><strong>content-repurposer</strong> — Turn one piece of content into many formats</summary>

**Best for:** Content marketers, social media managers, marketing teams

**What it does:** Transforms a single piece of content (blog post, video, podcast) into multiple formats optimized for different platforms. Handles blog-to-social, podcast-to-article, video-to-snippets, and more while maintaining consistent messaging.

**When to use:**
- Turning a blog post into LinkedIn posts, tweets, and newsletter content
- Converting a podcast episode into an article and quote graphics
- Repurposing webinar content for multiple channels
- Creating platform-specific variations of core content

**Example prompt:**
> "Take this 2,000-word blog post about AI trends and create a LinkedIn carousel, 5 tweets, and an email newsletter intro."

</details>

<details>
<summary><strong>editorial-calendar</strong> — Plan and coordinate content across channels</summary>

**Best for:** Content managers, marketing directors, editorial teams

**What it does:** Creates comprehensive content calendars with keyword-first planning, SEO integration, topic clusters, multi-channel coordination, and publication scheduling. Aligns content with business goals and seasonal events.

**When to use:**
- Planning quarterly content strategy
- Coordinating blog, social, and email campaigns
- Aligning content with product launches or events
- Building out topic clusters for SEO

**Example prompt:**
> "Create a 3-month editorial calendar for our B2B SaaS blog focusing on customer success themes. Include social media tie-ins."

</details>

<details>
<summary><strong>ace-content-engine</strong> — Generate blog content with brand voice consistency</summary>

**Best for:** Content writers, marketing teams, blog managers

**What it does:** Generates blog content with brand voice consistency, research support, and structured workflows. Supports Workshop Mode (guided, high-quality with iterations) and YOLO Mode (quick single-pass drafts). Handles citations, structured content sections, and brand voice configuration.

**When to use:**
- Writing blog posts with consistent brand voice
- Generating content with proper citations and research
- Creating high-quality drafts through guided iteration
- Producing quick content drafts when speed matters

**Example prompt:**
> "Write a blog post about AI productivity tools using Workshop Mode. Apply our brand voice and include citations."

</details>

<details>
<summary><strong>internal-comms</strong> — Craft effective internal communications</summary>

**Best for:** HR teams, internal communications managers, executives

**What it does:** Creates clear, engaging internal communications including all-hands announcements, policy updates, change management messages, and executive communications. Balances transparency with appropriate messaging.

**When to use:**
- Announcing organizational changes
- Communicating new policies or benefits
- Writing executive updates and town hall scripts
- Crafting sensitive employee communications

**Example prompt:**
> "Write an all-hands announcement about our office relocation. Emphasize the positives while acknowledging the transition period."

</details>

<details>
<summary><strong>doc-coauthoring</strong> — Co-author documents through structured stages</summary>

**Best for:** Writers, subject matter experts, documentation teams

**What it does:** Guides co-authoring through three structured stages: Context Gathering (transfer knowledge and intent), Refinement & Structure (iterate on content), and Reader Testing (verify with fresh perspective). Catches blind spots before real-world distribution by testing documents with a "fresh Claude."

**When to use:**
- Transferring complex knowledge into documents
- Iterating on drafts with structured refinement
- Testing if documents work for target readers
- Catching blind spots before publishing

**Example prompt:**
> "Help me co-author a technical guide. Start with context gathering to understand what I need to convey."

</details>

<details>
<summary><strong>brand-guidelines</strong> — Apply Anthropic brand colors and typography</summary>

**Best for:** Designers creating Anthropic-branded artifacts

**What it does:** Applies Anthropic's official brand colors, typography, and design standards to artifacts. Provides the specific color palette (Anthropic Tan, accent colors), font guidelines, and visual styling rules for creating on-brand presentations, documents, and HTML artifacts.

**When to use:**
- Styling artifacts with Anthropic brand colors
- Applying correct Anthropic typography
- Creating on-brand presentations or documents
- Ensuring visual consistency with Anthropic standards

**Example prompt:**
> "Apply Anthropic brand styling to this HTML artifact, using the correct colors and typography."

</details>

<details>
<summary><strong>presentation-composer</strong> — Create scientifically-optimized presentations</summary>

**Best for:** Consultants, executives, presenters, sales teams

**What it does:** Creates presentations using neuroscience-based frameworks (working memory limits, serial position effects) and consulting methodologies (Pyramid Principle, SCR, McKinsey/BCG approaches). Applies cognitive science principles: 3-4 chunks maximum per slide, 30 words or less, F/Z-pattern layouts, and strategic primacy/recency placement. Includes validation scripts and quality checklists.

**When to use:**
- Creating executive briefings or board decks
- Building sales presentations or strategy consulting deliverables
- Improving existing presentations with cognitive science principles
- Selecting the right framework (Pyramid Principle, SCR, Duarte's Resonate, TED 4-Step)

**Example prompt:**
> "Create an executive briefing deck using Pyramid Principle structure with recommendation upfront and MECE supporting arguments."

</details>

---

## Development Tools

Skills for coding, APIs, testing, and development patterns.

<details>
<summary><strong>api-design-patterns</strong> — Design robust REST and GraphQL APIs</summary>

**Best for:** Backend developers, API architects, full-stack engineers

**What it does:** Provides REST and GraphQL API design patterns for Node.js, Flask, and FastAPI. Covers endpoint design, request/response structures, pagination, authentication, rate limiting, and error handling.

**When to use:**
- Designing new API endpoints
- Reviewing API architecture decisions
- Implementing pagination and filtering
- Setting up API authentication and rate limiting

**Example prompt:**
> "Design a REST API for user management with CRUD operations, pagination, and role-based access control."

</details>

<details>
<summary><strong>test-generator</strong> — Generate comprehensive test suites</summary>

**Best for:** Developers, QA engineers, test automation specialists

**What it does:** Generates Jest or Pytest tests following testing best practices. Creates unit tests, integration tests, and mocks with proper coverage of edge cases and error conditions.

**When to use:**
- Adding test coverage to existing code
- Creating tests for new features
- Setting up mocks for external dependencies
- Improving test organization and structure

**Example prompt:**
> "Generate Jest tests for this UserService class, including happy path, error cases, and mocked database calls."

</details>

<details>
<summary><strong>react-patterns</strong> — Implement modern React best practices</summary>

**Best for:** Frontend developers, React engineers

**What it does:** Provides modern React patterns for TypeScript applications including hooks, state management, component composition, and performance optimization. Covers custom hooks, context patterns, and render optimization.

**When to use:**
- Building new React components
- Refactoring class components to hooks
- Implementing state management solutions
- Optimizing component performance

**Example prompt:**
> "Create a custom hook for managing form state with validation, loading states, and error handling."

</details>

<details>
<summary><strong>mcp-builder</strong> — Build Model Context Protocol servers</summary>

**Best for:** AI developers, integration engineers, tool builders

**What it does:** Comprehensive guide for building MCP servers that extend Claude's capabilities. Covers server architecture, tool definitions, resource handling, and deployment patterns.

**When to use:**
- Creating custom MCP servers for Claude
- Adding new tools and capabilities to Claude
- Integrating external services via MCP
- Debugging MCP server issues

**Example prompt:**
> "Build an MCP server that exposes our internal API as tools Claude can use."

</details>

<details>
<summary><strong>code-formatter</strong> — Apply consistent code style</summary>

**Best for:** Developers, tech leads, teams establishing standards

**What it does:** Formats code according to style guidelines for TypeScript, Python, and general best practices. Covers naming conventions (camelCase, PascalCase), 100-character line limits, trailing commas, import organization, and explicit type annotations.

**When to use:**
- Fixing linting and formatting issues
- Establishing code style standards
- Reviewing code for style consistency
- Setting up Prettier, Black, or ESLint

**Example prompt:**
> "Format this TypeScript file according to our style guide and fix any ESLint violations."

</details>

<details>
<summary><strong>error-handler</strong> — Implement robust error handling</summary>

**Best for:** Backend developers, full-stack engineers

**What it does:** Provides battle-tested error handling patterns for TypeScript and Python. Covers try/catch strategies, error types, logging, user-friendly messages, and recovery patterns.

**When to use:**
- Adding error handling to existing code
- Designing error handling strategies
- Creating custom error types
- Implementing graceful degradation

**Example prompt:**
> "Add comprehensive error handling to this API endpoint, including validation errors, database errors, and user-friendly responses."

</details>

---

## Data & Documents

Skills for working with spreadsheets, documents, PDFs, and data analysis.

<details>
<summary><strong>pdf</strong> — Extract, merge, split, fill forms, and manipulate PDFs</summary>

**Best for:** Business analysts, document managers, anyone working with PDFs

**What it does:** Comprehensive PDF toolkit for extracting text and tables, creating new PDFs, merging/splitting documents, filling forms, and adding watermarks. Works with both simple and complex PDF structures.

**When to use:**
- Filling out PDF forms programmatically
- Extracting text and tables from PDFs
- Merging or splitting PDF documents
- Adding annotations or watermarks

**Example prompt:**
> "Extract all the table data from this PDF invoice and convert it to a structured format."

</details>

<details>
<summary><strong>docx</strong> — Create and edit Word documents</summary>

**Best for:** Report writers, business analysts, document automation teams

**What it does:** Creates new Word documents using docx-js (JavaScript/TypeScript) or edits existing documents using Python OOXML library. Handles formatting, tables, images, headers/footers, tracked changes, and styles. Choose the right tool based on whether you're creating or editing.

**When to use:**
- Generating reports from templates
- Creating formatted documents from data
- Automating document production
- Converting content to Word format

**Example prompt:**
> "Create a professional report document with a cover page, table of contents, and formatted sections from this data."

</details>

<details>
<summary><strong>pptx</strong> — Create and edit PowerPoint presentations</summary>

**Best for:** Consultants, sales teams, presenters

**What it does:** Creates and edits PowerPoint presentations using OOXML format or html2pptx. Supports three workflows: creating from scratch (html2pptx), editing existing presentations (OOXML), and creating from templates (inventory → rearrange → replace). Handles slides, layouts, charts, and images.

**When to use:**
- Creating presentations from scratch with html2pptx
- Creating presentations from existing templates
- Editing slide content in existing presentations
- Automating recurring presentations with custom design

**Example prompt:**
> "Create a 10-slide investor pitch deck from this company overview, including charts for the financial data."

</details>

<details>
<summary><strong>xlsx</strong> — Work with Excel spreadsheets</summary>

**Best for:** Data analysts, financial analysts, operations teams

**What it does:** Creates and manipulates Excel files with proper formulas (never hardcoded calculations), charts, and formatting. Supports financial modeling standards with color coding. Uses pandas for data analysis and openpyxl for formula-based spreadsheets. Includes formula verification tools.

**When to use:**
- Generating Excel reports from data
- Processing and transforming spreadsheet data
- Creating templates with formulas
- Analyzing structured tabular data

**Example prompt:**
> "Create an Excel budget template with monthly columns, category rows, formulas for totals, and conditional formatting."

</details>

<details>
<summary><strong>ai-data-analyst</strong> — Perform comprehensive data analysis</summary>

**Best for:** Data scientists, business analysts, researchers

**What it does:** Performs comprehensive data analysis, statistical modeling, and visualization by writing and executing Python scripts. Covers exploratory analysis, statistical tests, and predictive modeling.

**When to use:**
- Analyzing datasets for patterns and insights
- Performing statistical hypothesis testing
- Creating data visualizations
- Building predictive models

**Not for:** Real-time streaming data, extremely large datasets requiring Spark/Dask, production ML deployment, or live dashboarding (use BI tools instead).

**Example prompt:**
> "Analyze this sales dataset: identify trends, correlations, and create visualizations for a management presentation."

</details>

<details>
<summary><strong>data-querying</strong> — Query internal data services</summary>

**Best for:** Business intelligence teams, analysts, data engineers

**What it does:** Queries internal data warehouses and marts (not production OLTP databases) to answer business questions. Produces results and reusable query artifacts while respecting data governance and PII policies. Does not create pipelines or share raw PII.

**When to use:**
- Pulling metrics from data warehouses
- Creating reusable query templates
- Building data extracts for stakeholders
- Answering ad-hoc data questions

**Example prompt:**
> "Query our data warehouse for monthly active users by region for the past 12 months and visualize the trend."

</details>

---

## Design & UI

Skills for frontend development, visual design, and UI/UX.

<details>
<summary><strong>frontend-design</strong> — Create distinctive, memorable interfaces</summary>

**Best for:** Frontend developers, UI designers, product teams

**What it does:** Creates distinctive, production-grade user interfaces that avoid generic AI aesthetics. Emphasizes intentional aesthetic direction—brutally minimal, maximalist, retro-futuristic, organic, luxury, playful, editorial, brutalist, or art deco. Implements production-grade working code with exceptional attention to typography, color harmony, motion, and spatial composition.

**When to use:**
- Building new web pages or applications
- Designing UI components and layouts
- Creating landing pages and marketing sites
- Improving visual design quality

**Example prompt:**
> "Design a modern dashboard interface for a project management app with a unique visual style."

</details>

<details>
<summary><strong>canvas-design</strong> — Create museum-quality visual art through design philosophy</summary>

**Best for:** Designers, visual artists, creative professionals

**What it does:** Creates museum and magazine-quality visual art through a two-step design philosophy workflow. First generates a visual philosophy (aesthetic movement manifesto) expressed through form, space, color, and composition. Then creates the artwork as PDF or PNG output (90% visual design, 10% essential text). Emphasizes meticulously crafted, expert-level work.

**When to use:**
- Creating visual pieces inspired by design movements
- Generating poster-quality static artwork
- Applying design philosophy to visual output
- Building portfolio-worthy visual designs

**Example prompt:**
> "Create a visual piece inspired by brutalist architecture principles, expressed as a museum-quality poster design."

</details>

<details>
<summary><strong>theme-factory</strong> — Apply professional themes to slides and documents</summary>

**Best for:** Presenters, document creators, anyone styling artifacts

**What it does:** Provides 10 curated professional font and color themes (Ocean Depths, Sunset Boulevard, Forest Canopy, etc.) that can be applied to presentation slides, documents, and HTML artifacts. Each theme includes cohesive color palettes with hex codes and complementary font pairings. Also supports custom theme generation.

**When to use:**
- Styling presentation slide decks with professional themes
- Applying consistent styling to reports and documents
- Viewing available themes before selecting one
- Generating custom themes for specific projects

**Example prompt:**
> "Show me the available themes, then apply Ocean Depths to my slide deck."

</details>

<details>
<summary><strong>algorithmic-art</strong> — Create generative art with p5.js and seeded reproducibility</summary>

**Best for:** Creative coders, digital artists, generative art enthusiasts

**What it does:** Creates generative art using p5.js through a two-step workflow. First generates an algorithmic philosophy (computational aesthetic manifesto emphasizing seeded randomness, emergent behavior, and mathematical beauty). Then implements as interactive HTML artifact with parameter controls, seed navigation (prev/next/random), and reproducible variations.

**When to use:**
- Creating generative art with reproducible seeds
- Building interactive parameter-controlled artwork
- Implementing creative coding projects with p5.js
- Exploring algorithmic aesthetics and emergent patterns

**Example prompt:**
> "Create a generative art piece about organic turbulence using flow fields and Perlin noise, with interactive seed exploration."

</details>

<details>
<summary><strong>web-artifacts-builder</strong> — Build complex React artifacts with shadcn/ui</summary>

**Best for:** Frontend developers building elaborate claude.ai artifacts

**What it does:** Creates complex, multi-component claude.ai HTML artifacts using React 18, TypeScript, Vite, Tailwind CSS, and shadcn/ui. Initializes frontend repo, develops artifact with state management and routing, then bundles to single HTML file. Explicitly avoids AI slop (centered layouts, purple gradients, excessive rounded corners).

**When to use:**
- Building complex interactive applications (not simple single-file artifacts)
- Creating artifacts requiring state management or routing
- Using shadcn/ui component library for polish
- Building artifacts beyond simple HTML/JSX prototypes

**Example prompt:**
> "Build a project management app with React, Tailwind, and shadcn/ui that has drag-and-drop and multi-page navigation."

</details>

<details>
<summary><strong>tailwind-conventions</strong> — Apply consistent Tailwind patterns</summary>

**Best for:** Frontend developers using Tailwind CSS

**What it does:** Provides consistent Tailwind CSS patterns for React/Next.js applications. Covers utility class organization, responsive design, dark mode, and component styling.

**When to use:**
- Styling components with Tailwind
- Implementing responsive designs
- Adding dark mode support
- Organizing utility classes consistently

**Example prompt:**
> "Style this React component using Tailwind with responsive breakpoints and dark mode support."

</details>

---

## Infrastructure & Ops

Skills for security, monitoring, reliability, and operations.

<details>
<summary><strong>security-guardian</strong> — Identify and fix security vulnerabilities</summary>

**Best for:** Security engineers, developers, DevSecOps teams

**What it does:** Provides security patterns and best practices for building secure applications. Covers implementation of authentication, authorization, API security, secrets management, plus OWASP Top 10 remediation. Guidance for building secure code, not just scanning existing code.

**When to use:**
- Reviewing code for security issues
- Fixing identified vulnerabilities
- Implementing security best practices
- Preparing for security audits

**Example prompt:**
> "Review this authentication module for security vulnerabilities and provide fixes for any issues found."

</details>

<details>
<summary><strong>observability-engineering</strong> — Implement monitoring and tracing</summary>

**Best for:** SRE teams, DevOps engineers, platform teams

**What it does:** Implements observability infrastructure including metrics, logging, tracing, and alerting. Covers OpenTelemetry setup, structured logging, trace correlation, sampling strategies, collector deployment, and alert/SLO design patterns.

**When to use:**
- Setting up application monitoring
- Implementing distributed tracing
- Creating dashboards and alerts
- Debugging production issues

**Example prompt:**
> "Add OpenTelemetry instrumentation to this Node.js service with custom metrics and tracing."

</details>

<details>
<summary><strong>sre-runbook-generator</strong> — Create operational runbooks</summary>

**Best for:** SRE teams, operations engineers, on-call responders

**What it does:** Generates operational runbooks for incident response, maintenance procedures, and troubleshooting guides. Follows SRE best practices for documentation.

**When to use:**
- Documenting incident response procedures
- Creating maintenance playbooks
- Building troubleshooting guides
- Standardizing operational procedures

**Example prompt:**
> "Create a runbook for responding to database connection pool exhaustion alerts."

</details>

<details>
<summary><strong>database-migration</strong> — Plan and execute database migrations</summary>

**Best for:** Database administrators, backend developers, DevOps engineers

**What it does:** Plans and manages database schema migrations safely. Covers migration strategies, rollback plans, zero-downtime deployments, and data transformations.

**When to use:**
- Planning schema changes
- Writing migration scripts
- Implementing zero-downtime migrations
- Rolling back failed migrations

**Example prompt:**
> "Create a migration plan to add a new column to our users table with zero downtime."

</details>

<details>
<summary><strong>web-accessibility-auditor</strong> — Audit and fix accessibility issues</summary>

**Best for:** Frontend developers, QA teams, accessibility specialists

**What it does:** Audits web applications for WCAG compliance and accessibility issues. Identifies problems with screen readers, keyboard navigation, color contrast, and ARIA usage.

**When to use:**
- Auditing sites for accessibility compliance
- Fixing identified accessibility issues
- Implementing accessible components
- Preparing for accessibility certifications

**Example prompt:**
> "Audit this page for WCAG 2.2 AA compliance and provide fixes for any issues found."

</details>

<details>
<summary><strong>webapp-testing</strong> — Test web applications comprehensively</summary>

**Best for:** QA engineers, test automation specialists, frontend developers

**What it does:** Tests web applications using Playwright for E2E testing, UI verification, and debugging. Covers automated browser interaction, DOM inspection, screenshot capture, selector discovery, and browser log viewing.

**When to use:**
- Writing Playwright E2E test suites
- Verifying frontend functionality
- Debugging UI behavior with browser inspection
- Capturing screenshots for documentation

**Example prompt:**
> "Write Playwright tests for our checkout flow covering happy path and common error scenarios."

</details>

---

## Business & Strategy

Skills for product management, strategic planning, and business analysis.

<details>
<summary><strong>product-discovery</strong> — Discover and specify new products</summary>

**Best for:** Product managers, founders, innovation teams

**What it does:** Guides product discovery from problem exploration to solution specification using structured questioning frameworks (Five Whys, MECE, Socratic Probing). Creates SPEC.md, DESIGN.md, and PLAN.md documents with detailed methodology for defining MVP scope and validating ideas.

**When to use:**
- Starting new product initiatives
- Validating product ideas
- Defining MVP scope
- Writing product requirements

**Example prompt:**
> "Help me discover and specify a new feature for improving user onboarding. Start with problem exploration."

</details>

<details>
<summary><strong>product-management</strong> — Execute core PM activities</summary>

**Best for:** Product managers, product owners, team leads, business analysts, startup founders

**What it does:** Assists with core PM activities including PRD writing, feature analysis, user research synthesis, roadmap planning, and communicating product decisions to stakeholders and engineering teams.

**When to use:**
- Writing product requirements documents
- Analyzing feature requests
- Synthesizing user research findings
- Planning product roadmaps
- Communicating product decisions to stakeholders

**Example prompt:**
> "Write a PRD for adding team collaboration features to our app based on these user research findings."

</details>

<details>
<summary><strong>strategy-frameworks</strong> — Apply strategic business frameworks</summary>

**Best for:** Strategists, consultants, business analysts, executives

**What it does:** Applies structured strategic frameworks including Porter's Five Forces, BCG Matrix, SWOT Analysis, and McKinsey 7S. Guides analysis and generates actionable outputs.

**When to use:**
- Analyzing industry competitive dynamics
- Evaluating product/business portfolios
- Strategic planning sessions
- Organizational transformation planning

**Example prompt:**
> "Conduct a Porter's Five Forces analysis for the electric vehicle charging market."

</details>

<details>
<summary><strong>competitive-intelligence</strong> — Gather and analyze competitor information</summary>

**Best for:** Sales teams, marketing strategists, product managers, competitive analysts, business development teams

**What it does:** Gathers and analyzes competitor information, creates battle cards, builds competitive matrices, and conducts win/loss analysis. Enables data-driven competitive positioning.

**When to use:**
- Creating sales battle cards
- Building feature comparison matrices
- Analyzing win/loss patterns
- Monitoring competitor activity

**Example prompt:**
> "Create a battle card for competing against [Competitor] including objection handling and trap questions."

</details>

<details>
<summary><strong>expense-categorizer</strong> — Categorize business expenses accurately</summary>

**Best for:** Finance teams, accountants, business owners

**What it does:** Categorizes business expenses with proper tax treatment and policy compliance. Assigns GL codes, determines deductibility, and flags policy violations.

**When to use:**
- Processing expense receipts
- Categorizing transactions for bookkeeping
- Checking tax deductibility
- Identifying policy violations

**Example prompt:**
> "Categorize this batch of expenses and identify any that exceed policy limits or have tax implications."

</details>

<details>
<summary><strong>ai-maturity-assessor</strong> — Assess organizational AI transformation readiness</summary>

**Best for:** AI consultants, transformation leads, strategy teams

**What it does:** Conducts structured diagnostic assessments evaluating AI maturity across four phases: Foundations (governance, data, executive alignment), AI Fluency (literacy, champions, learning), Scope & Prioritize (use case intake, evaluation), and Build & Scale (cross-functional teams, deployment). Generates quantitative scores, identifies capability gaps, and produces 12-18 month transformation roadmaps with investment estimates and ROI projections.

**When to use:**
- Evaluating a client's AI readiness before planning initiatives
- Creating AI transformation roadmaps with investment estimates
- Identifying capability gaps preventing progression from experimentation to maturity
- Benchmarking against industry standards

**Example prompt:**
> "Assess our organization's AI maturity level and create a transformation roadmap with investment estimates."

</details>

<details>
<summary><strong>software-research-analyst</strong> — Strategic software evaluation for major purchases</summary>

**Best for:** IT leaders, procurement teams, business analysts

**What it does:** Conducts systematic software research for decisions worth $50K+ annually using an 11-section template: vendor stability, feature analysis, technical architecture, user experience, pricing/TCO, security, support, implementation risks, decision matrix, strategic recommendation, and next steps. Produces executive-ready recommendations with evidence-based scoring.

**When to use:**
- Evaluating 2-5 finalist tools for major software purchases
- Justifying software choices to executives or board
- Calculating total cost of ownership over 3 years
- Creating vendor comparison matrices with weighted scoring

**Example prompt:**
> "Evaluate HubSpot, Salesforce, and Pipedrive for our 50-person sales team with $100K 3-year budget."

</details>

<details>
<summary><strong>tool-research-architect</strong> — Comprehensive tool research with LLM integration focus</summary>

**Best for:** AI consultants, solution architects, technical evaluators

**What it does:** Conducts comprehensive tool research using a 6-section framework: identity, description, primary/secondary use cases, pricing, and LLM connection analysis. Special emphasis on evaluating integration quality with ChatGPT, Claude, Gemini, and Copilot—categorizing as Official Integration, MCP Server, API Available, Community Integration, or None.

**When to use:**
- Researching tools with focus on AI/LLM integration capabilities
- Building tool comparison documents for client recommendations
- Creating competitive landscapes with Jobs-to-be-Done analysis
- Evaluating how tools connect to major LLM platforms

**Example prompt:**
> "Research these 10 GTM automation tools, focusing on their LLM integration capabilities and pricing."

</details>

---

## AI & Automation

Skills for working with AI APIs, prompts, and automation.

<details>
<summary><strong>anthropic-messages-api</strong> — Implement Anthropic's Claude API</summary>

**Best for:** AI developers, backend engineers, integration specialists

**What it does:** Implements and troubleshoots Anthropic Messages API calls including model selection, tool use blocks, streaming, response parsing, structured outputs, and prompt caching. Covers advanced patterns like tool runners and Message Batches API.

**When to use:**
- Integrating Claude via the Messages API
- Implementing tool use with Claude
- Handling streaming responses
- Troubleshooting API issues

**Example prompt:**
> "Help me implement Claude API integration with tool use for a customer support bot."

</details>

<details>
<summary><strong>openai-responses-api</strong> — Implement OpenAI's Responses API</summary>

**Best for:** AI developers, backend engineers, integration specialists

**What it does:** Implements and troubleshoots OpenAI Responses API calls including model selection, built-in tools (web search, file search, code interpreter), output parsing, and conversation state management. Covers migrating from Chat Completions API and tool output customization.

**When to use:**
- Integrating OpenAI models via Responses API
- Migrating from Chat Completions API
- Enabling built-in tools
- Troubleshooting API issues

**Example prompt:**
> "Migrate our Chat Completions integration to the new Responses API with web search enabled."

</details>

<details>
<summary><strong>ai-art-generation</strong> — Guide AI image generation</summary>

**Best for:** Game developers, creative teams, digital artists

**What it does:** Guides AI image generation for game assets and creative projects. Covers prompt engineering for Midjourney, DALL-E, Stable Diffusion, with focus on iterative refinement and style consistency.

**When to use:**
- Generating pixel art game assets and sprites
- Creating consistent visual styles across asset batches
- Iterating on and refining AI-generated images (3-5 cycles)
- Validating output quality before engine integration
- Selecting the right tool (Midjourney, DALL-E, Stable Diffusion)

**Example prompt:**
> "Help me create prompts for generating a consistent set of fantasy character portraits in pixel art style."

</details>

<details>
<summary><strong>clay-mastery</strong> — Build Clay.com data enrichment and GTM automation workflows</summary>

**Best for:** RevOps teams, sales operations, growth marketers

**What it does:** Provides implementation guidance for Clay.com workflows including waterfall enrichment (query multiple providers until data found), Claygent AI research (Helium, Neon, Argon, Navigator models), formula generation, and credit optimization. Covers outbound prospecting, inbound automation, CRM enrichment, and signal monitoring patterns.

**When to use:**
- Building prospect lists with email/phone waterfall enrichment
- Configuring Claygent for AI-powered research
- Optimizing credit usage across 150+ data providers
- Creating inbound lead scoring and routing workflows

**Example prompt:**
> "Build a Clay workflow: LinkedIn Sales Nav import → company filter → email waterfall → AI personalization → Smartlead export."

</details>

<details>
<summary><strong>n8n-workflow-patterns</strong> — 5 core workflow architectures for n8n</summary>

**Best for:** Automation engineers, solution architects, anyone starting n8n workflows

**What it does:** Provides proven architectural patterns based on real workflow analysis: Webhook Processing (35% of workflows), HTTP API Integration, Database Operations, AI Agent Workflows, and Scheduled Tasks. Includes pattern selection guide, workflow creation checklist, data flow patterns, and common gotchas.

**When to use:**
- Starting a new n8n workflow and choosing architecture
- Deciding between webhook vs scheduled vs API patterns
- Building AI agent workflows with tools and memory
- Understanding workflow statistics and best practices

**Example prompt:**
> "What pattern should I use for a Slack bot that queries our database and responds with formatted data?"

</details>

<details>
<summary><strong>n8n-mcp-tools-expert</strong> — Master guide for n8n MCP server tools</summary>

**Best for:** Anyone building n8n workflows programmatically

**What it does:** Complete guide for using n8n-mcp tools effectively. Covers search_nodes, get_node (with detail levels), validate_node (with profiles), workflow creation, and template deployment. Explains critical differences like nodeType formats (`nodes-base.*` vs `n8n-nodes-base.*`) and smart parameters for IF/Switch connections.

**When to use:**
- Finding nodes with search_nodes
- Understanding node configuration with get_node
- Validating configurations before deployment
- Creating and updating workflows via API

**Example prompt:**
> "How do I use get_node to understand Slack node configuration? What detail level should I use?"

</details>

<details>
<summary><strong>n8n-node-configuration</strong> — Operation-aware configuration with property dependencies</summary>

**Best for:** Anyone configuring n8n nodes

**What it does:** Explains that different operations require different fields (Slack post vs update), how displayOptions control field visibility, and the progressive discovery workflow. Guides when to use `detail="standard"` (95% of cases) vs `search_properties` vs `detail="full"`.

**When to use:**
- Configuring nodes and unsure what fields are required
- Understanding why fields appear/disappear based on selections
- Debugging "field not found" or "required field missing" issues
- Choosing between get_node detail levels

**Example prompt:**
> "Why does my HTTP Request node suddenly require sendBody when I switch to POST method?"

</details>

<details>
<summary><strong>n8n-validation-expert</strong> — Interpret validation errors and fix them</summary>

**Best for:** Anyone debugging n8n workflow issues

**What it does:** Explains validation severity levels (errors must fix, warnings should fix, suggestions optional), the iterative validation loop (avg 2-3 cycles, 23s thinking + 58s fixing), auto-sanitization system, and common false positives. Covers all error types: missing_required, invalid_value, type_mismatch, invalid_expression, invalid_reference.

**When to use:**
- Getting validation errors and need to understand them
- Deciding which validation profile to use
- Understanding auto-sanitization behavior
- Recognizing false positives vs real issues

**Example prompt:**
> "I'm getting a 'missing_required' error on my Slack node but I think I have all fields. Help me debug."

</details>

<details>
<summary><strong>n8n-expression-syntax</strong> — Write correct n8n expressions with {{}} syntax</summary>

**Best for:** Anyone writing dynamic content in n8n workflows

**What it does:** Explains n8n expression format (`{{expression}}`), core variables ($json, $node, $now, $env), the critical webhook data structure (data is under `.body`!), and when NOT to use expressions (Code nodes, webhook paths, credentials). Includes validation rules and common mistakes.

**When to use:**
- Writing expressions in n8n workflow fields
- Accessing data from webhooks (remember `.body`!)
- Referencing other nodes with $node
- Debugging "undefined" or expression syntax errors

**Example prompt:**
> "Why is `{{$json.email}}` returning undefined when my webhook clearly sends email in the body?"

</details>

<details>
<summary><strong>n8n-code-javascript</strong> — Write JavaScript in n8n Code nodes</summary>

**Best for:** Anyone writing custom logic in n8n workflows

**What it does:** Complete guide for JavaScript Code nodes: mode selection (Run Once for All Items vs Each Item), data access patterns ($input.all(), $input.first(), $input.item, $node), return format requirements (`[{json: {...}}]`), built-in functions ($helpers.httpRequest, DateTime/Luxon, $jmespath), and the top 5 mistakes with fixes.

**When to use:**
- Writing Code nodes for transformations or custom logic
- Choosing between "All Items" and "Each Item" modes
- Using $helpers for HTTP requests or DateTime for dates
- Debugging Code node errors

**Example prompt:**
> "Write a Code node that aggregates sales data from multiple items and returns total, count, and average."

</details>

<details>
<summary><strong>n8n-code-python</strong> — Write Python in n8n Code nodes (with limitations)</summary>

**Best for:** Python developers who need n8n Code nodes

**What it does:** Guide for Python Code nodes with an important caveat: **use JavaScript for 95% of cases**. Explains Python limitations (no external libraries—no requests, pandas, numpy), what IS available (standard library only), data access with `_input`/`_json`/`_node`, and when Python actually makes sense (statistics module, strong Python preference).

**When to use:**
- Deciding between Python and JavaScript for Code nodes
- Writing Python when you specifically need standard library functions
- Understanding Python's limitations in n8n
- Migrating from Python to JavaScript when needed

**Example prompt:**
> "I want to use pandas in my n8n Code node. Is that possible?" (Answer: No, but here's what you can do instead)

</details>

<details>
<summary><strong>prompt-engineering</strong> — Comprehensive prompt patterns for Claude, GPT, and Gemini</summary>

**Best for:** AI developers, prompt engineers, LLM application builders

**What it does:** Provides 45+ prompt patterns across content creation, analysis, code generation, problem-solving, and education. Includes model-specific optimizations for Claude 4.5 (extreme explicitness, XML tags), GPT-5.1 (persistence instructions, adaptive reasoning), and Gemini 3.0 Pro (context-first, temperature 1.0). Contains production-ready system prompt templates.

**When to use:**
- Writing prompts optimized for specific models
- Building AI agents or complex workflows
- Auditing and improving existing prompts
- Generating production system prompt templates

**Example prompt:**
> "Optimize this prompt for Claude 4.5 with tool use. Apply the appropriate patterns for autonomous coding."

</details>

<details>
<summary><strong>client-prompt-coach-builder</strong> — Generate customized prompt coaching CustomGPTs</summary>

**Best for:** AI consultants, client success teams, training specialists

**What it does:** Automates creation of client-specific Prompt Engineering Coach CustomGPTs by analyzing project knowledge bases. Extracts context about industry, personas, and tasks, then generates deployment-ready CustomGPT instructions (<8,000 chars) and team user guides with real persona examples and before/after prompts.

**When to use:**
- Deploying prompt coaching to new clients
- Creating industry-specific prompt training materials
- Building CustomGPTs with client context baked in
- Updating existing prompt coaches with new personas

**Example prompt:**
> "Build a prompt coach CustomGPT for our real estate client. Analyze their KB and generate instructions + user guide."

</details>

---

## Internal & Specialty

Specialized skills and meta-tools.

<details>
<summary><strong>skill-creator</strong> — Create new skills for this library</summary>

**Best for:** Skill authors, platform developers

**What it does:** Meta-skill for creating new skills that extend Claude's capabilities. Guides SKILL.md structure, frontmatter, progressive disclosure, and bundled resources.

**When to use:**
- Creating a new skill
- Validating skill structure
- Packaging skills for distribution
- Understanding skill authoring best practices

**Example prompt:**
> "Help me create a new skill for [domain]. Guide me through the structure and best practices."

</details>

<details>
<summary><strong>vibe-coding</strong> — Rapidly prototype web applications</summary>

**Best for:** Developers, indie hackers, prototypers

**What it does:** Rapidly prototypes and builds modern, responsive web applications from scratch. Local alternative to tools like Lovable, Bolt, and v0 with full control.

**When to use:**
- Building quick web app prototypes
- Creating MVPs rapidly
- Experimenting with ideas
- Building demos and proof-of-concepts

**Example prompt:**
> "Build a simple task management app with drag-and-drop, local storage, and a clean modern UI."

</details>

<details>
<summary><strong>browser</strong> — Automate browser interactions</summary>

**Best for:** Automation engineers, QA specialists, scrapers

**What it does:** Provides Chrome DevTools Protocol tools for browser automation and scraping. Start Chrome, navigate pages, execute JavaScript, take screenshots, and interact with DOM elements.

**When to use:**
- Automating repetitive browser tasks
- Scraping web data
- Taking screenshots programmatically
- Testing web interactions

**Example prompt:**
> "Navigate to this page, fill out the form, and capture a screenshot of the result."

</details>

<details>
<summary><strong>slack-gif-creator</strong> — Create animated GIFs for Slack</summary>

**Best for:** Team communicators, documentation creators

**What it does:** Creates animated GIFs optimized for Slack using programmatic graphics drawing (PIL/ImageDraw). Provides utilities for animation, easing functions, optimization, and proper sizing for chat platforms. Note: This is for generating GIFs with code, not screen recording.

**When to use:**
- Creating demo GIFs for Slack
- Documenting features visually
- Making quick tutorial animations
- Sharing visual updates with teams

**Example prompt:**
> "Create a GIF showing how to use the new feature, optimized for Slack."

</details>

<details>
<summary><strong>cadre-os</strong> — Cadre AI consulting operating system</summary>

**Best for:** Cadre consultants and team members

**What it does:** Cadre AI's consulting operating system for strategy engagements. Handles discovery sessions, client context, synthesis, deliverables, and branded outputs.

**When to use:**
- Preparing for discovery sessions
- Debriefing after client calls
- Creating strategy decks and reports
- Managing tech stack assessments

**Example prompt:**
> "/prep [Client Name] — Prepare for upcoming discovery session"

</details>

<details>
<summary><strong>documentation-templates</strong> — Generate structured documentation</summary>

**Best for:** Technical writers, developers, team leads

**What it does:** Generates README files, API documentation, and inline code comments following best practices. Creates consistent, well-structured documentation.

**When to use:**
- Creating project READMEs
- Documenting APIs
- Adding code comments
- Building documentation templates

**Example prompt:**
> "Generate a comprehensive README for this project including setup, usage, and API documentation."

</details>

<details>
<summary><strong>frontend-ui-integration</strong> — Integrate frontend with existing APIs</summary>

**Best for:** Frontend developers, full-stack engineers

**What it does:** Implements or extends user-facing workflows in web applications, integrating with existing backend APIs. Follows design system, routing, and testing conventions.

**When to use:**
- Building new UI features backed by existing APIs
- Integrating frontend with backend services
- Following established frontend patterns
- Creating consistent UI workflows

**Example prompt:**
> "Build a user settings page that integrates with our existing user API and follows our design system."

</details>

<details>
<summary><strong>service-integration</strong> — Integrate services in shared codebases</summary>

**Best for:** Backend developers, platform engineers

**What it does:** Extends or integrates services in shared monorepos while preserving ownership boundaries, reliability standards, and observability requirements.

**When to use:**
- Adding backend APIs in shared codebases
- Integrating with existing services
- Maintaining service boundaries
- Following monorepo conventions

**Example prompt:**
> "Add a new notification service that integrates with our existing user service in the monorepo."

</details>

<details>
<summary><strong>internal-tools</strong> — Build internal operational tools</summary>

**Best for:** Internal tools developers, operations teams

**What it does:** Designs and implements internal tools that help employees operate systems safely. Respects access controls and audit requirements.

**When to use:**
- Building admin dashboards
- Creating internal operational tools
- Implementing access-controlled interfaces
- Building audit-compliant tools

**Example prompt:**
> "Build an internal tool for customer support to view and manage user subscriptions with proper access logging."

</details>

<details>
<summary><strong>cadre-block-builder</strong> — Create implementation blocks for client SOWs</summary>

**Best for:** Cadre project managers, account leads, SOW authors

**What it does:** Creates month-by-month implementation blocks using compositional activity clusters (Discovery, Process Design, Integration, Custom Development, Automation, AI/LLM, Testing, Deployment, Training, Optimization). Generates both internal versions (risks, confidence scores, technical notes) and client-facing versions (executive summaries, business outcomes). Enforces strategy/implementation boundary separation.

**When to use:**
- Planning new client engagements or SOW components
- Defining project phases with month-by-month execution plans
- Creating blocks for proposals or schedules
- Generating dual internal/client documentation

**Example prompt:**
> "Create a 3-month implementation block for a Salesforce-HubSpot integration project with discovery and training phases."

</details>

<details>
<summary><strong>clickup-automation-architect</strong> — Design ClickUp automations for consulting workflows</summary>

**Best for:** Cadre operations team, project managers

**What it does:** Designs and implements ClickUp automations optimized for consulting workflows and the 10,000/month Business tier limit. Provides ready-to-use recipes for client onboarding, milestone alerts, approval routing, and time entry detection. Includes limit optimization strategies and troubleshooting guides.

**When to use:**
- Building automations for client onboarding sequences
- Creating approval workflows with status-based triggers
- Optimizing automation usage against monthly limits
- Troubleshooting failing or unexpected automations

**Example prompt:**
> "Build a ClickUp automation that triggers when a task enters 'Pending Approval' and notifies the assigned approver."

</details>

<details>
<summary><strong>clickup-guide</strong> — ClickUp structure and permissions for consulting firms</summary>

**Best for:** Cadre operations team, new team members

**What it does:** Provides consulting-firm-specific ClickUp guidance for structure (Space vs Folder vs List), permissions and guest access, custom fields, feature selection (subtasks vs checklists, docs vs descriptions), views/dashboards, and time tracking. Optimized for 30-person teams on Business tier with client guest access needs.

**When to use:**
- Organizing client projects in ClickUp
- Setting up permissions for client guests
- Choosing between subtasks and checklists
- Deciding on custom field configuration

**Example prompt:**
> "How should I organize our new client's project in ClickUp with proper folder structure and guest permissions?"

</details>

<details>
<summary><strong>onboarding</strong> — Generate comprehensive onboarding documentation</summary>

**Best for:** Cadre consultants, team leads, HR

**What it does:** Generates comprehensive onboarding documentation for three scenarios: (1) Client Engagement Onboarding for consultants joining existing engagements (30-50 page strategic briefs), (2) Employee-to-Client for team members joining delivery teams (15-25 page operational docs), (3) Employee-to-Pod for new hires joining internal teams. Analyzes contracts, discovery intelligence, and stakeholder context.

**When to use:**
- Onboarding a consultant to an existing client engagement
- Bringing a new team member onto a client delivery team
- Creating handoff documentation for account transitions
- Preparing strategic briefs for incoming strategists

**Example prompt:**
> "Onboard me to the Hyperion engagement. Generate a strategic handoff with contracts, stakeholders, and execution playbook."

</details>

<details>
<summary><strong>project-resource-planner</strong> — Convert SOWs to ClickUp resource allocation plans</summary>

**Best for:** Cadre project managers, resource planners

**What it does:** Transforms semi-structured SOWs into detailed week-by-week resource allocation plans for ClickUp. Creates hierarchical structure (Initiative → Monthly Goals → Weekly Goals → Sub-tasks) with SMART goals, hour estimates for AI Managers/Strategists/Engineers, and role-tagged sub-tasks. Generates optional weekly calendar views and CSV exports for ClickUp import.

**When to use:**
- Converting client SOWs into detailed project plans
- Planning 2-12 month consulting engagements
- Allocating hours across AI Manager, Strategist, and Engineer roles
- Creating ClickUp-importable resource schedules

**Example prompt:**
> "Convert this 6-month SOW into a resource allocation plan with weekly breakdowns and hour estimates by role."

</details>

---

## Need Something Else?

If none of these skills fit your needs:

1. **Ask Claude directly** — Many tasks don't require a specialized skill
2. **Check if a skill exists** — Skills auto-activate, so you might already have what you need
3. **Create a new skill** — Use the `skill-creator` skill to build your own

---

*This catalog contains 66 skills. Skills are auto-detected by the presence of a SKILL.md file. Run the validation script to verify all skills are documented.*
