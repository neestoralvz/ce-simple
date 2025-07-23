# `/analyze-parallel` - Parallel Execution Analysis Engine

**Purpose**: Comprehensive analysis of task plans for optimal parallel execution opportunities with aggressive optimization recommendations.

**Complexity**: 4-7 (Dynamic based on plan size)  
**Tools**: 8-24 (Analysis + Validation operations)

## 🎯 CORE FUNCTIONALITY

### Primary Operations
- **Batch Operations Analysis**: Identify tasks for simultaneous execution without conflicts
- **Dependency Mapping**: Comprehensive task dependency analysis and optimization
- **Risk Assessment**: Parallel execution safety evaluation with mitigation strategies  
- **Resource Optimization**: Maximize tool call efficiency and minimize execution time
- **Checkpoint Validation**: Ensure parallel execution maintains validation integrity

### Advanced Features
- **Conflict Detection**: Real-time identification of potential execution conflicts
- **Timing Estimation**: Precise performance projections for parallel vs sequential
- **Resource Allocation**: Optimal distribution of computational resources
- **Failure Recovery**: Parallel execution failure handling and recovery protocols

## 🚀 EXECUTION PROTOCOL

### Phase 1: Plan Discovery & Analysis (Parallel: 4-8 operations)
```javascript
// Comprehensive plan discovery
Glob("**/*plan*") +
Glob("**/*task*") + 
Glob("**/*cleanup*") +
Glob("**/*maintenance*") +
Grep("task.*list|todo.*list|phase.*\d+", {output_mode: "files_with_matches"}) +
Grep("batch.*\d+|step.*\d+|cleanup.*plan", {output_mode: "files_with_matches"}) +
Grep("parallel|concurrent|simultaneous", {output_mode: "files_with_matches"}) +
Grep("dependency|sequence|order", {output_mode: "files_with_matches"})
```

### Phase 2: Task Structure Analysis (Parallel: 6-12 operations)  
```javascript
// Deep task analysis
Read("identified_plan_file") +
Grep("^\s*\d+\.|^\s*-\s|\*\s", {output_mode: "content"}) + // List items
Grep("phase|step|batch|task", {output_mode: "content", "-C": 2}) +
Grep("depend|require|after|before", {output_mode: "content", "-C": 1}) +
Grep("parallel|concurrent|sync|async", {output_mode: "content", "-C": 1}) +
Grep("file|directory|path", {output_mode: "content"}) + // Resource conflicts
Grep("create|modify|delete|update", {output_mode: "content"}) + // Operation types
Grep("validation|check|verify|test", {output_mode: "content"}) // Checkpoints
```

### Phase 3: Parallelization Analysis (Core Algorithm)
```yaml
Dependency Graph Construction:
  - Parse task list into structured format
  - Identify explicit dependencies (after, before, requires)
  - Map resource conflicts (file modifications, database operations)
  - Build directed acyclic graph (DAG) of task relationships

Parallel Batch Identification:
  - Group independent tasks into parallel batches
  - Optimize batch sizes for resource utilization
  - Calculate parallel execution timing estimates
  - Identify bottleneck tasks and critical paths

Risk Assessment Matrix:
  - Evaluate safety of parallel execution per task
  - Identify potential race conditions and conflicts
  - Assess checkpoint integrity with parallel execution
  - Generate mitigation strategies for identified risks
```

### Phase 4: Optimization Recommendations (Parallel: 3-6 operations)
```javascript
// Performance analysis
Grep("time|duration|performance", {path: "docs/", output_mode: "content"}) +
Read("docs/core/parallelization-system.md") +
Read("docs/core/performance-system.md") +
Grep("resource|memory|cpu|network", {output_mode: "content"}) +
Bash("nproc") + // CPU core count
Bash("free -h") // Memory availability
```

## 🏗️ PARALLEL EXECUTION FRAMEWORK

### Batch Classification System
```yaml
Class A - Immediate Parallel (No Dependencies):
  - File discovery operations (Glob patterns)
  - Independent analysis tasks (Grep searches)
  - Read-only validation operations
  - Documentation generation tasks
  - Estimation: 90%+ tasks can execute immediately

Class B - Sequential Dependencies (Ordered):
  - File creation → content population
  - Directory creation → file placement  
  - Validation → correction → re-validation
  - Estimation: 15-25% require specific ordering

Class C - Resource Conflicts (Exclusive):
  - Concurrent file modifications
  - Database transaction operations
  - System configuration changes
  - Estimation: 5-10% require exclusive access

Class D - Checkpoint Dependencies (Gated):
  - Validation-dependent operations
  - Quality gate requirements
  - Approval-required changes
  - Estimation: 10-20% require checkpoint completion
```

### Optimization Strategies

#### Maximum Parallelization Pattern
```yaml
Strategy 1 - Aggressive Batching:
  - Batch Size: 8-16 parallel operations per phase
  - Resource Utilization: 85-95% target
  - Timing Target: 5-15x speed improvement
  - Risk Tolerance: Medium (with recovery protocols)

Strategy 2 - Conservative Parallel:
  - Batch Size: 4-8 parallel operations per phase
  - Resource Utilization: 70-85% target  
  - Timing Target: 3-8x speed improvement
  - Risk Tolerance: Low (high safety margins)

Strategy 3 - Hybrid Approach:
  - Class A: Maximum parallelization (16+ concurrent)
  - Class B: Sequential execution with parallel prep
  - Class C: Exclusive execution with parallel analysis
  - Class D: Parallel validation with sequential gates
```

