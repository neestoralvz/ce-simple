# Start - Discovery Workflow Master

## 🎯 Purpose
Initialize discovery workflow with dynamic questioning and automated agent orchestration.

## 🚀 Usage
Execute: `/start [optional: initial request]`

## 🔧 Implementation

### Autocontained Notification System
```bash
#!/bin/bash
# NOTIFICATION SYSTEM - Functional colors + unique emoticons
readonly B='\e[34m' G='\e[32m' R='\e[31m' Y='\e[33m' C='\e[36m' M='\e[35m' GB='\e[32;1m' N='\e[0m'
info()     { echo -e "${B}🔵 INFO${N}: $1"; }
success()  { echo -e "${G}🟢 SUCCESS${N}: $1"; }  
error()    { echo -e "${R}🔴 ERROR${N}: $1"; }
warn()     { echo -e "${Y}🟡 WARNING${N}: $1"; }
process()  { echo -e "${C}⚡ PROCESS${N}: $1"; }
data()     { echo -e "${M}📊 DATA${N}: $1"; }
complete() { echo -e "${GB}✅ COMPLETE${N}: $1"; }
calc()     { echo "scale=${2:-2}; $1" | bc -l; }
progress() { local p=$(calc "$1*100/$2" 0); process "$3 [$p% complete]"; }
```

### Behavioral Reinforcement Protocol  
**MANDATORY at command initialization**:

```javascript
TodoWrite([
  {"content": "🏗️ PHASE-0: Execute mandatory structural assessment with validation protocols", "status": "pending", "priority": "high", "id": "start-phase0-1"},
  {"content": "📊 THRESHOLD: Verify 85% completeness before agent deployment", "status": "pending", "priority": "high", "id": "start-threshold-1"},
  {"content": "🤖 ORCHESTRATION: Deploy agents only after Phase 0 validation gates passed", "status": "pending", "priority": "high", "id": "start-orchestration-1"},
  {"content": "⚠️ FAILURE-PREVENTION: Generate comprehensive failure mode analysis", "status": "pending", "priority": "high", "id": "start-prevention-1"},
  {"content": "📋 MONITORING: Track validation checkpoint progress", "status": "pending", "priority": "medium", "id": "start-monitoring-1"}
])
```

**Progressive Todo Management**: Mark todos as completed in real-time as actions are executed for complete user transparency

### Structural Enforcement Protocol
**AUTO-EXECUTION**:
1. **🏗️ VALIDATE**: LS directories → Verify docs/, context/, .claude/ structure
2. **🔍 DETECT**: Glob/Grep → Find structural violations and outdated references
3. **⚡ CORRECT**: Auto-fix violations → Migrate structure and update references
4. **✅ VERIFY**: Confirm corrections applied successfully

### Discovery Protocol
1. **VALIDATE**: Execute structural pre-validation
2. **CAPTURE**: Analyze user input complexity
3. **QUESTION**: Generate contextual clarification queries
4. **ASSESS**: Determine context sufficiency
5. **ORCHESTRATE**: Deploy parallel/sequential agents
6. **TRACK**: Maintain workflow notifications

### Workflow Orchestration Framework

#### Agent Orchestration Integration
**Auto-Triggered**: Deploy `/agent-orchestration` module for intelligent coordination
**Parameters**: Request complexity, context sufficiency, exploration requirements
**Output**: Optimized agent deployment strategy with execution timeline

#### Phase 1: Discovery & Context Building
**Framework**:
```
⟳ /start → structural validation → complexity analysis → /agent-orchestration → dynamic questions → context validation → agent deployment
```

**Dynamic Questions Engine**:
- **Objective**: "What specific outcome do you need?"
- **Scope**: "What are the boundaries of this request?"
- **Context**: "What information should I understand?"
- **Priority**: "What elements are most critical?"

#### Phase 2: Intelligent Agent Deployment
**Complexity-Based Strategy** (via `/agent-orchestration`):
- **Sequential Deployment** (1-5): Linear workflows, dependency-heavy operations
- **Parallel Deployment** (6-10): Independent research, multi-domain exploration

**Agent Coordination**:
- `/explore-codebase` → Internal discovery (52 operations: 16 Glob + 24 Grep + 12 Read)
- `/explore-web` → External research (4-16 parallel searches based on complexity)
- `/think-layers` → Progressive analysis (L1-L4 based on complexity)
- `/capture-learnings` → Pattern detection and learning integration

#### Phase 3: Result Consolidation & Analysis Planning
**Consolidation Protocol** (via `/agent-orchestration`):
1. **Collection**: Gather all agent outputs with metadata tagging
2. **Validation**: Verify result completeness and quality standards
3. **Synthesis**: Consolidate findings into coherent narrative
4. **Output**: Generate structured results with cross-references

### Load Management & Coordination
**Intelligent Distribution** (via `/agent-orchestration`):
- **Capacity Detection**: Monitor cognitive load and processing limits through real-time monitoring
- **Dynamic Balancing**: Redistribute workload based on agent performance metrics
- **Context Switching**: Minimize cognitive loss during agent handoffs with seamless continuation
- **Recovery Protocols**: Handle agent failures with automatic workload redistribution

### Intelligent Orchestration Protocol
**Real-Time Progress Framework**:
```
🎯 COMPLEXITY: Request analyzed → Complexity [N]/10 → [Strategy] deployment selected
🤖 DEPLOY: [N] agents activated → [Agent-types] assigned to [task-categories]
⚖️ BALANCE: Load optimization → [N] agents active → Cognitive utilization [X]%
📊 PROGRESS: Orchestration [X]% complete → [N] agents completed
🔄 SYNC: Agent synchronization → [N] results consolidated
✅ SUCCESS: Discovery complete → [execution-time] | Quality score: [X]%
```

