# Development Standards - ce-simple System

**Complete development standards for command creation, documentation, and system maintenance**  
**Last Updated:** 2025-07-23

## Core Standards

### Command Development Requirements

Every slash command MUST be:
1. **Self-contained**: All logic included, no external dependencies
2. **Orchestration-focused**: Commands coordinate, tasks execute
3. **Parallel-optimized**: Default to concurrent execution patterns
4. **Error-resilient**: Handle all failure modes gracefully
5. **Learning-enabled**: Improve performance with usage patterns
6. **Foundation-integrated**: Leverage 00-core infrastructure when applicable

### Foundation Integration Guidelines

Commands should integrate with foundation layer infrastructure:
- **Notifications**: Use notify-manager for transparent delegation tracking
- **Context Management**: Leverage context-engine for distributed memory coherence
- **State Transitions**: Use handoff-manager for seamless workflow phase transitions
- **Project Initialization**: Reference init-project for new project setup patterns

## Command Structure Standards

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

### Task Orchestration Framework

Must include orchestration specification:
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

### Error Handling Standards

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

## Documentation Standards

### Writing Principles

**Simple & Direct, But Complete**
- Clear on first read
- Essential information only
- Complete context provided
- Immediately actionable instructions

### Word Economy Standards
- Every word must contribute value
- Remove unnecessary phrases and fluff
- Focus on action verbs and specific nouns
- Eliminate redundancy - each concept appears once
- Remove "should", "might", "perhaps" qualifiers

### Length Limits
- **Commands**: ≤150 lines maximum
- **Documentation**: ≤200 lines maximum  
- **Patterns**: ≤100 lines maximum

### Progressive Disclosure Strategy

Extract to separate files when content is:
- Rarely needed during daily execution
- Complex details requiring deep study
- Reference material or templates

Keep in main file when content is:
- Used frequently (daily/weekly)
- Essential for basic understanding

### Import Strategies

**@ Import Syntax** (Preferred for Claude Code CLI):
```markdown
@docs/core/project-structure.md
@docs/commands/command-index.md
```
- Automatically includes complete file contents
- Eliminates duplication
- Dynamic updates when imported files change

**Reference Format** (Alternative):
```markdown
[See filename](filename.md) for [specific details]
```
- Use when @ imports not available
- Better for interactive navigation

### Natural Language Instructions

Write direct commands:
```
GOOD: "Search TypeScript files for function definitions"
BAD: "Glob('**/*.ts', {pattern: 'function'})"

GOOD: "Create component with error handling"
BAD: "const component = createComponent({errorBoundary: true})"
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
- **Total execution**: Documented estimate with rationale

### Documentation Quality
- **Purpose clarity**: Understandable in single read
- **Usage examples**: At least 3 real scenarios
- **Error scenarios**: All failure modes documented
- **Performance notes**: Expected timings included

## File Organization Standards

### Naming Conventions
- **Core files**: `topic.md`
- **Detailed content**: `topic-details.md`
- **Examples**: `topic-examples.md`
- **Advanced content**: `topic-advanced.md`

Use lowercase, hyphens for spaces, descriptive but concise names.

### Document Structure Template

```markdown
# [Document Title]

## Purpose
[Single paragraph explaining why this document exists and what value it provides]

## Overview
[2-3 paragraphs providing high-level context and scope]

## Key Concepts

### [Concept 1]
[Definition and explanation]

### [Concept 2]
[Definition and explanation]

## Detailed Information

### [Section 1]
[Detailed content with examples]

### [Section 2]  
[Detailed content with code samples]

## Best Practices
- **Do**: [Recommended approach]
- **Don't**: [Anti-pattern to avoid]
- **Consider**: [Contextual advice]

## Examples

### Example 1: [Basic Usage]
[Description and code example with expected outcome]

### Example 2: [Advanced Usage]
[Description and code example with expected outcome]

## Related Documents
- [Related Doc]: [Brief description]

---

**Last Updated**: [Date]
**Status**: [Draft | Review | Final]
```

## Anti-Patterns

### Command Anti-Patterns
- **God commands**: Doing too much in one command
- **Hidden dependencies**: Assuming external state
- **Sequential thinking**: Not leveraging parallelism
- **Poor error handling**: Letting failures cascade
- **No learning**: Not capturing improvement patterns

### Documentation Anti-Patterns
- **Programming code**: No implementation details
- **Theoretical explanations**: No academic content
- **Redundant phrases**: Avoid repetitive language
- **Meta-commentary**: No discussion about documentation
- **Verbose instructions**: >15 words per instruction
- **Vague descriptions**: Unclear or ambiguous language

## Quality Assurance

### Pre-Submission Checklist
- [ ] Command is fully self-contained
- [ ] All required sections documented
- [ ] Task orchestration strategy clear
- [ ] Error handling complete
- [ ] Performance metrics documented
- [ ] Real usage examples provided
- [ ] Patterns embedded where applicable
- [ ] Learning mechanism included
- [ ] Foundation integration considered

### Review Criteria
- [ ] Parallelization optimized (≥70%)
- [ ] Instructions clear and actionable
- [ ] Output format standardized
- [ ] Errors handled gracefully
- [ ] Code within size limits
- [ ] Anti-patterns avoided
- [ ] Word economy principles applied

### Quality Validation Questions
- Can I execute this immediately?
- Does every word contribute value?
- Would removing any word make it unclear?
- Is this the simplest way to express it?
- Would this need re-reading for comprehension?

## Excellence Indicators

A command demonstrates excellence when:
1. **Execution is 10x faster** than manual approach
2. **Parallelization exceeds 80%** of operations
3. **Error recovery is automatic** and transparent
4. **Learning improves performance** over time
5. **User experience is seamless** despite complexity

## Continuous Improvement

### When to Improve Documentation
- Users confused during execution
- Instructions require re-reading
- Content feels unnecessarily complex
- Words exist without clear purpose
- Performance degrades over time

### Learning Integration
Commands should capture and apply patterns from:
- Execution success/failure rates
- User interaction patterns
- Performance optimization discoveries
- Error resolution strategies
- Workflow efficiency improvements

---

**Standard Commitment**: Every command and document we create will be a masterpiece of orchestration—simple to use, powerful in execution, and continuously improving through systematic quality standards and learning integration.