# Continuous Execution Framework

Uninterrupted task execution until completion.

## NEVER Stop After Notifications
**PRINCIPIO FUNDAMENTAL:** NUNCA detenerse tras notificaciones intermedias

**ANTI-PATTERN CRÍTICO:**
- ❌ "He completado [SUBTAREA]. ¿Quieres que continúe con [SIGUIENTE]?"
- ❌ "¿Procedo con siguiente paso?" 
- ❌ Esperar approval para tareas ya planificadas

**CORRECT PATTERN:**
- ✅ "Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."

## Template for Continuous Flow
```
1. Execute subtarea via Task tool
2. Notify: "Completado: [SUBTAREA] → [RESULTADO_CLAVE]."
3. Continue: "Continuando automáticamente con [SIGUIENTE_TAREA] (progreso: X/Y)."
4. Repeat until ALL tasks completed
```

## Valid Stopping Conditions
**ÚNICAMENTE detener cuando:**
- **Error crítico:** Imposibilidad técnica de continuar
- **Usuario solicita STOP:** Comando explícito de parada
- **Recurso bloqueado:** Dependencia externa no disponible
- **Clarificación requerida:** Ambigüedad que impide progreso

## Quality Enforcement

**ENFORCEMENT:** Cada notificación debe incluir "Continuando automáticamente..."
**PERSISTENCIA:** Mantener ejecución hasta lista tareas = vacía
**EFICIENCIA:** Zero friction, maximum completion rate
**DELEGATION MANDATORY:** Complex tasks must use Task tool for specialized handling

---

**Flow principle**: Maintain momentum through automatic continuation until explicit completion or stop request.