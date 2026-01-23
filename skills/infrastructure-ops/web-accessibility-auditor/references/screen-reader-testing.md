# Screen Reader Testing

Guides for testing with NVDA, JAWS, and VoiceOver.

## Screen Reader Overview

| Reader | Platform | Cost | Usage Share |
|--------|----------|------|-------------|
| NVDA | Windows | Free | ~40% |
| JAWS | Windows | $$$ | ~35% |
| VoiceOver | macOS/iOS | Built-in | ~15% |
| TalkBack | Android | Built-in | ~5% |
| Narrator | Windows | Built-in | ~5% |

---

## NVDA (Windows)

### Setup

1. Download from nvaccess.org (free)
2. Install and launch
3. Recommend: Enable Speech Viewer (Tools > Speech Viewer)

### Key Commands

| Action | Keys |
|--------|------|
| Start/stop | Ctrl+Alt+N |
| Stop speech | Ctrl |
| Read all | NVDA+Down Arrow |
| Next item | Down Arrow |
| Previous item | Up Arrow |
| Next heading | H |
| Next link | K |
| Next button | B |
| Next form field | F |
| Next landmark | D |
| List headings | NVDA+F7 |
| List links | NVDA+F7, then Tab |
| Browse/focus mode | NVDA+Space |

### Browse Mode vs Focus Mode

**Browse mode:** Reading content, using quick navigation keys
**Focus mode:** Interacting with forms, typing

NVDA switches automatically, or toggle with NVDA+Space.

### Testing Checklist

- [ ] Page title announced on load
- [ ] Headings structure is logical
- [ ] Images have meaningful alt text
- [ ] Links describe destination
- [ ] Form labels announced with fields
- [ ] Error messages associated with fields
- [ ] Dynamic content changes announced

---

## JAWS (Windows)

### Key Commands

| Action | Keys |
|--------|------|
| Start/stop | Insert+Esc |
| Stop speech | Ctrl |
| Read all | Insert+Down Arrow |
| Next heading | H |
| Next link | Tab (in virtual) |
| Next form field | F |
| Heading list | Insert+F6 |
| Link list | Insert+F7 |
| Form field list | Insert+F5 |
| Virtual cursor on/off | Insert+Z |

### Virtual Cursor

JAWS uses a "virtual cursor" to navigate the page like a document.

**Virtual cursor on:** Reading content
**Virtual cursor off:** Interacting with applications

---

## VoiceOver (macOS)

### Enable/Disable

- Cmd+F5: Toggle VoiceOver
- System Preferences > Accessibility > VoiceOver

### Key Commands

VO = Control+Option (VoiceOver modifier)

| Action | Keys |
|--------|------|
| Next item | VO+Right Arrow |
| Previous item | VO+Left Arrow |
| Interact with element | VO+Shift+Down Arrow |
| Stop interaction | VO+Shift+Up Arrow |
| Read all | VO+A |
| Stop speech | Ctrl |
| Rotor | VO+U |
| Next heading | VO+Cmd+H |
| Next link | VO+Cmd+L |
| Next form field | VO+Cmd+J |

### The Rotor

VoiceOver's navigation menu. Access with VO+U.

- Use Left/Right to change category (headings, links, etc.)
- Use Up/Down to navigate items
- Press Enter to go to item

### VoiceOver for iOS

| Action | Gesture |
|--------|---------|
| Next item | Swipe right |
| Previous item | Swipe left |
| Activate | Double tap |
| Rotor | Two-finger rotate |
| Read all | Two-finger swipe down |

---

## Testing Workflow

### 1. First Impression

- Open page with screen reader
- Note: What's announced first?
- Check: Is page title clear and unique?

### 2. Structure Navigation

- Navigate by headings (H key)
- Check: Logical heading hierarchy?
- Check: All major sections have headings?

### 3. Link Review

- Navigate by links
- Check: Links make sense out of context?
- Avoid: "Click here", "Read more"

### 4. Form Testing

- Navigate by form fields
- Check: Labels announced with each field?
- Check: Required fields indicated?
- Check: Errors clearly associated?

### 5. Interactive Elements

- Test buttons, menus, tabs
- Check: State changes announced?
- Check: Keyboard fully functional?

### 6. Dynamic Content

- Trigger dynamic updates
- Check: Changes announced appropriately?
- Check: Focus managed correctly?

---

## Common Issues and Fixes

### Issue: No heading structure

```html
<!-- Before -->
<div class="title">Page Title</div>
<div class="subtitle">Section</div>

<!-- After -->
<h1>Page Title</h1>
<h2>Section</h2>
```

### Issue: Ambiguous links

```html
<!-- Before -->
<a href="/article">Read more</a>

<!-- After -->
<a href="/article">Read more about accessibility testing</a>

<!-- Or with hidden text -->
<a href="/article">
  Read more <span class="sr-only">about accessibility testing</span>
</a>
```

### Issue: Form labels not associated

```html
<!-- Before -->
<span>Email</span>
<input type="email">

<!-- After -->
<label for="email">Email</label>
<input type="email" id="email">
```

### Issue: Dynamic changes not announced

```html
<!-- Add live region -->
<div role="status" aria-live="polite" id="status"></div>

<script>
// Update live region
document.getElementById('status').textContent = 'Form saved';
</script>
```

---

## Screen Reader CSS

### Visually Hidden (but screen reader accessible)

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border: 0;
}

/* Allow element to be focused (for skip links) */
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
  white-space: normal;
}
```

### Hidden from Screen Readers

```html
<!-- Hidden from all (including SR) -->
<div hidden>Not accessible</div>
<div style="display: none">Not accessible</div>

<!-- Hidden from SR only -->
<img src="decorative.png" alt="" role="presentation">
<div aria-hidden="true">Decorative content</div>
```

---

## Recording Test Results

```markdown
## Screen Reader Test: [Page Name]

**Date:** YYYY-MM-DD
**Tester:** [Name]
**Screen Reader:** NVDA 2024.1 / Chrome 121

### Findings

| Issue | Location | WCAG | Severity | Status |
|-------|----------|------|----------|--------|
| Missing alt text | Hero image | 1.1.1 | High | Open |
| Unlabeled form field | Search box | 1.3.1 | High | Open |
| Low contrast text | Footer | 1.4.3 | Medium | Open |
| Focus not visible | Nav links | 2.4.7 | High | Fixed |

### Notes

- Heading structure is good (h1 > h2 > h3)
- Form errors announced correctly
- Modal traps focus properly
```
