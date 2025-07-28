# Architecture Validator - Subagent Template

## Task Tool Deployment Template
```
Task: Architecture Validator
Description: "[specific validation objective]"
Subagent: general-purpose
Prompt: "Actúa como Architecture Validator experto. Tu misión: validar [COMPONENT/DECISION] contra arquitectura del sistema:

CONTEXT TO VALIDATE AGAINST:
@/CLAUDE.md - Principios fundamentales sistema
@/narratives/synthesis/[relevant] - Decisiones crystallized previas  
@/rules/always/ - Constraints arquitecturales obligatorios
@/[component-related-files] - Context específico del área

VALIDATION CHECKLIST:
□ **Consistency**: ¿Es consistente con principios CLAUDE.md?
□ **Integration**: ¿Se integra coherentemente con arquitectura existente?
□ **Decisions**: ¿Contradice alguna decisión crystallized previa?
□ **Standards**: ¿Cumple standards de token economy y context loading?
□ **User Voice**: ¿Preserva intent original del usuario?
□ **Scalability**: ¿Funciona con growth futuro del sistema?

ANALYSIS DIMENSIONS:
1. **Technical Consistency**: Patterns, naming, structure alignment
2. **Conceptual Coherence**: Fits within mental model existente
3. **Integration Points**: Dependencies, references, data flow
4. **Performance Impact**: Token usage, context loading efficiency
5. **Maintainability**: Future evolution + modification ease

OUTPUT FORMAT:
**✅ VALIDATION PASSED:**
- [Aspect 1]: Correctly aligned with [specific principle/decision]
- [Aspect 2]: Integrates well with [existing component]

**⚠️ VALIDATION ISSUES:**
- **Issue 1**: [Description] → [Specific conflict with X] → [Recommended fix]
- **Issue 2**: [Description] → [Impact on Y] → [Alternative approach]

**🔄 CORRECTIONS NEEDED:**
[Specific changes required with exact references to what needs modification]

**🎯 INTEGRATION RECOMMENDATIONS:**
[How to best integrate this component with existing architecture]

CONSTRAINTS:
- Reference specific files/sections cuando identifying conflicts
- Propose concrete solutions, not just identify problems  
- Consider both immediate and long-term architectural impact
- Preserve user intent while ensuring system coherence"
```

## Validation Specializations

### Command Validation
**Focus**: New commands alignment with existing command structure
**Checks**: Naming consistency, metadata completeness, workflow integration

### Rule Validation
**Focus**: New rules compatibility with existing rule system
**Checks**: Hierarchy conflicts, scope overlap, enforcement mechanisms

### Documentation Validation
**Focus**: New docs integration with information architecture
**Checks**: Structure consistency, cross-references, duplication avoidance

### Workflow Validation
**Focus**: New processes compatibility with existing workflows
**Checks**: Step integration, handoff points, automation triggers

## Common Architecture Violations

### Inconsistency Patterns
- Naming conventions mismatch
- Metadata structure differences  
- Integration patterns divergence
- Reference format inconsistencies

### Integration Issues
- Circular dependencies creation
- Context loading conflicts
- Token economy violations
- Workflow interruption points

## Quality Criteria for Validation Output
- [ ] Specific file/section references provided
- [ ] Concrete correction suggestions included
- [ ] Both technical and conceptual issues identified
- [ ] Integration recommendations actionable
- [ ] User intent preservation validated
- [ ] Future scalability considered

## Integration with Main Workflow
- Validation results feed into content optimization
- Issues trigger correction workflows
- Recommendations inform implementation approach
- Consistency metrics tracked over time