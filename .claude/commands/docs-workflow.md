# Docs Workflow - Complete Documentation Optimization Workflow

## 🎯 Purpose
Execute comprehensive documentation optimization workflow through automated orchestration of audit, consolidation, optimization, and validation phases.

## 🚀 Usage
Execute: `/docs-workflow [mode]`
- **Default**: Complete pipeline (generate + optimize + validate)
- **audit**: Analysis only, no modifications
- **maintain**: Optimize existing docs without generation

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at docs workflow initialization**:

```javascript
TodoWrite([
  {"content": "📋 AUDIT: Execute comprehensive documentation health assessment", "status": "pending", "priority": "high", "id": "docs-audit-1"},
  {"content": "🔧 OPTIMIZATION: Apply progressive disclosure and size compliance", "status": "pending", "priority": "high", "id": "docs-optimize-1"},
  {"content": "✅ VALIDATION: Verify 85% minimum health score achievement", "status": "pending", "priority": "high", "id": "docs-validate-1"},
  {"content": "🔄 RECURSIVE: Apply correction cycles until quality threshold met", "status": "pending", "priority": "medium", "id": "docs-recursive-1"},
  {"content": "📊 TRACKING: Generate Git tracking for all documentation changes", "status": "pending", "priority": "medium", "id": "docs-tracking-1"}
])
```

**Quality-Threshold Management**: Add conditional todos for recursive optimization if 85% health score not achieved

### Structural Validation Protocol
**MANDATORY PRE-EXECUTION**:
1. 🏗️ **STRUCTURE-CHECK**: Validate project organization compliance with `../docs/structure/project-organization-protocol.md`
2. 🔗 **REFERENCE-VERIFY**: Check cross-reference integrity via `/matrix-maintenance validate`
3. 📏 **SIZE-VALIDATE**: Enforce file size limits with automatic extraction to docs/
4. ⚡ **AUTO-CORRECT**: Fix structural violations automatically before workflow execution
5. 🗺️ **MATRIX-SYNC**: Execute periodic matrix maintenance during workflow cycles

**File Placement Intelligence**:
- **Auto-Extract**: Oversized content → Appropriate docs/ subdirectory
- **Reference Repair**: Broken links → Updated paths with integrity verification
- **Structure Optimization**: File placement → Canonical directory structure

### Workflow Execution Protocol
**MAINTAIN Mode**: Progressive disclosure for oversized files (>140 lines)
**Execution Phases**: Structural validation → Matrix validation → Baseline audit → Progressive disclosure → Content consolidation → Standards optimization → Validation → Recursive correction (max 3 iterations)

### Recursive Quality Correction Logic
**Threshold**: 85% minimum health score requirement
**Decision Tree**: Score ≥85% → Success | Score <85% + retry <3 → Retry | Score <85% + retry ≥3 → Escalation
**Error Context**: Health score, failed metrics, issue locations, correction focus, iteration count

### Auto-Execution Framework
**Mode Detection**: Error context → MAINTAIN | No context → DEFAULT | Audit → Analysis-only
**Quality Management**: 85% threshold, recursive optimization, focused corrections, Git tracking

### Progress Notifications
**Real-time Tracking**: Health score monitoring with threshold comparison (85%)
**Decision Logic**: SUCCESS/RETRY/ESCALATION based on score and iteration count
**Context Preparation**: Detailed error context for recursive execution
**Progress Monitoring**: Track improvement across correction iterations

### Automatic Learning Capture Protocol
**POST-WORKFLOW ASSESSMENT**: Documentation workflows auto-trigger /capture-learnings due to high complexity scores

**Integration**: Seamless workflow completion → learning capture → pattern documentation

## ⚡ Triggers

### Input Triggers
**Context**: Error context with health score <85% and specific file size violations
**Previous**: System health degradation or maintenance requirement
**Keywords**: maintain, optimize, progressive, disclosure

### Output Triggers  
**Success**: Health score ≥85% → System optimized and compliant
**Partial**: Improvement with pending issues → Retry recommendations
**Chain**: Orchestrates: audit → consolidate → optimize → validate

### Success Patterns
**Maintain Success**: Size compliance + health ≥85% → Standards achieved
**Disclosure Success**: Verbose content extracted → Core functionality preserved
**Quality Success**: Recursive optimization → Threshold satisfaction

## 🔗 See Also

### Implementation References
- `../docs/implementation/docs-workflow-implementation.md` - Complete workflow orchestration details
- `../docs/structure/project-organization-protocol.md` - Structural validation framework and organizational standards
- `../docs/documentation/simplicity-principles.md` - Progressive disclosure principles
- `../docs/documentation/writing-standards.md` - File size and optimization standards

