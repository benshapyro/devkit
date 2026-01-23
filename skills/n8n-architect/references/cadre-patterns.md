# Cadre Client Workflow Patterns

Proven automation templates for client engagements and internal operations.

## Client Engagement Workflows

### 1. Rapid Assessment Automation

**Trigger:** New client intake form submission
**Process:**
1. Extract client data (industry, size, pain points, budget)
2. Query internal knowledge base for similar client patterns
3. Generate hypothesis matrix (problem → solution → ROI)
4. Score opportunities using Cadre's value framework
5. Draft initial assessment report with recommendations

**Outputs:**
- Opportunity map (MECE framework)
- ROI projection (3-5x target)
- Risk assessment matrix
- Recommended engagement scope

**N8N Components:**
- Webhook trigger (form submission)
- HTTP Request (knowledge base API)
- AI Agent (hypothesis generation)
- Google Docs (report generation)
- Gmail (delivery to engagement team)

### 2. Strategy Delivery Pipeline

**Trigger:** Strategy workshop completion
**Process:**
1. Compile workshop notes and client data
2. Apply MECE analysis to identify solution areas
3. Generate hypothesis statements for validation
4. Create recommendation framework with evidence
5. Build executive presentation with ROI models

**Outputs:**
- Strategy framework document
- Hypothesis validation plan
- Implementation roadmap
- Executive presentation deck

**N8N Components:**
- Schedule trigger (post-workshop)
- Google Drive (notes collection)
- AI Agent (MECE analysis)
- PowerPoint generation
- Slack (stakeholder notification)

### 3. Implementation Support System

**Trigger:** Project kickoff or weekly check-in
**Process:**
1. Collect progress data from project management tools
2. Analyze velocity and identify blockers
3. Apply pilot → lighthouse → scale framework
4. Generate status report with recommendations
5. Alert on risks or delays requiring intervention

**Outputs:**
- Weekly status dashboard
- Risk/issue alerts
- Scaling readiness assessment
- Stakeholder communication

**N8N Components:**
- Schedule trigger (weekly)
- Asana/Jira API (project data)
- AI Agent (progress analysis)
- Conditional logic (risk detection)
- Multi-channel notifications

### 4. Client Communication Hub

**Trigger:** Milestone completion or scheduled update
**Process:**
1. Aggregate metrics from multiple systems
2. Translate technical progress to business outcomes
3. Format insights for different stakeholder levels
4. Distribute via appropriate channels
5. Track engagement and response rates

**Outputs:**
- Executive summaries (C-suite)
- Operational updates (project teams)
- Technical briefs (IT teams)
- Board-ready metrics

**N8N Components:**
- Multiple triggers (event + schedule)
- Data aggregation (SQL queries)
- AI Agent (audience-specific formatting)
- Multi-channel delivery (email, Slack, dashboard)
- Analytics tracking

## Internal Efficiency Accelerators

### 5. Proposal Generation Engine

**Trigger:** RFP received or proposal request
**Process:**
1. Extract RFP requirements and evaluation criteria
2. Match to Cadre's service offerings and case studies
3. Apply Cadre methodologies to solution design
4. Generate proposal with ROI models and timelines
5. Include relevant case studies and team bios

**Outputs:**
- Complete RFP response
- Budget breakdown
- Timeline/milestone plan
- Supporting materials

**N8N Components:**
- Email trigger (RFP receipt)
- AI Agent (requirement extraction)
- Vector database (case study matching)
- Document generation (branded template)
- Review workflow (approval gates)

### 6. Client Onboarding Automation

**Trigger:** Contract signed
**Process:**
1. Create client workspace (folders, channels, projects)
2. Generate onboarding documentation
3. Schedule kickoff meetings with calendar integration
4. Assign team members and set permissions
5. Initialize project tracking and communication protocols

**Outputs:**
- Configured client workspace
- Onboarding document package
- Scheduled meeting series
- Team assignments

**N8N Components:**
- Webhook (contract signature)
- Multi-API integration (Drive, Slack, Asana, Calendar)
- Template processing
- Team notification system
- Audit logging

### 7. Knowledge Management System

**Trigger:** Project completion or learning moment
**Process:**
1. Extract key insights from project documentation
2. Identify reusable patterns and methodologies
3. Tag and categorize for discoverability
4. Update internal knowledge base
5. Notify relevant teams of new learnings

**Outputs:**
- Structured case studies
- Methodology refinements
- Best practice repository updates
- Team learning notifications

**N8N Components:**
- Manual trigger (project closure)
- AI Agent (insight extraction)
- Vector database (knowledge storage)
- Tagging/categorization logic
- Team communication

### 8. Performance Analytics Dashboard

**Trigger:** Real-time data updates or scheduled aggregation
**Process:**
1. Collect metrics from all client projects
2. Calculate KPIs (client satisfaction, delivery velocity, ROI)
3. Identify trends and anomalies
4. Generate actionable insights
5. Alert leadership on significant changes

**Outputs:**
- Real-time dashboard
- Weekly performance reports
- Trend analysis
- Improvement recommendations

**N8N Components:**
- Multiple data source integrations
- SQL aggregation
- AI Agent (trend analysis)
- Dashboard updates (Tableau/Looker API)
- Alert system (threshold-based)

## Standard Integration Templates

### CRM → Project Management → Communication
**Use case:** New deal closed → project created → team notified
**Components:**
- HubSpot/Salesforce webhook
- Asana/Jira project creation
- Slack channel creation
- Calendar event scheduling
- Email welcome sequence

### Time Tracking → Invoicing → Reporting
**Use case:** Weekly time compilation → invoice generation → revenue tracking
**Components:**
- Harvest/Toggl API
- Invoice generation (QuickBooks/Xero)
- Financial reporting (Google Sheets)
- Stakeholder notification
- Accounting system integration

### Lead Qualification → Opportunity Scoring → Engagement
**Use case:** Inbound lead → AI qualification → routing to sales
**Components:**
- Form submission webhook
- AI Agent (qualification criteria)
- CRM enrichment
- Scoring algorithm
- Sales team assignment and notification

### Resource Allocation → Capacity Planning → Performance
**Use case:** Project demand → team availability → optimization recommendations
**Components:**
- Resource management API
- Capacity calculation logic
- Optimization algorithms
- Dashboard visualization
- Staffing recommendations

## Cadre Methodology Integration

### MECE Analysis Automation
```
Apply to workflow outputs to ensure:
- Mutually Exclusive: No overlapping categories
- Collectively Exhaustive: All possibilities covered
```

### Hypothesis-Driven Discovery
```
Framework structure:
- Hypothesis statement
- Validation criteria
- Evidence requirements
- Decision triggers
```

### 10-20-70 Rule Application
```
Workflow design must consider:
- 10% algorithms/AI capabilities
- 20% technology/data infrastructure  
- 70% process/people change management
```

### 3-5x ROI Standard
```
Every automation must demonstrate:
- Cost baseline (manual process)
- Time savings quantification
- Error reduction value
- Scalability benefits
- Minimum 3x return within 12 months
```

## Workflow Quality Checklist

**Before Delivery:**
- [ ] Business value clearly quantified
- [ ] Cadre methodology properly applied
- [ ] Security requirements implemented
- [ ] Error handling comprehensive
- [ ] Scalability considerations addressed
- [ ] Documentation complete and professional
- [ ] Client adoption plan included
- [ ] Monitoring and maintenance defined