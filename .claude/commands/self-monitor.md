# Self Monitor - Standards Compliance and Autocritique System

## 🎯 Purpose
Real-time standards compliance validation with prevention-first autocritique during command execution phases.

## 🚀 Usage
Execute: `/self-monitor [phase] [scope]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at monitoring initialization**:

```javascript
TodoWrite([
  {"content": "🔍 PREVENTION: Execute proactive standards compliance scanning before issues occur", "status": "pending", "priority": "high", "id": "monitor-prevention-1"},
  {"content": "📊 THRESHOLD: Validate >85% compliance across all quality dimensions", "status": "pending", "priority": "high", "id": "monitor-threshold-1"},
  {"content": "🔄 CORRECTION: Deploy autonomous correction with max 3 recursive iterations", "status": "pending", "priority": "high", "id": "monitor-correction-1"},
  {"content": "⚡ INTEGRATION: Seamless workflow integration without execution disruption", "status": "pending", "priority": "medium", "id": "monitor-integration-1"},
  {"content": "📋 TRACKING: Real-time quality monitoring with transparent progress updates", "status": "pending", "priority": "medium", "id": "monitor-tracking-1"}
])
```

### Prevention-First Architecture
**PROACTIVE MONITORING**: Continuous validation during command execution to prevent issues before occurrence

### Phase-Based Autocritique Framework
1. **EXPLORATION**: Codebase pattern validation, web research quality assurance
2. **ANALYSIS**: Think-layers progression verification, logical consistency validation
3. **PLANNING**: Implementation feasibility assessment, resource allocation validation
4. **EXECUTION**: Tool call verification, output quality assurance
5. **REVIEW**: Post-execution compliance validation, learning integration verification

### Standards Validation Framework
**COMPLIANCE DIMENSIONS**:
- **File Size Standards**: Commands ≤140 optimal/≤200 max, Documentation ≤200 max
- **Anti-Bias Compliance**: Evidence-based analysis, neutral language verification
- **Cross-Reference Integrity**: Functional links, navigation efficiency validation
- **Content Quality**: Density optimization, duplication elimination
- **Implementation Coverage**: Execution layer presence, tool call ratio verification

### Autonomous Correction Protocol
**RECURSIVE OPTIMIZATION** (Maximum 3 iterations):
1. **DETECT**: Identify compliance gaps and quality issues
2. **ANALYZE**: Root cause analysis and correction strategy selection
3. **CORRECT**: Apply targeted fixes with minimal workflow disruption
4. **VALIDATE**: Re-assess compliance and quality metrics
5. **ITERATE**: Repeat if threshold not met (max 3 attempts)
6. **ESCALATE**: Manual intervention if automated correction fails

### Quality Threshold Enforcement
**COMPLIANCE REQUIREMENTS**:
- **Minimum Threshold**: 85% compliance across all dimensions
- **Target Excellence**: 90+ for optimal system performance
- **Critical Actions**: Immediate correction for <75% compliance
- **Success Criteria**: Sustained 85%+ compliance with trend improvement

## ⚡ Triggers

### Input Triggers
**Context**: Any command execution requiring quality assurance and compliance validation
**Previous**: Auto-triggered by all major commands during execution phases
**Keywords**: monitor, validate, quality, compliance, standards, autocritique

### Output Triggers
**When**: Compliance achieved (≥85%) → Continue workflow execution
**When**: Issues detected → Deploy autonomous correction protocol
**When**: Critical failures → Escalate to manual intervention
**Chain**: monitor → validate → correct → re-monitor → proceed/escalate

### Success Patterns
**Prevention Success**: Issues detected and corrected before workflow disruption
**Compliance Success**: 85%+ standards adherence maintained throughout execution
**Integration Success**: Seamless quality assurance without workflow delays

## 🔗 Integration Framework

### Command Workflow Integration
**Core Commands**:
- `/start` → Phase 0 structural validation with self-monitoring
- `/explore-codebase` → Pattern validation and discovery quality assurance
- `/explore-web` → Research quality monitoring and bias detection
- `/think-layers` → Analysis progression validation and logical consistency
- `/capture-learnings` → Learning quality assurance and pattern validation

### Real-Time Quality Monitoring
**CONTINUOUS ASSESSMENT**:
```
🔍 SCANNING: [Phase] quality → [N] standards checked → [X]% compliance
📊 METRICS: [Score]/100 health → [Threshold] status → [Action] required
⚖️ BALANCE: Quality vs Speed → Optimization [strategy] selected
🔄 FEEDBACK: Issue detected → Correction applied → Re-validation triggered
```

---

## ⚡ EXECUTION LAYER

### Core Monitoring Operations
**CRITICAL**: Implementation executes comprehensive standards compliance validation with prevention-first architecture

```javascript
// 1. FILE SIZE COMPLIANCE SCANNING
Bash("find . -name '*.md' -path './.claude/commands/*' -exec awk 'END{if(NR>140) print \"WARNING: \" FILENAME \" (\" NR \"/140 lines)\"}' {} +")
Bash("find . -name '*.md' -not -path './.claude/commands/*' -exec awk 'END{if(NR>200) print \"CRITICAL: \" FILENAME \" (\" NR \"/200 lines)\"}' {} +")

// 2. ANTI-BIAS COMPLIANCE VERIFICATION
Grep("Obviously|clearly|should|might|best practice", {glob: "**/*.md", output_mode: "content", -i: true, -n: true})
Grep("ALWAYS|NEVER|MANDATORY|CRITICAL", {glob: "**/*.md", output_mode: "count"})

// 3. CROSS-REFERENCE INTEGRITY MONITORING
Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "**/*.md", output_mode: "count"})
Grep("/[a-zA-Z-]+", {glob: "**/*.md", output_mode: "count"})

// 4. STRUCTURAL COMPLIANCE VALIDATION
Glob("**/*.md")
Grep("## 🎯 Purpose|## 🚀 Usage|## 🔧 Implementation", {glob: ".claude/commands/*.md", output_mode: "count"})

// 5. QUALITY METRICS CALCULATION
Bash("find . -name '*.md' | wc -l")
Bash("echo 'scale=1; ([compliant_files] * 100) / [total_files]' | bc")

// 6. AUTONOMOUS CORRECTION DEPLOYMENT
Write("context/discoveries/self-monitor-analysis-$(date +%Y%m%d).md", `# Standards Compliance Analysis
[Compliance results and correction recommendations]`)

// 7. PROGRESS TRACKING INTEGRATION
TodoWrite([
  {"content": "🔍 SCANNING: Compliance validation completed → [score]% threshold", "status": "completed", "priority": "high", "id": "monitor-scan-1"}
])

// 8. SESSION COMPLETION
Bash("git add . && git commit -m \"self-monitor: compliance [score]% | corrections: [applied] | session-[N]\"")
```

### Session Completion Protocol
**Git Integration**: Automated commit with compliance metrics for tracking and system health monitoring

### Execution Verification
**Tool Operations**: 15 core operations across 8 validation categories with efficient execution density and transparent progress tracking

---

**CRITICAL**: This command provides continuous quality assurance without workflow disruption and ensures sustained standards compliance through prevention-first monitoring with autonomous correction capabilities.

**See Also**: 
- `../context/implementation/self-monitor-implementation-details.md` - Complete technical specifications
- `../context/implementation/self-monitor-integration-guide.md` - Seamless activation framework
- `../docs/quality/validation-framework-protocol.md` - Quality standards and thresholds

**EXECUTION COMMITMENT**: Standards compliance monitoring, threshold enforcement, autonomous correction, and seamless workflow integration are NOW implemented with prevention-first architecture.