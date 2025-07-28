# Execution Mode Detector Utility

## Purpose
Universal detection logic for determining execution mode context (orchestrator vs standard user) across commands.

## Core Detection Functions

### 1. Context Detection Logic
```python
def detect_execution_context(conversation_context):
    """
    Detects execution mode based on conversation context markers.
    
    Returns:
        - "orchestrator_direct": For orchestrator hub context
        - "standard_subagent": For regular user context
    """
    orchestrator_markers = [
        "ORCHESTRATOR_HUB",
        "orchestrator-hub-coordinator", 
        "orquestador de orquestadores",
        "multi-subagent intelligence",
        "orchestrator context",
        "dispatcher mode"
    ]
    
    if any(marker in conversation_context for marker in orchestrator_markers):
        return "orchestrator_direct"
    else:
        return "standard_subagent"
```

### 2. Execution Mode Properties
```python
def get_execution_mode_properties(mode):
    """
    Returns execution properties for detected mode.
    """
    if mode == "orchestrator_direct":
        return {
            'task_tools_required': False,
            'direct_execution': True,
            'performance_optimized': True,
            'overhead_minimal': True,
            'context_preservation': 'integrated'
        }
    else:  # standard_subagent
        return {
            'task_tools_required': True,
            'direct_execution': False,
            'comprehensive_analysis': True,
            'specialist_deployment': True,
            'context_preservation': 'distributed'
        }
```

### 3. Mode-Specific Routing
```python
def get_execution_routing(mode):
    """
    Returns appropriate routing for detected execution mode.
    """
    routing_map = {
        'orchestrator_direct': {
            'command': 'session-close-direct',
            'workflow': 'integrated',
            'optimization': 'performance'
        },
        'standard_subagent': {
            'command': 'session-close-subagent', 
            'workflow': 'distributed',
            'optimization': 'comprehensive'
        }
    }
    
    return routing_map.get(mode, routing_map['standard_subagent'])
```

## Integration Pattern
```python
# Usage in commands:
mode = detect_execution_context(conversation_context)
properties = get_execution_mode_properties(mode)
routing = get_execution_routing(mode)

if mode == "orchestrator_direct":
    EXECUTE(routing.command, analysis_input)
else:
    EXECUTE(routing.command, analysis_input)
```

## Supported Commands
- session-close.md (primary user)
- Any future command requiring dual-mode execution
- Commands with orchestrator optimization needs

---
**Function**: Universal execution mode detection for optimal command routing