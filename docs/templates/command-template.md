# Command Template

## Purpose
Template structure for creating self-contained slash commands that orchestrate parallel task execution.

## Command Structure

### Header Section
```
# Command Name

## Purpose
Brief description of command's main objective and use case.
```

### Core Orchestration

#### Task Distribution Strategy
Design parallel task execution using Claude Code's Task Tool:
- Identify independent components for parallel processing
- Group related tasks to minimize context switching
- Balance workload across available task slots
- Plan task dependencies and execution order

#### Execution Pattern
Structure command flow:
1. Analyze user input and determine scope
2. Deploy initial discovery tasks in parallel
3. Process results and identify next wave requirements
4. Execute main work tasks concurrently
5. Aggregate results and present findings

### Task Instructions

#### Task Definition Template
For each parallel task:
- Write clear, specific instructions
- Define expected outputs and format
- Include context requirements
- Specify success criteria

#### Orchestration Logic
Plan multi-wave execution:
- Wave 1: Discovery and exploration tasks
- Wave 2: Analysis and understanding tasks  
- Wave 3: Creation and implementation tasks
- Wave 4: Validation and quality assurance

### Error Handling

#### Graceful Degradation
Handle task failures:
- Continue with successful tasks
- Adapt strategy based on available results
- Provide partial results when complete execution fails
- Maintain user transparency about limitations

#### Recovery Strategies
Plan for common failure modes:
- Task timeout handling
- Incomplete result processing
- Context limitation workarounds
- Alternative approach deployment

### Performance Optimization

#### Parallel Efficiency
Maximize concurrent execution:
- Use optimal task count for problem complexity
- Minimize duplicate work across tasks
- Structure tasks for independent execution
- Plan result aggregation strategy

#### Resource Management
Optimize command resource usage:
- Balance depth vs breadth in exploration
- Manage context token allocation
- Prioritize high-value tasks
- Plan progressive disclosure of results

### User Experience

#### Progress Communication
Keep users informed:
- Explain task deployment strategy
- Provide real-time execution updates
- Show intermediate results when valuable
- Communicate completion status clearly

#### Result Presentation
Structure command outputs:
- Lead with executive summary
- Organize findings logically
- Highlight key insights and recommendations
- Provide clear next steps

### Integration Standards

#### Context Management
Handle command context:
- Load relevant historical patterns
- Update context with new learnings
- Commit valuable discoveries to Git
- Maintain cross-session continuity

#### Quality Assurance
Ensure command reliability:
- Validate task results before aggregation
- Check output quality and completeness
- Verify user requirements fulfillment
- Test edge cases and error conditions

---

**Template Usage**: Copy structure, customize for specific command purpose, maintain orchestration principles throughout.