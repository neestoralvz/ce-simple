# Task Tool Communication Patterns

**Updated**: 2025-07-24 | **Pattern Type**: Technology/Workflow | **Status**: Active | **Limit**: 80 lines
**Purpose**: Agent coordination patterns and communication protocols

## Technical Authority References (Lines 5-20)
**Complete Agent Deployment Framework**: @docs/technical/agent-deployment-technical.md:1-80
**Parallel Execution Patterns**: @docs/technical/agent-deployment-technical.md:21-40
**Specialization Framework**: @docs/technical/agent-deployment-technical.md:41-60
**Best Practices**: @docs/technical/agent-deployment-technical.md:61-80

## Pattern Application Context (Lines 21-35)
### When to Apply
- Complex workflows requiring parallel execution
- Multiple independent operations can be parallelized  
- Coordination between multiple sub-agents needed
- Large-scale operations benefit from distributed processing

### Core Patterns
- **10-Agent Coordination**: @docs/technical/agent-deployment-technical.md:21-40
- **Wave-Based Deployment**: @docs/technical/agent-deployment-technical.md:21-40
- **Communication Protocols**: @docs/technical/agent-deployment-technical.md:41-60
- **Result Synthesis**: @docs/technical/agent-deployment-technical.md:61-80

### Deployment Strategies
**Analysis Wave**: Domain experts + research + context assessment (2-3 agents)
**Operations Wave**: File ops + CLI execution + configuration (4-6 agents) 
**Validation Wave**: Quality assurance + integration testing (1-2 agents)

## Implementation Patterns (Lines 36-55)
### Communication Architecture
- **Explicit Orchestration**: Detailed delegation instructions (multi-threading pattern)
- **One-Way Communication**: Sub-agents return final results only
- **Context Isolation**: Sub-agents operate in separate contexts  
- **Result Aggregation**: Main agent synthesizes all outputs

### Task Distribution Optimization
- **Group Related Operations**: Batch similar tasks for efficiency
- **Balance Complexity**: Distribute complex/simple tasks across agents
- **Consider Dependencies**: Use waves when output dependencies exist
- **Token Efficiency**: Design tasks minimizing context consumption

### Error Handling Protocols
- **Graceful Degradation**: Continue with available results on failures
- **Error Isolation**: Sub-agent failures contained within their context
- **Retry Mechanisms**: Automated retry for transient failures
- **Escalation Protocols**: Clear escalation for multiple agent failures

## Success Metrics & Evolution (Lines 56-80)
### Performance Targets
- **Execution Time**: ≥50% improvement over sequential | **Completion Rate**: ≥95% successful tasks
- **Coordination Overhead**: <10% agent coordination cost | **Context Efficiency**: Optimal token usage

### Quality Indicators  
- **Result Synthesis**: Clear, coherent sub-agent output integration
- **Error Isolation**: No failure cascades between agents
- **State Preservation**: Main agent maintains workflow state effectively

### Pattern Network
- **Error Resolution**: [error-resolution-workflow.md](error-resolution-workflow.md) - Task Tool debugging
- **Agent Coordination**: [../workflows/agent-coordination.md](../workflows/agent-coordination.md) - General principles
- **Quality Assurance**: [../frameworks/stp-validation-framework.md](../frameworks/stp-validation-framework.md) - Validation integration

### Evolution Log
- **2025-07-23**: Initial 10-agent parallel discovery + wave strategy integration
- **2025-07-24**: Authority consolidation + reference architecture implementation

---
**Application Authority**: This pattern references technical authority for agent deployment while providing application-specific coordination strategies.