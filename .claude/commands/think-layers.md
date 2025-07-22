# Think Layers - Progressive Analysis Framework

## 🎯 Purpose
Execute progressive cognitive analysis: Think → Think-Hard → Think-Harder → Ultra-Think for comprehensive problem solving.

## 🚀 Usage
Execute: `/think-layers [analysis-target] [starting-layer]`

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
**MANDATORY at analysis initialization**:

```javascript
TodoWrite([
  {"content": "🧠 DEPTH: Determine analysis depth via /agent-orchestration complexity matrix (L1-L4)", "status": "pending", "priority": "high", "id": "think-depth-1"},
  {"content": "🔄 ESCALATION: Execute progressive layer escalation with cognitive load management", "status": "pending", "priority": "high", "id": "think-escalate-1"},
  {"content": "🔀 ORCHESTRATION: Coordinate thinking layers via /agent-orchestration for optimal cognitive distribution", "status": "pending", "priority": "high", "id": "think-orchestration-1"},
  {"content": "🎯 CONSOLIDATION: Synthesize progressive analysis into implementable action plan", "status": "pending", "priority": "medium", "id": "think-consolidate-1"},
  {"content": "🤖 DELEGATION: Deploy intelligent task division and workflow coordination", "status": "pending", "priority": "medium", "id": "think-delegate-1"},
  {"content": "📚 LEARNING: Auto-trigger /capture-learnings if complexity threshold ≥4 points", "status": "pending", "priority": "low", "id": "think-learning-1"}
])
```

**Progressive Todo Updates**: Update todos in real-time as thinking layers escalate and insights emerge

### Progressive Analysis Protocol

#### Agent Orchestration Integration
**Auto-Triggered**: Deploy `/agent-orchestration` for cognitive load management and layer coordination
**Parameters**: Analysis complexity, thinking depth requirements, cognitive load limits
**Output**: Optimal thinking strategy with escalation protocols

#### Intelligent Depth Management
**Auto-Depth Selection**: System determines required thinking depth via complexity matrix (1-10 scale)
**Cognitive Load Distribution**: Dynamic balancing across thinking layers via `/agent-orchestration`
**Progressive Escalation**: Systematic depth increase with automated monitoring
**Layer Integration**: Build insights across thinking levels with validation protocols
**Plan Consolidation**: Convert progressive analysis to implementable steps with intelligent delegation

### Four-Layer Framework
**L1**: Think (25% load, 2-5min) - Surface patterns, basic understanding
**L2**: Think-Hard (50% load, 5-15min) - Component analysis, relationships  
**L3**: Think-Harder (75% load, 15-30min) - Systems integration, strategies
**L4**: Ultra-Think (95% load, 30-60min) - Meta-analysis, innovation

### Auto-Activation & Escalation System

#### Complexity-Based Layer Selection (via `/agent-orchestration`)
**Intelligence Framework**:
```
🧠 DEPTH-ANALYSIS: Complexity [N]/10 → Layer requirement determined
🔄 ESCALATION: Layer-[N] → Assessment → Escalation decision
⚖️ LOAD-BALANCE: Cognitive load [X]% → Layer coordination optimized
📊 PROGRESS: Layer [N] completion → Quality assessment → Next layer trigger
✅ CONSOLIDATION: All layers complete → Synthesis → Action plan generation
```

**Complexity Matrix & Layer Allocation**:
- **Simple** (1-3): L1-L2 sequential → Basic understanding with component analysis
- **Moderate** (4-6): L2-L3 focus → Relationship mapping with strategy development
- **Complex** (7-8): L1-L4 full spectrum → Complete progressive analysis
- **Maximum** (9-10): Full 4-layer → Comprehensive meta-analysis with innovation

**Dynamic Escalation Triggers**: Auto-escalate when contradictions detected, complexity increases, or solution inadequacy identified

### Intelligent Plan Consolidation Framework

#### Result Synthesis & Task Division (via `/agent-orchestration`)
**Auto-Consolidation Protocol**:
1. **🧠 SYNTHESIS**: Aggregate insights across all thinking layers with quality validation
2. **📊 ANALYSIS**: Identify implementation tasks, documentation needs, and execution priorities
3. **🤖 DIVISION**: Intelligent task categorization and workflow assignment
4. **🔄 COORDINATION**: Parallel workflow orchestration with progress monitoring

#### Multi-Stream Execution Coordination
**Documentation Stream**: Auto-classify docs tasks (README, API docs, guides, .md files)
- Auto-deploy docs-agent for `/docs-workflow` execution with generated todo plans
- Parallel documentation workflow with main implementation coordination

**Implementation Stream**: Core functionality development with structured task division
- Coordinate with `/start` for comprehensive agent deployment
- Integrate with `/matrix-maintenance` for cross-reference validation
- Execute via `/agent-orchestration` for optimal resource distribution

**Quality Assurance Stream**: Validation and testing coordination
- Cross-reference integrity via `/matrix-maintenance`
- Learning capture via `/capture-learnings` for pattern documentation
- Performance monitoring and optimization feedback loops

