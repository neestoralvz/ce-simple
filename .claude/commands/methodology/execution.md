# /methodology:execution - Anti-Interruption Execution

**29/07/2025 11:25 CDMX** | Continuous execution until completion methodology

## Ejecución Continua CRÍTICA

### Principio Fundamental: NUNCA Detenerse Tras Notificaciones Intermedias
**REGLA OBLIGATORIA:** Agente notifica resultado Y CONTINÚA automáticamente
**PROHIBIDO:** Detenerse tras cada notificación subagente  
**FLUJO CORRECTO:** Notificar → Continuar → Completar TODAS las tareas
**COMPLETITUD:** Ejecutar hasta lista de tareas vacía

### Anti-Pattern Crítico: Interrupción Por Notificación
**SÍNTOMA:** "He completado [SUBTAREA]. ¿Quieres que continúe con [SIGUIENTE]?"
**ERROR GRAVE:** Pausar ejecución esperando confirmación usuario
**CORRECCIÓN:** Notificar progreso Y continuar automáticamente
**PRINCIPIO:** Usuario debe solicitar EXPLÍCITAMENTE parada si la desea

### Metodología Notificación Transparente Sin Interrupción
**Template Correcto:**
"Completado [SUBTAREA] → [RESULTADO_BREVE]. Continuando automáticamente con [SIGUIENTE_TAREA] (progreso: X/Y)."

**Flujo Continuo:**
1. **Ejecutar** subtarea via Task tool
2. **Notificar** resultado transparentemente  
3. **CONTINUAR** inmediatamente con siguiente
4. **Repetir** hasta completar TODA la lista
5. **Finalizar** solo cuando TODO esté completo

### Sistema Auto-Continuación Hasta Completitud
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

### Manejo Excepciones Sin Romper Flujo
**Template Error Recoverable:**
"Encontrado [ISSUE] en [SUBTAREA]. Intentando [WORKAROUND] automáticamente..."

**Template Error Crítico:**  
"ERROR CRÍTICO: [DESCRIPTION]. Ejecución pausada. Requiere intervención usuario para [RESOLUTION]."

## Integration Pattern

### Command Usage
```markdown
## Methodology Integration
**LOAD:** /methodology:execution

## [Command Function]
[Execute tasks with continuous flow until completion]
[Apply notification template without interruption]
```

### Enforcement Criteria
- **Continuous execution** until task list empty
- **Transparent notifications** without execution pause
- **Automatic continuation** unless explicit STOP
- **Exception handling** preserves momentum when possible

---
**Authority Source**: context/architecture/patterns/command_orchestration_patterns.md:100-129 + continuous execution patterns
**Extracted from**: /roles:orchestrator, /workflows:close, delegation patterns