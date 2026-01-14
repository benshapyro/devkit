---
tool: claude-code
description: Gather production error context for debugging. Accepts stack traces, error messages, or error tracking URLs.
allowed-tools: Read, Grep, Glob, Bash(git:*)
argument-hint: <error-input>
---

# /trace

Debug production errors by gathering complete context automatically.

## Usage

```
/trace <error-input>
```

Where `<error-input>` is:
- A pasted stack trace
- An error message
- A Sentry/Bugsnag/Datadog URL

## Process

### 1. Parse Error Input

Analyze the input to extract:
- Error type (TypeError, NullPointerException, etc.)
- Error message
- Stack trace frames (file paths and line numbers)

**Stack trace patterns to recognize:**

```
# JavaScript/TypeScript
at FunctionName (file/path.ts:42:15)
at file/path.js:42:15

# Python
File "file/path.py", line 42, in function_name

# Java/Kotlin
at com.example.Class.method(File.java:42)

# Go
file/path.go:42 +0x1a4

# Rust
at src/main.rs:42:15
```

### 2. Gather Context

For each file:line in the stack trace (prioritize top frames):

**Read source code:**
```
Read file at path, show lines ±10 around error line
```

**Get git blame:**
```bash
git blame -L {line-5},{line+5} {file}
```

**Find recent commits:**
```bash
git log --oneline -5 -- {file}
```

**Search for similar errors:**
```bash
git log --all --oneline --grep="{error_type}" -- {file}
```

### 3. Search for Related Patterns

Look for:
- Similar error handling in the codebase
- Tests that cover the error location
- Configuration that might affect the behavior

```
Grep for: {function_name}, {error_type}, {variable_name}
```

### 4. Generate Diagnostic Report

```markdown
## Error Diagnostic Report

### Error Summary
**Type:** {error_type}
**Message:** {error_message}
**Location:** {file}:{line}

---

### Source Context

**{file}:{line}**
```{language}
{5 lines before}
>>> {error line highlighted}  // <-- ERROR HERE
{5 lines after}
```

---

### Git Blame

| Line | Author | Date | Commit | Message |
|------|--------|------|--------|---------|
| {line} | {author} | {date} | {hash} | {msg} |

---

### Recent Changes to This File

| Commit | Date | Author | Message |
|--------|------|--------|---------|
| {hash} | {date} | {author} | {message} |

---

### Root Cause Hypothesis

Based on the code and context:

1. **Most likely cause:** {hypothesis}
   - Evidence: {supporting details}

2. **Alternative possibility:** {hypothesis}
   - Evidence: {supporting details}

---

### Similar Past Issues

{Search results for similar errors in git history}

---

### Suggested Investigation

1. [ ] {First thing to check}
2. [ ] {Second thing to check}
3. [ ] {Third thing to check}

### Quick Fixes to Try

```{language}
// Potential fix 1
{code suggestion}
```

---

### Related Files

These files may be relevant:
- {related_file_1} - {why it's relevant}
- {related_file_2} - {why it's relevant}
```

## Example

Input:
```
/trace TypeError: Cannot read property 'user' of undefined
    at AuthController.getProfile (src/auth/controller.ts:45)
    at Router.handle (node_modules/express/router.js:123)
```

Output: A full diagnostic report with source context, blame info, recent changes, and investigation suggestions.

## Notes

- Focus on application code, not node_modules/vendor code
- Prioritize top stack frames (closest to error)
- If error tracking URL provided, fetch additional context if accessible
- Include test file locations for the affected code
