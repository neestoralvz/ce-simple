# Three-Layer Documentation Rule

**Purpose**: Progressive disclosure documentation structure for cognitive optimization  
**Authority**: Extracted from docs/decisions/governance/three-layer-system-adr.md  
**Trigger**: Documentation creation, methodology development  
**Status**: Active | **Lines**: ≤80

## When to Apply Three-Layer Structure

**Triggers**:
- Documentation exceeds cognitive load (≤50 lines concept limit)
- Users need both overview & detailed procedures
- Quality assurance requires systematic validation
- Agent deployment needed for implementation

**Test**: If content serves multiple cognitive needs → Apply three layers

## Layer Structure Definition

### Layer 1: Concept (≤50 lines, always loaded)
**Purpose**: Essential understanding + decision triggers
**Content**: Purpose definition | Core principles | When to apply | Success criteria | Quick references
**Access**: Always loaded in context for immediate decision support

### Layer 2: Implementation (referenced when needed)
**Purpose**: Detailed step-by-step procedures + technical specifications  
**Content**: Prerequisites | Detailed process | Technical specs | Integration | Troubleshooting
**Access**: Referenced when methodology needs to be applied

### Layer 3: Validation (agent-deployed)
**Purpose**: Quality gates + compliance checks + validation criteria
**Content**: Pre-validation | Process gates | Post-validation | Success metrics
**Access**: Agent-deployed for automated quality assurance

## Agent Deployment Standards

### Implementation Agent Footer
```markdown
**🤖 IMPLEMENTATION AGENT**: Deploy Task Tool
Agent Mission: Apply [methodology] using implementation guide
Required Context: @docs/implementation/[methodology]-implementation.md
Authority: This concept document + PTS 12/12 validation
Output: Complete implementation following all procedures
```

### Validation Agent Footer  
```markdown
**🔍 VALIDATION AGENT**: Deploy Task Tool
Agent Mission: Audit implementation against validation checklist
Required Context: @docs/validation/[methodology]-checklist.md
Authority: Validation criteria + measurement standards
Output: Compliance report + recommendations
```

## Benefits Achieved

- **Cognitive Load Optimization**: Immediate understanding without overload
- **Context Economy**: Load details only when needed (40% reduction)  
- **Automated Quality**: Agent-deployed validation ensures consistency
- **Scalable Growth**: New methodologies follow established pattern

---

**🤖 IMPLEMENTATION AGENT**: Apply three-layer structure when documentation exceeds cognitive limits  
**🔍 VALIDATION AGENT**: Verify layer separation & agent deployment compliance