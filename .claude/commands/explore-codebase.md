# Explore Codebase - Internal Knowledge Discovery

## 🎯 Purpose
Systematically explore codebase structure and patterns using parallel operations for maximum efficiency.

## 🚀 Usage
Execute: `/explore-codebase [search-target] [depth-level]`

## 🔧 Implementation

### Autocontained Notification System
```bash
#!/bin/bash
# NOTIFICATION SYSTEM - Functional colors + unique emoticons
readonly B='\e[34m' G='\e[32m' R='\e[31m' Y='\e[33m' C='\e[36m' M='\e[35m' GB='\e[32;1m' N='\e[0m'
info()     { echo -e "${B}🔵 INFO${N}: $1"; }
success()  { echo -e "${G}🟢 SUCCESS${N}: $1"; }  
error()    { echo -e "${R}🔴 ERROR${N}: $1"; }
warn()     { echo -e "${Y}🟡 WARNING${N}: $1"; }
process()  { echo -e "${C}⚡ PROCESS${N}: $1"; }
data()     { echo -e "${M}📊 DATA${N}: $1"; }
complete() { echo -e "${GB}✅ COMPLETE${N}: $1"; }
calc()     { echo "scale=${2:-2}; $1" | bc -l; }
progress() { local p=$(calc "$1*100/$2" 0); process "$3 [$p% complete]"; }
```

### Behavioral Reinforcement Protocol
**MANDATORY at exploration initialization**:

```javascript
TodoWrite([
  {"content": "🏗️ PHASE-0: Execute structural assessment with 85% completeness validation", "status": "pending", "priority": "high", "id": "explore-phase0-1"},
  {"content": "📊 THRESHOLD: Enforce 85% exploration completeness before consolidation", "status": "pending", "priority": "high", "id": "explore-threshold-1"},
  {"content": "⚡ DEPLOYMENT: Execute intelligent operation scaling (12-52 ops) with validation checkpoints", "status": "pending", "priority": "high", "id": "explore-deploy-1"},
  {"content": "🔍 DISCOVERY: Apply anti-bias pattern recognition with Phase 0 context integration", "status": "pending", "priority": "high", "id": "explore-discover-1"},
  {"content": "🔄 ORCHESTRATION: Coordinate parallel operations via validation-guided /agent-orchestration", "status": "pending", "priority": "high", "id": "explore-orchestration-1"},
  {"content": "✅ CONSOLIDATION: Integrate results only after completeness threshold validation", "status": "pending", "priority": "medium", "id": "explore-consolidation-1"}
])
```

**Dynamic Todo Addition**: Add new todos based on codebase characteristics and discoveries during exploration

### Structural Enforcement Protocol
**PRE-EXPLORATION AUTOMATION**:
1. **🏗️ VALIDATE**: LS paths → Verify docs/, context/, .claude/ structure
2. **🔍 ANALYZE**: Glob/Grep → Inventory documentation, detect outdated references
3. **⚡ CORRECT**: Auto-fix violations → Move files, edit references, create directories
4. **📊 OUTPUT**: Update existing context files only - NO new file creation allowed

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

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of the 52 operations documented above

