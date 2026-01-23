# Web Accessibility Auditor

WCAG 2.2 compliance checking, ARIA pattern guidance, and accessibility testing workflows.

## When to Use

Activate when:
- Auditing web pages for accessibility
- Implementing ARIA patterns
- Testing keyboard navigation
- Setting up automated accessibility testing
- Fixing accessibility issues
- Training teams on accessibility

## Command Routing

| User Request | Action | Reference |
|--------------|--------|-----------|
| "WCAG" or "compliance check" | Run full audit | wcag-2.2-checklist.md |
| "ARIA" or "role" | Pattern guidance | aria-patterns.md |
| "keyboard" or "focus" | Navigation testing | keyboard-navigation.md |
| "screen reader" or "NVDA" | SR testing guide | screen-reader-testing.md |
| "axe" or "automated testing" | Tool integration | automated-testing.md |
| "common mistakes" or "pitfalls" | Anti-patterns | common-mistakes.md |

## Quick Reference

### WCAG Principles (POUR)

| Principle | Meaning |
|-----------|---------|
| **Perceivable** | Content available to senses |
| **Operable** | Interface can be used |
| **Understandable** | Content is comprehensible |
| **Robust** | Works with assistive tech |

### Conformance Levels

| Level | Requirement |
|-------|-------------|
| **A** | Minimum accessibility |
| **AA** | Standard target (legal requirement) |
| **AAA** | Enhanced accessibility |

### Quick Wins

1. **Alt text** - All images have descriptive alt
2. **Headings** - Proper hierarchy (h1 → h2 → h3)
3. **Color contrast** - 4.5:1 for text, 3:1 for large text
4. **Focus visible** - Keyboard focus is obvious
5. **Labels** - Form inputs have associated labels
6. **Skip link** - Skip to main content link

### ARIA First Rule

> "No ARIA is better than bad ARIA"

Use semantic HTML first. ARIA only when HTML can't express the pattern.

```html
<!-- Bad: div with ARIA -->
<div role="button" tabindex="0">Click</div>

<!-- Good: native button -->
<button>Click</button>
```

### Testing Checklist

- [ ] Automated scan (axe-core)
- [ ] Keyboard navigation test
- [ ] Screen reader verification
- [ ] Color contrast check
- [ ] Zoom to 200% test
- [ ] Form error handling

## Reference Files

| File | Content |
|------|---------|
| wcag-2.2-checklist.md | All success criteria |
| aria-patterns.md | Correct ARIA usage |
| keyboard-navigation.md | Focus management |
| screen-reader-testing.md | NVDA, JAWS, VoiceOver guides |
| automated-testing.md | axe-core, pa11y integration |
| common-mistakes.md | Anti-patterns to avoid |
