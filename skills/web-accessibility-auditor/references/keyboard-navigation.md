# Keyboard Navigation

Focus management and keyboard accessibility patterns.

## Fundamental Keys

| Key | Action |
|-----|--------|
| Tab | Move forward through focusable elements |
| Shift+Tab | Move backward |
| Enter | Activate links, buttons |
| Space | Activate buttons, toggle checkboxes |
| Escape | Close dialogs, cancel |
| Arrow keys | Navigate within components |

---

## Focus Management

### What Should Be Focusable

**Naturally focusable:**
- `<a href="...">` (links with href)
- `<button>`
- `<input>`, `<select>`, `<textarea>`
- `<area>` (in image maps)
- `<iframe>`

**Made focusable with tabindex:**
```html
<!-- Add to focus order -->
<div tabindex="0">Interactive widget</div>

<!-- Programmatically focusable only -->
<div tabindex="-1">Can receive focus via JS</div>
```

### tabindex Values

| Value | Behavior |
|-------|----------|
| `0` | In natural tab order |
| `-1` | Focusable by script only |
| `1+` | **Avoid** - disrupts natural order |

### Focus Order

Focus should follow visual/DOM order.

```html
<!-- Bad: tabindex disrupts order -->
<button tabindex="3">Third</button>
<button tabindex="1">First</button>
<button tabindex="2">Second</button>

<!-- Good: natural DOM order -->
<button>First</button>
<button>Second</button>
<button>Third</button>
```

---

## Focus Visibility

### Default Focus Styles

```css
/* Browser default - often removed, which is bad */
:focus {
  outline: none; /* ❌ Never do this without replacement */
}

/* Good: enhanced focus styles */
:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* Better: focus-visible for keyboard only */
:focus:not(:focus-visible) {
  outline: none;
}

:focus-visible {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}
```

### High Contrast Focus

```css
:focus-visible {
  outline: 3px solid currentColor;
  outline-offset: 3px;
  box-shadow: 0 0 0 6px #ffffff;
}
```

---

## Skip Links

Allow users to bypass repeated navigation.

```html
<body>
  <a href="#main-content" class="skip-link">
    Skip to main content
  </a>

  <nav><!-- lengthy navigation --></nav>

  <main id="main-content" tabindex="-1">
    <!-- main content -->
  </main>
</body>

<style>
.skip-link {
  position: absolute;
  left: -9999px;
  z-index: 999;
  padding: 1em;
  background: #000;
  color: #fff;
}

.skip-link:focus {
  left: 50%;
  transform: translateX(-50%);
}
</style>
```

---

## Focus Trapping

Keep focus inside modal dialogs.

```javascript
function trapFocus(element) {
  const focusable = element.querySelectorAll(
    'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
  );

  const first = focusable[0];
  const last = focusable[focusable.length - 1];

  element.addEventListener('keydown', (e) => {
    if (e.key !== 'Tab') return;

    if (e.shiftKey) {
      if (document.activeElement === first) {
        e.preventDefault();
        last.focus();
      }
    } else {
      if (document.activeElement === last) {
        e.preventDefault();
        first.focus();
      }
    }
  });
}
```

### Focus Return

Return focus when dialog closes.

```javascript
let previousFocus;

function openModal(modal) {
  previousFocus = document.activeElement;
  modal.setAttribute('aria-hidden', 'false');
  modal.querySelector('[autofocus]')?.focus();
  trapFocus(modal);
}

function closeModal(modal) {
  modal.setAttribute('aria-hidden', 'true');
  previousFocus?.focus();
}
```

---

## Roving tabindex

For composite widgets (menus, toolbars, radio groups).

```html
<ul role="menu">
  <li role="menuitem" tabindex="0">Item 1</li>
  <li role="menuitem" tabindex="-1">Item 2</li>
  <li role="menuitem" tabindex="-1">Item 3</li>
</ul>
```

```javascript
const items = menu.querySelectorAll('[role="menuitem"]');
let currentIndex = 0;

menu.addEventListener('keydown', (e) => {
  if (!['ArrowUp', 'ArrowDown', 'Home', 'End'].includes(e.key)) return;

  e.preventDefault();

  // Update current item's tabindex
  items[currentIndex].setAttribute('tabindex', '-1');

  // Calculate new index
  switch (e.key) {
    case 'ArrowDown':
      currentIndex = (currentIndex + 1) % items.length;
      break;
    case 'ArrowUp':
      currentIndex = (currentIndex - 1 + items.length) % items.length;
      break;
    case 'Home':
      currentIndex = 0;
      break;
    case 'End':
      currentIndex = items.length - 1;
      break;
  }

  // Focus new item
  items[currentIndex].setAttribute('tabindex', '0');
  items[currentIndex].focus();
});
```

---

## Component Keyboard Patterns

### Tab Component

```
Tab: Move between tabs
Arrow Left/Right: Previous/next tab
Home: First tab
End: Last tab
```

### Menu

```
Enter/Space: Open menu, select item
Arrow Up/Down: Navigate items
Arrow Left/Right: Parent/submenu
Escape: Close menu
```

### Tree View

```
Arrow Up/Down: Navigate items
Arrow Right: Expand node / move to first child
Arrow Left: Collapse node / move to parent
Enter/Space: Select/activate
Home/End: First/last visible node
```

### Grid/Table

```
Arrow keys: Move cell to cell
Page Up/Down: Scroll
Home: First cell in row
End: Last cell in row
Ctrl+Home: First cell in grid
Ctrl+End: Last cell in grid
```

---

## Testing Keyboard Access

### Manual Testing Checklist

- [ ] Tab through entire page
- [ ] All interactive elements reachable
- [ ] Focus visible at all times
- [ ] Focus order logical
- [ ] No keyboard traps
- [ ] Dialogs trap focus correctly
- [ ] Escape closes overlays
- [ ] Skip link works

### Common Issues

| Issue | Fix |
|-------|-----|
| Invisible focus | Add `:focus` styles |
| Click-only handlers | Add keyboard handlers |
| Non-focusable widgets | Add `tabindex="0"` |
| Broken focus order | Fix DOM order or CSS |
| Modal doesn't trap focus | Implement focus trap |
| Focus lost after action | Manage focus programmatically |

---

## Code Patterns

### Keyboard Event Handler

```javascript
element.addEventListener('keydown', (e) => {
  switch (e.key) {
    case 'Enter':
    case ' ':
      e.preventDefault();
      activate();
      break;
    case 'Escape':
      e.preventDefault();
      close();
      break;
    case 'ArrowDown':
      e.preventDefault();
      moveNext();
      break;
    case 'ArrowUp':
      e.preventDefault();
      movePrevious();
      break;
  }
});
```

### React Focus Management

```jsx
import { useRef, useEffect } from 'react';

function Modal({ isOpen, onClose, children }) {
  const modalRef = useRef();
  const previousFocus = useRef();

  useEffect(() => {
    if (isOpen) {
      previousFocus.current = document.activeElement;
      modalRef.current?.focus();
    } else {
      previousFocus.current?.focus();
    }
  }, [isOpen]);

  return isOpen ? (
    <div
      ref={modalRef}
      role="dialog"
      tabIndex={-1}
      onKeyDown={(e) => e.key === 'Escape' && onClose()}
    >
      {children}
    </div>
  ) : null;
}
```
