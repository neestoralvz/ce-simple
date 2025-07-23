# ORCHESTRATOR.md - SuperClaude Intelligent Routing System

Intelligent routing system for Claude Code SuperClaude framework.

## 🧠 Detection Engine

Analyzes requests to understand intent, complexity, and requirements.

### Pre-Operation Validation Checks

**Resource Validation**:
- Token usage prediction based on operation complexity and scope
- Memory and processing requirements estimation
- File system permissions and available space verification
- MCP server availability and response time checks

**Compatibility Validation**:
- Flag combination conflict detection (e.g., `--no-mcp` with `--seq`)
- Persona + command compatibility verification
- Tool availability for requested operations
- Project structure requirements validation

**Risk Assessment**:
- Operation complexity scoring (0.0-1.0 scale)
- Failure probability based on historical patterns
- Resource exhaustion likelihood prediction
- Cascading failure potential analysis

**Validation Logic**: Resource availability, flag compatibility, risk assessment, outcome prediction, and safety recommendations. Operations with risk scores >0.8 trigger safe mode suggestions.

**Resource Management Thresholds**:
- **Green Zone** (0-60%): Full operations, predictive monitoring active
- **Yellow Zone** (60-75%): Resource optimization, caching, suggest --uc mode
- **Orange Zone** (75-85%): Warning alerts, defer non-critical operations  
- **Red Zone** (85-95%): Force efficiency modes, block resource-intensive operations
- **Critical Zone** (95%+): Emergency protocols, essential operations only

### Pattern Recognition Rules

#### Complexity Detection
**Simple**:
**Indicators**:
- single file operations
- basic CRUD tasks
- straightforward queries
- < 3 step workflows
- **Token Budget**: 5K
- **Time Estimate**: < 5 min
**Moderate**:
**Indicators**:
- multi-file operations
- analysis tasks
- refactoring requests
- 3-10 step workflows
- **Token Budget**: 15K
- **Time Estimate**: 5-30 min
**Complex**:
**Indicators**:
- system-wide changes
- architectural decisions
- performance optimization
- > 10 step workflows
- **Token Budget**: 30K+
- **Time Estimate**: > 30 min

#### Domain Identification
**Frontend**:
  **Keywords**:
  - UI
  - component
  - React
  - Vue
  - CSS
  - responsive
  - accessibility
  - implement component
  - build UI
  **File Patterns**:
  - *.jsx
  - *.tsx
  - *.vue
  - *.css
  - *.scss
  **Typical Operations**:
  - create
  - implement
  - style
  - optimize
  - test
