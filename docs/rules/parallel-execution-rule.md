# Parallel Execution Rule | Mandatory Task Tool Parallelization

**Authority**: Core Rule Module | **Enforcement**: Blocking | **Updated**: 2025-07-24

## Trigger Criteria | When Parallel Required
**3+ Similar Tasks Rule**: ANY operation with ≥3 similar/repetitive tasks MUST use parallel Task Tools
- File operations: Read/Write/Edit across multiple files
- Analysis tasks: Similar evaluations across domains  
- Validation checks: Multiple components requiring same verification
- Search operations: Pattern matching across directories

**10-Agent Limit**: Claude Code maximum concurrent sub-agents | Deploy in waves if >10 needed

## Execution Patterns | Good vs Bad

### ❌ BAD: Sequential Execution
```bash
# VIOLATION: 5 similar reads done sequentially
Read file1.js → Read file2.js → Read file3.js → Read file4.js → Read file5.js
```

### ✅ GOOD: Parallel Execution  
```bash
# COMPLIANT: Batch similar operations
Task Tool [Parallel]:
├── Agent1: Read file1.js, file2.js
├── Agent2: Read file3.js, file4.js  
└── Agent3: Read file5.js
```

## Wave Deployment Protocol | Reference: @tool-usage-protocols.md
**Wave Structure**: Analysis(2-3) → Operations(4-6) → Validation(1-2)
**Communication**: One-way only | Sub-agents return final results
**Context**: Isolated per agent | Main agent synthesizes

## Implementation Requirements
1. **Detection**: Identify repetitive patterns before execution
2. **Batching**: Group similar operations by type/domain
3. **Distribution**: Balance load across available agents
4. **Synthesis**: Main agent aggregates all results

## Effectiveness Metrics | Parallel Performance
- **Speedup Ratio**: Time(sequential)/Time(parallel) ≥ 2.5x
- **Agent Utilization**: Active agents/Total agents ≥ 80%
- **Error Isolation**: Failed agents don't block others
- **Result Quality**: Parallel output = Sequential output

## Blocking Violations
- Sequential execution of 3+ similar tasks = STOP
- Exceeding 10-agent limit = STOP
- Mixed task types in single wave = STOP
- No result synthesis plan = STOP

**Core Principle**: Parallel execution is mandatory optimization, not optional enhancement