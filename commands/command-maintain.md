# Command-Maintain - Automated Command System Maintenance

## 🎯 Purpose
Comprehensive automated command maintenance system with proactive guardrails, standards enforcement, and workflow efficiency optimization.

## 🚀 Usage
Execute: `/command-maintain [mode: audit|repair|optimize|full]`

**Default**: `full` mode - Complete maintenance cycle
**Modes**: 
- `audit` - Analysis and reporting only
- `repair` - Fix standard violations
- `optimize` - Size and complexity optimization  
- `full` - Complete maintenance cycle

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at maintenance initialization**:

```javascript
TodoWrite([
  {"content": "🔍 AUDIT: Systematic analysis of all commands against documented standards", "status": "pending", "priority": "high", "id": "maintain-audit-1"},
  {"content": "📊 ANALYZE: Complexity scoring, size violations, execution deficit detection", "status": "pending", "priority": "high", "id": "maintain-analyze-1"},
  {"content": "🔧 REPAIR: Automated fixes for standard violations and compliance issues", "status": "pending", "priority": "high", "id": "maintain-repair-1"},
  {"content": "⚙️ OPTIMIZE: File size reduction and execution layer implementation", "status": "pending", "priority": "medium", "id": "maintain-optimize-1"},
  {"content": "✅ VALIDATE: Comprehensive verification of maintenance improvements", "status": "pending", "priority": "medium", "id": "maintain-validate-1"},
  {"content": "📋 REPORT: Generate maintenance summary and compliance status", "status": "pending", "priority": "low", "id": "maintain-report-1"}
])
```

### Standards Compliance Audit Protocol
**MANDATORY first phase execution**:

1. **📏 SIZE VALIDATION**: Verify ≤150 line limits (`docs/core/writing-standards.md`)
2. **🧠 COMPLEXITY SCORING**: Apply scoring matrix (`context/dev/command-complexity-matrix.md`) 
3. **⚡ EXECUTION AUDIT**: Detect documentation theater (3:1 tool ratio required)
4. **🚫 ANTI-BIAS CHECK**: Validate compliance (`docs/core/anti-bias-enforcement.md`)
5. **📋 TEMPLATE VALIDATION**: Check structure (`docs/commands/command-template.md`)

### Automated Repair Framework
**CRITICAL violations requiring immediate fix**:

- **File Size Violations**: Commands >150 lines → Progressive disclosure extraction
- **Documentation Theater**: Missing execution layers → Add tool call implementations
- **Template Non-Compliance**: Missing sections → Add required structure
- **Cross-Reference Failures**: Broken links → Validate and repair references
- **Anti-Bias Violations**: Rule violations → Implement compliance measures

### Proactive Guardrails & Workflow Optimization
**REAL-TIME ENFORCEMENT**: File size (≤150), complexity (≤7.0), execution ratio (3:1), template compliance, anti-bias rules
**EFFICIENCY FEATURES**: Batch operations, parallel execution, smart defaults, progress tracking
**REFERENCE**: `docs/commands/command-maintain-implementation.md` for detailed specifications

## ⚡ Triggers

### Input/Output Chain
**Input**: Scheduled maintenance, violations detected, user request
**Output**: `/matrix-maintenance` → `/context-optimize` → validation complete
**Success**: >95% compliance, file sizes <150 lines, complexity <7.0

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Essential automation with full implementation details in `docs/commands/command-maintain-implementation.md`

```javascript
// 1. AUDIT PHASE (4 operations)
LS(".claude/commands") // List command files
Bash("find .claude/commands -name '*.md' -exec wc -l {} + | sort -nr") // Size audit
Grep("EXECUTION LAYER", {glob: ".claude/commands/*.md", output_mode: "count"}) // Theater detection
Bash("wc -l .claude/commands/*.md | awk '{if($1>150) print $2, $1}'") // Violations

// 2. REPAIR PHASE (variable based on violations)
Edit("[oversized-command].md", "[progressive-disclosure-content]") // Size reduction
Edit("[theater-command].md", "[execution-layer-content]") // Add tool calls

// 3. REPORTING & INTEGRATION (3 operations)
Bash("echo 'MAINTENANCE REPORT: Commands:' $(ls .claude/commands/*.md | wc -l) 'Violations:' $(wc -l .claude/commands/*.md | awk '$1>150' | wc -l)") // Metrics
Task("Matrix Maintenance", "Execute /matrix-maintenance for system validation")
Bash("git add . && git commit -m \"command-maintain: compliance: [X]% | violations-fixed: [N] ✓maintenance\"")
```

### Execution Modes
**`audit`**: Analysis only with compliance report
**`repair`**: Fix violations (size, theater, template, references)  
**`optimize`**: Advanced optimization with guardrail implementation
**`full`** (default): Complete cycle with `/matrix-maintenance` integration

**TOOL RATIO**: 7+ operations minimum ensures execution over documentation

---

**CRITICAL**: This command implements the user-requested automated maintenance system following ALL documented standards. Every maintenance operation uses actual tool executions with comprehensive verification protocols.

**EXECUTION COMMITMENT**: Complete command system maintenance with proactive guardrails, standards enforcement, and workflow efficiency optimization NOW implemented with verified tool calls.