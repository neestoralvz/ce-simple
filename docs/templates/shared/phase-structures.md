# Phase Structures - Reusable Component Library

## Purpose
Provides composable phase templates eliminating repeated structures across commands and documentation, implementing DRY principles through modular design.

## Standard Phase Templates

### 1. Basic 5-Phase Command Structure
```markdown
## Execution Process

### Phase 1: Discovery and Setup
**Duration**: {5-15} minutes
**Responsible**: Command executor
**Prerequisites**: 
- {prerequisite_1}
- {prerequisite_2}

**TodoWrite Update**: mark "{phase_1_task_name}" as in_progress

**Primary Actions**:
1. {discovery_action_1} - {expected_discovery_outcome}
2. {setup_action_2} - {environment_preparation_result}
3. {validation_action_3} - {readiness_verification}

**Quality Checks**:
- [ ] {discovery_checkpoint_1}
- [ ] {setup_checkpoint_2}
- [ ] {validation_checkpoint_3}

**Success Criteria**: {phase_1_completion_definition}

### Phase 2: Analysis and Planning
**Duration**: {10-20} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 1 completed successfully

**TodoWrite Update**: complete previous, mark "{phase_2_task_name}" as in_progress

**Primary Actions**:
1. {analysis_action_1} - {analysis_outcome}
2. {planning_action_2} - {strategy_definition}
3. {resource_action_3} - {resource_allocation}

**Quality Checks**:
- [ ] {analysis_checkpoint_1}
- [ ] {planning_checkpoint_2}
- [ ] {resource_checkpoint_3}

**Success Criteria**: {phase_2_completion_definition}

### Phase 3: Implementation and Execution
**Duration**: {15-30} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 2 planning approved

**TodoWrite Update**: complete previous, mark "{phase_3_task_name}" as in_progress

**Primary Actions**:
1. {implementation_action_1} - {concrete_deliverable}
2. {execution_action_2} - {measurable_outcome}
3. {quality_action_3} - {verification_result}

**Quality Checks**:
- [ ] {implementation_checkpoint_1}
- [ ] {execution_checkpoint_2}
- [ ] {quality_checkpoint_3}

**Success Criteria**: {phase_3_completion_definition}

### Phase 4: Validation and Documentation
**Duration**: {5-10} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 3 implementation complete

**TodoWrite Update**: complete previous, mark "{phase_4_task_name}" as in_progress

**Primary Actions**:
1. {validation_action_1} - {success_verification}
2. {documentation_action_2} - {evidence_recording}
3. {handoff_action_3} - {transition_preparation}

**Quality Checks**:
- [ ] {validation_checkpoint_1}
- [ ] {documentation_checkpoint_2}
- [ ] {handoff_checkpoint_3}

**Success Criteria**: {phase_4_completion_definition}

### Phase 5: Intelligent Routing and Handoff
**Duration**: {3-5} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 4 validation complete

**TodoWrite Update**: complete previous, mark "{phase_5_task_name}" as in_progress

**Command Routing Protocol**: Analyze execution results and recommend next commands
- **Context Analysis**: Review completion state and identify continuation opportunities
- **Priority Assessment**: Evaluate recommended commands using mathematical priority scoring
- **Handoff Protocol**: Format recommendations as "Next: /{command} ({priority}) - {rationale}"
- **Integration**: Coordinate with /handoff-manager and /notify-manager for seamless transitions
- **Documentation**: Record routing decisions and rationale for learning extraction

**Routing Format**: "Next: /{category}/{command} ({high|medium|low}) - {execution_rationale}"

**TodoWrite Update**: complete all {command_name} tasks

**Success Criteria**: Clear next steps identified and documented
```

### 2. P55/P56 Compliant Phase Structure
```markdown
## P55/P56 Compliant Execution Process

### Phase 1: Script Foundation and Compliance Setup
**Duration**: {5-10} minutes
**Responsible**: Command executor
**Prerequisites**: P55/P56 compliance environment available

**TodoWrite Update**: mark "{phase_1_task_name}" as in_progress

**🛡️ P55/P56 Compliance Protocol**:
```bash
# Load mathematical foundation
source scripts/core/path-helper.sh
source scripts/formulas/context_engineering_formulas.sh

