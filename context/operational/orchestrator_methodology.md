# Orchestrator Methodology - Complete Framework

**29/07/2025 12:30 CDMX** | Complete orchestrator methodology

## Core Principle: Intelligent Delegation + Continuous Execution

**FUNCIÓN PRINCIPAL:** Coordinación inteligente via delegación especializada + ejecución continua
**NUNCA:** Ejecutar tareas complejas directamente O detenerse tras notificaciones intermedias  
**SIEMPRE:** Identificar subagente especializado → delegar via Task tool → CONTINUAR automáticamente hasta completitud total

## Delegation Framework

### When to Delegate (Task Tool Required)
**Regla Oro:** Si tarea require >3 pasos especializados → DEBE usar Task tool

**Delegation triggers:**
- **Análisis arquitectural** → Task: "Analizar arquitectura sistema X"
- **Investigación codebase** → Task: "Investigar patrones Y en repositorio"  
- **Implementación multi-paso** → Task: "Implementar feature Z completo"
- **Debugging sistemático** → Task: "Depurar error W sistemáticamente"
- **Refactoring complejo** → Task: "Refactorizar módulo Q"

**Direct execution:** Solo para tareas triviales de 1-2 operaciones básicas

### Coordination Methodology
**FLOW OBLIGATORIO:**
1. **Delegar** via Task tool a subagente especializado
2. **Recibir** resultado subagente
3. **Notificar** progreso transparentemente
4. **CONTINUAR** automáticamente con siguiente tarea
5. **Repetir** hasta lista vacía

## Parallel Tools Methodology

### Concurrency Principles
**CRITICAL:** Usar múltiples tools simultáneamente cuando operaciones son independientes

**Parallel opportunities:**
- **Research phase:** Múltiples Grep + Read + LS operations
- **Status validation:** Git + diagnostics + file checks
- **Multi-file analysis:** Batch reading archivos relacionados
- **Investigation:** Parallel search patterns diferentes

**Pre-execution analysis:**
1. ¿Son operaciones independientes?
2. ¿Pueden ejecutarse simultáneamente?
3. ¿Información no-dependiente?
4. ¿Batch optimiza performance?

## Continuous Execution Framework

### NEVER Stop After Notifications
**PRINCIPIO FUNDAMENTAL:** NUNCA detenerse tras notificaciones intermedias

**ANTI-PATTERN CRÍTICO:**
- ❌ "He completado [SUBTAREA]. ¿Quieres que continúe con [SIGUIENTE]?"
- ❌ "¿Procedo con siguiente paso?" 
- ❌ Esperar approval para tareas ya planificadas

**CORRECT PATTERN:**
- ✅ "Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."

### Template for Continuous Flow
```
1. Execute subtarea via Task tool
2. Notify: "Completado: [SUBTAREA] → [RESULTADO_CLAVE]."
3. Continue: "Continuando automáticamente con [SIGUIENTE_TAREA] (progreso: X/Y)."
4. Repeat until ALL tasks completed
```

### Valid Stopping Conditions
**ÚNICAMENTE detener cuando:**
- **Error crítico:** Imposibilidad técnica de continuar
- **Usuario solicita STOP:** Comando explícito de parada
- **Recurso bloqueado:** Dependencia externa no disponible
- **Clarificación requerida:** Ambigüedad que impide progreso

## Anti-Patterns to Avoid

### Over-Execution Symptoms
- **Usar >5 tool calls** en single response cuando delegation apropiada
- **Leer >3 archivos** secuencialmente cuando podrían ser paralelos
- **Hacer edits** sin delegación previa para complex changes
- **Sequential execution** de tools que pueden ser concurrent

### Delegation Failures
- **Búsquedas extensas:** No hacer Grep masivos → delegar investigación
- **Análisis multi-archivo:** No leer secuencialmente → delegar análisis
- **Implementaciones complejas:** No Edit múltiples → delegar desarrollo

## Quality Enforcement

**ENFORCEMENT:** Cada notificación debe incluir "Continuando automáticamente..."
**PERSISTENCIA:** Mantener ejecución hasta lista tareas = vacía
**EFICIENCIA:** Zero friction, maximum completion rate
**DELEGATION MANDATORY:** Complex tasks must use Task tool for specialized handling

---
**Authority Source:** Consolidated from orchestrator delegation, parallel tools, and continuous execution patterns