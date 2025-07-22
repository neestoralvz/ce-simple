# Docs Workflow - Complete Documentation Optimization Workflow

## 🎯 Purpose
Execute comprehensive documentation optimization workflow through automated orchestration of audit, consolidation, optimization, and validation phases.

## 🚀 Usage
Execute: `/docs-workflow [mode]`
- **Default**: Complete pipeline (generate + optimize + validate)
- **audit**: Analysis only, no modifications
- **maintain**: Optimize existing docs without generation

## 🔧 Implementation

### Workflow Execution Protocol
**MAINTAIN Mode**: Apply progressive disclosure to oversized command files
```
🔧 PROGRESSIVE DISCLOSURE: Apply size optimization to files exceeding 140-line target
📏 EXTRACT: Verbose implementation details → Referenced standards files
⚡ OPTIMIZE: Maintain core functionality within optimal line limits
📊 VALIDATE: Achieve ≥85% health score through systematic optimization
```

**Execution Phases**:
1. **BASELINE AUDIT**: Health score assessment and issue identification
2. **PROGRESSIVE DISCLOSURE**: Extract verbose content to referenced files  
3. **CONTENT CONSOLIDATION**: Optimize duplication and reference integrity
4. **STANDARDS OPTIMIZATION**: Apply size compliance and token efficiency
5. **VALIDATION**: Comprehensive verification and quality measurement
6. **RECURSIVE CORRECTION**: Auto-retry if threshold not achieved (max 3 iterations)

### Recursive Quality Correction Logic
**AUTOMATIC EXECUTION**: After Phase 5 (Validation), evaluate health score and initiate correction cycles

**Threshold Validation Protocol**:
```
📊 HEALTH-CHECK: Extract numeric score from validation results
🎯 THRESHOLD: Compare score against 85% minimum requirement
🔄 DECISION-TREE:
  - Score ≥85% → ✅ SUCCESS: Workflow completion with final report
  - Score <85% AND retry_count <3 → ⚡ RETRY: Execute correction iteration
  - Score <85% AND retry_count ≥3 → ⚠️ ESCALATION: Manual intervention required

🧠 AUTO-RETRY Logic: /docs-workflow maintain with comprehensive error context
⚡ RETRY-[N]: Corrective workflow → Focus specific failed metrics → Re-validate
```

**Error Context Transmission Framework**:
```
ERROR CONTEXT FROM ITERATION-[N]:
- Health Score: [current]% ([points] below 85% threshold)  
- Failed Metrics: [specific measurements below standard]
- Issue Locations: [exact files and violations identified]
- Correction Focus: [targeted improvement areas for next iteration]
- Iteration: RETRY-[N] of maximum 3 iterations
```

### Auto-Execution Framework
**Mode Detection**:
- **Error Context Detected**: Execute MAINTAIN mode with focused corrections
- **No Context**: Execute comprehensive DEFAULT workflow
- **Audit Requested**: Analysis-only execution with baseline establishment

**Quality Threshold Management**:
```
📊 THRESHOLD: 85% minimum health score requirement
🔄 RETRY: Recursive optimization until threshold achieved
⚡ FOCUS: Target specific failed metrics from error context
✅ SUCCESS: System optimization complete with Git tracking
```

### Recursive Execution Notifications
**Real-time Progress Tracking**:
```
📊 FINAL-SCORE: Health score [X]/100 → Threshold: 85% minimum
🔄 DECISION: [Score < 85%] → Deploy /docs-workflow maintain with error context
⚡ RETRY-[N]: Corrective workflow initiated → Focus: [specific failed areas]
🎯 ITERATION: [N]/3 maximum → Targeting [failed metrics]
📈 PROGRESS: [previous]% → [current]% ([+/-X] points)
✅ SUCCESS: Quality threshold achieved → Workflow completed
⚠️ ESCALATION: Max iterations reached → Manual intervention required
```

**Automatic Delegation Protocol**:
1. **Validation Complete** → Extract health score from results
2. **Threshold Check** → Compare against 85% minimum requirement  
3. **Decision Logic** → Determine SUCCESS/RETRY/ESCALATION path
4. **Context Preparation** → Generate detailed error context for retry
5. **Recursive Execution** → Launch `/docs-workflow maintain` with context
6. **Progress Monitoring** → Track improvement across iterations
7. **Final Resolution** → Report success or escalation status

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
- `../../standards/docs-workflow-implementation.md` - Complete workflow orchestration details
- `../../standards/simplicity-principles.md` - Progressive disclosure principles
- `../../standards/writing-standards.md` - File size and optimization standards

### Related Commands
- Execute `/docs-audit` for isolated system health assessment
- Execute `/docs-consolidate` for targeted content optimization
- Execute `/docs-validate` for comprehensive system verification

---

**CRITICAL**: This command orchestrates complete documentation optimization with progressive disclosure application, recursive quality correction, and automated standards compliance.