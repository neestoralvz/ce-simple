# Task Tool Communication Patterns

**Pattern Type**: Technology/Workflow
**Status**: Active
**Complexity**: Moderate

## Overview

Communication protocols and coordination strategies for Claude Code Task Tool parallel execution, including 10-agent coordination, wave-based deployment, and result synthesis patterns.

## Context

Applies when:
- Complex workflows require parallel execution
- Multiple independent operations can be parallelized
- Coordination between multiple sub-agents is needed
- Large-scale operations benefit from distributed processing

## Implementation

### 10-Agent Parallel Coordination
```markdown
# Deploy up to 10 simultaneous Task Tools for:
- Independent file operations (reads, writes, analysis)
- Parallel CLI tool execution
- Simultaneous research and data gathering
- Mass creation operations (multiple files/configs)

# Queue Management: 
- Tasks beyond 10-agent limit automatically queue
- Batch processing for operations requiring >10 agents
```

### Wave-Based Deployment Strategy
```yaml
Wave 1 - Analysis (2-3 agents):
  - Domain expert analysis
  - Research and external data gathering
  - Context and requirement assessment

Wave 2 - Operations (4-6 agents):
  - File creation and modification
  - CLI tool execution
  - Configuration and setup tasks

Wave 3 - Validation (1-2 agents):
  - Quality assurance and compliance checking
  - Integration testing and error detection
```

### Communication Protocols
- **Explicit Orchestration**: Detailed delegation instructions (like multi-threading programming)
- **One-Way Communication**: Sub-agents return only final results to main agent
- **Context Isolation**: Sub-agents operate in separate context windows
- **Result Aggregation**: Main agent synthesizes outputs from all sub-agents

## Evolution Log

### 2025-07-23 15:45 - Initial Discovery
Identified Task Tool parallel execution capabilities through Anthropic documentation research. Confirmed 10-agent limit with automatic queueing for additional tasks.

### 2025-07-23 16:20 - Wave Strategy Integration
Added wave-based deployment pattern as alternative to pure parallel execution. Recognized that some workflows benefit from sequential waves with dependencies rather than full parallelization.

### 2025-07-23 16:35 - Communication Protocol Clarification
Documented one-way communication limitation and context isolation characteristics. Identified need for explicit orchestration similar to multi-threading programming patterns.

## Related Patterns

- [Error Resolution Workflow](error-resolution-workflow.md) - Uses Task Tools for systematic debugging
- [Agent Coordination Strategies](../workflows/agent-coordination.md) - General coordination principles
- [Quality Assurance Patterns](../workflows/quality-assurance.md) - Validation wave integration

## Success Metrics

### Performance Indicators
- **Execution Time Reduction**: ≥50% improvement over sequential execution
- **Task Completion Rate**: ≥95% successful sub-agent task completion
- **Coordination Efficiency**: <10% overhead for agent coordination

### Quality Measures
- **Result Synthesis Quality**: Clear, coherent integration of sub-agent outputs
- **Error Isolation Effectiveness**: Sub-agent failures don't cascade to other agents
- **Context Preservation**: Main agent maintains workflow state effectively

### Usage Patterns
- **Parallel vs Wave Decision**: Clear criteria for choosing execution strategy
- **Agent Load Balancing**: Optimal distribution of work across available agents
- **Tool Selection Optimization**: Best tool choices for specific operation types

## Best Practices Discovered

### Optimal Task Distribution
- **Group Related Operations**: Batch similar tasks for efficiency
- **Balance Complexity**: Distribute complex and simple tasks across agents
- **Consider Dependencies**: Use waves when output dependencies exist

### Error Handling Strategies
- **Graceful Degradation**: Continue with available results when sub-agents fail
- **Retry Mechanisms**: Automated retry for transient failures
- **Escalation Protocols**: Clear escalation when multiple agents fail

### Context Management
- **Token Efficiency**: Design tasks to minimize context consumption
- **State Preservation**: Maintain workflow state in main agent
- **Result Compression**: Efficiently compress sub-agent outputs for integration

---

**Application Note**: This pattern is fundamental to ce-simple's agent coordination strategy and should be referenced when designing any complex workflow requiring parallel execution or multi-agent coordination.