# [Methodology Name] - Three-Layer Architecture

**Updated**: [Date] | **Authority**: [Authority Level] | **Limit**: ≤50 lines (Concept Layer)
**Navigation**: [System Hub](../navigation/index.md) | **Related**: [Layer Separation Rules](../standards/layer-separation-rules.md)

## Layer 1: Core Concept | Philosophy

### Purpose Definition
**Objective**: [Clear, single-sentence purpose statement]
**Scope**: [What this methodology covers and doesn't cover]
**Authority**: [Reference to governing principles/frameworks]

### Essential Methodology
**Principle**: [Core governing principle in 1-2 sentences]
**Application**: [When and how to apply this methodology]
**Integration**: [How it connects with other system components]

### Decision Triggers
**Apply When**: [Specific conditions that trigger this methodology]
**Context Required**: [Essential context needed before application]
**Success Criteria**: [How to measure successful application]

### Key Concepts
**[Concept 1]**: [Essential understanding in 1 line]
**[Concept 2]**: [Essential understanding in 1 line]  
**[Concept 3]**: [Essential understanding in 1 line]

### Quick Reference
**Implementation Guide**: [Link to Layer 2 - Implementation file]
**Templates**: [Link to relevant templates]
**Validation**: [Link to Layer 3 - Verification checklist]

---

## Layer 2: Implementation → [Reference Link]

**Implementation File**: `@docs/implementation/[methodology-name]-implementation.md`
**Purpose**: Detailed step-by-step procedures, technical specifications, workflow patterns
**Structure**: Prerequisites → Process → Integration → Troubleshooting
**Access Pattern**: Reference when applying methodology

## Layer 3: Verification → [Agent Deployment]

**Validation File**: `@docs/validation/[methodology-name]-checklist.md`
**Purpose**: Quality gates, compliance checks, success verification
**Structure**: Pre-validation → Process validation → Post-validation → Metrics
**Access Pattern**: Agent-deployed for automated validation

---

## Agent Deployment Footer

**🤖 IMPLEMENTATION AGENT**: Deploy Task Tool
```
Agent Mission: Apply [methodology-name] using implementation guide
Required Context: @docs/implementation/[methodology-name]-implementation.md
Authority: This concept document + PTS 12/12 validation
Output: Complete implementation following all procedures
Quality Gate: Must pass pre-validation before proceeding
```

**🔍 VALIDATION AGENT**: Deploy Task Tool  
```
Agent Mission: Audit implementation against validation checklist
Required Context: @docs/validation/[methodology-name]-checklist.md
Authority: Validation criteria + measurement standards
Output: Compliance report + recommendations
Success Criteria: 100% validation checklist completion
```

**🔄 COORDINATION PROTOCOL**: Implementation Agent → Complete work → Validation Agent → Quality verification → Final delivery

---

**Architecture Principle**: Concept (essential understanding) → Implementation (detailed execution) → Verification (quality assurance) via coordinated agent deployment ensuring consistent, validated methodology application