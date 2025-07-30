# Architecture Standards

**30/07/2025 15:45 CDMX** | Technical standards and structural requirements

## PURPOSE
Define technical standards and structural requirements that enforce user vision through architectural constraints and quality gates.

## CONTENT CRITERIA
**Belongs here:**
- Code organization standards (file structure, naming)
- Component design patterns and requirements
- Integration standards between system parts
- Quality gate definitions for architectural compliance
- Technical debt prevention protocols

**Exclusions:**
- Content formatting (goes to @context/standards.md)
- Behavioral enforcement (goes to @context/standards.md)
- Command-specific standards (stays in commands/)

## NAMING CONVENTIONS
Format: `[domain]-[type]-standards.md`
Examples:
- `component-design-standards.md`
- `integration-pattern-standards.md`
- `code-organization-standards.md`
- `quality-gate-standards.md`

## STANDARD STRUCTURE TEMPLATE
```markdown
# [Domain] Standards

## Authority Source
Reference to user vision/authority

## Requirements (OBLIGATORIO)
Mandatory compliance items

## Guidelines (DEBE)
Strong recommendations

## Anti-Patterns (NUNCA)
Prohibited approaches

## Validation Protocol
How compliance is verified
```

## INTEGRATION REFERENCES

### ← claude_code/
**Connection**: Claude Code tool compliance and technical standards alignment
**Protocol**: Standards ensure Claude Code methodologies comply with architectural requirements

### ↑ @context/standards.md
**Authority Source**: Comprehensive enforcement authority for all technical standards
**Protocol**: Architectural standards implement comprehensive system standards framework

### ←→ @context/methodology.md
**Connection**: Research-first protocol and technical validation methodology
**Protocol**: Standards validation through systematic methodology and empirical evidence

### → @architecture/adr/
**Connection**: Architectural decision validation and compliance verification
**Protocol**: Standards inform architectural decisions and ensure decision quality

### ↑ @context/authority.md
**Authority Source**: User authority framework drives compliance requirements
**Protocol**: All technical standards serve user vision supremacy and authority preservation

---
**INTEGRATION**: Technical standards serve user vision through intelligent constraints