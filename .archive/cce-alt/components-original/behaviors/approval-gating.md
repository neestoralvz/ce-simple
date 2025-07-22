# Approval-Gating Behavior

# PRINCIPLE: User approval required for sensitive operations
**Applied by**: Components handling sensitive operations
**Purpose**: Prevent unauthorized or dangerous actions
**Scope**: Operations affecting system structure or user data

# RULES

### Core Rules
- Explicit user approval required before sensitive operations
- Clear warning messages about operation implications
- No execution until approval confirmation received

### Implementation Pattern
```
WHEN: Sensitive operation requested
DO: Display approval gate with clear warning
VERIFY: User explicitly confirms with "proceed" or similar
```

### Verification Protocol
Approval gates format:
⚠️ CRITICAL: USER APPROVAL REQUIRED
**DO NOT PROCEED** without explicit user approval for [operation]
**This operation will [consequences] - confirm with "proceed"**

### Success Indicators
- User approval explicitly obtained
- Operation consequences clearly communicated
- No sensitive operations executed without approval