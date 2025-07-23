# todo-manager

## Purpose
Universal TodoWrite management system extracted from 27+ commands providing standardized patterns for phase initiation, transition, completion, error handling, and behavioral reinforcement protocols across all ce-simple commands.

## Usage
```
/todo-manager [phase-type] [task-description] [current-status]
```

## Parameters
- `phase-type`: Phase transition type (init|progress|complete|error|final)
- `task-description`: Specific task description for TodoWrite entry
- `current-status`: Current task status (pending|in_progress|completed)

## Task Orchestration

### Universal TodoWrite Templates

#### Phase Initiation Template
```
Update TodoWrite: Mark "[Task Name]" as in_progress
```

#### Phase Transition Template  
```
Update TodoWrite: Complete previous, mark "[Next Task Name]" as in_progress
```

#### Error Handling Template
```
- Add TodoWrite task: "Resolve [error-type] issue: [specific problem]"
```

#### Phase Completion Template
```
Update TodoWrite: Complete previous, mark "[Final Task Name]" as in_progress
```

#### Final Completion Template
```
Update TodoWrite: Complete all [workflow-type] tasks
```

### Behavioral Reinforcement Protocols

**Progress Tracking Standards:**
- Single task in_progress at any time
- Immediate completion marking after task finish
- Specific error task creation with problem details
- Phase-based workflow progression
- Follow-up task generation for discovered issues

**Pattern Enforcement:**
- Consistent verb usage: "Mark", "Complete", "Add", "Resolve"
- Standardized task naming: descriptive + actionable
- Error specificity: include problem type and context
- Progress flow: linear progression through defined phases
- Completion verification: explicit workflow conclusion

### Common Task Categories

**Discovery Phase Tasks:**
- "[Domain] assessment", "[Context] discovery", "[Structure] analysis"

**Analysis Phase Tasks:**  
- "[Pattern] analysis", "[Complexity] calculation", "[Strategy] determination"

**Implementation Phase Tasks:**
- "[Action] execution", "[Component] generation", "[Integration] validation"

**Completion Phase Tasks:**
- "[Result] consolidation", "[Quality] validation", "[Status] reporting"

### Error Task Patterns

**Standard Error Types:**
- "Resolve calculation error: [specific issue]"
- "Resolve coordination failure: [specific issue]"  
- "Resolve analysis gap: [specific area]"
- "Address performance issue: [specific problem]"
- "Resolve matrix issue: [specific problem]"

**Error Task Structure:**
1. Action verb: "Resolve", "Address", "Fix"
2. Problem type: technical classification
3. Specific context: exact issue description
4. Priority: implicit high priority for error resolution

## Error Handling

**TodoWrite Failure Recovery:**
- Task state persistence across command failures
- Progress restoration from last valid state
- Error task automatic creation on workflow interruption
- Behavioral pattern correction through reinforcement

**Pattern Violation Detection:**
- Inconsistent verb usage monitoring
- Task naming standard validation
- Progress flow integrity checking
- Completion pattern verification

## Performance

**Template Application Time:** <0.1 seconds
**Pattern Validation:** <0.2 seconds
**Behavioral Reinforcement:** Real-time during command execution
**Cross-Command Standardization:** Immediate pattern propagation

## Examples

**Phase Initiation:**
```
/todo-manager init "Codebase structure assessment" pending
→ Update TodoWrite: Mark "Codebase structure assessment" as in_progress
```

**Phase Transition:**
```
/todo-manager progress "Architecture pattern discovery" "Codebase structure assessment"
→ Update TodoWrite: Complete previous, mark "Architecture pattern discovery" as in_progress  
```

**Error Handling:**
```
/todo-manager error "exploration gap" "missing dependency analysis"
→ Add TodoWrite task: "Address exploration gap: missing dependency analysis"
```

**Final Completion:**
```
/todo-manager final "codebase exploration" completed
→ Update TodoWrite: Complete all codebase exploration tasks
```
