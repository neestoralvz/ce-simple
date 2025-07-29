# Orchestrator Concurrent Patterns - Ejemplos Ejecución Paralela

**29/07/2025 09:20 CDMX | Actualizado: 29/07/2025 09:20 CDMX** | Ejemplos concretos ejecución herramientas concurrentes

## Ejemplos Ejecución Concurrente

### Pattern: Research Phase Parallel
1. ✅ CORRECTO - Parallel:
2. Read file1.md + Read file2.md + Grep pattern + Git status (simultáneo)
4. ❌ INCORRECTO - Sequential:
5. Read file1.md → analizar → Read file2.md → analizar → Git status

### Pattern: Metodología Coordinación
1. Recibir request usuario
2. Identificar: ¿Trivial (<3 pasos) o Complejo?
3. Si Trivial → BATCH tools paralelos cuando posible
4. Si Complejo → Task tool con context completo
5. Coordinar resultado con parallel assessment
6. Presentar opciones usuario organizadas
7. Coordinar siguiente acción con parallel assessment

### Pattern: Ejecución Paralela Multi-Task  
1. ✅ SIMULTANEO:
2. Task A (research) + Task B (analysis) + Task C (validation) → parallel execution
4. ❌ SECUENCIAL (anti-pattern):
5. Task A → wait → Task B → wait → Task C (ineficiente)

### Pattern: Secuencia Multi-Conversación
1. Assessment parallel opportunities
2. Launch concurrent Tasks/conversations 
3. Background monitoring + coordination
4. Cross-conversation integration
5. Unified results presentation

---

## Enlaces → Información Complementaria
**Si necesitas metodología:** → context/patterns/orchestrator_methodology.md:46-78
**Si requieres template:** → context/templates/template_command.md:15-35