#### Resource Allocation Framework
```yaml
CPU Optimization:
  - Core Count Assessment: Use all available cores
  - Load Distribution: Balance operations across cores
  - Priority Scheduling: Critical path tasks get priority
  - Thermal Management: Monitor sustained high utilization

Memory Optimization:
  - Operation Grouping: Batch memory-intensive tasks
  - Cache Efficiency: Optimize for data locality
  - Memory Pressure: Monitor and adjust batch sizes
  - Garbage Collection: Coordinate with high-memory phases

I/O Optimization:
  - File Access Patterns: Minimize concurrent file conflicts
  - Network Batching: Group web searches and API calls
  - Disk Scheduling: Optimize read/write operation ordering
  - Bandwidth Management: Distribute network load
```

## 🔍 ANALYSIS OUTPUT FORMAT

### Executive Summary
```yaml
Plan Analysis Results:
  Total Tasks: [count]
  Parallelizable Tasks: [count] ([percentage]%)
  Sequential Requirements: [count] ([percentage]%)
  Resource Conflicts: [count] ([percentage]%)
  
Performance Projections:
  Sequential Execution Time: [estimate]
  Parallel Execution Time: [estimate]  
  Speed Improvement: [multiplier]x
  Resource Utilization: [percentage]%
  
Risk Assessment:
  Safety Score: [score]/100
  Critical Risks: [count]
  Mitigation Strategies: [count]
```

### Detailed Batch Recommendations
```yaml
Phase 1 - Discovery (Parallel Batch):
  Tasks: [1, 3, 5, 8, 12]
  Execution: Simultaneous
  Duration: [estimate]
  Resources: [requirements]
  
Phase 2 - Analysis (Sequential):
  Tasks: [2, 4]
  Dependencies: [Phase 1 completion]
  Duration: [estimate]
  
Phase 3 - Implementation (Hybrid):
  Batch 3A: [6, 9, 11] (Parallel)
  Batch 3B: [7] (Sequential, depends on 3A)
  Batch 3C: [10, 13] (Parallel, independent)
```

### Conflict Detection Matrix
```yaml
Resource Conflicts Identified:
  - Tasks [4, 7]: Both modify file 'config.json'
  - Tasks [9, 11]: Sequential dependency (11 requires 9 output)
  - Tasks [15, 18]: Shared database table access

Mitigation Strategies:
  - File Conflicts: Implement file locking or task serialization
  - Dependencies: Ensure proper task ordering within batches
  - Database: Use transaction isolation or separate connections
```

## ⚡ PERFORMANCE OPTIMIZATION

### Timing Estimation Algorithm
```python
def calculate_parallel_timing(tasks, dependencies, resources):
    """Advanced timing estimation for parallel execution"""
    
    # Build critical path analysis
    critical_path = identify_critical_path(tasks, dependencies)
    parallel_batches = group_parallel_tasks(tasks, dependencies)
    
    # Calculate timing estimates
    sequential_time = sum(task.estimated_duration for task in tasks)
    parallel_time = max(
        batch.max_duration for batch in parallel_batches
    ) + critical_path.overhead
    
    # Resource scaling factors
    resource_factor = calculate_resource_scaling(resources)
    coordination_overhead = estimate_coordination_cost(parallel_batches)
    
    return {
        'sequential_time': sequential_time,
        'parallel_time': parallel_time * resource_factor + coordination_overhead,
        'improvement_factor': sequential_time / (parallel_time * resource_factor),
        'resource_utilization': calculate_utilization(parallel_batches, resources)
    }
```

### Real-Time Monitoring Protocol
```yaml
Execution Monitoring:
  - Task completion tracking per batch
  - Resource utilization monitoring
  - Failure detection and recovery triggers
  - Performance deviation alerts

Adaptive Optimization:
  - Dynamic batch size adjustment
  - Resource reallocation based on performance
  - Failure recovery and task redistribution
  - Real-time strategy switching
```

## 🎯 COMMAND INTEGRATION

### Auto-Trigger Conditions
- **Plan Detection**: When task list with 8+ items detected
- **Performance Request**: Explicit parallel optimization requests
- **Complexity Threshold**: Commands with complexity ≥6
- **Resource Optimization**: System performance optimization needs

### Cross-Command Integration  
```yaml
Integration Points:
  - /matrix-maintenance: Validate parallelization impact on system integrity
  - /context-optimize: Optimize documentation for parallel execution patterns
  - /worktree-start: Initialize isolated environments for parallel testing
  - /capture-learnings: Document parallel execution patterns and outcomes
```

### Success Metrics
```yaml
Performance Targets:
  - 5-15x speed improvement for parallelizable tasks
  - <5% failure rate with parallel execution
  - >90% resource utilization efficiency
  - <2% overhead for coordination costs

Quality Assurance:
  - 100% task completion (no lost operations)
  - Maintained checkpoint integrity
  - Zero data corruption incidents
  - >95% user satisfaction with parallel results
```

---

**CRITICAL**: This command provides comprehensive parallel execution analysis with aggressive optimization while maintaining safety through systematic risk assessment and mitigation strategies.