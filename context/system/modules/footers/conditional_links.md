# /modules:footer_conditional - Conditional Reference Links

**29/07/2025 11:30 CDMX** | Conditional reference footer template

## Footer Template

### Standard Format
```markdown
---
## Enlaces → Información Complementaria
**Si necesitas [DOMAIN]:** → [FILE_PATH]:[LINE_RANGE]
**Si requieres [FUNCTION]:** → [FILE_PATH]:[LINE_RANGE]
**Si buscas [CONTEXT]:** → [FILE_PATH]:[LINE_RANGE]
```

### Usage Pattern
**Conditional loading**: References triggered by specific needs
**Line specificity**: Exact line ranges for targeted information
**Domain coverage**: Links to relevant specialized knowledge
**Function routing**: Direct paths to implementation details

### Integration Syntax
```markdown
**FOOTER:** /modules:footer_conditional
```

### Variable Substitution
- **[DOMAIN]**: Replace with specific knowledge domain
- **[FUNCTION]**: Replace with specific functionality needed
- **[CONTEXT]**: Replace with contextual requirement
- **[FILE_PATH]**: Replace with actual file location
- **[LINE_RANGE]**: Replace with specific line numbers

### Example Usage
```markdown
---
## Enlaces → Información Complementaria
**Si necesitas simplicity principles:** → context/patterns/simplicity.md:15-40
**Si requieres authority framework:** → context/principles/authority.md:1-25
**Si buscas orchestrator patterns:** → context/patterns/orchestrator_methodology.md:100-150
```

---
**Authority Source**: Pattern observed across context/enforcement/, context/patterns/ files
**Extracted from**: "Si necesitas/Si requieres" footer pattern universally applied