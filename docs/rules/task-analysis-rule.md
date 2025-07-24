# Task Analysis Rule

**Authority**: Modular Rule System  
**Prerequisite**: Analysis before execution

## Mandatory Analysis Framework

### Dependency Matrix [D]
```
D = {(ti,tj) | ti must complete before tj}
Independent: I = {ti | ∄tj: (ti,tj) ∈ D ∨ (tj,ti) ∈ D}
```

### Parallelization Decision
```yaml
parallel_if:
  - |I| ≥ 2 AND resource_conflict = ∅
  - similarity_score(ti,tj) > 0.8
  - estimated_time(sequential) > 2×estimated_time(parallel)
```

## Analysis Patterns

### File Operations
- **Batch**: Read multiple files → `{f1,f2,...fn}` → single Read[] call
- **Transform**: Similar edits → MultiEdit with sequential operations
- **Create**: Multiple new files → parallel Write[] operations

### API/Search Operations  
- **Similarity**: Group by pattern/domain → batch requests
- **Independence**: No shared state → full parallel execution

### Validation Operations
- **Layer**: Independent checks → parallel validation agents
- **Cascade**: Dependent results → sequential with early exit

## Decomposition Examples

```yaml
Task: "Update all test files and run validation"
Analysis:
  Dependencies: update_files → run_tests
  Parallel_ops: [Read all tests, Group by type]
  Sequential: [Apply updates, Execute validation]
  
Task: "Search codebase for patterns and document"
Analysis:  
  Independent: [Grep patterns, Read docs]
  Parallel_batch: [[pattern1,pattern2,pattern3]]
  Synthesis: Consolidate findings → Write doc
```

## Implementation Protocol
1. Analyze task graph → identify |I|
2. Check resource conflicts (file locks, API limits)
3. Calculate speedup factor
4. Apply @parallel-execution-rule patterns
5. Monitor and adapt based on results

**Optimization**: Tasks with |I| > 3 mandatory parallel consideration