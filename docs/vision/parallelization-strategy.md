# Parallelization Strategy

## 🚀 Core Philosophy

Parallelization is not an optimization—it's the **default operating mode**. Every operation that CAN be parallel SHOULD be parallel.

## 🎯 Parallelization Principles

### 1. Parallel-First Mindset
```yaml
Default Assumption: Tasks are independent
Proof Required: For sequential execution
Question Always: "Why can't this be parallel?"
```

### 2. Independence Analysis
```yaml
Independent Operations:
  - Different files
  - Different search queries
  - Different analysis perspectives
  - Separate validations

Dependent Operations:
  - Output feeds next input
  - Shared state modifications
  - Ordered business logic
  - Resource constraints
```

### 3. Granularity Optimization
```yaml
Too Coarse: Underutilizes parallelism
Too Fine: Overhead exceeds benefit
Just Right: Meaningful work units
```

## 📊 Parallelization Patterns

### Core Operation Types
- **Search Operations**: Maximum parallelization (20x speedup)
- **File Operations**: Git WorkTree isolation (10x speedup)
- **Analysis Operations**: Multiple perspectives (4x speedup)
- **Validation Operations**: Distributed testing (minutes vs hours)

See [parallelization-strategy-details.md](parallelization-strategy-details.md) for complete pattern examples and implementation strategies.

## 🔧 Implementation Strategies

### The 7-Parallel-Tasks Method
```yaml
Optimal for: Component development
Tasks:
  1. Core component logic
  2. Styling and appearance
  3. Test suite creation
  4. Type definitions
  5. Utility functions
  6. Integration points
  7. Documentation

Why 7?: 
  - Balances overhead vs benefit
  - Clear separation of concerns
  - Manageable aggregation
```

### Wave-Based Execution
```yaml
When: Multi-stage workflows
Pattern:
  Wave 1: All discovery tasks
  Wave 2: All analysis tasks
  Wave 3: All creation tasks
  Wave 4: All validation tasks

Benefits:
  - Clear stage boundaries
  - Easy progress tracking
  - Natural checkpoints
```

### Dynamic Parallelization
```yaml
Concept: Adjust based on findings
Flow:
  1. Initial probe (1-3 tasks)
  2. Analyze scope
  3. Calculate optimal parallelization
  4. Deploy calculated tasks

Example:
  - Small codebase: 4 parallel
  - Medium codebase: 8 parallel
  - Large codebase: 10 parallel
```

## 🎪 Advanced Techniques

### Competitive Parallelization
```yaml
Use Case: Critical operations
Strategy:
  - Same task, different approaches
  - Compare results
  - Select best outcome

Example:
  - 3 different search strategies
  - 3 different fix approaches
  - Choose most effective
```

### Hierarchical Parallelization
```yaml
Concept: Parallel tasks spawn parallel subtasks
Implementation:
  - Main command: 5 high-level tasks
  - Each task: Handles subsection
  - Natural work distribution

Caution: Sub-agents can't spawn tasks
Solution: Pre-plan hierarchy
```

### Resource-Aware Parallelization
```yaml
Monitoring:
  - File system load
  - API rate limits
  - Memory usage
  - Network capacity

Adaptation:
  - Reduce parallelism if constrained
  - Queue tasks if at limit
  - Batch similar operations
```

## 📈 Performance Metrics

### Speedup Calculations
```yaml
Linear Operations:
  Sequential: O(n)
  Parallel: O(n/p) where p = parallel tasks
  Speedup: Near p times

Complex Operations:
  Consider: Aggregation overhead
  Formula: Speedup = n/(n/p + overhead)
  Typical: 60-80% of theoretical max
```

### Optimal Parallelization Levels
```yaml
Search Tasks: 8-16 parallel
File Operations: 5-10 parallel
Analysis Tasks: 4-8 parallel
Creation Tasks: 3-7 parallel
Validation Tasks: 5-10 parallel
```

## 🚨 Anti-Patterns

### Over-Parallelization
```yaml
Problem: Overhead exceeds benefit
Signs:
  - Tasks complete instantly
  - Aggregation takes longer
  - Resource contention

Solution: Larger work units
```

### False Dependencies
```yaml
Problem: Assuming sequential need
Signs:
  - "Must do X before Y"
  - Linear thinking
  - Slow execution

Solution: Challenge assumptions
```

### Shared State Trap
```yaml
Problem: Hidden dependencies
Signs:
  - Race conditions
  - Inconsistent results
  - Merge conflicts

Solution: True isolation
```

## 💡 Parallelization Checklist

### Before Implementation
- [ ] Can tasks run independently?
- [ ] Is work unit size appropriate?
- [ ] Are outputs mergeable?
- [ ] Is isolation complete?
- [ ] Are instructions self-contained?

### During Execution
- [ ] Monitor resource usage
- [ ] Track completion rates
- [ ] Validate partial results
- [ ] Handle failures gracefully

### After Completion
- [ ] Measure actual speedup
- [ ] Identify bottlenecks
- [ ] Refine for next time
- [ ] Document patterns

### Validation Procedures
- [ ] Test with different parallelization levels
- [ ] Verify result consistency
- [ ] Measure performance impact
- [ ] Document optimal configurations

---

**Key Insight**: Parallelization isn't about making things faster—it's about doing more things at once. The magic happens when 10 tasks complete in the time of 1.