---
contextflow:
  purpose: "Universal conversation analysis for session closure preparation"
  parent-command: "session-close"
  auxiliary: true
  output-format: "structured-analysis"
  execution-mode: "internal"
  research-driven: false
---

# Auxiliary Command `/session-close-analysis`

## Purpose
Extract conversation metadata and context for session-close mode routing and processing.

## Core Analysis Functions

### 1. Conversation Metadata Extraction
```python
def extract_session_metadata():
    return {
        'conversation_content': capture_full_conversation(),
        'session_context': extract_session_context(),
        'timestamp_mx': generate_mexico_timestamp(),
        'participants': identify_conversation_participants(),
        'timeline': extract_conversation_timeline()
    }
```

### 2. Context Detection Logic
```python
def detect_execution_context():
    if context.contains(["ORCHESTRATOR_HUB", "orchestrator-hub-coordinator", "orquestador de orquestadores"]):
        return "orchestrator_direct"
    else:
        return "standard_subagent"
```

### 3. Theme & Category Analysis
```python
def analyze_conversation_themes(conversation_content):
    return {
        'primary_theme': identify_primary_topic(conversation_content),
        'secondary_themes': extract_secondary_topics(conversation_content),
        'category': classify_conversation_type(conversation_content),
        'decision_points': extract_key_decisions(conversation_content)
    }
```

### 4. Command Impact Scanning
```python
def scan_command_impacts(conversation_content):
    return {
        'commands_mentioned': scan_explicit_command_mentions(conversation_content),
        'implied_commands': detect_implied_command_needs(conversation_content),
        'modifications_required': identify_command_modifications(conversation_content),
        'new_command_specs': extract_new_command_requirements(conversation_content)
    }
```

## Output Structure
```json
{
  "execution_mode": "orchestrator_direct|standard_subagent",
  "metadata": {
    "conversation_content": "...",
    "timestamp_mx": "...",
    "session_context": "..."
  },
  "analysis": {
    "theme": "...",
    "category": "...",
    "decision_points": [...]
  },
  "command_impacts": {
    "commands_mentioned": [...],
    "modifications_required": [...],
    "new_command_specs": [...]
  },
  "routing_data": {
    "orchestrator_context": true|false,
    "complexity_level": "basic|intermediate|complex",
    "specialist_requirements": [...]
  }
}
```

## Integration Points
- **INPUT**: Full conversation context from session
- **OUTPUT**: Structured analysis for session-close-direct/subagent routing
- **NEXT**: Route to appropriate execution mode based on context detection

---
**Function**: Universal analysis preparation for modular session closure execution