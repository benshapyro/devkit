# WCAG 2.2 Checklist

All success criteria organized by principle and level.

## Level A - Minimum

### 1. Perceivable

#### 1.1.1 Non-text Content
All non-text content has text alternatives.

```html
<!-- Image with alt text -->
<img src="chart.png" alt="Sales increased 25% from Q1 to Q2">

<!-- Decorative image -->
<img src="decorative-line.png" alt="" role="presentation">

<!-- Icon button -->
<button aria-label="Close dialog">
  <svg>...</svg>
</button>
```

**Check:**
- [ ] All images have alt text
- [ ] Decorative images have empty alt=""
- [ ] Icon buttons have accessible names
- [ ] CAPTCHA has audio alternative

#### 1.2.1 Audio-only and Video-only
Provide alternatives for pre-recorded media.

- Audio-only: Provide transcript
- Video-only: Provide transcript OR audio description

#### 1.2.2 Captions (Prerecorded)
All prerecorded video has synchronized captions.

#### 1.2.3 Audio Description (Prerecorded)
Video content has audio description of visual information.

#### 1.3.1 Info and Relationships
Information and relationships are programmatically determinable.

```html
<!-- Use semantic HTML -->
<table>
  <thead><tr><th>Name</th><th>Price</th></tr></thead>
  <tbody><tr><td>Widget</td><td>$10</td></tr></tbody>
</table>

<!-- Associate labels with inputs -->
<label for="email">Email:</label>
<input type="email" id="email">

<!-- Use headings properly -->
<h1>Page Title</h1>
<h2>Section</h2>
<h3>Subsection</h3>
```

#### 1.3.2 Meaningful Sequence
Reading order is logical when CSS is disabled.

#### 1.3.3 Sensory Characteristics
Instructions don't rely solely on shape, size, location, or sound.

```html
<!-- Bad: relies on color/position -->
<p>Click the green button on the right</p>

<!-- Good: includes text -->
<p>Click the "Submit" button</p>
```

#### 1.4.1 Use of Color
Color is not the only way to convey information.

```html
<!-- Bad: only color indicates error -->
<input style="border: 2px solid red">

<!-- Good: includes icon and text -->
<input style="border: 2px solid red" aria-invalid="true">
<span class="error">⚠ Email is required</span>
```

#### 1.4.2 Audio Control
Audio that plays automatically can be paused/stopped.

### 2. Operable

#### 2.1.1 Keyboard
All functionality available via keyboard.

#### 2.1.2 No Keyboard Trap
Keyboard focus can be moved away from any component.

#### 2.1.4 Character Key Shortcuts
Shortcuts using single character keys can be turned off or remapped.

#### 2.2.1 Timing Adjustable
Time limits can be extended or turned off.

#### 2.2.2 Pause, Stop, Hide
Moving/auto-updating content can be paused.

#### 2.3.1 Three Flashes
No content flashes more than 3 times per second.

#### 2.4.1 Bypass Blocks
Skip links to bypass repeated content.

```html
<a href="#main-content" class="skip-link">Skip to main content</a>
<!-- navigation -->
<main id="main-content">...</main>
```

#### 2.4.2 Page Titled
Pages have descriptive titles.

```html
<title>Contact Us - Company Name</title>
```

#### 2.4.3 Focus Order
Focus order is logical and meaningful.

#### 2.4.4 Link Purpose (In Context)
Link purpose is clear from link text or context.

```html
<!-- Bad -->
<a href="/article">Click here</a>

<!-- Good -->
<a href="/article">Read the full accessibility guide</a>
```

#### 2.5.1 Pointer Gestures
Multi-point or path-based gestures have single-pointer alternatives.

#### 2.5.2 Pointer Cancellation
Actions complete on up-event, can be aborted.

#### 2.5.3 Label in Name
Accessible name contains visible text.

#### 2.5.4 Motion Actuation
Motion-based functionality has alternatives and can be disabled.

### 3. Understandable

#### 3.1.1 Language of Page
Page language is identified.

```html
<html lang="en">
```

#### 3.2.1 On Focus
Focus doesn't cause unexpected context change.

#### 3.2.2 On Input
Input doesn't cause unexpected context change without warning.

#### 3.3.1 Error Identification
Errors are identified and described in text.

#### 3.3.2 Labels or Instructions
Form inputs have labels or instructions.

### 4. Robust

