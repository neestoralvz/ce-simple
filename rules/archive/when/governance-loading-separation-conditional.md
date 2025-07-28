# Loading Separation Rule

**Purpose**: Define exact criteria for rule classification & loading architecture  
**Authority**: Foundational governance - defines the governance system itself  
**Source**: Think×4 analysis of rules/CLAUDE_RULES.md vs conditional loading separation  
**Status**: Active | **Lines**: ≤80

## Rule Classification Criteria

### Perpetual Rules (rules/CLAUDE_RULES.md)
**Criteria**: 🛑 Blocking, applies to ALL actions, mandatory enforcement
**Content**:
- Think×4 requirement (mandatory for all decisions)
- PTS validation (12/12 required, blocks progression)  
- User-input authority (sacred hierarchy)
- Sub-agent transparency (individual progress reporting)
- Partnership protocol essentials

**Test**: If rule prevents ALL work when violated → Perpetual

### Conditional Rules (rules/)
**Criteria**: Context-specific, task-dependent, domain-focused
**Content**:
- Modular architecture procedures
- Documentation structure guidelines
- Content organization protocols
- Naming & classification standards

**Test**: If rule applies only to specific tasks → Conditional

### Orchestration Logic (conditional-loading-protocols.md)
**Criteria**: Routing logic, loading management, no procedures
**Content**:
- IF/THEN task detection
- Context-based rule references
- Dynamic loading triggers
- NO actual rule content, only references

**Test**: If content is routing logic → Orchestration

## Loading Sequence Protocol

1. **rules/CLAUDE_RULES.md** (always loaded) - Establishes perpetual framework
2. **conditional-loading-protocols.md** (when needed) - Routes to specific rules
3. **rules/specific-rule.md** (on-demand) - Provides detailed procedures

## Authority Hierarchy

1. **user-input/** - Sacred authority (never modify)
2. **rules/CLAUDE_RULES.md** - Perpetual rules (blocking enforcement)
3. **conditional-loading-protocols.md** - Orchestration layer
4. **rules/** - Specific operational rules

## Enforcement Standards

**Perpetual**: Must pass before ANY action proceeds
**Conditional**: Applied when context matches trigger conditions
**Orchestration**: Manages loading but doesn't block progression

## Integration Requirements

- No circular references between files
- Clear trigger conditions for conditional loading
- Maintained authority precedence throughout system
- Cognitive load optimization (≤80 lines per rule)

---

**🤖 IMPLEMENTATION AGENT**: Deploy Task Tool when unclear about rule classification
**🔍 VALIDATION AGENT**: Verify no rule misclassification or loading conflicts