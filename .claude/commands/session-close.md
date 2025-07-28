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

**MODULAR DETECTION LOGIC**:
```python
if context.contains(["ORCHESTRATOR_HUB", "orchestrator-hub-coordinator", "orquestador de orquestadores"]):
    EXECUTE: /session-close-direct
else:
    EXECUTE: /session-close-subagent
```


## Auxiliary Commands
- [@session-close-analysis.md] - Universal conversation analysis
- [@session-close-direct.md] - Orchestrator direct execution
- [@session-close-subagent.md] - Standard user subagent deployment  
- [@session-close-git.md] - Universal git commit workflow

## Execution Flow
```python
# Step 1: Universal Analysis
analysis = EXECUTE("/session-close-analysis")

# Step 2: Mode-Specific Execution
if analysis.orchestrator_context:
    results = EXECUTE("/session-close-direct", analysis)
else:
    results = EXECUTE("/session-close-subagent", analysis)

# Step 3: Git Commit
EXECUTE("/session-close-git", results)
```

## Usage
```bash
/session-close --tema "nombre-tema"
/session-close --categoria "tecnico|personal|planning"
/session-close  # Auto-detection for orchestrator context
```

## Factorization Benefits
- Token Economy: Main <80 lines, auxiliaries ~50-80 lines
- Functionality preserved via modular execution
- Self-contained ecosystem per user vision
- Command interoperability maintained

---
**Ready for**: Immediate usage with identical functionality via modular execution