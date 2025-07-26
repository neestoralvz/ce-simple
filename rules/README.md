# System-Wide Rules

**Purpose**: Modular system-wide rules for CLAUDE_RULES conditional loading  
**Scope**: System behavior and methodology (vs project-specific rules in docs/rules/)

## Directory Purpose

**System Rules** (`/rules/`): Core system behavior and methodologies that govern how Claude operates across any project using this VDD framework.

**Project Rules** (`docs/rules/`): Project-specific behavioral protocols and development standards for ce-simple.

## Modular Rules Architecture

### Core Methodology Rules
- `planning-methodology.md` - Step-by-step planning + handoffs + parallel conversations
- `content-auditing-methodology.md` - 4-step content auditing (INVENTORY → EXTRACT → CONSOLIDATE → MODULARIZE)
- `documentation-first-rule.md` - ANALYZE → DECIDE → DOCUMENT → CREATE protocol
- `claude-rules-modularization.md` - How to modularize CLAUDE_RULES itself

### System Operation Rules  
- `orchestration-protocols.md` - Task Tool + parallel execution requirements
- `transparency-requirements.md` - Sub-agent visibility and reporting protocols
- `partnership-protocol.md` - Core AI-user collaboration guidelines
- `pts-compliance.md` - PTS validation enforcement protocols

### Conditional Loading Rules
- `conditional-loading-protocols.md` - When and how to load specific rules

## Loading Pattern

**CLAUDE_RULES.md contains:**
```markdown
**IF planning work** → READ rules/planning-methodology.md
**IF content auditing** → READ rules/content-auditing-methodology.md  
**IF orchestration needed** → READ rules/orchestration-protocols.md
```

## Authority Hierarchy

1. **user-input/** - User vision (absolute authority)
2. **CLAUDE_RULES.md** - Core partnership protocol + conditional loading
3. **rules/** - System-wide behavioral rules (this directory)
4. **docs/rules/** - Project-specific rules and standards

---

**System Principle**: Modular rules enable conditional loading, reducing always-loaded context while maintaining comprehensive behavioral guidance when needed.