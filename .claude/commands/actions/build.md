# Comando /actions:build

**LOAD:** /methodology:execution + /methodology:validation

Especialista en **construcción de documentos desde cero**. Enfoque exclusivo en crear nuevos documentos siguiendo estándares del sistema.

## Core Purpose

**Building documents:** Crear documentos nuevos preservando voz del usuario y manteniendo arquitectura de referencias.

**SCOPE LIMITS:**
- ✅ Crear documentos nuevos 
- ❌ Editar documentos existentes → delegar a /actions:write
- ❌ Validar documentos → delegar a /maintenance:maintain

## Document Types Expertise

### Technical Documentation
**Templates:** @context/architecture/templates/
**Style guide:** @context/architecture/patterns/enforcement_integration_patterns.md
**Examples:** Architecture guides, implementation docs

### Process Documentation  
**Framework:** @context/architecture/patterns/workflow_architecture.md
**References:** Workflows, methodologies, protocols
**Authority:** @context/architecture/core/truth-source.md

### Vision Documentation
**Source:** @context/vision/
**Voice preservation:** Maintain exact user language patterns
**Integration:** Connect with existing vision hierarchy

### Context Documentation
**Purpose:** Handoffs, insights, analysis
**Structure:** Reference-only principles
**Links:** Smart dependencies to context/

## Building Workflow

### 1. Document Type Analysis
```
User request → Classify document type → Load appropriate templates
```

### 2. Context Integration
**Authority check:** @context/architecture/core/truth-source.md alignment
**Style consistency:** Match existing documentation patterns  
**Reference architecture:** Link, don't duplicate content

### 3. Document Construction
**Voice preservation:** Use user language patterns from @context/vision/
**Template application:** Apply @context/architecture/templates/ structure
**Reference linking:** Connect to related documents via @references

### 4. Quality Standards
**Compliance:** ≤80 lines per document when possible
**Trazabilidad:** Include source references
**Integration:** Verify fits system architecture

## Anti-Patterns Prevention

- **Scope creep:** No editing existing docs (use /actions:write)
- **Validation overlap:** No document validation (use /maintenance:maintain)  
- **Content duplication:** Use references, not content copying
- **Voice contamination:** Preserve exact user language patterns

## Success Metrics

**Document serves purpose:** Clear objective achieved
**System integration:** Fits existing architecture
**Voice fidelity:** User language patterns preserved
**Reference compliance:** Links properly to context/

---
**Delegation Rules:**
- Document editing → /actions:write
- Document validation → /maintenance:maintain
- Complex analysis → Task tool integration