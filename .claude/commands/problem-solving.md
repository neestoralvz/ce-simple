# Problem-Solving - Universal Error Resolution Workflow

## 🎯 Purpose
Universal methodology for systematic problem resolution through structured diagnosis, comprehensive research, and progressive analysis leading to executable solution plans.

## 🚀 Usage
**Auto-Triggered**: Activated automatically when errors/problems detected
**Manual**: Execute `/problem-solving [error-description]`

## 🔧 Implementation

### Enhanced Behavioral Reinforcement Protocol
**MANDATORY at problem-solving initialization**:

```javascript
TodoWrite([
  {"content": "🔍 PHASE 0: Execute pre-solution structural assessment and mapping", "status": "pending", "priority": "high", "id": "solve-phase0-1"},
  {"content": "🗺️ STRUCTURAL: Generate cross-reference matrix and dependency analysis via /matrix-maintenance", "status": "pending", "priority": "high", "id": "solve-structural-1"},
  {"content": "📊 COMPLEXITY: Assess problem complexity and failure patterns", "status": "pending", "priority": "high", "id": "solve-complexity-1"},
  {"content": "🔗 INTEGRATION: Deploy explore-codebase + explore-web with validation protocols", "status": "pending", "priority": "high", "id": "solve-integration-1"},
  {"content": "🧠 ANALYSIS: Apply think-layers for multi-phase resolution planning", "status": "pending", "priority": "medium", "id": "solve-analysis-1"},
  {"content": "🛡️ PREVENTION: Generate risk assessment and mitigation strategies", "status": "pending", "priority": "medium", "id": "solve-prevention-1"},
  {"content": "✅ SOLUTION: Create executable solution plan with failure prevention", "status": "pending", "priority": "medium", "id": "solve-solution-1"}
])
```

**Problem-Adaptive Todos**: Add specific todos based on problem type and complexity discovered during diagnosis

### Enhanced Resolution Protocol
**Sequential Execution**: 6-phase methodology with mandatory structural assessment
**Integration**: Leverages cross-reference matrix and enhanced command integration
**Auto-Trigger**: Activated on error detection with failure prevention protocols
**Progressive Analysis**: Escalating depth with structural validation at each phase

### Enhanced Execution Framework
**Phase 0**: Pre-solution structural assessment and dependency mapping
**Phase 1**: Cross-reference matrix generation and failure pattern analysis
**Phase 2**: Enhanced internal context discovery using /explore-codebase with validation
**Phase 3**: Comprehensive external research using /explore-web with cross-validation
**Phase 4**: Multi-layer analysis using /think-layers with structural intelligence
**Phase 5**: Risk assessment and prevention planning with mitigation strategies
**Phase 6**: Executable solution planning with comprehensive failure prevention

### Structural Assessment Requirements
**MANDATORY Phase 0**: Before any solution implementation:
- Execute structural mapping of problem domain
- Generate dependency cross-reference matrix via `/matrix-maintenance validate`
- Validate exploration completeness using established protocols
- Assess risk factors and potential failure modes
- Document structural constraints and requirements

## ⚡ Triggers

### Input Triggers
**Auto-Error**: Automatic activation when problems/errors detected
**Manual**: Direct execution for proactive problem investigation
**Integration**: Called by other commands when resolution needed

### Output Triggers
**Solution Ready**: Executable plan generated → Implementation coordination
**Escalation**: Complex problems → Expert consultation recommended
**Learning**: Novel solutions → Automatic capture-learnings activation

### Success Patterns
**Resolution Success**: Root cause identified → Comprehensive solution planned
**Knowledge Integration**: External research → Internal context enhancement
**Methodology Validation**: Systematic approach → Consistent problem resolution

## 🔗 See Also

### Enhanced Implementation References
- `../docs/implementation/problem-solving-implementation.md` - Complete 6-phase methodology with Phase 0 protocols
- `../docs/methodology/cross-reference-matrix-framework.md` - FMEA implementation for software systems
- `../docs/methodology/structural-failure-prevention.md` - Prevention strategies and assessment protocols
- `../docs/workflow/workflow-notifications.md` - Problem-solving progress tracking standards
- `../docs/workflow/git-integration.md` - Solution deployment and error recovery protocols
- `../docs/maintenance/matrix-maintenance-implementation.md` - Auto-trigger matrix validation for structural assessment

### Enhanced Command Flow
1. **problem-solving** → STRUCTURAL-ASSESSMENT (Phase 0)
2. **CROSS-REF-MATRIX** → /explore-codebase + /explore-web (validated)
3. **VALIDATION-PROTOCOLS** → /think-layers (enhanced)
4. **PREVENTION-PLANNING** → Solution implementation

### Related Commands
- Execute `/matrix-maintenance` for cross-reference matrix validation and structural assessment
- Execute `/explore-codebase` with enhanced validation protocols for comprehensive internal discovery
- Execute `/explore-web` with cross-validation requirements for external research patterns
- Execute `/think-layers` with structural intelligence and prevention planning capabilities
- Execute `/capture-learnings` for enhanced solution pattern documentation with failure prevention insights

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of 6-phase problem-solving methodology with structural assessment

```javascript
// PHASE 0: PRE-SOLUTION STRUCTURAL ASSESSMENT
// Mandatory structural mapping before solution implementation

// Problem domain discovery
Grep("[problem-keywords]", {glob: "**/*.md", output_mode: "content", -C: 3})      // Find problem context
Grep("error|ERROR|fail|FAIL", {glob: "**/*.md", output_mode: "content", -n: true}) // Error pattern detection
Glob("**/[problem-domain]/**/*", {path: "."})                                      // Domain-specific files

// Cross-reference matrix generation via matrix-maintenance
Task("Matrix Validation", "Execute /matrix-maintenance validate for structural assessment and dependency mapping")

// Risk assessment and constraint analysis
Grep("constraint|limitation|requirement", {glob: "**/*.md", output_mode: "content"}) // Constraint discovery
Write("context/discoveries/problem-structural-assessment-[timestamp].md", `# Problem Structural Assessment

