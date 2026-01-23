# LLM Integration Research Guide

## Overview

This guide helps you systematically research how software tools connect to major LLM platforms. This information is critical for AI consulting recommendations on automation opportunities.

## The Four LLM Platforms to Research

For EVERY tool, investigate connections to:

1. **OpenAI's ChatGPT** (most common, largest ecosystem)
2. **Anthropic's Claude** (growing rapidly, MCP focus)
3. **Google's Gemini** (enterprise focused, Google ecosystem)
4. **Microsoft's Copilot** (Microsoft 365 integration)

## Connection Types (Strongest → Weakest)

### 1. Official Integration

**What it is:** Built directly by the tool company or the LLM provider

**Look for:**
- "Official ChatGPT integration" or "Official Claude integration"
- "Built in partnership with [LLM Provider]"
- Announced on tool's official blog or press releases
- Listed in LLM provider's marketplace or partner directory

**Where to search:**
- Tool's official features page
- Integration or marketplace sections
- Recent press releases (2024-2025)
- LLM provider's partner directory

**Example findings:**
- "Official Integration - Zapier announced ChatGPT integration in partnership with OpenAI (Nov 2024)"
- "Official Integration - Built by Notion team, available in all paid plans"
- "Official Integration - Available in Claude.ai via official connection"

**Documentation format:**
```
**OpenAI ChatGPT:** Official Integration - Native connection available in Pro plan and above, announced Oct 2024
```

### 2. Official MCP Server

**What it is:** Model Context Protocol server maintained by the tool's official team

**Background:** MCP (Model Context Protocol) is a standard for connecting LLMs to external tools and data sources. Anthropic's Claude uses MCP extensively.

**Look for:**
- Official MCP server on tool's GitHub organization
- Listed in MCP server directories
- Announced by tool company in official channels

**Where to search:**
- GitHub: "site:github.com/[company] MCP server"
- Tool's developer documentation
- MCP directory listings
- Tool's official announcements

**Example findings:**
- "Official MCP Server - Maintained by Airtable team at github.com/airtable/mcp-server"
- "Official MCP Server - Available in Claude desktop app, documented at docs.toolname.com/mcp"

**Documentation format:**
```
**Anthropic Claude:** Official MCP Server - Maintained by tool team, available at github.com/[company]/mcp-server
```

### 3. Community MCP Server

**What it is:** MCP server built by third parties or community members, not officially maintained

**Look for:**
- MCP servers on GitHub by individual developers
- Community contributions and forks
- Not from the official company organization

**Where to search:**
- GitHub: "[Tool name] MCP server" (check author)
- MCP community directories
- Developer forums and discussions

**Example findings:**
- "Community MCP Server - Built by @username, 50+ stars on GitHub, actively maintained"
- "Community MCP Server - Available at github.com/community-dev/tool-mcp, last updated Nov 2025"

**Documentation format:**
```
**Anthropic Claude:** Community MCP Server - Built by @developer, 100+ stars, github.com/dev/tool-mcp
```

### 4. API Available

**What it is:** Tool has public API that CAN be connected to LLMs, but no pre-built integration exists

**Important distinction:** Having an API doesn't mean an integration exists—it means integration is POSSIBLE with custom development.

**Look for:**
- Public API documentation
- REST API or GraphQL endpoints
- Developer portal with authentication docs
- No pre-built LLM integrations mentioned

**Example findings:**
- "API Available - Public REST API at api.toolname.com, well-documented but no pre-built LLM integrations"
- "API Available - GraphQL API with authentication, could be connected via custom code or no-code tools"

**Documentation format:**
```
**OpenAI ChatGPT:** API Available - Public REST API documented at docs.toolname.com/api, no pre-built ChatGPT integration found
```

### 5. Community Integration

**What it is:** Third-party automation platforms that bridge the connection

**Look for:**
- Zapier apps and zaps
- Make.com (formerly Integromat) scenarios
- Pipedream workflows
- n8n nodes
- IFTTT applets

**Example findings:**
- "Community Integration - Available via Zapier with 10+ pre-built zaps for ChatGPT"
- "Community Integration - Make.com connector with ChatGPT templates available"

**Documentation format:**
```
**OpenAI ChatGPT:** Community Integration - Zapier connector available with 10+ pre-built automations
```

### 6. None

**What it is:** No documented way to connect after thorough research

**When to use:**
- After comprehensive research across all channels
- No API available
- No integrations exist
- Closed/proprietary system

**Example findings:**
- "None - No public API or documented integration method available"
- "None - Closed system with no external connections, confirmed via documentation review"

**Documentation format:**
```
**All platforms:** None - No public API or integration options available as of Nov 2025
```

## Research Methodology

### Phase 1: Official Features (Start Here)

**Search queries:**
```
"[Tool name] ChatGPT integration"
"[Tool name] Claude integration"
"[Tool name] AI features"
"[Tool name] OpenAI"
"[Tool name] Anthropic"
```

