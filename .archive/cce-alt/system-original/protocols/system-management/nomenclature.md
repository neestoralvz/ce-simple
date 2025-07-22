# Nomenclature Standards - Estándares Unificados de Nomenclatura

## 🎯 UNIFIED NOMENCLATURE SYSTEM

**Propósito**: Estándares unificados de nomenclatura que aseguran consistencia, claridad y mantenibilidad en todo el ecosistema inteligente, consolidando todas las reglas de nomenclatura en un solo sistema coherente.

### Core Nomenclature Principles
- **Consistency**: Nomenclatura uniforme en todo el sistema
- **Clarity**: Nombres descriptivos y auto-explicativos
- **Maintainability**: Facilitar mantenimiento y evolución
- **Self-Documentation**: Nombres que documentan su propósito

## 📋 COMPONENT NOMENCLATURE STANDARDS

### Agent Naming Convention
```markdown
Agent Naming Pattern: [domain]-[function]

Examples:
✅ file-operations → Domain: file, Function: operations
✅ data-analysis → Domain: data, Function: analysis  
✅ quality-verification → Domain: quality, Function: verification
✅ cross-reference-validator → Domain: cross-reference, Function: validator
✅ system-health-monitor → Domain: system-health, Function: monitor

Rules:
├── Use kebab-case for all agent names
├── Domain-first naming for clarity
├── Function describes primary capability
├── Avoid abbreviations unless universally clear
└── Max 3-4 words total for cognitive efficiency
```

### Orchestrator Naming Convention
```markdown
Orchestrator Naming Pattern: [scope]-[coordination-type]

Examples:
✅ zero-unified-complete → Scope: zero (master), Type: unified-complete
✅ quality-assurance → Scope: quality, Type: assurance
✅ documentation-coordination → Scope: documentation, Type: coordination
✅ evolution-management → Scope: evolution, Type: management
✅ claude-md-maintenance → Scope: claude-md, Type: maintenance

Rules:
├── Scope indicates coordination domain
├── Type indicates coordination pattern
├── Use descriptive, not generic names
├── Avoid "orchestrator" suffix (implicit)
└── Focus on coordination responsibility
```

### Behavior Naming Convention
```markdown
Behavior Naming Pattern: [protocol]-[application-type]

Examples:
✅ coherence-system-unified → Protocol: coherence-system, Type: unified
✅ mathematical-verification-system-unified → Protocol: mathematical-verification-system, Type: unified
✅ component-evolution → Protocol: component, Type: evolution
✅ emergency-response → Protocol: emergency, Type: response
✅ parallel-operations → Protocol: parallel, Type: operations

Rules:
├── Protocol describes the behavioral pattern
├── Type indicates application method
├── Behaviors are reusable across components
├── Clear distinction from agent/orchestrator names
└── Focus on the behavioral pattern, not implementation
```

## 📁 FILE AND DIRECTORY NOMENCLATURE

### File Naming Standards
```markdown
File Naming Convention: [concept]-[type].md

Examples:
✅ universal-rules.md → Concept: universal, Type: rules
✅ component-evolution.md → Concept: component, Type: evolution
✅ cognitive-limits.md → Concept: cognitive, Type: limits
✅ file-references.md → Concept: file, Type: references
✅ lazy-loading.md → Concept: lazy, Type: loading

Rules:
├── Use kebab-case for all file names
├── Concept-first, type-second pattern
├── .md extension for all documentation
├── Avoid generic names like "protocol.md"
└── Self-documenting file names
```

### Directory Naming Standards
```markdown
Directory Naming Convention: [purpose] (singular or plural based on content)

Examples:
✅ architecture/ → Single purpose, descriptive
✅ protocols/ → Multiple items, plural appropriate
✅ orchestration/ → Domain-specific organization
✅ system-management/ → Compound purpose, clear scope
✅ getting-started/ → User journey stage

Rules:
├── Use kebab-case for multi-word directories
├── Descriptive of contained content
├── Logical grouping principle
├── Avoid generic names like "misc" or "other"
└── Hierarchical organization principle
```

## 🎭 OPERATIONAL NOMENCLATURE

### Task Deployment Naming
```markdown
Task Deployment Pattern: Task("[location]/[component-name]", "[description]")

Examples:
✅ Task("components/agents/file-operations", "File validation specialist")
✅ Task("components/orchestrators/quality-assurance", "Quality coordination")
✅ Task("system/protocols/verification-validation-testing", "VVP protocol")

Rules:
├── Full path specification for clarity
├── Component name matches file name
├── Description explains deployment purpose
├── Consistent with component nomenclature
└── Self-documenting deployment calls
```

