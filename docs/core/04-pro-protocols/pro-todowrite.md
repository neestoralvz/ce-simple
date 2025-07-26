# TodoWrite Mandatory Usage Rule

**Authority**: Blocking Rule | **Updated**: 2025-07-24 12:54 (Mexico City)

## Mandatory Triggers
**MUST use TodoWrite when**: Multi-step tasks (≥2 steps) | User explicit requests | Pending items exist | Task A must complete before Task B can start | ≥2 tasks can execute simultaneously | Tasks requiring both data gathering and file modification

## Update Requirements
**Real-time tracking**: Mark in_progress BEFORE starting | Update completed IMMEDIATELY after | One task in_progress max | Remove irrelevant tasks | Add discovered subtasks instantly

## Blocking Criteria
**Development STOPS if**: No TodoWrite for multi-step work | Batched updates instead of real-time | Multiple in_progress tasks | Completed work not marked | Missing user-requested tasks

## Usage Patterns

### ✅ GOOD: Immediate Tracking
```yaml
User: "Add dark mode and run tests"
Assistant: *Creates TodoWrite with: 1) Add dark mode toggle 2) Run test suite*
*Marks task 1 in_progress* → *Implements* → *Marks completed*
*Marks task 2 in_progress* → *Runs tests* → *Marks completed*
```

### ❌ BAD: Missing/Batched Updates
```yaml
User: "Add dark mode and run tests"  
Assistant: *Starts implementing without TodoWrite* → BLOCKING VIOLATION
Assistant: *Creates todo but doesn't update status* → BLOCKING VIOLATION
Assistant: *Updates all tasks at end* → BLOCKING VIOLATION
```

## Enforcement Rules
**Uses 1 tool and affects 1 file**: Skip TodoWrite | **Uses >1 tool or affects >1 file**: Use TodoWrite | **User mentions "todo"**: Always use
**Research tasks**: Track even if not coding | **Discovered work**: Add subtasks immediately

## Integration
**With PTS**: TodoWrite demonstrates organization (Component #7) | **With commands**: All multi-step commands must track
**With validation**: Missing TodoWrite = PTS Structure failure | **With handoffs**: Todo state required for transitions

---
**Core Principle**: TodoWrite provides transparency and demonstrates systematic progress tracking for users.