# Performance Framework - Consolidated

**Updated**: 2025-07-26 | **Authority**: Core performance metrics  
**Source**: Consolidated from frameworks/performance-framework.md  
**Purpose**: Comprehensive performance monitoring and benchmarks for parallel operations

## Performance Targets

### Scale-Based Performance Standards

**Small Codebase (< 1000 files)**
- Analysis completion: < 30 seconds
- Quality target: > 95% accuracy
- Error rate: < 1% operation failures
- Resource utilization: < 50% system capacity
- Parallel operations: 12 (4 Glob + 6 Grep + 2 Read)

**Medium Codebase (1000-10000 files)**
- Analysis completion: < 3 minutes
- Quality target: > 90% accuracy
- Error rate: < 2% operation failures
- Resource utilization: 50-80% system capacity
- Parallel operations: 24 (8 Glob + 12 Grep + 4 Read)

**Large Codebase (10000-100000 files)**
- Analysis completion: < 15 minutes
- Quality target: > 85% accuracy
- Error rate: < 5% operation failures
- Resource utilization: 80-95% system capacity
- Parallel operations: 52 (16 Glob + 24 Grep + 12 Read)

### Command-Specific Benchmarks

**/start Workflow**
- Context gathering: < 2 minutes
- Agent deployment: < 30 seconds
- Total completion: < 15 minutes
- Quality score: > 90%

**/explore-codebase**
- Small projects: < 1 minute (12 operations)
- Medium projects: < 5 minutes (24 operations)
- Large projects: < 20 minutes (52 operations)
- Accuracy rate: > 92%

**/init-project**
- Basic setup: < 30 seconds
- Full initialization: < 2 minutes
- Quality validation: > 95%

## Concurrent Operations Framework

### Optimal Parallelization Ranges

**Task Tool Parallelization**
- Optimal Range: 3-8 concurrent operations
- Maximum Effective: 12 concurrent operations
- Critical Threshold: 15 operations (performance degradation)
- Recovery Protocol: Scale down to optimal range

**MultiEdit Operations**
- Single File Optimization: 3-5 edits per operation
- Complex Refactoring: 8-12 edits per operation
- Cross-File Coordination: Use parallel Task Tools instead

---
**Authority References**: [PTS Framework](pts-framework-consolidated.md) | [Task Orchestration](task-orchestration.md)