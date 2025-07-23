# Template Composition Examples - Practical Usage Guide

## Purpose
Demonstrates practical usage of the template composition framework with real examples showing how to combine base templates, shared components, and mixins to create specific templates.

## Real-World Composition Examples

### 1. Creating a Basic Command Template

**Scenario**: Need a simple command without special compliance requirements

**Composition**:
```markdown
# /example-command - Basic Command Example

<!-- Base command structure -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block

## Purpose
Demonstrate basic command creation using shared components

<!-- Core principles -->
@./docs/templates/shared/metadata-schema.md#principles_and_guidelines

## Execution Process
<!-- Standard 5-phase structure -->
@./docs/templates/shared/phase-structures.md#basic_5_phase_command_structure

<!-- Standard error handling -->
@./docs/templates/shared/metadata-schema.md#error_handling_template

<!-- Cross-references -->
@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

**Result**: Clean, standard command with all essential components but no specialized features.

### 2. Creating a P55/P56 Compliant Command

**Scenario**: Need a command with mathematical validation and tool call compliance

**Composition**:
```markdown
# /math-analysis - P55/P56 Compliant Command Example

<!-- Base command structure -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block

## Purpose
Perform mathematical analysis with full P55/P56 compliance

<!-- P55/P56 compliance enhancement -->
@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin

## Execution Process
<!-- P55/P56 compliant phases -->
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure

<!-- Standard error handling -->
@./docs/templates/shared/metadata-schema.md#error_handling_template

<!-- Cross-references -->
@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

**Result**: Command with mathematical compliance, tool call integration, and precision requirements.

### 3. Creating an Enforcement Command

**Scenario**: Need a command with blocking mechanisms and mandatory compliance

**Composition**:
```markdown
# /security-enforce - Enforcement Command Example

<!-- Base command structure -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block

## **🚨 BLOCKING Security Enforcement Command**
**🚨 MANDATORY: Sistema WILL enforce security protocols with AUTOMATIC blocking**

## Purpose
🚨 BLOCKING: Sistema WILL enforce security compliance with ZERO tolerance

<!-- Enforcement enhancement -->
@./docs/templates/mixins/template-mixins.md#enforcement_framework_mixin

## Execution Process
<!-- Enforcement phases -->
@./docs/templates/shared/phase-structures.md#enforcement_phase_structure

<!-- Standard error handling -->
@./docs/templates/shared/metadata-schema.md#error_handling_template

<!-- Cross-references -->
@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

**Result**: Enforcement command with blocking mechanisms and mandatory compliance patterns.

### 4. Creating Progressive Disclosure Documentation

**Scenario**: Need documentation with layered information for complex topics

**Composition**:
```markdown
# Complex System Architecture

<!-- Base documentation structure -->
@./docs/templates/shared/metadata-schema.md#ownership_schema
@./docs/templates/shared/metadata-schema.md#versioning_schema

## Purpose
Explain complex system architecture using progressive disclosure

<!-- Progressive disclosure enhancement -->
@./docs/templates/mixins/template-mixins.md#progressive_disclosure_mixin

## Layer 1: Quick Start (2-3 minutes)

### Quick Summary
System provides distributed processing with automatic load balancing

### Key Points
- **Distributed**: Processes run across multiple nodes
- **Load Balanced**: Automatic work distribution
- **Fault Tolerant**: Continues operation despite failures

### Immediate Actions
1. Verify system status: `./status-check.sh`
2. Start basic processing: `./start-processing.sh`
3. Monitor operations: `./monitor.sh`

### Success Indicator
Processing dashboard shows green status with active nodes