# Initialize compliance tracking
compliance_start_time=$(date +%s.%N)
tool_calls_executed=0
required_tool_calls={expected_count}
```

**Primary Actions**:
1. **Script Loading**: Load mathematical formula library via tool calls
2. **Environment Validation**: Validate script availability and function access  
3. **Compliance Initialization**: Initialize tracking and evidence collection

**Quality Checks**:
- [ ] Mathematical formulas loaded successfully
- [ ] Tool call execution environment verified
- [ ] Compliance tracking initialized

**Success Criteria**: 100% compliance environment ready

### Phase 2: Mathematical Analysis and Tool Integration
**Duration**: {10-15} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 1 compliance environment active

**TodoWrite Update**: complete previous, mark "{phase_2_task_name}" as in_progress

**🛡️ Mathematical Integration**:
```bash
# Execute calculations with ≥4 decimal precision
confidence_score=$(calculate_confidence $param1 $param2 $param3)
threshold_compliance=$(calculate_threshold_compliance $score $threshold "gte")
tool_calls_executed=$((tool_calls_executed + 2))

# Visual transparency announcement
echo "🔧 TOOL EXECUTION: Calculating confidence and threshold compliance"
echo "📊 PRECISION: ≥4 decimal places maintained"
```

**Primary Actions**:
1. **Mathematical Calculation**: Execute core functionality with tool call integration
2. **Precision Validation**: Perform calculations with ≥4 decimal precision
3. **Transparency Maintenance**: Visual announcements throughout execution

**Quality Checks**:
- [ ] Mathematical precision ≥4 decimal places
- [ ] Tool calls executed (never simulated)
- [ ] Visual transparency maintained

**Success Criteria**: 100% tool call execution with mathematical precision

### Phase 3: Implementation with Compliance Verification
**Duration**: {15-25} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 2 mathematical foundation established

**TodoWrite Update**: complete previous, mark "{phase_3_task_name}" as in_progress

**🛡️ Compliance Monitoring**:
```bash
# Track implementation progress
implementation_start=$(date +%s.%N)
performance_metrics=$(calculate_performance_metrics $start_time $current_time)
tool_calls_executed=$((tool_calls_executed + 3))

# Validate P55/P56 compliance continuously
echo "P55_COMPLIANCE: $tool_calls_executed/$required_tool_calls tool calls executed"
echo "P56_TRANSPARENCY: All operations visible with mathematical evidence"
```

**Primary Actions**:
1. **Core Implementation**: Execute primary functionality with full transparency
2. **Performance Measurement**: Continuous monitoring with mathematical precision
3. **Evidence Collection**: Document all operations for compliance audit trail

**Quality Checks**:
- [ ] Implementation complete with evidence trail
- [ ] Performance metrics within acceptable bounds
- [ ] Compliance requirements continuously met

**Success Criteria**: Implementation complete with 100% P55/P56 compliance

### Phase 4: Transparent Reporting and Validation
**Duration**: {5-8} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 3 implementation with compliance verification

**TodoWrite Update**: complete previous, mark "{phase_4_task_name}" as in_progress

**🛡️ Compliance Reporting**:
```bash
# Calculate final compliance metrics
total_execution_time=$(echo "scale=4; $(date +%s.%N) - $compliance_start_time" | bc)
compliance_percentage=$(echo "scale=4; $tool_calls_executed / $required_tool_calls * 100" | bc)

# Generate compliance report
echo "📊 EXECUTION METRICS:"
echo "  - Tool Calls: $tool_calls_executed/$required_tool_calls (100% required)"
echo "  - Execution Time: ${total_execution_time}s"
echo "  - Mathematical Precision: ≥4 decimal places"
echo "  - Transparency Level: ≥95% visibility"
```

**Primary Actions**:
1. **Metrics Calculation**: Display execution metrics and compliance status
2. **Performance Reporting**: Report measurements with mathematical precision
3. **Documentation Update**: Update records with execution evidence

**Quality Checks**:
- [ ] P55 compliance: 100% tool call execution
- [ ] P56 transparency: ≥95% operation visibility
- [ ] Mathematical precision: ≥4 decimal accuracy

**Success Criteria**: Complete transparency with mathematical evidence

### Phase 5: P55/P56 Compliant Mathematical Routing
**Duration**: {5-7} minutes
**Responsible**: Command executor
**Prerequisites**: Phase 4 compliance validation complete

**TodoWrite Update**: complete previous, mark "{phase_5_task_name}" as in_progress

**🛡️ Mathematical Command Routing**:
```bash
# Calculate routing priority with mathematical precision
completion_metrics=$(calculate_completion_metrics $execution_data)
context_factors=$(analyze_context_factors $current_state)
routing_score=$(calculate_routing_priority $completion_metrics $context_factors)
tool_calls_executed=$((tool_calls_executed + 3))

