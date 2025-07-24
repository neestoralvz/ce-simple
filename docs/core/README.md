# Core Architecture - ce-simple

**Last Updated: 2025-07-23**

## Purpose

Core system documentation for ce-simple command architecture implementing PTS (Pragmatic Technical Simplicity) framework with specialized agent coordination and parallel execution capabilities.

## Architecture Overview

### Foundation: PTS Framework
- **12-Component Validation**: Technical, Communication, Cognitive clusters
- **Blocking Enforcement**: Development stops when PTS compliance fails
- **Authority Hierarchy**: CLAUDE_RULES.md → PTS Framework → System Implementation

### Specialized Agent Strategy
- **Analysis Agents**: Domain experts (frontend, backend, research, security)
- **Operations Agents**: Mass execution (file creation, CLI automation)  
- **Synthesis Agent**: Content consolidation following writing standards
- **Validation Guardian**: PTS compliance and quality assurance

### Task Tool Communication
- **10-Agent Parallel Limit**: Claude Code maximum concurrent sub-agents
- **Wave-Based Deployment**: Batch coordination (Analysis → Operations → Validation)
- **One-Way Communication**: Sub-agents return only final results
- **Context Isolation**: Sub-agents operate in separate contexts

## Command Development Standards

### PTS Compliance Requirements
```bash
# Pre-development validation (2 minutes)
- [ ] Clear purpose in 30 seconds?
- [ ] Single responsibility only?
- [ ] Simplest solution that works?
- [ ] Works without configuration?

# Deployment gates
- [ ] ≤150 lines (commands), ≤200 lines (docs)
- [ ] English-only content
- [ ] 12/12 PTS components pass
- [ ] Self-contained operation
```

### Quality Gates
- **Length Limits**: 150 lines commands, 200 lines documentation (blocking)
- **Complexity Scoring**: Normalized complexity with objective thresholds
- **Marketing Language**: Zero tolerance (blocking violation)
- **PTS Validation**: Automated 12-component checking

## Document Organization

### Core Framework Files
- **[pts-framework.md](pts-framework.md)** - Complete 12-component PTS specification
- **[pts-checklist.md](pts-checklist.md)** - Development validation checklist
- **[development-principles.md](development-principles.md)** - 33-principle hierarchy (6 tiers)

### Implementation Guidance
- **[../templates/foundation-command-patterns.md](../templates/foundation-command-patterns.md)** - Proven command templates
- **[../frameworks/](../frameworks/)** - Validation and quality frameworks
- **[../vision/overview.md](../vision/overview.md)** - System philosophy and technical direction

## Agent Coordination Patterns

### Wave-Based Deployment
```yaml
Wave 1 - Analysis (2-3 agents):
  - Domain expert agents for technical assessment
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
- **Explicit Orchestration**: Detailed delegation instructions (like multi-threading)
- **Result Aggregation**: Main agent synthesizes sub-agent outputs
- **Error Isolation**: Sub-agent failures contained within their context
- **State Management**: Main agent maintains workflow state

## Implementation Checklist

### Before Development
1. **PTS Pre-validation**: 2-minute essential criteria check
2. **Agent Strategy**: Determine if parallel agents needed
3. **Tool Selection**: Choose appropriate Claude Code tools
4. **Wave Planning**: Design agent deployment sequence

### During Development  
1. **Real-time Validation**: Apply PTS checklist continuously
2. **Length Monitoring**: Track line count against limits
3. **Quality Gates**: Check compliance before proceeding
4. **Agent Coordination**: Manage parallel execution effectively

### Before Deployment
1. **Complete PTS Validation**: Full 12-component assessment
2. **Integration Testing**: Verify agent coordination works
3. **Documentation Updates**: Ensure all references current
4. **Pattern Capture**: Save successful patterns for reuse

## Success Metrics

### Development Quality
- **PTS Compliance**: 12/12 components pass (blocking requirement)
- **Execution Speed**: Optimized for 10-agent parallel coordination
- **Token Efficiency**: Minimal context consumption, maximum value
- **User Experience**: ≤30 seconds to understand component purpose

### Agent Effectiveness
- **Wave Coordination**: Smooth transition between agent batches
- **Result Quality**: High-quality output from parallel execution
- **Error Recovery**: Graceful handling of sub-agent failures
- **Pattern Reuse**: Successful patterns documented and reused

---

**Core Principle**: Simple commands with clear responsibilities that coordinate through intelligent parallel execution to achieve complex workflows while maintaining PTS compliance and token efficiency.