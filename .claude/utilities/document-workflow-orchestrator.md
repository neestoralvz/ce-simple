# Document Workflow Orchestrator - Utility

## Core Orchestration Pattern

### Multi-Specialist Deployment (Conditional)

**INSTRUCCIÓN**: Deploy specialists based on workflow step requirements

#### Step 1: Document Creation
**Deploy when**: New document requested
**Specialists**: Research + Content + Voice Preservation + Integration
**Pattern**: `create-doc-orchestration`

#### Step 2: Document Alignment  
**Deploy when**: Architecture validation needed
**Specialists**: Architecture Validator + Integration + Cross-Reference + Conflict Detector
**Pattern**: `align-doc-orchestration`

#### Step 3: Document Verification
**Deploy when**: Final quality assurance required
**Specialists**: Quality Assurance + Performance + Compliance + Production Readiness
**Pattern**: `verify-doc-orchestration`

## Template References

### Available Specialists
- **Research Specialist**: `../templates/research-specialist.md`
- **Content Optimizer**: `../templates/content-optimizer.md`
- **Architecture Validator**: `../templates/architecture-validator.md`
- **Quality Assurance**: `../templates/quality-assurance.md`
- **Voice Preservation**: `../templates/voice-preservation.md`
- **Integration Specialist**: `../templates/integration-specialist.md`

### Deployment Instructions

#### Research + Content Pattern
```
Task: Research Specialist (from ../templates/research-specialist.md)
Focus: Document type best practices + optimization patterns

Task: Content Optimizer (from ../templates/content-optimizer.md)  
Focus: Generate core structure using research findings
```

#### Architecture + Validation Pattern
```
Task: Architecture Validator (from ../templates/architecture-validator.md)
Focus: System integration + consistency validation

Task: Integration Specialist (from ../templates/integration-specialist.md)
Focus: Cross-reference validation + conflict detection
```

#### Quality + Compliance Pattern
```
Task: Quality Assurance (from ../templates/quality-assurance.md)
Focus: Final verification + production readiness

Task: Performance Optimizer (from ../templates/performance-optimizer.md)
Focus: Token economy + context loading optimization
```

## Auto-Chain Logic

### Conditional Progression
- **create-doc** → **align-doc**: IF document complexity > basic
- **align-doc** → **verify-doc**: IF alignment issues detected
- **verify-doc** → **complete**: Always (workflow termination)

### Override Patterns
- User can skip steps with explicit instruction
- Emergency override available for urgent documents
- Quality gates can be bypassed with documentation

## Success Criteria
- [ ] Zero hardcoded specialist prompts
- [ ] Template references functional
- [ ] Conditional deployment working
- [ ] Auto-chain logic preserved
- [ ] Token economy optimized