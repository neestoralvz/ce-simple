# Modular Architecture Directory Structure - Organization Design

**29/07/2025** | Commands methodology + documentation template modules structure

## Commands Methodology Modules Structure
```
.claude/commands/methodology/
├── thinkx4.md                 # Universal 4-perspective analysis
├── parallel_execution.md      # Concurrent tools enforcement  
├── continuous_flow.md         # Anti-interruption execution
├── research_first.md          # Timestamp validation + WebSearch protocols
├── validation_protocol.md     # Authority alignment verification
├── context_loading.md         # Conditional reference patterns
└── template_integration.md    # How commands load methodology
```

## Documentation Template Modules Structure
```
context/modules/
├── headers/
│   ├── standard.md            # Basic header template
│   ├── timestamped.md         # Creation + update timestamp format
│   └── decision.md            # Decision document header
├── footers/
│   ├── conditional_links.md   # "Si necesitas X → link" pattern
│   ├── authority_chain.md     # Authority source + references  
│   └── trazabilidad.md        # Source traceability footer
├── enforcement/
│   ├── vocabulary.md          # DEBE, OBLIGATORIO, NUNCA patterns
│   ├── templates.md           # "Template correcto:" patterns
│   └── anti_patterns.md       # "NUNCA hacer:" patterns
├── content/
│   ├── think_sections.md      # Think 1-4 analysis structure
│   ├── phase_structure.md     # Phase 1-N organization
│   └── validation_gates.md    # Validation criteria templates
└── integration/
    ├── module_loading.md      # How docs reference modules
    ├── reference_syntax.md    # **LOAD:** syntax standards
    └── template_composition.md # Multiple module composition
```

## Module Reference Syntax Standards

### Commands Loading Methodology Pattern
```markdown
# Standard methodology loading pattern
## Methodology Integration
**LOAD:** /methodology:thinkx4 + /methodology:parallel + /methodology:validation
**CONTEXT:** context/patterns/specific_domain.md

## Core Function
[Command-specific implementation using loaded methodologies]
```

### Documentation Loading Templates Pattern  
```markdown
# Standard documentation template pattern
**TEMPLATE:** /modules:header_timestamped + /modules:enforcement_vocabulary
**CONTENT:** /modules:think_sections + /modules:phase_structure  
**FOOTER:** /modules:footer_authority + /modules:conditional_links

## Document-Specific Content
[Unique information not available in templates]
```

---
**Referencias:** → context/operational/decisions/modular_architecture_methodology_specs.md (methodology specifications)
→ context/operational/decisions/modular_architecture_template_specs.md (template specifications)