# Agent Deployment Protocols

**Purpose**: Standardized agent coordination for documentation creation and validation
**Authority**: Documentation standards compliance and quality assurance
**Usage**: Deploy agents for specialized documentation tasks

## Documentation Creation Agent Coordination

### Writing Agent Deployment
**🤖 WRITING AGENT**: Deploy when creating methodology docs
```
Agent Mission: Apply three-layer architecture using methodology template
Required Context: docs/templates/three-layer-methodology-template.md + docs/standards/layer-separation-rules.md
Authority: Documentation standards + PTS 12/12 validation
Output: Concept layer (≤50 lines) + implementation/verification file structure
Quality Gate: Layer separation validated + agent deployment footer included
```

### Validation Agent Deployment
**🔍 VALIDATION AGENT**: Deploy for standards compliance audit
```
Agent Mission: Audit documentation against standards + three-layer architecture
Required Context: docs/rules/documentation-standards.md + docs/rules/markdown-standards.md
Authority: Documentation standards + compaction requirements + anti-bias language
Output: Compliance report + line count verification + layer separation validation
Success Criteria: 100% standards compliance + ≤100 lines + proper layer organization
```

## Agent Coordination Workflow

### Sequential Deployment Pattern
1. **Writing Agent**: Create initial three-layer structure
2. **Validation Agent**: Audit compliance and standards adherence
3. **Quality Gate**: Final verification before deployment

### Parallel Deployment Pattern
- **Complex Documents**: Deploy multiple writing agents for different layers simultaneously
- **Large Projects**: Coordinate validation agents across multiple document sets
- **System Updates**: Parallel audit of multiple documentation components

## Agent Mission Templates

### Standard Writing Mission
```
Agent Specialization: Documentation Creation
Objective: [Specific documentation goal]
Context Sources: [Relevant template and standard files]
Authority Framework: [Applicable standards and validation requirements]
Output Requirements: [Expected deliverables and format]
Quality Criteria: [Success metrics and validation requirements]
```

### Standard Validation Mission
```
Agent Specialization: Compliance Validation
Objective: [Specific audit scope]
Context Sources: [Standards and reference documentation]
Authority Framework: [Compliance requirements and quality gates]
Output Requirements: [Validation report format]
Success Criteria: [Pass/fail criteria and metrics]
```

## Integration Requirements

### Documentation Standards Integration
- **Three-Layer Architecture**: Agents must apply concept/implementation/verification separation
- **Component Extraction**: Agents must identify and extract reusable components
- **Line Limit Compliance**: Agents must achieve ≤100 lines through extraction and compaction
- **Context Management**: Agents must use precise line references for imports

### Quality Assurance Integration
- **PTS Validation**: All agent output must pass 12-component PTS framework
- **English-Only Compliance**: Agents must enforce language standards
- **Anti-Bias Language**: Agents must eliminate subjective terminology
- **Cross-Reference Integrity**: Agents must maintain accurate file references

---

**Deployment Principle**: Specialized agents with precise missions, sufficient context, and clear success criteria produce higher quality documentation while maintaining system standards compliance.