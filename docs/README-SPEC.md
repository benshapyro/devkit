# README.md Specification

This document defines the requirements for the devkit README.md based on stakeholder interview conducted 2026-01-13.

## Strategic Decisions

### Audience
**Mixed**: Primarily internal/personal use, but structured well enough to go public later without major rewrites.

### Positioning
**Standalone tool**: No Cadre branding or ecosystem references. Self-contained, easy to share or repurpose.

### Primary Goal
**Both consume and create**: Quick start for consumers, clear path to creation for those who want to extend.

## Content Requirements

### Value Proposition
- **Explicit comparison**: Short section explaining library approach (version control, sharing, multi-tool) vs. built-in customization (simpler but siloed)
- Do NOT include alternatives comparison or "Why not X?" section

### Artifact Coverage
- **Equal treatment**: All four artifact types (skills, hooks, commands, agents) get same prominence
- Do NOT establish a hierarchy or lead with any single type

### Diagram
- **ASCII diagram with relationship arrows**: Show how pieces connect (commands invoke agents, hooks monitor events, skills provide knowledge)
- Version controllable, works everywhere, no external dependencies

### Examples
- **One synthetic minimal example per artifact type**: Purpose-built examples showing just the essential pattern
- No distracting real-world details
- Examples should be inline in README, not just links

### Inventory
- **Categories only**: Mention categories exist (document processing, development, etc.) without listing every artifact
- Avoids maintenance burden and staleness

### Prerequisites
- **Brief section**: List what's needed (Claude Code, Python 3.11+) without installation instructions
- Link out for details
- Silent failure model - reader's responsibility to have prerequisites installed

### Multi-tool Support
- **Brief forward-looking note**: One line acknowledging architecture supports multiple tools
- Do NOT create roadmap or commit to timeline

### Deployment Model
- **Source of truth framing**: This repo is canonical. Deployed copies are downstream. Edit here, redeploy to update.

### Hook Scripts
- **Brief mention**: Note that hooks/scripts/ contains reusable Python for common patterns
- Discoverable for those who look, not documented as API

## Structure Requirements

### Length
**Single-page scannable**: Everything fits in one scroll-through. Use links for deeper dives.

### Table of Contents
**Manual TOC**: Simple markdown links to sections. Works everywhere, signals structure upfront.

### Creation Documentation
**In README with examples**: Show the pattern inline. Reader sees both consumption and creation without leaving the page.

### Relationship to CUSTOMIZATION.md
**Deprecate**: README covers essential patterns (90% case). Deep specs either:
- Move to subdirectory CLAUDE.md files, or
- Get dropped entirely

CUSTOMIZATION.md should be archived after README is complete.

## Presentation Requirements

### Badges
**None**: No CI pipeline to show status for. Badges without meaning are vanity metrics.

### Tone
**Technical and direct**: No fluff, no marketing speak. Assumes reader is competent. Respects their time.

### License
**None**: Keep private/proprietary for now. Can add license later if going public.

### Attribution
**None**: Let git history speak. No maintenance when people join/leave.

## Explicit Exclusions

The README should NOT include:
- Troubleshooting section (use issues/discussions)
- Performance considerations (not relevant)
- Security guidance (handle in artifact-specific docs if needed)
- Explanation of CLAUDE.md files (they're for Claude, not humans)
- Changelog (separate CHANGELOG.md file)
- Full spec details (move to subdirectory docs or drop)

## Additional Deliverables

### CHANGELOG.md
Create new file with:
- **Keep a Changelog format**: [Unreleased], [version] - date, Added/Changed/Removed sections
- Plain English, clear, concise overview of each change

### CLAUDE.md Update
Update root CLAUDE.md to instruct Claude to:
- Update git with proper commit messages
- Update CHANGELOG.md with each significant change

## Outline

Based on requirements, the README structure should be:

```
# Devkit

[One-line description]

## Table of Contents

## Why a Library?
[Explicit comparison: library vs built-in]

## Prerequisites
[Brief list with links]

## Architecture
[ASCII diagram with relationship arrows]

## Skills
[What they are + synthetic minimal example]

### Available Categories
[List categories, not individual skills]

## Hooks
[What they are + synthetic minimal example]

### Hook Scripts
[Brief mention of hooks/scripts/]

## Commands
[What they are + synthetic minimal example]

## Agents
[What they are + synthetic minimal example]

## Creating New Artifacts
[Brief patterns for each type]

## Deployment
[Source of truth framing + how to deploy each type]

## Multi-tool Support
[Brief forward-looking note]

## Documentation
[Links to subdirectory CLAUDE.md files and external resources]
```

## Success Criteria

The README is complete when:
1. A new reader can deploy an existing artifact within 2 minutes
2. A new reader understands how to create a new artifact without reading other docs
3. The document fits in a single scroll (~300 lines max)
4. All four artifact types have equal visual weight
5. No maintenance burden from inventories or changelogs in the README itself