### Related Commands
- Execute `/matrix-maintenance` for periodic cross-reference validation during workflow cycles
- Execute `/docs-audit` for isolated system health assessment
- Execute `/docs-consolidate` for targeted content optimization
- Execute `/docs-validate` for comprehensive system verification

---

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of complete documentation optimization workflow

```javascript
// COMPREHENSIVE DOCUMENTATION WORKFLOW ORCHESTRATION
// Execute full documentation optimization pipeline

// 1. WORKFLOW INITIALIZATION
// Structural validation and mode detection
Grep("health.*score|optimization|maintain", {glob: "context/**/*.md", output_mode: "content"}) // Detect mode
Bash("find . -name '*.md' | wc -l")                          // Count total markdown files
Bash("find docs/ -name '*.md' 2>/dev/null | wc -l || echo 0") // Check docs directory

// 2. AUDIT PHASE EXECUTION
// Deploy comprehensive documentation audit
Task("Documentation Audit", "Execute /docs-audit for comprehensive system health assessment and issue identification")

// 3. CONDITIONAL CONSOLIDATION
// Execute consolidation if duplication detected
Grep("duplication|duplicate|overlap", {glob: "context/**/*.md", output_mode: "files_with_matches"}) // Check for duplication issues
Task("Content Consolidation", "Execute /docs-consolidate if duplication >20% detected from audit results")

// 4. OPTIMIZATION PHASE
// Apply standards compliance and CLAUDE.md optimization
Task("Standards Optimization", "Execute /docs-optimize for CLAUDE.md compliance and system-wide standards application")

// 5. VALIDATION PHASE
// Comprehensive system health verification
Task("Final Validation", "Execute /docs-validate for cross-reference integrity and health score verification")

// 6. RECURSIVE CORRECTION LOGIC
// Health score assessment and correction cycles
Bash("echo 'scale=1; ([valid_references] * 100) / [total_references]' | bc") // Calculate health score

// 7. WORKFLOW RESULT DOCUMENTATION
Write("context/discoveries/docs-workflow-session-[timestamp].md", `# Documentation Workflow Results

## Workflow Execution Summary
- Mode: [workflow_mode]
- Health Score: Before [initial_score]% → After [final_score]%
- Files Processed: [file_count]
- Issues Resolved: [resolved_issues]
- Recursive Cycles: [cycle_count]

## Phase Execution Results
1. **Audit Phase**: [audit_results]
2. **Consolidation Phase**: [consolidation_results] 
3. **Optimization Phase**: [optimization_results]
4. **Validation Phase**: [validation_results]

## Quality Metrics
- Reference Integrity: [reference_percentage]%
- Size Compliance: [size_compliance]%
- Standards Adherence: [standards_percentage]%
- Navigation Efficiency: [navigation_score]/10

## Success Criteria Achievement
- Health Score ≥85%: [ACHIEVED/FAILED]
- Progressive Disclosure Applied: [YES/NO]
- Recursive Correction Complete: [YES/NO]
`)

// 8. AUTOMATED GIT INTEGRATION
// Track documentation workflow progress
Bash("echo 'Documentation workflow completed: health [final_score]% | cycles: [cycle_count]'")
Bash("echo 'Files optimized: [file_count] | standards compliance: [compliance_percentage]%'")

// 9. LEARNING VALUE ASSESSMENT
// Trigger capture-learnings if workflow complexity high
Bash("echo 'scale=1; ([workflow_complexity] + [issues_resolved] + [cycles_executed]) / 3' | bc") // Learning value
Task("Learning Assessment", "Evaluate workflow learning value: if complexity ≥4 points, trigger /capture-learnings")
```

### Workflow Orchestration Logic
**EXECUTION STRATEGY**:
- **Mode Detection**: Analyze context for maintain/default/audit mode
- **Phase Coordination**: Sequential audit → consolidation → optimization → validation
- **Quality Gates**: 85% health threshold for success, recursive correction if needed
- **Learning Integration**: Auto-trigger learning capture for complex workflows

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with workflow metrics (no Claude attribution)
Bash("git add . && git commit -m \"docs-workflow: [mode] | health: [initial]%→[final]% | cycles: [N] | session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Initialization**: 3 Grep + 2 Bash operations for mode detection
- **Phase orchestration**: 4 Task operations for command deployment
- **Assessment**: 1 Bash calculation for health scoring
- **Documentation**: 1 Write operation for results
- **Tracking**: 2 Bash operations for progress monitoring
- **Learning**: 1 Bash + 1 Task for learning assessment
- **Ratio**: 15 tool calls to ~100 documentation lines = 15% (HEALTHY)

---

**CRITICAL**: This command orchestrates complete documentation optimization with progressive disclosure application, recursive quality correction, and automated standards compliance.

**EXECUTION COMMITMENT**: Complete documentation workflow orchestration with audit, consolidation, optimization, and validation phases are NOW implemented with actual tool calls.