# Start - Discovery Workflow Master

## 🎯 Purpose
Initialize comprehensive discovery workflow with dynamic questioning, context generation, and automated orchestration of analysis agents.

## 🚀 Usage
Execute: `/start [optional: initial request]`

## 🔧 Implementation

### Discovery Protocol
1. **REQUEST CAPTURE**: Receive user input and analyze complexity level
2. **DYNAMIC QUESTIONING**: Generate contextual questions to clarify objectives
3. **CONTEXT SUFFICIENCY**: Determine if conceptual understanding is complete
4. **EXPLORATION ORCHESTRATION**: Deploy parallel/sequential agent workflows
5. **PROGRESS TRACKING**: Maintain transparent workflow notifications

### Workflow Orchestration Framework

#### Phase 1: Discovery & Context Building
```
⟳ /start → discovery questions → context validation → exploration trigger
```

**MANDATORY Questions (Dynamic Generation)**:
- Objective clarification: "What specific outcome do you need?"
- Scope definition: "What are the boundaries of this request?"
- Context requirements: "What conceptual information should I understand?"
- Priority assessment: "What elements are most critical?"

#### Phase 2: Exploration Deployment
**AUTOMATIC Determination**:
- **Parallel Execution**: Independent research, pattern search, codebase exploration
- **Sequential Execution**: Dependent analysis requiring previous results

**Agent Deployment Matrix**:
- `/explore-codebase` → Internal knowledge discovery
- `/explore-web` → External pattern research  
- `/think-layers` → Progressive analysis with context consolidation
- `/capture-learnings` → Parallel pattern detection and post-execution learning

#### Phase 3: Analysis & Planning
**Progressive Thinking Protocol**:
1. **Think**: Basic analysis of discovered information
2. **Think-Hard**: Deep pattern recognition and connection mapping
3. **Think-Harder**: Complex integration and solution architecture
4. **Ultra-Think**: Comprehensive planning with execution roadmap

### Cognitive Load Management
**CRITICAL**: Monitor agent capacity and distribute workload optimally
- **Threshold Detection**: Identify when agent reaches cognitive limits
- **Load Balancing**: Distribute tasks across multiple agent instances
- **Context Switching**: Minimize context loss during agent handoffs

### Intelligent Notification System
**Real-Time Progress with Decision Context**:
```
🎯 START: Discovery initiated [timestamp]
📊 DISCOVERY: Questions generated → User response required
🧠 DECISION: [Brief decision reasoning]
🔧 EXPLORATION: Deploying [N] agents → [strategy + rationale]
⚡ ANALYSIS: Think-layers activated → Level [N] ([why this depth])
🧠 LEARNING: Pattern capture active → Process learning in parallel
✓ COMPLETION: Plan generated → Ready for execution
🎯 ASSESSMENT: Post-execution learning evaluation → [interview decision]
```

**Decision Transparency Examples**:
```
🧠 DECISION: Local exploration sufficient → Request matches existing patterns
🧠 DECISION: Web research needed → External validation required for solution
🧠 DECISION: Parallel agents optimal → Independent domains identified
🧠 DECISION: Sequential flow required → Analysis dependencies detected
🧠 DECISION: Level 3 analysis needed → Complex integration patterns found
🧠 DECISION: Sufficient at level 2 → Clear execution path identified
```

**Agent Communication Protocol**:
- **Deploy**: Main agent → Task agent with specific objectives
- **Execute**: Task agent performs assigned function
- **Return**: Task agent → Main agent with results summary
- **Announce**: Main agent updates user with progress + brief rationale

### Auto-Activation Triggers
**IMMEDIATE Activation**:
- User provides initial request with `/start`
- Insufficient context detected in any command
- Complex multi-step request identified

**Quick Decision Matrix**:
- **Complexity ≤5**: Local exploration, sequential agents, level 1-2 analysis
- **Complexity 6-7**: Mixed exploration, context-dependent agents, level 2-3 analysis  
- **Complexity ≥8**: Full exploration, parallel agents, level 3-4 analysis

### Output Standards
**Context Generation**:
- Create `context/discoveries/[session-id].md` with findings
- Update `context/patterns/[discovered-pattern].md` with new patterns
- Consolidate `context/research/[topic].md` with web findings

**Documentation Requirements**:
- Anti-bias content creation
- Cross-reference integration
- ≤200 lines per generated file
- Maximum density optimization

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

### Git Integration Protocol
**SESSION-COMPLETION Tracking**: Automatic commit generation on successful discovery workflow completion

**Commit Structure**:
```bash
git add . && git commit -m "start: [intent] | [complexity]([X]) | [X]min | [outcome]

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"
```

## 🔗 See Also

### Related Commands
- Execute `/explore-codebase` for internal knowledge discovery and pattern analysis
- Execute `/explore-web` for external research and solution validation  
- Execute `/think-layers` for progressive analysis with automatic plan consolidation and docs delegation
- Execute `/capture-learnings` for intelligent pattern detection and post-execution learning
- Execute `/docs-workflow` via automatic agent delegation during analysis completion

### Documentation Workflow Commands
- Execute `/docs-workflow` for complete automated documentation optimization
- Execute `/docs-audit` → `/docs-consolidate` → `/docs-optimize` → `/docs-validate` for granular control
- Comprehensive documentation health analysis and systematic optimization

### System Integration
- All commands follow writing standards for LLM-optimized documentation
- Real-time progress notifications maintain workflow transparency
- Anti-bias protocols ensure neutral information processing
- Standardized command structure enables consistent cross-command integration

---

**CRITICAL**: This command orchestrates the entire system and MUST maintain state awareness across all deployed agents. All other commands are triggered through this master workflow.