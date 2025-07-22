# Start Agent Communication Protocol

## Decision Transparency Framework

### Decision Types and Rationales

**Exploration Decision Examples**:
```
🧠 DECISION: Local exploration sufficient → Request matches existing patterns
🧠 DECISION: Web research needed → External validation required for solution
🧠 DECISION: Parallel agents optimal → Independent domains identified
🧠 DECISION: Sequential flow required → Analysis dependencies detected
🧠 DECISION: Level 3 analysis needed → Complex integration patterns found
🧠 DECISION: Sufficient at level 2 → Clear execution path identified
```

### Agent Communication Protocol
- **Deploy**: Main agent → Task agent with specific objectives
- **Execute**: Task agent performs assigned function
- **Return**: Task agent → Main agent with results summary
- **Announce**: Main agent updates user with progress + brief rationale

### Quick Decision Matrix
- **Complexity ≤5**: Local exploration, sequential agents, level 1-2 analysis
- **Complexity 6-7**: Mixed exploration, context-dependent agents, level 2-3 analysis  
- **Complexity ≥8**: Full exploration, parallel agents, level 3-4 analysis

## Intelligent Notification System

**Real-Time Progress with Decision Context**: Uses standardized notification patterns for consistent user experience

**Reference**: See `../../docs/workflow/workflow-notifications.md` for complete notification templates and patterns

## Git Integration Protocol

**SESSION-COMPLETION Tracking**: Uses discovery workflow commit template for standardized session tracking

**Reference**: See `../../docs/workflow/git-integration.md` for discovery workflow commit structure