# Common Mistakes

Anti-patterns and how to fix them.

## The First Rule

> "No ARIA is better than bad ARIA"

Bad ARIA is worse than no ARIA. Broken accessibility is harder to use than default behavior.

---

## HTML Mistakes

### Missing Language

```html
<!-- Bad: No language declared -->
<html>

<!-- Good: Language declared -->
<html lang="en">

<!-- Good: Language change marked -->
<p>The German word <span lang="de">Kindergarten</span></p>
```

**Why:** Screen readers use language to select correct pronunciation.

### Skipped Heading Levels

```html
<!-- Bad: h1 → h3 (skips h2) -->
<h1>Page Title</h1>
<h3>Section</h3>

<!-- Good: Sequential -->
<h1>Page Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

**Why:** Screen reader users navigate by headings. Skipping breaks mental model.

### Empty Links

```html
<!-- Bad: No accessible name -->
<a href="/cart">
  <img src="cart.svg">
</a>

<!-- Good: Alt text on image -->
<a href="/cart">
  <img src="cart.svg" alt="Shopping cart (3 items)">
</a>

<!-- Good: aria-label -->
<a href="/cart" aria-label="Shopping cart (3 items)">
  <img src="cart.svg" alt="">
</a>
```

### Generic Link Text

```html
<!-- Bad: Not descriptive -->
<a href="/report">Click here</a>
<a href="/report">Read more</a>
<a href="/report">Learn more</a>

<!-- Good: Descriptive -->
<a href="/report">Download the Q3 sales report</a>

<!-- Good: Hidden text for context -->
<a href="/report">
  Read more <span class="sr-only">about our Q3 results</span>
</a>
```

---

## Form Mistakes

### Missing Labels

```html
<!-- Bad: Placeholder as label -->
<input type="email" placeholder="Email">

<!-- Bad: Label not associated -->
<label>Email</label>
<input type="email">

<!-- Good: Explicit association -->
<label for="email">Email</label>
<input type="email" id="email">

<!-- Good: Implicit association -->
<label>
  Email
  <input type="email">
</label>
```

### No Error Messages

```html
<!-- Bad: Only visual indication -->
<input type="email" style="border-color: red">

<!-- Good: Programmatic error -->
<label for="email">Email</label>
<input type="email" id="email" aria-invalid="true" aria-describedby="email-error">
<span id="email-error" class="error">Please enter a valid email address</span>
```

### Required Fields Not Indicated

```html
<!-- Bad: Color only -->
<label class="red">Email</label>
<input type="email">

<!-- Good: Multiple indicators -->
<label for="email">
  Email <span aria-hidden="true" class="required">*</span>
</label>
<input type="email" id="email" required aria-required="true">
<span class="field-note">* Required field</span>
```

---

## ARIA Mistakes

### Redundant ARIA

```html
<!-- Bad: Native element has implicit role -->
<button role="button">Click</button>
<a href="/" role="link">Home</a>
<input type="checkbox" role="checkbox">

<!-- Good: No redundant role -->
<button>Click</button>
<a href="/">Home</a>
<input type="checkbox">
```

### Invalid ARIA

```html
<!-- Bad: Made-up role -->
<div role="card">...</div>

<!-- Bad: Wrong attribute -->
<input aria-placeholder="Enter name">

<!-- Bad: Invalid value -->
<button aria-pressed="yes">...</button>

<!-- Good: Valid role -->
<div role="article">...</div>

<!-- Good: Valid attribute -->
<input placeholder="Enter name">

<!-- Good: Valid value -->
<button aria-pressed="true">...</button>
```

### aria-hidden on Focusable

```html
<!-- Bad: Hidden but still focusable -->
<div aria-hidden="true">
  <button>This is confusing</button>
</div>

<!-- Good: Also remove from tab order -->
<div aria-hidden="true" inert>
  <button tabindex="-1">Hidden</button>
</div>
```

### Misusing aria-label

```html
<!-- Bad: Overriding visible text -->
<button aria-label="Submit form">
  Cancel
</button>

<!-- Bad: Long description in aria-label -->
<button aria-label="Click this button to submit the form and proceed to the confirmation page">
  Submit
</button>

