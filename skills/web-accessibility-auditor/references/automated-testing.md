# Automated Testing

axe-core, pa11y, and CI integration for accessibility testing.

## Tool Comparison

| Tool | Type | Coverage | Best For |
|------|------|----------|----------|
| axe-core | Library | ~50% | Integration tests |
| Lighthouse | Browser | ~30% | Quick audits |
| pa11y | CLI/Library | ~40% | CI pipelines |
| WAVE | Browser ext | ~40% | Manual review |
| IBM Equal Access | Library | ~40% | Enterprise |

**Note:** Automated tools catch ~30-50% of issues. Manual testing required.

---

## axe-core

### Browser DevTools

1. Install axe DevTools extension
2. Open DevTools > axe DevTools
3. Click "Scan ALL of my page"

### Jest Integration

```bash
npm install @axe-core/react jest-axe --save-dev
```

```javascript
// setup-tests.js
import { toHaveNoViolations } from 'jest-axe';
expect.extend(toHaveNoViolations);
```

```javascript
// Component.test.js
import { render } from '@testing-library/react';
import { axe } from 'jest-axe';
import { MyComponent } from './MyComponent';

describe('MyComponent', () => {
  it('should have no accessibility violations', async () => {
    const { container } = render(<MyComponent />);
    const results = await axe(container);
    expect(results).toHaveNoViolations();
  });
});
```

### Cypress Integration

```bash
npm install cypress-axe --save-dev
```

```javascript
// cypress/support/commands.js
import 'cypress-axe';

// cypress/e2e/accessibility.cy.js
describe('Accessibility', () => {
  beforeEach(() => {
    cy.visit('/');
    cy.injectAxe();
  });

  it('has no detectable a11y violations on load', () => {
    cy.checkA11y();
  });

  it('checks specific element', () => {
    cy.checkA11y('.main-content');
  });

  it('excludes known issues', () => {
    cy.checkA11y(null, {
      rules: {
        'color-contrast': { enabled: false }
      }
    });
  });
});
```

### Playwright Integration

```bash
npm install @axe-core/playwright --save-dev
```

```javascript
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('should not have accessibility violations', async ({ page }) => {
  await page.goto('/');

  const accessibilityScanResults = await new AxeBuilder({ page }).analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});

// With options
test('should not have violations (with options)', async ({ page }) => {
  await page.goto('/');

  const accessibilityScanResults = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21aa'])
    .exclude('.third-party-widget')
    .analyze();

  expect(accessibilityScanResults.violations).toEqual([]);
});
```

---

## pa11y

### CLI Usage

```bash
# Install
npm install -g pa11y

# Basic scan
pa11y https://example.com

# With specific standard
pa11y --standard WCAG2AA https://example.com

# Output as JSON
pa11y --reporter json https://example.com > results.json

# Multiple pages
pa11y-ci https://example.com/page1 https://example.com/page2
```

### Configuration File

```json
// .pa11yci.json
{
  "defaults": {
    "standard": "WCAG2AA",
    "timeout": 30000,
    "wait": 1000,
    "chromeLaunchConfig": {
      "headless": true
    }
  },
  "urls": [
    "http://localhost:3000/",
    "http://localhost:3000/about",
    {
      "url": "http://localhost:3000/login",
      "actions": [
        "wait for element #login-form to be visible"
      ]
    }
  ]
}
```

### Node.js Usage

```javascript
const pa11y = require('pa11y');

async function testPage(url) {
  const results = await pa11y(url, {
    standard: 'WCAG2AA',
    includeWarnings: true,
    runners: ['htmlcs', 'axe']
  });

  console.log(`Issues found: ${results.issues.length}`);

  results.issues.forEach(issue => {
    console.log(`
      Type: ${issue.type}
      Code: ${issue.code}
      Message: ${issue.message}
      Selector: ${issue.selector}
    `);
  });
}

testPage('http://localhost:3000/');
```

