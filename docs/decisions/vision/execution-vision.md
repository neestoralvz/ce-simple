# Execution Strategies

**Updated**: 2025-07-26 12:00 (Mexico City) | **Authority**: Parallelization & orchestration vision | **Lines**: ≤80

## Core Parallelization Philosophy
Parallelization is not optimization—it's the default operating mode. Every operation that CAN be parallel SHOULD be parallel.

## Fundamental Patterns

**Seven-Parallel-Tasks Pattern**: Most efficient for component development:
1. Component creation | 2. Styles/CSS | 3. Tests | 4. Type definitions | 5. Hooks/utilities | 6. Integration updates | 7. Documentation
All in parallel → 7x speedup

**Scatter-Gather Pattern**: Information collection & synthesis:
- Scatter: Deploy multiple search tasks with different strategies
- Gather: Collect results, synthesize findings, identify patterns

**Wave Deployment Pattern**: Complex multi-stage workflows:
- Wave 1: Discovery (parallel exploration, context gathering)
- Wave 2: Analysis (process discoveries, apply think layers)  
- Wave 3: Creation (generate solutions, parallel development)
- Wave 4: Validation (test outputs, verify success)

**Competitive Redundancy Pattern**: Critical operations requiring reliability:
Multiple agents same task with different approaches → Compare results → Select best outcome

## Advanced Techniques

**Git-Based Intelligence**: Orchestration driven by Git metrics & autonomous decision making:
- Commit patterns & success indicators for optimal command sequence selection
- Branch lifecycle data for resource allocation
- Performance timeline analysis for recovery strategy selection
- Usage analysis triggers for new command creation

**Dynamic Task Generation**: Create tasks based on discovery:
Initial exploration → Analyze findings → Generate specific tasks → Deploy dynamically

**Resource-Aware Parallelization**: Monitor file system load, API limits, memory usage → Adapt parallelism levels accordingly

## Performance Optimization

**Parallelization Guidelines**: Always parallel first (assume independence) | Batch wisely (group related operations) | Limit scope (focused tasks perform better) | Clear boundaries (no overlapping responsibilities)

**Optimal Levels**: Search tasks (8-16 parallel) | File operations (5-10 parallel) | Analysis tasks (4-8 parallel) | Creation tasks (3-7 parallel) | Validation tasks (5-10 parallel)

**Case Studies**: Large refactoring (50 files, 4 hours → 15 minutes) | Bug hunting (2 days → 30 minutes) | Feature development (1 week → 1 day)

## Implementation Vision
**Best Practices**: Plan parallelization upfront | Design clear task boundaries | Standardize output formats | Build aggregation logic | Handle partial failures

---

**Execution Vision**: Maximum productivity through intelligent parallel orchestration with autonomous decision making.