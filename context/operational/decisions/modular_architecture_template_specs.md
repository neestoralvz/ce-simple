# Modular Architecture Template Specs - Template Module Specifications

**29/07/2025** | Template modules + integration patterns

## Template Modules

### /modules:header_timestamped
Standard timestamp format | All context/ docs
```markdown
# [TITLE] - [PURPOSE]
**DD/MM/YYYY HH:MM CDMX** | [BRIEF_PURPOSE]
```

### /modules:enforcement_vocabulary  
Consistent enforcement language | All enforcement docs
```markdown
**DEBE usar:** DEBE, SIEMPRE, NUNCA, OBLIGATORIO, FUNDAMENTAL, ESENCIAL
**Template correcto:** [PATTERN] | **ANTI-PATTERN:** [INCORRECT]
```

### /modules:footer_conditional
Conditional reference links | Most context/ docs
```markdown
---
## Enlaces → Información Complementaria
**Si necesitas [DOMAIN]:** → [FILE_PATH]:[LINES]
```

### /modules:footer_authority
Authority source + traceability | Decision docs, principles  
```markdown
---
**Authority Source**: [SOURCE] | **Trazabilidad**: [REFERENCES]
```

## Integration Patterns

### Command Refactoring
BEFORE: 93 lines with embedded methodology → AFTER: 30 lines focused function
```markdown
**LOAD:** /methodology:required_modules
## Core Function
[Command-specific logic only]
```

### Documentation Refactoring  
BEFORE: Manual headers/footers/enforcement → AFTER: Template-driven
```markdown
**TEMPLATE:** /modules:required_templates
## Unique Content
[Document-specific information only]
```

## Composition Rules

### Multiple Loading
```markdown
**LOAD:** /methodology:thinkx4 + /methodology:parallel + /methodology:validation
```

### Template Stacking
```markdown
**TEMPLATE:** /modules:header_timestamped + /modules:enforcement_vocabulary
**CONTENT:** /modules:think_sections | **FOOTER:** /modules:footer_authority
```

---
**Referencias:** → context/operational/decisions/modular_architecture_methodology_specs.md (methodology specs)
→ context/operational/decisions/modular_architecture_implementation.md (migration strategy)