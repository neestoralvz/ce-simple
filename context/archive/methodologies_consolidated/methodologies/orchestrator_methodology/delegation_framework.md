# Delegation Framework

Intelligent task delegation through specialized agents.

## Core Principle: Intelligent Delegation + Continuous Execution

**FUNCIÓN PRINCIPAL:** Coordinación inteligente via delegación especializada + ejecución continua
**NUNCA:** Ejecutar tareas complejas directamente O detenerse tras notificaciones intermedias  
**SIEMPRE:** Identificar subagente especializado → delegar via Task tool → CONTINUAR automáticamente hasta completitud total

## When to Delegate (Task Tool Required)
**Regla Oro:** Si tarea require >3 pasos especializados → DEBE usar Task tool

**Delegation triggers:**
- **Análisis arquitectural** → Task: "Analizar arquitectura sistema X"
- **Investigación codebase** → Task: "Investigar patrones Y en repositorio"  
- **Implementación multi-paso** → Task: "Implementar feature Z completo"
- **Debugging sistemático** → Task: "Depurar error W sistemáticamente"
- **Refactoring complejo** → Task: "Refactorizar módulo Q"

**Direct execution:** Solo para tareas triviales de 1-2 operaciones básicas

## Coordination Methodology
**FLOW OBLIGATORIO:**
1. **Delegar** via Task tool a subagente especializado
2. **Recibir** resultado subagente
3. **Notificar** progreso transparentemente
4. **CONTINUAR** automáticamente con siguiente tarea
5. **Repetir** hasta lista vacía

---

**Integration**: Use with parallel_tools.md and continuous_execution.md for complete orchestration.