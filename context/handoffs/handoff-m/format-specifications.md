# Format Specifications - @ vs Reference Syntax Standards

**31/07/2025 14:45 CDMX** | Complete format specifications for @ auto-import vs conditional references

## AUTORIDAD SUPREMA
@context/handoffs/HANDOFF_M_MARKDOWN_REFERENCE_STANDARDS.md → format-specifications.md implements format standards per handoff authority

## PRINCIPIO FUNDAMENTAL
**"Clear format specifications ensure consistent @ vs reference usage"** - Precise syntax standards enabling systematic implementation and validation.

## CORRECTED FORMAT STANDARDS

### **AUTO-IMPORT ONLY (with @)**
```markdown
@context/vision/vision_foundation.md  # Always loaded in CLAUDE.md
@context/architecture/core/truth-source.md  # Auto-loaded by dispatcher
LOAD: @context/architecture/claude-code.md  # Semantic trigger auto-load
```

### **REFERENCES (without @)**

#### **Simple Format**
```markdown
← context/architecture/core/authority.md
←→ context/architecture/patterns.md
→ context/architecture/templates.md
```

#### **Markdown Format**
```markdown
← [Authority Framework](context/architecture/core/authority.md)
←→ [Architecture Patterns](context/architecture/patterns.md)
→ [Template System](context/architecture/templates.md)
```

#### **Reference-Style Format**
```markdown
← [Authority Framework][authority-ref]
←→ [Architecture Patterns][patterns-ref]
→ [Template System][templates-ref]

[authority-ref]: context/architecture/core/authority.md
[patterns-ref]: context/architecture/patterns.md
[templates-ref]: context/architecture/templates.md
```

## USAGE VALIDATION RULES

### **@ Usage Requirements**
- **ONLY for auto-loading**: Content automatically loads into conversation context
- **NEVER for documentary**: No @ for links that don't auto-load
- **Semantic triggers**: LOAD operations using @ for auto-import
- **CLAUDE.md core**: Always-loaded context using @ for auto-import

### **Reference Usage Requirements**
- **NO @ for documentary**: Conditional/documentary links without auto-loading
- **Authority chain preservation**: Directional indicators (←, →, ←→) maintained
- **Navigation functionality**: Links work for navigation without auto-loading
- **Markdown compliance**: Standard markdown syntax for reference links

## QUALITY STANDARDS

### **Format Quality Requirements**
- **Readability**: Clear display text describing component purpose
- **Consistency**: Standardized reference ID naming convention
- **Authority Preservation**: Maintain authority chain semantics
- **System Integration**: Compatible with existing @context/ prefix system

### **Validation Criteria**
- **Semantic Accuracy**: @ only for actual auto-loading functionality
- **Reference Functionality**: Conditional references work without auto-import
- **Authority Integrity**: Authority chains function with reference format
- **System Coherence**: Complete system functionality maintained

---

**FORMAT SPECIFICATIONS DECLARATION**: Complete @ vs reference format standards enabling systematic implementation and validation of proper semantic distinction per user authority requirements.