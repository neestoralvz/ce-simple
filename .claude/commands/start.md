---
contextflow:
  purpose: "Session starter universal con auto-loading de handoffs"
  triggers: ["inicio de sesión", "continuidad entre sesiones", "contexto perdido"]
  next: ["analyze", "implement", "explore", "refactor", "extract-insights", "process-layer"]
  communication-rules:
    - "NUNCA bash echo para comunicar con usuario"
    - "SIEMPRE Task tools → Main agent → Usuario"
    - "Parallel Task tools obligatorio en mismo mensaje"
    - "Subagents NUNCA comunican directamente"
  decision-tree:
    use-when: 
      - "Primera interacción de la sesión"
      - "Usuario necesita orientación sobre qué hacer"
      - "Continuidad desde sesión anterior requerida"
    alternatives: ["meta-narrative", "explore"]
    load-context: ["handoff más reciente", "commands ecosystem"]
  research-driven: false
    semantic-triggers:
      - "empezar" / "iniciar" / "comenzar"
      - "qué sigue" / "continuar" / "seguir"
      - "contexto" / "dónde estaba" / "estado actual"
---

# Comando Universal `/start`

## Core Execution Flow

### 1. Git Status Check (Obligatorio)
```bash
git status && git pull origin master && git log --oneline -5
```

### 2. Context Loading (Condicional)
**SI context perdido O primera sesión → Deploy handoff specialist**:
```
Task: "Auto-load handoff + git analysis"
Prompt: "Load latest handoff from /handoff/, analyze git changes, identify discrepancies"
```

## Análisis de Contexto (Condicional)

**INSTRUCCIÓN**: Solo ejecutar specialists SI se detecta:
- Handoff desactualizado (>48h)
- System drift indicators  
- Uncommitted changes críticos
- Usuario explícitamente requiere analysis

**Specialists disponibles**:
1. **Research Specialist**: Project maintenance + pending items
2. **Architecture Validator**: System integrity + compliance  
3. **Content Optimizer**: Insights extraction + correlation
4. **Quality Assurance**: Evolution opportunities + roadmap

**Output esperado**: Priority-based options con context inteligente

## Decision Logic

**Context Assessment** → **Conditional Specialist Deployment** → **Options Generation**

### Casos de Uso
- **Fresh start**: Git check + basic options
- **Context loss**: Deploy handoff specialist
- **System maintenance**: Deploy full analysis suite
- **User direction**: Generate contextual options

### Success Criteria
- Context loading efficiency optimized
- Specialist deployment solo cuando necesario  
- User voice preserved como source of truth
- Options basadas en real project state