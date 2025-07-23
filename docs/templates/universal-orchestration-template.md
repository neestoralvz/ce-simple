# Universal Orchestration Template

**A comprehensive framework for creating self-orchestrating systems with parallel execution, intelligent assessment, and adaptive deployment.**

## Multi-Purpose Applications

### Command Systems
- Slash commands for development workflows
- CI/CD pipeline orchestration  
- Automated deployment systems
- Quality assurance workflows

### Business Processes
- Project management automation
- Resource allocation systems
- Decision support frameworks
- Performance monitoring systems

### Technical Infrastructure
- Microservice coordination
- Data processing pipelines
- System health monitoring
- Load balancing systems

## Universal Header Structure

```markdown
# [SYSTEM_NAME] - [TYPE] [CATEGORY]

## Purpose  
[Single paragraph defining orchestration objective, scope, and expected outcomes]

## Operating Principles
**Primary Responsibility**: [Define exclusive focus and operational boundaries]
**Processing Methodology**: [Describe work decomposition and execution approach]  
**Decision Framework**: [Define assessment criteria and deployment thresholds]
**Resilience Protocol**: [Specify failure handling, recovery, and adaptation mechanisms]
```

## Universal 4-Phase Orchestration Framework

### Phase 1: System Validation and Assessment
```markdown
Update TodoWrite: Mark "[PROCESS_NAME] system validation" as in_progress

System Structure Validation:
- Use LS tool to verify [REQUIRED_DIRECTORIES] accessibility
- Validate [CRITICAL_COMPONENTS] existence and integrity  
- Confirm [DEPENDENCY_STRUCTURES] organization
- Ensure system readiness before [PROCESS_TYPE] execution

Complexity Assessment Framework:
```bash
# Universal complexity calculation
scope=$(analyze_[DOMAIN]_scope)
breadth=$(count_[ENTITY]_domains)
interdep=$(analyze_[RELATIONSHIP]_dependencies)  
complexity=$(echo "scale=4; ($scope + $breadth + $interdep) / 3" | bc)
```

Requirements Analysis:
- Determine [SCOPE_TYPE] depth and breadth requirements
- Identify [EXPERTISE_DOMAINS] needed for execution
- Evaluate [DEPENDENCY_TYPE] complexity factors
- Calculate optimal deployment strategy from complexity metrics
```

### Phase 2: Intelligent Agent Deployment  
```markdown
Update TodoWrite: Complete previous, mark "Intelligent agent deployment" as in_progress

Conditional Deployment Logic:
- If complexity ≥[THRESHOLD_1]: Deploy `/[PRIMARY_COMMAND]` for [PRIMARY_PURPOSE]
- If [METRIC_TYPE] ≥[THRESHOLD_2]: Deploy `/[SECONDARY_COMMAND]` for [SECONDARY_PURPOSE]  
- If [CONDITION_TYPE] detected: Deploy `/[SPECIALIZED_COMMAND_1]` for [SPECIALIZED_PURPOSE_1]
- If [CONDITION_TYPE] detected: Deploy `/[SPECIALIZED_COMMAND_2]` for [SPECIALIZED_PURPOSE_2]

Parallel Coordination Protocol:
- Execute simultaneous Task Tool deployment for maximum efficiency
- Monitor agent initialization and readiness status
- Validate successful deployment before proceeding to execution
- Implement retry mechanisms for deployment failures
```

### Phase 3: Execution Coordination and Monitoring
```markdown  
Update TodoWrite: Complete previous, mark "[PROCESS_NAME] coordination and monitoring" as in_progress

Parallel Execution Management:
- Monitor Task Tool agent progress and execution status
- Track [DELIVERABLE_TYPE] completion across all deployed agents
- Coordinate inter-agent communication and dependency management
- Resolve coordination bottlenecks and execution issues

Intermediate Result Collection:
- Gather partial [OUTPUT_TYPE] from active agents
- Validate [QUALITY_METRIC] and completeness standards
- Identify gaps requiring additional [PROCESS_TYPE]
- Adjust execution strategy based on intermediate findings
```

### Phase 4: Result Aggregation and Validation
```markdown
Update TodoWrite: Complete previous, mark "[PROCESS_NAME] result aggregation" as in_progress

Comprehensive Result Synthesis:
- Collect final outputs from all deployed Task Tool agents
- Synthesize findings with pattern extraction and conflict resolution
- Resolve discrepancies between agent [OUTPUT_TYPES]
- Generate comprehensive [DELIVERABLE_NAME] with complete coverage

Systematic Validation Protocol:
```bash
# Universal completion validation
total_scope=$(calculate_total_[SCOPE_TYPE])
covered_scope=$(get_covered_[SCOPE_TYPE])
completeness=$(echo "scale=4; $covered_scope * 100 / $total_scope" | bc)
```

Quality Assurance Checks:
- Verify request fulfillment ≥[COMPLETION_THRESHOLD]% scope coverage
- Confirm all Task Tool agents completed successfully
- Validate learning patterns captured and documented  
- Ensure system integrity maintained ≥[INTEGRITY_THRESHOLD]%

Failure Recovery Protocol:
- If validation fails: Add TodoWrite task "Resolve [PROCESS_NAME] gap: [SPECIFIC_ISSUE]"
- Re-deploy agents with enhanced [PROCESS_TYPE] protocols
- Recalculate complexity using refined assessment parameters
- Re-execute phases with adjusted scope and strategy

Update TodoWrite: Complete all [COMMAND_NAME] tasks
Add follow-up: "[COMMAND_NAME] complete with comprehensive [DELIVERABLE_TYPE] ready"
```

