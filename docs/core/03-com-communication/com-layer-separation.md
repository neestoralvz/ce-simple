# Layer Separation Rules - Three-Layer Architecture

**Updated**: 2025-07-24 | **Authority**: Document architecture standard | **Limit**: 100 lines
**Navigation**: [System Hub](../navigation/index.md) | **Related**: [Three-Layer Template](../templates/three-layer-methodology-template.md)

## Layer Definition Standards

### Layer 1: Concept | Philosophy (≤50 lines)
**Purpose**: Essential understanding + methodology core + decision triggers
**Content Rules**: What to include vs exclude for optimal cognitive load

#### INCLUDE in Concept Layer
- **Purpose Definition**: Single sentence objective + scope boundaries
- **Core Principle**: Governing methodology in 1-2 sentences maximum  
- **Decision Triggers**: When to apply + required context + success criteria
- **Key Concepts**: Essential understanding (3-5 concepts, 1 line each)
- **Integration Points**: How methodology connects with system components
- **Quick Reference**: Links to implementation + templates + validation

#### EXCLUDE from Concept Layer
- Step-by-step procedures | Technical specifications | Detailed examples
- Code implementations | Configuration details | Troubleshooting guides  
- Comprehensive checklists | Historical context | Alternative approaches
- Tool-specific instructions | Platform details | Version requirements

### Layer 2: Implementation (Referenced)
**Purpose**: Detailed procedures + technical specifications + workflow patterns
**Access Pattern**: Referenced when applying methodology + agent-deployed

#### INCLUDE in Implementation Layer
- **Prerequisites**: Required setup + dependencies + environment preparation
- **Step-by-Step Process**: Detailed workflow + decision points + alternatives
- **Technical Specifications**: Code examples + configuration + parameters
- **Integration Procedures**: How to connect with other system components
- **Troubleshooting Guide**: Common issues + solutions + recovery procedures
- **Tools + Resources**: Specific tool usage + platform requirements

#### STRUCTURE Requirements
```markdown
## Prerequisites
## Core Process
## Integration Points  
## Troubleshooting
## Tools + Resources
```

### Layer 3: Verification (Agent-Deployed)
**Purpose**: Quality gates + compliance checks + success validation + metrics
**Access Pattern**: Agent-deployed for automated validation

#### INCLUDE in Verification Layer
- **Pre-Validation**: Requirements check before starting implementation
- **Process Validation**: Quality gates during methodology application
- **Post-Validation**: Completion verification + success criteria assessment
- **Compliance Checks**: Standards adherence + framework compliance
- **Success Metrics**: Quantitative measures + qualitative assessments
- **Failure Recovery**: What to do when validation fails

#### STRUCTURE Requirements
```markdown
## Pre-Validation Checklist
## Process Quality Gates
## Post-Validation Criteria  
## Compliance Standards
## Success Metrics
## Failure Recovery Protocol
```

## Content Migration Rules

### Moving Content FROM Concept TO Implementation
**Triggers**: >1 line explanation needed | Step-by-step required | Technical details | Tool-specific instructions
**Process**: Extract to implementation file → Replace with reference link → Update agent deployment footer

### Moving Content FROM Implementation TO Verification  
**Triggers**: Quality checking | Compliance measurement | Success criteria | Validation procedures
**Process**: Extract to validation file → Reference in implementation → Include in agent deployment footer

### Keeping Content IN Concept Layer
**Criteria**: Essential for understanding | Decision-making support | 1-line maximum | Core methodology

## File Organization Standards

### Naming Conventions
- **Concept**: `[methodology-name].md` (primary file)
- **Implementation**: `[methodology-name]-implementation.md` (@docs/implementation/)
- **Verification**: `[methodology-name]-checklist.md` (@docs/validation/)

### Directory Structure
```
docs/
├── [category]/                    # Concept layer files
├── implementation/                # Layer 2 files
└── validation/                   # Layer 3 files
```

### Reference Integration
**Concept → Implementation**: Reference link with context explanation
**Concept → Verification**: Agent deployment footer with mission definition
**Implementation → Verification**: Quality gate references throughout process

## Quality Gates

### Concept Layer Validation
- [ ] ≤50 lines total length
- [ ] Purpose clear in first paragraph
- [ ] Core principle stated in 1-2 sentences
- [ ] Decision triggers clearly defined
- [ ] Implementation + validation properly referenced
- [ ] No step-by-step procedures included

### Implementation Layer Validation  
- [ ] Complete procedure coverage
- [ ] Clear prerequisite definition
- [ ] Step-by-step process documented
- [ ] Integration points specified
- [ ] Troubleshooting guidance included
- [ ] Tools + resources listed

### Verification Layer Validation
- [ ] Pre-validation checklist complete
- [ ] Process quality gates defined
- [ ] Post-validation criteria measurable
- [ ] Compliance standards referenced
- [ ] Success metrics quantified
- [ ] Failure recovery documented

---

**Architecture Principle**: Separate essential understanding (concept) from detailed execution (implementation) from quality assurance (verification) to optimize cognitive load while ensuring complete methodology coverage through coordinated layer integration