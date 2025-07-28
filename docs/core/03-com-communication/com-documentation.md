# Documentation Standards - Foundation Layer

**Updated**: 2025-07-24 | **Authority**: Core methodology | **Limit**: ≤50 lines
**Navigation**: [System Hub](../navigation/index.md) | **Implementation**: @docs/implementation/documentation-standards-implementation.md | **Validation**: @docs/validation/documentation-standards-checklist.md

## Core Philosophy

**Objective**: Create clear, actionable documentation optimized for Claude Code agent deployment
**Authority**: Three-layer architecture + conditional import framework + PTS 12/12 compliance
**Integration**: Enhanced Conditional Context System triggers + agent coordination patterns

## Essential Principles

**Apply Simplicity**: Clear first read | Essential only | Complete | Actionable
**Execute Word Economy**: Contributing words only | Action verbs | Zero redundancy
**Enforce Anti-Bias**: Objective criteria | Measurable standards | Agnostic tone
**Deploy Agent Architecture**: Foundation → Implementation → Validation coordination

## Decision Triggers

**Apply When**: Creating/updating documentation | Setting writing standards | Agent deployment needed
**Context Required**: Purpose clarity | Audience identification | Integration requirements
**Success Criteria**: Three-layer compliance | Agent-deployable procedures | Measurable validation

## Three-Layer Architecture

**Layer 1 (Foundation)**: Core concepts as agent prompts (≤50 lines) - THIS FILE
**Layer 2 (Implementation)**: @docs/implementation/documentation-standards-implementation.md
**Layer 3 (Validation)**: @docs/validation/documentation-standards-checklist.md

## Three-Layer Line Limits

**Foundation Layer**: ≤50 lines - Essential concepts as agent prompts (cognitive load optimized)
**Implementation Layer**: ≤100 lines - Detailed procedures for agent deployment (context economy)
**Validation Layer**: ≤100 lines - Quality gates and checklists for agent validation (focused compliance)
**Zero Duplication**: One specialized file per concept | Layer separation prevents overlap
**Protocol Integration**: @rules/CLAUDE_RULES.md partnership governance + @CLAUDE.md navigation rules apply

## Context Management

**Reference Standards**: [Claude.md Import Methodology](../standards/claude-md-import-methodology.md) - @ import vs reference patterns
**Conditional Instructions**: `**IF condition** → READ docs/path/file.md:lines` for workflow triggers
**Navigation Links**: `[Title](docs/path/file.md)` standard markdown for all regular documentation
**Protocol Coordination**: Authority hierarchy + conditional loading integration
**Component Extraction**: Preserve agent-deployable content before compaction

---

**🤖 AGENTS**: Implementation + Validation + Coordination via Task Tool deployment

**Architecture Principle**: Essential understanding enables agent-coordinated documentation excellence