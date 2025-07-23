# Template Composition Framework - Modular Template System

## Purpose
Implements composition over inheritance principles for ce-simple templates, enabling modular template construction through mixins and shared components while eliminating DRY violations.

## Core Composition Principles

### 1. Component-Based Architecture
```markdown
# Template = Base + Components + Mixins + Variants
Template Structure:
├── Base Template (core structure)
├── Shared Components (reusable elements)
├── Mixins (optional features)
└── Variants (specialization patterns)
```

### 2. Inheritance Hierarchy
```yaml
template_hierarchy:
  base_templates:
    - command-base.md          # Core command structure
    - documentation-base.md    # Core documentation structure  
    - validation-base.md       # Core validation structure
  
  shared_components:
    - metadata-schema.md       # Common metadata patterns
    - phase-structures.md      # Reusable phase templates
    - navigation-patterns.md   # Standard navigation elements
  
  mixins:
    - p55-p56-compliance.md    # P55/P56 mathematical compliance
    - enforcement-framework.md # Enforcement capabilities
    - progressive-disclosure.md # Layered information presentation
    - integration-patterns.md  # System integration capabilities
  
  variants:
    - basic-variant.md         # Standard functionality
    - compliant-variant.md     # Compliance-focused
    - enforcement-variant.md   # Enforcement-focused
```

## Base Templates

### 1. Command Base Template
```markdown
# {command_name} - Base Command Structure

@./docs/templates/shared/metadata-schema.md#command_metadata_block

## Purpose
{single_sentence_purpose}

@./docs/templates/shared/metadata-schema.md#principles_and_guidelines

@./docs/templates/shared/phase-structures.md#basic_5_phase_command_structure

@./docs/templates/shared/metadata-schema.md#error_handling_template

@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

### 2. Documentation Base Template
```markdown
# {document_title} - Base Documentation Structure

@./docs/templates/shared/metadata-schema.md#document_status_schema
@./docs/templates/shared/metadata-schema.md#ownership_schema

## Purpose
{document_purpose}

## Overview
{high_level_context}

@./docs/templates/shared/metadata-schema.md#standard_navigation_pattern

{main_content_sections}

@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
{footer_metadata}
```

### 3. Validation Base Template  
```markdown
# {validation_name} - Base Validation Structure

@./docs/templates/shared/metadata-schema.md#ownership_schema
@./docs/templates/shared/metadata-schema.md#versioning_schema

## Purpose
{validation_purpose}

## Scope
{validation_scope}

@./docs/templates/shared/metadata-schema.md#success_metrics_template

{validation_phases}

@./docs/templates/shared/metadata-schema.md#performance_benchmarks

---
{validation_footer}
```

## Mixin System

### 1. P55/P56 Compliance Mixin
```markdown
# P55/P56 Compliance Enhancement Mixin

## 🛡️ P55/P56 Compliance Framework
**Inherits from**: Universal P55/P56 compliance standards

### Tool Call Execution Protocol
**MANDATORY**: This command executes:
- Real tool calls (never simulation)
- Mathematical calculations via script execution
- Visual announcements before each tool execution
- Complete transparency of all operations
- Evidence trail maintenance for compliance verification

### Mathematical Integration Pattern
```bash
# Load script foundation
source scripts/core/path-helper.sh
source scripts/formulas/context_engineering_formulas.sh

# Execute calculations with ≥4 decimal precision
confidence_score=$(calculate_confidence $param1 $param2 $param3)
threshold_compliance=$(calculate_threshold_compliance $score $threshold "gte")

# Validate P55/P56 compliance
echo "P55_COMPLIANCE: $(tool_calls_executed)/$(required_tool_calls) = 100%"
echo "P56_TRANSPARENCY: All operations visible with mathematical precision"
```

### Success Metrics Enhancement
- **P55 Compliance**: 100% tool call execution (0% simulation)
- **P56 Transparency**: ≥95% execution visibility
- **Mathematical Precision**: ≥4 decimal places accuracy
- **Performance**: ≤2.0s execution time

### Phase Integration Points
- **Phase 1**: Script foundation loading and compliance initialization
- **Phase 2**: Mathematical validation with tool call integration
- **Phase 3**: Compliance verification throughout implementation
- **Phase 4**: Transparent reporting with mathematical evidence
- **Phase 5**: Mathematical routing with precision calculations
```

### 2. Enforcement Framework Mixin
```markdown
# Enforcement Framework Enhancement Mixin

## 🚨 ENFORCEMENT MECHANISMS

### **🚨 MANDATORY Execution Requirements**
- 🚨 REQUIRED: {Function} with AUTOMATIC {enforcement mechanism}
- 🚨 BLOCKING: {Function} with real-time {monitoring/detection}  
- 🚨 CRITICAL: {Function} with immediate {correction/activation}

