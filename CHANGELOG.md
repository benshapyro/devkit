# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Added
- 23 marketing skills imported from coreyhaines31/marketingskills
  - CRO skills: page-cro, form-cro, popup-cro, signup-flow-cro, onboarding-cro, paywall-upgrade-cro
  - SEO skills: seo-audit, programmatic-seo, schema-markup
  - Growth skills: launch-strategy, referral-program, free-tool-strategy
  - Copy skills: copywriting, copy-editing
  - Strategy skills: marketing-psychology, pricing-strategy, competitor-alternatives, marketing-ideas
  - Other: email-sequence, paid-ads, ab-test-setup, analytics-tracking, social-content
- Rating column (⭐ favorite, 👍 like, ❓ not reviewed) added to all Quick Reference tables in skills README
- 31 skills from official Claude Code plugins (superpowers, plugin-dev, figma, vercel)
  - Development Tools: brainstorming, TDD, systematic-debugging, verification-before-completion, writing-plans, etc.
  - Design & UI: code-connect-components, create-design-system-rules, implement-design (Figma)
  - Infrastructure & Ops: deploy, logs, setup (Vercel)
  - Internal & Specialty: Claude Code plugin development skills (agents, commands, hooks, MCP, skills)
- 7 specialized n8n skills replacing monolithic n8n-architect
- 13 new skills: ai-maturity-assessor, clay-mastery, clickup-automation-architect, n8n-architect, onboarding, presentation-composer, prompt-engineering, and more
- Comprehensive skills catalog README with Quick Reference tables and detailed entries
- Packaging script with group support (`--group` flag)
- README.md with comprehensive documentation, architecture diagram, and examples for all artifact types
- CHANGELOG.md to track project changes
- README-SPEC.md capturing documentation requirements

### Changed
- Split content-marketing into marketing/ (27 skills) and communications/ (3 skills)
- Reorganized skills directory into 9 group subdirectories matching README categories
- Updated packaging script to handle grouped directory structure
- Skills count increased from initial ~30 to 120
- Updated CLAUDE.md with changelog maintenance instructions

### Removed
- n8n-architect skill (superseded by 7 specialized n8n skills, archived)

## [0.1.0] - 2025-01-08

### Added
- Initial devkit structure with four artifact types: skills, hooks, commands, agents
- Skills library with document processing (PDF, Word, PowerPoint, Excel), development tools, business frameworks, and content utilities
- 7 agents migrated from personal config: code-reviewer, debugger, documentation-researcher, git-helper, performance-optimizer, refactoring-assistant, spec-discovery
- 5 hooks migrated from personal config for security, formatting, and testing automation
- 10 commands: backlog, greenfield, learn, plan, progress, research, review, ship, slop, validate
- Skill creator tooling: init_skill.py, package_skill.py, quick_validate.py
- CUSTOMIZATION.md specification for hooks, commands, and agents
- CLAUDE.md files in each subdirectory for context-aware assistance

### Changed
- Commands updated with allowed-tools restrictions and improved error handling
- Reduced command verbosity for cleaner output

## Types of Changes

- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for bug fixes
- **Security** for vulnerability fixes
