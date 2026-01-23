---
name: tool-research-architect
description: Conduct comprehensive software tool research for strategic analysis and client presentations. Use when (1) Researching software tools with focus on capabilities, pricing, and LLM integrations, (2) Creating tool comparison documents or competitive landscapes, (3) Building tool profiles for client recommendations, (4) Investigating how tools connect to OpenAI, Anthropic, Google, or Microsoft LLMs. Produces structured research following Jobs-to-be-Done framework with emphasis on AI integration opportunities.
---

# Tool Research Architect

## Overview

This skill guides comprehensive software tool research using a 6-section framework optimized for strategic analysis and client presentations. Special emphasis on LLM integration capabilities—a critical differentiator for AI consulting work.

## Research Framework

For each tool, research these 6 sections:

1. **Tool Name** - Official name, rebrands, acquisitions
2. **Description** - 1-3 sentences, plain English, business-person friendly
3. **Primary Use Case** - The #1 job-to-be-done
4. **Secondary Use Cases** - 3-5 additional valuable use cases
5. **Pricing Model & Starting Price** - Structure, tiers, dates, minimums
6. **LLM Connection** - Integration quality with OpenAI, Anthropic, Google, Microsoft

## Core Workflow

### Preparation Phase

Before starting research:

1. Review the tool list for duplicates or related tools
2. Identify tools you're familiar with vs. completely new ones
3. Plan your research strategy (batch vs. sequential)
4. Read references/llm-integration-guide.md for the most challenging section

### Research Phase

For each tool, follow this sequence:

#### Step 1: Establish Identity (2-3 minutes)

- Find official website and documentation
- Note any recent rebrands or acquisitions
- Verify the current official name
- If tools are related (mergers/rebrands): See references/special-situations.md

#### Step 2: Core Understanding (3-4 minutes)

- Write description in plain English (see references/description-guidelines.md)
  - Use the "3 L's": Lucid, Lean, Layman
  - Include analogies where helpful
  - Avoid technical jargon and buzzwords
- Identify primary use case (the ONE main problem it solves)
- List 3-5 secondary use cases (additional valuable features)

#### Step 3: Pricing Research (3-4 minutes)

- Check official pricing pages with dates
- Document pricing structure and starting prices
- Note free tiers, minimums, enterprise options
- Always include dates: "as of November 2025"
- See references/pricing-research-guide.md for detailed methodology

**Critical:** Pricing changes frequently. Always verify on official sources and include verification dates.

#### Step 4: LLM Integration Research (8-12 minutes) ⭐ CRITICAL

This is often the most valuable and challenging section. For EACH major LLM platform, identify the TYPE and QUALITY of integration:

**Platforms to research:**
- OpenAI's ChatGPT
- Anthropic's Claude
- Google's Gemini
- Microsoft's Copilot

**Connection types (strongest → weakest):**
1. **Official Integration** - Built by tool company or LLM provider
2. **Official MCP Server** - Model Context Protocol server (official)
3. **Community MCP Server** - MCP server by third parties
4. **API Available** - Public API that CAN connect to LLMs
5. **Community Integration** - Via Zapier, Make, Pipedream, etc.
6. **None** - No documented connection

**Research methodology:**
- Start with official tool website and feature pages
- Check developer portals and API documentation
- Search GitHub for "[Tool] MCP server"
- Look for recent announcements (2024-2025)
- See references/llm-integration-guide.md for comprehensive search patterns

**Time allocation:** This section deserves 40-50% of your research time—it's where you provide the most unique value.

#### Step 5: Documentation (2-3 minutes)

- Use the template from assets/output-template.md
- Maintain consistent formatting
- Include dates for all pricing and time-sensitive information
- Follow markdown standards (proper headers, bullets, bold labels)

### Quality Check Phase

Before finalizing, verify:

**Completeness:**
- [ ] All 6 sections completed for each tool
- [ ] No placeholder text or TODO items
- [ ] All reference guides consulted when needed

