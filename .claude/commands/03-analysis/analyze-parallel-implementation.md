# analyze-parallel-implementation

## Purpose

Executes comprehensive task plan analysis for optimal parallel execution through dependency mapping providing performance improvements with safety protocols and resource efficiency.

## Principles

- **Single Responsibility**: Focus on task plan analysis without execution implementation
- **Granular Approach**: Break task discovery into dependency mapping with clear phases
- **Resource Management**: Handle execution graphs with explicit optimization requirements
- **Error Recovery**: Built-in discovery retry mechanisms and classification fallbacks

## Execution Process

### Phase 1: Task Discovery Analysis
Mark "Task Discovery and Structure Analysis" as in_progress using TodoWrite

Execute task plan discovery:
- Discover all task plans using file discovery methods
- Parse task definitions and extract execution requirements
- Classify task types and identify parallelization candidates
- Extract constraints through pattern analysis methods

Use Glob to discover plans:
- File discovery achieving task identification
- Structure analysis with requirement extraction

If discovery failures occur:
- Add TodoWrite task: "Resolve discovery error: expanded search patterns"
- Execute expanded search pattern retry for failures
- Validate discovery completeness ensuring task coverage
- Continue with validated task classification

Complete previous phase, mark "Dependency Mapping and Batch Classification" as in_progress using TodoWrite

### Phase 2: Dependency Mapping
Mark "Dependency Mapping and Batch Classification" as in_progress using TodoWrite

Execute relationship building:
- Build directed acyclic graph of task relationships
- Group tasks into optimal parallel execution batches
- Classify execution types and identify conflict requirements
- Generate batch strategies based on dependency constraints

Use Read to build graphs:
- Graph building achieving relationship mapping
- Batch optimization with conflict detection

If classification ambiguity occurs:
- Add TodoWrite task: "Resolve classification error: conservative fallback"
- Execute conservative sequential classification for ambiguous tasks
- Validate classification accuracy ensuring execution safety
- Continue with validated batch strategies

Complete previous phase, mark "Performance Analysis and Risk Assessment" as in_progress using TodoWrite

### Phase 3: Performance Analysis
Mark "Performance Analysis and Risk Assessment" as in_progress using TodoWrite

Execute timing calculation:
- Calculate timing estimates and resource utilization
- Evaluate execution safety and generate mitigation strategies
- Analyze resource constraints and identify bottlenecks
- Generate risk assessment results for execution batches

Use Bash to calculate timing:
- Timing calculation achieving resource estimation
- Safety evaluation with mitigation strategies

If projection validation issues occur:
- Add TodoWrite task: "Resolve projection error: benchmarking validation"
- Execute performance benchmarking validation for accuracy
- Validate projection reliability ensuring implementation confidence
- Continue with validated performance analysis

Complete previous phase, mark "Strategy Synthesis and Optimization Recommendations" as in_progress using TodoWrite

### Phase 4: Strategy Synthesis
Mark "Strategy Synthesis and Optimization Recommendations" as in_progress using TodoWrite

Execute implementation strategy:
- Synthesize batch execution strategies with timing estimates
- Generate implementation recommendations with improvement projections
- Create optimization strategies with safety protocols
- Provide resource efficiency guidelines for execution

Use Write to synthesize strategy:
- Strategy synthesis achieving implementation guidance
- Optimization generation with safety protocols

If synthesis validation gaps occur:
- Add TodoWrite task: "Resolve synthesis gap: comprehensive validation"
- Execute comprehensive validation for implementation plans
- Validate synthesis completeness ensuring executable guidance
- Complete analysis with validated optimization strategies

Complete all tasks using TodoWrite

---

**Task plan analysis executes parallel optimization providing implementation strategies.**