echo "🧮 ROUTING CALCULATION:"
echo "  - Priority Score: $(printf "%.4f" $routing_score)"
echo "  - Mathematical Basis: Context engineering formulas"
echo "  - Tool Integration: Real calculations (0% simulation)"
```

**Primary Actions**:
1. **Performance Analysis**: Mathematical formulas for completion assessment
2. **Compliance Routing**: Next command recommendations maintain P55/P56 standards
3. **Evidence Documentation**: Record routing calculations with precision

**Routing Format**: "Next: /{command} ($(printf "%.4f" $routing_score)) - {mathematical_rationale}"

**TodoWrite Update**: complete all {command_name} tasks

**Success Criteria**: Mathematical routing with ≥4 decimal precision evidence
```

### 3. Enforcement Phase Structure
```markdown
## 🚨 ENFORCEMENT Execution Process

### Phase 1: **🚨 MANDATORY Discovery and Blocking Setup**
**Duration**: {5-10} minutes
**Responsible**: Sistema executor
**Prerequisites**: 🚨 CRITICAL enforcement environment required

**TodoWrite Update**: mark "{phase_1_task_name}" as in_progress

**🚨 BLOCKING Requirements**:
- **🚨 AUTOMATIC Discovery**: Sistema WILL identify {target_components} with ZERO tolerance
- **🚨 MANDATORY Setup**: Sistema WILL configure {enforcement_mechanisms} with BLOCKING validation
- **🚨 CRITICAL Validation**: Sistema WILL verify {readiness_criteria} with IMMEDIATE correction

**Primary Actions**:
1. **🚨 BLOCKING Discovery**: {discovery_description} with ZERO tolerance enforcement
2. **🚨 AUTOMATIC Setup**: {setup_description} with real-time monitoring
3. **🚨 CRITICAL Validation**: {validation_description} with immediate verification

**Quality Checks**:
- [ ] 🚨 MANDATORY: {checkpoint_1} with BLOCKING verification
- [ ] 🚨 AUTOMATIC: {checkpoint_2} with continuous monitoring
- [ ] 🚨 CRITICAL: {checkpoint_3} with immediate validation

**Success Criteria**: 🚨 MAXIMUM enforcement readiness with ZERO tolerance

### Phase 2: **🚨 REQUIRED Analysis and Blocking Mechanisms**
**Duration**: {10-15} minutes
**Responsible**: Sistema executor
**Prerequisites**: Phase 1 🚨 MANDATORY setup complete

**TodoWrite Update**: complete previous, mark "{phase_2_task_name}" as in_progress

**🚨 ENFORCEMENT Mechanisms**:
- **🚨 BLOCKING Analysis**: Sistema WILL analyze {target_area} with AUTOMATIC violation detection
- **🚨 MANDATORY Planning**: Sistema WILL create {enforcement_strategy} with REQUIRED compliance
- **🚨 CRITICAL Resource**: Sistema WILL allocate {enforcement_resources} with MAXIMUM priority

**Primary Actions**:
1. **🚨 MANDATORY Analysis**: {analysis_description} with systematic enforcement
2. **🚨 BLOCKING Planning**: {planning_description} with violation prevention
3. **🚨 AUTOMATIC Resource**: {resource_description} with continuous operation

**Quality Checks**:
- [ ] 🚨 BLOCKING: {checkpoint_1} with ZERO tolerance
- [ ] 🚨 MANDATORY: {checkpoint_2} with REQUIRED compliance
- [ ] 🚨 CRITICAL: {checkpoint_3} with MAXIMUM enforcement

**Success Criteria**: 🚨 BLOCKING mechanisms active with MANDATORY compliance

### Phase 3: **🚨 CRITICAL Implementation and Maximum Enforcement**
**Duration**: {15-25} minutes
**Responsible**: Sistema executor
**Prerequisites**: Phase 2 🚨 BLOCKING mechanisms active

**TodoWrite Update**: complete previous, mark "{phase_3_task_name}" as in_progress

**🚨 MAXIMUM Enforcement Protocol**:
- **🚨 ZERO TOLERANCE Implementation**: Sistema WILL execute {core_functionality} with ABSOLUTE priority
- **🚨 REAL-TIME Monitoring**: Sistema WILL monitor {implementation_aspects} with continuous correction
- **🚨 UNIVERSAL Compliance**: Sistema WILL enforce {compliance_requirements} with cross-domain application

**Primary Actions**:
1. **🚨 MAXIMUM Implementation**: PRIORIDAD ABSOLUTA with strictest enforcement
2. **🚨 BLOCKING Execution**: {execution_description} with immediate correction
3. **🚨 REQUIRED Quality**: {quality_description} with compliance verification

**Quality Checks**:
- [ ] 🚨 ZERO TOLERANCE: {checkpoint_1} with absolute priority
- [ ] 🚨 REAL-TIME: {checkpoint_2} with continuous monitoring
- [ ] 🚨 UNIVERSAL: {checkpoint_3} with cross-domain validation

**Success Criteria**: 🚨 MAXIMUM implementation with ZERO tolerance enforcement

### Phase 4: **🚨 MAXIMUM Validation and Enforcement Documentation**
**Duration**: {5-10} minutes
**Responsible**: Sistema executor
**Prerequisites**: Phase 3 🚨 CRITICAL implementation complete

**TodoWrite Update**: complete previous, mark "{phase_4_task_name}" as in_progress

**🚨 ENFORCEMENT Validation**:
- **🚨 BLOCKING Verification**: Sistema WILL validate {success_criteria} with ZERO tolerance
- **🚨 MANDATORY Documentation**: Sistema WILL record {evidence_requirements} with BLOCKING execution
- **🚨 AUTOMATIC Handoff**: Sistema WILL prepare {transition_requirements} with REQUIRED protocols

**Primary Actions**:
1. **🚨 ZERO TOLERANCE Validation**: {validation_description} with absolute priority enforcement
2. **🚨 REAL-TIME Documentation**: {documentation_description} with continuous monitoring and correction
3. **🚨 UNIVERSAL Handoff**: {handoff_description} with cross-domain application

**Quality Checks**:
- [ ] 🚨 BLOCKING: {checkpoint_1} with MANDATORY validation
- [ ] 🚨 AUTOMATIC: {checkpoint_2} with REQUIRED documentation
- [ ] 🚨 CRITICAL: {checkpoint_3} with MAXIMUM handoff preparation

**Success Criteria**: 🚨 MAXIMUM validation with REAL-TIME enforcement evidence

### Phase 5: **🚨 MANDATORY Routing Enforcement and Blocking Transitions**
**Duration**: {3-5} minutes
**Responsible**: Sistema executor
**Prerequisites**: Phase 4 🚨 MAXIMUM validation complete

**TodoWrite Update**: complete previous, mark "{phase_5_task_name}" as in_progress

**🚨 BLOCKING Command Routing**: AUTOMATIC next command determination with ZERO tolerance
- **🚨 CRITICAL Priority Calculation**: MANDATORY mathematical assessment of routing decisions
- **🚨 BLOCKING Handoff Protocol**: REQUIRED format "Next: /{command} (🚨{priority}) - {rationale}"
- **🚨 AUTOMATIC Integration**: Sistema WILL coordinate with /handoff-manager enforcement
- **🚨 MANDATORY Documentation**: BLOCKING execution without routing decision recording
- **🚨 REAL-TIME Monitoring**: Continuous validation of routing compliance and effectiveness

**Routing Format**: "Next: /{category}/{command} (🚨{high|medium|low}) - {enforcement_rationale}"

**TodoWrite Update**: complete all {command_name} tasks

**🚨 ENFORCEMENT Success**: Sistema WILL calculate routing with MAXIMUM priority and BLOCKING validation

**Success Criteria**: 🚨 MANDATORY routing with ZERO tolerance compliance
```

