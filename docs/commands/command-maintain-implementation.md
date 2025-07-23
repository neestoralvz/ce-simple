# Command-Maintain Implementation Details

## Purpose
Implementation specifications for `/command-maintain` command with proactive guardrails and automated repair.

## Proactive Guardrails

### Validation System
- **File Size**: Block edits >150 lines, suggest progressive disclosure
- **Complexity**: Real-time scoring, warn at 7.0 threshold
- **Execution Ratio**: Enforce 3:1 tool calls to documentation minimum
- **Template**: Validate Purpose, Usage, Implementation, Triggers sections
- **Anti-Bias**: Detect assumptions, provide neutralization suggestions

**Guardrail Specifications**:
- **Size Guard**: Reject edits >150 lines, suggest progressive disclosure extraction
- **Complexity Guard**: Real-time scoring with 7.0 threshold warnings
- **Execution Guard**: Enforce minimum 3:1 tool calls to documentation ratio
- **Template Guard**: Validate required sections (Purpose, Usage, Implementation, Triggers)
- **Anti-Bias Guard**: Detect assumptions, provide neutralization recommendations

## Audit Framework

### File Size Analysis
Detect violations >150 lines, calculate excess content for extraction.

### Documentation Theater Detection
Analyze tool call ratio, require >0.03 tool calls per line.

### Template Compliance
Verify Purpose, Usage, Implementation, Triggers sections presence.

**Audit Framework**:
- **Size Analysis**: Detect files >150 lines, calculate excess for extraction
- **Theater Detection**: Analyze tool call ratio, flag <0.03 calls per line
- **Template Compliance**: Verify all required sections present and complete
- **Reference Integrity**: Validate cross-references and link accessibility
- **Standards Compliance**: Check against documentation and command standards

## Automated Repair

### Progressive Disclosure
Extract oversized content to implementation files, update with references.

### Execution Layer Addition
Add missing tool calls to commands with documentation theater.

**Repair Operations**:
- **Progressive Disclosure**: Extract oversized content to *-details.md files with references
- **Execution Addition**: Add missing tool calls to eliminate documentation theater
- **Template Repair**: Insert missing sections with standard templates
- **Reference Repair**: Fix broken links, update paths, consolidate duplicate content
- **Standards Alignment**: Apply current documentation and command standards

## Workflow Efficiency

### Batch Operations
1. **Audit Phase**: LS, Bash, Grep operations for analysis
2. **Repair Phase**: Size violations, theater detection, template compliance
3. **Reporting**: Compliance metrics, violation summary, health score

### Parallel Execution
Concurrent analysis with batch processing for performance optimization.

**Workflow Efficiency**:
- **Batch Phase**: Parallel LS/Bash/Grep operations for comprehensive analysis
- **Repair Phase**: Sequential size violations, theater detection, template compliance
- **Report Phase**: Generate compliance metrics, violation summary, health scores
- **Optimization**: Concurrent analysis with resource pooling for performance

## Smart Defaults

### Decision Matrix
- **Size Violations**: Auto-extract at 150 lines (no confirmation)
- **Documentation Theater**: Add execution layer at <0.03 ratio (confirm)
- **Template Violations**: Auto-add missing sections (no confirmation)
- **Broken References**: Auto-repair with manual fallback

## Progress Tracking

### Real-Time Updates
Progress tracking with TodoWrite integration for audit, repair, and optimize phases.

---

**Detailed specifications for command-maintain with automated operations and verification protocols.**