# Conditional Loading Protocols

**Purpose**: Context-based rule loading orchestration system  
**Authority**: Orchestration layer - routes to specific rules based on task context  
**Reference**: rules/loading-separation-rule.md for classification criteria  
**Status**: Active | **Lines**: ≤80

## Governance Rules Context (NEW)

### Documentation Tasks
**IF writing documentation** → READ rules/three-layer-documentation-rule.md + rules/nomenclature-rule.md  
**IF organizing content** → READ rules/content-distribution-rule.md + rules/nomenclature-rule.md  
**IF creating methodology** → READ rules/three-layer-documentation-rule.md
**IF creating files** → READ rules/template-usage-protocols.md
**IF communicating with user** → READ rules/communication-standards-protocols.md
**IF documenting work** → READ rules/communication-standards-protocols.md

### System Design Tasks
**IF modular architecture** → READ rules/modular-architecture-rule.md  
**IF system restructuring** → READ rules/content-distribution-rule.md + rules/modular-architecture-rule.md  
**IF unclear about rule loading** → READ rules/loading-separation-rule.md

### Content Organization Tasks  
**IF file classification** → READ rules/nomenclature-rule.md  
**IF directory structure** → READ rules/nomenclature-rule.md + rules/modular-architecture-rule.md  
**IF consolidation decision** → READ rules/content-distribution-rule.md
**IF context economy optimization** → READ tools/templates/context-economy-template.md

### Core Workflow Context
**IF user request received** → READ rules/master-workflow-protocols.md

## Legacy System Context (EXISTING)

### System Operation Context
**Orchestration Work**: Complex workflow coordination → READ rules/orchestration-protocols.md
**Planning Activities**: Structured project approach → READ rules/planning-methodology.md  
**Sub-Agent Tasks**: Parallel execution transparency → READ rules/transparency-requirements.md

### Development Work Context
**Code Implementation**: Programming and TDD → READ rules/development-workflow-protocols.md + rules/tdd-protocols.md
**Architecture Decisions**: System design choices → READ rules/architecture-decision-protocols.md
**Quality Validation**: Testing and verification → READ rules/validation-protocols.md
**Command Creation**: New command development → READ rules/command-review-protocols.md

### Technical Context
**Git Operations**: Version control workflows → READ docs/rules/git-workflow-protocols.md
**CLAUDE.md Architecture**: Import methodology → READ docs/standards/claude-md-import-methodology.md

## Core Authority Context (docs/core/ Integration)

### Governance & Authority Context
**IF governance decisions** → READ docs/core/02-std-standards/std-command-governance.md
**IF authority hierarchy needed** → READ docs/core/02-std-standards/std-command-governance.md
**IF modular rules architecture** → READ docs/decisions/governance/modular-rules-adr.md

### Technical Standards Context (BLOCKING)
**IF development standards needed** → READ docs/core/02-std-standards/std-development.md
**IF command structure rules** → READ docs/core/02-std-standards/std-command-structure.md
**IF command review required** → READ docs/core/02-std-standards/std-command-review.md

### Communication Standards Context
**IF documentation standards work** → READ docs/core/03-com-communication/com-documentation.md
**IF markdown standards needed** → READ docs/core/03-com-communication/com-markdown.md
**IF context management rules** → READ docs/core/03-com-communication/com-context-management.md

### Performance Optimization Context
**IF context economy work** → READ docs/core/05-per-performance/per-context-economy.md
**IF efficiency optimization** → READ docs/core/05-per-performance/per-efficiency.md
**IF context mapping needed** → READ docs/context/methodologies/context-mapping.md

### Advanced Protocols Context
**IF task orchestration work** → READ docs/core/04-pro-protocols/pro-task-orchestration.md
**IF parallel execution needed** → READ docs/core/04-pro-protocols/pro-parallel-execution.md
**IF advanced git workflows** → READ docs/core/04-pro-protocols/pro-git-workflow.md