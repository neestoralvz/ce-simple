# Start - Master Discovery & Workflow Orchestration Engine

## 🎯 Purpose
Intelligent workflow initialization with dynamic questioning, agent orchestration, and adaptive complexity assessment for optimal execution pathway determination.

## 🚀 Usage
Execute: `/start [initial-request]` 

**Auto-Detection**: Activates automatically for complex multi-step workflows
**Manual Execution**: Direct invocation for explicit workflow control

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at workflow initialization**:

```javascript
TodoWrite([
  {"content": "🎯 ASSESS: Analyze request complexity and determine optimal workflow pathway", "status": "pending", "priority": "high", "id": "start-assess-1"},
  {"content": "🤖 ORCHESTRATE: Deploy intelligent agent coordination for parallel analysis", "status": "pending", "priority": "high", "id": "start-orchestrate-1"},
  {"content": "❓ QUESTION: Execute dynamic questioning for context clarification", "status": "pending", "priority": "high", "id": "start-question-1"},
  {"content": "🚀 EXECUTE: Launch optimized execution pipeline based on analysis", "status": "pending", "priority": "high", "id": "start-execute-1"},
  {"content": "📊 MONITOR: Track workflow progress with real-time optimization", "status": "pending", "priority": "medium", "id": "start-monitor-1"}
])
```

### Structural Enforcement Protocol
**AUTO-EXECUTION**:
1. **🏗️ VALIDATE**: LS directories → Verify docs/, context/, .claude/ structure
2. **🔍 DETECT**: Glob/Grep → Find structural violations and outdated references
3. **🧠 PHILOSOPHY**: Execute `/self-monitor` compatibility gates → Prevent complexity reintroduction
4. **⚡ CORRECT**: Auto-fix violations → Migrate structure and update references
5. **✅ VERIFY**: Confirm corrections applied successfully

### Discovery Framework
**PHASE-BASED WORKFLOW**:
- **Phase 0**: Structural assessment and integrity validation
- **Phase 1**: Request analysis with complexity scoring (1-10 scale)
- **Phase 2**: Agent orchestration deployment for parallel analysis
- **Phase 3**: Dynamic questioning for context clarification
- **Phase 4**: Execution pathway optimization and launch

### Complexity Assessment Matrix
**AUTO-TRIGGER THRESHOLDS**:
- **Complexity ≥6**: Auto-trigger `/worktree-start` for isolated development
- **Analysis Required**: Auto-deploy `/agent-orchestration` for intelligence coordination
- **Multi-Domain**: Deploy `/explore-codebase` + `/explore-web` for comprehensive analysis
- **Learning Value ≥4**: Auto-trigger `/capture-learnings` for pattern documentation

### Dynamic Questioning Engine
**INTELLIGENT CONTEXT CLARIFICATION**:
- **Request Scope**: Determine breadth and depth requirements
- **Technical Context**: Identify technology stack and architectural constraints
- **Success Criteria**: Define measurable outcomes and validation requirements
- **Timeline & Resources**: Assess urgency and resource allocation needs

**DETAILED IMPLEMENTATION**: Complete workflow specifications and questioning algorithms in `docs/commands/start-implementation.md`

## ⚡ Triggers

### Input Triggers
**Context**: New project requests, complex problem solving, multi-step workflows
**Auto-Activation**: Commands detecting complexity ≥6 or requiring workflow coordination
**Keywords**: start, begin, workflow, complex, multi-step, coordination

### Output Triggers
**When**: Complexity ≥6 → `/worktree-start` for isolated development environment
**When**: Analysis required → `/agent-orchestration` for intelligent coordination
**When**: Learning value ≥4 → `/capture-learnings` for pattern documentation
**Chain**: start → [worktree-start] → agent-orchestration → explore-* → execution → capture-learnings

### Success Patterns
**Workflow Success**: Optimal execution pathway selected and launched successfully
**Intelligence Success**: Agent coordination provides comprehensive analysis and recommendations
**Efficiency Success**: Dynamic questioning minimizes iteration cycles and maximizes clarity

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Complete workflow initialization with structural validation and intelligent orchestration