**Where to look:**
- Tool's main features page
- Integration marketplace or app directory
- "What's New" or announcements section
- Product roadmap if public

**Time: 2-3 minutes per platform**

### Phase 2: Developer Resources

**Search queries:**
```
"[Tool name] API documentation"
"[Tool name] developer portal"
"[Tool name] MCP server"
site:[tool-domain].com API
site:[tool-domain].com integration
```

**Where to look:**
- docs.[tool-domain].com
- developer.[tool-domain].com
- api.[tool-domain].com
- GitHub official organization

**Time: 2-3 minutes per platform**

### Phase 3: Recent Announcements

**Search queries:**
```
"[Tool name] AI" 2024..2025
"[Tool name] integration" 2024..2025
"[Tool name] ChatGPT" 2024..2025
"[Tool name] Claude" 2024..2025
site:github.com "[Tool name] MCP"
```

**Where to look:**
- Company blog
- Press releases
- Product Hunt launches
- Tech news sites (TechCrunch, VentureBeat)

**Time: 2-3 minutes per platform**

### Phase 4: Community Solutions

**Search queries:**
```
"[Tool name] Zapier"
"[Tool name] Make.com"
"[Tool name] automation ChatGPT"
site:github.com "[Tool name] MCP server"
```

**Where to look:**
- Zapier app directory
- Make.com apps listing
- GitHub (filter by stars/recent activity)
- Pipedream app directory

**Time: 2-3 minutes per platform**

## Platform-Specific Research Notes

### OpenAI ChatGPT

**Key characteristics:**
- Most mature integration ecosystem
- GPT Store for custom GPTs with actions
- Actions allow API connections to tools
- Many tools prioritize ChatGPT integration first

**Specific searches:**
- Check GPT Store: "site:chat.openai.com/g [Tool name]"
- Look for "ChatGPT Actions" in documentation
- Search for "GPT integration" on tool site

**Common integration types:**
- GPT Store custom GPTs (most common)
- Direct API integration via Actions
- Zapier/Make connectors

**Red flags:**
- "ChatGPT integration coming soon" (not yet available)
- Old announcements from 2023 (may be outdated)

### Anthropic Claude

**Key characteristics:**
- Rapidly growing ecosystem
- MCP (Model Context Protocol) is preferred integration method
- Projects feature allows file/data connections
- Strong focus on enterprise and developers

**Specific searches:**
- "[Tool name] MCP server" site:github.com
- "[Tool name] Claude integration"
- Check tool's developer docs for "Claude" or "Anthropic"

**Common integration types:**
- MCP servers (official or community)
- API connections via Projects
- Indirect via automation platforms

**Red flags:**
- Generic "AI integration" may not include Claude specifically
- MCP servers with no recent updates (check last commit date)

### Google Gemini

**Key characteristics:**
- Strong in Google Workspace ecosystem
- Often bundled with Google Cloud
- Enterprise-focused integrations
- Vertex AI platform for custom connections

**Specific searches:**
- "[Tool name] Gemini integration"
- "[Tool name] Google Cloud"
- "[Tool name] Vertex AI"
- Check if tool is in Google Workspace Marketplace

**Common integration types:**
- Google Workspace add-ons
- Vertex AI extensions
- Google Cloud integrations
- Direct API connections

**Red flags:**
- "Google AI" may refer to older Google AI Studio, not Gemini
- Workspace integrations may not include Gemini specifically

### Microsoft Copilot

**Key characteristics:**
- Strong Microsoft 365 ecosystem integration
- Power Automate connections common
- Azure AI integration points
- Enterprise and Teams focus

**Specific searches:**
- "[Tool name] Microsoft Copilot"
- "[Tool name] Power Automate"
- "[Tool name] Teams integration"
- "[Tool name] Azure AI"

**Common integration types:**
- Microsoft 365 Copilot plugins
- Power Automate connectors
- Teams app integrations
- Azure AI connections

**Red flags:**
- "Microsoft integration" may be Office/Teams, not Copilot
- Older Microsoft AI references may predate Copilot

## Verification Checklist

Before documenting a connection:

- [ ] Confirmed information is current (2024-2025)
- [ ] Verified connection type is accurate (not overstating)
- [ ] Checked if officially maintained or community-built
- [ ] Noted any plan/tier requirements
- [ ] Confirmed it works with the specific LLM platform mentioned
- [ ] Distinguished between "announced" and "available"

## Common Pitfalls and How to Avoid Them

### Pitfall 1: Confusing API with Integration

**Problem:** "Tool has an API" ≠ "Tool has LLM integration"

**Solution:** 
- API Available = potential for connection
- Official/Community Integration = actual working connection
- Be explicit: "API Available - No pre-built LLM integrations found"

