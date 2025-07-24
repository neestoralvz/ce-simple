# Documentation Standards - Implementation Layer

**Purpose**: Detailed procedures for agent-deployed documentation creation and optimization
**Foundation**: @docs/rules/documentation-standards-foundation.md
**Validation**: @docs/validation/documentation-standards-checklist.md

## Prerequisites

### Required Context Loading
- **Always Load**: @docs/rules/markdown-standards.md when creating documentation
- **Conditional Load**: @docs/templates/three-layer-methodology-template.md for methodology docs
- **Agent Deployment**: @docs/standards/agent-deployment-footer-standard.md for coordination

### Environment Setup
- English-only language environment confirmed
- PTS 12/12 validation framework loaded
- Target audience identified (Claude Code agents vs users)
- Integration points mapped with existing documentation

## Implementation Process

### Phase 1: Foundation Creation (≤50 lines)
1. **Purpose Definition**: Single-sentence objective statement
2. **Authority Establishment**: Reference governing principles/frameworks
3. **Essential Principles**: Core concepts in imperative voice
4. **Decision Triggers**: When/how to apply methodology
5. **Quick References**: Links to implementation and validation layers

### Phase 2: Implementation Development
1. **Detailed Procedures**: Step-by-step agent-executable instructions
2. **Technical Specifications**: Precise requirements and constraints
3. **Integration Patterns**: How methodology connects with system components
4. **Error Handling**: Fallback procedures and troubleshooting guides

### Phase 3: Validation Framework Creation
1. **Quality Gates**: Measurable compliance criteria
2. **Success Metrics**: Quantifiable validation standards
3. **Agent Checklists**: Automated verification procedures
4. **Feedback Loops**: Continuous improvement mechanisms

## Content Organization Standards

### Component Extraction Protocol
**Extract to Specialized Files**:
- Checklists → `/docs/validation/[name]-checklist.md`
- Examples → `/docs/examples/[name]-examples.md`
- Templates → `/docs/templates/[name]-template.md`
- Procedures → `/docs/procedures/[name]-procedure.md`

### Cross-Reference Management
**Reference Syntax**: Use @path/to/file.md for internal references
**Line-Level Imports**: @file.md:15-23 for precision context loading
**Conditional Loading**: Implement decision-triggered imports based on work type

## Agent Deployment Patterns

### Implementation Agent Mission Template
```
Agent Mission: Execute [methodology-name] following implementation procedures
Required Context: Complete implementation guide + foundation concepts
Authority: PTS 12/12 validation + governing principles
Output Format: Structured deliverable meeting all specifications
Quality Gates: Must pass pre-validation before proceeding to next phase
Integration: Coordinate with validation agent for final verification
```

### Coordination Workflow
1. **Foundation Agent**: Loads concept layer for contextual understanding
2. **Implementation Agent**: Executes detailed procedures with full context
3. **Validation Agent**: Audits output against comprehensive checklist
4. **Integration Agent**: Ensures system-wide consistency and cross-references

## Troubleshooting Guide

### Common Issues and Solutions
- **Length Exceeding Limits**: Apply component extraction before compaction
- **Cross-Reference Errors**: Validate all @path references during creation
- **Agent Context Overload**: Use line-level imports (@file.md:15-23) for precision
- **Validation Failures**: Deploy validation agent to identify specific non-compliance

### Quality Recovery Procedures
1. **Identify Root Cause**: Use validation agent to pinpoint failure points
2. **Apply Targeted Fixes**: Focus on specific PTS component failures
3. **Re-validate Incrementally**: Test each fix against validation criteria
4. **Document Patterns**: Capture successful recovery patterns for future use

## Integration Requirements

### System Integration Points
- **CLAUDE_RULES.md**: Enhanced Conditional Context System updates
- **Navigation System**: Update navigation/index.md with new architecture
- **Cross-Module Dependencies**: Validate references across documentation system
- **Agent Coordination**: Ensure compatibility with existing deployment patterns

### Maintenance Protocols
- **Regular Audits**: Deploy validation agents monthly for compliance checks
- **Context Optimization**: Monitor token usage and optimize imports quarterly
- **Pattern Evolution**: Update templates based on successful implementation patterns
- **Quality Metrics**: Track documentation effectiveness and agent deployment success

---

**Implementation Status**: Ready for agent deployment
**Next Phase**: Validation agent deployment for quality assurance