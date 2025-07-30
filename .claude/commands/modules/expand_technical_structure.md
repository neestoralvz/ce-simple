# Expand Technical Structure Module

## Purpose
Standardized technical documentation structure for `/actions:docs/` expansion

## Target Structure Template
```
/actions:docs/
├── technical/ (NEW - LLM guidance documents)
    ├── stack_requirements.md (research-driven)
    ├── code_organization.md (research-driven)
    ├── implementation_patterns.md (research-driven)
    ├── error_handling.md (research-driven)
    ├── configuration_management.md (research-driven)
    ├── testing_standards.md (research-driven)
    └── deployment_patterns.md (research-driven)
```

## Document Format Template
```markdown
# [Título Técnico]

## Derivación de Principios Establecidos
[Citas directas de @context/architecture/core/truth-source.md que justifican este contenido]

## Research Actualizado ([current_date])
### Industry Best Practices
[WebSearch + Context7 MCP results]

## Implementation Guidance
[Technical specifics for LLM implementation]
```

**Usage**: Referenced by expand.md to maintain consistent technical structure