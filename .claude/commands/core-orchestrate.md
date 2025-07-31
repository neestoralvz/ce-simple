# /core-orchestrate - Complex Orchestration & Multi-Component Tasks

**FUNCIÓN**: L4-Pure Orchestration + hybrid protocol + subagent coordination

## PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE

**NIVEL ORQUESTADOR** (Claude Principal):
- **TodoWrite Management**: DESPLIEGA TodoWrite OBLIGATORIO en execution mode
- **Subagent Deployment**: Especializado para explorar codebase ANTES de acciones críticas
- **Parallel Coordination**: Búsqueda paralela via múltiples Task tools CUANDO complejidad justifica
- **Analysis Delegation**: Think x4 de información a subagente analítico PARA decisiones complejas
- **Multi-Subagent Planning**: Coordinación con múltiples subagentes especializados SEGÚN necesidad

**NIVEL EJECUTOR** (Subagentes):
- **Direct Execution**: Subtareas específicas dentro de scope delegado
- **Tool Usage**: Read/Edit/Bash/Grep/Glob según necesario para completar objetivos
- **Validation**: Criterios específicos establecidos antes de reportar completado

**COORDINATION PROTOCOL**:
```bash
# Parallel execution management (MÁXIMO 3 subagentes simultáneos)
if subagent_count > 3; then
    queue_management=true
    resource_optimization=active
fi

# Resource management escalation
if pending_actions > 10; then
    add_specialized_subagents()
fi
```

**SYSTEMATIC CONTINUATION**:
- ✅ Coordinación ejecución paralela con resource management
- ✅ Orquestación validación SIEMPRE OBLIGATORIO
- ✅ Iteración hasta éxito total - NUNCA abandones tarea incompleta
- ✅ Delegación actualización archivos SIEMPRE
- ✅ Extracción insights conversacionales via subagente
- ✅ Integración version control coordination

**FALLBACK**: Execution directa con TodoWrite + basic coordination si orchestration falla
**INTEGRATION**: Coordinates with /core-validate for quality gates + /core-finalize for completion