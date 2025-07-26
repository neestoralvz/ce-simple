# start

**Purpose**: Project analysis & guidance via 4 Task Tool agents

## Execution: 3 Steps

### Step 1: Deploy 4 Analysis Agents with Individual Reporting
```markdown
Task Tool execution: 4 concurrent analysis agents with mandatory individual user reporting

Agent 1 (Task Tool): "State analysis via LS -la; Read README.md; Grep 'TODO\|FIXME'"
→ **INDIVIDUAL REPORT TO USER**: Agent 1 will report current project state directly to you before synthesis

Agent 2 (Task Tool): "Tech assessment via Read package.json requirements.txt; Bash 'npm list'"
→ **INDIVIDUAL REPORT TO USER**: Agent 2 will report technology assessment directly to you before synthesis

Agent 3 (Task Tool): "Goals extraction via Read README.md docs/*; Grep 'goal\|objective\|mission'"
→ **INDIVIDUAL REPORT TO USER**: Agent 3 will report project goals and objectives directly to you before synthesis

Agent 4 (Task Tool): "Synthesis via analysis compilation from agents 1-3 results"
→ **INDIVIDUAL REPORT TO USER**: Agent 4 will report synthesis analysis directly to you before final guidance

**TRANSPARENCY REQUIREMENT**: Each agent MUST report findings individually to user before synthesis
**FOCUSED SCOPE**: Each agent analyzes specific project aspects with transparent reporting
```

### Step 2: Individual Agent Reporting Phase
**MANDATORY**: Each deployed agent reports results directly to user with clear attribution:
- Agent identification: "Agent X Results" 
- Current state, technology stack, or goals findings
- Specific insights and recommendations from analysis area
- Progress confirmation before moving to synthesis

### Step 3: User-Visible Synthesis & Guidance Generation
After all individual agent reports are delivered to user:
- Agent 4 synthesizes all findings with clear source attribution
- Generate actionable guidance with prioritized next steps
- Reference specific agent contributions in recommendations

## Success Metrics
- Analysis completion: <90 seconds with 4 parallel agents
- Project understanding: Comprehensive state & objectives
- Guidance quality: Specific, actionable recommendations
- 4x speedup vs sequential analysis

---
**Implementation**: Real Task Tool parallelization with actual project analysis.