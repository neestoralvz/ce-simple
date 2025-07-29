# Orchestrator Methodology - Reference Index

**Pure Reference-Only** | Navegación modular metodología orquestador

## Core Methodology References

### Delegation & Task Tool Protocol
→ **context/operational/patterns/orchestrator_delegation_core.md:5-15** (definición orquestador)
→ **context/operational/patterns/orchestrator_delegation_core.md:17-30** (Task tool methodology) 
→ **context/operational/patterns/orchestrator_delegation_core.md:32-47** (subagente identification)
→ **context/operational/patterns/orchestrator_delegation_core.md:49-64** (anti-patterns delegación)

### Parallel Tools & Concurrency
→ **context/operational/patterns/orchestrator_parallel_tools.md:5-8** (simultaneidad principle)
→ **context/operational/patterns/orchestrator_parallel_tools.md:12-18** (oportunidades paralelas)
→ **context/operational/patterns/orchestrator_parallel_tools.md:20-25** (tools simultáneos)
→ **context/operational/patterns/orchestrator_parallel_tools.md:29-36** (anti-patterns secuencial)

### Continuous Execution CRÍTICO
→ **context/operational/patterns/orchestrator_continuous_execution.md:5-9** (principio fundamental)
→ **context/operational/patterns/orchestrator_continuous_execution.md:11-20** (anti-pattern interrupción)
→ **context/operational/patterns/orchestrator_continuous_execution.md:22-32** (notificación transparente)
→ **context/operational/patterns/orchestrator_continuous_execution.md:34-45** (auto-continuación)

### Multi-Agent Coordination
→ **context/operational/patterns/orchestrator_coordination.md:5-9** (ultra-orchestration)
→ **context/operational/patterns/orchestrator_coordination.md:13-18** (notificación estructura)
→ **context/operational/patterns/orchestrator_coordination.md:22-34** (cambios methodology)
→ **context/operational/patterns/orchestrator_coordination.md:36-47** (validación sistema)

## Quick Access Patterns

### Task Delegation Triggers
- **>3 pasos especializados** → DEBE usar Task tool
- **Análisis arquitectural/investigación** → Task delegation obligatorio
- **Multi-archivo operations** → Subagente specialization
- **Complex debugging/refactoring** → Task tool required

### Parallel Tools Triggers  
- **Independent file operations** → Batch execution obligatorio
- **Research + Analysis** → Simultaneous tools required
- **Status validation** → Combined diagnostics
- **Multi-domain investigation** → Parallel search patterns

### Continuous Execution Enforcement
- **Notification template**: "Completado [X] → [RESULTADO]. Continuando automáticamente..."
- **PROHIBIDO**: "¿Quieres que continúe?" tras subtareas
- **OBLIGATORIO**: Ejecutar hasta lista de tareas vacía
- **Interruption exceptions**: Error crítico, STOP explícito, clarification required

### Multi-Agent Coordination
- **Múltiples Task tools simultáneas** cuando dominios independientes
- **Usuario como ultra-orchestrator** de N agentes paralelos
- **Background processes + git worktrees** para isolation
- **Inter-conversation tickets** para coordination

## Critical Success Indicators
- **Zero interrupciones** durante multi-task execution
- **Batch operations** para tools independientes
- **Continuous notification** sin pausar workflow
- **Task completion hasta lista vacía** automático
- **Ultra-orchestrator coordination** effective

---
**Complete Methodology**: Load all 4 reference modules para comprehensive understanding
**Examples**: → context/system/examples/orchestrator_concurrent_patterns.md
**Templates**: → context/system/examples/templates/ error handling + workflows