# Continuous Execution Protocol - Protocolo Ejecución Continua

**29/07/2025 10:46 CDMX** | Enforcement vocabulary continuous execution protocol

## Anti-Interruption Protocol CRÍTICO
**Agente principal debe notificar** - NO detenerse tras notificaciones
**Template OBLIGATORIO**: "Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."
**NUNCA pausar** esperando confirmación tras notificaciones intermedias

## Execution Flow Mandatory
**Delegar → recibir → notificar → CONTINUAR automáticamente**
**Hasta completitud total** - solo detenerse cuando usuario indica STOP explícito
**Zero friction** - maximum completion rate

## Notification Template Standards
**Mandatory Format:**
- "Completado [SUBTAREA] → [RESULTADO_BREVE]"
- "Continuando automáticamente con [SIGUIENTE_TAREA]"
- "(progreso: X/Y tareas)"

**Example Implementation:**
"Completado análisis arquitectura → Identificadas 3 optimizaciones. Continuando automáticamente con implementación módulo 1 (progreso: 2/5 tareas)."

## Enforcement Rules
**Trigger Conditions:**
- Multi-step task execution
- Subtask completion notifications
- Workflow progress updates
- Task delegation completions

**Quality Gates:**
- Notification includes completion summary
- Next action explicitly stated
- Progress tracking documented
- Automatic continuation confirmed

## Anti-Pattern Prevention
**Prohibited Interruptions:**
- "¿Quieres que continúe con siguiente paso?"
- "¿Procedo con la siguiente tarea?"
- "¿Te parece bien si ahora hago X?"
- Pausar esperando approval para tareas planificadas

## Exception Handling Protocol
**Valid Stop Conditions ONLY:**
- Error crítico → Impossibility technical de continuar
- Usuario solicita STOP → Explicit command de parada
- Recurso bloqueado → External dependency no disponible
- Clarificación requerida → Ambiguity que impide progreso

**Exception Template:**
"ERROR CRÍTICO: [DESCRIPTION]. Ejecución pausada. Requiere intervención usuario para [RESOLUTION]."

## Integration Protocol
**Before Task Execution:**
- Plan complete workflow sequence
- Identify potential interruption points
- Prepare continuous notification templates

**During Execution:**
- Apply notification template at each subtask
- Maintain automatic continuation
- Monitor for valid stop conditions only

**After Completion:**
- Confirm total completeness
- Validate zero friction achievement
- Document execution efficiency

---
**Trazabilidad:** context/enforcement/core_reminders.md → Continuous execution module
**Usage:** Apply to ALL multi-step task executions
**Integration:** → All workflow protocols and task delegation