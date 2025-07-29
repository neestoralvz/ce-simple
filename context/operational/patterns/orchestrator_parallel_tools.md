# Orchestrator Parallel Tools - Metodología Herramientas Paralelas

**29/07/2025 11:40 CDMX** | Parallel tools methodology

## Principio Fundamental: Simultaneidad vs Secuencia

**APPLICATION:** Usar múltiples tools simultáneamente/concurrentemente en un solo mensaje cuando sea posible, ejecución secuencial de tools que pueden ser paralelos, batch operations para información independiente

## Identificación Oportunidades Paralelas

### Criteria para Simultaneidad
- **Información independiente:** Múltiples archivos sin dependencias  
- **Operaciones no-bloqueantes:** Lecturas, búsquedas, validaciones paralelas
- **Research + Analysis:** Investigación simultánea múltiples dominios
- **Status checks:** Git status + diagnostics + file checks batch

### Cuándo Usar Tools Simultáneos
- **Research phase:** Múltiples Grep + Read + LS operations
- **Status validation:** Git + diagnostics + file checks
- **Multi-file analysis:** Batch reading archivos relacionados
- **Investigation:** Parallel search patterns diferentes

## Anti-Patterns Herramientas

### Ejecución Secuencial Innecesaria
- **Tools independientes:** NUNCA ejecutar Read → Read → Grep cuando pueden ser simultáneos
- **Information gathering:** Batch todas operaciones de lectura/búsqueda
- **Status checks:** Combinar git + diagnostics + validaciones en single call
- **Research operations:** Parallel investigation múltiples dominios

### Detección Oportunidades Perdidas
**Signals para concurrent execution:**
- Múltiples archivos diferentes mencionados
- Operaciones read-only independientes
- Research en dominios separados
- Validation checks no-dependientes

## Metodología Batch Operations

### Template Concurrency Analysis
**ANTES de ejecutar tools** → analizar:
1. ¿Son operaciones independientes?
2. ¿Pueden ejecutarse simultáneamente?
3. ¿Información no-dependiente?
4. ¿Batch optimiza performance?

### Examples Execution Patterns
→ **Ver context/system/examples/orchestrator_concurrent_patterns.md** para ejemplos completos
→ **Ver context/system/examples/bash/research_integration.sh** para scripts concurrency

---
**Referencias:** → context/operational/patterns/orchestrator_delegation_core.md (principios delegación)
→ context/operational/patterns/orchestrator_continuous_execution.md (ejecución continua)