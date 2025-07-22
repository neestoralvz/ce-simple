# Claude.md Import System

## 🎯 IMPORT SYSTEM SPECIFICATION

**Propósito**: Sistema avanzado de importación que permite incluir contenido externo en Claude.md de manera dinámica, condicional y optimizada para el contexto.

### Core Import Principles
- **Dynamic Content Inclusion**: Importación de archivos externos según necesidades
- **Conditional Importing**: Contenido se importa basado en triggers contextuales
- **Context Optimization**: Minimizar uso de contexto cargando solo lo necesario
- **Self-Contained Compliance**: Todos los imports respetan autocontención dual

## 📋 IMPORT SYNTAX SPECIFICATIONS

### Basic Import Syntax
```markdown
@import[TYPE](file:options)

Types Available:
├── LAZY → On-demand loading
├── CONDITIONAL → Context-based loading  
├── LINES → Specific line ranges
└── FULL → Complete file inclusion (use sparingly)
```

### Lazy Import
```markdown
@import[LAZY](relative/path/to/file.md)

Example:
@import[LAZY](system/protocols/project-structure-detailed.md:lines:1-25)

Usage: Content loaded only when explicitly requested or triggered
Context Impact: Minimal initial load, +20-25% when accessed
```

### Conditional Import  
```markdown
@import[CONDITIONAL](file.md:trigger:condition)

Examples:
@import[CONDITIONAL](system/protocols/reference-catalog.md:trigger:exploration_mode)
@import[CONDITIONAL](system/protocols/implementation-status.md:trigger:handoff_context)
@import[CONDITIONAL](system/architecture/operational-flow.md:lines:15-45:trigger:complexity>5)

Usage: Content loaded automatically when trigger conditions are met
Context Impact: +10-15% per triggered import
```

### Line-Specific Import
```markdown
@import[LINES](file.md:start_line-end_line)

Examples:
@import[LINES](system/protocols/extended-system-components.md:1-50)
@import[LINES](architecture/overview.md:15-30)

Usage: Import specific sections of files to minimize context usage
Context Impact: Proportional to lines imported
```

## 🚀 TRIGGER SYSTEM

### Conditional Trigger Definitions
```markdown
Available Triggers:
├── complexity>N → Content for operations above complexity level N
├── component_request → Component catalog and detailed descriptions
├── exploration_mode → Research, analysis, and discovery content
├── handoff_context → Implementation handoff and transfer content
├── metrics_request → Detailed metrics, thresholds, and success criteria
├── troubleshooting_mode → Diagnostic and problem resolution content
├── architecture_focus → Deep architectural specifications
└── protocol_detail → Comprehensive protocol documentation
```

### Trigger Activation Logic
```markdown
Trigger Evaluation Process:
1. Analyze current operation context
2. Assess user request patterns
3. Check system state indicators
4. Evaluate complexity requirements
5. Activate relevant conditional imports
6. Monitor context usage impact
7. Optimize trigger sensitivity
```

### Multi-Trigger Conditions
```markdown
Complex Trigger Logic:
@import[CONDITIONAL](file.md:trigger:complexity>3&handoff_context)
@import[CONDITIONAL](file.md:trigger:component_request|exploration_mode)
@import[CONDITIONAL](file.md:trigger:metrics_request&architecture_focus)

Logical Operators:
├── & (AND) → All conditions must be true
├── | (OR) → Any condition can be true  
└── ! (NOT) → Condition must be false
```

## 📊 CONTEXT OPTIMIZATION STRATEGIES

### Import Hierarchy
```markdown
Import Priority Levels:
├── Level 0: Core system information (Always loaded)
├── Level 1: Conditional imports (Trigger-based)
├── Level 2: Lazy imports (On-demand)
└── Level 3: Deep reference imports (Explicit request only)
```

### Context Budget Management
```markdown
Context Usage Allocation:
├── Core Claude.md content: 40-50% context
├── Conditional imports: 20-25% context
├── Lazy imports: 15-20% context
├── Reserved for operations: 10-15% context
└── Emergency buffer: 5% context
```

### Smart Import Caching
```markdown
Caching Strategy:
├── Cache frequently triggered imports
├── Pre-load high-probability conditional content
├── Maintain cache of recent lazy imports
├── Expire cache based on context pressure
└── Optimize cache based on usage patterns
```

## 🔧 IMPLEMENTATION RULES

### File Location Requirements
```markdown
Import Source Requirements:
✅ All imported files must exist in system/ directory
✅ Files must respect self-contained architecture
✅ Maximum file size: 200 lines
✅ Files must be optimized for partial import (LINES)
❌ No imports from components/ directory
❌ No imports from handoffs/ directory
❌ No external URL imports
```

### Import Validation Protocol
```markdown
Pre-Import Validation:
├── Verify file exists and is accessible
├── Check file size and line count limits
├── Validate line range specifications (for LINES imports)
├── Confirm trigger condition syntax
├── Test context impact estimation
└── Verify self-containment compliance
```

### Error Handling
```markdown
Import Error Management:
├── File not found → Graceful degradation with warning
├── Line range invalid → Import available lines with notification
├── Context overflow → Skip import with alternative summary
├── Trigger malfunction → Default to lazy loading
└── Circular imports → Detection and prevention protocol
```

## 🎭 ADVANCED IMPORT PATTERNS

### Progressive Import Enhancement
```markdown
Progressive Content Strategy:
├── @import[LINES](overview.md:1-20) → Summary
├── @import[CONDITIONAL](detailed.md:trigger:complexity>3) → Details
├── @import[LAZY](comprehensive.md) → Complete specification
└── Each level provides functional completeness
```

### Context-Aware Import Scaling
```markdown
Dynamic Import Adjustment:
├── High context availability → More aggressive imports
├── Low context availability → Minimal essential imports
├── Critical operations → Override context limits for essential imports
├── Background operations → Defer non-essential imports
└── Emergency situations → Essential imports only
```

### Import Chain Management
```markdown
Dependency Chain Handling:
├── Map import dependencies between files
├── Resolve import chains efficiently
├── Prevent circular import dependencies
├── Optimize import order for context efficiency
└── Cache common import chains
```

## 📋 MAINTENANCE AND OPTIMIZATION

### Import Performance Monitoring
```markdown
Performance Metrics:
├── Import resolution time per file
├── Context usage per import type
├── Trigger accuracy and false positive rates  
├── Cache hit rates and effectiveness
├── User satisfaction with import responsiveness
└── System coherence maintenance during imports
```

### Import System Evolution
```markdown
Continuous Improvement:
├── Analyze import usage patterns
├── Optimize trigger conditions based on actual usage
├── Refine context budget allocations
├── Update file organization for import efficiency
├── Enhance caching strategies
└── Improve error handling and recovery
```

## 🔗 Internal References

- [Lazy Loading](./lazy-loading.md)
- [Core Rules](./core-rules.md) (próximamente)
- [File References](../../implementation/file-references.md)
- [System Management](../README.md)

---

*Sistema de importación avanzado que permite inclusión dinámica y optimizada de contenido externo manteniendo eficiencia contextual y coherencia del sistema*