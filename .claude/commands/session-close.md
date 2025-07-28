---
contextflow:
  purpose: "Cierre inteligente de sesión con captura narrative y handoff generation"
  triggers: ["final sesión", "cambio contexto", "handoff requerido"]
  workflow-final: true
  factorized: true
  research-driven: false
  auxiliary-commands:
    - session-close-analysis
    - session-close-direct
    - session-close-subagent
    - session-close-git
  communication-rules:
    - "NUNCA bash file generation directo"
    - "Mode detection via auxiliar commands"
    - "Modular execution maintaining functionality"
---

# Comando `/session-close` - Modular Orchestrator

## Propósito Core
Cerrar sesión conversacional mediante modular factorization manteniendo funcionalidad completa.

## Execution Mode Detection & Routing

**UTILITY-BASED DETECTION**:
```python
# Import execution mode detection utility
mode = execution_mode_detector.detect_execution_context(conversation_context)
routing = execution_mode_detector.get_execution_routing(mode)

EXECUTE: routing.command
```


## Utilities & Auxiliary Commands

### Core Utilities
- [@execution-mode-detector.md] - Universal dual-mode detection logic
- [@session-orchestrator.md] - Handoff generation & file management patterns

### Auxiliary Commands  
- [@session-close-analysis.md] - Universal conversation analysis
- [@session-close-direct.md] - Orchestrator direct execution
- [@session-close-subagent.md] - Standard user subagent deployment  
- [@session-close-git.md] - Universal git commit workflow

## Execution Flow
```python
# Step 1: Universal Analysis with Mode Detection
analysis = EXECUTE("/session-close-analysis")
mode = execution_mode_detector.detect_execution_context(analysis.conversation_context)
routing = execution_mode_detector.get_execution_routing(mode)

# Step 2: Mode-Optimized Execution
results = EXECUTE(routing.command, analysis)

# Step 3: Universal Git Commit
EXECUTE("/session-close-git", results)
```

## Usage
```bash
/session-close --tema "nombre-tema"
/session-close --categoria "tecnico|personal|planning"
/session-close  # Auto-detection for orchestrator context
```

## Factorization Benefits
- **Token Economy**: Main ~70 lines, utilities ~40-60 lines, auxiliaries ~80-150 lines
- **Template Integration**: Hardcoded prompts replaced with template references
- **Utility Reusability**: Core utilities available for other commands
- **Functionality Preserved**: Identical dual-mode execution via modular architecture
- **Maintenance Efficiency**: Centralized logic in utilities vs distributed across commands

---
**Ready for**: Immediate usage with identical functionality via modular execution