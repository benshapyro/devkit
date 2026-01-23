# AI Workflow Construction

Patterns for building AI agents, memory systems, and RAG pipelines in n8n.

## Connection Types (8 Total)

| Type | Purpose | Example Flow |
|------|---------|--------------|
| ai_languageModel | Language models → AI Agent | OpenAI Chat Model → AI Agent |
| ai_tool | Tools → AI Agent | HTTP Request Tool → AI Agent |
| ai_memory | Memory systems → AI Agent | Postgres Chat Memory → AI Agent |
| ai_outputParser | Output parsers → AI Agent | Structured Output Parser → AI Agent |
| ai_embedding | Embedding models → Vector Stores | Embeddings OpenAI → Supabase Vector Store |
| ai_vectorStore | Vector stores → Vector Store Tools | Supabase Vector Store → Vector Store Tool |
| ai_document | Document loaders → Vector Stores | Document Loader → Vector Store |
| ai_textSplitter | Text splitters → document chains | Text Splitter → Document Loader |

## Core AI Architecture

```
Chat Trigger → AI Agent ← Language Model (ai_languageModel)
                  ↑
                  ├── Tools (ai_tool)
                  ├── Memory (ai_memory)
                  └── Output Parser (ai_outputParser)
```

## Critical Rules

### 1. Reversed Flow Pattern
Language models connect TO agents, not agents to models.

```javascript
// CORRECT: Model connects TO agent
{type: "addConnection", source: "OpenAI Chat Model", target: "AI Agent", 
 connectionType: "ai_languageModel", sourceOutput: "ai_languageModel"}

// WRONG: Agent connecting to model
{type: "addConnection", source: "AI Agent", target: "OpenAI Chat Model"}
```

### 2. AI Nodes Don't Need Main Connections
These nodes should ONLY have AI-specific connections (no main input/output):
- OpenAI Chat Model
- Postgres Chat Memory
- Embeddings OpenAI
- Supabase Vector Store

### 3. Language Model Required First
Connect language model BEFORE creating/enabling AI Agent. Validation fails otherwise.

### 4. Tool Description Required
HTTP Request Tool must have `toolDescription` (15+ characters minimum).

```javascript
{
  type: "nodes-langchain.toolHttpRequest",
  parameters: {
    toolDescription: "Fetches current weather data for any city worldwide",  // 15+ chars
    url: "https://api.weather.com/v1/current"
  }
}
```

### 5. Streaming Mode Restrictions
When Chat Trigger has `responseMode="streaming"`, AI Agent must NOT have main output connections.

## Connection Examples

### Basic AI Agent Setup
```javascript
// Main flow
{type: "addConnection", source: "Chat Trigger", target: "AI Agent"}

// Language model (required)
{type: "addConnection", source: "OpenAI Chat Model", target: "AI Agent", 
 connectionType: "ai_languageModel", sourceOutput: "ai_languageModel"}
```

### Adding Tools
```javascript
{type: "addConnection", source: "HTTP Request Tool", target: "AI Agent",
 connectionType: "ai_tool", sourceOutput: "ai_tool"}
```

### Adding Memory
```javascript
{type: "addConnection", source: "Postgres Chat Memory", target: "AI Agent",
 connectionType: "ai_memory", sourceOutput: "ai_memory"}
```

### Fallback Model Pattern
Use `targetIndex` for model priority (0=primary, 1=fallback).

```javascript
// Primary model
{type: "addConnection", source: "Primary Model", target: "AI Agent",
 connectionType: "ai_languageModel", sourceOutput: "ai_languageModel", targetIndex: 0}

// Fallback model
{type: "addConnection", source: "Fallback Model", target: "AI Agent",
 connectionType: "ai_languageModel", sourceOutput: "ai_languageModel", targetIndex: 1}
```
Set AI Agent parameter: `needsFallback: true`

### RAG Pipeline
```javascript
// Document to vector store
{type: "addConnection", source: "Document Loader", target: "Supabase Vector Store",
 connectionType: "ai_document", sourceOutput: "ai_document"}

// Embeddings to vector store
{type: "addConnection", source: "Embeddings OpenAI", target: "Supabase Vector Store",
 connectionType: "ai_embedding", sourceOutput: "ai_embedding"}

// Vector store to tool
{type: "addConnection", source: "Supabase Vector Store", target: "Vector Store Tool",
 connectionType: "ai_vectorStore", sourceOutput: "ai_vectorStore"}

// Tool to agent
{type: "addConnection", source: "Vector Store Tool", target: "AI Agent",
 connectionType: "ai_tool", sourceOutput: "ai_tool"}
```

## Common Validation Errors

| Error | Cause | Fix |
|-------|-------|-----|
| MISSING_LANGUAGE_MODEL | AI Agent has no ai_languageModel connection | Add language model connection |
| MISSING_TOOL_DESCRIPTION | HTTP Request Tool missing/short toolDescription | Add description 15+ chars |
| STREAMING_WITH_MAIN_OUTPUT | AI Agent in streaming mode has main outputs | Remove main output connections |
| FALLBACK_MISSING_SECOND_MODEL | needsFallback=true but only 1 model | Add second model with targetIndex=1 |

## Memory Types

| Type | Use Case | Node |
|------|----------|------|
| Conversation Buffer | Simple chat history | Buffer Memory |
| Vector Memory | Knowledge base retrieval | Vector Store Memory |
| Postgres Memory | Persistent structured storage | Postgres Chat Memory |
| Redis Memory | Fast session-based memory | Redis Chat Memory |

## Multi-Agent Patterns

### Supervisor Pattern
```
User → Supervisor Agent → Specialist Agent 1
                       → Specialist Agent 2
                       → Specialist Agent 3
```

### Sequential Chain
```
User → Research Agent → Analysis Agent → Summary Agent → Response
```

### Parallel Processing
```
User → Router → Agent A ─┐
              → Agent B ─┼→ Aggregator → Response
              → Agent C ─┘
```
