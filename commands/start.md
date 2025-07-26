# start

**Purpose**: Project analysis & guidance via 4 Task Tool agents

## Execution: 3 Steps

### Step 1: Deploy 4 Analysis Agents
```markdown
Task Tool execution: 4 concurrent analysis agents with focused scopes

Agent 1 (Task Tool): State analysis via LS -la; Read README.md; Grep "TODO\|FIXME"
Agent 2 (Task Tool): Tech assessment via Read package.json requirements.txt; Bash "npm list"
Agent 3 (Task Tool): Goals extraction via Read README.md docs/*; Grep "goal\|objective\|mission"
Agent 4 (Task Tool): Synthesis via analysis compilation from agents 1-3 results

**FOCUSED SCOPE**: Each agent analyzes specific project aspects for targeted insights
```

### Step 2: Parallel Analysis Execution
### Step 3: Synthesis & Guidance Generation
Agent 4 synthesizes all findings into actionable guidance with prioritized next steps.

## Success Metrics
- Analysis completion: <90 seconds with 4 parallel agents
- Project understanding: Comprehensive state & objectives
- Guidance quality: Specific, actionable recommendations
- 4x speedup vs sequential analysis

---
**Implementation**: Real Task Tool parallelization with actual project analysis.