### Thinking Layer Orchestration Framework

#### Layer Coordination Protocol (via `/agent-orchestration`)
**L1 - Think** (25% cognitive load, 2-5min): Surface pattern analysis with basic understanding
- **Pattern Recognition**: Initial hypothesis generation and basic connections
- **Context Assembly**: Gather relevant information and establish scope boundaries
- **Quick Assessment**: Rapid evaluation of complexity and escalation requirements

**L2 - Think-Hard** (50% cognitive load, 5-15min): Component analysis with relationship mapping
- **Deep Analysis**: Detailed component examination and interdependency mapping
- **System Understanding**: Comprehensive grasp of relationships and integration points
- **Strategy Formation**: Initial strategic approaches and solution pathways

**L3 - Think-Harder** (75% cognitive load, 15-30min): Systems integration with strategy development
- **Complex Integration**: Multi-system analysis with comprehensive understanding
- **Strategic Planning**: Detailed solution architectures and implementation strategies
- **Risk Assessment**: Potential challenges and mitigation approaches

**L4 - Ultra-Think** (95% cognitive load, 30-60min): Meta-analysis with innovation
- **Meta-Analysis**: High-level pattern synthesis and innovation opportunities
- **Comprehensive Planning**: Complete solution architecture with execution roadmap
- **Future-Proofing**: Long-term sustainability and evolution considerations

## ⚡ Triggers

### Input Triggers
**Context**: Complex analysis or synthesis required following discovery phases
**Previous**: `/explore-codebase` or `/explore-web` with discovered patterns requiring analysis
**Keywords**: analyze, think, understand, synthesize, evaluate, assess

### Output Triggers
**Success**: Analysis complete → Plan consolidation and intelligent agent delegation
**Documentation**: Tasks detected → Independent `/docs-workflow` execution with todo plans
**Implementation**: Roadmap ready → Main workflow execution coordination
**Chain**: think-layers → {docs-agent + main-execution} → capture-learnings

### Success Patterns
**Analysis Success**: Clear understanding achieved → Plan consolidation triggered
**Synthesis Success**: Implementation roadmap generated → Task division executed  
**Delegation Success**: Documentation + execution tasks → Parallel workflow coordination
**Integration Success**: Multi-agent workflows → Combined execution readiness

### Automatic Learning Capture Integration
**POST-ANALYSIS ASSESSMENT**: After analysis completion, evaluate session learning value and auto-trigger capture when warranted

**Learning Value Auto-Detection**:
```
📊 ANALYSIS-SCORING: Calculate cognitive complexity and pattern discovery value
🧠 COMPLEXITY-INDICATORS:
  - Multiple thinking layers activated (+2 points)
  - Novel pattern synthesis achieved (+2 points)
  - Error resolution during analysis (+2 points)
  - Alternative strategies evaluated (+1 point)
  - Cross-domain insights generated (+1 point)

🎯 AUTO-THRESHOLD: ≥4 points → Automatic /capture-learnings activation
⚡ EXECUTION: Seamless transition from analysis → learning documentation
```

**Integration Protocol**:
1. **Analysis Complete** → Evaluate session complexity using learning scoring framework
2. **Threshold Check** → Compare against ≥4 point learning value requirement
3. **Auto-Trigger** → Execute /capture-learnings with analysis context when threshold met
4. **Pattern Documentation** → Capture analysis insights and decision patterns automatically
5. **System Learning** → Integrate discoveries into context architecture for future analysis enhancement

### Problem-Solving Mode Integration

#### Enhanced Analysis Capabilities for Problem Resolution
**Specialized Integration**: When called from `/problem-solving` workflow, each thinking layer applies problem-resolution focused analysis

**🧠 L1-THINK: Problem Understanding & Root Cause Analysis**
- **Symptom Analysis**: Break down error manifestation and behavior patterns
- **Root Cause Hypothesis**: Initial theories based on symptoms and discovered context
- **Quick Mitigation**: Immediate actions to prevent further impact
- **Impact Assessment**: System stability and user experience evaluation

**💪 L2-THINK-HARD: Deep Investigation & Solution Architecture**
- **Forensic Analysis**: Detailed investigation using internal context and external research
- **Solution Strategies**: Multiple approach evaluation with trade-off analysis
- **Architecture Review**: System design implications and improvement opportunities
- **Hypothesis Testing**: Validation approach for root cause theories

**🚀 L3-THINK-HARDER: Complex Solution Design & Implementation Strategy**
- **Solution Architecture**: Comprehensive fix design with dependency analysis
- **Risk Assessment**: Potential side effects and rollback strategy planning
- **Integration Planning**: How solution fits within existing system architecture
- **Implementation Roadmap**: Detailed step-by-step execution planning

**⭐ L4-ULTRA-THINK: Comprehensive Resolution & Future Prevention**
- **Execution Plan**: Complete solution implementation with validation criteria
- **Prevention Strategy**: System enhancements to prevent recurrence
- **Monitoring Approach**: Success metrics and ongoing health assessment
- **System Evolution**: Learning integration and architecture improvements

