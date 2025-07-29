# Modular Architecture Methodology Specs - Methodology Module Specifications

**29/07/2025** | Detailed specifications for /methodology: modules

## /methodology:thinkx4
**Content**: 4-perspective analysis template with enforcement
**Used by**: All commands requiring systematic analysis
**Template**:
```markdown
### Think x4 Analysis OBLIGATORIO
**Think 1**: ¿Cuál es el objetivo/problema real?
**Think 2**: ¿Qué alternativas/opciones existen?  
**Think 3**: ¿Qué estructura/approach optimiza resultado?
**Think 4**: ¿Cómo previene problemas identificados previamente?
**Conclusión**: Based on 4-perspective analysis
```

## /methodology:parallel_execution
**Content**: Concurrent tools enforcement patterns
**Used by**: research, orchestrator, close, start
**Template**:
```markdown
### Herramientas Paralelas OBLIGATORIO
**Antes tool execution** → analyze concurrency opportunities
**Batch operations** para información independiente obligatorio
**WebSearch + MCP context 7** simultáneamente cuando research
**ANTI-PATTERN**: Sequential execution cuando parallel posible
```

## /methodology:continuous_flow
**Content**: Anti-interruption execution templates
**Used by**: orchestrator, close workflows
**Template**:
```markdown
### Ejecución Continua CRÍTICA
**Template notification**: "Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."
**NUNCA pausar** esperando confirmación tras notificaciones intermedias
**Flujo obligatorio**: Ejecutar → notificar → CONTINUAR automáticamente → completar TODO
```

## /methodology:research_first
**Content**: Timestamp validation + research protocols
**Used by**: research, investigation patterns
**Template**:
```markdown
### Research-First Protocol OBLIGATORIO
**OBLIGATORIO iniciar** con $(date) command para current timestamp
**WebSearch + MCP context integration** simultáneamente requerido
**Best practices 2025** must be explicitly verified
**NUNCA asumir** información sin validation temporal
```

## /methodology:validation_protocol
**Content**: Authority alignment verification
**Used by**: All commands with system changes
**Template**:
```markdown
### Post-Validation Sistemática
**Authority alignment**: user-vision/TRUTH_SOURCE.md verification
**Simplicity compliance**: context/patterns/simplicity.md check
**Standards validation**: Según context apropiado domain-specific
**Second Task tool**: Para verification después delegación
```

---
**Referencias:** → context/operational/decisions/modular_architecture_directory_structure.md (structure design)
→ context/operational/decisions/modular_architecture_template_specs.md (template modules)