**Backend**:
  **Keywords**:
  - API
  - database
  - server
  - endpoint
  - authentication
  - performance
  - implement API
  - build service
  **File Patterns**:
  - *.js
  - *.ts
  - *.py
  - *.go
  - controllers/*
  - models/*
  **Typical Operations**:
  - implement
  - optimize
  - secure
  - scale
**Infrastructure**:
  **Keywords**:
  - deploy
  - Docker
  - CI/CD
  - monitoring
  - scaling
  - configuration
  **File Patterns**:
  - Dockerfile
  - *.yml
  - *.yaml
  - .github/*
  - terraform/*
  **Typical Operations**:
  - setup
  - configure
  - automate
  - monitor
**Security**:
  **Keywords**:
  - vulnerability
  - authentication
  - encryption
  - audit
  - compliance
  **File Patterns**:
  - *auth*
  - *security*
  - *.pem
  - *.key
  **Typical Operations**:
  - scan
  - harden
  - audit
  - fix
**Documentation**:
  **Keywords**:
  - document
  - README
  - wiki
  - guide
  - manual
  - instructions
  - commit
  - release
  - changelog
  **File Patterns**:
  - *.md
  - *.rst
  - *.txt
  - docs/*
  - README*
  - CHANGELOG*
  **Typical Operations**:
  - write
  - document
  - explain
  - translate
  - localize
**Iterative**:
  **Keywords**:
  - improve
  - refine
  - enhance
  - correct
  - polish
  - fix
  - iterate
  - loop
  - repeatedly
  **File Patterns**:
  - *.*
  **Typical Operations**:
  - improve
  - refine
  - enhance
  - correct
  - polish
  - fix
  - iterate
**Wave Eligible**:
  **Keywords**:
  - comprehensive
  - systematically
  - thoroughly
  - enterprise
  - large-scale
  - multi-stage
  - progressive
  - iterative
  - campaign
  - audit
  **Complexity Indicators**:
  - system-wide
  - architecture
  - performance
  - security
  - quality
  - scalability
  **Operation Indicators**:
  - improve
  - optimize
  - refactor
  - modernize
  - enhance
  - audit
  - transform
  **Scale Indicators**:
  - entire
  - complete
  - full
  - comprehensive
  - enterprise
  - large
  - massive
  **Typical Operations**:
  - comprehensive_improvement
  - systematic_optimization
  - enterprise_transformation
  - progressive_enhancement

#### Operation Type Classification
**Analysis**:
  **Verbs**:
  - analyze
  - review
  - explain
  - understand
  - investigate
  - troubleshoot
  **Outputs**:
  - insights
  - recommendations
  - reports
  **Typical Tools**:
  - Grep
  - Read
  - Sequential
**Creation**:
  **Verbs**:
  - create
  - build
  - implement
  - generate
  - design
  **Outputs**:
  - new files
  - features
  - components
  **Typical Tools**:
  - Write
  - Magic
  - Context7
**Implementation**:
  **Verbs**:
  - implement
  - develop
  - code
  - construct
  - realize
  **Outputs**:
  - working features
  - functional code
  - integrated components
  **Typical Tools**:
  - Write
  - Edit
  - MultiEdit
  - Magic
  - Context7
  - Sequential
**Modification**:
  **Verbs**:
  - update
  - refactor
  - improve
  - optimize
  - fix
  **Outputs**:
  - edited files
  - improvements
  **Typical Tools**:
  - Edit
  - MultiEdit
  - Sequential
**Debugging**:
  **Verbs**:
  - debug
  - fix
  - troubleshoot
  - resolve
  - investigate
  **Outputs**:
  - fixes
  - root causes
  - solutions
  **Typical Tools**:
  - Grep
  - Sequential
  - Playwright
**Iterative**:
  **Verbs**:
  - improve
  - refine
  - enhance
  - correct
  - polish
  - fix
  - iterate
  - loop
  **Outputs**:
  - progressive improvements
  - refined results
  - enhanced quality
  **Typical Tools**:
  - Sequential
  - Read
  - Edit
  - MultiEdit
  - TodoWrite
**Wave Operations**:
  **Verbs**:
  - comprehensively
  - systematically
  - thoroughly
  - progressively
  - iteratively
  **Modifiers**:
  - improve
  - optimize
  - refactor
  - modernize
  - enhance
  - audit
  - transform
  **Outputs**:
  - comprehensive improvements
  - systematic enhancements
  - progressive transformations
  **Typical Tools**:
  - Sequential
  - Task
  - Read
  - Edit
  - MultiEdit
  - Context7
  **Wave Patterns**:
  - review-plan-implement-validate
  - assess-design-execute-verify
  - analyze-strategize-transform-optimize

### Intent Extraction Algorithm
```
1. Parse user request for keywords and patterns
2. Match against domain/operation matrices
3. Score complexity based on scope and steps
4. Evaluate wave opportunity scoring
5. Estimate resource requirements
6. Generate routing recommendation (traditional vs wave mode)
7. Apply auto-detection triggers for wave activation
```

**Enhanced Wave Detection Algorithm**:
- **Flag Overrides**: `--single-wave` disables, `--force-waves`/`--wave-mode` enables
- **Scoring Factors**: Complexity (0.2-0.4), scale (0.2-0.3), operations (0.2), domains (0.1), flag modifiers (0.05-0.1)
- **Thresholds**: Default 0.7, customizable via `--wave-threshold`, enterprise strategy lowers file thresholds
- **Decision Logic**: Sum all indicators, trigger waves when total ≥ threshold

## 🚦 Routing Intelligence

Dynamic decision trees that map detected patterns to optimal tool combinations, persona activation, and orchestration strategies.

### Wave Orchestration Engine
Multi-stage command execution with compound intelligence. Automatic complexity assessment or explicit flag control.

**Wave Control Matrix**:
**Wave-Activation**:
  - **Automatic**: complexity >= 0.7
  - **Explicit**: --wave-mode, --force-waves
  - **Override**: --single-wave, --wave-dry-run
**Wave-Strategies**:
  - **Progressive**: Incremental enhancement
  - **Systematic**: Methodical analysis
  - **Adaptive**: Dynamic configuration

**Wave-Enabled Commands**:
- **Tier 1**: `/analyze`, `/build`, `/implement`, `/improve`
- **Tier 2**: `/design`, `/task`

### Master Routing Table

| Pattern | Complexity | Domain | Auto-Activates | Confidence |
|---------|------------|---------|----------------|------------|
| "analyze architecture" | complex | infrastructure | architect persona, --ultrathink, Sequential | 95% |
| "create component" | simple | frontend | frontend persona, Magic, --uc | 90% |
| "implement feature" | moderate | any | domain-specific persona, Context7, Sequential | 88% |
| "implement API" | moderate | backend | backend persona, --seq, Context7 | 92% |
| "implement UI component" | simple | frontend | frontend persona, Magic, --c7 | 94% |
| "implement authentication" | complex | security | security persona, backend persona, --validate | 90% |
| "fix bug" | moderate | any | analyzer persona, --think, Sequential | 85% |
| "optimize performance" | complex | backend | performance persona, --think-hard, Playwright | 90% |
| "security audit" | complex | security | security persona, --ultrathink, Sequential | 95% |
| "write documentation" | moderate | documentation | scribe persona, --persona-scribe=en, Context7 | 95% |
| "improve iteratively" | moderate | iterative | intelligent persona, --seq, loop creation | 90% |
| "analyze large codebase" | complex | any | --delegate --parallel-dirs, domain specialists | 95% |
| "comprehensive audit" | complex | multi | --multi-agent --parallel-focus, specialized agents | 95% |
| "improve large system" | complex | any | --wave-mode --adaptive-waves | 90% |
| "security audit enterprise" | complex | security | --wave-mode --wave-validation | 95% |
| "modernize legacy system" | complex | legacy | --wave-mode --enterprise-waves --wave-checkpoint | 92% |
| "comprehensive code review" | complex | quality | --wave-mode --wave-validation --systematic-waves | 94% |

### Decision Trees

#### Tool Selection Logic

**Base Tool Selection**:
- **Search**: Grep (specific patterns) or Agent (open-ended)
- **Understanding**: Sequential (complexity >0.7) or Read (simple)  
- **Documentation**: Context7
- **UI**: Magic
- **Testing**: Playwright

**Delegation & Wave Evaluation**:
- **Delegation Score >0.6**: Add Task tool, auto-enable delegation flags based on scope
- **Wave Score >0.7**: Add Sequential for coordination, auto-enable wave strategies based on requirements

**Auto-Flag Assignment**:
- Directory count >7 → `--delegate --parallel-dirs`
- Focus areas >2 → `--multi-agent --parallel-focus`  
- High complexity + critical quality → `--wave-mode --wave-validation`
- Multiple operation types → `--wave-mode --adaptive-waves`

#### Task Delegation Intelligence

**Sub-Agent Delegation Decision Matrix**:

**Delegation Scoring Factors**:
- **Complexity >0.6**: +0.3 score
- **Parallelizable Operations**: +0.4 (scaled by opportunities/5, max 1.0)
- **High Token Requirements >15K**: +0.2 score  
- **Multi-domain Operations >2**: +0.1 per domain

**Wave Opportunity Scoring**:
- **High Complexity >0.8**: +0.4 score
- **Multiple Operation Types >2**: +0.3 score
- **Critical Quality Requirements**: +0.2 score
- **Large File Count >50**: +0.1 score
- **Iterative Indicators**: +0.2 (scaled by indicators/3)
- **Enterprise Scale**: +0.15 score

**Strategy Recommendations**:
- **Wave Score >0.7**: Use wave strategies
- **Directories >7**: `parallel_dirs`
- **Focus Areas >2**: `parallel_focus`  
- **High Complexity**: `adaptive_delegation`
- **Default**: `single_agent`

**Wave Strategy Selection**:
- **Security Focus**: `wave_validation`
- **Performance Focus**: `progressive_waves`
- **Critical Operations**: `wave_validation`
- **Multiple Operations**: `adaptive_waves`
- **Enterprise Scale**: `enterprise_waves`
- **Default**: `systematic_waves`

**Auto-Delegation Triggers**:
**Directory Threshold**:
  - **Condition**: directory_count > 7
  - **Action**: auto_enable --delegate --parallel-dirs
  - **Confidence**: 95%
**File Threshold**:
  - **Condition**: file_count > 50 AND complexity > 0.6
  - **Action**: auto_enable --delegate --sub-agents [calculated]
  - **Confidence**: 90%
**Multi Domain**:
  - **Condition**: domains.length > 3
  - **Action**: auto_enable --delegate --parallel-focus
  - **Confidence**: 85%
**Complex Analysis**:
  - **Condition**: complexity > 0.8 AND scope = comprehensive
  - **Action**: auto_enable --delegate --focus-agents
  - **Confidence**: 90%
**Token Optimization**:
  - **Condition**: estimated_tokens > 20000
  - **Action**: auto_enable --delegate --aggregate-results
  - **Confidence**: 80%

**Wave Auto-Delegation Triggers**:
- Complex improvement: complexity > 0.8 AND files > 20 AND operation_types > 2 → --wave-count 5 (95%)
- Multi-domain analysis: domains > 3 AND tokens > 15K → --adaptive-waves (90%)
- Critical operations: production_deploy OR security_audit → --wave-validation (95%)
- Enterprise scale: files > 100 AND complexity > 0.7 AND domains > 2 → --enterprise-waves (85%)
- Large refactoring: large_scope AND structural_changes AND complexity > 0.8 → --systematic-waves --wave-validation (93%)

**Delegation Routing Table**:

| Operation | Complexity | Auto-Delegates | Performance Gain |
|-----------|------------|----------------|------------------|
| `/load @monorepo/` | moderate | --delegate --parallel-dirs | 65% |
| `/analyze --comprehensive` | high | --multi-agent --parallel-focus | 70% |
| Comprehensive system improvement | high | --wave-mode --progressive-waves | 80% |
| Enterprise security audit | high | --wave-mode --wave-validation | 85% |
| Large-scale refactoring | high | --wave-mode --systematic-waves | 75% |

**Sub-Agent Specialization Matrix**:
- **Quality**: qa persona, complexity/maintainability focus, Read/Grep/Sequential tools
- **Security**: security persona, vulnerabilities/compliance focus, Grep/Sequential/Context7 tools
- **Performance**: performance persona, bottlenecks/optimization focus, Read/Sequential/Playwright tools
- **Architecture**: architect persona, patterns/structure focus, Read/Sequential/Context7 tools
- **API**: backend persona, endpoints/contracts focus, Grep/Context7/Sequential tools

**Wave-Specific Specialization Matrix**:
- **Review**: analyzer persona, current_state/quality_assessment focus, Read/Grep/Sequential tools
- **Planning**: architect persona, strategy/design focus, Sequential/Context7/Write tools
- **Implementation**: intelligent persona, code_modification/feature_creation focus, Edit/MultiEdit/Task tools
- **Validation**: qa persona, testing/validation focus, Sequential/Playwright/Context7 tools
- **Optimization**: performance persona, performance_tuning/resource_optimization focus, Read/Sequential/Grep tools

#### Persona Auto-Activation System

**Multi-Factor Activation Scoring**:
- **Keyword Matching**: Base score from domain-specific terms (30%)
- **Context Analysis**: Project phase, urgency, complexity assessment (40%)
- **User History**: Past preferences and successful outcomes (20%)
- **Performance Metrics**: Current system state and bottlenecks (10%)

**Intelligent Activation Rules**:

**Performance Issues** → `--persona-performance` + `--focus performance`
- **Trigger Conditions**: Response time >500ms, error rate >1%, high resource usage
- **Confidence Threshold**: 85% for automatic activation

**Security Concerns** → `--persona-security` + `--focus security`
- **Trigger Conditions**: Vulnerability detection, auth failures, compliance gaps
- **Confidence Threshold**: 90% for automatic activation

**UI/UX Tasks** → `--persona-frontend` + `--magic`
- **Trigger Conditions**: Component creation, responsive design, accessibility
- **Confidence Threshold**: 80% for automatic activation

**Complex Debugging** → `--persona-analyzer` + `--think` + `--seq`
- **Trigger Conditions**: Multi-component failures, root cause investigation
- **Confidence Threshold**: 75% for automatic activation

**Documentation Tasks** → `--persona-scribe=en`
- **Trigger Conditions**: README, wiki, guides, commit messages, API docs
- **Confidence Threshold**: 70% for automatic activation

#### Flag Auto-Activation Patterns

**Context-Based Auto-Activation**:
- Performance issues → --persona-performance + --focus performance + --think
- Security concerns → --persona-security + --focus security + --validate
- UI/UX tasks → --persona-frontend + --magic + --c7
- Complex debugging → --think + --seq + --persona-analyzer
- Large codebase → --uc when context >75% + --delegate auto
- Testing operations → --persona-qa + --play + --validate
- DevOps operations → --persona-devops + --safe-mode + --validate
- Refactoring → --persona-refactorer + --wave-strategy systematic + --validate
- Iterative improvement → --loop for polish, refine, enhance keywords

**Wave Auto-Activation**:
- Complex multi-domain → --wave-mode auto when complexity >0.8 AND files >20 AND types >2
- Enterprise scale → --wave-strategy enterprise when files >100 AND complexity >0.7 AND domains >2
- Critical operations → Wave validation enabled by default for production deployments
- Legacy modernization → --wave-strategy enterprise --wave-delegation tasks
- Performance optimization → --wave-strategy progressive --wave-delegation files
- Large refactoring → --wave-strategy systematic --wave-delegation folders

**Sub-Agent Auto-Activation**:
- File analysis → --delegate files when >50 files detected
- Directory analysis → --delegate folders when >7 directories detected
- Mixed scope → --delegate auto for complex project structures
- High concurrency → --concurrency auto-adjusted based on system resources

**Loop Auto-Activation**:
- Quality improvement → --loop for polish, refine, enhance, improve keywords
- Iterative requests → --loop when "iteratively", "step by step", "incrementally" detected
- Refinement operations → --loop for cleanup, fix, correct operations on existing code

#### Flag Precedence Rules
1. Safety flags (--safe-mode) > optimization flags
2. Explicit flags > auto-activation
3. Thinking depth: --ultrathink > --think-hard > --think
4. --no-mcp overrides all individual MCP flags
5. Scope: system > project > module > file
6. Last specified persona takes precedence
7. Wave mode: --wave-mode off > --wave-mode force > --wave-mode auto
8. Sub-Agent delegation: explicit --delegate > auto-detection
9. Loop mode: explicit --loop > auto-detection based on refinement keywords
10. --uc auto-activation overrides verbose flags

### Confidence Scoring
Based on pattern match strength (40%), historical success rate (30%), context completeness (20%), resource availability (10%).

## Quality Gates & Validation Framework

### 8-Step Validation Cycle with AI Integration
**Quality Gates**:
  - **Step 1 Syntax**: language parsers, Context7 validation, intelligent suggestions
  - **Step 2 Type**: Sequential analysis, type compatibility, context-aware suggestions
  - **Step 3 Lint**: Context7 rules, quality analysis, refactoring suggestions
  - **Step 4 Security**: Sequential analysis, vulnerability assessment, OWASP compliance
  - **Step 5 Test**: Playwright E2E, coverage analysis (≥80% unit, ≥70% integration)
  - **Step 6 Performance**: Sequential analysis, benchmarking, optimization suggestions
  - **Step 7 Documentation**: Context7 patterns, completeness validation, accuracy verification
  - **Step 8 Integration**: Playwright testing, deployment validation, compatibility verification
**Validation Automation**:
  - **Continuous Integration**: CI/CD pipeline integration, progressive validation, early failure detection
  - **Intelligent Monitoring**: success rate monitoring, ML prediction, adaptive validation
  - **Evidence Generation**: comprehensive evidence, validation metrics, improvement recommendations
**Wave Integration**:
  - **Validation Across Waves**: wave boundary gates, progressive validation, rollback capability
  - **Compound Validation**: AI orchestration, domain-specific patterns, intelligent aggregation

### Task Completion Criteria
**Completion Requirements**:
  - **Validation**: all 8 steps pass, evidence provided, metrics documented
  - **Ai Integration**: MCP coordination, persona integration, tool orchestration, ≥90% context retention
  - **Performance**: response time targets, resource limits, success thresholds, token efficiency
  - **Quality**: code quality standards, security compliance, performance assessment, integration testing
**Evidence Requirements**:
  - **Quantitative**: performance/quality/security metrics, coverage percentages, response times
  - **Qualitative**: code quality improvements, security enhancements, UX improvements
  - **Documentation**: change rationale, test results, performance benchmarks, security scans

## ⚡ Performance Optimization

Resource management, operation batching, and intelligent optimization for sub-100ms performance targets.

**Token Management**: Intelligent resource allocation based on unified Resource Management Thresholds (see Detection Engine section)

**Operation Batching**:
- **Tool Coordination**: Parallel operations when no dependencies
- **Context Sharing**: Reuse analysis results across related routing decisions
- **Cache Strategy**: Store successful routing patterns for session reuse
- **Task Delegation**: Intelligent sub-agent spawning for parallel processing
- **Resource Distribution**: Dynamic token allocation across sub-agents

**Resource Allocation**:
- **Detection Engine**: 1-2K tokens for pattern analysis
- **Decision Trees**: 500-1K tokens for routing logic
- **MCP Coordination**: Variable based on servers activated


## 🔗 Integration Intelligence

Smart MCP server selection and orchestration.

### MCP Server Selection Matrix
**Reference**: See MCP.md for detailed server capabilities, workflows, and integration patterns.

**Quick Selection Guide**:
- **Context7**: Library docs, framework patterns
- **Sequential**: Complex analysis, multi-step reasoning
- **Magic**: UI components, design systems
- **Playwright**: E2E testing, performance metrics

### Intelligent Server Coordination
**Reference**: See MCP.md for complete server orchestration patterns and fallback strategies.

**Core Coordination Logic**: Multi-server operations, fallback chains, resource optimization

### Persona Integration
**Reference**: See PERSONAS.md for detailed persona specifications and MCP server preferences.

## 🚨 Emergency Protocols

Handling resource constraints and failures gracefully.

### Resource Management
Threshold-based resource management follows the unified Resource Management Thresholds (see Detection Engine section above).

### Graceful Degradation
- **Level 1**: Reduce verbosity, skip optional enhancements, use cached results
- **Level 2**: Disable advanced features, simplify operations, batch aggressively
- **Level 3**: Essential operations only, maximum compression, queue non-critical

### Error Recovery Patterns
- **MCP Timeout**: Use fallback server
- **Token Limit**: Activate compression
- **Tool Failure**: Try alternative tool
- **Parse Error**: Request clarification




## 🔧 Configuration

### Orchestrator Settings
**Orchestrator Config**:
  - **Enable Caching**: True
  - **Cache Ttl**: 3600
  - **Parallel Operations**: True
  - **Max Parallel**: 3
  - **Learning Enabled**: True
  - **Confidence Threshold**: 0.7
  - **Pattern Detection**: aggressive
  - **Token Reserve**: 10%
  - **Emergency Threshold**: 90%
  - **Compression Threshold**: 75%
  **Wave Mode**:
    - **Enable Auto Detection**: True
    - **Wave Score Threshold**: 0.7
    - **Max Waves Per Operation**: 5
    - **Adaptive Wave Sizing**: True
    - **Wave Validation Required**: True

### Custom Routing Rules
Users can add custom routing patterns via YAML configuration files.


---


