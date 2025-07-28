# Research Protocols Module

## RESEARCH-FIRST PROTOCOL OBLIGATORIO
TODA decisión/tarea DEBE iniciar con:
1. `$(date)` para timestamp actualizado
2. WebSearch con fecha actual para best practices
3. MCP Context7 para análisis de patrones 
4. Sistematización automática de findings

## RESEARCH INTEGRATION REQUIREMENTS
- **Pre-Task Research**: OBLIGATORIO para cada Task tool deployment
- **Context Updates**: Research findings deben actualizarse sistemáticamente
- **Pattern Recognition**: MCP Context7 para identificar patterns emergentes
- **Best Practice Adoption**: WebSearch findings integrados automáticamente
- **Temporal Accuracy**: Siempre usar fecha actual $(date) para relevancia

## RESEARCH PROTOCOL SELECTIVE CRITERIA (USER REFINEMENT 2025-07-28)

### RESEARCH OBLIGATORIO - TIER 1
- Crear/modificar comandos nuevos (implementación)
- Cambios arquitecturales que afecten ecosystem 
- Decisiones técnicas complejas >100 líneas
- Document creation via /create-doc workflow
- System modifications que requieren best practices validation

### RESEARCH CONDICIONAL - TIER 2
- Workflow modifications con user impact
- Command updates con architectural implications
- Integration changes entre systems

### RESEARCH INNECESARIO - TIER 3
- Activación de sistemas existentes (ej: /become-orchestrator)
- Lectura de archivos y status checks
- Ejecución de workflows predefinidos
- Comandos de configuración rutinaria <20 líneas
- Session management operations

### ENFORCEMENT
Todos los comandos con `research-driven: true` deben evaluarse contra estos criterios. Comandos de activación deben cambiar a `research-driven: false`.

### SYSTEMATIC IMPACT
Este refinement debe aplicarse across ALL commands in ecosystem para consistency y efficiency optimization.

### Voice preservation
Esta refinement preserva user voice exactly while optimizing system efficiency.