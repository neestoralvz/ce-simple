# /modules:footer_authority - Authority Source & Traceability

**29/07/2025 11:30 CDMX** | Authority chain footer template

## Footer Template

### Standard Format
```markdown
---
**Authority Source**: [SOURCE_DESCRIPTION]
**Trazabilidad**: [CONVERSATION_REFERENCES]
**References**: [RELATED_DOCUMENTS]
```

### Usage Pattern
**Authority declaration**: Clear source of decision/information authority
**Conversation traceability**: Links to originating conversations
**Document relationships**: Related documentation for context
**Decision lineage**: Chain of authority from user vision to implementation

### Integration Syntax
```markdown
**FOOTER:** /modules:footer_authority
```

### Variable Substitution
- **[SOURCE_DESCRIPTION]**: Replace with specific authority source
- **[CONVERSATION_REFERENCES]**: Replace with conversation links/quotes
- **[RELATED_DOCUMENTS]**: Replace with related documentation

### Example Usage
```markdown
---
**Authority Source**: user-vision/TRUTH_SOURCE.md + partner consultation analysis
**Trazabilidad**: user-vision/TRUTH_SOURCE.md [L1:67, L1:23]
**References**: 
- Authority framework: context/principles/authority.md
- Simplicity principles: context/patterns/simplicity.md
- Decision context: context/conversations/session-reference.md
```

### Authority Source Types
- **User vision quotes**: Direct quotes from TRUTH_SOURCE or conversations
- **System decisions**: Architectural or methodological decisions
- **Pattern analysis**: Extracted from behavioral patterns
- **Consultation results**: Partner/challenge analysis outcomes

---
**Authority Source**: Pattern observed in context/decisions/ and context/principles/ files
**Extracted from**: Authority declaration + trazabilidad pattern across system documentation