#### Problem-Solving Integration Success Patterns
**Context Inheritance**: Receives diagnosis, codebase analysis, and web research from previous phases
**Enhanced Analysis**: Applies problem-resolution lens to all thinking layers
**Solution Focus**: Prioritizes actionable solutions over theoretical analysis
**Risk Awareness**: Considers system stability and rollback requirements throughout analysis

## 🔗 Module Integration

### Command Module Dependencies
**Core Integration**:
- `/agent-orchestration` → Cognitive load management and progressive layer coordination
- `/matrix-maintenance` → Cross-reference validation during analysis consolidation

**Execution Chain**:
- `/start` → Initiates workflows triggering progressive analysis
- `/explore-codebase` & `/explore-web` → Generate analysis input and context foundation
- `/docs-workflow` → Automatic delegation for documentation tasks via intelligent task division
- `/capture-learnings` → Post-execution pattern detection and analysis insight documentation
- `/problem-solving` → Enhanced integration for problem-resolution focused analysis

### Success Patterns & Performance Metrics
**Analysis Success**: Clear understanding achieved via optimal layer selection → Plan consolidation triggered
**Orchestration Success**: Cognitive load optimally distributed → Layer coordination efficiency >90%
**Synthesis Success**: Implementation roadmap generated → Intelligent task division executed
**Integration Success**: Multi-agent workflows coordinated → Combined execution readiness achieved

### Integration Success Indicators
**Cognitive Efficiency**: Optimal thinking depth with minimal cognitive waste
**Quality Synthesis**: Progressive insights build coherently across layers
**Intelligent Delegation**: Automatic task division and parallel workflow coordination
**Learning Integration**: Analysis patterns captured and documented for system enhancement

### Context Output Locations
- `context/discoveries/` → Analysis output and pattern synthesis documentation
- `context/patterns/` → Decision frameworks and analytical approach patterns
- `context/research/` → Cross-domain insights and innovation opportunities

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of progressive thinking layers and agent coordination

```javascript
// COGNITIVE DEPTH ASSESSMENT
// Determine thinking layer depth (L1-L4) based on complexity

// LAYER 1 - BASIC ANALYSIS (Simple problems 1-3)
Task("Think L1", "Basic analysis: [problem] - identify core components, obvious solutions, immediate actions")

// LAYER 2 - DEEPER ANALYSIS (Moderate problems 4-6) 
Task("Think L2", "Deeper analysis: [problem] - explore alternatives, consider constraints, evaluate tradeoffs")

// LAYER 3 - COMPREHENSIVE ANALYSIS (Complex problems 7-8)
Task("Think L3", "Comprehensive analysis: [problem] - system implications, stakeholder impacts, long-term consequences")

// LAYER 4 - ULTRA-DEEP ANALYSIS (Maximum complexity 9-10)
Task("Think L4", "Ultra-deep analysis: [problem] - philosophical implications, paradigm shifts, emergent properties")

// COGNITIVE LOAD MANAGEMENT
Bash("echo 'scale=2; [current_layer] * 100 / 4' | bc") // Calculate cognitive utilization

// LEARNING THRESHOLD ASSESSMENT  
// Auto-trigger capture-learnings if complexity ≥4 points
Task("Learning Assessment", "Evaluate learning value: [analysis-insights] - score 1-10 based on novelty, reusability, importance")

// PROGRESSIVE CONSOLIDATION
Write("context/discoveries/analysis-[timestamp].md", "# Progressive Analysis Results\n[layer-by-layer-insights]")
```

### Progressive Layer Logic
**EXECUTION STRATEGY**:
- **Assess problem complexity** (1-10 scale)
- **Deploy thinking layers accordingly**:
  - 1-3: Execute L1 basic analysis
  - 4-6: Execute L1 + L2 deeper analysis  
  - 7-8: Execute L1 + L2 + L3 comprehensive
  - 9-10: Execute L1 + L2 + L3 + L4 ultra-deep

### Auto-Learning Trigger
**LEARNING CAPTURE AUTOMATION**:
```javascript
// If analysis complexity ≥4 points, auto-trigger learning capture
if (complexity_score >= 4) {
  Task("Auto Learning Capture", "Execute /capture-learnings for high-value analysis insights")
}
```

### Session Completion Protocol  
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with analysis metrics (no Claude attribution)
Bash("git add . && git commit -m \"think-layers: [analysis-topic] | depth: L[N] | complexity: [N]/10 | session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **1-4 Task operations**: Based on complexity-driven layer selection
- **Cognitive load calculation**: Mathematical assessment via bc command
- **Learning assessment**: Automated threshold evaluation
- **Output generation**: Analysis documentation via Write tool
- **Ratio**: 4-8 tool calls to ~150 documentation lines = 3-5% (HEALTHY)

---

**CRITICAL**: This command provides core analytical engine with automatic plan consolidation. Progressive thinking layers ensure appropriate cognitive depth, followed by intelligent task division and documentation workflow delegation.

**EXECUTION COMMITMENT**: Progressive thinking layers L1-L4 are NOW implemented with actual Task tool deployments. Cognitive load management and learning triggers are automated.