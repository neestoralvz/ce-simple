# Documentation Standards

**Updated**: 2025-07-24 | **Language**: English-only | **Limit**: 100 lines | **Architecture**: Three-layer with conditional import framework  
**Navigation**: [System Hub](../navigation/index.md) | [Communication Rules](communication-rules.md) | [Markdown Standards](markdown-standards.md)

## Core Principles
**Apply Simplicity**: Write clear on first read | Include essential only | Make complete | Ensure actionable  
**Execute Word Economy**: Use contributing words only | Eliminate fluff | Use action verbs | Remove redundancy  
**Enforce Anti-Bias Language**: Eliminate subjective terms that introduce interpretation bias | Use objective, measurable criteria | Remove embellishments and subjective adjectives | Maintain agnostic tone
**Apply Three-Layer Architecture**: Concept (≤50 lines) → Implementation (referenced) → Verification (agent-deployed)
**Execute Component Extraction**: Extract reusable components to specialized files before applying compaction
**Deploy Agent Integration**: Use specialized writing agents for standard compliance
**Document Self-Reference**: All documentation directed to Claude Code - write as instructions for Claude Code to follow

## Conditional Import Framework

### Decision-Triggered Loading
**Documentation Creation Trigger**: Load @docs/rules/markdown-standards.md when creating new documentation
**Methodology Creation Trigger**: Load @docs/templates/three-layer-methodology-template.md + @docs/standards/layer-separation-rules.md
**Agent Deployment Trigger**: Load @docs/standards/agent-deployment-footer-standard.md when adding agent coordination
**Component Extraction Trigger**: Load @docs/standards/context-compaction-techniques.md:51-70 when file exceeds 80% of line limits
**Template Usage Trigger**: Reference vs import based on frequency (daily use → import | rare use → reference)
**Line Reference Trigger**: Use precise line ranges (@file.md:15-23) when referencing specific procedures | **Line Import Standards**: @docs/standards/line-level-import-standards.md

### Three-Layer Architecture Integration
**Layer 1 (Concept)**: Essential understanding ≤50 lines | Core methodology | Decision triggers | Quick references | **Extract components before layer assignment**
**Layer 2 (Implementation)**: Referenced via @docs/implementation/ | Technical procedures | Step-by-step guides | Agent-deployed context | **Include extracted procedures & examples**
**Layer 3 (Verification)**: Agent-deployed via @docs/validation/ | Quality gates | Compliance checks | Success metrics | **Include extracted checklists & validation lists**

### Length Limits | Anti-Duplication Mandate
Commands: ≤80 | **Docs: ≤100** | **Concept Layer: ≤50** | Patterns: ≤80 | Standards: ≤80
**Zero Duplication**: Technical content exists in ONE specialized file only | Layer separation prevents content duplication

## Component Extraction Requirements

### Mandatory Extraction Components
**Create Independent Files For**:
- **Checklists & Validation Lists**: `/docs/validation/[name]-checklist.md` | Preserve functional structure
- **Examples & Demonstrations**: `/docs/examples/[name]-examples.md` | Maintain practical clarity  
- **Templates & Frameworks**: `/docs/templates/[name]-template.md` | Enable reusability
- **Diagrams & Visual Content**: `/docs/diagrams/[name]-diagram.md` | Preserve visual integrity
- **Code Samples & Procedures**: `/docs/procedures/[name]-procedure.md` | Maintain step-by-step clarity

### Extraction Decision Criteria
**Apply Systematic Assessment**: Reusability test | Structural independence | Volume impact (>15 lines) | Reference frequency | Functional content protection

## Context Management Framework
**Standards**: @docs/standards/context-management-framework.md

## Agent Deployment Protocols
**Standards**: @docs/protocols/agent-deployment-protocols.md

## Quality Gates
**Validation Requirements**: @docs/validation/documentation-quality-gates.md

## Essential References | Context Loading Triggers

### Always Load (Import)
**@docs/rules/markdown-standards.md**: When creating any documentation
**@docs/templates/three-layer-methodology-template.md**: When creating methodology documentation  
**@docs/standards/layer-separation-rules.md**: When applying three-layer architecture

### Load When Needed (Conditional)
**@docs/standards/agent-deployment-footer-standard.md**: When adding agent coordination
**@docs/standards/context-compaction-techniques.md**: When optimizing documentation length

---

## See Also
- **[Communication Rules](communication-rules.md)** - Language & style standards
- **[Markdown Standards](markdown-standards.md)** - Official compliance framework
- **[Context Compaction](../standards/context-compaction-techniques.md)** - Mandatory compaction techniques
- **[System Navigation](../navigation/index.md)** - Complete system access hub
- **[PTS Framework](../core/pts-framework.md)** - Technical validation system

**Architecture Principle**: Three-layer architecture + conditional import framework + agent coordination = scalable, maintainable, validated documentation system with optimal cognitive load management