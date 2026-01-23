#!/usr/bin/env python3
"""
Software Research Brief Generator

This script helps you create a customized research plan for evaluating software tools.
It gathers your decision context and generates a tailored research brief that combines
the research template with your specific requirements.

Usage:
    python init_research.py
    
The script will guide you through entering:
- Decision description
- Budget parameters
- Critical requirements
- Tools to evaluate
- Timeline and stakeholders

Output: A customized research brief document ready to use.
"""

import json
import sys
from datetime import datetime
from pathlib import Path


def print_header(text):
    """Print a formatted header."""
    print("\n" + "="*70)
    print(f"  {text}")
    print("="*70 + "\n")


def print_section(text):
    """Print a formatted section header."""
    print(f"\n--- {text} ---\n")


def get_input(prompt, required=True, multiline=False):
    """Get input from user with validation."""
    while True:
        if multiline:
            print(f"{prompt}")
            print("(Enter a blank line when done)")
            lines = []
            while True:
                line = input()
                if line == "":
                    break
                lines.append(line)
            value = "\n".join(lines)
        else:
            value = input(f"{prompt}: ").strip()
        
        if value or not required:
            return value
        print("This field is required. Please provide a value.\n")


def get_yes_no(prompt):
    """Get yes/no input from user."""
    while True:
        response = input(f"{prompt} (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        print("Please enter 'y' or 'n'\n")


def get_list_input(prompt, min_items=1):
    """Get a list of items from user."""
    print(f"\n{prompt}")
    print(f"(Enter one per line, blank line to finish, minimum {min_items} required)")
    items = []
    while True:
        item = input(f"  {len(items) + 1}. ").strip()
        if item == "":
            if len(items) >= min_items:
                break
            else:
                print(f"Please enter at least {min_items} item(s)")
                continue
        items.append(item)
    return items


def main():
    """Main script execution."""
    print_header("Software Research Brief Generator")
    print("This script will help you create a customized research plan for")
    print("evaluating software tools. It takes about 5-10 minutes to complete.")
    print("\nYou'll provide:")
    print("  • Decision context and budget")
    print("  • Critical requirements and nice-to-haves")
    print("  • Tools to evaluate")
    print("  • Timeline and stakeholders")
    
    input("\nPress Enter to begin...")
    
    # Initialize data structure
    brief = {
        "generated_date": datetime.now().strftime("%Y-%m-%d"),
        "decision_context": {},
        "requirements": {},
        "tools": [],
        "budget": {},
        "timeline": {},
        "stakeholders": {}
    }
    
    # Section 1: Decision Context
    print_section("1. Decision Context")
    brief["decision_context"]["description"] = get_input(
        "What decision are you making?\n"
        "(e.g., 'Replace Salesforce with more affordable CRM for 50-person sales team')\n"
        "Decision"
    )
    
    brief["decision_context"]["company_size"] = get_input(
        "How many employees in your company?",
        required=False
    )
    
    brief["decision_context"]["users"] = get_input(
        "How many people will use this tool?",
        required=False
    )
    
    brief["decision_context"]["current_tool"] = get_input(
        "What tool (if any) are you replacing?",
        required=False
    )
    
    # Section 2: Budget
    print_section("2. Budget Parameters")
    brief["budget"]["annual_software"] = get_input(
        "Annual software budget (e.g., $50000 or $50K)",
        required=False
    )
    
    brief["budget"]["implementation"] = get_input(
        "Implementation/setup budget (e.g., $10000)",
        required=False
    )
    
    brief["budget"]["training"] = get_input(
        "Training budget (if separate)",
        required=False
    )
    
    brief["budget"]["total_3year_target"] = get_input(
        "Total 3-year budget target (if known)",
        required=False
    )
    
    # Section 3: Critical Requirements
    print_section("3. Critical Requirements")
    print("List your MUST-HAVE requirements (deal-breakers).")
    print("These are features or capabilities you absolutely need.")
    brief["requirements"]["must_haves"] = get_list_input(
        "Enter must-have requirements:",
        min_items=1
    )
    
    print("\nList your NICE-TO-HAVE requirements (not deal-breakers).")
    if get_yes_no("Do you have nice-to-have requirements?"):
        brief["requirements"]["nice_to_haves"] = get_list_input(
            "Enter nice-to-have requirements:",
            min_items=0
        )
    else:
        brief["requirements"]["nice_to_haves"] = []
    
    # Section 4: Tools to Evaluate
    print_section("4. Tools to Evaluate")
    print("List the software tools you're considering (2-5 recommended).")
    brief["tools"] = []
    tools = get_list_input("Enter tool names:", min_items=2)
    
    for i, tool in enumerate(tools):
        tool_info = {"name": tool}
        print(f"\nFor {tool}:")
        reason = get_input(
            f"  Why is {tool} a finalist? (brief reason)",
            required=False
        )
        if reason:
            tool_info["reason"] = reason
        brief["tools"].append(tool_info)
    
    # Section 5: Timeline
    print_section("5. Timeline")
    brief["timeline"]["decision_by"] = get_input(
        "When must the decision be made? (e.g., Dec 31, 2025)"
    )
    
    brief["timeline"]["implementation_target"] = get_input(
        "When do you want to implement? (e.g., Q1 2026)",
        required=False
    )
    
    # Section 6: Stakeholders
    print_section("6. Key Stakeholders")
    print("Identify key people involved in this decision.")
    
    brief["stakeholders"]["decision_maker"] = get_input(
        "Who makes the final decision? (name and role)"
    )
    
    brief["stakeholders"]["economic_buyer"] = get_input(
        "Who controls the budget? (name and role)",
        required=False
    )
    
    brief["stakeholders"]["primary_users"] = get_input(
        "Who will use this tool? (team/department)",
        required=False
    )
    
    # Section 7: Special Focus Areas
    print_section("7. Special Focus Areas (Optional)")
    if get_yes_no("Are there specific areas you want to focus research on?"):
        print("\nExamples: integrations, security/compliance, ease of use, mobile apps")
        brief["focus_areas"] = get_list_input(
            "Enter focus areas:",
            min_items=0
        )
    else:
        brief["focus_areas"] = []
    
    # Generate the brief
    print_section("Generating Your Research Brief")
    print("Creating customized research document...")
    
    # Create output filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"research_brief_{timestamp}.md"
    
    # Generate brief content
    content = generate_brief_content(brief)
    
    # Write to file
    output_path = Path(filename)
    output_path.write_text(content)
    
    # Success message
    print_header("Research Brief Generated!")
    print(f"Your customized research brief has been saved to:")
    print(f"  {output_path.absolute()}")
    print(f"\nThis brief includes:")
    print(f"  • Your decision context and requirements")
    print(f"  • {len(brief['tools'])} tools to research")
    print(f"  • Complete 11-section research template")
    print(f"  • Customized priorities based on your focus areas")
    print(f"\nNext steps:")
    print(f"  1. Review the brief and adjust as needed")
    print(f"  2. Begin systematic research using the template")
    print(f"  3. Complete all required sections for each tool")
    print(f"  4. Compare and score when research is complete")
    print(f"\nExpected time: {len(brief['tools']) * 3} - {len(brief['tools']) * 4} hours total")


def generate_brief_content(brief):
    """Generate the actual brief content."""
    content = []
    
    # Header
    content.append("# Software Research Brief")
    content.append(f"\n**Generated:** {brief['generated_date']}")
    content.append(f"**Decision Deadline:** {brief['timeline']['decision_by']}")
    content.append("\n---\n")
    
    # Executive Summary
    content.append("## Executive Summary\n")
    content.append(f"**Decision:** {brief['decision_context']['description']}\n")
    content.append(f"**Tools Evaluating:** {', '.join([t['name'] for t in brief['tools']])}\n")
    
    if brief['budget']['annual_software']:
        content.append(f"**Budget:** {brief['budget']['annual_software']} annual")
    if brief['budget']['total_3year_target']:
        content.append(f" ({brief['budget']['total_3year_target']} 3-year target)")
    content.append("\n")
    
    content.append(f"**Must-Have Requirements:** {len(brief['requirements']['must_haves'])}")
    content.append(f"**Timeline:** Decision by {brief['timeline']['decision_by']}")
    if brief['timeline']['implementation_target']:
        content.append(f", implement by {brief['timeline']['implementation_target']}")
    content.append("\n\n")
    
    # Decision Context
    content.append("## Decision Context\n")
    content.append(f"### What We're Deciding\n")
    content.append(f"{brief['decision_context']['description']}\n")
    
    if brief['decision_context']['company_size'] or brief['decision_context']['users']:
        content.append(f"\n### Organization Context\n")
        if brief['decision_context']['company_size']:
            content.append(f"- Company size: {brief['decision_context']['company_size']} employees\n")
        if brief['decision_context']['users']:
            content.append(f"- Expected users: {brief['decision_context']['users']}\n")
        if brief['decision_context']['current_tool']:
            content.append(f"- Current tool: {brief['decision_context']['current_tool']}\n")
    
    # Budget
    content.append("\n## Budget Parameters\n")
    if brief['budget']['annual_software']:
        content.append(f"- Annual software budget: {brief['budget']['annual_software']}\n")
    if brief['budget']['implementation']:
        content.append(f"- Implementation budget: {brief['budget']['implementation']}\n")
    if brief['budget']['training']:
        content.append(f"- Training budget: {brief['budget']['training']}\n")
    if brief['budget']['total_3year_target']:
        content.append(f"- **Total 3-year target: {brief['budget']['total_3year_target']}**\n")
    
    # Requirements
    content.append("\n## Critical Requirements (Must-Haves)\n")
    content.append("These are deal-breakers. Tools must meet ALL of these:\n\n")
    for i, req in enumerate(brief['requirements']['must_haves'], 1):
        content.append(f"{i}. {req}\n")
    
    if brief['requirements']['nice_to_haves']:
        content.append("\n## Nice-to-Have Requirements\n")
        content.append("These would be valuable but are not deal-breakers:\n\n")
        for i, req in enumerate(brief['requirements']['nice_to_haves'], 1):
            content.append(f"{i}. {req}\n")
    
    # Tools
    content.append("\n## Tools to Research\n")
    for i, tool in enumerate(brief['tools'], 1):
        content.append(f"\n### {i}. {tool['name']}\n")
        if 'reason' in tool and tool['reason']:
            content.append(f"**Why evaluating:** {tool['reason']}\n")
        content.append("**Status:** Not started\n")
    
    # Timeline
    content.append("\n## Timeline & Milestones\n")
    content.append(f"- **Decision deadline:** {brief['timeline']['decision_by']}\n")
    if brief['timeline']['implementation_target']:
        content.append(f"- **Implementation target:** {brief['timeline']['implementation_target']}\n")
    content.append("\n**Research timeline:**\n")
    content.append(f"- Complete research: [Add date]\n")
    content.append(f"- Compare and score: [Add date]\n")
    content.append(f"- Final recommendation: [Add date]\n")
    content.append(f"- Decision: {brief['timeline']['decision_by']}\n")
    
    # Stakeholders
    content.append("\n## Key Stakeholders\n")
    content.append(f"- **Decision maker:** {brief['stakeholders']['decision_maker']}\n")
    if brief['stakeholders']['economic_buyer']:
        content.append(f"- **Budget authority:** {brief['stakeholders']['economic_buyer']}\n")
    if brief['stakeholders']['primary_users']:
        content.append(f"- **Primary users:** {brief['stakeholders']['primary_users']}\n")
    
    # Focus Areas
    if brief['focus_areas']:
        content.append("\n## Special Focus Areas\n")
        content.append("Pay extra attention to these areas during research:\n\n")
        for area in brief['focus_areas']:
            content.append(f"- {area}\n")
    
    # Research Instructions
    content.append("\n---\n\n## Research Instructions\n")
    content.append("### Overview\n")
    content.append("For each tool above, complete the full research template.\n\n")
    content.append("**Required sections (all tools):**\n")
    content.append("1. Company & Product Foundation\n")
    content.append("2. Feature Analysis\n")
    content.append("5. Pricing & TCO\n")
    content.append("9. Decision Matrix\n")
    content.append("10. Strategic Recommendation\n\n")
    
    content.append("**Recommended sections:**\n")
    content.append("3. Technical Architecture (if integrations critical)\n")
    content.append("4. User Experience (if adoption is a concern)\n")
    content.append("6. Security & Compliance (if enterprise/regulated)\n")
    content.append("7. Support & Services (always valuable)\n")
    content.append("8. Implementation Risks (for complex deployments)\n")
    content.append("11. Next Steps (always helpful)\n\n")
    
    content.append("### Time Estimate\n")
    num_tools = len(brief['tools'])
    content.append(f"- Per tool: 2-4 hours for comprehensive analysis\n")
    content.append(f"- Total for {num_tools} tools: {num_tools * 2}-{num_tools * 4} hours\n")
    content.append(f"- Comparison & synthesis: 2-3 hours\n")
    content.append(f"- **Total project: {num_tools * 2 + 2}-{num_tools * 4 + 3} hours**\n\n")
    
    content.append("### Getting Started\n")
    content.append("1. Load the research template: `view references/template.md`\n")
    content.append("2. Start with Tool 1 and complete all required sections\n")
    content.append("3. Move to Tool 2 and repeat\n")
    content.append("4. After all tools researched, create comparison matrices\n")
    content.append("5. Score each tool using weighted criteria\n")
    content.append("6. Deliver executive summary + detailed analysis\n\n")
    
    content.append("### Quality Standards\n")
    content.append("Reference `quality-guide.md` for:\n")
    content.append("- Good vs bad research examples\n")
    content.append("- Red flags to watch for\n")
    content.append("- Source quality requirements\n")
    content.append("- Common mistakes to avoid\n\n")
    
    # Template sections reference
    content.append("\n---\n\n## Research Template (Quick Reference)\n")
    content.append("Complete these 11 sections for each tool:\n\n")
    
    sections = [
        "1. Company & Product Foundation - Vendor stability, product maturity, market position",
        "2. Feature Analysis - Core features, AI capabilities, LLM integrations, gaps",
        "3. Technical Architecture - API quality, integrations, data portability",
        "4. User Experience - Interface quality, learning curve, real user feedback",
        "5. Pricing & TCO - All costs, 3-year model, ROI analysis",
        "6. Security & Compliance - Certifications, uptime, incident history",
        "7. Support & Services - Response times, implementation support, account management",
        "8. Implementation Risks - Technical, organizational, business risks",
        "9. Decision Matrix - Weighted scoring, deal-breaker check",
        "10. Strategic Recommendation - SWOT, fit analysis, go/no-go",
        "11. Next Steps - Action plan and timeline"
    ]
    
    for section in sections:
        content.append(f"{section}\n")
    
    content.append("\n**For complete guidance on each section, see `references/template.md`**\n")
    
    # Comparison Framework
    content.append("\n---\n\n## Comparison Framework\n")
    content.append("After researching all tools, create:\n\n")
    content.append("### 1. Feature Matrix\n")
    content.append("Side-by-side comparison of all must-have and nice-to-have features\n\n")
    
    content.append("### 2. Pricing Comparison\n")
    content.append("| Tool | Year 1 | Year 2 | Year 3 | 3-Year Total | Per User |\n")
    content.append("|------|--------|--------|--------|--------------|----------|\n")
    for tool in brief['tools']:
        content.append(f"| {tool['name']} | | | | | |\n")
    content.append("\n")
    
    content.append("### 3. Scoring Matrix\n")
    content.append("Weight criteria based on importance, score each tool 1-5:\n\n")
    
    criteria = [
        ("Core Features", "25%"),
        ("Ease of Use", "20%"),
        ("Integration Quality", "15%"),
        ("Total Cost", "15%"),
        ("Support Quality", "10%"),
        ("Security/Compliance", "10%"),
        ("Vendor Stability", "5%")
    ]
    
    content.append("| Criteria | Weight | " + " | ".join([t['name'] for t in brief['tools']]) + " |\n")
    content.append("|----------|--------|" + "|".join(["--------"] * len(brief['tools'])) + "|\n")
    for crit, weight in criteria:
        content.append(f"| {crit} | {weight} | " + " | ".join([""] * len(brief['tools'])) + " |\n")
    content.append("| **TOTAL** | **100%** | " + " | ".join([""] * len(brief['tools'])) + " |\n")
    content.append("\n")
    
    content.append("### 4. Trade-Off Analysis\n")
    content.append("Document key trade-offs between tools:\n")
    content.append("- Which tool wins on ease of use?\n")
    content.append("- Which has best value?\n")
    content.append("- Which has strongest enterprise features?\n")
    content.append("- Which has best support?\n\n")
    
    # Final Deliverable Structure
    content.append("\n---\n\n## Final Deliverable Structure\n")
    content.append("Your final analysis should include:\n\n")
    content.append("1. **Executive Summary** (2-3 paragraphs)\n")
    content.append("   - One paragraph per tool with key finding\n")
    content.append("   - Bottom-line recommendation\n")
    content.append("   - Critical decision factors\n\n")
    
    content.append("2. **Detailed Analysis** (15,000-25,000 words)\n")
    content.append("   - Complete research for each tool\n")
    content.append("   - All required sections thoroughly covered\n")
    content.append("   - Evidence and sources throughout\n\n")
    
    content.append("3. **Side-by-Side Comparison**\n")
    content.append("   - Feature matrices\n")
    content.append("   - Pricing comparison\n")
    content.append("   - Scoring results\n")
    content.append("   - Trade-off analysis\n\n")
    
    content.append("4. **Recommendation & Next Steps**\n")
    content.append("   - Clear winner with detailed rationale\n")
    content.append("   - Implementation approach\n")
    content.append("   - Risk mitigation plan\n")
    content.append("   - Action items with owners and dates\n\n")
    
    # Success Criteria
    content.append("\n---\n\n## Success Criteria\n")
    content.append("This research will be successful when:\n\n")
    content.append("✓ All critical requirements have clear answers\n")
    content.append("✓ Total cost is known with confidence\n")
    content.append("✓ Key risks are identified with mitigation strategies\n")
    content.append("✓ Can clearly articulate trade-offs between tools\n")
    content.append("✓ Recommendation is evidence-based and defensible\n")
    content.append("✓ Stakeholders have enough information to decide\n")
    content.append(f"✓ Decision can be made by {brief['timeline']['decision_by']}\n")
    
    return "".join(content)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nResearch brief generation cancelled.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nError: {e}")
        sys.exit(1)