---
*For detailed implementation → [Layer 2: Implementation Details](#layer-2-implementation-details)*

## Layer 2: Implementation Details (5-10 minutes)

### Prerequisites
- Kubernetes cluster with minimum 3 nodes
- Persistent storage available

### Step-by-Step Process
1. **Deploy Core Services**: Deploy system components to cluster
   - Expected outcome: All pods running and healthy
   - Troubleshooting: Check pod logs for startup errors

2. **Configure Load Balancer**: Set up traffic distribution
   - Expected outcome: Even load distribution across nodes
   - Troubleshooting: Verify service endpoints are accessible

### Validation Steps
- [ ] All services responding to health checks
- [ ] Load distribution within 10% variance

---
*For advanced configuration → [Layer 3: Advanced Details](#layer-3-advanced-details)*

<!-- Continue with additional layers as needed -->

<!-- Standard navigation -->
@./docs/templates/shared/metadata-schema.md#standard_navigation_pattern

<!-- Cross-references -->
@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/templates/shared/metadata-schema.md#document_status_schema
```

**Result**: Documentation with progressive information disclosure from basic to expert level.

### 5. Creating Integration-Focused Documentation

**Scenario**: Need documentation that emphasizes system integration patterns

**Composition**:
```markdown
# API Integration Guide

<!-- Base documentation structure -->
@./docs/templates/shared/metadata-schema.md#ownership_schema
@./docs/templates/shared/metadata-schema.md#versioning_schema

## Purpose
Guide for integrating with external APIs and systems

<!-- Integration patterns enhancement -->
@./docs/templates/mixins/template-mixins.md#integration_patterns_mixin

## System Integration Framework

### Integration Scope
- **System A**: Customer database via REST API
- **System B**: Payment processor via webhook
- **Data Flow**: Bidirectional - customer data and payment status

### Integration Points
1. **Customer Sync**: Synchronize customer records between systems
   - **Input**: Customer ID and profile data
   - **Output**: Sync confirmation and timestamp
   - **Validation**: Schema compliance and data integrity checks

2. **Payment Processing**: Handle payment events and updates
   - **Input**: Payment request with customer context
   - **Output**: Payment status and transaction ID
   - **Validation**: Amount verification and fraud checks

### Data Flow Validation
```bash
# Input validation
curl -X POST api/validate-customer -d @customer.json

# Data transformation
./transform-data.sh --input=customer.json --output=processed.json

# Output verification
./verify-output.sh --data=processed.json --schema=customer-schema.json
```

**Validation Criteria**:
- **Data Integrity**: 100% accuracy across system boundaries
- **Format Compliance**: Adherence to API schemas
- **Performance**: ≤200ms average processing time

<!-- Standard navigation and references -->
@./docs/templates/shared/metadata-schema.md#standard_navigation_pattern
@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/templates/shared/metadata-schema.md#document_status_schema
```

**Result**: Documentation focused on integration patterns with concrete examples and validation.

## Variable Substitution Examples

### 1. Command Template Variable Substitution

**Before (Template)**:
```markdown
### Phase 1: {phase_1_name}
**Duration**: {phase_1_duration}
**Prerequisites**: {phase_1_prerequisites}

**Primary Actions**:
1. {action_1} - {outcome_1}
2. {action_2} - {outcome_2}
```

**After (Substituted)**:
```markdown
### Phase 1: Data Analysis and Preparation
**Duration**: 10-15 minutes
**Prerequisites**: Clean dataset available, analysis tools configured

**Primary Actions**:
1. Load and validate dataset - Data quality report generated
2. Perform statistical analysis - Summary statistics calculated
```

### 2. Documentation Template Variable Substitution

**Before (Template)**:
```markdown
## Layer 1: Quick Start ({target_reading_time_l1} minutes)

### Key Points
- **{point_1}**: {detail_1}
- **{point_2}**: {detail_2}
```

**After (Substituted)**:
```markdown
## Layer 1: Quick Start (3-5 minutes)

### Key Points
- **Authentication**: API requires Bearer token in Authorization header
- **Rate Limiting**: Maximum 1000 requests per hour per API key
```

## Mixin Combination Examples

### 1. P55/P56 + Integration Patterns

**Use Case**: Command that needs mathematical compliance AND system integration

```markdown
# /system-sync - P55/P56 Compliant Integration Command

@./docs/templates/shared/metadata-schema.md#command_metadata_block

## Purpose
Synchronize systems with mathematical validation and integration monitoring

<!-- Combine P55/P56 compliance with integration patterns -->
@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin
@./docs/templates/mixins/template-mixins.md#integration_patterns_mixin

## Execution Process
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure

<!-- Integration phases added to standard P55/P56 phases -->
@./docs/templates/shared/phase-structures.md#integration_orchestration_phase

@./docs/templates/shared/metadata-schema.md#error_handling_template
@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

**Result**: Command with both mathematical compliance and integration capabilities.

### 2. Progressive Disclosure + Performance Monitoring

**Use Case**: Documentation that explains performance concepts with layered complexity

```markdown
# Performance Optimization Guide

@./docs/templates/shared/metadata-schema.md#ownership_schema
@./docs/templates/shared/metadata-schema.md#versioning_schema

## Purpose
Comprehensive performance optimization with progressive complexity

<!-- Combine progressive disclosure with performance monitoring -->
@./docs/templates/mixins/template-mixins.md#progressive_disclosure_mixin
@./docs/templates/mixins/template-mixins.md#performance_monitoring_mixin

<!-- Layer 1: Basic performance concepts -->
## Layer 1: Performance Basics (3-5 minutes)

### Performance Baseline Establishment
```bash
# Simple performance baseline
./performance/baseline.sh --quick --duration=60
```

**Baseline Metrics**:
- **Response Time**: Current average response time
- **Throughput**: Current operations per second

<!-- Layer 2: Detailed monitoring -->
## Layer 2: Advanced Monitoring (10-15 minutes)

### Real-time Performance Monitoring
```bash
# Comprehensive monitoring with alerts
./performance/monitor.sh --metrics=all --alerts=true --frequency=30s
```

@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/templates/shared/metadata-schema.md#document_status_schema
```

**Result**: Documentation that explains performance from basic to advanced with monitoring integration.

## Anti-Patterns and Common Mistakes

### 1. Over-Composition Anti-Pattern

**❌ Wrong**:
```markdown
# Over-composed command with too many mixins

@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin
@./docs/templates/mixins/template-mixins.md#enforcement_framework_mixin
@./docs/templates/mixins/template-mixins.md#progressive_disclosure_mixin
@./docs/templates/mixins/template-mixins.md#integration_patterns_mixin
@./docs/templates/mixins/template-mixins.md#performance_monitoring_mixin
```

**❌ Problem**: Too many mixins create complexity and potential conflicts

**✅ Correct**:
```markdown
# Focused command with appropriate mixins

@./docs/templates/shared/metadata-schema.md#command_metadata_block
@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure
```

**✅ Solution**: Use only necessary mixins for specific requirements

### 2. Missing Base Template Anti-Pattern

**❌ Wrong**:
```markdown
# Template with mixins but no base

@./docs/templates/mixins/template-mixins.md#enforcement_framework_mixin
@./docs/templates/shared/phase-structures.md#enforcement_phase_structure
```

**❌ Problem**: No foundational structure, missing essential components

**✅ Correct**:
```markdown
# Proper template with base + mixins

@./docs/templates/shared/metadata-schema.md#command_metadata_block
@./docs/templates/mixins/template-mixins.md#enforcement_framework_mixin
@./docs/templates/shared/phase-structures.md#enforcement_phase_structure
```

**✅ Solution**: Always start with appropriate base template

### 3. Incompatible Mixin Combination Anti-Pattern

**❌ Wrong**:
```markdown
# Incompatible mixins combined

@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin
@./docs/templates/mixins/template-mixins.md#enforcement_framework_mixin
```

**❌ Problem**: P55/P56 and enforcement have different compliance paradigms

**✅ Correct**:
```markdown
# Choose one compliance approach

@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin
@./docs/templates/mixins/template-mixins.md#integration_patterns_mixin
```

**✅ Solution**: Check compatibility matrix before combining mixins

## Validation and Testing

### 1. Template Composition Validation

```bash
# Validate template composition
./scripts/templates/validate-composition.sh \
  --base=command-base \
  --mixins=p55-p56-compliance,integration-patterns \
  --output=validation-report.json

# Check results
if [[ $? -eq 0 ]]; then
  echo "✅ Template composition valid"
else
  echo "❌ Template composition has issues"
  cat validation-report.json
fi
```

### 2. Variable Substitution Testing

```bash
# Test variable substitution
./scripts/templates/test-substitution.sh \
  --template=example-command.md \
  --variables=test-variables.json \
  --output=generated-command.md

# Verify no placeholder variables remain
if grep -q '{[^}]*}' generated-command.md; then
  echo "❌ Unsubstituted variables found"
  grep '{[^}]*}' generated-command.md
else
  echo "✅ All variables substituted correctly"
fi
```

### 3. Integration Testing

```bash
# Test complete template functionality
./scripts/templates/integration-test.sh \
  --template=generated-command.md \
  --test-scenarios=basic,error-handling,performance

# Results
echo "Integration test results:"
echo "- Basic functionality: PASS"
echo "- Error handling: PASS"
echo "- Performance: PASS"
```

## Best Practices Summary

### 1. Composition Guidelines
- **Start Simple**: Begin with base template, add mixins only as needed
- **Check Compatibility**: Verify mixin combinations before use
- **Test Early**: Validate composition before variable substitution
- **Document Rationale**: Explain why specific mixins were chosen

### 2. Variable Management
- **Use Descriptive Names**: Variables should be self-explaining
- **Provide Examples**: Show expected variable values
- **Validate Substitution**: Ensure all variables are replaced
- **Maintain Consistency**: Use consistent naming patterns

### 3. Quality Assurance
- **Regular Validation**: Run composition validation regularly
- **Version Tracking**: Track template versions and dependencies
- **Performance Testing**: Test template generation performance
- **User Feedback**: Collect feedback on template usability

---

**Framework Authority**: ce-simple template composition system
**Usage Examples**: Practical demonstrations of composition patterns
**Maintenance**: Updated with new examples as patterns emerge
**Evolution**: Examples evolve based on real usage and user feedback