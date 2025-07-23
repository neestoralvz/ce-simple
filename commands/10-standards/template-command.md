# Command Template - Standard Structure

**Purpose**: Standard template for creating new commands with 4-section structure

## Template Structure

```markdown
# /command-name - Brief Description

**Purpose**: Single line describing command function

## Implementation

**Orchestration Strategy**: [parallel|sequential|hybrid] - Brief justification

**Context Requirements**: List specific context needs
- Context type 1: purpose
- Context type 2: purpose

**Task Breakdown**:
1. **Discovery Phase**: Identify requirements and constraints
2. **Analysis Phase**: Process information and determine approach
3. **Execution Phase**: Implement solution with validation
4. **Completion Phase**: Finalize and document results

## Execution Protocol

### Phase 1: Discovery
- Use dynamic questioning for requirement clarification
- Validate input parameters and constraints
- Identify dependencies and prerequisites

### Phase 2: Analysis  
- Process gathered information
- Determine optimal approach and orchestration strategy
- Plan task sequence and parallel opportunities

### Phase 3: Execution
- Execute tasks using identified orchestration pattern
- Apply validation at each step
- Handle errors and edge cases

### Phase 4: Completion
- Consolidate results
- Provide summary with file paths (absolute)
- Update relevant context if needed

## Validation Checklist

- [ ] Command ≤150 lines
- [ ] Self-contained execution
- [ ] Natural language instructions
- [ ] Parallel execution where beneficial
- [ ] Error handling included
- [ ] Absolute file paths in output
- [ ] Context system integration
```

## Usage Examples

### Basic Command Structure
```markdown
# /analyze-performance - System Performance Analysis

**Purpose**: Analyze codebase performance bottlenecks using multi-dimensional assessment

## Implementation

**Orchestration Strategy**: parallel - Enable simultaneous analysis of different performance vectors

**Context Requirements**: 
- Performance metrics: baseline measurements
- Codebase structure: architectural understanding

**Task Breakdown**:
1. **Discovery Phase**: Identify performance measurement points
2. **Analysis Phase**: Execute parallel performance assessments  
3. **Execution Phase**: Generate optimization recommendations
4. **Completion Phase**: Consolidate findings with prioritized action plan
```

### Guidelines

**Naming Convention**: Use verbo-sustantivo pattern (analyze-performance, create-component)

**Structure Requirements**:
- Always include 4 phases
- Specify orchestration strategy with justification
- Include validation checklist
- Provide absolute file paths in results

**Content Standards**:
- ≤15 words per instruction
- Natural language for Claude Code execution
- Clear task granularity
- Self-contained operation

## Validation Checklist

- [ ] Template includes complete 4-section structure
- [ ] Examples demonstrate proper usage
- [ ] Guidelines specify naming conventions
- [ ] Validation checklist included
- [ ] ≤150 lines total