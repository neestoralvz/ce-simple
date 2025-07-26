# VDD Sub-Agent Command Mapping

**Updated**: 2025-07-26 | **Purpose**: Migration mapping from monolithic commands to specialized sub-agents | **Authority**: Sub-agent architecture transition

## Migration Overview

Transform 89 existing commands across 15 categories into specialized sub-agent architecture with 4 primary agent types maintaining backward compatibility and improving parallel coordination.

## Agent Specialization Matrix

### Discovery Agent - Autonomous Explorer
**Specialization**: Code analysis, pattern detection, information gathering, computational analysis  
**Coordination**: Independent operation with result sharing  
**Assigned Categories**: 01-discovery, 03-analysis, 12-math, 13-search

#### Command Assignments
**01-discovery (4 commands)**:
- `/explore-codebase` → Discovery Agent: Codebase exploration and mapping
- `/think-layers` → Discovery Agent: Progressive analysis methodology  
- `/think-layers-parallel` → Discovery Agent: Parallel cognitive analysis
- `/explore-web` → Discovery Agent: Web-based information gathering

**03-analysis (5 commands)**:
- `/complexity-assess` → Discovery Agent: Technical complexity evaluation
- `/load-balance` → Discovery Agent: Resource distribution analysis
- `/analyze-parallel` → Discovery Agent: Parallel analysis coordination
- `/analyze-parallel-implementation` → Discovery Agent: Implementation analysis
- `/problem-solving` → Discovery Agent: Systematic problem decomposition

**12-math (5 commands)**:
- `/calculate-complexity` → Discovery Agent: Mathematical complexity computation
- `/analyze-metrics` → Discovery Agent: Metrics analysis and evaluation
- `/statistical-analyze` → Discovery Agent: Statistical data analysis
- `/optimize-calculate` → Discovery Agent: Optimization calculations
- `/predictive-model` → Discovery Agent: Predictive modeling and forecasting

**13-search (4 commands)**:
- `/search-advanced` → Discovery Agent: Advanced search with intelligent filtering
- `/discover-information` → Discovery Agent: Information discovery and synthesis
- `/filter-results` → Discovery Agent: Result filtering and optimization
- `/index-content` → Discovery Agent: Content indexing and organization

**Total Discovery Agent Commands**: 18

### Planning Agent - Strategic Coordinator
**Specialization**: Strategy development, resource planning, system evolution, meta-coordination  
**Coordination**: Collaborative leadership with other agents  
**Assigned Categories**: 00-core, 02-planning, 08-learning, 11-meta

#### Command Assignments
**00-core (7 commands)**:
- `/enhanced-start` → Planning Agent: Advanced discovery workflow orchestration
- `/start` → Planning Agent: Intelligent discovery workflow initiation
- `/init-project` → Planning Agent: Project initialization strategy
- `/handoff-manager` → Planning Agent: Context preservation coordination
- `/context-engine` → Planning Agent: Context management and optimization
- `/notify-manager` → Planning Agent: Communication and notification coordination

**02-planning (7 commands)**:
- `/strategy-optimize` → Planning Agent: Strategic optimization and planning
- `/plan-phases` → Planning Agent: Phase-based planning and coordination
- `/resource-plan` → Planning Agent: Resource allocation and management
- `/risk-assess` → Planning Agent: Risk assessment and mitigation planning
- `/architect-solution` → Planning Agent: Solution architecture development
- `/feedback-vision` → Planning Agent: Vision feedback integration
- `/vision-propagate` → Planning Agent: Vision propagation and alignment

**08-learning (4 commands)**:
- `/capture-learnings` → Planning Agent: Pattern extraction and learning coordination
- `/interview-feedback` → Planning Agent: User feedback capture coordination
- `/system-monitor` → Planning Agent: System monitoring coordination
- `/performance-track` → Planning Agent: Performance tracking coordination

**11-meta (4 commands)**:
- `/command-create` → Planning Agent: Meta-level command development coordination
- `/command-maintain` → Planning Agent: System maintenance coordination
- `/sub-agent-migrate` → Planning Agent: Migration strategy coordination
- `/matrix-maintenance` → Planning Agent: Cross-reference maintenance coordination

**Total Planning Agent Commands**: 22

### Execution Agent - Implementation Specialist
**Specialization**: Implementation, file operations, documentation generation, git workflow  
**Coordination**: Coordinated execution with synchronization  
**Assigned Categories**: 04-execution, 06-documentation, 09-git

#### Command Assignments
**04-execution (6 commands)**:
- `/agent-orchestration` → Execution Agent: Master agent deployment and coordination
- `/agent-coordinate` → Execution Agent: High-level orchestration strategy
- `/agent-deploy` → Execution Agent: Agent deployment and management
- `/config-dynamic` → Execution Agent: Configuration management implementation
- `/result-consolidate` → Execution Agent: Result aggregation and consolidation

**06-documentation (2 commands)**:
- `/docs-maintain` → Execution Agent: Documentation maintenance and consistency

