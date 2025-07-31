# ADR-028: Systematic Component Obsolescence Management Protocol

**Date**: 2025-07-31  
**Status**: ACCEPTED  
**Authority**: User vision supremacy → @context/architecture/core/truth-source.md → ADR-028

## Context

System requires systematic approach for managing component obsolescence and archiving decisions. Current ad-hoc elimination creates authority contamination risk and lacks evidence-based evaluation framework. Case study: handoff-7-system directories and roadmap system evolution required systematic evaluation to determine continued utility versus archiving necessity.

**Problem Statement**: 
- No systematic framework for evaluating component continued utility
- Ad-hoc archiving decisions without evidence-based assessment
- Risk of eliminating valuable components or preserving obsolete overhead
- Lack of historical intelligence preservation during obsolescence management

## Decision

**SYSTEMATIC COMPONENT OBSOLESCENCE MANAGEMENT PROTOCOL OBLIGATORIO** with evidence-based assessment and intelligence preservation.

### 4-Phase Obsolescence Assessment Framework:

#### Phase 1: **Utility Analysis**
- **Mission Completion Assessment**: Evaluate if component fulfilled original purpose
- **Current Integration Assessment**: Analyze active dependencies and cross-references
- **Functional Redundancy Assessment**: Identify if functionality superseded by evolved components
- **Value Contribution Assessment**: Measure current system contribution vs overhead cost

#### Phase 2: **Evidence-Based Decision**  
- **Think x4 Analysis OBLIGATORIO**: Apply 4-perspective systematic evaluation
- **Stakeholder Impact Assessment**: Evaluate user workflow and system disruption
- **Authority Preservation Assessment**: Verify critical user authority maintained
- **Evolution Path Assessment**: Analyze if component blocks or enables system evolution

#### Phase 3: **Archive-with-Intelligence Methodology**
- **Historical Intelligence Extraction**: Preserve successful patterns and learnings
- **Authority Preservation**: Maintain 95%+ user voice fidelity in archived content
- **Cross-Reference Documentation**: Create README.md explaining archive rationale
- **Learning Integration**: Document insights for future similar decisions

#### Phase 4: **Systematic Implementation**
- **TodoWrite Process Tracking**: Track assessment and implementation steps systematically
- **Legacy Archive Organization**: Structured preservation in `/context/archive/legacy/`
- **Reference Update**: Systematic cleanup of broken references post-archiving
- **Validation Protocol**: Confirm zero functionality loss and authority preservation

### Decision Criteria Framework:

```
Archive Component When:
├── Mission Completed: ✓ Original purpose fulfilled successfully
├── Functionality Superseded: ✓ Capabilities absorbed by evolved components  
├── System Overhead: ✓ Maintenance cost > current value contribution
└── Evolution Blocker: ✓ Presence impedes organic system evolution

Preserve Component When:
├── Active Integration: ✓ Critical dependencies or active cross-references
├── Unique Value: ✓ Functionality not available elsewhere in system
├── Evolution Enabler: ✓ Supports or enables planned system evolution
└── User Authority: ✓ Contains irreplaceable user authority statements
```

### Integration Requirements:
- **Archive Structure**: `/context/archive/legacy/[component-name]-experiments/`
- **README Template**: Historical intelligence preservation with archive rationale
- **Reference Cleanup**: Systematic broken reference identification and resolution
- **Authority Chain**: Complete traceability preservation through archive process

## Consequences

### Positive:
- **Evidence-Based Decisions**: Systematic evaluation eliminates guesswork in obsolescence management
- **Historical Intelligence Preservation**: Learning continuity through structured archive methodology  
- **Authority Integrity**: User voice preservation through systematic assessment protocols
- **System Evolution**: Organic growth enabled through systematic obsolete component removal

### Negative:
- **Assessment Overhead**: Systematic evaluation requires time investment vs immediate decisions
- **Archive Maintenance**: Additional responsibility for preserved component organization

### Risk Mitigation:
- **TodoWrite Tracking**: Process transparency and systematic completion validation
- **Think x4 Analysis**: Multi-perspective evaluation reduces decision error probability
- **Authority Preservation**: 95%+ user voice fidelity prevents authority contamination

## Case Study Validation

**Handoff System Archiving (2025-07-31)**:
- ✅ **Mission Completed**: HANDOFF 6 & 7 successfully processed 981 files
- ✅ **Functionality Superseded**: orchestration.md + methodology.md absorbed successful patterns  
- ✅ **System Overhead**: Token economy optimization without functional loss
- ✅ **Authority Preservation**: Historical intelligence documented in archive README

**Results**: Successful archiving with zero functionality loss and complete authority preservation

## Compliance Monitoring

**Enforcement Protocol**: Guardian role OBLIGATORIO validates systematic assessment completion
**Quality Gates**: Evidence-based decision framework DEBE be applied for all obsolescence decisions
**Authority Preservation**: 95%+ user voice fidelity FUNDAMENTAL during archive process

## References

- **Authority Source**: @context/architecture/core/truth-source.md (supreme architecture authority)
- **Methodology Integration**: @context/architecture/core/methodology.md (systematic evaluation integration)
- **Archive Protocol**: @context/archive/README.md (archive authority and preservation protocols)
- **Case Study**: @context/archive/legacy/handoff-system-experiments/README.md (implementation example)

---
**EVOLUTION**: Systematic obsolescence management enables organic system evolution through evidence-based component lifecycle decisions with complete authority preservation and historical intelligence continuity.