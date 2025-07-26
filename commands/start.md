# start

**Purpose**: Project analysis and guidance with parallel assessment

## User Vision Implementation

From `user-input/core-mission-concept.md`:
- "Transform complex software workflows into simple command executions through intelligent orchestration"
- "Analysis tasks: 4-8 parallel (4x speedup)"

## Execution Process

### Real Parallelization Strategy
Deploy 4 parallel sub-agents via Task Tool for comprehensive project analysis:

1. **Current State Agent** - Analyze existing project structure and current state
2. **Technology Assessment Agent** - Evaluate technology stack and dependencies
3. **Goals & Requirements Agent** - Identify project goals and requirements from documentation
4. **Guidance Generator Agent** - Synthesize findings into actionable guidance

### Task Tool Implementation

```markdown
I'll deploy 4 specialized analysis agents to understand your project and provide guidance.

**TRANSPARENCY GUARANTEE**: You will see individual results from each agent before final synthesis.

**Agent 1 - Current State Analysis**
Task: Analyze existing project structure, files, and current development state
Tools: LS, Read, Grep
Focus: Project status, existing structure, current capabilities
**Reports to**: User directly, then to synthesis

**Agent 2 - Technology Assessment**
Task: Evaluate technology stack, dependencies, and technical setup
Tools: Read, Grep, Bash
Focus: Tech stack analysis, dependency mapping, technical capabilities
**Reports to**: User directly, then to synthesis

**Agent 3 - Goals & Requirements Analysis**
Task: Extract project goals and requirements from documentation and user input
Tools: Read, Grep  
Focus: Project objectives, user requirements, success criteria
**Reports to**: User directly, then to synthesis

**Agent 4 - Guidance Synthesis**
Task: Synthesize analysis into actionable next steps and recommendations
Tools: Compile results from agents 1-3 (after user has seen individual results)
Focus: Strategic guidance, next steps, optimization recommendations

EXECUTION PATTERN:
1. Deploy Agents 1-3 in parallel → Individual results shown to user
2. Deploy Agent 4 for synthesis → Final integrated guidance
3. User sees both individual agent work AND final synthesis
```

## Analysis Framework

Based on user vision for "simple command executions through intelligent orchestration":

### Current State Assessment
- Project structure and organization
- Existing files and capabilities  
- Development setup and configuration
- Git repository status and history

### Technology Evaluation
- Programming languages and frameworks
- Dependencies and package management
- Build tools and development environment
- Testing and quality assurance setup

### Goal Identification
- Project mission and objectives
- User requirements and success criteria
- Technical constraints and requirements
- Performance and quality targets

### Strategic Guidance
- Immediate next steps and priorities
- Development recommendations and best practices
- Optimization opportunities and improvements
- Resource allocation and workflow suggestions

## Expected Results

- **Comprehensive project understanding** from 4 parallel analysis streams
- **Technology stack assessment** with recommendations
- **Clear goal identification** based on project documentation
- **Actionable guidance** with prioritized next steps
- **Strategic recommendations** for project success

## Success Metrics

- 4 parallel agents complete analysis in under 90 seconds
- Clear understanding of project state and objectives
- Specific, actionable guidance with priorities
- Technology assessment with optimization recommendations
- 4x faster than sequential analysis (user target achieved)

---

**Implementation Truth**: Uses real Task Tool parallelization with actual project analysis, not simulated results.