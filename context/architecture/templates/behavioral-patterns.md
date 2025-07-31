# Behavioral Pattern Templates - System Behavior Consistency

**31/07/2025 CDMX** | Behavioral pattern templates for consistent system behavior

## AUTORIDAD SUPREMA  
@context/architecture/core/truth-source.md → templates/ → behavioral-patterns.md implements behavioral consistency per system authority

## EXECUTION FLOW PATTERNS

### Continuous Execution Templates
**CORRECTO Pattern**:
"Completado [SUBTAREA] → [RESULTADO]. Continuando automáticamente con [SIGUIENTE] (progreso: X/Y)."

**FLUJO CORRECTO**:
1. Ejecutar subtarea via Task tool
2. Notificar resultado transparentemente  
3. CONTINUAR inmediatamente con siguiente
4. Repetir hasta completar TODA la lista
5. Finalizar solo cuando TODO esté completo

**PROHIBIDO Pattern**:
"He completado X. ¿Continúo con Y?" - NUNCA pausar esperando confirmación

### Authority vs Implementation Boundaries
**User Domain (Vision/Requirements)**:
- Story conception y dirección narrativa
- Estándares calidad y criterios aceptación  
- Filosofía arquitectural y principios
- Expectativas comportamiento sistema

**AI Domain (Implementation/Execution)**:
- Choices implementación técnica
- Estructura código y organización
- Selección herramientas y uso
- Estrategias optimización

## QUALITY ASSURANCE PATTERNS

### Research Protocol Patterns
**Research Protocol**: OBLIGATORIO usar fecha más reciente con comando $(date)
**WebSearch + MCP context 7** simultáneamente cuando research requerido
**NUNCA asumir** información without validation temporal

### Documentation Style Patterns
**PROHIBIDO**: Usar code blocks para cualquier contenido
**CORRECTO**: Texto directo, listas numeradas, referencias inline
**RATIONALE**: Visual bloat sin valor añadido - contenido debe ser autoexplicativo

### Conversation Preservation Patterns
**OBLIGATORIO**: Mantener 95%+ fidelidad quotes usuario originales
**NUNCA**: Parafrasear o interpretar declaraciones de autoridad
**SIEMPRE**: Preservar context decisional y rationale original

## BEHAVIORAL CONSISTENCY STANDARDS

### Language Patterns
**DO use**: DEBE, SIEMPRE, NUNCA, OBLIGATORIO for critical requirements
**DON'T use**: Weak language for behavioral boundaries
**DO maintain**: Consistent terminology across all components

### System Behavior Expectations
**RESULTADO ESPERADO**: "Completado TODAS las tareas. Sistema totalmente operativo."
**PROHIBIDO**: "Completado tarea 1 de 5. ¿Continúo con tarea 2?"

---
**BEHAVIORAL AUTHORITY**: Consistent system behavior serving user authority supremacy through standardized behavioral patterns.