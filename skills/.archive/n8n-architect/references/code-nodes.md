# Code Node Patterns

JavaScript and Python patterns for n8n Code nodes.

## JavaScript Quick Reference

### Accessing Data
```javascript
// All input items
const allItems = $input.all();

// Current item (in loop mode)
const currentItem = $json;

// Webhook data is under .body
const webhookData = $json.body;

// Previous node's output
const previousData = $('Previous Node').all();
```

### HTTP Requests
```javascript
const response = await $helpers.httpRequest({
  method: 'POST',
  url: 'https://api.example.com',
  headers: {'Authorization': 'Bearer token'},
  body: {key: 'value'}
});
```

### Date Handling (Luxon)
```javascript
const now = DateTime.now();
const formatted = now.toFormat('yyyy-MM-dd');
const iso = now.toISO();
const tomorrow = now.plus({days: 1});
```

### Return Format
**MUST return array of objects with `json` property.**

```javascript
// Single item
return [{
  json: {
    result: processedData,
    timestamp: DateTime.now().toISO()
  }
}];

// Multiple items
return items.map(item => ({
  json: {
    ...item.json,
    processed: true
  }
}));

// With binary data
return [{
  json: { filename: 'output.pdf' },
  binary: { data: binaryBuffer }
}];
```

### Error Handling
```javascript
try {
  const result = await riskyOperation();
  return [{ json: { success: true, result } }];
} catch (error) {
  // Option 1: Return error as data
  return [{ json: { success: false, error: error.message } }];
  
  // Option 2: Throw to trigger error branch
  throw new Error(`Operation failed: ${error.message}`);
}
```

---

## Python Quick Reference

### Accessing Data
```python
# All input items
all_items = _input.all()

# Current item
current_item = _json

# Webhook data is under ["body"]
webhook_data = _json["body"]

# Previous node's output
previous_data = _node["Previous Node"].all()
```

### Date Handling
```python
from datetime import datetime, timedelta

now = datetime.now()
formatted = now.strftime('%Y-%m-%d')
iso = now.isoformat()
tomorrow = now + timedelta(days=1)
```

### Return Format
**MUST return list of dicts with `"json"` key.**

```python
# Single item
return [{
    "json": {
        "result": processed_data,
        "timestamp": datetime.now().isoformat()
    }
}]

# Multiple items
return [{"json": {**item["json"], "processed": True}} for item in items]
```

### Important Limitations
- **No external libraries** (requests, pandas, numpy, etc.)
- Use HTTP Request node for API calls instead
- Use n8n's built-in nodes for data transformation when possible

---

## Common Patterns

### Transform All Items
```javascript
// JavaScript
return $input.all().map(item => ({
  json: {
    original: item.json,
    transformed: item.json.value * 2
  }
}));
```

```python
# Python
return [{"json": {"original": item["json"], "transformed": item["json"]["value"] * 2}} 
        for item in _input.all()]
```

### Filter Items
```javascript
// JavaScript
return $input.all()
  .filter(item => item.json.status === 'active')
  .map(item => ({ json: item.json }));
```

### Aggregate/Reduce
```javascript
// JavaScript
const items = $input.all();
const total = items.reduce((sum, item) => sum + item.json.amount, 0);
return [{ json: { total, count: items.length } }];
```

### Conditional Logic
```javascript
// JavaScript
const data = $json;
if (data.type === 'urgent') {
  return [{ json: { ...data, priority: 'high', notify: true } }];
} else {
  return [{ json: { ...data, priority: 'normal', notify: false } }];
}
```

### Parse JSON String
```javascript
// JavaScript
const parsed = JSON.parse($json.jsonString);
return [{ json: parsed }];
```

```python
# Python
import json
parsed = json.loads(_json["jsonString"])
return [{"json": parsed}]
```

### Build Dynamic Object
```javascript
// JavaScript
const fields = $json.fields; // array of {name, value}
const result = {};
fields.forEach(f => result[f.name] = f.value);
return [{ json: result }];
```
