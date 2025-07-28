# Workflow Enforcement Utility

## ENFORCEMENT PROTOCOL

**CRITICAL**: This utility implements the obligatory document workflow enforcement mechanism.

### PRE-EXECUTION VALIDATION

Before ANY Write/MultiEdit/NotebookEdit operation for .md files:

```pseudocode
FUNCTION validate_document_operation(operation, file_path, context):
    IF file_extension(file_path) == ".md":
        IF context != "create-doc-workflow" AND context != "system-maintenance":
            log_violation(operation, file_path, get_timestamp())
            return BLOCK_WITH_REDIRECT
    RETURN ALLOW
```

### VIOLATION HANDLING

**BLOCKING MESSAGE:**
```
🚫 WORKFLOW ENFORCEMENT ACTIVE

Direct document creation detected. Required workflow:

1. `/create-doc [type] [description]` - Content Specialist deployment
2. `/align-doc` - Architecture validation (auto-chains)  
3. `/verify-doc` - Quality assurance (auto-chains)

Your content will be preserved and processed through proper workflow.

Execute `/create-doc` to continue with your document creation.
```

### VIOLATION LOGGING

Log to: `/data/workflow-violations/violations-[YYYY-MM-DD].json`

```json
{
  "timestamp": "ISO-8601",
  "violation_type": "DIRECT_WRITE|DIRECT_MULTIEDIT|BYPASS_WORKFLOW",
  "user_request": "original request text",
  "attempted_file": "file path",
  "blocked_operation": "Write|MultiEdit|NotebookEdit", 
  "redirect_message_shown": true,
  "user_guided_to_workflow": true
}
```

### COMPLIANCE TRACKING

**Real-time Metrics:**
- Total document operations attempted
- Violations blocked and redirected
- Successful workflow completions
- Current compliance score (%)

**Pattern Analysis:**
- Most common violation types
- Peak violation periods
- User guidance effectiveness
- Workflow optimization opportunities

### ENFORCEMENT EXCEPTIONS

**ALLOWED WITHOUT WORKFLOW:**
- System-generated files during workflow execution
- Emergency system maintenance (explicit override required)
- Approved architectural modifications (documented)

**BLOCKED OPERATIONS:**
- Direct Write to .md files
- Direct MultiEdit to .md files  
- Document creation bypassing `/create-doc`
- Workflow step skipping

### INTEGRATION POINTS

**Commands Integration:**
- `/create-doc` - Sets workflow context flag
- `/align-doc` - Validates within workflow context
- `/verify-doc` - Completes workflow with context reset

**Error Recovery:**
- Clear user guidance on proper workflow
- Content preservation during redirection
- Automatic workflow initiation when possible

### SYSTEM STATUS

**✅ ENFORCEMENT ACTIVE**
- Pre-execution validation enabled
- Violation blocking operational
- User redirection functional
- Compliance logging active
- Pattern analysis running

## MAINTENANCE

**Override Protocol:** Emergency system maintenance requires explicit override flag in context.
**Updates:** All enforcement logic updates must preserve user voice as absolute source of truth.
**Monitoring:** Continuous compliance monitoring ensures 100% workflow adherence.