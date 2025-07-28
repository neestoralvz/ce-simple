# Edit Workflow Orchestrator - Utility

## Core Edit Orchestration Pattern

### Multi-Specialist Deployment (Conditional)

**INSTRUCCIÓN**: Deploy edit specialists based on change complexity and scope

#### Step 1: Document Editing
**Deploy when**: Existing document modification requested
**Specialists**: Edit Specialist + Change Impact + Content Optimizer + Voice Preservation
**Pattern**: `edit-doc-orchestration`

#### Step 2: Edit Alignment  
**Deploy when**: Edit validation needed for consistency
**Specialists**: Architecture Validator + Integration + Change Verification + Conflict Detector
**Pattern**: `align-edit-orchestration`

#### Step 3: Edit Verification
**Deploy when**: Final edit quality assurance required
**Specialists**: Quality Assurance + Change Validation + Performance + Production Readiness
**Pattern**: `verify-edit-orchestration`

## Template References

### Available Edit Specialists
- **Edit Specialist**: `../templates/edit-specialist.md`
- **Change Impact Analyzer**: `../templates/change-impact-analyzer.md`
- **Architecture Validator**: `../templates/architecture-validator.md`
- **Quality Assurance**: `../templates/quality-assurance.md`
- **Voice Preservation**: `../templates/voice-preservation.md`
- **Integration Specialist**: `../templates/integration-specialist.md`

### Deployment Instructions

#### Edit + Impact Analysis Pattern
```
Task: Edit Specialist (from ../templates/edit-specialist.md)
Focus: Document modification + change implementation

Task: Change Impact Analyzer (from ../templates/change-impact-analyzer.md)  
Focus: Change scope assessment + impact evaluation
```

#### Architecture + Integration Pattern
```
Task: Architecture Validator (from ../templates/architecture-validator.md)
Focus: Edit consistency + system integration validation

Task: Integration Specialist (from ../templates/integration-specialist.md)
Focus: Cross-reference updates + dependency validation
```

#### Quality + Change Verification Pattern
```
Task: Quality Assurance (from ../templates/quality-assurance.md)
Focus: Edit quality verification + production readiness

Task: Change Verification Specialist (from ../templates/change-verification-specialist.md)
Focus: Change completeness + voice preservation validation
```

## Auto-Chain Logic

### Conditional Progression
- **edit-doc** → **align-edit**: IF change complexity > minor
- **align-edit** → **verify-edit**: IF alignment issues detected
- **verify-edit** → **complete**: Always (workflow termination)

### Override Patterns
- User can skip steps for minor edits
- Emergency override available for urgent changes
- Quality gates can be bypassed with documentation

## Change Classification

### Minor Edits (Skip alignment/verification)
- Typo corrections
- Format adjustments
- Simple content additions

### Major Edits (Full workflow required)
- Structural changes
- Logic modifications
- Voice preservation updates

### Critical Edits (Enhanced validation)
- Architecture changes
- System integration modifications
- Voice preservation score impacts

## Success Criteria
- [ ] Zero hardcoded specialist prompts
- [ ] Template references functional
- [ ] Conditional deployment based on change scope
- [ ] Auto-chain logic preserved
- [ ] Token economy optimized
- [ ] Change impact properly assessed