### Notification Format Naming
```markdown
Notification Pattern: 📊 [LX:TYPE] ACTION | DATA | METRICS

Examples:
✅ 📊 [L1:Quality] Deploy | agents:4 | mission:validation | State: ACTIVE
✅ 📊 [L2:Agent] Execute | tool:Read | file:system/protocols/ | State: SUCCESS  
✅ 📊 [L0:Zero] Coordinate | orchestrators:3 | parallel:yes | State: OPTIMIZED

Type Codes:
├── Zero → Orchestrator-Zero (L0)
├── Orch → Generic Orchestrator (L1+)  
├── Agent → Agent Execution (L2+)
├── Behav → Behavior Application
├── MathVer → Mathematical Verification
└── System → System-wide operations
```

## 📊 QUALITY NOMENCLATURE STANDARDS

### Verification and Metrics Naming
```markdown
Verification Pattern: [metric-type]:[value]:[threshold]:[state]

Examples:
✅ Success:94%:>90%:VALID → Success rate 94%, threshold >90%, state valid
✅ Performance:+15%:>10%:ENHANCED → Performance improved 15%, threshold >10%
✅ Context:68%:<70%:OPTIMAL → Context usage 68%, threshold <70%
✅ Quality:97%:>95%:EXCELLENT → Quality 97%, threshold >95%

Rules:
├── Metric type describes what's being measured
├── Value is the actual measurement
├── Threshold is the success/failure criteria
├── State indicates the evaluation result
└── Consistent format for mathematical verification
```

### Reference and Link Naming
```markdown
Reference Pattern: [Display Text](relative/path/to/file.md) - Description

Examples:
✅ [Architecture Overview](./overview.md) - Complete system architecture
✅ [Universal Rules](../protocols/orchestration/universal-rules.md) - Orchestrator standards
✅ [Component Playbook](./guides/advanced/component-playbook.md) - Advanced usage guide

Rules:
├── Display text is human-readable and descriptive
├── Path uses relative references for portability
├── Description explains link purpose
├── Consistent with file naming standards
└── Self-documenting link purpose
```

## 🔧 IMPLEMENTATION AND COMPLIANCE

### Nomenclature Validation Protocol
```markdown
📊 [L2:Nomenclature] Validation | Standard: component-naming | Compliance: 98% | State: VALID
📊 [L2:Nomenclature] Validation | Standard: file-naming | Compliance: 100% | State: COMPLIANT
📊 [L2:Nomenclature] Validation | Standard: directory-structure | Compliance: 95% | State: VALID
```

### Automated Compliance Checking
```markdown
Nomenclature Compliance Tools:
├── **File Name Validation**: Check kebab-case and pattern compliance
├── **Directory Structure**: Verify hierarchical organization standards
├── **Component Name Consistency**: Ensure component names match across references
├── **Reference Format Validation**: Check link format and description standards
├── **Documentation Consistency**: Verify terminology usage across files
└── **Pattern Compliance**: Automated checking of naming pattern adherence
```

### Migration and Update Protocols
```markdown
Nomenclature Evolution Process:
1. **Standard Proposal**: New or updated naming standard proposal
2. **Impact Analysis**: Assess changes required across system
3. **Migration Planning**: Plan systematic update across all components
4. **Automated Updates**: Use tools to update naming where possible
5. **Manual Review**: Human review of critical name changes
6. **Validation Testing**: Ensure all references work after updates
7. **Documentation Update**: Update standards documentation
8. **Compliance Monitoring**: Ongoing monitoring of new standard adoption
```

## 📋 SPECIAL CASES AND EXCEPTIONS

### Abbreviation Guidelines
```markdown
Approved Abbreviations:
✅ API → Application Programming Interface (universally understood)
✅ URL → Uniform Resource Locator (standard web terminology)
✅ VVT → Verification-Validation-Testing (system-specific, documented)
✅ L0, L1, L2 → Layer indicators (system hierarchy shorthand)

Rules for New Abbreviations:
├── Must be universally understood in context
├── Must be documented when first introduced
├── Should not sacrifice clarity for brevity
├── Consistent usage across entire system required
└── Prefer full names unless abbreviation adds significant value
```

### Legacy Name Handling
```markdown
Legacy Component Management:
├── **Gradual Migration**: Phase out old names over time
├── **Deprecation Warnings**: Mark old names as deprecated
├── **Reference Updates**: Update all internal references systematically
├── **Documentation Clarity**: Clear mapping of old to new names
└── **Backward Compatibility**: Maintain understanding of legacy references during transition
```

## 🔗 Internal References

- [System Management](./README.md)
- [File References](../../implementation/file-references.md)
- [Component Repository](./component-repository.md)
- [Quality Standards](../../../guides/reference/quality-standards.md) (próximamente)

---

*Sistema unificado de nomenclatura que asegura consistencia, claridad y mantenibilidad en todo el ecosistema inteligente a través de estándares sistemáticos y verificables*