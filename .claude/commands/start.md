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

### Intelligent Orchestration
**Real-Time Progress**: Discovery → Dynamic questions → Context validation → Multi-agent deployment

**Decision Framework**: Transparent rationale for exploration strategy, agent coordination, and analysis depth selection

**Communication Protocol**: Deploy → Execute → Return → Announce cycle with progress rationale

### Auto-Activation Framework
**IMMEDIATE Triggers**: Direct `/start` invocation, insufficient context detection, complex multi-step requests

**Complexity Matrix**: ≤5 (local+sequential+L1-2) → 6-7 (mixed+context+L2-3) → ≥8 (full+parallel+L3-4)

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

### Automatic Learning Capture Protocol
**POST-WORKFLOW ASSESSMENT**: After workflow completion, evaluate learning value using scoring framework

**Learning Value Detection**:
```
📊 AUTO-SCORING: Calculate session complexity and learning value
🎯 THRESHOLD: ≥4 points → Automatic /capture-learnings execution
🔄 DECISION-LOGIC:
  - Sequential commands >2 (+2 points)
  - Error resolution occurred (+2 points)  
  - New patterns discovered (+2 points)
  - Alternative strategies (+1 point)
  - Context switching required (+1 point)

🧠 AUTO-EXECUTE: /capture-learnings when threshold exceeded
⚡ NOTIFICATION: Learning capture initiated → Dynamic interview activated
```

**Automatic Integration Framework**:
1. **Workflow Complete** → Calculate learning value score from session
2. **Threshold Assessment** → Compare against ≥4 point minimum requirement
3. **Auto-Execution** → Launch /capture-learnings with session context when threshold met
4. **Learning Documentation** → Capture patterns and user insights automatically
5. **System Enhancement** → Apply learning insights to future workflow optimization

### Git Integration Protocol
**SESSION-COMPLETION Tracking**: Automatic standardized commit generation on successful workflow completion

## 🔗 See Also

### Implementation Details
- `../../standards/start-agent-communication.md` - Complete agent communication protocols and decision transparency framework

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