**09-git (4 commands)**:
- `/git-worktree` → Execution Agent: Git worktree management and coordination
- `/worktree-start` → Execution Agent: Worktree initialization and setup
- `/worktree-close` → Execution Agent: Worktree cleanup and finalization
- `/worktree-cleanup` → Execution Agent: Comprehensive worktree maintenance

**Total Execution Agent Commands**: 12

### Validation Agent - Quality Assurance Specialist
**Specialization**: Quality assurance, system health, standards enforcement, compliance checking  
**Coordination**: Independent validation with strict criteria  
**Assigned Categories**: 05-validation, 07-maintenance, 10-standards

#### Command Assignments
**05-validation (7 commands)**:
- `/validate-complete` → Validation Agent: Comprehensive validation framework
- `/validate-code` → Validation Agent: Code quality validation
- `/validate-creative` → Validation Agent: Creative output validation
- `/validate-visual` → Validation Agent: Visual verification and validation
- `/quality-gates` → Validation Agent: Quality gate enforcement
- `/test-orchestrate` → Validation Agent: Testing orchestration and coordination
- `/performance-validate` → Validation Agent: Performance validation and benchmarking

**07-maintenance (2 commands)**:
- `/context-optimize` → Validation Agent: Context optimization and validation

**10-standards (4 commands)**:
- `/standard-writing` → Validation Agent: Writing standards enforcement
- `/standard-naming` → Validation Agent: Naming convention validation
- `/template-command` → Validation Agent: Command template compliance
- `/template-docs` → Validation Agent: Documentation template compliance

**Total Validation Agent Commands**: 13

### Shared Utilities - Multi-Agent Support
**Specialization**: Common functionality across all agent types  
**Coordination**: Utility services for all agents  
**Assigned Categories**: 14-utils

#### Command Assignments
**14-utils (9 commands)**:
- `/calc-engine` → All Agents: Mathematical computation utilities
- `/config-manager` → All Agents: Configuration management utilities
- `/deploy-core` → All Agents: Deployment coordination utilities
- `/monitor-core` → All Agents: System monitoring utilities
- `/todo-manager` → All Agents: Task management utilities
- `/validator-core` → All Agents: Validation service utilities
- `/agent-lifecycle` → All Agents: Agent lifecycle management
- `/phase-manager` → All Agents: Phase management utilities
- `/validation-engine` → All Agents: Validation engine services

**Total Utility Commands**: 9

## Migration Statistics

**Total Commands Analyzed**: 89  
**Discovery Agent**: 18 commands (20%)  
**Planning Agent**: 22 commands (25%)  
**Execution Agent**: 12 commands (13%)  
**Validation Agent**: 13 commands (15%)  
**Shared Utilities**: 9 commands (10%)  
**Local Commands**: 3 commands (3%) - explore-codebase.md, init-project.md, start.md  
**Top-level Commands**: 3 commands (3%) - handled by Planning Agent
**README Files**: 15 files (17%) - documentation only

## Migration Priorities

### Phase 1: Core Agent Implementation
**Priority**: Critical foundation commands  
**Timeline**: Immediate implementation  
**Commands**: `/enhanced-start`, `/agent-orchestration`, `/validate-complete`, `/explore-codebase`

### Phase 2: Category Migration
**Priority**: Complete category specialization  
**Timeline**: Systematic category-by-category migration  
**Order**: 01-discovery → 04-execution → 05-validation → 02-planning

### Phase 3: Coordination Integration
**Priority**: Inter-agent communication and coordination  
**Timeline**: After individual agent specialization  
**Focus**: Communication protocols, task distribution, result aggregation

### Phase 4: Optimization & Refinement
**Priority**: Performance optimization and fine-tuning  
**Timeline**: Continuous improvement based on usage patterns  
**Focus**: Resource optimization, load balancing, coordination efficiency

## Backward Compatibility Strategy

### Compatibility Layer
- **Command Interface Preservation**: Original command syntax and parameters maintained
- **Gradual Migration**: Commands transparently delegate to appropriate sub-agents
- **Feature Flag Control**: Migration controlled via configuration flags
- **Fallback Mechanism**: Automatic fallback to monolithic execution on sub-agent failure

### Migration Validation
- **Functional Testing**: Ensure identical outputs between monolithic and sub-agent execution
- **Performance Testing**: Validate performance improvements with sub-agent architecture
- **Integration Testing**: Comprehensive testing of inter-agent coordination
- **User Experience Testing**: Ensure seamless transition with no user disruption

## Success Metrics

**Migration Completeness**: 100% of commands successfully mapped to appropriate agents  
**Performance Improvement**: ≥25% improvement in parallel execution efficiency  
**Coordination Effectiveness**: ≥90% successful inter-agent task coordination  
**Backward Compatibility**: 100% functional compatibility maintained during transition  
**System Reliability**: ≤5% increase in failure rate during migration period

---

**Migration Principle**: Systematic transformation of monolithic command architecture into specialized agent coordination while preserving user experience and system reliability.