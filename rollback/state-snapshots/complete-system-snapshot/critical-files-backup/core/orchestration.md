# Task Orchestration

## Purpose
Orchestrate parallel task execution via Claude Code's Task Tool to achieve 10x productivity gains through intelligent work distribution.

## Task Tool Architecture

### Core Specifications
- **Concurrent Limit**: Up to 10 sub-agents
- **Tool Access**: Read, Write, Edit, MultiEdit, Bash
- **Restrictions**: No Task Tool access, no slash command invocation
- **Execution Model**: True parallelism with independent contexts

### Sub-Agent Properties
- Independent execution context
- Full tool access (except Task)
- Cannot see other sub-agents
- Cannot access parent context
- Must receive complete instructions

### Command Hierarchy
- **Foundation Commands**: Infrastructure layer providing notifications, context management, and handoffs  
- **Slash Commands**: Primary orchestrators that deploy sub-agents
- **Sub-Agents**: Workers created via Task Tool
- **Task Patterns**: Proven orchestration strategies
- **Result Aggregation**: Combining outputs from parallel tasks

### Foundation Integration
- **notify-manager**: Provides transparent delegation tracking across all orchestration phases
- **context-engine**: Maintains distributed memory coherence during parallel task execution
- **handoff-manager**: Enables seamless transitions between agents and workflow phases

## Core Orchestration Patterns

### Seven-Parallel-Tasks Pattern
Optimal for component development with 7x speedup:
1. Component logic
2. Styles/CSS
3. Tests
4. Type definitions
5. Utilities/hooks
6. Integration points
7. Documentation

### Multi-Agent Discovery Pattern
Deploy Task Tools for parallel discovery:
- Agent A: Internal codebase analysis using Glob, Grep, Read
- Agent B: External research using WebSearch
- Agent C: Documentation analysis using Read, Grep
- Coordinate through TodoWrite updates and result synthesis

### Wave Deployment Strategy
Structure multi-phase execution:
- **Phase 1**: Broad exploration and discovery
- **Phase 2**: Focused analysis and understanding
- **Phase 3**: Targeted creation and development
- **Phase 4**: Comprehensive validation and testing

### Competitive Redundancy Pattern
Deploy multiple Task Tools with overlapping objectives:
- Primary approach (main strategy)
- Secondary approach (alternative strategy)
- Validation approach (cross-verification method)
- Compare results and select optimal outcome

### Sequential Agent Deployment
Phase-based Task Tool deployment:
- Phase 1: Prerequisite analysis → results inform Phase 2
- Phase 2: Dependent analysis → results inform Phase 3
- Phase 3: Synthesis and integration

## Task Design Patterns

### Discovery Tasks
Structure exploration activities:
- Search specific areas or patterns
- Explore different aspects simultaneously
- Gather information from multiple sources
- Map system landscape in parallel

### Analysis Tasks
Organize analytical work:
- Process different data sets concurrently
- Apply various analytical approaches
- Examine multiple perspectives simultaneously
- Generate insights from parallel analysis

### Creation Tasks
Structure generative work:
- Build components independently
- Create different sections simultaneously
- Generate alternatives in parallel
- Develop solutions concurrently

### Validation Tasks
Organize quality assurance:
- Test different aspects simultaneously
- Validate multiple criteria in parallel
- Execute various verification approaches
- Confirm requirements from multiple angles

## Task Instruction Framework

### Clear Specifications
Write effective task instructions:
- State objective clearly and specifically
- Define expected output format
- Specify success criteria
- Include necessary context information

### Actionable Directives
Structure instructions for execution:
- Use action verbs and direct language
- Provide specific steps when needed
- Include examples for clarity
- Specify deliverable requirements

### Common Pitfalls to Avoid
- Vague instructions
- Missing context
- No success criteria
- Assumed knowledge
- External dependencies

## Parallelization Guidelines

### When to Use Parallel
- Independent operations (different files, searches)
- Multiple perspectives needed
- Time-sensitive work
- Abundant resources available

### When to Use Sequential
- Tasks have critical dependencies
- Resource constraints exist
- Shared state modifications required
- Quality gates need validation checkpoints

### Load Distribution
Balance work across parallel tasks:
- Distribute complexity evenly
- Assign similar execution time requirements
- Group related operations efficiently
- Optimize for concurrent processing

## Result Processing

### Aggregation Strategies
- **Merge Similar**: Combine compatible outputs
- **Resolve Conflicts**: Handle contradictory results
- **Extract Patterns**: Identify successful approaches
- **Synthesize Insights**: Create unified understanding

### Quality Control
- Monitor task completion status
- Identify potential bottlenecks
- Detect quality issues early
- Plan intervention strategies

### Validation Methods
- Verify task completion criteria
- Validate result accuracy
- Check information consistency
- Confirm requirement fulfillment

## Performance Optimization

### Core Guidelines
- Always parallel first
- Batch wisely
- Limit scope
- Clear boundaries

### Resource Management
- 10-task limit with queuing
- Token efficiency focus
- Time boxing approach
- Error budget planning

### Performance Targets
- **Seven-Parallel-Tasks**: ~6x speedup vs sequential
- **Search Operations**: 10x faster information gathering
- **Analysis Tasks**: 4x more comprehensive insights
- **Overall Efficiency**: 85% improvement in workflow completion

## Success Metrics

### Quality Standards
- All tasks complete successfully
- Results are coherent and usable
- No information loss in aggregation
- Conflicts resolved intelligently

### Performance Indicators
- 10x productivity gains through parallel execution
- 85% improvement in workflow completion
- True parallelism with independent contexts
- Intelligent work distribution optimization

---

**Key Principle**: Task orchestration transforms single-threaded work into parallel execution while maintaining quality and coherence through intelligent sub-agent coordination.

See orchestration-details.md for advanced techniques and implementation specifications.