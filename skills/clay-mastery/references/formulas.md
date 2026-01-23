# Clay Formulas Reference

This reference covers both the **AI Formula Generator** (for creating formulas with plain English) and **Clayscript** (the underlying code). When helping users create formulas, always provide both outputs.

## Table of Contents
1. [AI Formula Generator](#ai-formula-generator)
2. [Clayscript Syntax](#clayscript-syntax)
3. [JavaScript Essentials](#javascript-essentials)
4. [Lodash (_) Functions](#lodash-_-functions)
5. [Moment.js Date Handling](#momentjs-date-handling)
6. [FormulaJS Spreadsheet Functions](#formulajs-spreadsheet-functions)
7. [Conditional Run Patterns](#conditional-run-patterns)
8. [Formula Examples (Both Formats)](#formula-examples-both-formats)
9. [Debugging & Troubleshooting](#debugging--troubleshooting)

---

## AI Formula Generator

The AI Formula Generator converts plain English descriptions into Clayscript code. It's **FREE** (0 credits) and the fastest way to create formulas.

### How to Access

**Method 1:** Click column header → Edit Column → Formula
**Method 2:** Add Enrichment → Tools → Formula

### Writing Effective Descriptions

The key to good formula generation is **specificity**. Write like you're explaining to someone who doesn't know your data.

#### Column References

In the AI generator, use `/` to reference columns:
- `/Email` → references the Email column
- `/Company Name` → references Company Name column
- Type `/` and a picker appears showing all columns

The generator converts `/field` references to `{{Field}}` syntax automatically.

#### Best Practices

| Do This | Not This |
|---------|----------|
| "Extract the domain from /Email by splitting on @ and taking the part after it" | "Get domain from email" |
| "Return 'Enterprise' if /Employee Count is greater than 1000, 'Mid-Market' if between 100-1000, otherwise 'SMB'" | "Categorize by size" |
| "Check if /Title contains CEO, CFO, CTO, or COO (case insensitive) and return true if it does" | "Find executives" |
| "Calculate the number of days between /Created Date and today" | "How old is the lead" |
| "Combine /First Name and /Last Name with a space between them" | "Make full name" |

#### Formula Description Template

Use this structure for complex formulas:

```
[ACTION] using /Column1 and /Column2.
If [CONDITION], return [VALUE1].
Otherwise, return [VALUE2].
Treat missing/empty values as [DEFAULT].
```

**Example:**
```
Classify company size using /Employee Count.
If greater than 1000, return "Enterprise".
If between 100 and 1000, return "Mid-Market".
If between 10 and 100, return "SMB".
Otherwise, return "Startup".
Treat missing values as "Unknown".
```

### Three Main Use Cases

1. **Conditional Logic** - Run enrichments only when conditions are met
2. **Data Formatting** - Transform, combine, or reformat existing data  
3. **Data Cleaning** - Extract, validate, or standardize messy data

### Iteration Workflow

1. Write description and click "Generate Formula"
2. Review sample outputs on 3 rows
3. If wrong: Click "Output is wrong" → manually edit expected outputs → "Try generating with expected outputs"
4. If right: Click "Output is correct. Save formula"

### Common Pitfalls

| Problem | Solution |
|---------|----------|
| Column not found | Use exact column name from picker (case-sensitive) |
| Smart quotes breaking formula | Replace " " with straight quotes "" |
| Formula errors on empty cells | Add "Treat missing values as empty string" |
| Partial word matches (e.g., "micro" matching "cro") | Specify "match whole word only" or "word boundary" |

---

## Clayscript Syntax

Clayscript is JavaScript-based and runs row-by-row. Four libraries are available:

| Library | Access | Best For |
|---------|--------|----------|
| Standard JavaScript | Native | String manipulation, math, logic |
| Lodash | `_` | Array/object manipulation |
| Moment.js | `moment` | Date parsing and formatting |
| FormulaJS | Function names | Excel-style functions (SUM, VLOOKUP, IF) |

### Column References in Code

```javascript
{{Column Name}}                    // Basic reference
{{Column Name||""}}                // Fallback if empty (empty string)
{{Column Name||"N/A"}}             // Fallback with custom value
{{Column Name||0}}                 // Fallback for numbers
```

### Basic Operators

| Operator | Meaning | Example |
|----------|---------|---------|
| `+` | Add/concatenate | `{{First}} + " " + {{Last}}` |
| `-`, `*`, `/` | Math | `{{Revenue}} / {{Employees}}` |
| `===` | Equals (strict) | `{{Country}} === "USA"` |
| `!==` | Not equals | `{{Status}} !== "Closed"` |
| `>`, `<`, `>=`, `<=` | Comparison | `{{Score}} >= 70` |
| `&&` | AND | `{{A}} > 10 && {{B}} === "Yes"` |
| `\|\|` | OR | `{{A}} > 10 \|\| {{B}} === "Yes"` |
| `!` | NOT | `!{{Email}}` (true if empty) |
| `? :` | Ternary (if/else) | `{{X}} > 5 ? "High" : "Low"` |

### Ternary Chains

```javascript
{{Employee Count}} > 1000 ? "Enterprise" :
{{Employee Count}} > 100 ? "Mid-Market" :
{{Employee Count}} > 10 ? "SMB" : "Startup"
```

---

## JavaScript Essentials

### String Methods

```javascript
// Case
{{Text}}.toLowerCase()
{{Text}}.toUpperCase()

// Whitespace
{{Text}}.trim()

// Substrings
{{Text}}.slice(0, 10)              // First 10 chars
{{Text}}.substring(5)              // From position 5

// Search
{{Email}}.includes("@gmail")       // true/false
{{Title}}.startsWith("VP")
{{Domain}}.endsWith(".edu")

// Split & join
{{Email}}.split("@")               // ["user", "domain.com"]
{{Email}}.split("@")[1]            // "domain.com"
{{Email}}.split("@").pop()         // "domain.com" (last)

// Replace
{{Text}}.replace("old", "new")     // First occurrence
{{Text}}.replace(/old/g, "new")    // All occurrences

// Length
{{Text}}.length
```

### Array Methods

```javascript
{{Array}}[0]                       // First element
{{Array}}.pop()                    // Last element
{{Array}}.join(", ")               // To string
{{Array}}.slice(0, 3)              // First 3
{{Array}}.length                   // Count
```

### Number Methods

```javascript
Number({{Text}})                   // Convert to number
parseInt({{Text}})                 // To integer
parseFloat({{Text}})               // To decimal
{{Number}}.toFixed(2)              // 2 decimal places

// Math
Math.round({{Number}})
Math.floor({{Number}})
Math.ceil({{Number}})
Math.abs({{Number}})
Math.max(10, 20, 30)               // 30
Math.min(10, 20, 30)               // 10
```

### Regular Expressions

```javascript
// Test for match
/pattern/i.test({{Text}})          // i = case-insensitive

// Title matching
/ceo|cfo|cto|founder/i.test({{Title}})

// Word boundary (prevents "micro" matching "cro")
/\b(cro|ceo)\b/i.test({{Title}})

// Extract
{{Text}}.match(/\d+/)              // First number
{{Text}}.match(/\d+/g)             // All numbers

// Common patterns
/^[^\s@]+@[^\s@]+\.[^\s@]+$/       // Email
/^\+?[\d\s-]{10,}$/                // Phone
```

---

## Lodash (_) Functions

### Safe Property Access

```javascript
_.get({{Object}}, 'user.address.city')
_.get({{Object}}, 'user.city', 'Unknown')  // With default
```

### Array Operations

```javascript
// Duplicates
_.uniq([1, 2, 2, 3])                       // [1, 2, 3]
_.uniqBy({{Array}}, 'email')               // Unique by property

// Filter & find
_.filter({{Array}}, {active: true})        // All matching
_.find({{Array}}, {id: 123})               // First match

// Sort
_.sortBy({{Array}}, 'name')
_.orderBy({{Array}}, ['score'], ['desc'])

// Transform
_.map({{Array}}, 'email')                  // Extract property
_.flatten([[1,2], [3,4]])                  // [1,2,3,4]

// Group
_.groupBy({{Array}}, 'department')

// Aggregate
_.sumBy({{Array}}, 'amount')
_.meanBy({{Array}}, 'score')
_.maxBy({{Array}}, 'revenue')

// Combine
_.union([1,2], [2,3])                      // [1,2,3]
_.intersection([1,2,3], [2,3,4])           // [2,3]
_.difference([1,2,3], [2,3])               // [1]

// Access
_.first({{Array}})
_.last({{Array}})
_.take({{Array}}, 5)                       // First 5

// Check
_.includes({{Array}}, 'value')
_.isEmpty({{Array}})
```

### String Operations

```javascript
_.camelCase('hello world')                 // 'helloWorld'
_.snakeCase('Hello World')                 // 'hello_world'
_.startCase('hello world')                 // 'Hello World'
_.capitalize('hello')                      // 'Hello'
_.truncate({{Text}}, {length: 50})
_.trim({{Text}})
```

### Utility

```javascript
_.isString({{Value}})
_.isNumber({{Value}})
_.isArray({{Value}})
_.isEmpty({{Value}})
_.isNil({{Value}})                         // null or undefined
_.defaultTo({{Value}}, 'fallback')
_.cloneDeep({{Object}})
```

---

## Moment.js Date Handling

### Creating Moments

```javascript
moment()                                   // Now
moment('2024-03-15')                        // ISO format
moment('03/15/2024', 'MM/DD/YYYY')          // Custom format
moment({{Date Column}})                     // From column
```

### Format Tokens

| Token | Output | Example |
|-------|--------|---------|
| `YYYY` | 4-digit year | 2024 |
| `MM` | Month (01-12) | 03 |
| `MMM` | Month abbrev | Mar |
| `DD` | Day (01-31) | 15 |
| `Do` | Day ordinal | 15th |
| `dddd` | Weekday | Friday |
| `HH` | Hour 24h | 14 |
| `hh` | Hour 12h | 02 |
| `mm` | Minutes | 30 |
| `a` | am/pm | pm |

### Formatting

```javascript
moment({{Date}}).format('YYYY-MM-DD')      // 2024-03-15
moment({{Date}}).format('MMM D, YYYY')     // Mar 15, 2024
moment({{Date}}).format('h:mm A')          // 2:30 PM
```

### Date Math

```javascript
moment({{Date}}).add(7, 'days')
moment({{Date}}).subtract(30, 'days')
moment({{Date}}).startOf('month')
moment({{Date}}).endOf('week')
```

### Comparisons

```javascript
moment({{End}}).diff(moment({{Start}}), 'days')
moment({{Date}}).isBefore(moment())        // Is past?
moment({{Date}}).isAfter(moment())         // Is future?
moment({{Date}}).fromNow()                 // "3 days ago"
moment({{Date}}).isValid()                 // Check valid
```

---

## FormulaJS Spreadsheet Functions

### Logic

```javascript
IF({{Score}} >= 70, "Pass", "Fail")
AND({{A}} > 10, {{B}} === "Yes")
OR({{A}} > 10, {{B}} > 10)
IFERROR({{Formula}}, "Default")
```

### Math

```javascript
SUM([1, 2, 3])                             // 6
AVERAGE([85, 90, 78])                      // 84.33
COUNT([1, "text", 3])                      // 2
MAX([10, 50, 30])                          // 50
MIN([10, 50, 30])                          // 10
ROUND({{Number}}, 2)
```

### Text

```javascript
CONCATENATE({{First}}, " ", {{Last}})
LEFT({{Text}}, 5)
RIGHT({{Text}}, 3)
MID({{Text}}, 2, 5)
TRIM({{Text}})
UPPER({{Text}})
LOWER({{Text}})
PROPER({{Text}})                           // Title Case
LEN({{Text}})
SUBSTITUTE({{Text}}, "old", "new")
```

### Lookup

```javascript
VLOOKUP({{Search}}, {{Table}}, 2, false)
INDEX({{Array}}, MATCH({{Search}}, {{Column}}, 0))
```

### Date

```javascript
TODAY()
NOW()
YEAR({{Date}})
MONTH({{Date}})
DAY({{Date}})
DAYS({{End}}, {{Start}})
DATEDIF({{Start}}, {{End}}, "M")           // Months between
NETWORKDAYS({{Start}}, {{End}})            // Work days
```

### Conditional Aggregation

```javascript
COUNTIF({{Array}}, ">100")
SUMIF({{Array}}, ">100")
AVERAGEIF({{Array}}, ">0")
```

---

## Conditional Run Patterns

Control when enrichments run to save credits.

### Setup

1. Click column → Run Settings
2. Find "Only run if" box
3. Enter condition (plain English or formula)

### Common Patterns

```javascript
// Only if empty
!{{Email}}

// Score threshold
{{ICP Score}} >= 70

// Title matching
/vp|director|chief/i.test({{Title}}||"")

// Company size range
{{Employee Count}} >= 50 && {{Employee Count}} <= 500

// Not in CRM
!{{HubSpot ID}}

// Previous step empty (waterfall)
!{{Email 1}} || {{Email 1}} === ""

// Combined
{{ICP Score}} >= 70 && !{{Email}} && {{Country}} === "USA"
```

### Credit Gating Example

```
Column 1: Company enrichment - Run on all
Column 2: ICP Score (FREE formula) - Calculate fit
Column 3: Contact finder - ONLY IF {{ICP Score}} >= 60
Column 4: Email waterfall - ONLY IF {{Contact Found}}
Column 5: Phone enrichment - ONLY IF {{Email}} && {{ICP Score}} >= 80
```

---

## Formula Examples (Both Formats)

When creating formulas, provide BOTH the AI generator description AND the Clayscript code.

### Domain from Email

**AI Generator Description:**
```
Extract the domain from /Email by splitting on the @ symbol and returning the part after it. If email is empty, return empty string.
```

**Clayscript:**
```javascript
({{Email}}||"").split("@").pop() || ""
```

---

### Company Size Classification

**AI Generator Description:**
```
Classify company size using /Employee Count.
If greater than 1000, return "Enterprise".
If between 100 and 1000, return "Mid-Market".  
If between 10 and 100, return "SMB".
Otherwise return "Startup".
Treat missing values as "Unknown".
```

**Clayscript:**
```javascript
!{{Employee Count}} ? "Unknown" :
{{Employee Count}} > 1000 ? "Enterprise" :
{{Employee Count}} > 100 ? "Mid-Market" :
{{Employee Count}} > 10 ? "SMB" : "Startup"
```

---

### Title Seniority Detection

**AI Generator Description:**
```
Check /Title for executive titles. Return "C-Suite" if title contains CEO, CFO, CTO, COO, President, or Founder (case insensitive, whole words only). Return "VP" if contains VP or Vice President. Return "Director" if contains Director or Head of. Otherwise return "Other". Handle missing values as "Unknown".
```

**Clayscript:**
```javascript
!{{Title}} ? "Unknown" :
/\b(ceo|cfo|cto|coo|president|founder|co-?founder)\b/i.test({{Title}}) ? "C-Suite" :
/\b(vp|vice president|svp|evp)\b/i.test({{Title}}) ? "VP" :
/\b(director|head of)\b/i.test({{Title}}) ? "Director" : "Other"
```

---

### ICP Scoring

**AI Generator Description:**
```
Calculate ICP score by adding points:
- Add 25 if /Employee Count is over 100
- Add 25 if /Revenue is over 1000000
- Add 25 if /Industry equals "Technology" or "Software"
- Add 25 if /Title contains VP, Director, or Chief (case insensitive)
Return the total score (0-100).
```

**Clayscript:**
```javascript
({{Employee Count}} > 100 ? 25 : 0) +
({{Revenue}} > 1000000 ? 25 : 0) +
(/technology|software/i.test({{Industry}}||"") ? 25 : 0) +
(/vp|director|chief/i.test({{Title}}||"") ? 25 : 0)
```

---

### Days Since Created

**AI Generator Description:**
```
Calculate the number of days between /Created Date and today. Return as a whole number. If date is missing or invalid, return "N/A".
```

**Clayscript:**
```javascript
moment({{Created Date}}).isValid() 
  ? moment().diff(moment({{Created Date}}), 'days')
  : "N/A"
```

---

### Waterfall Result (First Non-Empty)

**AI Generator Description:**
```
Return the first non-empty value from /Email 1, /Email 2, or /Email 3. If all are empty, return "Not Found".
```

**Clayscript:**
```javascript
{{Email 1}} || {{Email 2}} || {{Email 3}} || "Not Found"
```

---

### Personal Email Filter

**AI Generator Description:**
```
Check if /Email is a business email. Return "Personal" if it contains gmail, yahoo, hotmail, outlook, or aol. Return "Business" otherwise. Case insensitive.
```

**Clayscript:**
```javascript
/(gmail|yahoo|hotmail|outlook|aol)/i.test({{Email}}||"") ? "Personal" : "Business"
```

---

### Full Name Combination

**AI Generator Description:**
```
Combine /First Name and /Last Name with a space between them. Trim any extra whitespace. If both are empty, return empty string.
```

**Clayscript:**
```javascript
(({{First Name}}||"") + " " + ({{Last Name}}||"")).trim()
```

---

### LinkedIn URL Builder

**AI Generator Description:**
```
Create a LinkedIn search URL by combining /First Name, /Last Name, and /Company Name. URL encode the search terms.
```

**Clayscript:**
```javascript
"https://www.linkedin.com/search/results/people/?keywords=" + 
encodeURIComponent(({{First Name}}||"") + " " + ({{Last Name}}||"") + " " + ({{Company Name}}||""))
```

---

### Clean Domain from URL

**AI Generator Description:**
```
Clean /Website URL by removing http://, https://, and www. prefix. Return only the domain without any path. Lowercase the result.
```

**Clayscript:**
```javascript
({{Website}}||"")
  .toLowerCase()
  .replace(/^https?:\/\//, "")
  .replace(/^www\./, "")
  .split("/")[0]
```

---

## Debugging & Troubleshooting

### Preview Testing

1. Click column with formula
2. Click "Preview" to see calculated values
3. Test on rows with edge cases (empty, unusual formats)

### Common Errors

| Error | Cause | Fix |
|-------|-------|-----|
| `undefined` | Column typo | Check exact name |
| `NaN` | Math on text | Use `Number({{Field}})` |
| Empty result | Null in chain | Add `\|\|""` fallback |
| `Cannot read property 'split'` | Method on null | `({{Field}}\|\|"").split(...)` |
| `Invalid date` | Bad format | Specify format in `moment()` |

### Safe Patterns

```javascript
// Safe strings
({{Email}}||"").toLowerCase()
({{Text}}||"").split(" ")

// Safe numbers
Number({{Revenue}}||0) > 1000000

// Safe dates
moment({{Date}}).isValid() ? moment({{Date}}).format('YYYY-MM-DD') : ""

// Safe arrays
({{Array}}||[])[0]
_.get({{Array}}, '[0]', 'default')

// Safe objects
_.get({{Object}}, 'nested.property', 'default')
```

### Testing Process

1. Test on 1 row first
2. Find edge cases: empty fields, nulls, weird formats
3. Add fallbacks for each edge case
4. Test on 10 diverse rows
5. Run full table only when confident