#### 4.1.1 Parsing (Obsolete in 2.2)
Valid HTML no longer required.

#### 4.1.2 Name, Role, Value
All UI components have accessible names and roles.

---

## Level AA - Standard Target

### 1. Perceivable

#### 1.2.4 Captions (Live)
Live video has real-time captions.

#### 1.2.5 Audio Description (Prerecorded)
Video has audio description.

#### 1.3.4 Orientation
Content not locked to single orientation.

#### 1.3.5 Identify Input Purpose
Input purpose can be programmatically determined.

```html
<input type="email" autocomplete="email">
<input type="tel" autocomplete="tel">
```

#### 1.4.3 Contrast (Minimum)
Text has 4.5:1 contrast ratio (3:1 for large text).

**Large text:** 18pt (24px) or 14pt (18.5px) bold

#### 1.4.4 Resize Text
Text can be resized to 200% without loss.

#### 1.4.5 Images of Text
Use real text, not images of text.

#### 1.4.10 Reflow
Content reflows at 320px width without horizontal scrolling.

#### 1.4.11 Non-text Contrast
UI components and graphics have 3:1 contrast.

#### 1.4.12 Text Spacing
Content remains usable with adjusted text spacing.

#### 1.4.13 Content on Hover or Focus
Hover/focus content is dismissible, hoverable, persistent.

### 2. Operable

#### 2.4.5 Multiple Ways
Multiple ways to find pages (navigation, search, sitemap).

#### 2.4.6 Headings and Labels
Headings and labels are descriptive.

#### 2.4.7 Focus Visible
Keyboard focus is visible.

```css
:focus {
  outline: 2px solid #0066cc;
  outline-offset: 2px;
}
```

#### 2.4.11 Focus Not Obscured (Minimum) - New in 2.2
Focused element is not entirely hidden.

#### 2.5.7 Dragging Movements - New in 2.2
Drag operations have single-pointer alternatives.

#### 2.5.8 Target Size (Minimum) - New in 2.2
Touch targets are at least 24x24 CSS pixels.

### 3. Understandable

#### 3.1.2 Language of Parts
Language changes are marked.

```html
<p>The French word <span lang="fr">bonjour</span> means hello.</p>
```

#### 3.2.3 Consistent Navigation
Navigation is consistent across pages.

#### 3.2.4 Consistent Identification
Components with same function identified consistently.

#### 3.3.3 Error Suggestion
Error messages suggest corrections.

#### 3.3.4 Error Prevention (Legal, Financial, Data)
Actions can be reviewed, confirmed, or reversed.

#### 3.3.7 Redundant Entry - New in 2.2
Previously entered information auto-populated or selectable.

#### 3.3.8 Accessible Authentication (Minimum) - New in 2.2
No cognitive tests required for auth (allow password managers, copy-paste).

---

## Level AAA - Enhanced

Most demanding. Not typically required but consider for specialized audiences.

#### 1.2.6 Sign Language (Prerecorded)
#### 1.2.7 Extended Audio Description
#### 1.2.8 Media Alternative (Prerecorded)
#### 1.2.9 Audio-only (Live)
#### 1.3.6 Identify Purpose
#### 1.4.6 Contrast (Enhanced) - 7:1 ratio
#### 1.4.7 Low or No Background Audio
#### 1.4.8 Visual Presentation
#### 1.4.9 Images of Text (No Exception)
#### 2.1.3 Keyboard (No Exception)
#### 2.2.3 No Timing
#### 2.2.4 Interruptions
#### 2.2.5 Re-authenticating
#### 2.2.6 Timeouts
#### 2.3.2 Three Flashes
#### 2.3.3 Animation from Interactions
#### 2.4.8 Location
#### 2.4.9 Link Purpose (Link Only)
#### 2.4.10 Section Headings
#### 2.4.12 Focus Not Obscured (Enhanced) - New in 2.2
#### 2.4.13 Focus Appearance - New in 2.2
#### 2.5.5 Target Size (Enhanced) - 44x44 pixels
#### 2.5.6 Concurrent Input Mechanisms
#### 3.1.3-3.1.6 Language features
#### 3.2.5 Change on Request
#### 3.2.6 Consistent Help - New in 2.2
#### 3.3.5 Help
#### 3.3.6 Error Prevention (All)
#### 3.3.9 Accessible Authentication (Enhanced) - New in 2.2
