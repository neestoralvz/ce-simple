# explore-codebase

**Purpose**: Parallel codebase analysis via 8 Task Tool agents in <2 minutes

## Execution: 3 Steps

### Step 1: Deploy 8 Parallel Agents with Individual Reporting
```markdown
Task Tool execution: 8 concurrent agents with mandatory individual user reporting

Agent 1 (Task Tool): "Project structure mapping via LS /*, Read core files, Grep dependencies"
→ **INDIVIDUAL REPORT TO USER**: Agent 1 will report project structure findings directly to you before synthesis

Agent 2 (Task Tool): "Pattern scanning via Grep '\.(js|py|ts|go)' *, Read pattern files"  
→ **INDIVIDUAL REPORT TO USER**: Agent 2 will report code patterns and technologies directly to you before synthesis

Agent 3 (Task Tool): "Technology detection via Glob 'package.json' 'requirements.txt' '*.toml'"
→ **INDIVIDUAL REPORT TO USER**: Agent 3 will report technology stack findings directly to you before synthesis

Agent 4 (Task Tool): "Documentation discovery via Grep -i 'readme\|doc' *, Read doc files"
→ **INDIVIDUAL REPORT TO USER**: Agent 4 will report documentation status directly to you before synthesis

Agent 5 (Task Tool): "Config analysis via Read package.json Makefile *.yaml *.json"
→ **INDIVIDUAL REPORT TO USER**: Agent 5 will report configuration analysis directly to you before synthesis

Agent 6 (Task Tool): "Git metrics via Bash 'git log --oneline' 'git shortlog -sn'"
→ **INDIVIDUAL REPORT TO USER**: Agent 6 will report git history insights directly to you before synthesis

Agent 7 (Task Tool): "Test discovery via Grep -r 'test\|spec' *, LS test/ tests/"
→ **INDIVIDUAL REPORT TO USER**: Agent 7 will report testing infrastructure directly to you before synthesis

Agent 8 (Task Tool): "Performance scan via Grep 'TODO\|FIXME\|performance' *"
→ **INDIVIDUAL REPORT TO USER**: Agent 8 will report performance issues directly to you before synthesis

**TRANSPARENCY REQUIREMENT**: Each agent MUST report findings individually to user before synthesis
**PARALLELIZATION**: Real Task Tool concurrent execution with transparent progress reporting
```

### Step 2: Individual Agent Reporting Phase
**MANDATORY**: Each deployed agent reports results directly to user with clear attribution:
- Agent identification: "Agent X Results"
- Specific findings from assigned analysis area
- Raw data and insights discovered
- Progress status and completion confirmation

### Step 3: User-Visible Progress & Final Synthesis
After all individual agent reports are delivered to user:
- Combine all agent findings with clear source attribution
- Generate comprehensive project understanding with actionable insights
- Reference specific agent contributions in final recommendations

## Success Metrics
- Analysis completion: <2 minutes
- Technology stack identification: 100%
- Architecture mapping: Complete
- Quality assessment: With specific recommendations
- Speedup achieved: 20x vs sequential analysis

---
**Implementation**: Real Task Tool parallelization with 8 concurrent agents.