---

## Universal Customization Guide

### Required Template Variables
```yaml
COMMAND_NAME: "Actual command name (e.g., 'Enhanced Analysis')"
CATEGORY: "Command category (e.g., 'Discovery', 'Analysis', 'Validation')"
PROCESS_NAME: "Main process identifier (e.g., 'analysis', 'discovery', 'execution')"
PROCESS_TYPE: "Process methodology (e.g., 'investigation', 'computation', 'validation')"

# System Structure Variables
REQUIRED_DIRECTORIES: "Critical directories for validation (e.g., 'docs/', 'commands/')"
CRITICAL_COMPONENTS: "Essential system components (e.g., 'core commands', 'configuration files')"
DEPENDENCY_STRUCTURES: "Dependency organization (e.g., 'context directories', 'framework files')"

# Assessment Variables  
DOMAIN: "Assessment domain (e.g., 'request', 'technical', 'business')"
ENTITY: "Countable entities (e.g., 'feature', 'component', 'requirement')" 
RELATIONSHIP: "Dependency relationships (e.g., 'system', 'data', 'workflow')"
SCOPE_TYPE: "Scope classification (e.g., 'technical', 'functional', 'business')"
EXPERTISE_DOMAINS: "Required expertise areas (e.g., 'technical domains', 'business areas')"
DEPENDENCY_TYPE: "Dependency classification (e.g., 'technical', 'organizational', 'temporal')"

# Deployment Variables
THRESHOLD_1: "Primary deployment threshold (numeric, e.g., '6.0', '0.7500')"
THRESHOLD_2: "Secondary deployment threshold (numeric, e.g., '4.0', '0.6000')"
PRIMARY_COMMAND: "Main command for deployment (e.g., 'worktree-start', 'explore-codebase')"
SECONDARY_COMMAND: "Secondary command (e.g., 'capture-learnings', 'validate-code')"
SPECIALIZED_COMMAND_1: "First specialized command (e.g., 'explore-codebase')"
SPECIALIZED_COMMAND_2: "Second specialized command (e.g., 'explore-web')"
PRIMARY_PURPOSE: "Main command purpose (e.g., 'isolation setup', 'code analysis')"
SECONDARY_PURPOSE: "Secondary command purpose (e.g., 'knowledge extraction', 'quality validation')"
SPECIALIZED_PURPOSE_1: "First specialized purpose (e.g., 'internal analysis')"
SPECIALIZED_PURPOSE_2: "Second specialized purpose (e.g., 'external research')"

# Execution Variables
DELIVERABLE_TYPE: "Expected deliverable (e.g., 'analysis', 'findings', 'recommendations')"
OUTPUT_TYPE: "Agent output format (e.g., 'results', 'reports', 'analyses')"
QUALITY_METRIC: "Quality measurement (e.g., 'accuracy', 'completeness', 'depth')"
DELIVERABLE_NAME: "Final deliverable name (e.g., 'comprehensive analysis', 'discovery report')"

# Validation Variables
SCOPE_TYPE: "Scope measurement unit (e.g., 'requirements', 'features', 'components')"
COMPLETION_THRESHOLD: "Completion percentage (e.g., '95', '90', '85')"
INTEGRITY_THRESHOLD: "System integrity percentage (e.g., '85', '90', '95')"

# Conditional Variables  
METRIC_TYPE: "Measurement metric (e.g., 'learning_value', 'technical_depth', 'business_impact')"
CONDITION_TYPE: "Detection condition (e.g., 'multi-domain', 'high-complexity', 'cross-functional')"
```

### Universal Principles for Any Command Type

1. **Structure Consistency**: Always maintain 4-phase execution framework
2. **Mathematical Precision**: Use 4-decimal precision for all calculations  
3. **Parallel Optimization**: Default to concurrent execution unless dependencies exist
4. **Error Resilience**: Include comprehensive failure handling and recovery
5. **Learning Integration**: Capture patterns and improve execution over time
6. **Foundation Integration**: Leverage 00-core infrastructure when applicable

### Adaptation Guidelines by Command Category

**Discovery Commands**: Focus on investigation breadth and information gathering
**Analysis Commands**: Emphasize depth, accuracy, and systematic evaluation  
**Execution Commands**: Prioritize efficiency, parallel processing, and deliverable quality
**Validation Commands**: Concentrate on verification, quality assurance, and compliance
**Maintenance Commands**: Focus on system health, optimization, and reliability

## Template Usage Instructions

### Required Replacements
1. **[Command Name]**: Replace with actual command name (e.g., "Enhanced Analysis")
2. **[Category]**: Replace with command category (e.g., "Discovery", "Analysis", "Validation")
3. **[Process]**: Replace with the main process type (e.g., "Discovery", "Analysis", "Execution")
4. **[threshold]**: Replace with specific numerical thresholds for deployment decisions
5. **[relevant-command]**: Replace with actual command names for Task Tool execution
6. **[purpose]**: Replace with specific purpose for each command deployment
7. **[condition]**: Replace with specific conditions for deployment decisions

### Customization Guidelines
- Adapt the complexity calculation formula based on command-specific factors
- Modify deployment conditions based on command requirements
- Adjust validation criteria based on expected outcomes
- Update error handling based on command-specific failure modes

### Structure Principles
- Maintain 4-phase structure for consistency
- Keep TodoWrite integration for progress tracking
- Preserve parallel deployment patterns
- Maintain validation and error recovery protocols