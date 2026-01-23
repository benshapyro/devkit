# Research Quality Guide

Load this file when validating research quality or when unsure what "deep research" actually means in practice.

## Core Quality Principle

**Don't just copy marketing claims.** Research means digging into real user experiences, finding hidden costs, verifying claims, and identifying trade-offs.

---

## Good vs Bad Research Examples

### Example 1: Pricing Analysis

**❌ Surface-level (DON'T DO THIS):**
> "HubSpot offers email marketing starting at $15/month. It integrates with Salesforce."

**✅ Deep research (DO THIS):**
> "HubSpot's Marketing Hub starts at $15/user/month but requires a 2-seat minimum ($30/month). At this tier, email marketing is limited to 1,000 sends/month. Based on 247 G2 reviews from 50-100 employee companies, most businesses need the $800/month Professional tier for unlimited marketing contacts and advanced automation. The Salesforce integration is bi-directional but requires the $50/month Operations Hub add-on, and users report sync delays of 5-15 minutes. Total 3-year TCO for a 50-person team: $43,800 including $5,000 implementation and $800/year extra storage."

**What makes it deep:**
- Specific constraints (2-seat minimum, 1,000 email limit)
- Evidence from reviews (247 reviews, specific company sizes)
- Real limitations (sync delays with timing)
- Hidden costs ($50/month add-on)
- Total cost calculated (3-year TCO with all components)

---

### Example 2: Feature Evaluation

**❌ Surface-level:**
> "Has email marketing and workflow automation features."

**✅ Deep research:**
> "Email builder rated 4.5/5 by users (praised for drag-and-drop simplicity and template library). Workflow automation rated 3.2/5 - users report steep learning curve with 18% of recent reviews mentioning difficulty creating conditional logic. The automation engine supports if/then branches and delays but lacks loop functionality available in competitors like ActiveCampaign. Maximum of 50 workflows on Pro tier (vs unlimited on Enterprise)."

**What makes it deep:**
- Quality ratings from actual users (4.5/5, 3.2/5)
- Specific complaints (18% mention learning curve)
- Feature limitations (no loops, 50 workflow max)
- Comparison to competitors (ActiveCampaign has loops)

---

### Example 3: Integration Assessment

**❌ Surface-level:**
> "Integrates with Salesforce, Slack, and many other popular tools."

**✅ Deep research:**
> "Native integrations with 500+ apps including Salesforce, Slack, Shopify. Salesforce integration quality varies by review: enterprise customers praise the bi-directional sync for contacts and deals, but 12% of reviews mention issues with custom field mapping. Slack integration is one-way only (HubSpot → Slack notifications). API rate limit is 100 requests per 10 seconds (lower than Salesforce's 15,000/day), which caused issues for 3 reviewers running large data syncs. Zapier integration available with 50 triggers and 30 actions. Make.com and n8n supported but marked as 'community maintained' with limited documentation."

**What makes it deep:**
- Specific integration count (500+)
- Quality nuances (enterprise praise but custom field issues)
- Limitations documented (one-way Slack, API rate limits)
- Real user impact (3 reviewers hit limits)
- Integration platform coverage with details

---

### Example 4: Support Quality

**❌ Surface-level:**
> "Offers email, phone, and chat support."

**✅ Deep research:**
> "Support channels include email (24-hour average response time), phone (9am-5pm ET, Mon-Fri), and live chat (included in Pro+ tiers only). Based on 156 support-related reviews from the past 6 months: Response times increased from 6 hours to 24 hours compared to a year ago. 15% of recent reviews specifically complain about support quality declining after company moved to offshore team in Q2 2024. First-contact resolution dropped from ~70% to ~45% based on review mentions. Premium support ($500/month) provides 1-hour response time and dedicated Slack channel, which consistently receives 4.5/5 ratings."

**What makes it deep:**
- Specific response times (24 hours average)
- Availability details (9am-5pm ET, Mon-Fri)
- Trend analysis (6 hours → 24 hours over time)
- Specific complaints (15% mention offshore issues)
- Premium tier details and ratings

---

### Example 5: Security & Compliance

**❌ Surface-level:**
> "SOC 2 compliant and uses encryption."

**✅ Deep research:**
> "SOC 2 Type II certified (report dated August 2024, verified on vendor security page). Uses AES-256 encryption at rest and TLS 1.3 in transit. HIPAA compliant with BAA available (requires Enterprise tier minimum). Data centers in US (Virginia, Oregon), EU (Frankfurt), and APAC (Sydney) with residency controls at Enterprise tier. Status page shows 99.96% actual uptime over past 12 months (vs 99.9% SLA). One security incident in March 2024: unauthorized access to 3 customer accounts via credential stuffing, disclosed within 72 hours, affected customers notified, mandatory password resets implemented. Bug bounty program active via HackerOne since 2022."

**What makes it deep:**
- Certification verified with date (August 2024)
- Specific encryption standards (AES-256, TLS 1.3)
- Compliance nuances (HIPAA needs Enterprise tier)
- Data residency options with locations
- Actual vs promised uptime (99.96% vs 99.9%)
- Security incident history with response details
- Security practices (bug bounty program)

---

### Example 6: User Experience Analysis

**❌ Surface-level:**
> "Users say it's easy to use with a modern interface."

**✅ Deep research:**
> "UI rated 4.2/5 for modern design but 3.4/5 for navigation complexity. Common praise (65 mentions): clean dashboard, intuitive contact management. Common complaints (42 mentions): report builder requires 5-7 clicks for simple reports, mobile app lacks key features (can't create workflows, limited to viewing only). Learning curve: reviews from new users (< 3 months) average 3.1/5 difficulty; experienced users (6+ months) average 4.3/5. Admin setup: 8-12 hours typical for basic configuration based on implementation timelines in reviews. End users: 2-3 hours to basic proficiency. Migration from Salesforce specifically mentioned as 'painful' in 8 reviews due to different data model."

**What makes it deep:**
- Separate ratings for different aspects (4.2/5 design, 3.4/5 navigation)
- Quantified mentions (65 praise, 42 complaints)
- Specific pain points (5-7 clicks for reports)
- Learning curve by experience level
- Time estimates from real users
- Migration-specific feedback

---

## Information Quality Requirements

### Source Priority

Use sources in this priority order:

1. **Official vendor documentation** (pricing, features, security)
   - Vendor website, help docs, status pages
   - Security/compliance pages
   - Official API documentation

2. **Third-party analyst reports** (Gartner, Forrester)
   - Most reliable for market positioning
   - Good for comparing multiple vendors
   - Often behind paywalls but valuable

3. **Review sites with verified users** (G2, Capterra, TrustRadius)
   - Filter by company size similar to yours
   - Recent reviews more valuable (< 6 months)
   - Look for detailed reviews (> 100 words)

4. **Community discussions** (Reddit, LinkedIn, Twitter)
   - Good for unfiltered opinions
   - Useful for finding edge cases
   - Verify multiple sources before trusting

5. **News articles and press releases**
   - Good for funding, acquisitions, major changes
   - Verify dates and sources
   - Watch for company-written vs independent journalism

### Always Include

For every major claim:

**Source**: Where did you find this?
- Good: "G2 review from CFO at 75-person SaaS company, posted Oct 2024"
- Good: "Vendor pricing page, accessed Nov 24, 2025"
- Bad: "Reviews say..." (which reviews?)
- Bad: "The vendor claims..." (where specifically?)

**Date**: When was this information current?
- Good: "as of November 2025"
- Good: "based on Oct 2024 pricing"
- Bad: No date mentioned
- Bad: "recently" (how recent?)

**Confidence Level**: How certain are you?
- Verified: Confirmed from official source
- Likely: Multiple sources agree
- Estimated: Based on incomplete information
- Unknown: Could not find information

### Handling Conflicting Information

When sources disagree:

1. **Note the discrepancy explicitly**
   - "Vendor website says $50/user/month, but G2 reviews mention $65/user/month after recent price increase"

2. **Use most recent official source**
   - "Using $65/user/month based on pricing page accessed Nov 24, 2025"

3. **Explain credibility**
   - "Status page shows 99.96% uptime, but vendor markets 99.99%. Using actual measured uptime."

---

## Red Flags by Category

### Company Health Red Flags

Watch for these warning signs about vendor stability:

**Critical (immediate concern):**
- Mass layoffs (>20% of staff) in past 6 months
- CEO or CTO departure in past 3 months
- Running out of runway (<6 months cash)
- Acquisition announced but uncertain
- Product being "sunset" or merged

**Moderate (monitor closely):**
- Funding struggles (failed to raise when expected)
- Key executive departures (VP level)
- Declining Glassdoor ratings (>0.5 stars in past year)
- Market share loss to competitors (>10% in past year)
- Negative press about company culture or practices

**Minor (note but not deal-breaker):**
- Normal executive turnover
- Single round of targeted layoffs
- Compensation/benefits changes
- Office relocations or downsizing

**How to assess:**
- Check Crunchbase for funding history
- Review LinkedIn for employee count trends
- Search news for recent layoffs or departures
- Check Glassdoor for culture trends

---

### Product Quality Red Flags

**Critical:**
- No meaningful product updates in 12+ months
- Major features removed or "deprecated"
- Frequent outages (>5 incidents per month)
- Data loss incidents in past year
- Critical security vulnerabilities unpatched >30 days

**Moderate:**
- Buggy releases mentioned in recent reviews (>20%)
- Roadmap promises not delivered (announced features >6 months late)
- Declining review scores (>0.3 stars in past year)
- API breaking changes without adequate notice
- Technical debt signals (old tech stack, no mobile apps)

**Minor:**
- Occasional bugs in new features
- Slow feature development
- Minor UI inconsistencies
- Limited customization options

**How to assess:**
- Check release notes for frequency and quality
- Review GitHub issues if API is public
- Read recent reviews specifically about bugs
- Check status page for incident history
- Look for "used to be great, now..." patterns

---

### Pricing Red Flags

**Critical:**
- Frequent price increases (>15% annually)
- Surprise charges not in contract
- Retroactive price changes mid-contract
- Unclear or deceptive pricing structure
- Required upgrades to maintain features

**Moderate:**
- Annual price increases (10-15%)
- Many hidden fees (storage, API calls, support)
- Confusing pricing tiers
- Minimum seat requirements (pay for 10, use 5)
- Price jumps between tiers (2x or more)

**Minor:**
- Standard annual escalation (3-5%)
- Premium features cost extra
- Overage charges for usage
- Annual commitment required

**How to assess:**
- Read reviews mentioning "price" or "cost"
- Calculate percentage of reviews mentioning price increases
- Check if pricing page shows "starting at" without full details
- Look for complaints about surprise charges

---

### Support Red Flags

**Critical:**
- No human support (chatbot only)
- Response times >5 days consistently
- Support moved offshore with quality collapse
- Tickets closed without resolution
- Support SLAs not met (>20% violation rate)

**Moderate:**
- Response times increasing over time (2x slower)
- First-contact resolution <50%
- Support only available in one timezone
- Premium support required for reasonable response
- Frequent support quality complaints (>25% of reviews)

**Minor:**
- Slow response on low-priority issues
- Limited phone support hours
- Knowledge base gaps
- Support via email only (no chat/phone)

**How to assess:**
- Calculate % of reviews mentioning support issues
- Note response time trends (improving or declining)
- Check support hours against your timezone
- Look for "support used to be great" patterns
- Verify support SLAs against user reports

---

### User Experience Red Flags

**Critical:**
- Consistently poor UX reviews (<3.0/5)
- "Unusable" mentioned in multiple reviews
- Mobile app broken or missing core features
- Accessibility issues (no keyboard nav, no screen reader support)
- Data loss through UI bugs

**Moderate:**
- High learning curve (>20 hours to proficiency)
- Clunky workflows (many clicks for common tasks)
- Poor mobile experience (app rated <3.5)
- Inconsistent UI across modules
- Heavy browser requirements (Chrome only)

**Minor:**
- Dated visual design
- Some features hard to find
- Customization limited
- Occasional UI bugs

**How to assess:**
- Filter reviews by "ease of use" rating
- Watch YouTube videos from real users (not vendor demos)
- Check app store ratings and reviews
- Look for specific workflow complaints
- Estimate learning curve from review mentions

---

### Integration & Technical Red Flags

**Critical:**
- Critical integrations don't actually work (broken)
- No API or extremely limited API
- Data export blocked or extremely difficult
- Vendor lock-in by design (can't extract data)
- API rate limits that break normal usage

**Moderate:**
- Integration quality varies significantly
- API documentation poor or outdated
- One-way syncs when bi-directional needed
- Sync delays >1 hour
- Limited webhook support

**Minor:**
- Some integrations require paid tier
- API has minor limitations
- Integration setup is complex
- Community integrations only (no official)

**How to assess:**
- Test critical integrations if possible
- Read API documentation quality
- Check for "integration issues" in reviews
- Look for data portability information
- Verify API rate limits match your needs

---

## Common Research Mistakes

### Mistake 1: Parroting Marketing

**What it looks like:**
- Copying feature lists from vendor website
- Using vendor's exact language and claims
- No verification or real user experiences
- All positive, no limitations mentioned

**Why it's wrong:**
Marketing is designed to sell, not inform objectively. Real research finds both strengths AND limitations.

**How to avoid:**
- Cross-reference every claim with reviews
- Look for specific user experiences
- Find the gaps between promise and reality
- Always include limitations discovered

---

### Mistake 2: Missing Hidden Costs

**What it looks like:**
- Only reporting advertised "starting at" price
- Ignoring implementation, training, support costs
- Missing add-on modules required for full functionality
- Not calculating actual TCO

**Why it's wrong:**
A $50/month tool can actually cost $20,000/year with all the extras.

**How to avoid:**
- Build full 3-year TCO model
- Check reviews for "surprise costs"
- Add up all required add-ons
- Include implementation and training
- Factor in storage, API overages, premium support

---

### Mistake 3: Ignoring Negative Signals

**What it looks like:**
- Only mentioning positive reviews
- Dismissing complaints as "outliers"
- Not investigating warning signs
- Assuming problems are resolved

**Why it's wrong:**
Negative signals often reveal critical issues that will impact you.

**How to avoid:**
- Specifically look for negative reviews
- Investigate patterns in complaints
- Check if issues were actually resolved
- Weigh negative signals appropriately

---

### Mistake 4: Insufficient Depth

**What it looks like:**
- Only reading vendor website
- Not checking reviews or community discussions
- Missing integration details
- No TCO calculation
- No risk assessment

**Why it's wrong:**
Surface research misses the information that matters most for the decision.

**How to avoid:**
- Use all 11 template sections
- Check multiple information sources
- Read 20+ relevant reviews
- Actually calculate costs
- Identify specific risks

---

### Mistake 5: No Comparison

**What it looks like:**
- Researching tools in isolation
- No side-by-side feature matrix
- No trade-off analysis
- Can't articulate why one tool is better

**Why it's wrong:**
Without comparison, you can't make an informed choice between options.

**How to avoid:**
- Create comparison matrices
- Explicitly identify trade-offs
- Use weighted scoring
- State which tool wins each category

---

## Quality Checklist

Before delivering research, verify:

### Completeness
- [ ] All required template sections completed
- [ ] Every critical requirement explicitly evaluated
- [ ] All comparison tables filled in
- [ ] Clear recommendation with rationale
- [ ] No "TBD" or placeholder content

### Accuracy
- [ ] Pricing includes dates (e.g., "as of Nov 2025")
- [ ] Source URLs or specific review mentions provided
- [ ] Review counts and ratings are current
- [ ] No contradictory information unresolved
- [ ] Confidence levels indicated (Verified/Likely/Estimated)

### Depth
- [ ] Goes beyond marketing materials
- [ ] Includes real user experiences (specific examples)
- [ ] Identifies hidden costs and limitations
- [ ] Addresses implementation risks
- [ ] Quantifies claims (not just "many users say...")

### Objectivity
- [ ] Presents both strengths AND weaknesses
- [ ] Doesn't just copy vendor marketing
- [ ] Acknowledges information gaps
- [ ] Separates facts from opinions
- [ ] Provides balanced perspective

### Utility
- [ ] Actionable recommendations
- [ ] Clear next steps with owners and dates
- [ ] Specific to the stated use case
- [ ] Decision-ready (enough to choose)
- [ ] Answers stakeholder questions

---

## When Research is "Good Enough"

**You've done enough research when:**

1. **Critical questions answered**
   - All must-have requirements clearly met or not met
   - Total cost calculated with confidence
   - Key risks identified with mitigation strategies
   - Integration capabilities verified

2. **Comparison is clear**
   - Can articulate specific trade-offs
   - Scoring shows clear winner or explains why close
   - Understand why each tool fits or doesn't fit

3. **Evidence-based**
   - Claims backed by sources
   - User experiences captured
   - Limitations documented
   - Costs verified

4. **Stakeholders can decide**
   - Recommendation is clear
   - Rationale is compelling
   - Next steps are defined
   - Objections anticipated and addressed

**You need to go deeper when:**

1. **Major unknowns remain**
   - Critical integration capabilities unclear
   - Pricing for your scale not confirmed
   - Implementation complexity uncertain
   - Key risks not understood

2. **Tools score very close**
   - Within 5 points on weighted scorecard
   - No clear winner on critical factors
   - Trade-offs not well understood

3. **High-risk decision**
   - Large investment (>$100K annually)
   - Hard to reverse (multi-year contract)
   - Complex implementation
   - Business-critical system

4. **Stakeholder questions unanswered**
   - Technical evaluation incomplete
   - ROI case not compelling
   - Risk assessment insufficient
   - Implementation plan unclear

---

**Remember: Deep research takes time but prevents expensive mistakes. Better to invest 10-15 hours in research than make a $100K wrong decision.**