**Accuracy:**
- [ ] Pricing includes dates (2024-2025)
- [ ] Tool names are current official names
- [ ] LLM connections accurately categorized
- [ ] Sources verified (official > third-party)

**Clarity:**
- [ ] Descriptions are jargon-free and clear
- [ ] Use cases reflect actual product capabilities
- [ ] No technical assumptions about reader knowledge

**Format:**
- [ ] Consistent markdown structure
- [ ] Proper bold labels and bullets
- [ ] Clean, scannable layout

## Research Best Practices

### Information Sources (Priority Order)

1. **Official company website and documentation** - Most reliable
2. **Developer portals and API documentation** - Technical accuracy
3. **Recent press releases and announcements** - Current changes
4. **Third-party sources** - Only if needed, always verify

### Search Strategies

**Start broad, then narrow:**
- "[Tool name]" → "[Tool name] pricing" → "[Tool name] API documentation"

**Platform-specific searches:**
- "[Tool name] ChatGPT integration"
- "[Tool name] Claude integration"
- "[Tool name] MCP server" site:github.com

**Date-sensitive searches:**
- "[Tool name] AI" 2024..2025
- "[Tool name] integration" 2024..2025

### Date Sensitivity

Always note when information was retrieved or last updated:
- "as of November 2025"
- "updated Oct 2024"
- "starting at $X/month (2024 pricing)"

**Why this matters:** Pricing changes frequently, integrations launch regularly, tools rebrand—dated information ensures accuracy.

### Handling Ambiguity

If information is unclear or contradictory:
- State what could not be verified
- Note if tool is new/small with limited public documentation
- Provide best available estimates with caveats
- Document discrepancies: "Official site shows $25/user, but some third-party sources show $20 (may be outdated)"

### Cross-Referencing

- Verify pricing across multiple sources
- Check official sources before trusting third-party claims
- Look for recent news about changes
- Compare current info with historical data

## Output Format

Use the template in assets/output-template.md for consistent structure.

### Standard Tool Profile Structure

Each tool should have:
- Clear markdown headers (`## 1. Tool Name`)
- Bold labels for sections (`**Description:**`, `**Pricing Model:**`)
- Bullet points for lists (use cases, pricing tiers, LLM connections)
- Consistent formatting throughout
- Date stamps on time-sensitive information

### Optional Summary Analysis

For multi-tool research (5+ tools), consider adding:
- **LLM Integration Landscape** - Which tools have strong vs. weak integrations
- **Pricing Patterns** - Trends across similar tools
- **Market Gaps** - What's missing in the ecosystem
- **Recommendations** - Strategic insights for specific use cases

## Time Estimates

**Per Tool:**
- Simple tool (well-documented): 10-12 minutes
- Complex tool (enterprise, multiple products): 15-20 minutes
- Challenging (limited info, heavy LLM research): 20-25 minutes

**Breakdown by section:**
- Identity: 2-3 min (10-15%)
- Understanding: 3-4 min (15-20%)
- Pricing: 3-4 min (15-20%)
- LLM Integration: 8-12 min (40-50%) ⭐
- Documentation: 2-3 min (10-15%)

**For 30 tools:** Plan 5-7 hours of focused research

## Reference Guides - When to Use

Load these detailed guides as needed:

### references/llm-integration-guide.md
**Load when:**
- Starting LLM integration research (always read this)
- Unsure how to categorize a connection type
- Need search patterns for specific LLM platforms
- Struggling to find integration information

**Contains:**
- Detailed connection type definitions
- Platform-specific research methodology
- Search patterns and verification checklists
- Common pitfalls and how to avoid them

### references/pricing-research-guide.md
**Load when:**
- Encountering complex pricing models
- Finding contradictory pricing information
- Unsure how to document usage-based or custom pricing
- Need guidance on source reliability