## Specialized Phase Variants

### 1. Documentation Progressive Disclosure Phase
```markdown
### Layer {number}: {layer_name} ({target_reading_time} minutes)

**Information Density**: {essential|detailed|advanced|expert} level
**Target Audience**: {audience_specification}
**Prerequisites**: {required_knowledge_or_completion}

**Core Content**:
- **Primary Concept**: {main_idea_in_one_sentence}
- **Key Points**: 
  - {point_1} - {actionable_detail}
  - {point_2} - {measurable_outcome}
  - {point_3} - {verification_method}

**Practical Actions**:
1. {action_1} → {expected_result}
2. {action_2} → {validation_criteria}
3. {action_3} → {success_indicator}

**Navigation**:
- **Previous Layer**: [Layer {n-1}](#layer-{n-1}-{name})
- **Next Layer**: [Layer {n+1}](#layer-{n+1}-{name})
- **Quick Reference**: [Essential Points](#quick-reference)

**Success Indicator**: {how_to_know_this_layer_is_understood}
```

### 2. Validation Testing Phase
```markdown
### Validation Phase {number}: {validation_type}

**Validation Scope**: {what_is_being_validated}
**Success Threshold**: {quantitative_success_criteria}
**Failure Response**: {what_happens_on_failure}

**Pre-Validation Setup**:
- {setup_requirement_1} with {verification_method}
- {setup_requirement_2} with {verification_method}

**Validation Execution**:
```bash
# {description_of_validation_commands}
{validation_command_1}
{validation_command_2}
{validation_command_3}
```

**Result Analysis**:
- **Metrics Collection**: {how_metrics_are_gathered}
- **Threshold Comparison**: {how_success_is_determined}
- **Trend Analysis**: {how_results_compare_to_historical_data}

**Success Criteria**:
- {metric_1}: {threshold_1} {operator} {value_1}
- {metric_2}: {threshold_2} {operator} {value_2}
- Overall: {combined_success_definition}

**Failure Handling**:
1. **Detection**: {how_failure_is_identified}
2. **Classification**: {failure_severity_determination}
3. **Response**: {immediate_actions_on_failure}
4. **Recovery**: {steps_to_remediate_failure}
```

