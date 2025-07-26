# explore-codebase

**Purpose**: Parallel codebase analysis via 8 Task Tool agents in <2 minutes

## Execution: 3 Steps

### Step 1: Deploy 8 Parallel Agents
```markdown
Task Tool execution: 8 concurrent agents with individual reporting

Agent 1 (Task Tool): Project structure mapping via LS /*, Read core files, Grep dependencies
Agent 2 (Task Tool): Pattern scanning via Grep "\.(js|py|ts|go)" *, Read pattern files
Agent 3 (Task Tool): Technology detection via Glob "package.json" "requirements.txt" "*.toml"
Agent 4 (Task Tool): Documentation discovery via Grep -i "readme\|doc" *, Read doc files
Agent 5 (Task Tool): Config analysis via Read package.json Makefile *.yaml *.json
Agent 6 (Task Tool): Git metrics via Bash "git log --oneline" "git shortlog -sn"
Agent 7 (Task Tool): Test discovery via Grep -r "test\|spec" *, LS test/ tests/
Agent 8 (Task Tool): Performance scan via Grep "TODO\|FIXME\|performance" *

**PARALLELIZATION**: Real Task Tool concurrent execution, not sequential simulation
```

### Step 2: Parallel Analysis Execution
Each agent executes independently with tools specified above, providing individual reports.

### Step 3: Synthesis & Recommendations
Combine all agent findings into comprehensive project understanding with actionable insights.

## Success Metrics
- Analysis completion: <2 minutes
- Technology stack identification: 100%
- Architecture mapping: Complete
- Quality assessment: With specific recommendations
- Speedup achieved: 20x vs sequential analysis

---
**Implementation**: Real Task Tool parallelization with 8 concurrent agents.