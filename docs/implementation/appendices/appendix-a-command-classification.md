# Appendix A: Command Classification Matrices

**Reference**: Concurrent Bash Execution - Safety and Coordination Guide  
**Last Updated**: 2025-07-22

## Complete Command Safety Categories

```
COMMAND SAFETY CATEGORIES:
├─ SAFE_PARALLEL (8-16 instances)
│  ├─ Read-only operations (ls, cat, grep, find)
│  ├─ Status queries (git status, ps, df, top)
│  ├─ Analysis commands (wc, sort, uniq, awk)
│  └─ Non-destructive utilities (date, whoami, uname)
├─ CONDITIONAL_PARALLEL (4-8 instances)
│  ├─ Build operations (make, npm build, cargo build)
│  ├─ Test execution (pytest, npm test, go test)
│  ├─ Package operations (npm install, pip install)
│  └─ Compilation (gcc, javac, rustc)
├─ SEQUENTIAL_REQUIRED (1 instance)
│  ├─ File modifications (mv, cp, rm, chmod)
│  ├─ Git operations (commit, push, merge, rebase)
│  ├─ Database operations (migrations, schema changes)
│  └─ System modifications (service start/stop, config changes)
└─ DANGEROUS_ISOLATED (1 instance with locks)
   ├─ Destructive operations (rm -rf, format, truncate)
   ├─ System-wide changes (apt update, yum install)
   ├─ Network modifications (iptables, route changes)
   └─ Process termination (kill -9, pkill)
```

## Intelligent Command Batching Strategies

```
BATCHING ALGORITHMS:

1. DIRECTORY-BASED BATCHING:
┌─ Batch 1: ./src/ operations (4 instances)
├─ Batch 2: ./test/ operations (4 instances)  
├─ Batch 3: ./docs/ operations (2 instances)
├─ Batch 4: ./config/ operations (2 instances)
├─ Batch 5: ./scripts/ operations (2 instances)
└─ Batch 6: ./build/ operations (2 instances)

2. COMMAND-TYPE BATCHING:
┌─ Analysis Batch: grep, awk, sed, sort (6 instances)
├─ Build Batch: make, npm, cargo, go (4 instances)
├─ Test Batch: pytest, jest, mocha, go test (4 instances)
└─ Status Batch: git status, ps, df, ls (2 instances)

3. DEPENDENCY-AWARE BATCHING:
┌─ Independent Commands: No dependencies (8-12 instances)
├─ Chain Commands: Sequential dependencies (2-4 instances)
├─ Tree Commands: Hierarchical dependencies (4-6 instances)
└─ Network Commands: Cross-dependencies (1-2 instances)
```

## Resource Conflict Detection Matrix

```
CONFLICT DETECTION MATRIX:
                │ File │ Dir │ Process │ Network │ Memory │
├─ Read Ops     │  ✓   │  ✓  │    ✓    │    ✓    │   ✓    │
├─ Write Ops    │  ⚠   │  ⚠  │    ⚠    │    ⚠    │   ✓    │
├─ Create Ops   │  ⚠   │  ⚠  │    ✓    │    ⚠    │   ✓    │
├─ Delete Ops   │  ✗   │  ✗  │    ⚠    │    ⚠    │   ✓    │
├─ Modify Ops   │  ⚠   │  ⚠  │    ⚠    │    ⚠    │   ✓    │
└─ System Ops   │  ✗   │  ✗  │    ✗    │    ✗    │   ⚠    │

LEGEND: ✓ Safe | ⚠ Conditional | ✗ Restricted

CONFLICT RESOLUTION STRATEGIES:
├─ File Locks: Exclusive write access with queue management
├─ Directory Locks: Hierarchical locking with inheritance
├─ Process Locks: PID-based resource claiming
├─ Network Locks: Port and interface reservation
└─ Resource Semaphores: Bounded concurrent access control
```

## Advanced Priority Scoring Algorithm

```
PRIORITY CALCULATION MATRIX:

Base Priority Factors:
├─ Command Safety Level (1-10 scale)
│  ├─ Safe operations: 8-10 (high priority)
│  ├─ Conditional operations: 5-7 (medium priority)
│  ├─ Sequential operations: 3-4 (low priority)
│  └─ Dangerous operations: 1-2 (minimal priority)
├─ Resource Requirements (1-10 scale)
│  ├─ Low resource: 8-10 (high priority)
│  ├─ Medium resource: 5-7 (medium priority)
│  ├─ High resource: 3-4 (low priority)
│  └─ System resource: 1-2 (minimal priority)
├─ Execution Time Estimate (1-10 scale)
│  ├─ Quick (<1s): 10 (highest priority)
│  ├─ Fast (1-10s): 8-9 (high priority)
│  ├─ Moderate (10-60s): 5-7 (medium priority)
│  ├─ Slow (1-10min): 3-4 (low priority)
│  └─ Very slow (>10min): 1-2 (minimal priority)
└─ User Priority Override (1-10 scale)
   ├─ Critical: 10 (absolute priority)
   ├─ High: 8-9 (high priority)
   ├─ Normal: 5-7 (default priority)
   ├─ Low: 3-4 (background priority)
   └─ Deferred: 1-2 (eventual execution)

COMPOSITE PRIORITY SCORE:
Priority = (Safety * 0.3) + (Resource * 0.25) + (Time * 0.25) + (User * 0.2)
```

## Scheduling Algorithm Specifications

```
SCHEDULING STRATEGIES:

1. ROUND-ROBIN WITH PRIORITY:
   ├─ High-priority queue (8-10): 60% allocation
   ├─ Medium-priority queue (5-7): 30% allocation
   ├─ Low-priority queue (1-4): 10% allocation
   └─ Dynamic rebalancing based on queue lengths

2. SHORTEST JOB FIRST (SJF):
   ├─ Estimated execution time sorting
   ├─ Starvation prevention (aging mechanism)
   ├─ Preemptive vs non-preemptive options
   └─ Learning from actual execution times

3. RESOURCE-AWARE SCHEDULING:
   ├─ CPU-intensive operations batching
   ├─ I/O-intensive operations parallelization
   ├─ Memory-constrained operations sequencing
   └─ Network-bound operations aggregation

4. DEPENDENCY-DRIVEN SCHEDULING:
   ├─ Topological sort execution order
   ├─ Critical path optimization
   ├─ Parallel execution of independent branches
   └─ Dynamic dependency resolution
```