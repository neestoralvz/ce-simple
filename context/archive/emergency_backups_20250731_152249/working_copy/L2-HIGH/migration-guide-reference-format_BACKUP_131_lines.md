# Migration Guide - @ vs Reference Format Correction

**31/07/2025 02:00 CDMX** | Systematic migration guide for @ vs reference semantic correction

## AUTORIDAD SUPREMA
context/architecture/standards/reference-format-standards.md → migration-guide implements systematic correction per format authority

## MIGRATION OBJECTIVE
**Correct semantic misuse**: Remove @ from conditional/documentary references while preserving @ for auto-import functionality

## MIGRATION ANALYSIS

### **Files Requiring @ Preservation (Auto-Import)**
- `CLAUDE.md`: Core context auto-loading
- `context/architecture/claude_code/semantic-triggers/README.md`: LOAD statements
- Any semantic trigger LOAD/EXECUTE/VALIDATE patterns
- Context dispatcher auto-loading mechanisms

### **Files Requiring @ Removal (Convert to References)**
- Authority chain references: `← @context/` → `← context/`
- Cross-references: `←→ @context/` → `←→ context/`
- Forward references: `→ @context/` → `→ context/`
- Documentary/informational links throughout system

## SYSTEMATIC MIGRATION PROTOCOL

### **Phase 1: Audit & Classification**
1. **Auto-Import Audit**: Identify all legitimate @ usage (semantic triggers, CLAUDE.md core)
2. **Reference Audit**: Identify all @ usage that should be references
3. **Impact Assessment**: Map all files requiring conversion
4. **Dependency Analysis**: Ensure no functional breakage from @ removal

### **Phase 2: Reference Conversion**
1. **Authority Chains**: Convert `← @context/` to `← context/`
2. **Cross-References**: Convert `←→ @context/` to `←→ context/`
3. **Forward References**: Convert `→ @context/` to `→ context/`
4. **Line-Specific**: Convert `→ @context/file.md:15-25` to `→ context/file.md:15-25`

### **Phase 3: Markdown Enhancement**
1. **Simple Format**: Keep directional + path format
2. **Markdown Format**: Add `[Display Text](context/path/file.md)` where readability improves
3. **Reference-Style**: Use `[Display Text][ref-id]` with footer for complex documents
4. **Consistency**: Maintain format consistency within documents

### **Phase 4: Validation & Testing**
1. **Auto-Import Testing**: Verify @ usage still functions for semantic triggers
2. **Reference Testing**: Verify references work without auto-loading
3. **Authority Chain Testing**: Verify authority semantics preserved
4. **System Integration**: Full system functionality validation

## MIGRATION EXAMPLES

### **Authority Chain Conversion**
```
# BEFORE (Incorrect)
← @context/architecture/core/authority.md

# AFTER (Correct - Simple)
← context/architecture/core/authority.md

# AFTER (Correct - Markdown) 
← [Authority Framework](context/architecture/core/authority.md)

# AFTER (Correct - Reference-Style)
← [Authority Framework][authority-ref]
[authority-ref]: context/architecture/core/authority.md
```

### **Cross-Reference Conversion**
```
# BEFORE (Incorrect)
←→ @context/architecture/patterns.md

# AFTER (Correct - Simple)
←→ context/architecture/patterns.md

# AFTER (Correct - Markdown)
←→ [Architecture Patterns](context/architecture/patterns.md)
```

### **Auto-Import Preservation**
```
# PRESERVE (Correct - Auto-Loading)
@context/vision/vision_foundation.md  # CLAUDE.md core
LOAD: @context/architecture/claude-code.md  # Semantic trigger
```

## RISK MITIGATION

### **Functional Preservation**
- **Authority Chain Integrity**: References maintain authority semantics without auto-loading
- **Cross-Reference Functionality**: Bidirectional relationships preserved 
- **System Navigation**: All navigation paths remain functional
- **Auto-Import Protection**: Legitimate @ usage protected from conversion

### **Rollback Capability**
- **Pre-Migration Backup**: Complete system state before conversion
- **Incremental Migration**: File-by-file conversion with validation
- **Rollback Testing**: Verify rollback procedures before migration
- **Functionality Testing**: Full system test after each migration phase

## VALIDATION CHECKLIST

### **@ Usage Validation**
- [ ] Semantic triggers maintain @ for LOAD statements
- [ ] CLAUDE.md core context maintains @ for always-loaded
- [ ] Context dispatcher maintains @ for auto-loading
- [ ] NO @ usage for documentary/conditional references

### **Reference Validation**
- [ ] Authority chains function without @ prefix
- [ ] Cross-references maintain bidirectional semantics
- [ ] Forward references maintain delegation semantics
- [ ] All directional indicators (←, ←→, →) preserved

### **System Integration Validation**
- [ ] Authority chain integrity preserved throughout system
- [ ] Cross-reference navigation remains functional
- [ ] Semantic trigger auto-loading unaffected
- [ ] Documentation readability improved with markdown format

## INTEGRATION REFERENCES

**Format Standards**: ← context/architecture/standards/reference-format-standards.md
**Migration Authority**: → context/handoffs/HANDOFF_M_MARKDOWN_REFERENCE_STANDARDS.md
**Validation Protocol**: → context/architecture/standards/validation-reference-compliance.md

---

**MIGRATION DECLARATION**: Systematic @ vs reference correction preserving auto-import functionality while converting conditional references to proper format per user semantic authority.

**SUCCESS CRITERIA**: @ restricted to auto-import, all references converted to conditional format with preserved functionality and improved markdown readability.