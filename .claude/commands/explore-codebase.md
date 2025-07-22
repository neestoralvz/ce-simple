# Explore Codebase - Internal Knowledge Discovery

## 🎯 Purpose
Systematically explore and analyze codebase structure, patterns, and implementation details using parallel Task Tool operations for maximum efficiency.

## 🚀 Usage
Execute: `/explore-codebase [search-target] [depth-level]`

## 🔧 Implementation

### Exploration Protocol
1. **SCOPE DEFINITION**: Determine exploration boundaries and objectives
2. **PARALLEL DEPLOYMENT**: Execute multiple Task Tools simultaneously
3. **PATTERN RECOGNITION**: Identify architectural patterns and conventions
4. **CONTEXT INTEGRATION**: Consolidate findings into actionable intelligence
5. **DOCUMENTATION GENERATION**: Create structured context files

### Parallel Execution Framework

#### Simultaneous Task Deployment
**MANDATORY**: Deploy multiple Task Tools for maximum efficiency

**Core Exploration Tasks** (Parallel Execution):
- **Structure Analysis**: Map directory hierarchy and file organization
- **Pattern Detection**: Identify coding patterns, frameworks, libraries
- **Dependency Mapping**: Analyze imports, exports, and connections
- **Configuration Discovery**: Locate and analyze config files
- **Documentation Analysis**: Review existing documentation and comments

### Task Tool Orchestration

#### Task 1: Structure Discovery
```
🔧 TASK-01: Directory structure mapping
  Objective: Complete file system analysis
  Tools: Glob, LS, Read
  Output: context/discoveries/structure-[timestamp].md
```

#### Task 2: Pattern Analysis  
```
🔧 TASK-02: Code pattern identification
  Objective: Framework and library detection
  Tools: Grep, Read with pattern matching
  Output: context/patterns/code-patterns-[timestamp].md
```

#### Task 3: Dependency Resolution
```
🔧 TASK-03: Import/export mapping
  Objective: Component relationship analysis
  Tools: Grep for imports, Read for package files
  Output: context/research/dependencies-[timestamp].md
```

#### Task 4: Configuration Analysis
```
🔧 TASK-04: Configuration file analysis
  Objective: Environment and build setup understanding
  Tools: Glob for config patterns, Read for content
  Output: context/discoveries/config-[timestamp].md
```

### Search Strategies

#### Targeted Exploration
**SPECIFIC Targets**:
- Function implementations: `grep -r "function.*{target}"` 
- Class definitions: `grep -r "class.*{target}"`
- Configuration patterns: `glob "**/*config*"`
- Test patterns: `glob "**/*test*" "**/*spec*"`

#### Comprehensive Exploration
**FULL Codebase**:
- Architecture overview: Complete structure mapping
- Technology stack: Framework and library identification
- Development patterns: Coding conventions and standards
- Integration points: API endpoints, data flows

### Anti-Bias Discovery Protocol
**CRITICAL**: NO predetermined assumptions about codebase structure

#### Discovery Rules
- **EMERGENCE**: Patterns emerge from actual code analysis
- **NEUTRALITY**: No preconceived architectural expectations
- **EVIDENCE**: All conclusions based on discovered evidence
- **COMPLETENESS**: Explore all areas without selective focus

### Context Generation Standards

#### File Organization
```
context/discoveries/
├── structure-[timestamp].md      # Directory and file mapping
├── architecture-[timestamp].md   # High-level organization
└── components-[timestamp].md     # Component analysis

context/patterns/
├── code-patterns-[timestamp].md  # Programming patterns found
├── naming-conventions-[timestamp].md  # Variable/function naming
└── design-patterns-[timestamp].md    # Architectural patterns

context/research/
├── dependencies-[timestamp].md   # External libraries and frameworks
├── technologies-[timestamp].md   # Tech stack analysis
└── integrations-[timestamp].md   # Third-party integrations
```

#### Content Standards
- **DENSITY**: Maximum information per line
- **STRUCTURE**: Hierarchical organization with clear sections
- **REFERENCES**: Cross-links to related discoveries
- **ACTIONABLE**: Findings translate to implementable insights

### Efficiency Optimization

#### Task Tool Parallelization
**ADVANTAGE**: Reduce exploration time by 70-80%
- **Simultaneous Execution**: Multiple discovery tasks running concurrently
- **Resource Optimization**: Each task focuses on specific analysis area
- **Context Preservation**: Results integrated without information loss

#### Progressive Depth Levels
- **Level 1**: Surface structure and obvious patterns
- **Level 2**: Implementation details and relationships
- **Level 3**: Complex integrations and custom patterns
- **Level 4**: Deep architectural analysis and optimization opportunities

### Integration Protocol

#### Result Consolidation
**MANDATORY**: Integrate all parallel task results into coherent narrative

1. **ANALYSIS**: Compare findings across all tasks
2. **SYNTHESIS**: Identify common themes and contradictions
3. **VALIDATION**: Cross-reference discoveries for accuracy
4. **DOCUMENTATION**: Create comprehensive exploration summary

#### Handoff to Analysis
```
✓ EXPLORATION-COMPLETE: Codebase analysis finished
  Files Generated: [N] context files
  Patterns Identified: [N] architectural patterns
  Next Command: /think-layers for deep analysis
  Integration Ready: All context available for planning
```

## ⚡ Triggers

### Input Triggers
**Context**: Complex codebase analysis required
**Previous**: `/start` → Exploration phase activated
**Keywords**: codebase, structure, patterns, architecture, implementation

### Output Triggers  
**When**: Exploration complete → `/think-layers` for analysis
**When**: Specific patterns found → `/explore-web` for external research
**When**: Configuration issues → `/validate-system` for health check
**Chain**: explore-codebase → think-layers → plan-execution

### Success Patterns
**Discovery Success**: >85% codebase structure mapped → Proceed to analysis
**Pattern Success**: Clear architectural patterns identified → Generate recommendations
**Integration Success**: All components understood → Ready for modifications

## 🔗 See Also

### Related Commands
- Execute `/start` to initiate discovery workflow that triggers this exploration
- Execute `/explore-web` for external research to complement internal findings
- Execute `/think-layers` for progressive analysis of discovered patterns
- Execute `/validate-system` for health checks when configuration issues found

### Integration Points
- Operates through parallel Task Tool deployment for maximum efficiency
- Anti-bias protocols ensure evidence-based discovery without assumptions
- Generated context feeds directly into progressive thinking workflows
- Cross-references findings with external research for comprehensive analysis

---

**CRITICAL**: This command operates through parallel Task Tool deployment for maximum efficiency. All discoveries MUST be evidence-based with anti-bias protocols enforced.