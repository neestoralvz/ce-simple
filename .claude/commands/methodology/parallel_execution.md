# /methodology:parallel_execution - Concurrent Tools Enforcement

**29/07/2025 11:25 CDMX** | Parallel tool execution methodology for maximum efficiency

## Herramientas Paralelas OBLIGATORIO

### Principio Fundamental: Simultaneidad vs Secuencia
**OBLIGATORIO:** Usar múltiples tools simultáneamente/concurrentemente en un solo mensaje cuando sea posible
**ANTI-PATTERN:** Ejecución secuencial de tools que pueden ser paralelos
**EFICIENCIA:** Batch operations para información independiente

### Identificación Oportunidades Paralelas
**Criteria para Simultaneidad:**
- **Información independiente:** Múltiples archivos sin dependencias
- **Operaciones no-bloqueantes:** Lecturas, búsquedas, validaciones paralelas  
- **Research + Analysis:** Investigación simultánea múltiples dominios
- **Status checks:** Git status + diagnostics + file checks batch

### Web Searches Concurrentes OBLIGATORIO
**WebSearch + MCP context 7** simultáneamente cuando research requerido
**SIEMPRE concurrent/simultaneous** cuando multiple searches needed
**NUNCA** sequential web research cuando parallel possible
**Multiple domain research** via parallel investigation

### Cuándo Usar Tools Simultáneos
- **Research phase:** Múltiples Grep + Read + LS operations
- **Status validation:** Git + diagnostics + file checks
- **Multi-file analysis:** Batch reading archivos relacionados
- **Investigation:** Parallel search patterns diferentes

### Pre-Tool Execution Analysis
**ANTES de ejecutar cualquier tool** → DEBE analizar oportunidades concurrency
**OBLIGATORIO preguntar**: ¿Pueden estos tools ejecutarse simultáneamente?
**BATCH operations** para tools independientes en single message
**ANTI-PATTERN**: Sequential execution cuando parallel posible

## Concurrency Opportunities Identification

### Independent File Operations
**Diferentes archivos = parallel execution**
**Read-only operations**: Grep + Read + LS = siempre paralelos
**Multiple searches**: Grep patterns diferentes = batch execution
**File + analysis**: Edit + analysis cuando no overlap = simultáneos

### Templates Ejecución Concurrente
```markdown
# Research phase concurrent pattern
**Research operations**: WebSearch + MCP context 7 + Grep patterns simultáneamente
**File analysis**: Read multiple files + LS directories + Grep searches batch
**Status validation**: Git status + diagnostics + file system checks parallel
```

## Integration Pattern

### Command Usage
```markdown
## Methodology Integration
**LOAD:** /methodology:parallel_execution

## [Command Function]
[Analyze concurrency opportunities before tool execution]
[Use parallel tools when information is independent]
```

### Enforcement Criteria
- **Tool execution analysis** required before any multi-tool operation
- **Concurrent tools preferred** over sequential when possible
- **Batch operations mandatory** for independent information gathering
- **Web research concurrent** with MCP context integration

---
**Authority Source**: context/patterns/orchestrator_methodology.md + context/enforcement/core_reminders.md
**Extracted from**: /roles:research, /roles:orchestrator, /workflows:close patterns