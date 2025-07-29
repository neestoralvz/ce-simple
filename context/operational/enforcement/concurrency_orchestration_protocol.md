# Concurrency Orchestration Protocol - Protocolo Concurrencia Obligatorio

## Pre-Tool Execution Analysis OBLIGATORIO
**ANTES de ejecutar cualquier tool** → DEBE analizar oportunidades concurrency
**OBLIGATORIO preguntar**: ¿Pueden estos tools ejecutarse simultáneamente?
**BATCH operations** para tools independientes en single message
**ANTI-PATTERN**: Sequential execution cuando parallel posible

## Concurrency Opportunities Identification
**Independent file operations**: Diferentes archivos = parallel execution
**Read-only operations**: Grep + Read + LS = siempre paralelos
**Multiple searches**: Grep patterns diferentes = batch execution
**File + analysis**: Edit + analysis cuando no overlap = simultáneos

## Orchestration Protocol SIEMPRE

### Delegation Mandatory
**Si tarea require >3 pasos especializados** → DEBE usar Task tool
**NUNCA ejecutar** trabajo directo - SIEMPRE delegar via subagentes especializados
**Parallel tools** cuando información independiente (batch operations obligatorio)

### Recognition → Delegation → Validation Pattern
**Reconocer patrón** → Task tool con contexto específico → post-validation automática
**Second Task tool** para verification alignment después cada delegación
**Authority validation** con user-vision/TRUTH_SOURCE.md systematic

## TodoWrite Auto-Detection Protocol

### Dependency Scanning Automatic
**Cada task completion** → auto-generar tareas actualización archivos relacionados
**OBLIGATORIO identificar** automáticamente archivos requieren sincronización  
**Análisis concurrencia** automático para maximize throughput

### Dynamic Methodology Integration
**Auto-add** tareas discovered during execution
**Dependency-scanning** para file propagation requirements
**Concurrency analysis** para parallel execution opportunities

## Enforcement Rules
**Trigger Conditions:**
- Multiple tool operations required
- Independent information gathering needed
- Task complexity >3 specialized steps
- File operations on different files

**Quality Gates:**
- Concurrency analysis completed before execution
- Batch operations identified and implemented
- Task delegation applied for complex operations
- Authority validation integrated post-delegation

## Anti-Pattern Prevention
**Prohibited Sequential Patterns:**
- Execute Read → Read → Grep when can be parallel
- Single tool when batch operation possible
- Direct execution for >3 step tasks
- Skip dependency scanning after completions

## Implementation Protocol
**Before Tool Execution:**
- Analyze concurrency opportunities systematically
- Identify independent operations for batching
- Plan delegation for complex multi-step tasks

**During Execution:**
- Apply batch operations when identified
- Delegate complex tasks to specialized subagents
- Maintain orchestration coordination

**After Completion:**
- Auto-scan dependencies for follow-up tasks
- Generate related tasks automatically
- Validate authority alignment systematically

---
**Trazabilidad:** context/enforcement/core_reminders.md → Concurrency module factorization
**Usage:** Apply to ALL tool executions and task delegations
**Integration:** → All workflow protocols requiring parallel operations