---

## Lighthouse CI

### GitHub Actions

```yaml
# .github/workflows/lighthouse.yml
name: Lighthouse CI
on: [push]
jobs:
  lighthouse:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - run: npm install && npm run build

      - name: Run Lighthouse
        uses: treosh/lighthouse-ci-action@v10
        with:
          configPath: './lighthouserc.js'
          uploadArtifacts: true
          temporaryPublicStorage: true
```

### Configuration

```javascript
// lighthouserc.js
module.exports = {
  ci: {
    collect: {
      url: ['http://localhost:3000/', 'http://localhost:3000/about'],
      startServerCommand: 'npm run start',
    },
    assert: {
      assertions: {
        'categories:accessibility': ['error', { minScore: 0.9 }],
        'categories:best-practices': ['warn', { minScore: 0.9 }],
      },
    },
    upload: {
      target: 'temporary-public-storage',
    },
  },
};
```

---

## CI Pipeline Integration

### GitHub Actions (axe + Playwright)

```yaml
# .github/workflows/a11y.yml
name: Accessibility Tests
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  a11y:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Install Playwright
        run: npx playwright install --with-deps

      - name: Build
        run: npm run build

      - name: Run a11y tests
        run: npm run test:a11y

      - name: Upload report
        uses: actions/upload-artifact@v3
        if: always()
        with:
          name: a11y-report
          path: a11y-report/
```

### Pre-commit Hook

```json
// package.json
{
  "husky": {
    "hooks": {
      "pre-commit": "npm run lint && npm run test:a11y:changed"
    }
  },
  "scripts": {
    "test:a11y:changed": "pa11y-ci --sitemap http://localhost:3000/sitemap.xml --sitemap-find origin --sitemap-exclude /admin"
  }
}
```

---

## Handling Results

### Severity Levels

| Severity | Action | Example |
|----------|--------|---------|
| Critical | Block PR | Missing form labels |
| Serious | Block PR | Low contrast |
| Moderate | Warn | Minor issues |
| Minor | Log | Suggestions |

### Filtering False Positives

```javascript
// axe-config.js
module.exports = {
  rules: [
    // Disable specific rule
    { id: 'color-contrast', enabled: false },

    // Adjust severity
    { id: 'landmark-one-main', reviewOnFail: true },
  ],
  // Exclude third-party content
  exclude: [
    '.third-party-widget',
    '#ad-container',
    'iframe[src*="youtube"]'
  ]
};
```

### Baseline Approach

```javascript
// Record baseline (first run)
const baseline = await axe(page);
fs.writeFileSync('a11y-baseline.json', JSON.stringify(baseline));

// Compare against baseline
const current = await axe(page);
const newViolations = current.violations.filter(
  v => !baseline.violations.find(b => b.id === v.id)
);

if (newViolations.length > 0) {
  throw new Error(`New accessibility violations: ${newViolations.length}`);
}
```

---

## Reporting

### HTML Report

```javascript
const { createHtmlReport } = require('axe-html-reporter');

const results = await axe.run();

createHtmlReport({
  results,
  options: {
    projectKey: 'My Project',
    outputDir: 'a11y-report',
    reportFileName: 'accessibility-report.html'
  }
});
```

### JSON for Tracking

```javascript
const report = {
  timestamp: new Date().toISOString(),
  url: page.url(),
  violations: results.violations.length,
  passes: results.passes.length,
  incomplete: results.incomplete.length,
  details: results.violations
};

fs.writeFileSync('a11y-report.json', JSON.stringify(report, null, 2));
```

---

## Best Practices

1. **Run on every PR** - Catch issues early
2. **Test all page states** - Modals, errors, loading
3. **Use multiple tools** - axe + manual testing
4. **Set thresholds** - Block on critical/serious
5. **Track over time** - Monitor trends
6. **Document exceptions** - Explain disabled rules
