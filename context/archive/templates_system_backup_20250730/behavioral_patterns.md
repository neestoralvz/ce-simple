# Behavioral Pattern Templates - Consolidated

**29/07/2025 11:35 CDMX** | Behavioral pattern templates for consistent system behavior

## Correcto vs Incorrecto Templates

### Basic Behavioral Templates
**Template correcto:** [CORRECT_PATTERN_DESCRIPTION]
**Template incorrecto:** [INCORRECT_BEHAVIOR_DESCRIPTION]

### Execution Flow Templates
**CORRECTO:** "Completado X → [RESULTADO]. Continuando automáticamente con Y..."
**PROHIBIDO:** "He completado X. ¿Continúo con Y?"

**CORRECTO:** Notificar progreso Y continuar automáticamente
**PROHIBIDO:** "¿Quieres que continúe?" tras cada subtarea

### Continuous Execution Templates
**Template Correcto Implementado:**
"Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."

**FLUJO CORRECTO:**
1. Ejecutar subtarea via Task tool
2. Notificar resultado transparentemente  
3. CONTINUAR inmediatamente con siguiente
4. Repetir hasta completar TODA la lista
5. Finalizar solo cuando TODO esté completo

### Authority vs Implementation Templates
**User Domain (Vision/Requirements):**
- Story conception y dirección narrativa
- Estándares calidad y criterios aceptación
- Filosofía arquitectural y principios
- Expectativas comportamiento sistema

**AI Domain (Implementation/Execution):**
- Choices implementación técnica
- Estructura código y organización
- Selección herramientas y uso
- Estrategias optimización

### Research vs Execution Templates
**Research Protocol:** OBLIGATORIO usar fecha más reciente con comando $(date)
**WebSearch + MCP context 7** simultáneamente cuando research requerido
**NUNCA asumir** información without validation temporal

### Documentation Style Templates
**PROHIBIDO:** Usar o code blocks para cualquier contenido
**CORRECTO:** Texto directo, listas numeradas, referencias inline
**RATIONALE:** Visual bloat sin valor añadido - contenido debe ser autoexplicativo

## Quality Assurance Templates

### Conversation Compacting Templates
**OBLIGATORIO:** Mantener 95%+ fidelidad quotes usuario originales
**NUNCA:** Parafrasear o interpretar declaraciones de autoridad
**SIEMPRE:** Preservar context decisional y rationale original

### System Behavior Templates
**RESULTADO ESPERADO:** "Completado TODAS las tareas. Sistema totalmente operativo."
**PROHIBIDO:** "Completado tarea 1 de 5. ¿Continúo con tarea 2?"

## Integration Syntax
```markdown
**TEMPLATE:** /examples:behavioral_patterns
```

---
**Authority Source**: context/operational/enforcement/anti_patterns.md + context/operational/decisions/continuous_execution_methodology.md
**Extracted from**: Behavioral pattern templates across enforcement and decision documentation
**Consolidation Date**: 29/07/2025 - Template deduplication initiative