<!-- Good: Matches visible text -->
<button aria-label="Submit">
  Submit
</button>
```

---

## Keyboard Mistakes

### Removing Focus Styles

```css
/* Bad: No focus indication */
:focus {
  outline: none;
}

/* Good: Custom focus style */
:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}

/* Better: Focus-visible for keyboard only */
:focus:not(:focus-visible) {
  outline: none;
}
:focus-visible {
  outline: 2px solid #0066cc;
}
```

### Non-Focusable Interactive Elements

```html
<!-- Bad: Not keyboard accessible -->
<div onclick="submit()">Submit</div>

<!-- Still bad: Focusable but no keyboard handler -->
<div tabindex="0" onclick="submit()">Submit</div>

<!-- Good: Full keyboard support -->
<div tabindex="0"
     role="button"
     onclick="submit()"
     onkeydown="if(event.key==='Enter'||event.key===' ')submit()">
  Submit
</div>

<!-- Best: Use a button -->
<button onclick="submit()">Submit</button>
```

### Keyboard Traps

```html
<!-- Bad: No way to close with keyboard -->
<div class="modal">
  <input type="text">
  <!-- No close button, no Escape handler -->
</div>

<!-- Good: Escape closes, focus trapped -->
<div class="modal"
     role="dialog"
     aria-modal="true"
     onkeydown="if(event.key==='Escape')close()">
  <button onclick="close()">Close</button>
  <input type="text">
</div>
```

---

## Color and Contrast Mistakes

### Low Contrast Text

```css
/* Bad: 2.5:1 ratio */
.text {
  color: #888;
  background: #fff;
}

/* Good: 4.5:1 ratio for normal text */
.text {
  color: #595959;
  background: #fff;
}

/* Good: 3:1 ratio for large text */
.large-text {
  color: #767676;
  font-size: 24px;
}
```

### Color as Only Indicator

```html
<!-- Bad: Only color shows error -->
<input style="border-color: red">

<!-- Good: Icon + text + color -->
<input aria-invalid="true" aria-describedby="error">
<span id="error" class="error">
  ⚠️ This field is required
</span>
```

### Colorblind Unfriendly

```html
<!-- Bad: Red/green only -->
<span class="success">✓</span>
<span class="error">✗</span>

<!-- Good: Shape + text -->
<span class="success" aria-label="Success">✓ Passed</span>
<span class="error" aria-label="Error">✗ Failed</span>
```

---

## Image Mistakes

### Missing Alt Text

```html
<!-- Bad: No alt -->
<img src="photo.jpg">

<!-- Bad: Useless alt -->
<img src="photo.jpg" alt="image">
<img src="photo.jpg" alt="photo.jpg">

<!-- Good: Descriptive -->
<img src="photo.jpg" alt="Team meeting in conference room">
```

### Decorative Images Not Hidden

```html
<!-- Bad: Announced by screen readers -->
<img src="decorative-line.png" alt="decorative line">

<!-- Good: Hidden from AT -->
<img src="decorative-line.png" alt="">
<img src="decorative-line.png" alt="" role="presentation">
```

### Complex Images Without Description

```html
<!-- Bad: Alt text insufficient -->
<img src="chart.png" alt="Sales chart">

<!-- Good: Detailed description -->
<figure>
  <img src="chart.png" alt="Bar chart showing quarterly sales"
       aria-describedby="chart-desc">
  <figcaption id="chart-desc">
    Q1: $1.2M, Q2: $1.5M, Q3: $1.8M, Q4: $2.1M.
    Sales increased 75% over the year.
  </figcaption>
</figure>
```

---

## Quick Reference

| Mistake | Fix |
|---------|-----|
| No lang attribute | Add `lang="en"` to html |
| Skipped headings | Use sequential h1→h2→h3 |
| Empty links | Add alt or aria-label |
| "Click here" links | Make link text descriptive |
| No form labels | Associate labels with for/id |
| Error color only | Add text + icon |
| outline: none | Replace with visible focus |
| div onclick | Use button or add keyboard |
| Low contrast | Meet 4.5:1 / 3:1 ratios |
| Missing alt text | Add meaningful descriptions |
| Redundant ARIA | Remove when HTML suffices |
