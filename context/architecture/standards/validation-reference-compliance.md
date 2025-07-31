# Validation Reference Compliance - @ vs Reference Authority

**31/07/2025 02:00 CDMX** | Complete validation framework for @ vs reference compliance

## AUTORIDAD SUPREMA
@context/architecture/standards/reference-format-standards.md → validation-reference-compliance.md implements validation authority per format standards

## VALIDATION FRAMEWORK OBJECTIVE
**Systematic compliance verification**: Ensure @ restricted to auto-import and references used for conditional/documentary links per user semantic authority

## VALIDATION CATEGORIES

### **Auto-Import Validation (@ Required)**
**Validation Rule**: @ usage MUST have actual auto-loading functionality
**Valid Patterns**:
- `@context/vision/vision_foundation.md` in CLAUDE.md (always loaded)
- `LOAD: @context/architecture/claude-code.md` in semantic triggers
- `@context/architecture/core/truth-source.md` in context dispatcher
- Any pattern that loads context automatically into conversation

**Invalid Patterns**:
- `← @context/file.md` (authority chain - should be reference)
- `←→ @context/file.md` (cross-reference - should be reference)
- `→ @context/file.md` (forward reference - should be reference)

### **Reference Validation (@ Forbidden)**
**Validation Rule**: References MUST NOT use @ prefix
**Valid Patterns**:
- `← context/architecture/core/authority.md` (authority chain)
- `←→ context/architecture/patterns.md` (cross-reference)
- `→ context/architecture/templates.md` (forward reference)
- `[Display Text](context/path/file.md)` (markdown format)
- `[Display Text][ref-id]` with `[ref-id]: context/path/file.md` (reference-style)

**Invalid Patterns**:
- Any reference using @ when not auto-loading
- Authority chains with @ prefix
- Cross-references with @ prefix

## VALIDATION PROTOCOLS

### **Automated Validation Rules**
```bash
# Auto-Import Validation
# VALID: @ in semantic triggers with LOAD
grep -r "LOAD:.*@context/" context/

# VALID: @ in CLAUDE.md core context
grep -r "@context/" CLAUDE.md

# INVALID: @ in authority chains (should be references)
grep -r "← @context/" context/

# INVALID: @ in cross-references (should be references)  
grep -r "←→ @context/" context/

# INVALID: @ in forward references (should be references)
grep -r "→ @context/" context/
```

### **Manual Validation Criteria**
1. **Context Loading Test**: Does @ usage actually load context automatically?
2. **Semantic Trigger Test**: Is @ used in LOAD/EXECUTE/VALIDATE patterns?
3. **CLAUDE.md Core Test**: Is @ used for always-loaded core context?
4. **Reference Function Test**: Do references work without auto-loading?

### **Validation Checklist**
- [ ] **Auto-Import Compliance**: All @ usage has actual auto-loading functionality
- [ ] **Reference Compliance**: All references without @ work for conditional links
- [ ] **Authority Chain Integrity**: Authority semantics preserved without @
- [ ] **Cross-Reference Functionality**: Bidirectional relationships work without @
- [ ] **Directional Preservation**: ←, ←→, → indicators maintained in all formats
- [ ] **Markdown Compatibility**: Reference formats support markdown enhancement

## COMPLIANCE MONITORING

### **System-Wide Validation**
**Pre-Migration Validation**: Current system @ vs reference usage audit
**Post-Migration Validation**: Verify @ restricted to auto-import only
**Ongoing Validation**: Regular compliance monitoring for new content
**Integration Validation**: System functionality preserved after conversion

### **Quality Gates**
1. **Auto-Import Gate**: @ usage validated for actual context loading
2. **Reference Gate**: References validated for conditional/documentary function
3. **Authority Gate**: Authority chain semantics preserved without auto-loading
4. **System Gate**: Full system functionality after @ vs reference correction

## ERROR DETECTION & CORRECTION

### **Common Violations**
- **@ in Authority Chains**: `← @context/` should be `← context/`
- **@ in Cross-References**: `←→ @context/` should be `←→ context/`
- **@ in Forward References**: `→ @context/` should be `→ context/`
- **References in Auto-Import**: Missing @ in semantic triggers/CLAUDE.md core

### **Correction Protocols**
1. **Violation Detection**: Automated scanning for @ vs reference violations
2. **Impact Assessment**: Determine functional impact of correction
3. **Systematic Correction**: Apply format standards per violation type
4. **Validation Testing**: Verify correction preserves functionality

## INTEGRATION REFERENCES

**Format Standards**: ← @context/architecture/standards/reference-format-standards.md
**Migration Guide**: ← @context/architecture/standards/migration-guide-reference-format.md
**Handoff Authority**: → @context/handoffs/HANDOFF_M_MARKDOWN_REFERENCE_STANDARDS.md

---

**VALIDATION DECLARATION**: Complete validation framework ensuring @ restricted to auto-import and references used for conditional/documentary links per user semantic authority distinction.

**ENFORCEMENT PROTOCOL**: Systematic validation preventing @ misuse while preserving auto-import functionality and enabling markdown enhancement for references.