```javascript
// STRUCTURE DISCOVERY (16 Glob operations)
Glob("**/*.{js,ts,py,go,java,cpp}", {path: "."})  // Core language files
Glob("**/config*", {path: "."})                   // Configuration discovery
Glob("**/package.json", {path: "."})              // Package configurations  
Glob("**/README*", {path: "."})                   // Documentation mapping
Glob("**/docs/**", {path: "."})                   // Documentation structure
Glob("**/*.md", {path: "."})                      // Markdown documentation
Glob("**/Makefile", {path: "."})                  // Build system detection
Glob("**/build.*", {path: "."})                   // Build configurations
Glob("**/src/**", {path: "."})                    // Source architecture
Glob("**/lib/**", {path: "."})                    // Library structure
Glob("**/components/**", {path: "."})             // Component organization
Glob("**/.env*", {path: "."})                     // Environment files
Glob("**/CMakeLists.txt", {path: "."})           // CMake configurations
Glob("**/docker*", {path: "."})                   // Docker configurations
Glob("**/requirements.*", {path: "."})            // Dependency files
Glob("**/go.mod", {path: "."})                    // Go module files

// PATTERN ANALYSIS (24 Grep operations)
Grep("function\\s+\\w+", {glob: "**/*.{js,ts}", output_mode: "count"})     // Function discovery
Grep("def\\s+\\w+", {glob: "**/*.py", output_mode: "count"})               // Python functions
Grep("func\\s+\\w+", {glob: "**/*.go", output_mode: "count"})              // Go functions  
Grep("class\\s+\\w+", {glob: "**/*.{js,ts,py}", output_mode: "count"})     // Class identification
Grep("interface\\s+\\w+", {glob: "**/*.{ts,go}", output_mode: "count"})    // Interface analysis
Grep("struct\\s+\\w+", {glob: "**/*.go", output_mode: "count"})            // Struct patterns
Grep("import\\s+", {glob: "**/*.{js,ts,py}", output_mode: "count"})        // Import mapping
Grep("require\\(", {glob: "**/*.js", output_mode: "count"})                // CommonJS requires
Grep("#include", {glob: "**/*.{c,cpp,h}", output_mode: "count"})           // C/C++ includes
Grep("async\\s+", {glob: "**/*.{js,ts}", output_mode: "count"})            // Async patterns
Grep("await\\s+", {glob: "**/*.{js,ts}", output_mode: "count"})            // Await patterns
Grep("Promise", {glob: "**/*.{js,ts}", output_mode: "count"})              // Promise usage
Grep("test\\(", {glob: "**/*.{js,ts}", output_mode: "count"})              // Test functions
Grep("describe\\(", {glob: "**/*.{js,ts}", output_mode: "count"})          // Test descriptions
Grep("it\\(", {glob: "**/*.{js,ts}", output_mode: "count"})                // Test assertions
Grep("express", {glob: "**/*.{js,ts}", output_mode: "count"})              // Express framework
Grep("react", {glob: "**/*.{js,ts,jsx,tsx}", output_mode: "count"})        // React usage
Grep("django", {glob: "**/*.py", output_mode: "count"})                    // Django framework
Grep("spring", {glob: "**/*.java", output_mode: "count"})                  // Spring framework
Grep("TODO|FIXME|BUG", {glob: "**/*", output_mode: "count"})               // Code issues
Grep("console\\.log", {glob: "**/*.{js,ts}", output_mode: "count"})        // Debug logging
Grep("print\\(", {glob: "**/*.py", output_mode: "count"})                  // Python logging
Grep("fmt\\.Print", {glob: "**/*.go", output_mode: "count"})               // Go logging
Grep("\\bapi\\b|\\bAPI\\b", {glob: "**/*", output_mode: "count"})          // API references

// CONTENT EXAMINATION (12 Read operations) 
Read("package.json")          // If exists - JavaScript dependencies
Read("requirements.txt")      // If exists - Python dependencies  
Read("go.mod")               // If exists - Go module info
Read("README.md")            // If exists - Project documentation
Read("CHANGELOG.md")         // If exists - Version history
Read(".env")                 // If exists - Environment config
Read("Dockerfile")           // If exists - Container config
Read("Makefile")             // If exists - Build configuration
Read("webpack.config.js")    // If exists - Build tooling
Read("tsconfig.json")        // If exists - TypeScript config
Read(".gitignore")           // If exists - Git ignore patterns
Read("LICENSE")              // If exists - Project license
```

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with metrics tracking
Bash("git add . && git commit -m \"explore-codebase: [codebase-type] analysis | files: [N] | patterns: [N] ✓session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **52 TOTAL operations**: 16 Glob + 24 Grep + 12 Read
- **Ratio**: 52 tool calls to ~200 documentation lines = 26% (HEALTHY)
- **Evidence-based**: All discoveries backed by actual file system exploration  
- **Anti-bias**: Conclusions emerge from real codebase analysis

---

**CRITICAL**: This command operates through parallel Task Tool deployment for maximum efficiency. All discoveries MUST be evidence-based with anti-bias protocols enforced.

**EXECUTION COMMITMENT**: The 52 operations documented above are NOW implemented with actual tool calls. No more documentation theater.