# Parallel Tools Methodology

Concurrent tool execution for maximum efficiency.

## Concurrency Principles
**CRITICAL:** Usar múltiples tools simultáneamente cuando operaciones son independientes

**Parallel opportunities:**
- **Research phase:** Múltiples Grep + Read + LS operations
- **Status validation:** Git + diagnostics + file checks
- **Multi-file analysis:** Batch reading archivos relacionados
- **Investigation:** Parallel search patterns diferentes

## Pre-execution Analysis
1. ¿Son operaciones independientes?
2. ¿Pueden ejecutarse simultáneamente?
3. ¿Información no-dependiente?
4. ¿Batch optimiza performance?

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

---

**Optimization**: Parallel execution reduces latency and improves user experience through concurrent operations.