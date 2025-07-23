# Shared Metadata Schema - Template Composition Framework

## Purpose
Eliminates DRY violations by providing reusable metadata patterns, status definitions, and ownership structures for all ce-simple templates.

## Core Metadata Components

### 1. Document Status Schema
```yaml
# Standard document status patterns
status_definitions:
  draft: "Initial creation, work in progress"
  review: "Complete draft ready for stakeholder review"
  approved: "Reviewed and approved for implementation"
  active: "Currently in use and maintained"
  deprecated: "Superseded but maintained for compatibility"
  archived: "No longer maintained, preserved for reference"
```

### 2. Ownership Schema
```yaml
# Standard ownership and responsibility patterns
ownership_schema:
  owner: "Primary responsible party for content accuracy and maintenance"
  contributors: "Additional parties who contributed to content creation"
  reviewers: "Parties responsible for quality assurance and approval"
  stakeholders: "Parties affected by or interested in the content"
  maintainer: "Party responsible for ongoing updates and currency"
```

### 3. Versioning Schema
```yaml
# Standard versioning patterns
versioning_schema:
  version: "Semantic version (X.Y.Z format)"
  last_updated: "ISO 8601 timestamp of last modification"
  created_date: "ISO 8601 timestamp of initial creation"
  next_review: "ISO 8601 timestamp of scheduled review"
  review_frequency: "Frequency of mandatory reviews (monthly/quarterly/annually)"
```

### 4. Cross-Reference Schema
```yaml
# Standard cross-reference patterns
cross_reference_schema:
  prerequisites: "Required knowledge or resources before using this content"
  dependencies: "Other documents or systems this content relies on"
  related_docs: "Contextually related but not dependent documents"
  see_also: "Additional resources for deeper understanding"
  integrations: "System components this content integrates with"
```

## Phase Structure Components

### 1. Standard Phase Header
```markdown
### Phase {number}: {phase_name}
**Duration**: {time_estimate}
**Responsible**: {role_or_person}
**Prerequisites**: 
- {prerequisite_1}
- {prerequisite_2}

**TodoWrite Update**: {phase_transition_instruction}
```

### 2. Phase Actions Template
```markdown
**Primary Actions**:
1. {action_1} - {expected_outcome}
2. {action_2} - {validation_criteria}
3. {action_3} - {deliverable_specification}

**Quality Checks**:
- [ ] {checkpoint_1}
- [ ] {checkpoint_2}
- [ ] {checkpoint_3}

**Success Criteria**: {measurable_success_definition}
```

### 3. Phase Routing Template
```markdown
**Phase Completion**:
- **Deliverables**: {concrete_outputs}
- **Next Phase Trigger**: {condition_for_progression}
- **Rollback Criteria**: {conditions_requiring_rollback}
- **Documentation**: {required_documentation_updates}
```

## Command-Specific Components

### 1. Command Metadata Block
```markdown
---
**Command**: /{command_name}
**Category**: {category_number}-{category_name}
**Purpose**: {single_sentence_purpose}
**Complexity**: {low|medium|high}
**Execution Time**: {estimated_duration}
**Prerequisites**: {required_conditions}
**Outputs**: {expected_deliverables}
**Integration**: {system_touchpoints}
---
```

### 2. TodoWrite Integration Pattern
```markdown
## TodoWrite Integration
**Pattern**: Standard 5-phase TodoWrite orchestration
**Updates**: Automatic phase transitions with status tracking
**Format**: 
- Phase start: `mark "{task_name}" as in_progress`
- Phase complete: `complete previous, mark "{next_task}" as in_progress`
- Command complete: `complete all {command_name} tasks`
```

### 3. Error Handling Template
```markdown
## Error Handling Protocol
**Detection**: {error_identification_method}
**Classification**: 
- Critical: {immediate_halt_required}
- Major: {corrective_action_required}
- Minor: {documentation_and_monitoring}

**Response Procedures**:
1. **Immediate**: {first_response_action}
2. **Analysis**: {root_cause_investigation}
3. **Resolution**: {corrective_action_plan}
4. **Prevention**: {future_prevention_measures}
```

## Documentation Components

### 1. Progressive Disclosure Structure
```markdown
## Layer 1: Quick Start ({target_reading_time} minutes)
{essential_information_only}

## Layer 2: Implementation Details ({target_reading_time} minutes)  
{step_by_step_procedures}

## Layer 3: Advanced Configuration ({target_reading_time} minutes)
{customization_and_optimization}

## Layer 4: Architecture Details ({target_reading_time} minutes)
{technical_deep_dive}

## Layer 5: Expert Troubleshooting ({target_reading_time} minutes)
{diagnostic_and_recovery}
```

