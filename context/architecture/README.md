# Architecture Component

**30/07/2025 15:45 CDMX** | Architecture authority hub

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → architecture/ implements structural vision

## PURPOSE
Central hub for all architectural decisions, patterns, and structural guidance following user vision of "hacerlo lo que tiene que ser" - structure follows discovered function.

## COMPONENT ORGANIZATION

### `/adr/` - Architecture Decision Records
**Purpose**: Formal architectural decisions with context and rationale
**Content**: Decision documentation following ADR format
**Cross-reference**: @context/architecture/core/authority.md for decision validation

### `/standards/` - Architecture Standards  
**Purpose**: Technical standards and structural requirements
**Content**: Coding standards, design patterns, quality gates
**Cross-reference**: @context/architecture/standards/README.md for enforcement

### `/templates/` - Architecture Templates
**Purpose**: Reusable architectural patterns and structures
**Content**: Component templates, pattern definitions
**Cross-reference**: context/architecture/templates/README.md for template authority

### `/ux/` - User Experience Architecture
**Purpose**: Conversation-first design and interaction patterns
**Content**: UX patterns, interface design, conversation flows
**Cross-reference**: @context/vision/vision_foundation.md vision foundation

### `/workflows/` - Process Architecture
**Purpose**: Workflow patterns and process definitions
**Content**: Process flows, integration patterns, orchestration
**Cross-reference**: @context/architecture/core/methodology.md workflow authority

## NAMING CONVENTIONS
- **English naming** for all files and directories
- **Lowercase with hyphens** for multi-word names
- **Descriptive but concise** following 3-step explanation rule
- **Version suffixes** when evolution tracking needed

## CONTENT CRITERIA
- **Structural decisions** that affect system organization
- **Pattern definitions** for reusable architectural elements
- **Standards enforcement** related to system structure
- **Design rationale** behind architectural choices

## AUTHORITY CHAIN
@context/architecture/core/truth-source.md → architecture/ → specialized subdirectories → implementation

---
**INTEGRATION**: Architecture serves discovered user vision through structural intelligence