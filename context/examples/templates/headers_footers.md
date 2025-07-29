# Headers & Footers Templates - Consolidated

**29/07/2025 11:35 CDMX** | Document structure templates for consistent formatting

## Standard Header Templates

### Timestamped Header Template
```markdown
# [DOCUMENT_TITLE] - [PURPOSE]

**DD/MM/YYYY HH:MM CDMX** | [BRIEF_PURPOSE]
```

### Updated Timestamped Header Template
```markdown
# [DOCUMENT_TITLE] - [PURPOSE]

**DD/MM/YYYY HH:MM CDMX | Actualizado: DD/MM/YYYY HH:MM CDMX** | [BRIEF_PURPOSE]
```

### Module Header Template
```markdown
# /[MODULE_TYPE]:[MODULE_NAME] - [MODULE_PURPOSE]

**DD/MM/YYYY HH:MM CDMX** | [MODULE_DESCRIPTION]
```

## Standard Footer Templates

### Authority Chain Footer Template
```markdown
---
**Authority Source**: [SOURCE_DESCRIPTION]
**Trazabilidad**: [CONVERSATION_REFERENCES]
**References**: [RELATED_DOCUMENTS]
```

### Extraction Footer Template
```markdown
---
**Authority Source**: [ORIGINAL_SOURCE_FILES]
**Extracted from**: [EXTRACTED_CONTENT_DESCRIPTION]
**Consolidation Date**: [DATE] - [CONSOLIDATION_PURPOSE]
```

### Decision Footer Template
```markdown
---
**Trazabilidad:** [SOURCE_FILE] [REFERENCE_MARKERS]
**Usage:** [APPLICATION_CONTEXT]
**Integration:** [INTEGRATION_INSTRUCTIONS]
```

## Variable Substitution Guidelines

### Header Variables
- **[DOCUMENT_TITLE]**: Replace with actual document title
- **[PURPOSE]**: Replace with document's specific purpose
- **DD/MM/YYYY HH:MM**: Replace with actual timestamps
- **[BRIEF_PURPOSE]**: Replace with concise purpose description
- **[MODULE_TYPE]**: Replace with module category (examples, modules, patterns, etc.)
- **[MODULE_NAME]**: Replace with specific module identifier
- **[MODULE_PURPOSE]**: Replace with module function description

### Footer Variables
- **[SOURCE_DESCRIPTION]**: Replace with specific authority source
- **[CONVERSATION_REFERENCES]**: Replace with conversation links/quotes
- **[RELATED_DOCUMENTS]**: Replace with related documentation
- **[ORIGINAL_SOURCE_FILES]**: Replace with source file paths
- **[EXTRACTED_CONTENT_DESCRIPTION]**: Replace with description of extracted content
- **[DATE]**: Replace with consolidation/creation date
- **[CONSOLIDATION_PURPOSE]**: Replace with reason for consolidation

## Usage Patterns

### Document Creation Pattern
1. **Header**: Use appropriate header template based on document type
2. **Content**: Structure content according to document purpose
3. **Footer**: Use appropriate footer template for authority/traceability

### Authority Declaration Pattern
**Authority declaration**: Clear source of decision/information authority
**Conversation traceability**: Links to originating conversations
**Document relationships**: Related documentation for context
**Decision lineage**: Chain of authority from user vision to implementation

### Module Reference Pattern
**Module identification**: Clear module type and name
**Integration syntax**: Standard integration format
**Usage guidelines**: How to apply the module

## Integration Syntax
```markdown
**TEMPLATE:** /examples:headers_footers
```

## Example Applications

### Standard Document Example
```markdown
# System Validation Protocol - Methodology Guide

**29/07/2025 11:35 CDMX** | System validation methodology for quality assurance

[Document content here]

---
**Authority Source**: user-vision/TRUTH_SOURCE.md + system validation requirements
**Trazabilidad**: context/user-vision/TRUTH_SOURCE.md [L1:43]
**References**: 
- Quality gates: context/operational/enforcement/quality_gates.md
- Validation patterns: context/validation/methodology_integration_test.md
```

### Module Documentation Example
```markdown
# /modules:validation_protocol - System Validation Templates

**29/07/2025 11:35 CDMX** | Validation protocol templates for system compliance

[Module content here]

---
**Authority Source**: System validation patterns across enforcement documentation
**Extracted from**: Quality gates and validation templates in context/operational/
**Consolidation Date**: 29/07/2025 - Template deduplication initiative
```

---
**Authority Source**: context/system/modules/headers/timestamped.md + context/system/modules/footers/authority_chain.md
**Extracted from**: Header and footer patterns across context/ documentation
**Consolidation Date**: 29/07/2025 - Template deduplication initiative