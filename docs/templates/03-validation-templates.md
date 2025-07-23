# Validation Templates - Unified Template System

@./docs/templates/shared/metadata-schema.md#document_status_schema
@./docs/templates/shared/template-versioning.md#version_declaration_format

## Purpose
Consolidated validation templates using shared component system to eliminate DRY violations and promote modular, reusable validation patterns.

**Template Evolution**: Now leverages shared components and mixins for maximum reusability and maintainability.

## Template Categories

### 1. System Validation Template
```markdown
# [System/Component Name] Validation

@./docs/templates/shared/metadata-schema.md#ownership_schema
@./docs/templates/shared/metadata-schema.md#versioning_schema

## Purpose
[What this validation ensures or verifies]

## Scope
- **Target**: [What is being validated]
- **Coverage**: [Percentage or scope of validation]
- **Frequency**: [How often validation occurs]

@./docs/templates/shared/metadata-schema.md#success_metrics_template

## Validation Process
@./docs/templates/shared/phase-structures.md#validation_testing_phase

@./docs/templates/shared/metadata-schema.md#code_block_standards

---
@./docs/templates/shared/metadata-schema.md#document_status_schema
```

### 2. Compliance Validation Template
```markdown
# [Standard/Requirement Name] Compliance Validation

@./docs/templates/shared/metadata-schema.md#ownership_schema
@./docs/templates/shared/metadata-schema.md#versioning_schema

## Purpose
Verify adherence to [specific standard/requirement] with automated checking and reporting

@./docs/templates/shared/metadata-schema.md#compliance_framework

@./docs/templates/shared/phase-structures.md#validation_testing_phase

@./docs/templates/shared/metadata-schema.md#code_block_standards

---
@./docs/templates/shared/metadata-schema.md#document_status_schema
```

### 3. Performance Validation Template
```markdown
# [System/Component Name] Performance Validation

## Purpose
Ensure [system/component] performance meets established benchmarks and user requirements

## Performance Areas
- **Response Time**: [Time-based performance metrics and thresholds]
- **Throughput**: [Volume-based performance metrics and capacity]
- **Resource Utilization**: [Resource efficiency metrics and limits]
- **Scalability**: [Scale-related performance metrics and boundaries]

## Benchmarking Protocol

### Phase 1: Baseline Establishment
```bash
# Establish performance baseline
./scripts/performance/baseline.sh --component=[name] --duration=300 --samples=100

# Document baseline metrics
./scripts/performance/document-baseline.sh --output=performance/baselines/
```

### Phase 2: Load Testing Execution
```bash
# Execute load testing scenarios
./scripts/performance/load-test.sh --scenario=normal --duration=600
./scripts/performance/load-test.sh --scenario=peak --duration=300
./scripts/performance/load-test.sh --scenario=stress --duration=180
```

### Phase 3: Performance Measurement
- **Response Time Measurement**: [Methodology and tools]
- **Throughput Analysis**: [Calculation methods and validation]
- **Resource Monitoring**: [Metrics collection and analysis]
- **Scalability Assessment**: [Testing approach and evaluation]

### Phase 4: Benchmark Comparison
- **Current vs Baseline**: [Comparison methodology]
- **Trend Analysis**: [Historical performance evaluation]
- **Threshold Validation**: [Success criteria verification]
- **Improvement Identification**: [Optimization opportunity analysis]

## Performance Thresholds
- **Response time**: ≤[value]ms for [percentage]% of requests
- **Throughput**: ≥[value] operations per second under normal load
- **CPU utilization**: ≤[percentage]% average usage during peak load  
- **Memory utilization**: ≤[percentage]% peak usage with [safety margin]
- **Scalability**: Linear performance up to [scale factor]x normal load

## Performance Issue Response
### Degradation Detection
```bash
# Automated performance monitoring
./scripts/performance/monitor.sh --threshold-response=[ms] --threshold-cpu=[%]

# Alert generation for threshold violations
./scripts/alerts/performance-alert.sh --severity=[level] --component=[name]
```

### Optimization Procedures
1. **Issue Identification**: [Performance bottleneck analysis methodology]
2. **Root Cause Analysis**: [Investigation steps and diagnostic tools]
3. **Optimization Implementation**: [Performance improvement procedures]
4. **Validation Testing**: [Verification of optimization effectiveness]

---

**Performance Standard**: [Benchmark specification]
**Monitoring Frequency**: [Real-time/scheduled]
**SLA Commitment**: [Performance guarantees]
```

