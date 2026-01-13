# Assets

User-facing files, templates, and SOPs. These are NOT loaded into Claude's context — they're presented to users or used as output templates.

## Directory Structure

```
assets/
├── artifact-kit/          # Reusable UI components
├── artifact-templates/    # Complete artifact layouts
├── templates/             # Document and spreadsheet templates
└── sops/                  # Standard Operating Procedures
```

---

## Artifact Kit

Reusable Cadre-branded UI components for building artifacts.

| File | Format | Description |
|------|--------|-------------|
| `cadre-components.jsx` | JSX | React components for Claude artifacts |
| `cadre-components.html` | HTML | Standalone HTML version for Cadre Portal |

**Usage:** Import components into artifact templates. JSX for Claude artifacts, HTML for portal embedding.

---

## Artifact Templates

Complete layouts for client-facing artifacts.

| File | Format | Description |
|------|--------|-------------|
| `tech-stack-overview.html` | HTML | Visualize client's technology landscape |
| `integration-map.jsx` | JSX | Interactive connection diagram (Claude artifact) |
| `integration-map.html` | HTML | Static integration map (portal version) |
| `findings-summary.html` | HTML | Discovery session findings visualization |
| `solution-catalog.html` | HTML | AI solutions catalog for clients |
| `transformation-deck.html` | HTML | Strategy transformation overview |
| `client-kickoff.html` | HTML | Project kickoff presentation |
| `monthly-business-review.html` | HTML | MBR artifact format |
| `roi-calculator.jsx` | JSX | Interactive ROI calculation tool |

**Dual formats:** JSX templates are for Claude artifacts. HTML versions embed in Cadre Portal.

---

## Templates

Document and spreadsheet templates.

### Documents

| File | Format | Description |
|------|--------|-------------|
| `mbr-template-01-07-25.pptx` | PPTX | Current Monthly Business Review template |
| `scoping-template.docx` | DOCX | Solution scoping document |
| `prioritization-matrix.docx` | DOCX | Opportunity prioritization worksheet |

### Spreadsheets

| File | Format | Description |
|------|--------|-------------|
| `discovery-catalog-lite-template.xlsx` | XLSX | Lite mode discovery capture (offline) |
| `tech-stack-survey-template.xlsx` | XLSX | Blank tech stack survey grid |
| `scoping-spreadsheet.xlsx` | XLSX | Detailed scoping calculations |
| `use-case-library.xlsx` | XLSX | Master use case reference |

## SOPs (Standard Operating Procedures)

User-facing process documentation. Present these when users ask "how do I...?" or "what's the process for...?"

| File | Description |
|------|-------------|
| `discovery-catalog-sop.md` | End-to-end discovery catalog process |
| `tech-stack-survey-sop.md` | Tech stack survey collection and parsing |
| `solutions-sop.md` | AI solutions discovery and scoping workflow |

**Behavior:**
- **Present** SOP when user asks about process
- **Follow** SOP when user requests action
- Claude reads both SOP and detailed reference files when executing

---

## Placeholder Conventions

Different asset types use different placeholder patterns:

### Artifact Templates (`artifact-templates/`)

Use example data directly — replace with real client data:

```html
<title>Acme Corp - Tech Stack Overview</title>
<!-- Replace "Acme Corp" with actual client name -->
```

### Common Placeholders

| Placeholder | Description |
|-------------|-------------|
| `[CLIENT_NAME]` or "Acme Corp" | Client organization name |
| `[DATE]` | Current date |
| `[CONSULTANT_NAME]` | Cadre consultant name |
| `[LIMIT]`, `[X]` | Numeric values to customize |

---

## Binary File Versioning

Date-versioned filenames: `mbr-template-01-07-25.pptx`

When updating binary templates:
1. Create new file with current date suffix
2. Mark old version as legacy or remove
3. Update references in SKILL.md

---

## Modifying Assets

### HTML/JSX Artifacts
1. Edit the template file
2. Preserve CSS variable usage (`var(--cadre-primary)`)
3. Test in Claude artifact or portal
4. Maintain both JSX and HTML versions if applicable

### PPTX/DOCX Templates
1. Open in respective application
2. Maintain Cadre brand styling
3. Update version date in filename
4. Keep deprecated versions until full migration

### XLSX Spreadsheets
1. Preserve formula cells
2. Maintain column headers exactly
3. Test with sample data
4. Update schema documentation if structure changes

## Troubleshooting

| Issue | Solution |
|-------|----------|
| CSS variables not rendering | Ensure `<style>` block includes Cadre CSS variable definitions |
| JSX not compiling | Check for React/JSX syntax compatibility with Claude artifacts |
| XLSX formulas broken | Verify cell references after structural changes |
| Legacy template used | Check SKILL.md references point to current version |
