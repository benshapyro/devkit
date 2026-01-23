# Sample Blocks Library

## Purpose

This directory will house example blocks from past client projects, organized for easy reference when creating new blocks.

## Future Organization Structure

```
sample-blocks/
├── by-cluster-combo/
│   ├── discovery-integration/
│   ├── discovery-development/
│   ├── discovery-process-design/
│   ├── integration-automation/
│   └── ai-llm-deployment/
├── by-industry/
│   ├── healthcare/
│   ├── financial-services/
│   ├── manufacturing/
│   └── saas/
└── by-duration/
    ├── 1-2-months/
    ├── 3-4-months/
    └── 6-plus-months/
```

## How It Will Work

When creating a new block, the skill will:
1. Identify which activity clusters apply
2. Search this library for similar combinations
3. Offer: "I found 3 similar blocks. Would you like me to use [Block X from Client Y] as a template?"
4. Adapt the template to the current client's needs

## Adding Blocks

As projects complete:
1. Save both internal and client versions
2. Anonymize client names (or keep if approved)
3. Add to appropriate category directories
4. Update index if tracking metadata

## Not Built Yet

This is a placeholder for future functionality. For now, the skill will guide block creation from scratch using the templates and references.

**Target for v2.0**: Progressive disclosure with historical blocks as reference material.