**Contains:**
- Source hierarchy and verification methods
- Common pricing model patterns
- Date sensitivity requirements
- Examples of well-documented pricing

### references/description-guidelines.md
**Load when:**
- Struggling to write jargon-free descriptions
- Tool is very technical and needs simplification
- Want examples of effective analogies
- Need to translate technical terms

**Contains:**
- The "3 L's" rule (Lucid, Lean, Layman)
- Template patterns for descriptions
- Jargon translation table
- Before/after examples

### references/special-situations.md
**Load when:**
- Information is very limited (new/beta tools)
- Tools are related (mergers, acquisitions, rebrands)
- Company has multiple products (unclear which to focus on)
- Finding contradictory information across sources

**Contains:**
- Handling limited information scenarios
- Clarifying tool relationships
- Documenting edge cases
- Resolution strategies for conflicts

## Research Tips

### Efficiency Strategies

**Front-load LLM research:**
Read references/llm-integration-guide.md before starting ANY research. This section takes the most time and benefits most from systematic methodology.

**Batch similar tasks:**
If researching multiple tools, do all identity checks first, then all descriptions, then all pricing—this builds pattern recognition.

**Use multiple tabs:**
Open official site, pricing page, and developer docs simultaneously. Switch between them rather than sequential searching.

**GitHub for MCP Servers:**
Search: "[Tool name] MCP server" to find community-built integrations quickly.

**Developer portals:**
Often have the most accurate API and integration information.

### Quality Indicators

**Good sources:**
- Official .com domains
- Developer documentation sites
- Recent press releases (2024-2025)
- GitHub official organization repos

**Questionable sources:**
- Third-party review sites with no update dates
- Forum discussions (unless very recent)
- Cached/archived pages
- Marketing copy without technical details

### Pattern Recognition

After researching 5-10 tools, you'll notice:
- Common pricing models by category
- Typical LLM integration patterns
- Standard documentation structures
- Industry-specific features

Use these patterns to speed up subsequent research while remaining thorough.

## Common Pitfalls to Avoid

### In LLM Integration Research

❌ Assuming "Has API" = "Has LLM integration" (API is just potential)
❌ Assuming "Works with AI" = "Works with specific LLM" (may be proprietary AI)
❌ Trusting old announcements without current verification
❌ Not distinguishing between official and community integrations

✓ Verify integration is actually available (not just planned)
✓ Confirm which specific LLM platforms are supported
✓ Check whether it's officially maintained or community-built
✓ Verify current status (many announced but not released)

### In Pricing Research

❌ Using third-party pricing without verification
❌ Omitting dates on pricing information
❌ Ignoring seat minimums or contract requirements
❌ Confusing free trials with free tiers

✓ Always check official pricing pages
✓ Include verification dates on all pricing
✓ Note any minimums, commitments, or setup fees
✓ Distinguish between trials and permanent free plans

### In Descriptions

❌ Copying marketing jargon verbatim
❌ Using technical terms without explanation
❌ Writing overly long descriptions
❌ Focusing on features instead of outcomes

✓ Translate to plain English
✓ Use analogies where helpful
✓ Keep to 1-3 sentences
✓ Focus on the job-to-be-done

## Skill Success Metrics

This skill is working effectively when:

1. **Consistency:** Multiple researchers produce uniform quality reports
2. **Speed:** Research time per tool drops by 25-33%
3. **Completeness:** Zero reports missing any of the 6 required sections
4. **LLM Integration Quality:** All reports accurately categorize integration types
5. **Client Value:** Reports directly support recommendations without additional research

## Final Notes

This skill framework emphasizes **systematic thoroughness over speed**. While efficiency matters, the real value comes from:

- Comprehensive LLM integration research (most differentiating)
- Accurate, current pricing information (most actionable)
- Clear, accessible descriptions (most shareable)
- Consistent formatting (most professional)

Quality research takes time, but the systematic approach in this skill ensures that time is well-spent and produces reusable, reliable outputs.
