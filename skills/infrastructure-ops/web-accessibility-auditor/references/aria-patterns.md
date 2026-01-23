# ARIA Patterns

Correct ARIA usage for common UI components.

## ARIA Fundamentals

### The First Rule of ARIA

> "No ARIA is better than bad ARIA"

Use semantic HTML first. ARIA only when HTML cannot express the pattern.

```html
<!-- Bad: ARIA on div -->
<div role="button" tabindex="0" onclick="submit()">Submit</div>

<!-- Good: native HTML -->
<button onclick="submit()">Submit</button>
```

### The Five Rules of ARIA

1. **Use native HTML** when possible
2. **Don't change semantics** unless necessary
3. **All interactive ARIA** must be keyboard accessible
4. **Don't hide focusable elements** with aria-hidden
5. **All interactive elements** need accessible names

---

## Common Patterns

### Button

```html
<!-- Native (preferred) -->
<button>Save</button>

<!-- ARIA (when needed) -->
<div role="button" tabindex="0" aria-pressed="false">
  Toggle Dark Mode
</div>
```

**Required keyboard:**
- Enter/Space: Activate

### Link

```html
<!-- Native (preferred) -->
<a href="/page">Link Text</a>

<!-- ARIA (for SPA navigation) -->
<span role="link" tabindex="0" onclick="navigate()">
  Navigate
</span>
```

### Checkbox

```html
<!-- Native -->
<label>
  <input type="checkbox" checked> Accept terms
</label>

<!-- ARIA -->
<div role="checkbox"
     tabindex="0"
     aria-checked="true"
     aria-labelledby="terms-label">
  <span id="terms-label">Accept terms</span>
</div>
```

**States:**
- `aria-checked="true"` - checked
- `aria-checked="false"` - unchecked
- `aria-checked="mixed"` - indeterminate

### Radio Group

```html
<div role="radiogroup" aria-labelledby="color-label">
  <span id="color-label">Choose a color:</span>
  <div role="radio" tabindex="0" aria-checked="true">Red</div>
  <div role="radio" tabindex="-1" aria-checked="false">Blue</div>
  <div role="radio" tabindex="-1" aria-checked="false">Green</div>
</div>
```

**Keyboard:**
- Arrow keys: Move selection
- Tab: Move to/from group

### Tabs

```html
<div role="tablist" aria-label="Product tabs">
  <button role="tab"
          id="tab-1"
          aria-selected="true"
          aria-controls="panel-1">
    Description
  </button>
  <button role="tab"
          id="tab-2"
          aria-selected="false"
          aria-controls="panel-2"
          tabindex="-1">
    Reviews
  </button>
</div>

<div role="tabpanel"
     id="panel-1"
     aria-labelledby="tab-1">
  Product description content...
</div>

<div role="tabpanel"
     id="panel-2"
     aria-labelledby="tab-2"
     hidden>
  Reviews content...
</div>
```

**Keyboard:**
- Arrow Left/Right: Switch tabs
- Home/End: First/last tab
- Tab: Move into panel

### Dialog (Modal)

```html
<div role="dialog"
     aria-modal="true"
     aria-labelledby="dialog-title"
     aria-describedby="dialog-desc">
  <h2 id="dialog-title">Confirm Delete</h2>
  <p id="dialog-desc">Are you sure you want to delete this item?</p>
  <button>Cancel</button>
  <button>Delete</button>
</div>
```

**Requirements:**
- Focus trapped inside modal
- Escape closes modal
- Focus returns to trigger on close

### Alert

```html
<!-- Polite announcement -->
<div role="status" aria-live="polite">
  Form saved successfully
</div>

<!-- Urgent announcement -->
<div role="alert" aria-live="assertive">
  Session expired. Please log in again.
</div>
```

### Menu

```html
<button aria-haspopup="true" aria-expanded="false" aria-controls="menu-1">
  Options
</button>

<ul role="menu" id="menu-1" aria-label="Options">
  <li role="menuitem" tabindex="0">Edit</li>
  <li role="menuitem" tabindex="-1">Duplicate</li>
  <li role="menuitem" tabindex="-1">Delete</li>
</ul>
```

**Keyboard:**
- Arrow Up/Down: Navigate items
- Enter/Space: Select item
- Escape: Close menu

### Combobox (Autocomplete)

```html
<label for="city">City</label>
<input type="text"
       id="city"
       role="combobox"
       aria-autocomplete="list"
       aria-expanded="true"
       aria-controls="city-listbox"
       aria-activedescendant="city-option-3">

<ul role="listbox" id="city-listbox">
  <li role="option" id="city-option-1">New York</li>
  <li role="option" id="city-option-2">Los Angeles</li>
  <li role="option" id="city-option-3" aria-selected="true">Chicago</li>
</ul>
```

### Accordion

```html
<div class="accordion">
  <h3>
    <button aria-expanded="true" aria-controls="section-1">
      Section 1
    </button>
  </h3>
  <div id="section-1" role="region" aria-labelledby="section-1-heading">
    Content for section 1...
  </div>

  <h3>
    <button aria-expanded="false" aria-controls="section-2">
      Section 2
    </button>
  </h3>
  <div id="section-2" hidden>
    Content for section 2...
  </div>
</div>
```

---

## Live Regions

### Types

| Attribute | Behavior |
|-----------|----------|
| `aria-live="polite"` | Announces when idle |
| `aria-live="assertive"` | Announces immediately |
| `role="status"` | Polite, status messages |
| `role="alert"` | Assertive, important updates |
| `role="log"` | Polite, chat/activity logs |

### Best Practices

```html
<!-- Add to DOM first, then update content -->
<div id="status" role="status" aria-live="polite"></div>

<script>
// This will be announced
document.getElementById('status').textContent = 'Saved!';
</script>
```

---

## States and Properties

### Common States

| State | Purpose |
|-------|---------|
| `aria-expanded` | Disclosure widgets |
| `aria-selected` | Selection state |
| `aria-checked` | Checkboxes, switches |
| `aria-pressed` | Toggle buttons |
| `aria-disabled` | Disabled state |
| `aria-hidden` | Hide from AT |
| `aria-invalid` | Form validation |
| `aria-busy` | Loading state |

### Relationships

| Property | Purpose |
|----------|---------|
| `aria-labelledby` | References visible label |
| `aria-describedby` | References description |
| `aria-controls` | References controlled element |
| `aria-owns` | Parent-child relationship |
| `aria-activedescendant` | Current focus in composite |

---

## Common Mistakes

### Hidden Content

```html
<!-- Bad: hidden from all users -->
<button aria-hidden="true">Submit</button>

<!-- Bad: visible but hidden from AT -->
<div aria-hidden="true">Important info</div>
```

### Redundant ARIA

```html
<!-- Bad: button already has implicit role -->
<button role="button">Click</button>

<!-- Bad: link already has implicit role -->
<a href="/" role="link">Home</a>
```

### Invalid ARIA

```html
<!-- Bad: made-up role -->
<div role="card">...</div>

<!-- Bad: invalid attribute -->
<input aria-placeholder="Enter name">
```

### Missing Keyboard

```html
<!-- Bad: clickable but not focusable -->
<div role="button" onclick="submit()">Submit</div>

<!-- Good: focusable and activatable -->
<div role="button" tabindex="0" onclick="submit()"
     onkeydown="if(event.key==='Enter')submit()">Submit</div>
```
