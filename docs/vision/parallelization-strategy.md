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

### Core Methods
- **7-Parallel-Tasks Method**: Optimal for component development
- **Wave-Based Execution**: Multi-stage workflows with checkpoints
- **Dynamic Parallelization**: Adjust based on scope findings

See [parallelization-strategy-details.md](parallelization-strategy-details.md) for complete implementation details and examples.

## 🎪 Advanced Techniques

### Specialized Approaches
- **Competitive Parallelization**: Multiple approaches, best result
- **Hierarchical Parallelization**: Pre-planned task hierarchies
- **Resource-Aware Parallelization**: Dynamic adaptation to constraints

See [parallelization-strategy-details.md](parallelization-strategy-details.md) for complete advanced technique specifications.

## 📈 Performance Metrics

### Speedup Guidelines
- **Linear Operations**: Near p times speedup
- **Complex Operations**: 60-80% of theoretical max
- **Optimal Levels**: 3-16 parallel depending on task type

See [parallelization-strategy-details.md](parallelization-strategy-details.md) for complete metrics and calculation formulas.

## 🚨 Anti-Patterns

### Common Problems
- **Over-Parallelization**: Overhead exceeds benefit
- **False Dependencies**: Assuming sequential need
- **Shared State Trap**: Hidden dependencies causing conflicts

See [parallelization-strategy-details.md](parallelization-strategy-details.md) for complete anti-pattern identification and solutions.

## 💡 Parallelization Checklist

### Before Implementation
- [ ] Task independence verified
- [ ] Work unit size appropriate
- [ ] Outputs mergeable
- [ ] Complete isolation
- [ ] Self-contained instructions

### During Execution
- [ ] Resource usage monitored
- [ ] Completion rates tracked
- [ ] Partial results validated
- [ ] Failures handled gracefully

### After Completion
- [ ] Actual speedup measured
- [ ] Bottlenecks identified
- [ ] Strategy refined
- [ ] Patterns documented

See [parallelization-strategy-details.md](parallelization-strategy-details.md) for expanded checklists and validation procedures.

---

**Key Insight**: Parallelization isn't about making things faster—it's about doing more things at once. The magic happens when 10 tasks complete in the time of 1.