### Pitfall 2: Generic "AI Integration" Claims

**Problem:** Tool says "AI-powered" but doesn't specify which LLM platforms

**Solution:**
- Don't assume generic "AI" means specific LLM integration
- Look for explicit platform names (ChatGPT, Claude, Gemini, Copilot)
- May be proprietary AI, not external LLM

### Pitfall 3: Outdated Announcements

**Problem:** Old blog post announces integration but current status unclear

**Solution:**
- Always verify current availability
- Check official docs for confirmation
- Look for recent user reports or reviews
- Note: "Announced in 2023, current status unclear as of Nov 2025"

### Pitfall 4: Official vs. Community Confusion

**Problem:** Unclear whether integration is officially supported

**Solution:**
- Check GitHub organization (company org = official, personal account = community)
- Look for official documentation references
- Check who announced it (company blog = official, personal blog = community)

### Pitfall 5: Planned vs. Available

**Problem:** Roadmap shows planned integration, documented as if available

**Solution:**
- "Coming soon" ≠ "Available"
- "In beta" ≠ "Generally available"
- Be explicit about status: "Announced for Q1 2026, not yet available"

## Documentation Examples

### Example 1: Strong Integration Across Platforms

```markdown
**LLM Connection:**
- **OpenAI ChatGPT:** Official Integration - Native connection in Enterprise plan, GPT Store app available (launched Oct 2024)
- **Anthropic Claude:** Official MCP Server - Maintained by tool team at github.com/company/mcp-server, full CRUD operations supported
- **Google Gemini:** Community Integration - Available via Zapier connector with 15+ pre-built workflows
- **Microsoft Copilot:** API Available - Public REST API documented, no pre-built Copilot integration found
```

### Example 2: Limited/Mixed Integration

```markdown
**LLM Connection:**
- **OpenAI ChatGPT:** Community Integration - Zapier app available with basic read/write operations
- **Anthropic Claude:** None - No documented integration method as of Nov 2025
- **Google Gemini:** None - No documented integration method as of Nov 2025
- **Microsoft Copilot:** API Available - RESTful API at api.toolname.com, potential for custom integration
```

### Example 3: No Integration Available

```markdown
**LLM Connection:**
- **OpenAI ChatGPT:** None - No public API or integration options available
- **Anthropic Claude:** None - Closed system with no external connections
- **Google Gemini:** None - No documented integration capability
- **Microsoft Copilot:** None - No public integration method available

**Note:** Tool operates as a closed system with no external API or integration support as of Nov 2025.
```

### Example 4: New/Beta Tool

```markdown
**LLM Connection:**
- **OpenAI ChatGPT:** In Development - ChatGPT integration announced in company blog (Oct 2024) for Q1 2026 release
- **Anthropic Claude:** None - No announced plans as of Nov 2025
- **Google Gemini:** None - No announced plans as of Nov 2025
- **Microsoft Copilot:** None - No announced plans as of Nov 2025

**Note:** Tool is in early beta with limited integration roadmap. ChatGPT integration confirmed but not yet available.
```

## Time Management

**Per LLM platform:** 2-3 minutes of focused research
**Total per tool (4 platforms):** 8-12 minutes
**Percentage of total research:** 40-50%

**Time allocation by phase:**
- Phase 1 (Official Features): 3-4 min
- Phase 2 (Developer Resources): 2-3 min
- Phase 3 (Recent Announcements): 2-3 min
- Phase 4 (Community Solutions): 2-3 min

**Efficiency tips:**
- Use multiple tabs for parallel searching
- Start with most likely platforms (ChatGPT usually first)
- Build search query templates you can reuse
- Keep notes on common patterns by tool category

## Quality Standards

### Excellent Research

✓ All 4 platforms investigated thoroughly
✓ Connection types accurately categorized
✓ Current status verified (not just announced)
✓ Dates included for time-sensitive info
✓ Official vs. community clearly distinguished
✓ Limitations or requirements noted

### Needs Improvement

✗ Only 1-2 platforms researched
✗ Generic "Has API" without specifics
✗ Old announcements treated as current
✗ No verification of actual availability
✗ Unclear if official or community
✗ Missing important caveats

## Final Tips

1. **Front-load this section:** Read this entire guide before starting any tool research. Understanding the methodology upfront saves time.

2. **Build pattern recognition:** After 5-10 tools, you'll recognize common integration patterns by tool category (e.g., project management tools often have strong ChatGPT integration).

3. **Use multiple search approaches:** Don't rely on one search method. Combine official docs, GitHub, news, and community platforms.

4. **Document uncertainty clearly:** It's better to say "No integration found" than to overstate capabilities.

5. **Keep dates prominent:** LLM integration landscape changes rapidly. Always date your findings.

6. **This is your differentiator:** Most tool research skips LLM integrations. Your thoroughness here provides unique value for AI consulting recommendations.
