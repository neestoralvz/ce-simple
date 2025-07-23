# Command Templates - Unified Template System

@./docs/templates/shared/metadata-schema.md#document_status_schema
@./docs/templates/shared/template-versioning.md#version_declaration_format

## Purpose
Consolidated command templates providing standardized structure through shared components, eliminating DRY violations and promoting composition over inheritance.

**Template Evolution**: Now uses shared component system from `docs/templates/shared/` for maximum reusability and maintainability.

## Template Categories

### 1. Basic Command Template
```markdown
# /command-name - Command Title

@./docs/templates/shared/metadata-schema.md#command_metadata_block

## Purpose
[Single sentence describing what this command accomplishes]

@./docs/templates/shared/metadata-schema.md#principles_and_guidelines

## Execution Process
@./docs/templates/shared/phase-structures.md#basic_5_phase_command_structure

@./docs/templates/shared/metadata-schema.md#error_handling_template

@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

### 2. P55/P56 Compliant Command Template
```markdown
# /command-name - Command Title

@./docs/templates/shared/metadata-schema.md#command_metadata_block

## Purpose
[Command description with P55/P56 compliance integration]

@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin

## Execution Process
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure

@./docs/templates/shared/metadata-schema.md#error_handling_template

@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

### 3. Enforcement Command Template
```markdown
# [Command Type]: `/command-name`

@./docs/templates/shared/metadata-schema.md#command_metadata_block

## **🚨 BLOCKING [Command Category]: [Command Title]**
**🚨 MANDATORY: Sistema WILL [core functionality] with AUTOMATIC blocking of [violations] and REQUIRED [verification type]**

## Purpose
🚨 BLOCKING: Sistema WILL [execute core function] with AUTOMATIC [blocking mechanism] and REQUIRED [compliance verification]. BLOCKING of [specific violations] and MANDATORY [enforcement protocols].

@./docs/templates/mixins/template-mixins.md#enforcement_framework_mixin

## Execution Process
@./docs/templates/shared/phase-structures.md#enforcement_phase_structure

@./docs/templates/shared/metadata-schema.md#error_handling_template

@./docs/templates/shared/metadata-schema.md#cross_reference_schema

---
@./docs/core/README.md
@./docs/core/system-principles.md
```

## Implementation Guidelines

@./docs/templates/shared/composition-framework.md#template_creation_process

### Choosing the Right Template
1. **Basic Command**: Use command-base + basic phase structure
2. **P55/P56 Compliant**: Use command-base + P55/P56 compliance mixin + compliant phase structure
3. **Enforcement Command**: Use command-base + enforcement framework mixin + enforcement phase structure

### Template Composition Process
```markdown
# Example: Creating P55/P56 Compliant Command

<!-- Base structure -->
@./docs/templates/shared/command-base.md

<!-- Add P55/P56 compliance -->
@./docs/templates/mixins/template-mixins.md#p55_p56_mathematical_compliance_mixin

<!-- Use compliant phases -->
@./docs/templates/shared/phase-structures.md#p55_p56_compliant_phase_structure

<!-- Standard metadata -->
@./docs/templates/shared/metadata-schema.md#command_metadata_block
```

@./docs/templates/shared/template-versioning.md#version_selection_guidelines

### Quality Standards
@./docs/templates/shared/composition-framework.md#quality_standards

## Cross-References
- [Shared Components](./shared/) - Core template building blocks
- [Template Mixins](./mixins/template-mixins.md) - Composable feature enhancements
- [Documentation Templates](./02-documentation-templates.md) - For command documentation
- [Validation Templates](./03-validation-templates.md) - For command testing
- [Composition Framework](./shared/composition-framework.md) - Template assembly guidelines

---

@./docs/templates/shared/metadata-schema.md#document_status_schema

**Template Category**: Command development templates
**Evolution**: DRY violations eliminated through shared component system
**Composition**: Base templates + mixins + shared components = modular commands
**Usage**: All command development in ce-simple system
**Authority**: Unified command template system with composition framework