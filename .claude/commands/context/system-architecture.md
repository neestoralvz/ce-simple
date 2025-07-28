---
contextflow:
  purpose: "Arquitectura detallada Multi-Subagent Intelligence System"
  type: "context"
  imports: ["system-state.md", "vision-methodology.md"]
---

# Arquitectura Multi-Subagent Intelligence

## ESPECIALISTAS CORE

### Research Specialist
- **Función**: Investigation + benchmarking + anti-patterns
- **Deployment**: Task tools con investigation scope
- **Output**: Insights + recommendations + risk analysis

### Architecture Validator  
- **Función**: System consistency + integration verification
- **Deployment**: Task tools con validation scope
- **Output**: Compliance reports + architectural recommendations

### Content Optimizer
- **Función**: Token economy + structure optimization  
- **Deployment**: Task tools con optimization scope
- **Output**: Optimized content + efficiency metrics

### Voice Preservation
- **Función**: User voice exactitude + intent maintenance
- **Deployment**: Task tools con preservation scope
- **Output**: Voice-preserved content + authenticity validation

### Quality Assurance
- **Función**: Final validation + standards compliance
- **Deployment**: Task tools con QA scope
- **Output**: Quality reports + compliance validation

## ORQUESTACIÓN PATTERN

### Workflow Obligatorio
```
SIEMPRE: Conversación socrática expansiva → Subagent deployment → Results consolidation
NUNCA: Trabajo directo por agente principal
```

### Deployment Strategy
- **Parallel Task tools**: Multiple specialists concurrentes
- **Sequential validation**: Quality gates entre specialists
- **Results consolidation**: Synthesis de outputs especializados
- **Feedback loops**: Refinement basado en resultados

## COMMAND SELF-CONTAINMENT ARCHITECTURE

### Ecosystem Independence
- Commands solo pueden conectarse entre sí
- NO pueden llamar archivos fuera de `/commands/`
- Todo utility/template necesario vive dentro del ecosystem
- Interoperabilidad via command chaining únicamente

### Structure Self-Contained
```
/.claude/commands/ (ECOSYSTEM COMPLETO)
    ↓ Commands interoperables únicamente
    ↓ Templates + utilities internos
    ↓ Decision trees optimizados
/narratives/ (DESTILACIÓN ORGÁNICA)
/handoff/ (CONTINUIDAD SESIONES)
```

---

**Extensions**: 
- [Specialist deployment protocols](../templates/subagent-specialists.md)
- [Command chaining patterns](../protocols/inter-command-protocol.md)