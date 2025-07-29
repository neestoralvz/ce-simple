# /modules:header_timestamped - Standard Timestamp Header

**TEMPLATE:** /examples:headers_footers
**CONTEXT:** Timestamped header template for documentation

## Header Template

### Standard Format
```markdown
# [DOCUMENT_TITLE] - [PURPOSE]

**DD/MM/YYYY HH:MM CDMX | Actualizado: DD/MM/YYYY HH:MM CDMX** | [BRIEF_PURPOSE]
```

### Usage Pattern
**Creation timestamp**: Date document was first created
**Update timestamp**: Date of most recent significant modification  
**Location**: CDMX timezone standard
**Purpose**: Brief description of document function

### Integration Syntax
```markdown
**TEMPLATE:** /modules:header_timestamped
```

### Variable Substitution
- **[DOCUMENT_TITLE]**: Replace with actual document title
- **[PURPOSE]**: Replace with document's specific purpose
- **DD/MM/YYYY HH:MM**: Replace with actual timestamps
- **[BRIEF_PURPOSE]**: Replace with concise purpose description

---
**Authority Source**: context/patterns/documentation_style.md:12-16 + header consistency patterns
**Extracted from**: Universal documentation header format across context/ files