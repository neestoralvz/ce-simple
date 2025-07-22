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

**CRITICAL**: This command orchestrates complete documentation optimization with progressive disclosure application, recursive quality correction, and automated standards compliance.