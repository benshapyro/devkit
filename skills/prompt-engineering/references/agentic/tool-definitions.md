# Tool Definitions Guide

Tool description quality is the single most important factor in reliable tool use. Detailed descriptions produce 54% improvement in task success.

## Table of Contents
- [Why Tool Descriptions Matter](#why-tool-descriptions-matter)
- [Anatomy of a Great Tool Definition](#anatomy-of-a-great-tool-definition)
- [Required Elements](#required-elements)
- [Examples by Quality Level](#examples-by-quality-level)
- [Model-Specific Considerations](#model-specific-considerations)
- [Common Mistakes](#common-mistakes)

---

## Why Tool Descriptions Matter

Models decide when and how to use tools based entirely on the descriptions you provide. Vague descriptions lead to:
- Random tool selection
- Parameter guessing
- Missing edge cases
- Failed workflows

**Research finding:** Detailed tool descriptions (6+ sentences covering what/how/when/limitations) show 54% performance improvement over minimal descriptions.

---

## Anatomy of a Great Tool Definition

Every tool description should answer these questions:

1. **What does it do?** (core function)
2. **What does it return?** (output format)
3. **What does it NOT return?** (limitations)
4. **When should it be used?** (trigger conditions)
5. **What format does it expect?** (input requirements)
6. **What are the edge cases?** (special handling)

---

## Required Elements

### Minimum Description Length: 3-4 sentences

```json
{
  "name": "tool_name",
  "description": "[Sentence 1: What it does] [Sentence 2: What it returns] [Sentence 3: When to use it] [Sentence 4: Limitations or format requirements]",
  "input_schema": {
    "type": "object",
    "properties": {
      "param_name": {
        "type": "string",
        "description": "[Detailed parameter description including format, examples, edge cases]"
      }
    },
    "required": ["param_name"]
  }
}
```

### Parameter Descriptions

Each parameter needs:
- Type and format expectations
- Valid examples
- Edge case handling
- Default behavior (if applicable)

---

## Examples by Quality Level

### ❌ Bad: Minimal Description

```json
{
  "name": "search_database",
  "description": "Search the customer database",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {"type": "string"}
    }
  }
}
```

**Problems:**
- No indication of what can be searched
- No return format specified
- No guidance on query format
- No limitations mentioned

---

### ⚠️ Mediocre: Partial Description

```json
{
  "name": "search_database",
  "description": "Search the customer database by name, email, or customer ID. Returns matching customer records.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term"
      }
    }
  }
}
```

**Problems:**
- Still no format guidance
- No limitations
- Parameter description too brief

---

### ✅ Good: Comprehensive Description

```json
{
  "name": "search_database",
  "description": "Search the customer database by name, email, or customer ID. Returns an array of matching customer records including name, email, signup_date, and subscription_tier. Supports partial matching for names and emails (minimum 3 characters). LIMITATION: Maximum 50 results returned; use filters for large result sets. WHEN TO USE: When user asks about a specific customer, needs to look up customer details, or wants to find customers matching criteria.",
  "input_schema": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string",
        "description": "Search term. Can be: full/partial name (e.g., 'John', 'John Smith'), email address or partial email (e.g., 'john@', '@company.com'), or exact customer ID (e.g., 'CUST-12345'). Minimum 3 characters for partial matching."
      },
      "filter": {
        "type": "string",
        "enum": ["all", "active", "churned", "trial"],
        "description": "Filter results by customer status. Default: 'all'"
      },
      "limit": {
        "type": "integer",
        "description": "Maximum results to return. Default: 20, Maximum: 50"
      }
    },
    "required": ["query"]
  }
}
```

---

## Full Example: Weather Tool

```json
{
  "name": "get_weather",
  "description": "Get current weather information for a specific location. Returns temperature (in requested unit), weather conditions (sunny, cloudy, rainy, etc.), humidity percentage, and wind speed. IMPORTANT: Use city and state format for US locations (e.g., 'San Francisco, CA'). For international locations, include country (e.g., 'London, UK'). LIMITATION: Only returns current conditions—historical data and forecasts are not available through this tool. WHEN TO USE: When user asks about current weather, temperature, what to wear, or whether they need an umbrella.",
  "input_schema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "The location to get weather for. Format: 'City, State' for US (e.g., 'San Francisco, CA', 'New York, NY') or 'City, Country' for international (e.g., 'London, UK', 'Tokyo, Japan'). Be as specific as possible to avoid ambiguity."
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "Temperature unit for the response. Default: fahrenheit for US locations, celsius for international locations if not specified."
      }
    },
    "required": ["location"]
  }
}
```

---

## Full Example: File Operations Tool

```json
{
  "name": "read_file",
  "description": "Read the contents of a file from the project directory. Returns the full text content of the file as a string. Supports text files including .txt, .md, .json, .py, .js, .ts, .html, .css, and other text-based formats. LIMITATION: Cannot read binary files (images, PDFs, executables)—use appropriate tools for those formats. Maximum file size: 1MB. WHEN TO USE: When you need to examine file contents, understand existing code, check configuration, or reference documentation.",
  "input_schema": {
    "type": "object",
    "properties": {
      "path": {
        "type": "string",
        "description": "Relative path to the file from project root. Use forward slashes (e.g., 'src/components/Button.tsx', 'config/settings.json'). Do not include leading slash."
      },
      "encoding": {
        "type": "string",
        "enum": ["utf-8", "ascii", "latin-1"],
        "description": "File encoding. Default: 'utf-8'. Use 'latin-1' for legacy files with special characters."
      }
    },
    "required": ["path"]
  }
}
```

---

## Model-Specific Considerations

### Claude
- Integrates tools directly into message structure
- Benefits most from detailed descriptions
- Use `strict: true` for guaranteed schema conformance
- Opus defaults to chain-of-thought before tool calls

### GPT
- Separate tool definitions from usage rules
- Put detailed usage instructions in system prompt
- Include 2-3 examples in system prompt (not tool description)
- Use `tool_choice` to force specific tool when needed

### Gemini
- Native function calling support
- Benefits from clear trigger conditions
- Works well with hierarchical tool organization

---

## Common Mistakes

### 1. Relying on Tool Name Alone
❌ Assuming "search_customers" is self-explanatory
✅ Describe exactly what can be searched and what's returned

### 2. Missing Return Format
❌ "Returns customer information"
✅ "Returns JSON with fields: id, name, email, signup_date, status"

### 3. No Trigger Guidance
❌ Description only covers what tool does
✅ Include "WHEN TO USE:" section for disambiguation

### 4. Ambiguous Parameters
❌ `"query": {"type": "string"}`
✅ Include format, examples, valid ranges, edge cases

### 5. No Limitations
❌ Implying tool can do everything
✅ Explicitly state what it can't do, rate limits, size limits

### 6. Conflicting Tools Without Disambiguation
❌ Two similar tools with no guidance on which to use
✅ Clear "use X when... use Y when..." in descriptions

---

## Template for New Tools

```json
{
  "name": "[verb_noun format, e.g., search_customers, create_task]",
  "description": "[1. What it does—core function] [2. What it returns—format and fields] [3. Important format requirements or constraints] LIMITATION: [What it cannot do] WHEN TO USE: [Trigger conditions that should invoke this tool]",
  "input_schema": {
    "type": "object",
    "properties": {
      "[param_name]": {
        "type": "[type]",
        "description": "[What this parameter controls]. Format: [expected format with examples]. [Edge case handling or defaults]."
      }
    },
    "required": ["[required_params]"]
  }
}
```