### 2. Standard Navigation Pattern
```markdown
---
*Quick Navigation*:
- **Prerequisites** → [Layer 1: Quick Start](#layer-1-quick-start)
- **Implementation** → [Layer 2: Details](#layer-2-implementation-details)  
- **Customization** → [Layer 3: Advanced](#layer-3-advanced-configuration)
- **Architecture** → [Layer 4: Technical](#layer-4-architecture-details)
- **Troubleshooting** → [Layer 5: Expert](#layer-5-expert-troubleshooting)
---
```

### 3. Code Block Standards
```markdown
## Code Block Template
```{language}
# {description_of_what_code_does}
{code_content}

# Expected output:
{expected_result_description}
```

**Verification**: {how_to_verify_code_worked}
**Troubleshooting**: {common_issues_and_solutions}
```

## Validation Components

### 1. Success Metrics Template
```markdown
## Success Metrics
- **Primary Metric**: {metric_name} {operator} {threshold} {unit}
- **Secondary Metrics**: 
  - {metric_2}: {threshold_2}
  - {metric_3}: {threshold_3}
- **Overall Success**: {combined_success_criteria}
```

### 2. Compliance Framework
```markdown
## Compliance Framework
**Standards Adherence**:
- {standard_1}: {compliance_level} compliance required
- {standard_2}: {compliance_level} compliance required

**Validation Methods**:
- Automated: {automated_check_description}
- Manual: {manual_review_requirements}
- Continuous: {ongoing_monitoring_approach}
```

### 3. Performance Benchmarks
```markdown
## Performance Benchmarks
**Response Time**: ≤{value}ms for {percentage}% of operations
**Throughput**: ≥{value} operations per second under normal load
**Resource Usage**: ≤{percentage}% {resource_type} utilization
**Scalability**: Linear performance up to {scale_factor}x normal load
```

## Integration Patterns

### 1. System Integration Template
```markdown
## System Integration
**Integration Points**:
- {system_1} ↔ {system_2}: {interface_type} - {data_flow_description}
- {system_2} ↔ {system_3}: {interface_type} - {data_flow_description}

**Data Flow Validation**:
- Input validation: {validation_rules}
- Transformation verification: {transformation_checks}
- Output validation: {output_verification}
```

### 2. Command Routing Pattern
```markdown
## Command Routing Protocol
**Analysis Framework**:
1. **Context Assessment**: {evaluation_criteria}
2. **Priority Calculation**: {mathematical_assessment}
3. **Routing Decision**: {selection_logic}

**Format**: "Next: /{category}/{command} ({priority}) - {rationale}"
**Integration**: Coordinates with /handoff-manager and /notify-manager
```

## Usage Examples

### Template Composition Example
```markdown
# Example: Using Shared Components

## Import Metadata Schema
@./docs/templates/shared/metadata-schema.md#document_status_schema
@./docs/templates/shared/metadata-schema.md#ownership_schema

## Apply Standard Phase Structure  
@./docs/templates/shared/phase-structures.md#standard_5_phase_template

## Include Validation Components
@./docs/templates/shared/metadata-schema.md#success_metrics_template
```

### Mixin Usage Pattern
```markdown
# Example: Command Template with Mixins

<!-- Base command structure -->
@./docs/templates/shared/command-base.md

<!-- Add P55/P56 compliance -->
@./docs/templates/mixins/p55-p56-compliance.md

<!-- Add enforcement capabilities -->
@./docs/templates/mixins/enforcement-framework.md
```

## Template Versioning

### Version Control Schema
```yaml
template_versioning:
  schema_version: "1.0.0"
  compatibility: 
    minimum_version: "0.9.0"
    breaking_changes: []
  changelog:
    - version: "1.0.0"
      date: "2025-07-23"
      changes: ["Initial shared schema creation"]
```

### Migration Support
```markdown
## Template Migration
**Backward Compatibility**: Maintained for 2 major versions
**Migration Path**: Automated conversion tools available
**Deprecation Notice**: 30-day notice before breaking changes
```

---

**Schema Authority**: ce-simple template system
**Usage**: All templates must inherit from shared components
**Maintenance**: Weekly review for component optimization
**Integration**: Automatic inclusion in all new templates