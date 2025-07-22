# Context-Tracking Behavior

## 🎯 PRINCIPLE: Context Optimization Required
**Applied by**: Components when managing context and handoffs
**Purpose**: Optimize context usage and trigger automatic handoffs
**Scope**: All operations that consume context

## ⚡ RULES

### Core Rules
- Track context usage continuously
- Trigger handoff preparation at 90%
- Calculate CTX percentage mathematically

### Implementation Pattern
```
WHEN: Any operation consuming context
DO: Calculate CTX = (tokensUsed/maxContext) * 100
VERIFY: Trigger handoff if CTX >= 90%
```

### Verification Protocol
Real-time context calculation using token counting tools

### Success Indicators
- Context percentage calculated accurately
- 90% handoff triggers activated automatically