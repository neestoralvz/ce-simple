# /modules:enforcement_vocabulary - Consistent Enforcement Language

**TEMPLATE:** /examples:headers_footers
**CONTEXT:** Enforcement vocabulary module for behavioral consistency

## Enforcement Vocabulary

### Required Language Patterns
**TEMPLATE:** /examples:enforcement_vocabulary
**CONTEXT:** Documentation vocabulary standards
**APPLICATION:** Usar DEBE, SIEMPRE, NUNCA, OBLIGATORIO, FUNDAMENTAL, ESENCIAL; ser verboso, redundante, duplicativo; lenguaje natural puro, directo, técnico

### Template Patterns

#### Obligation Templates
```markdown
**DEBE [ACTION]:** [SPECIFIC_REQUIREMENT]
**SIEMPRE [BEHAVIOR]:** [CONSISTENT_PATTERN]
**NUNCA [ANTI-PATTERN]:** [PROHIBITED_BEHAVIOR]
**OBLIGATORIO:** [CRITICAL_REQUIREMENT]
```

#### Behavioral Templates
```markdown
**Template correcto:** [CORRECT_PATTERN_DESCRIPTION]
**ANTI-PATTERN:** [INCORRECT_BEHAVIOR_DESCRIPTION]
**PROHIBIDO:** [FORBIDDEN_ACTION]
**ENFORCEMENT:** [COMPLIANCE_MECHANISM]
```

#### Execution Templates
```markdown
**REGLA OBLIGATORIA:** [RULE_STATEMENT]
**FLUJO CORRECTO:** [PROPER_SEQUENCE]
**ERROR GRAVE:** [SERIOUS_VIOLATION]
**CORRECCIÓN:** [REMEDIATION_ACTION]
```

### Integration Syntax
```markdown
**TEMPLATE:** /modules:enforcement_vocabulary
```

### Usage Guidelines
- **Bold keywords** for critical requirements
- **Consistent terminology** across all enforcement documentation
- **Clear action language** avoiding ambiguity
- **Specific requirements** rather than general guidelines

### Example Integration
```markdown
**DEBE aplicar** Think x4 methodology en all analysis
**SIEMPRE usar** parallel tools cuando información independiente
**NUNCA pausar** ejecución tras notificaciones intermedias
**OBLIGATORIO verificar** authority alignment después delegación
```

---
**Authority Source**: context/patterns/documentation_style.md:7-11 + enforcement language patterns
**Extracted from**: context/enforcement/core_reminders.md, behavioral_enforcement.md vocabulary