#!/bin/bash

# Skill Auto-Activation Hook
# Triggers skill suggestions based on user prompts and file context

TMP_INPUT="/tmp/claude_hook_input_$$"

# Read stdin safely. Prefer timeout when available; fall back to plain cat.
if command -v timeout >/dev/null 2>&1; then
    timeout 5 cat > "$TMP_INPUT" 2>/dev/null || exit 0
elif command -v gtimeout >/dev/null 2>&1; then
    gtimeout 5 cat > "$TMP_INPUT" 2>/dev/null || exit 0
else
    cat > "$TMP_INPUT" 2>/dev/null || exit 0
fi

INPUT=$(cat "$TMP_INPUT")
rm -f "$TMP_INPUT" 2>/dev/null

# Get the project directory (defaults to current directory)
CLAUDE_PROJECT_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}"

# Path to skill rules configuration (project override if present)
SKILL_RULES_USER="$HOME/.claude/skill-rules.json"
SKILL_RULES_PROJECT="$CLAUDE_PROJECT_DIR/.claude/skill-rules.json"
if [ -f "$SKILL_RULES_PROJECT" ]; then
    SKILL_RULES="$SKILL_RULES_PROJECT"
else
    SKILL_RULES="$SKILL_RULES_USER"
fi

# Check if skill-rules.json exists
if [ ! -f "$SKILL_RULES" ]; then
    exit 0
fi

# Extract user prompt from the input
USER_PROMPT=$(echo "$INPUT" | jq -r '.prompt // ""')

# If no prompt, exit
if [ -z "$USER_PROMPT" ] || [ "$USER_PROMPT" = "null" ]; then
    exit 0
fi

# Convert prompt to lowercase for matching
USER_PROMPT_LOWER=$(echo "$USER_PROMPT" | tr '[:upper:]' '[:lower:]')

# Match prompt against configured keyword patterns
MATCHED_SKILLS=$(jq -r --arg prompt "$USER_PROMPT_LOWER" '
  .skills | to_entries[] |
  select(
    (.value.promptTriggers.keywords // [] |
     any(. as $keyword | $prompt | contains($keyword | ascii_downcase)))
  ) |
  "\(.key):\(.value.priority // "medium")"
' "$SKILL_RULES" 2>/dev/null)

# Also match against intent patterns (regex)
INTENT_MATCHED=$(jq -r --arg prompt "$USER_PROMPT_LOWER" '
  .skills | to_entries[] |
  select(
    (.value.promptTriggers.intentPatterns // [] |
     any(. as $pattern | $prompt | test($pattern; "i")))
  ) |
  "\(.key):\(.value.priority // "medium")"
' "$SKILL_RULES" 2>/dev/null)

# Combine matches and sort by priority (high first), then deduplicate by skill name
# Format is "skillname:priority" - sort by priority field, keep first occurrence of each skill
ALL_MATCHED=$(echo -e "$MATCHED_SKILLS\n$INTENT_MATCHED" | grep -v '^$' | \
    awk -F: '{
        priority_order = ($2 == "high" ? 1 : ($2 == "medium" ? 2 : 3));
        print priority_order ":" $0
    }' | sort -t: -k1,1n | cut -d: -f2- | \
    awk -F: '!seen[$1]++')

# Match agents (subagents) too, using the same trigger structure
MATCHED_AGENTS=$(jq -r --arg prompt "$USER_PROMPT_LOWER" '
  .agents // {} | to_entries[] |
  select(
    (.value.promptTriggers.keywords // [] |
     any(. as $keyword | $prompt | contains($keyword | ascii_downcase)))
  ) |
  "\(.key):\(.value.priority // "medium")"
' "$SKILL_RULES" 2>/dev/null)

INTENT_MATCHED_AGENTS=$(jq -r --arg prompt "$USER_PROMPT_LOWER" '
  .agents // {} | to_entries[] |
  select(
    (.value.promptTriggers.intentPatterns // [] |
     any(. as $pattern | $prompt | test($pattern; "i")))
  ) |
  "\(.key):\(.value.priority // "medium")"
' "$SKILL_RULES" 2>/dev/null)

ALL_MATCHED_AGENTS=$(echo -e "$MATCHED_AGENTS\n$INTENT_MATCHED_AGENTS" | grep -v '^$' | \
    awk -F: '{
        priority_order = ($2 == "high" ? 1 : ($2 == "medium" ? 2 : 3));
        print priority_order ":" $0
    }' | sort -t: -k1,1n | cut -d: -f2- | \
    awk -F: '!seen[$1]++')

HAS_SKILLS=0
HAS_AGENTS=0
if [ -n "$ALL_MATCHED" ]; then
    HAS_SKILLS=1
    SKILL_NAMES=$(echo "$ALL_MATCHED" | cut -d':' -f1 | tr '\n' ', ' | sed 's/,$//')
fi

if [ -n "$ALL_MATCHED_AGENTS" ]; then
    HAS_AGENTS=1
    AGENT_NAMES=$(echo "$ALL_MATCHED_AGENTS" | cut -d':' -f1 | tr '\n' ', ' | sed 's/,$//')
fi

if [ $HAS_SKILLS -eq 1 ] || [ $HAS_AGENTS -eq 1 ]; then
    MSG=""
    if [ $HAS_SKILLS -eq 1 ]; then
        MSG="Relevant skills detected for this task: $SKILL_NAMES. Consider using the Skill tool to load these for best practices and patterns."
    fi
    if [ $HAS_AGENTS -eq 1 ]; then
        if [ -n "$MSG" ]; then
            MSG="$MSG "
        fi
        MSG="$MSG Relevant agents detected for this task: $AGENT_NAMES. Consider using the Task tool with the matching subagent."
    fi

    cat << EOF
{
  "additionalContext": "$MSG"
}
EOF
fi

exit 0