**Decision Framework**: Transparent rationale for exploration strategy via `/agent-orchestration` complexity matrix
**Communication Protocol**: Deploy → Execute → Monitor → Consolidate → Announce with progress rationale

### Auto-Activation Framework
**Triggers**: Direct invocation, insufficient context, complex requests requiring systematic analysis
**Complexity Matrix** (via `/agent-orchestration`):
- **Simple** (1-5): Sequential deployment → Single/dual agent with basic monitoring
- **Complex** (6-8): Parallel deployment → 4-8 agents with advanced coordination  
- **Maximum** (9-10): High-parallel deployment → 8-16 agents with intelligent load balancing

**Auto-Scaling**: Dynamic agent count based on request scope, breadth, and interdependency requirements

### Output Standards
**Output**:
- `context/discoveries/[session-id].md` → Findings
- `context/patterns/[pattern].md` → New patterns
- `context/research/[topic].md` → Web findings
- Anti-bias, cross-referenced, ≤200 lines, maximum density

## ⚡ Triggers

### Input Triggers
**Context**: Any complex user request requiring systematic analysis
**Previous**: Entry point for all workflows
**Keywords**: start, begin, analyze, explore, research, plan, discovery

### Output Triggers
**When**: Discovery complete → `/think-layers` for analysis and automatic consolidation
**When**: Insufficient context → Recursive `/start` with refined scope
**When**: Simple request → Direct command execution
**Chain**: start → explore → think-layers → {docs-agent + main-execution} → capture-learnings

### Success Patterns
**Discovery Success**: >90% context clarity achieved → Proceed to analysis
**Exploration Success**: Comprehensive patterns identified → Generate actionable plan
**Analysis Success**: Clear execution roadmap created → Initiate implementation

### Automatic Learning Capture Protocol
**POST-WORKFLOW ASSESSMENT**: After workflow completion, evaluate learning value using scoring framework

**Learning Value Detection**: Auto-scoring ≥4 points → /capture-learnings execution
**Framework**: Session completion → threshold assessment → auto-execution → system enhancement

### Git Integration Protocol
**SESSION-COMPLETION Tracking**: Automatic standardized commit generation on successful workflow completion

## 🔗 Module Integration

### Command Module Dependencies
**Core Integration**:
- `/agent-orchestration` → Intelligent agent deployment and coordination protocol
- `/matrix-maintenance` → Cross-reference matrix validation and system integrity maintenance

**Execution Chain**:
- `/explore-codebase` → Internal knowledge discovery and pattern analysis
- `/explore-web` → External research and solution validation  
- `/think-layers` → Progressive analysis with plan consolidation
- `/capture-learnings` → Pattern detection and post-execution learning
- `/docs-workflow` → Automatic agent delegation during analysis completion

### Success Patterns & Performance Metrics
**Discovery Success**: >90% context clarity achieved via intelligent questioning → Proceed to analysis
**Orchestration Success**: Optimal agent strategy selected → Execution efficiency >85%
**Coordination Success**: Agent synchronization achieved → Result integration <5min
**Analysis Success**: Clear execution roadmap created → Implementation readiness achieved

### Integration Success Indicators
**Module Reusability**: Successfully coordinates across all command network workflows
**Performance Enhancement**: Measurable improvement in discovery workflow efficiency
**Quality Maintenance**: Consolidated results maintain individual agent quality standards
**Scalability**: Handles increasing complexity without coordination degradation

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: These are the ACTUAL tool calls that implement the documented functionality

```javascript
// 1. STRUCTURAL VALIDATION (real execution)
LS("/Users/nalve/ce-simple") // Verify root structure
LS("/Users/nalve/ce-simple/docs") // Verify docs/ directory  
LS("/Users/nalve/ce-simple/context") // Verify context/ directory
LS("/Users/nalve/ce-simple/.claude") // Verify .claude/ directory

// 2. STRUCTURAL VIOLATIONS DETECTION (real execution)
Glob("**/*.md", {path: "."}) // Find all markdown files
Grep("BROKEN|MISSING|ERROR", {glob: "**/*.md", output_mode: "files_with_matches"}) // Find violations

// 3. GIT INTEGRATION (real execution - workflow completion)
Bash("git add . && git commit -m \"start: [workflow-name] | [metrics] ✓session-[N]\"") // Clean commit format

// 4. AGENT DEPLOYMENT (real execution via Task tool)
Task("Agent deployment", "[deployment-strategy] based on complexity assessment")
```

### Execution Prevention Framework
**ANTI-DOCUMENTATION-THEATER MEASURES**:

1. **Execution Verification**: Every documented automation MUST have corresponding tool calls
2. **Tool Call Ratio**: Minimum 3:1 ratio of actual tools to documentation lines
3. **Git Commit Tracking**: Each workflow completion triggers real git commit
4. **Performance Metrics**: Track execution vs documentation discrepancies

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with usage tracking
Bash("git add . && git commit -m \"start: [description] | metrics: [data] ✓session-[N]\"")
```

---

**CRITICAL**: This command orchestrates the entire system and MUST maintain state awareness across all deployed agents. All other commands are triggered through this master workflow.

**EXECUTION COMMITMENT**: Every automation documented above MUST be implemented with actual tool calls. Documentation without execution is system integrity violation.