# Tool Usage Protocols

**Last Updated: 2025-07-23**
**Authority**: Tool optimization protocols implementing Partnership Protocol

## Task Tool Priority and Execution

### Task Tool Priority Rule
**Default to Task Tools**: Use Task Tools whenever possible for context economy and performance
- **Parallel Execution Default**: Simultaneous, concurrent task tool execution in single messages
- **Context Economy**: Efficient use of context through proper tool selection
- **Performance Optimization**: Maximize execution speed through parallel processing
- **Resource Efficiency**: Optimal distribution of workload across available tools

### 10-Agent Parallel Coordination
**Maximum Concurrency Management**:
- **10-Agent Limit**: Claude Code maximum concurrent sub-agents per execution
- **Queue Management**: Tasks beyond 10-agent limit automatically queue for next batch
- **Batch Processing**: Coordinate operations requiring >10 agents through sequential waves
- **Resource Balancing**: Distribute complex and simple tasks across available agents

## Wave-Based Deployment Strategies

### Wave Strategy Implementation
```yaml
Wave 1 - Analysis (2-3 agents):
  - Domain expert analysis for technical assessment
  - Research agents for external information gathering  
  - Context analysis agents for requirement understanding

Wave 2 - Operations (4-6 agents):
  - File creation and modification agents
  - CLI tool execution agents
  - Configuration and setup agents

Wave 3 - Validation (1-2 agents):
  - PTS compliance validation agent
  - Quality assurance and integration testing agent
```

### Communication Protocols
- **Explicit Orchestration**: Detailed delegation instructions (like multi-threading programming)
- **One-Way Communication**: Sub-agents return only final results to main agent
- **Context Isolation**: Sub-agents operate in separate context windows
- **Result Aggregation**: Main agent synthesizes outputs from all sub-agents

## Think x4 Methodology Integration

### Think Protocol Application
**Layered Analysis Before Implementation**:
- **Think**: Initial analysis and immediate understanding
- **Think Hard**: Deeper investigation and root cause analysis
- **Think Harder**: Comprehensive assessment and solution architecture
- **Ultra Think**: Integral solutions and long-term prevention strategies

### Integration with Tool Usage
- **Think Phase**: Use analysis tools and research agents
- **Implementation Phase**: Deploy operation agents based on think results
- **Validation Phase**: Apply validation agents to verify think-based solutions
- **Learning Phase**: Capture insights for future think processes

## Context Economy and Token Optimization

### Token Economy Rule Implementation
**Context Optimization Without Quality Sacrifice**:
- **Strategic Tool Selection**: Choose tools that maximize value per token consumed
- **Efficient Task Distribution**: Group related operations for token efficiency
- **Result Compression**: Efficiently compress sub-agent outputs for integration
- **Context Preservation**: Maintain workflow state in main agent with minimal overhead

### Context Management Strategies
- **State Preservation**: Main agent maintains workflow state efficiently
- **Token Efficiency**: Design tasks to minimize context consumption
- **Result Synthesis**: Clear, coherent integration of sub-agent outputs
- **Error Isolation**: Sub-agent failures contained within their context

## Research and External Integration

### Research Integration Protocols
- **Context 7 MCP Integration**: Leverage MCP capabilities for real-time documentation
- **Web Search Coordination**: Use research agents for comprehensive information gathering
- **Best Practice Integration**: Incorporate external research into tool usage patterns
- **External Validation**: Cross-reference internal approaches with industry standards

### Tool Combination Patterns
- **Analysis + Research**: Combine internal analysis with external research agents
- **Implementation + Validation**: Pair operation agents with validation agents
- **Creation + Optimization**: Balance creation agents with performance optimization
- **Monitoring + Learning**: Integrate monitoring tools with learning capture mechanisms

## Success Metrics and Optimization

### Performance Indicators
- **Execution Time Reduction**: ≥50% improvement over sequential execution
- **Task Completion Rate**: ≥95% successful sub-agent task completion
- **Coordination Efficiency**: <10% overhead for agent coordination
- **Context Efficiency**: Optimal token usage per unit of value delivered

### Quality Measures
- **Result Synthesis Quality**: Clear, coherent integration of sub-agent outputs
- **Error Isolation Effectiveness**: Sub-agent failures don't cascade to other agents
- **Tool Selection Optimization**: Best tool choices for specific operation types
- **Pattern Reuse**: Successful tool usage patterns documented and reused

---

**Application**: These protocols ensure optimal tool usage while maintaining quality and efficiency. Reference when planning complex operations or optimizing workflow execution.