### **🚨 ERROR PROTOCOL ENFORCEMENT**
**🚨 ZERO TOLERANCE Error Enforcement**:
- **🚨 CRITICAL Error Detection**: IMMEDIATE activation of 8-step resolution protocol
- **🚨 BLOCKING Continuation**: NO execution continues without protocol completion
- **🚨 MANDATORY Protocol Steps**: Steps 1-4 AUTOMATIC, Steps 5-8 MANUAL with verification

### Enforcement Validation Standards
- **Sistema WILL/MUST patterns**: ≥3 per command
- **🚨 enforcement symbols**: ≥5 per command  
- **BLOCKING/MANDATORY designations**: ≥70% coverage
- **Real-time monitoring**: ≥2 specifications per command

### Phase Enhancement Pattern
- **Phase Headers**: 🚨 MANDATORY/BLOCKING/CRITICAL designations
- **Action Items**: 🚨 enforcement symbols with specific mechanisms
- **Quality Checks**: 🚨 validation requirements with tolerance levels
- **Success Criteria**: 🚨 MAXIMUM/ZERO TOLERANCE specifications
```

### 3. Progressive Disclosure Mixin
```markdown
# Progressive Disclosure Enhancement Mixin

## Layer-Based Information Architecture

### Layer Structure Template
@./docs/templates/shared/phase-structures.md#documentation_progressive_disclosure_phase

### Layer Integration Guidelines
- **Layer 1**: ≤200 words, 3-5 key points maximum, {target_reading_time} minutes
- **Layer 2**: Detailed implementation, practical focus, step-by-step procedures
- **Layer 3**: Configuration and customization options, advanced features
- **Layer 4**: Architecture and theoretical background, expert-level details
- **Layer 5**: Deep diagnostic and troubleshooting, recovery procedures

### Navigation Enhancement
```markdown
---
*Progressive Navigation*:
- **Quick Start** → [Layer 1: Essentials](#layer-1-essentials)
- **Implementation** → [Layer 2: Details](#layer-2-implementation-details)  
- **Advanced** → [Layer 3: Configuration](#layer-3-advanced-configuration)
- **Architecture** → [Layer 4: Technical](#layer-4-architecture-details)
- **Expert** → [Layer 5: Troubleshooting](#layer-5-expert-troubleshooting)
---
```

### Content Density Standards
- **Information Density**: ≥95% executable value per word
- **Cognitive Load**: ≤3 steps to any information
- **Comprehension**: ≥90% for target audience
- **Navigation Efficiency**: ≤2 clicks to relevant content
```

### 4. Integration Patterns Mixin
```markdown
# Integration Patterns Enhancement Mixin

## System Integration Framework

### Integration Types
- **Command-to-Command**: Routing and handoff protocols
- **System-to-System**: External system communication patterns
- **Data-to-Process**: Information flow and transformation patterns
- **Tool-to-Execution**: Tool call integration and orchestration

### Standard Integration Pattern
@./docs/templates/shared/metadata-schema.md#system_integration_template
@./docs/templates/shared/metadata-schema.md#command_routing_pattern

### Integration Validation
@./docs/templates/shared/phase-structures.md#integration_orchestration_phase

### Performance Standards
- **Integration Latency**: ≤{value}ms for {percentage}% of operations
- **Data Integrity**: 100% accuracy across system boundaries
- **Error Handling**: Graceful degradation with automatic recovery
- **Monitoring**: Real-time integration health tracking
```

## Composition Patterns

### 1. Basic Command Composition
```markdown
# Example: Standard Command Template

<!-- Base structure -->
@./docs/templates/shared/command-base.md

<!-- Standard phases -->
@./docs/templates/shared/phase-structures.md#basic_5_phase_command_structure

<!-- Standard metadata -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block
@./docs/templates/shared/metadata-schema.md#error_handling_template

Result: Clean, standard command with all essential components
```

### 2. Compliant Command Composition
```markdown
# Example: P55/P56 Compliant Command Template

<!-- Base structure -->
@./docs/templates/shared/command-base.md

<!-- P55/P56 compliance enhancement -->
@./docs/templates/mixins/p55-p56-compliance.md

<!-- Compliant phases -->
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure

<!-- Mathematical integration -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block

Result: Mathematically compliant command with tool call integration
```

### 3. Enforcement Command Composition
```markdown
# Example: Enforcement Command Template

<!-- Base structure -->
@./docs/templates/shared/command-base.md

<!-- Enforcement enhancement -->
@./docs/templates/mixins/enforcement-framework.md

<!-- Enforcement phases -->
@./docs/templates/shared/phase-structures.md#enforcement_phase_structure

<!-- Enforcement metadata -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block

Result: Enforcement command with blocking mechanisms and mandatory compliance
```

### 4. Progressive Documentation Composition
```markdown
# Example: Progressive Disclosure Documentation

<!-- Base documentation structure -->
@./docs/templates/shared/documentation-base.md

<!-- Progressive disclosure enhancement -->
@./docs/templates/mixins/progressive-disclosure.md

<!-- Layer-based phases -->
@./docs/templates/shared/phase-structures.md#documentation_progressive_disclosure_phase

