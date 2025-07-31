# Implementation Strategy - 3-Phase @ vs Reference Correction

**31/07/2025 14:45 CDMX** | Systematic 3-phase implementation strategy for @ vs reference distinction

## AUTORIDAD SUPREMA
context/handoffs/HANDOFF_M_MARKDOWN_REFERENCE_STANDARDS.md → implementation-strategy.md implements strategy per handoff authority

## PRINCIPIO FUNDAMENTAL
**"3-phase systematic correction preserves functionality while establishing proper semantics"** - Strategic implementation ensuring no functionality loss during semantic correction.

## IMPLEMENTATION STRATEGY

### **Phase 1: Semantic Distinction Establishment**
**STRICT SEPARATION**: @ for auto-import, references for conditional
**Auto-Import Validation**: Audit all @context/ usage - only keep if auto-loads
**Reference Conversion**: Convert documentary @context/ to simple references

### **Phase 2: Format Standardization**
**Auto-Import Format**: `@context/file.md` (unchanged)
**Reference Format Options**:
- Simple: `context/file.md`
- Markdown: `[Display Text](context/file.md)`
- Reference-style: `[Display Text][ref-id]` with `[ref-id]: context/file.md`

### **Phase 3: Authority Chain Correction**
**Authority References**: `← context/architecture/core/authority.md` (NO @)
**Cross-References**: `←→ context/architecture/patterns.md` (NO @)
**Forward References**: `→ context/architecture/templates.md` (NO @)
**Semantic Preservation**: Maintain directional indicators without auto-import

## SYSTEMATIC EXECUTION PROTOCOL

### **Phase 1 Implementation Steps**
1. **Auto-Import Audit**: Identify legitimate @context/ usage (auto-loading only)
2. **Documentary Reference Identification**: Find @context/ used for non-loading references
3. **Semantic Validation**: Verify each @context/ usage purpose and behavior
4. **Conversion Planning**: Prepare documentary references for format conversion

### **Phase 2 Implementation Steps**
1. **Format Selection**: Choose appropriate reference format per use case
2. **Batch Conversion**: Systematic conversion of documentary @context/ references
3. **Syntax Validation**: Ensure proper markdown syntax compliance
4. **Authority Chain Preservation**: Maintain directional reference semantics

### **Phase 3 Implementation Steps**
1. **Authority Chain Updates**: Convert authority references from @ to conditional format
2. **Cross-Reference Updates**: Update bidirectional references without auto-import
3. **Forward Reference Updates**: Update forward references maintaining navigation
4. **System Integration**: Validate complete system functionality post-conversion

---

**IMPLEMENTATION STRATEGY DECLARATION**: 3-phase systematic correction strategy ensuring @ vs reference semantic distinction while preserving complete system functionality and authority chain integrity.