## Problem Domain Analysis
- Domain: [problem-domain]
- Scope: [problem-scope]
- Affected Components: [component-list]

## Dependency Matrix Results
[Matrix validation results from /matrix-maintenance]

## Structural Constraints
[Identified constraints and limitations]

## Risk Factors
[Potential failure modes and risk assessment]
`)

// PHASE 1: ENHANCED INTERNAL CONTEXT DISCOVERY
// Deploy explore-codebase with validation protocols
Task("Internal Discovery", "Execute /explore-codebase [problem-domain] with enhanced validation for comprehensive internal context discovery")

// PHASE 2: COMPREHENSIVE EXTERNAL RESEARCH  
// Deploy explore-web with cross-validation requirements
Task("External Research", "Execute /explore-web [problem-topic] with cross-validation for external research patterns and solutions")

// PHASE 3: MULTI-LAYER ANALYSIS WITH STRUCTURAL INTELLIGENCE
// Apply think-layers with structural intelligence
Task("Progressive Analysis", "Execute /think-layers [problem-analysis] with structural intelligence and prevention planning capabilities")

// PHASE 4: SOLUTION PATTERN DETECTION
// Analyze discovered solutions and patterns
Grep("solution|fix|resolve|workaround", {glob: "context/**/*.md", output_mode: "content", -C: 2}) // Solution extraction
Grep("success|working|effective", {glob: "context/**/*.md", output_mode: "content", -C: 2})      // Success patterns

// PHASE 5: RISK ASSESSMENT AND PREVENTION PLANNING
// Generate comprehensive prevention strategies
Write("context/discoveries/risk-prevention-analysis-[timestamp].md", `# Risk Assessment and Prevention Planning

## Identified Risk Factors
[Risk analysis from structural assessment]

## Prevention Strategies
[Mitigation strategies for identified risks]

## Failure Mode Analysis
[FMEA-based analysis of potential failure modes]

## Monitoring Requirements
[Ongoing monitoring and validation protocols]
`)

// PHASE 6: EXECUTABLE SOLUTION PLANNING
// Create comprehensive solution with failure prevention
Write("context/discoveries/solution-plan-[timestamp].md", `# Executable Solution Plan

## Problem Summary
- Root Cause: [root-cause-analysis]
- Impact Assessment: [impact-analysis]
- Resolution Priority: [priority-level]

## Solution Strategy
[Step-by-step solution implementation plan]

## Implementation Steps
1. [Step 1 with validation checkpoints]
2. [Step 2 with rollback procedures]
3. [Step 3 with success metrics]

## Failure Prevention
- Rollback Plan: [rollback-procedures]
- Monitoring: [success-metrics-tracking]
- Validation: [solution-verification-steps]

## Success Criteria
[Measurable success indicators]

## Learning Integration
[Pattern documentation for future problems]
`)

// COMPLEXITY ASSESSMENT
Bash("echo 'scale=1; ([problem_scope] + [affected_components] + [risk_level]) / 3' | bc") // Calculate problem complexity

// SOLUTION VALIDATION
Bash("echo 'Solution plan generated with [N] implementation steps'")
Bash("echo 'Risk factors identified: [N] with mitigation strategies'")
Bash("echo 'Prevention measures: [N] failure modes addressed'")

// LEARNING TRIGGER ASSESSMENT
// Auto-trigger capture-learnings for novel solutions
Task("Learning Assessment", "Evaluate learning value of solution: if novel/reusable ≥4 points, trigger /capture-learnings")
```

### Progressive Phase Logic
**EXECUTION STRATEGY**:
- **Phase 0**: Always execute structural assessment and matrix validation
- **Phase 1-2**: Deploy parallel exploration (codebase + web research)
- **Phase 3**: Progressive analysis based on discovered complexity
- **Phase 4-5**: Solution pattern detection and risk prevention
- **Phase 6**: Executable solution generation with failure prevention

### Auto-Trigger Integration
**ERROR DETECTION**:
```javascript
// When errors detected, auto-trigger problem-solving
if (error_detected) {
  Task("Problem Solving", "Execute /problem-solving [error-description] with full 6-phase methodology")
}
```

### Solution Validation Framework
**SOLUTION QUALITY METRICS**:
- Root cause identification completeness
- Implementation step clarity and detail  
- Risk prevention coverage and mitigation strategies
- Success criteria measurability and validation
- **Quality Threshold**: All metrics ≥80% for solution approval

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with problem-solving metrics (no Claude attribution)
Bash("git add . && git commit -m \"problem-solving: [problem-type] | phases: 6 | complexity: [N]/10 | session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Structural assessment**: 3 Grep + 1 Glob + 1 Task + 1 Write operations
- **Phase execution**: 4 Task operations for integrated command deployment
- **Solution generation**: 2 Grep + 2 Write operations for solution planning
- **Validation**: 3 Bash operations for complexity and success metrics
- **Learning integration**: 1 Task operation for capture-learnings trigger
- **Ratio**: 18 tool calls to ~200 documentation lines = 9% (HEALTHY)

---

**CRITICAL**: This workflow provides universal problem-solving methodology that integrates seamlessly with existing commands while leveraging established system capabilities. Auto-triggered on errors, manual execution for proactive investigation, with comprehensive solution planning through enhanced multi-layer analysis.

**EXECUTION COMMITMENT**: 6-phase problem-solving methodology with structural assessment, integrated command deployment, risk prevention, and executable solution planning are NOW implemented with actual tool calls.