### 4. Integration Validation Template
```markdown
# [Integration Name] Validation Framework

## Purpose
Validate integration points, data flow, and system interoperability

## Integration Scope
- **System A**: [First system in integration with interface details]
- **System B**: [Second system in integration with interface details]
- **Data Flow**: [Direction and type of data exchange]
- **Interface Type**: [API, file transfer, database, etc.]

## Validation Scenarios

### Scenario 1: Normal Operation Validation
```bash
# Test normal data flow
./scripts/integration/test-normal-flow.sh --from=[system-a] --to=[system-b]

# Verify data integrity
./scripts/integration/verify-data.sh --source=[data-source] --target=[data-target]
```

**Expected Results**:
- Data transfer completion: 100% success rate
- Data integrity: 100% accuracy
- Response time: ≤[value]ms average

### Scenario 2: Error Condition Validation
```bash
# Test error handling
./scripts/integration/test-error-conditions.sh --scenario=[error-type]

# Verify recovery procedures
./scripts/integration/test-recovery.sh --error=[condition] --recovery=[method]
```

**Expected Results**:
- Error detection: 100% coverage
- Error handling: Graceful degradation
- Recovery time: ≤[value] seconds

### Scenario 3: Load Condition Validation
```bash
# Test under load conditions
./scripts/integration/load-test-integration.sh --load=[multiplier] --duration=[seconds]

# Monitor integration performance
./scripts/integration/monitor-load.sh --metrics=all --alert-threshold=[value]
```

**Expected Results**:
- Load handling: No degradation up to [load level]
- Performance maintenance: ≤[degradation]% under peak load
- Resource utilization: Within normal operating parameters

## Interface Validation
### API Integration Validation
```bash
# API endpoint testing
curl -X GET "[api-endpoint]" -H "Authorization: Bearer [token]" | jq '.'

# API response validation
./scripts/integration/validate-api-response.sh --endpoint=[url] --schema=[file]
```

### Data Validation
```bash
# Schema validation
./scripts/integration/validate-schema.sh --source=[data] --schema=[definition]

# Data transformation validation  
./scripts/integration/validate-transform.sh --input=[source] --output=[target] --rules=[file]
```

## Continuous Integration Validation
```bash
# Automated integration testing
./scripts/ci/integration-test-suite.sh --environment=[test/staging/prod]

# Integration health monitoring
./scripts/monitoring/integration-health.sh --all-interfaces --report-interval=300
```

## Integration Failure Response
1. **Immediate Isolation**: Prevent cascade failures
2. **Failover Activation**: Switch to backup systems if available
3. **Stakeholder Notification**: Alert affected teams within 5 minutes
4. **Investigation**: Root cause analysis and resolution planning
5. **Recovery Validation**: Verify system restoration before resuming operations

---

**Integration Owner**: [Responsible team]
**Monitoring**: [Continuous/scheduled]
**SLA**: [Availability and performance commitments]
```

## Implementation Guidelines

@./docs/templates/shared/composition-framework.md#template_creation_process

### Choosing the Right Template
1. **System Validation**: Use validation-base + performance monitoring mixin
2. **Compliance Validation**: Use validation-base + P55/P56 compliance mixin
3. **Performance Validation**: Use validation-base + performance monitoring mixin
4. **Integration Validation**: Use validation-base + integration patterns mixin

### Template Composition Process
```markdown
# Example: Creating Compliance Validation Template

<!-- Base structure -->
@./docs/templates/shared/validation-base.md

<!-- Add compliance capabilities -->
@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin

<!-- Use validation phases -->
@./docs/templates/shared/phase-structures.md#validation_testing_phase
```

@./docs/templates/shared/composition-framework.md#validation_design_principles
@./docs/templates/shared/composition-framework.md#quality_standards

## Cross-References
- [Shared Components](./shared/) - Core template building blocks
- [Template Mixins](./mixins/template-mixins.md) - Composable feature enhancements
- [Command Templates](./01-command-templates.md) - For validation command structure
- [Documentation Templates](./02-documentation-templates.md) - For validation documentation
- [Composition Framework](./shared/composition-framework.md) - Template assembly guidelines

---

@./docs/templates/shared/metadata-schema.md#document_status_schema

**Template Category**: Validation and testing templates
**Evolution**: DRY violations eliminated through shared component system
**Composition**: Base templates + mixins + shared components = modular validation
**Usage**: All validation activities in ce-simple system
**Authority**: Unified validation template system with composition framework