# Analyze Parallel - Parallelization Opportunity Detection

## Purpose
Detect parallelization opportunities and optimize performance through intelligent workload analysis, resource allocation, and bottleneck identification with measurable improvements.

## Principles and Guidelines
- **Pattern Detection**: Identify sequential operations that can be parallelized through codebase analysis
- **Dependency Analysis**: Map operation dependencies and execution chains to optimize resource allocation
- **Resource Assessment**: Evaluate available processing capacity and bottleneck identification
- **Optimization Scoring**: Rank improvements by impact/effort ratio with >20% performance improvement targets

## Execution Process

### Phase 1: Codebase Scanning and Pattern Detection
```javascript
TodoWrite([
  {"content": "Scan codebase for parallelizable patterns: for/while/map/forEach, async/await, Promise.all", "status": "pending", "priority": "high", "id": "parallel-scan-1"},
  {"content": "Identify large files and iteration patterns for optimization opportunities", "status": "pending", "priority": "high", "id": "parallel-identify-1"}
])
```

### Phase 2: Bottleneck Detection and Analysis
```javascript
TodoWrite([
  {"content": "Detect blocking operations: sleep/delay/timeout/throttle patterns", "status": "pending", "priority": "high", "id": "parallel-bottleneck-1"},
  {"content": "Find sequential patterns and synchronous operations for parallelization", "status": "pending", "priority": "high", "id": "parallel-sequential-1"}
])
```

### Phase 3: Performance Analysis and Optimization Strategy
```javascript
TodoWrite([
  {"content": "Analyze codebase for parallelization opportunities and generate optimization recommendations", "status": "pending", "priority": "high", "id": "parallel-analyze-1"},
  {"content": "Measure current performance metrics and establish optimization targets", "status": "pending", "priority": "medium", "id": "parallel-baseline-1"}
])
```

### Phase 4: Optimization Scoring and Implementation Recommendations
```javascript
TodoWrite([
  {"content": "Rank optimization opportunities by impact/effort ratio", "status": "pending", "priority": "high", "id": "parallel-rank-1"},
  {"content": "Generate specific implementation recommendations with performance projections", "status": "pending", "priority": "medium", "id": "parallel-implement-1"}
])
```

## Workload Analysis Framework

### Pattern Detection Categories
**Parallelizable Patterns**: for/while loops, map/forEach operations, async/await chains, Promise.all opportunities
**Blocking Operations**: sleep/delay/timeout/throttle patterns, synchronous file operations, sequential API calls
**Resource Conflicts**: Concurrent file modifications, shared state access, database transaction bottlenecks

### Performance Assessment Criteria
**Optimization Targets**:
- >20% performance improvement in identified bottlenecks
- 90%+ coverage of parallelizable operations identified
- Measurable gains through benchmark validation

**Analysis Integration**:
- Baseline metrics establishment through performance tracking
- Real-time optimization validation via system monitoring
- Isolated optimization testing via git worktree environments

## Resource Optimization Framework

### Performance Benchmarking Integration
**Measurement Protocol**: Integrate with `/system-monitor performance` for baseline metrics and benchmarking
**Environment Setup**: Use `/git-worktree` for isolated optimization testing environments
**Validation Process**: Apply `/system-monitor development` for real-time optimization validation

### Success Indicators
**Detection Success**: 90%+ coverage of parallelizable operations identified across codebase
**Optimization Success**: >20% performance improvement in identified bottlenecks with measurable validation
**Implementation Success**: Recommendations successfully applied with benchmark-proven gains

---

**Single Responsibility**: Parallelization opportunity detection engine providing intelligent workload analysis with measurable optimization recommendations and performance improvement validation.