# Documentation Workflow Implementation Standards

## 🎯 Implementation Architecture

### Complete Workflow Protocol
1. **PLAN GENERATION** (if todo plans detected): Execute `/docs-generate` for new documents
2. **AUTO-EXPLORATION** (if no todo plans): Execute `/explore-codebase` for context-aware optimization
3. **BASELINE AUDIT**: Initial system health assessment and issue identification  
4. **CONTENT CONSOLIDATION**: Automated duplication resolution and reference repair
5. **STANDARDS OPTIMIZATION**: CLAUDE.md optimization and compliance enforcement
6. **INTEGRITY VALIDATION**: Comprehensive verification and health score calculation
7. **RECURSIVE CORRECTION**: Auto-retry if quality threshold not met (max 3 iterations)

### Automated Orchestration Framework

#### Mode-Specific Execution Logic
**DEFAULT Mode**: Complete pipeline with generation
**AUDIT Mode**: Analysis only, no system modifications
**MAINTAIN Mode**: Optimization without generation

**Phase 0: Plan Generation** (Default mode only)
```
📝 GENERATE: Detecting todo plans → Executing /docs-generate
⚡ WAVE-1: [N] document agents deployed → Parallel creation
🔗 WAVE-2: Cross-references integrated → Bidirectional linking
✅ WAVE-3: Initial validation → Quality gates verified
```

**Phase 0B: Auto-Exploration** (When no todo plans detected)
```
🔍 EXPLORE: No todo plans detected → Executing /explore-codebase
📊 CONTEXT: Analyzing codebase structure and implementation status
🎯 SCOPE: Identifying documentation optimization targets
✅ BASELINE: Context-aware workflow configuration prepared
```

**Phase 1: Documentation Audit**
```
🔍 AUDIT: Executing comprehensive system analysis...
📊 BASELINE: Health score [X]/100, [Y] issues identified
📋 ISSUES: [Critical/Warning/Info breakdown]
```

**Phase 2: Content Consolidation**
```
🔧 CONSOLIDATE: Resolving content duplication and reference issues...
📄 DUPLICATION: [X]% → [Y]% content overlap reduction
🔗 REFERENCES: [X] broken links repaired, [Y]% functional rate achieved
```

**Phase 3: Standards Optimization**
```
⚡ OPTIMIZE: Applying CLAUDE.md and system compliance standards...
📏 SIZE COMPLIANCE: [X] files optimized, [Y]% compliance achieved
🎯 CLAUDE.MD: Token efficiency improved by [X]%
```

**Phase 4: System Validation**
```
✅ VALIDATE: Comprehensive system health verification...
🔍 INTEGRITY: [X]% reference health, [Y] cognitive steps navigation
📊 FINAL SCORE: [X]/100 health score (improvement: +[Y] points)
```

### Workflow Execution Logic

#### Recursive Quality Correction
**AUTO-RETRY Logic**: Execute up to 3 correction cycles for quality threshold achievement

**Threshold Validation**:
```
📊 FINAL-SCORE: Health score [X]/100 → Threshold: 85% minimum
🔄 DECISION: [Score < 85%] → Deploy /docs-workflow maintain with error context
⚡ RETRY-[N]: Corrective workflow initiated → Focus: [specific failed areas]
✅ SUCCESS: Quality threshold achieved → Workflow completed
```

**Error Context Transmission**:
- **Failed Metrics**: Specific measurements below threshold
- **Issue Locations**: Exact files and sections requiring correction
- **Correction Focus**: Targeted improvement areas for next iteration

**Success Criteria Validation**:
- **Quality Score ≥85%**: Workflow completion with success report + Git tracking
- **Max Iterations Reached**: Manual intervention recommended with detailed analysis
- **Critical Failures**: Immediate escalation with preservation of system state

#### Git Integration Protocol
**SESSION-COMPLETION Tracking**: Automatic commit generation on successful workflow completion

**Success Commit Structure**:
```bash
git add . && git commit -m "docs-workflow: [mode] optimization completed

📊 EXECUTION METRICS:
- Mode: [Default/Audit/Maintain]
- Duration: [X] minutes
- Health Score: [before]% → [after]% (+[delta]%)
- Files Modified: [N] files

🎯 PHASE RESULTS:
$(if_generation_executed)
- Audit: [X] issues identified → [Y] resolved
- Consolidation: [X]% duplication reduction
- Optimization: [X]% standards compliance
- Validation: [X]% reference integrity

🔄 QUALITY MANAGEMENT:
- Recursive iterations: [N]/3
- Final quality score: [X]%
- Threshold status: [Achieved/Exceeded]
- System stability: [Status]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

**Error Recovery Commit** (if partial success):
```bash
git add . && git commit -m "docs-workflow: [mode] partial completion

⚠️ EXECUTION STATUS: Partial success with [X] unresolved issues
📊 Achieved: [list of completed phases]
🔧 Pending: [list of pending issues]
🎯 Next Steps: [recommended actions]

🤖 Generated with Claude Code - Partial Execution
Co-Authored-By: Claude <noreply@anthropic.com>"
```

### Comprehensive Reporting Framework

#### Workflow Execution Summary
**Final Report Generation**:
```
📊 DOCUMENTATION WORKFLOW COMPLETION REPORT

🎯 OVERALL RESULTS:
Health Score: [X]/100 → [Y]/100 (improvement: +[Z] points)
Issues Resolved: [X] critical, [Y] warning, [Z] info
Execution Time: [X] minutes for complete optimization

📋 PHASE BREAKDOWN:
✅ AUDIT: [X] files analyzed, [Y] issues identified
✅ CONSOLIDATE: [X]% duplication reduced, [Y] references repaired  
✅ OPTIMIZE: [X] files resized, [Y]% compliance achieved
✅ VALIDATE: [X]% reference integrity, [Y] cognitive steps navigation

🎯 RECOMMENDATIONS:
[Specific suggestions for ongoing maintenance]
[Areas for future optimization]
[System health monitoring guidelines]
```

#### Issue Resolution Tracking
**Detailed Change Log**:
- **Files Modified**: Complete list with before/after line counts
- **References Updated**: Broken links repaired and new connections created
- **Content Consolidated**: Duplication elimination and optimization details
- **Standards Applied**: Compliance improvements and policy enforcement

### Quality Assurance Integration

#### Pre-Execution Validation
**System State Verification**:
- **Backup Recommendation**: Suggest git commit before workflow execution
- **Dependency Check**: Verify all required files and references accessible
- **Permission Validation**: Ensure write access to all documentation directories
- **Baseline Capture**: Record initial state for comparison and rollback

#### Post-Execution Verification
**Comprehensive Quality Gates**:
- **Functional Testing**: Verify all cross-references operational
- **Content Integrity**: Confirm no information loss during optimization
- **Performance Validation**: Measure navigation efficiency improvements
- **Compliance Confirmation**: Validate adherence to all established standards

### Usage Optimization

#### Execution Modes
**Standard Mode** (Default):
- Complete workflow execution with detailed reporting
- Interactive confirmation for critical changes
- Comprehensive validation and verification

**Express Mode** (`/docs-workflow express`):
- Automated execution with minimal interaction
- Essential reporting only
- Optimized for routine maintenance

**Audit-Only Mode** (`/docs-workflow audit`):
- Execute only audit phase for health assessment
- No modifications to system
- Baseline reporting for planning purposes

---

**REFERENCE**: Detailed implementation standards for /docs-workflow command execution. Referenced from `.claude/commands/docs-workflow.md` for progressive disclosure optimization.