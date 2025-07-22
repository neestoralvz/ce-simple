# Explore Codebase - Internal Knowledge Discovery

## 🎯 Purpose
Systematically explore codebase structure and patterns using parallel operations for maximum efficiency.

## 🚀 Usage
Execute: `/explore-codebase [search-target] [depth-level]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at exploration initialization**:

```javascript
TodoWrite([
  {"content": "📏 ASSESSMENT: Analyze codebase size via /agent-orchestration for optimal parallelization", "status": "pending", "priority": "high", "id": "explore-assess-1"},
  {"content": "⚡ DEPLOYMENT: Execute intelligent operation scaling (12-52 ops) based on complexity matrix", "status": "pending", "priority": "high", "id": "explore-deploy-1"},
  {"content": "🔍 DISCOVERY: Apply anti-bias pattern recognition with evidence-based conclusions", "status": "pending", "priority": "high", "id": "explore-discover-1"},
  {"content": "🔄 ORCHESTRATION: Coordinate parallel operations (16 Glob + 24 Grep + 12 Read) via /agent-orchestration", "status": "pending", "priority": "high", "id": "explore-orchestration-1"},
  {"content": "✅ CONSOLIDATION: Integrate all parallel operation results into coherent findings", "status": "pending", "priority": "medium", "id": "explore-consolidation-1"},
  {"content": "📝 CONTEXT: Generate structured documentation from exploration discoveries", "status": "pending", "priority": "medium", "id": "explore-context-1"}
])
```

**Dynamic Todo Addition**: Add new todos based on codebase characteristics and discoveries during exploration

### Structural Enforcement Protocol
**PRE-EXPLORATION AUTOMATION**:
1. **🏗️ VALIDATE**: LS paths → Verify docs/, context/, .claude/ structure
2. **🔍 ANALYZE**: Glob/Grep → Inventory documentation, detect outdated references
3. **⚡ CORRECT**: Auto-fix violations → Move files, edit references, create directories
4. **📊 OUTPUT**: Generate structure analysis → context/discoveries/structure-analysis-[timestamp].md

### Dynamic Analysis Protocol
**PHASE 1 - CODEBASE ASSESSMENT**: Analyze project size and complexity to determine optimal operation count
**PHASE 2 - PARALLEL OPTIMIZATION**: Scale operations based on codebase characteristics
**PHASE 3 - AGGRESSIVE EXECUTION**: Deploy optimized concurrent operations in single message

### Exploration Protocol Framework

#### Agent Orchestration Integration
**Auto-Triggered**: Deploy `/agent-orchestration` for intelligent parallelization coordination
**Parameters**: Codebase size, analysis depth, parallel operation requirements
**Output**: Optimized search strategy with dynamic operation scaling

#### Dynamic Assessment Protocol
**MANDATORY Pre-Execution**: Assess codebase characteristics to optimize parallelization
**Complexity Analysis**: Project size → File count → Architecture patterns → Operation scaling
**Intelligence Framework**:
```
📏 SIZE-ANALYSIS: Codebase assessment → Complexity [N]/10 → [Operation-count] selected
⚡ DEPLOY-STRATEGY: [N] operations activated → [16 Glob + 24 Grep + 12 Read] coordinated
🔍 PATTERN-RECOGNITION: Anti-bias discovery → Evidence-based conclusions only
🔄 COORDINATION: Parallel execution → [N] operations synchronized
✅ CONSOLIDATION: Results integration → Coherent narrative generation
```

#### Evidence-Based Discovery Framework
**Anti-Bias Processing**: NO predetermined assumptions - patterns emerge from discovered evidence only
**Context Integration**: Consolidate findings from all parallel operations via `/agent-orchestration`
**Quality Assurance**: Cross-validate patterns across multiple operation results

### Intelligent Parallelization Matrix
**Complexity-Based Scaling** (via `/agent-orchestration`):

#### Small Codebases (Complexity 1-3, <100 files)
**Operation Count**: 12 operations
- **4 Glob**: File types, configs, basic structure
- **6 Grep**: Core functions, main classes, imports
- **2 Read**: Primary config, entry point

#### Medium Codebases (Complexity 4-6, 100-1000 files)
**Operation Count**: 28 operations
- **8 Glob**: Architecture patterns, build systems, docs, tests
- **16 Grep**: Functions, classes, async patterns, frameworks
- **4 Read**: Configs, documentation, environments, dependencies

#### Large Codebases (Complexity 7-10, 1000+ files)
**Operation Count**: 52 operations (Maximum Parallelization)
- **16 Glob**: Complete architecture, all patterns, comprehensive structure
- **24 Grep**: Exhaustive pattern analysis, integration points, test coverage
- **12 Read**: All configs, docs, environments, build files, specifications

### Parallel Operation Orchestration
**Intelligent Coordination** (via `/agent-orchestration`):

#### Structure Discovery Operations (16 Glob Maximum)
**File Type Analysis**: `**/*.{js,ts,py,go,java,cpp}` - Core language files
**Configuration Discovery**: `**/config*`, `**/.env*`, `**/package.json` - System configs
**Documentation Mapping**: `**/README*`, `**/docs/**`, `**/*.md` - Documentation structure
**Build System Detection**: `**/Makefile`, `**/CMakeLists.txt`, `**/build.*` - Build configurations
**Architecture Patterns**: `**/src/**`, `**/lib/**`, `**/components/**` - Code organization

#### Pattern Analysis Operations (24 Grep Maximum)
**Function Discovery**: `function\s+\w+`, `def\s+\w+`, `func\s+\w+` - Core functionality
**Class Identification**: `class\s+\w+`, `interface\s+\w+`, `struct\s+\w+` - Object structures
**Import Mapping**: `import\s+`, `require\(`, `#include` - Dependency analysis
**Async Pattern Detection**: `async\s+`, `await\s+`, `Promise` - Concurrency patterns
**Testing Framework**: `test\(`, `describe\(`, `it\(` - Test coverage analysis
**Framework Integration**: `express`, `react`, `django`, `spring` - Technology stack

#### Content Examination Operations (12 Read Maximum)
**Configuration Files**: package.json, requirements.txt, go.mod - Dependencies
**Documentation Review**: README.md, CHANGELOG.md, API docs - Project overview
**Environment Setup**: .env files, docker configs, deployment specs - Runtime environment
**Entry Points**: main.py, index.js, main.go - Application initialization
**Build Specifications**: Makefile, webpack.config.js, setup.py - Build processes
**API Specifications**: OpenAPI, GraphQL schemas, API documentation - Interface definitions

### Search Strategy
**Targeted**: Specific function/class/config/test patterns
**Comprehensive**: Complete architecture, tech stack, integration analysis
**Evidence-Based**: Conclusions from discovered code evidence
**90% Efficiency**: 52 operations reduce hours to minutes

### Result Consolidation & Context Generation

#### Intelligent Result Synthesis (via `/agent-orchestration`)
**Collection Protocol**:
1. **📊 GATHERING**: Aggregate all operation outputs with metadata tagging
2. **🔍 VALIDATION**: Cross-validate patterns across multiple operation results
3. **🧠 SYNTHESIS**: Consolidate findings into architectural understanding
4. **📝 OUTPUT**: Generate structured context documentation

#### Context Documentation Framework
**File Organization**: Structured output with hierarchical information architecture
- `context/discoveries/codebase-[session-id].md` → Structural findings and architecture
- `context/patterns/code-patterns-[timestamp].md` → Identified patterns and best practices
- `context/research/tech-stack-[project].md` → Technology analysis and dependencies

**Content Standards**: Maximum information density with actionable insights
**Cross-References**: Direct implementation translation with specific file locations
**Evidence-Based Conclusions**: All findings supported by discovered code evidence

## ⚡ Triggers

### Input Triggers
**Context**: Complex codebase analysis required following discovery initiation
**Previous**: `/start` exploration phase or direct codebase analysis requirement
**Keywords**: codebase, structure, patterns, architecture, implementation

### Output Triggers  
**Success**: Exploration complete → `/think-layers` for pattern analysis and synthesis
**Validation**: Specific patterns found → `/explore-web` for external research confirmation
**Integration**: All components understood → Implementation planning readiness
**Chain**: explore-codebase → think-layers → execution workflow

### Success Patterns
**Discovery Success**: >85% codebase structure mapped → Analysis pipeline triggered
**Pattern Success**: Clear architectural patterns identified → Recommendation generation
**Integration Success**: All components understood → Implementation workflow ready

## 🔗 Module Integration

### Command Module Dependencies
**Core Integration**:
- `/agent-orchestration` → Intelligent parallelization coordination and result consolidation
- `/matrix-maintenance` → Cross-reference validation during structural analysis

**Execution Chain**:
- `/start` → Initiates discovery workflows triggering codebase exploration
- `/explore-web` → External research complementing internal architectural findings
- `/think-layers` → Progressive analysis of discovered patterns and architecture
- `/capture-learnings` → Pattern documentation and architectural insights

### Success Patterns & Performance Metrics
**Discovery Success**: >85% codebase structure mapped via intelligent parallelization → Analysis pipeline triggered
**Orchestration Success**: Optimal operation count selected → Execution efficiency >90%
**Pattern Success**: Clear architectural patterns identified → Evidence-based recommendations generated
**Integration Success**: All components understood → Implementation workflow readiness achieved

### Integration Success Indicators
**Parallelization Efficiency**: 52 operations reduce exploration time from hours to minutes
**Evidence-Based Discovery**: All conclusions supported by discovered code artifacts
**Anti-Bias Processing**: Patterns emerge from evidence, not predetermined assumptions
**Context Generation**: Structured documentation ready for analysis and implementation phases

### Context Output Locations
- `context/discoveries/` → Structural and component analysis documentation
- `context/patterns/` → Code pattern identification and best practices
- `context/research/` → Technology stack and dependency analysis

---

**CRITICAL**: This command operates through parallel Task Tool deployment for maximum efficiency. All discoveries MUST be evidence-based with anti-bias protocols enforced.