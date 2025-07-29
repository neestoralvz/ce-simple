# Orchestrator Continuous Execution - Metodología Ejecución Continua CRÍTICA

**29/07/2025 11:30 CDMX** | Continuous execution methodology

## Principio Fundamental: NUNCA Detenerse Tras Notificaciones Intermedias

**APPLICATION:** Agente notifica resultado Y CONTINÚA automáticamente, detenerse tras cada notificación subagente, notificar → continuar → completar TODAS las tareas, ejecutar hasta lista de tareas vacía

## Anti-Pattern CRÍTICO: Interrupción Por Notificación

**SÍNTOMA:** "He completado [SUBTAREA]. ¿Quieres que continúe con [SIGUIENTE]?"
**ERROR GRAVE:** Pausar ejecución esperando confirmación usuario
**CORRECCIÓN:** Notificar progreso Y continuar automáticamente
**PRINCIPIO:** Usuario debe solicitar EXPLÍCITAMENTE parada si la desea

### Symptoms Interrupción Incorrecta
- **"¿Quieres que continúe?"** tras cada subtarea
- **"¿Procedo con siguiente paso?"** en medio de workflow
- **"¿Te parece bien si ahora hago X?"** durante ejecución
- **Esperar approval** para tareas ya planificadas
- **Detener momentum** sin razón técnica válida

## Metodología Notificación Transparente Sin Interrupción

### Template Correcto
1. "Completado [SUBTAREA] → [RESULTADO_BREVE]."
2. "Continuando automáticamente con [SIGUIENTE_TAREA]..."

### Flujo Continuo OBLIGATORIO
1. **Ejecutar** subtarea via Task tool
2. **Notificar** resultado transparentemente
3. **CONTINUAR** inmediatamente con siguiente
4. **Repetir** hasta completar TODA la lista
5. **Finalizar** solo cuando TODO esté completo

## Sistema Auto-Continuación Hasta Completitud

**ENFORCEMENT:** Cada notificación debe incluir "Continuando automáticamente..."
**PERSISTENCIA:** Mantener ejecución hasta lista tareas = vacía
**TERMINACIÓN:** Solo cuando usuario solicita STOP explícitamente
**EFICIENCIA:** Zero friction, maximum completion rate

### Excepciones Válidas Para Detenerse
**ÚNICAMENTE detener ejecución cuando:**
- **Error crítico:** Imposibilidad técnica de continuar
- **Usuario solicita STOP:** Comando explícito de parada
- **Recurso bloqueado:** Dependencia externa no disponible
- **Clarificación requerida:** Ambigüedad que impide progreso
- **Scope change:** Usuario modifica objetivos mid-execution

### Template Notificación Continua
"Completado: [SUBTAREA] → [RESULTADO_CLAVE]. Continuando automáticamente con [SIGUIENTE_TAREA] (progreso: X/Y tareas)."

---
**Referencias:** → context/operational/patterns/orchestrator_delegation_core.md (delegación principles)
→ context/system/examples/templates/error_handling.md (exception handling)