<!-- Navigation enhancement -->
@./docs/templates/shared/metadata-schema.md#standard_navigation_pattern

Result: Layered documentation with progressive information disclosure
```

## Template Versioning System

### 1. Semantic Versioning
```yaml
template_versioning:
  major: 1    # Breaking changes to composition framework
  minor: 0    # New mixins or components added
  patch: 0    # Bug fixes or minor improvements
  
  compatibility_matrix:
    base_templates: "1.0.0"
    shared_components: "1.0.0" 
    mixins: "1.0.0"
    variants: "1.0.0"
```

### 2. Component Compatibility
```yaml
compatibility_rules:
  base_with_mixins:
    command-base: [p55-p56-compliance, enforcement-framework, integration-patterns]
    documentation-base: [progressive-disclosure, integration-patterns]
    validation-base: [p55-p56-compliance, enforcement-framework]
  
  mixin_combinations:
    compatible:
      - [p55-p56-compliance, integration-patterns]
      - [enforcement-framework, integration-patterns]
    incompatible:
      - [p55-p56-compliance, enforcement-framework]  # Different compliance paradigms
```

### 3. Migration Paths
```markdown
## Template Migration Support

### Automated Migration
```bash
# Migrate templates to new composition framework
./scripts/templates/migrate-to-composition.sh --version=1.0.0 --backup=true

# Validate composition compatibility
./scripts/templates/validate-composition.sh --template={template_name}
```

### Manual Migration Steps
1. **Identify Current Pattern**: Analyze existing template structure
2. **Select Base Template**: Choose appropriate base from framework
3. **Add Required Mixins**: Include necessary feature enhancements
4. **Validate Composition**: Ensure component compatibility
5. **Test Integration**: Verify template functionality
```

## Usage Guidelines

### 1. Template Creation Process
```markdown
## Step-by-Step Template Creation

1. **Select Base Template**
   - Choose from: command-base, documentation-base, validation-base
   
2. **Identify Required Features**
   - Compliance needs: P55/P56 mathematical compliance
   - Enforcement needs: Blocking mechanisms and mandatory operations
   - Presentation needs: Progressive disclosure layers
   - Integration needs: System interconnection patterns

3. **Add Appropriate Mixins**
   - Include only necessary mixins to avoid complexity
   - Verify mixin compatibility using compatibility matrix
   
4. **Customize Variables**
   - Replace all {variable} placeholders with specific content
   - Maintain structural consistency with base template
   
5. **Validate Composition**
   - Run composition validation tools
   - Test template functionality with realistic content
```

### 2. Best Practices
```markdown
## Template Composition Best Practices

### Favor Composition Over Inheritance
- Use mixins for optional features rather than template variants
- Combine small, focused components rather than large monolithic templates
- Maintain clear separation of concerns between components

### Minimize Dependencies  
- Each component should be as self-contained as possible
- Avoid deep dependency chains between components
- Document all component dependencies explicitly

### Optimize for Maintainability
- Keep individual components small and focused
- Use descriptive names for components and variables
- Maintain backward compatibility for component interfaces

### Ensure Consistency
- Use shared metadata schemas across all templates
- Maintain consistent naming conventions for variables
- Follow established patterns for component integration
```

### 3. Quality Assurance
```markdown
## Template Quality Standards

### Component Standards
- **Size Limit**: Individual components ≤50 lines
- **Focus**: Single responsibility per component
- **Documentation**: Clear usage instructions and examples
- **Testing**: Validation scripts for component functionality

### Composition Standards
- **Compatibility**: All component combinations tested
- **Performance**: Template generation ≤2 seconds
- **Maintainability**: Clear dependency documentation
- **Usability**: Intuitive composition patterns for developers
```

## Tool Integration

### 1. Composition Validation
```bash
# Validate template composition
./scripts/templates/validate-composition.sh \
  --base=command-base \
  --mixins=p55-p56-compliance,integration-patterns \
  --output=validation-report.json

# Check component compatibility
./scripts/templates/check-compatibility.sh \
  --components=metadata-schema,phase-structures \
  --version=1.0.0
```

### 2. Template Generation
```bash
# Generate template from composition
./scripts/templates/generate-template.sh \
  --base=command-base \
  --mixins=enforcement-framework \
  --variables=variables.json \
  --output=new-command.md

# Batch generate templates
./scripts/templates/batch-generate.sh \
  --config=template-config.json \
  --output-dir=generated-templates/
```

### 3. Maintenance Tools
```bash
# Update shared components
./scripts/templates/update-components.sh \
  --component=metadata-schema \
  --version=1.1.0 \
  --migrate-templates=true

# Validate all template compositions
./scripts/templates/validate-all.sh \
  --fix-issues=true \
  --report=full
```

---

**Framework Authority**: ce-simple template composition system
**Usage**: All new templates must use composition framework
**Maintenance**: Quarterly review of component efficiency and compatibility
**Evolution**: Framework evolves based on usage patterns and developer feedback