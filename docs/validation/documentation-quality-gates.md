# Documentation Quality Gates

**Purpose**: Quality validation requirements for documentation standards compliance
**Authority**: Documentation standards enforcement and quality assurance
**Usage**: Apply before documentation deployment to ensure standards adherence

## Pre-Deployment Checklist

### Architecture Compliance
- [ ] Three-layer architecture applied (concept ≤50 lines | implementation referenced | verification agent-deployed)
- [ ] Component extraction completed for reusable elements
- [ ] Conditional import framework used for context loading decisions
- [ ] Agent deployment footer included with proper mission statements

### Content Standards
- [ ] Anti-bias language enforced (no subjective terms or embellishments)
- [ ] English-only language compliance maintained throughout
- [ ] Compaction techniques applied (pipe headers | arrow notation | dense lists)
- [ ] Line-level references used for precision (@path/file.md:42-47)

### Technical Requirements
- [ ] Markdown standards compliance (@docs/rules/markdown-standards.md)
- [ ] 100-line limit respected for documentation | 80-line limit for commands
- [ ] Zero content duplication across files
- [ ] Cross-reference integrity maintained

## Blocking Criteria

### Architecture Violations
**Critical Failures** (Stop deployment):
- Missing layer separation in three-layer architecture
- No agent deployment footer in methodology documents
- Exceeded concept layer limit (>50 lines)
- Component extraction not applied when reusable content identified

### Standards Violations
**Quality Failures** (Requires correction):
- Subjective language present (eliminate terms like "complex", "simple", "important")
- Missing compaction techniques application
- No conditional import framework implementation
- Vague references used instead of precise line targeting

### Agent Coordination Violations
**Process Failures** (Workflow correction needed):
- No writing agent deployment for major document creation
- Missing validation agent coordination for standards compliance
- Incomplete mission statements in agent deployment
- No specialized context provided for agent tasks

## Success Criteria Validation

### Quantitative Metrics
- **Line Compliance**: ≤100 lines for docs, ≤50 lines for concept layer, ≤80 lines for commands
- **Reference Precision**: 100% use of @path/file.md:line format for specific content
- **Language Compliance**: 0% non-English content
- **Duplication Rate**: 0% technical content duplication

### Qualitative Assessment
- **Clarity**: Immediate comprehension without additional context required
- **Completeness**: All necessary information present for intended use
- **Actionability**: Clear instructions that can be executed immediately
- **Maintainability**: Updates can be made without breaking system integrity

## Validation Workflow

### Automated Checks
1. **Line Count Validation**: Verify file length compliance
2. **Reference Format Validation**: Check @path/file.md:line syntax accuracy
3. **Language Detection**: Scan for non-English content
4. **Cross-Reference Integrity**: Validate all links and references

### Manual Review Requirements
1. **Architecture Assessment**: Confirm three-layer structure implementation
2. **Content Quality Review**: Verify anti-bias language compliance
3. **Agent Coordination Verification**: Check agent deployment protocols followed
4. **Integration Testing**: Ensure documentation functions within system context

## Remediation Guidelines

### Architecture Issues
- **Missing Layer Separation**: Apply three-layer methodology template
- **Exceeded Line Limits**: Apply component extraction before compaction
- **No Agent Coordination**: Add agent deployment protocols and mission statements

### Content Issues
- **Subjective Language**: Replace with objective, measurable criteria
- **Missing Compaction**: Apply context compaction techniques systematically
- **Poor References**: Convert to precise line-level targeting format

---

**Quality Principle**: Documentation must pass all quality gates before deployment to ensure system integrity, user experience, and standards compliance.