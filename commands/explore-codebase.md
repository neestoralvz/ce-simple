# explore-codebase

**Purpose**: Intelligent codebase exploration with parallel analysis using Task Tool

## User Vision Implementation

From `user-input/technical-requirements/technical-architecture-user.md`:
- "Search tasks: 8-16 parallel (20x speedup)"
- "Task Tool provides core execution foundation: Parallel execution of up to 10 sub-agents per command"

## Execution Process

### Real Parallelization Strategy
Deploy 8 parallel sub-agents via Task Tool for comprehensive codebase analysis:

1. **Architecture Analysis Agent** - Map overall project structure and dependencies
2. **Pattern Detection Agent** - Identify coding patterns, frameworks, conventions  
3. **File Type Analyzer** - Categorize and analyze different file types
4. **Documentation Scanner** - Find and analyze README, docs, comments
5. **Configuration Analyzer** - Examine config files, package managers, build tools
6. **Git History Agent** - Analyze commit patterns and project evolution
7. **Test Coverage Agent** - Identify tests, coverage, quality indicators
8. **Performance Scanner** - Look for performance bottlenecks and optimizations

### Task Tool Implementation

```markdown
I'll deploy 8 specialized analysis agents to explore your codebase in parallel.

**TRANSPARENCY GUARANTEE**: You will see individual results from each agent as they complete their analysis.

**Agent 1 - Architecture Analysis**
Task: Analyze project structure, main directories, and architectural patterns
Tools: LS, Read, Grep | **Reports to**: User directly
Focus: High-level organization and dependencies

**Agent 2 - Pattern Detection** 
Task: Identify coding patterns, frameworks, and conventions used
Tools: Grep, Read | **Reports to**: User directly
Focus: Code patterns, naming conventions, architectural decisions

**Agent 3 - File Type Analysis**
Task: Categorize files and analyze technology stack
Tools: Glob, LS, Read | **Reports to**: User directly
Focus: Languages, frameworks, file organization

**Agent 4 - Documentation Analysis**
Task: Find and analyze documentation, README files, comments
Tools: Grep, Read | **Reports to**: User directly
Focus: Project documentation quality and coverage

**Agent 5 - Configuration Analysis**
Task: Examine configuration files, dependencies, build tools
Tools: Read, Grep | **Reports to**: User directly
Focus: Project setup, dependencies, build configuration

**Agent 6 - Git History Analysis**
Task: Analyze commit patterns and project evolution
Tools: Bash (git commands), Read | **Reports to**: User directly
Focus: Development patterns, contributor activity, project maturity

**Agent 7 - Test Coverage Analysis**
Task: Identify tests, testing frameworks, coverage indicators
Tools: Grep, LS, Read | **Reports to**: User directly
Focus: Testing strategy, coverage, quality assurance

**Agent 8 - Performance Analysis**
Task: Look for performance bottlenecks and optimization opportunities
Tools: Grep, Read | **Reports to**: User directly
Focus: Performance patterns, potential improvements

EXECUTION PATTERN:
1. Deploy all 8 agents in parallel
2. Each agent reports findings directly to user as completed
3. Final synthesis combines all individual reports into comprehensive understanding
4. User sees both individual agent discoveries AND integrated analysis
```

## Expected Results

- **Comprehensive project understanding** from 8 parallel analysis streams
- **Technology stack identification** with frameworks and dependencies
- **Architecture mapping** showing project organization and patterns
- **Quality assessment** including tests, documentation, performance
- **Development insights** from Git history and contributor patterns
- **Optimization recommendations** based on analysis findings

## Success Metrics

- 8 parallel agents complete analysis in under 2 minutes
- Comprehensive understanding of codebase architecture and patterns
- Clear technology stack and dependency mapping
- Quality assessment with specific recommendations
- 20x faster than sequential analysis (user target achieved)

---

**Implementation Truth**: Uses real Task Tool parallelization with 8 concurrent agents, not simulated architecture.