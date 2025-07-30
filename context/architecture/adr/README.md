# Architecture Decision Records (ADR)

**30/07/2025 15:45 CDMX** | Formal architectural decision authority

## PURPOSE
Document significant architectural decisions with full context, alternatives considered, and rationale following user authority supremacy.

## CONTENT CRITERIA
**Belongs here:**
- Major architectural changes affecting system structure
- Technology choice decisions with user vision impact
- Structural pattern adoptions with rationale
- Integration approach decisions

**Exclusions:**
- Minor implementation details
- Temporary workarounds
- Feature-specific logic

## NAMING CONVENTIONS
Format: `YYYY-MM-DD-decision-title.md`
Examples:
- `2025-07-30-context-architecture-consolidation.md`
- `2025-07-30-reference-only-content-protocol.md`
- `2025-07-30-semantic-trigger-system.md`

## ADR STRUCTURE TEMPLATE
```markdown
# ADR-XXXX: Decision Title

**Date**: YYYY-MM-DD
**Status**: Proposed/Accepted/Deprecated/Superseded
**Authority**: User vision alignment validation

## Context
Architectural challenge requiring decision

## Decision
What was decided and why

## Consequences
Positive and negative outcomes expected

## Alternatives Considered
Other options evaluated

## Authority Validation
Reference to user vision/authority source
```

## CROSS-REFERENCES
- **Authority validation**: @context/architecture/core/authority.md decision hierarchy
- **Vision alignment**: @context/vision/vision_foundation.md foundation check
- **Implementation impact**: @context/architecture/core/methodology.md process integration

---
**AUTHORITY**: All ADRs validated against @context/architecture/core/truth-source.md before acceptance