### 3. Integration Orchestration Phase
```markdown
### Integration Phase {number}: {integration_type}

**Integration Scope**: 
- **System A**: {first_system} via {interface_type}
- **System B**: {second_system} via {interface_type}
- **Data Flow**: {direction_and_type_of_data}

**Pre-Integration Validation**:
- [ ] {system_a_readiness_check}
- [ ] {system_b_readiness_check}
- [ ] {interface_compatibility_verification}

**Integration Execution**:
```bash
# {description_of_integration_process}
{integration_command_1}  # {what_this_accomplishes}
{integration_command_2}  # {expected_outcome}
{integration_command_3}  # {verification_step}
```

**Data Flow Validation**:
- **Input Validation**: {how_input_data_is_verified}
- **Transformation Check**: {how_data_transformation_is_validated}
- **Output Verification**: {how_output_correctness_is_confirmed}

**Performance Monitoring**:
- **Latency**: ≤{value}ms for {percentage}% of operations
- **Throughput**: ≥{value} operations per second
- **Error Rate**: ≤{percentage}% acceptable failure rate

**Success Criteria**: {integration_success_definition}
```

## Phase Composition Patterns

### 1. Sequential Phase Chain
```markdown
## Sequential Execution Pattern
Phase 1 → Phase 2 → Phase 3 → Phase 4 → Phase 5

**Dependencies**: Each phase requires previous phase completion
**Rollback**: Failure at any phase triggers rollback to last stable state
**Progress Tracking**: TodoWrite updates at each phase transition
```

### 2. Parallel Phase Execution
```markdown
## Parallel Execution Pattern
Phase 1 → [Phase 2a | Phase 2b | Phase 2c] → Phase 3

**Coordination**: Central coordination for parallel phase management
**Synchronization**: All parallel phases must complete before progression
**Resource Management**: Resource allocation across parallel executions
```

### 3. Conditional Phase Routing
```markdown
## Conditional Execution Pattern
Phase 1 → Decision Point → [Phase 2a OR Phase 2b] → Phase 3

**Decision Criteria**: {conditions_for_path_selection}
**Path Selection**: {logic_for_choosing_execution_path}
**Convergence**: All paths converge at specified phase
```

## Usage Instructions

### 1. Template Selection
```markdown
# Choose appropriate phase structure based on command type:

## For Standard Commands:
@./docs/templates/shared/phase-structures.md#basic_5_phase_command_structure

## For P55/P56 Compliant Commands:
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure

## For Enforcement Commands:
@./docs/templates/shared/phase-structures.md#enforcement_phase_structure
```

### 2. Phase Customization
```markdown
# Replace template variables with command-specific content:
- {phase_name} → Actual phase name
- {duration} → Realistic time estimate
- {prerequisite_n} → Specific requirements
- {action_n} → Concrete actions with deliverables
- {checkpoint_n} → Measurable validation points
```

### 3. Phase Integration
```markdown
# Ensure consistent TodoWrite integration:
- Phase start: mark "{specific_task_name}" as in_progress
- Phase complete: complete previous, mark "{next_task_name}" as in_progress
- Command complete: complete all {command_name} tasks
```

---

**Structure Authority**: ce-simple phase standardization
**Usage**: All commands must use shared phase structures
**Customization**: Replace variables while maintaining structure
**Integration**: Automatic TodoWrite and routing protocol inclusion