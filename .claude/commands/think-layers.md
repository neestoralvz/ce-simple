# Think Layers - Progressive Analysis Framework

## 🎯 Purpose
Execute progressive cognitive analysis through structured thinking layers: Think → Think-Hard → Think-Harder → Ultra-Think for comprehensive problem solving.

## 🚀 Usage
Execute: `/think-layers [analysis-target] [starting-layer]`

## 🔧 Implementation

### Progressive Analysis Protocol
**Auto-Depth Selection**: System determines required thinking depth based on complexity scoring
**Cognitive Escalation**: Systematic analysis depth increase with load management
**Integration Cascade**: Build insights across all thinking levels with validation
**Plan Consolidation**: Convert analysis into implementable steps with agent delegation

### Four-Layer Framework
**Layer 1**: Think (25% load, 2-5min) - Surface patterns and basic understanding
**Layer 2**: Think-Hard (50% load, 5-15min) - Component analysis and relationships  
**Layer 3**: Think-Harder (75% load, 15-30min) - Systems integration and strategies
**Layer 4**: Ultra-Think (95% load, 30-60min) - Meta-analysis and innovation

### Auto-Activation System
**Complexity Matrix**:
- Score 1-3: Simple → Layer 1-2
- Score 4-6: Moderate → Layer 2-3  
- Score 7-8: High → Layer 1-4
- Score 9-10: Maximum → Full 4-layer analysis

**Dynamic Escalation**: Auto-escalate when contradictions, complexity emergence, or solution inadequacy detected

### Plan Consolidation Framework
**AUTO-TRIGGER**: After synthesis completion → Intelligent task division
**Context Consolidation**: Aggregate discoveries from parallel analysis agents when triggered by `/start`
**Documentation Detection**: Automatic classification of documentation tasks (README, API docs, guides, .md files)
**Agent Delegation**: Deploy independent docs-agent for `/docs-workflow` with structured todo plans
**Parallel Execution**: Documentation workflow + main implementation workflow coordination

*Context consolidation protocols and implementation details in `../../standards/think-layers-implementation.md`*

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

### Problem-Solving Mode Enhancement

**SPECIALIZED CAPABILITIES**: When called from `/problem-solving` workflow, each thinking layer applies problem-resolution focused analysis

**🧠 THINK: Problem Understanding & Root Cause Analysis**
```
🔍 SYMPTOM ANALYSIS: Break down error manifestation and behavior patterns
🎯 ROOT CAUSE HYPOTHESIS: Initial theories based on symptoms and context
⚡ QUICK MITIGATION: Immediate actions to prevent further impact
📊 IMPACT ASSESSMENT: System stability and user experience evaluation
```

**💪 THINK-HARD: Deep Investigation & Solution Architecture**
```
🕵️ FORENSIC ANALYSIS: Detailed investigation using internal context and external research
🔧 SOLUTION STRATEGIES: Multiple approach evaluation with trade-off analysis
📐 ARCHITECTURE REVIEW: System design implications and improvement opportunities
🧪 HYPOTHESIS TESTING: Validation approach for root cause theories
```

**🚀 THINK-HARDER: Complex Solution Design & Implementation Strategy**
```
🏗️ SOLUTION ARCHITECTURE: Comprehensive fix design with dependency analysis
⚠️ RISK ASSESSMENT: Potential side effects and rollback strategy planning
🔄 INTEGRATION PLANNING: How solution fits within existing system architecture
📋 IMPLEMENTATION ROADMAP: Detailed step-by-step execution planning
```

**⭐ ULTRA-THINK: Comprehensive Resolution & Future Prevention**
```
🎯 EXECUTION PLAN: Complete solution implementation with validation criteria
🛡️ PREVENTION STRATEGY: System enhancements to prevent recurrence
📈 MONITORING APPROACH: Success metrics and ongoing health assessment
🔄 SYSTEM EVOLUTION: Learning integration and architecture improvements
```

**Problem-Solving Integration**:
- **Context Inheritance**: Receives diagnosis, codebase analysis, and web research from previous phases
- **Enhanced Analysis**: Applies problem-resolution lens to all thinking layers
- **Solution Focus**: Prioritizes actionable solutions over theoretical analysis
- **Risk Awareness**: Considers system stability and rollback requirements throughout analysis

## 🔗 See Also

### Implementation References
- `../../standards/think-layers-implementation.md` - Complete analysis framework details
- `context/discoveries/` - Analysis output documentation location
- `../../standards/simplicity-principles.md` - Progressive analysis principles

### Related Commands
- Execute `/start` to initiate workflows triggering progressive analysis
- Execute `/explore-codebase` and `/explore-web` to generate analysis input
- Execute `/docs-workflow` via automatic delegation for documentation tasks
- Execute `/capture-learnings` for post-execution pattern detection

---

**CRITICAL**: This command provides core analytical engine with automatic plan consolidation. Progressive thinking layers ensure appropriate cognitive depth, followed by intelligent task division and documentation workflow delegation.