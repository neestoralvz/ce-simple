# Command Development Standards

## Core Requirements

Every slash command MUST be:
1. **Self-contained**: All logic included
2. **Orchestration-focused**: Commands coordinate, tasks execute
3. **Parallel-optimized**: Default to concurrent execution
4. **Error-resilient**: Handle all failure modes
5. **Learning-enabled**: Improve with use
6. **Foundation-integrated**: Leverage 00-core infrastructure when applicable

### Foundation Integration Guidelines
Commands should integrate with foundation layer infrastructure:
- **Notifications**: Use notify-manager for transparent delegation tracking
- **Context Management**: Leverage context-engine for distributed memory coherence
- **State Transitions**: Use handoff-manager for seamless workflow phase transitions
- **Project Initialization**: Reference init-project for new project setup patterns

## Command Structure

### Required Sections

```markdown
# command-name

## Purpose
[Single paragraph describing what this command orchestrates]

## Usage
```
/command-name [required-param] [optional-param]
```

## Parameters
- `required-param`: Description
- `optional-param`: Description (default: value)

## Task Orchestration
[Detailed orchestration strategy]

## Error Handling
[How failures are managed]

## Performance
[Expected execution time and parallelization]

## Examples
[Real usage examples with expected outcomes]
```

### Task Orchestration Section

Must include:
```yaml
Strategy:
  - Task distribution plan
  - Parallelization approach
  - Resource requirements
  
Tasks:
  task-1:
    purpose: What this task does
    parallel: true/false
    dependencies: none/[task-list]
    
  task-2:
    purpose: What this task does
    parallel: true/false
    dependencies: none/[task-list]
    
Result Aggregation:
  - How results combine
  - Conflict resolution
  - Output format
```

## Implementation Standards

### Complexity Assessment Framework

Before implementing any command, assess complexity using systematic criteria:

#### Scoring Components (1-10 Scale)
**Total Score = Domain Scope + Technical Depth + Context Requirements + Implementation Steps**

**Domain Scope (1-3 points)**
- 1 point: Single domain, isolated changes
- 2 points: Dual domain interaction required
- 3 points: Multi-domain integration, system-wide impact

**Technical Depth (1-3 points)**
- 1 point: Surface-level modifications, existing patterns
- 2 points: Moderate complexity, some architectural considerations
- 3 points: Deep architectural changes, new patterns required

**Context Requirements (1-2 points)**
- 1 point: Self-contained, existing knowledge sufficient
- 2 points: External knowledge, research, or validation needed

**Implementation Steps (1-2 points)**
- 1 point: Linear execution, independent steps
- 2 points: Complex dependencies, ordered execution required

#### Complexity Categories
- **Simple (1-3)**: Direct execution, minimal analysis
- **Medium (4-6)**: Moderate analysis, single-domain solutions
- **Complex (7-9)**: Multi-domain analysis, architectural planning
- **Critical (10)**: System-wide impact, comprehensive research

### Task Deployment Strategy

#### Agent Deployment Based on Complexity

**Parallel Execution (Score ≥8)**
- Independent research domains (web + codebase)
- No dependency chain between tasks
- High complexity requiring distributed cognitive load
- Multiple pattern sources need simultaneous analysis

**Sequential Execution (Score ≤7)**
- Analysis dependencies detected (results inform next steps)
- Medium complexity manageable by ordered workflow
- Context building requires information hierarchy
- Resource optimization for focused exploration

#### Task Instruction Template

Deploy tasks using clear natural language instructions:
```
Objective: [Single clear goal]
Context: [All necessary information]
Steps: [Specific actions]
Success Criteria: [Measurable outcomes]
Output Format: [Structured result format]
```

### Parallelization Requirements

```yaml
Default Mode: Parallel
Sequential Only When:
  - Explicit dependencies exist
  - Resource constraints apply
  - Business logic requires

Parallelization Levels:
  - Small tasks: 8-10 parallel
  - Medium tasks: 5-7 parallel  
  - Large tasks: 3-5 parallel
```

### Error Handling

```yaml
Required Strategies:
  - Retry logic with backoff
  - Partial result recovery
  - Graceful degradation
  - Clear error reporting

Error Categories:
  - Task failures
  - Timeout errors
  - Resource constraints
  - Invalid inputs
```

## Quality Standards

### Code Metrics
- **Command size**: ≤500 lines (including embedded patterns)
- **Task instruction clarity**: Self-contained and complete
- **Parallelization ratio**: ≥70% of tasks parallel
- **Error handling coverage**: 100% of failure modes

### Performance Standards
- **Startup time**: <2 seconds
- **Task deployment**: <1 second per task
- **Result aggregation**: <5 seconds
- **Total execution**: Documented estimate

### Documentation Standards
- **Purpose clarity**: Understandable in one read
- **Usage examples**: At least 3 real scenarios
- **Error scenarios**: All failure modes documented
- **Performance notes**: Expected timings included

## Anti-Patterns

### Command Anti-Patterns
- **God commands**: Doing too much in one command
- **Hidden dependencies**: Assuming external state
- **Sequential thinking**: Not leveraging parallelism
- **Poor error handling**: Letting failures cascade
- **No learning**: Not capturing patterns

### Task Anti-Patterns
- **Vague instructions**: Sub-agents can't infer
- **External dependencies**: Referencing other commands
- **Shared state**: Creating race conditions
- **No validation**: Trusting all outputs
- **Poor aggregation**: Losing information in merge

## Quality Checklist

Before submission:
- [ ] Command is fully self-contained
- [ ] All sections documented
- [ ] Task orchestration clear
- [ ] Error handling complete
- [ ] Performance documented
- [ ] Examples provided
- [ ] Patterns embedded
- [ ] Learning mechanism included
- [ ] Foundation integration considered

During review:
- [ ] Parallelization optimized
- [ ] Instructions clear
- [ ] Output standardized
- [ ] Errors handled gracefully
- [ ] Code within limits
- [ ] Anti-patterns avoided

## Excellence Indicators

A command demonstrates excellence when:
1. **Execution is 10x faster** than manual approach
2. **Parallelization exceeds 80%** of operations
3. **Error recovery is automatic** and transparent
4. **Learning improves performance** over time
5. **User experience is seamless** despite complexity

---

**Standard Commitment**: Every command we create will be a masterpiece of orchestration—simple to use, powerful in execution, and continuously improving.