```javascript
// 1. STRUCTURAL VALIDATION & ENFORCEMENT
LS(".") // Verify root directory structure
LS("docs") // Verify documentation structure
LS("context") // Verify context organization
LS(".claude") // Verify command system structure

// 2. STRUCTURAL INTEGRITY DETECTION
Glob("**/*.md", {path: "docs"}) // Document inventory
Glob("**/*.md", {path: "context"}) // Context file inventory
Glob("**/*.md", {path: ".claude/commands"}) // Command inventory
Grep("docs/commands/", {glob: "**/*.md", output_mode: "files_with_matches"}) // Detect obsolete references

// 3. AUTO-CORRECTION EXECUTION
Edit("[file-with-violation]", "[corrected-content]") // Fix structural violations
Bash("find . -name '*.md' -exec grep -l 'obsolete-pattern' {} + | wc -l") // Count violations

// 4. COMPLEXITY ASSESSMENT
Grep("complex|workflow|multi-step|coordination", {glob: "**/*.md", output_mode: "count"}) // Complexity indicators
Bash("echo 'Complexity assessment: [score]/10 | Triggers: [trigger_list]'") // Assessment summary

// 5. AGENT ORCHESTRATION DEPLOYMENT
Task("Agent Orchestration", "Execute /agent-orchestration with request analysis and complexity matrix for intelligent coordination")

// 6. DYNAMIC QUESTIONING EXECUTION
Write("context/workflows/dynamic-questions-[timestamp].md", `# Dynamic Questions: [request]

## Request Analysis
- **Complexity Score**: [score]/10
- **Domain**: [domain_list]
- **Required Analysis**: [analysis_types]

## Context Clarification Questions
[Generated dynamic questions based on request analysis]

## Success Criteria
[Measurable outcomes and validation requirements]

**Session**: [session_id] | **Timestamp**: [current_time]`)

// 7. WORKFLOW PATHWAY OPTIMIZATION
Bash("if [[ [complexity_score] -ge 6 ]]; then echo 'AUTO-TRIGGER: /worktree-start for isolated development'; fi")
Task("Worktree Management", "Execute /worktree-start if complexity ≥6 for isolated development environment")

// 8. EXECUTION PIPELINE LAUNCH
Task("Execution Coordination", "Launch optimized execution pipeline: [pathway] with agent coordination and monitoring")

// 9. MONITORING & OPTIMIZATION
Bash("echo 'Workflow initialized: [workflow_type] | Complexity: [score] | Agents: [agent_count] | ETA: [estimate]'")
Write("context/workflows/execution-plan-[timestamp].md", `# Execution Plan: [request]

## Workflow Configuration
- **Pathway**: [selected_pathway]
- **Complexity**: [score]/10
- **Agent Coordination**: [coordination_type]
- **Expected Commands**: [command_sequence]

## Real-Time Optimization
- **Progress Tracking**: [tracking_method]
- **Adaptation Triggers**: [adaptation_conditions]
- **Success Metrics**: [success_criteria]

**Initialized**: [timestamp] | **Session**: [session_id]`)

// 10. COMPLETION & HANDOFF
Bash("git add . && git commit -m 'start: [request-summary] | complexity: [score] | pathway: [pathway] ✓session-[id]'")
```

### Workflow Optimization Logic
**INTELLIGENT PATHWAY SELECTION**:
- **Simple (1-3)**: Direct execution with minimal coordination
- **Moderate (4-5)**: Standard workflow with agent assistance
- **Complex (6-7)**: Worktree isolation + comprehensive agent orchestration
- **Critical (8-10)**: Full system coordination with predictive analysis

### Session Management Integration
**WORKFLOW LIFECYCLE**:
- **Initialization**: Session setup with complexity assessment
- **Execution**: Coordinated command execution with real-time monitoring
- **Adaptation**: Dynamic pathway adjustment based on discoveries
- **Completion**: Session closure with learning capture and optimization

### Execution Verification
**TOOL CALL SUMMARY**: 10 tool operations implementing complete workflow initialization
- **Validation**: 4 LS operations for structural verification
- **Discovery**: 4 Glob/Grep operations for inventory and violation detection
- **Optimization**: 2 Task operations for orchestration and execution coordination

---

**CRITICAL**: This command ensures systematic workflow initialization with structural integrity, intelligent coordination, and adaptive optimization for maximum execution effectiveness.

**EXECUTION COMMITMENT**: All workflow initialization, structural validation, and orchestration operations implemented with actual tool calls for systematic coordination.