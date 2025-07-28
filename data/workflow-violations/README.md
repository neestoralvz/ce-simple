# Workflow Violations Logging System

## Purpose
Tracks all attempts to bypass the obligatory document creation workflow: `/create-doc` → `/align-doc` → `/verify-doc`

## Violation Types
- **DIRECT_WRITE**: Attempted Write operation to .md file outside workflow
- **DIRECT_MULTIEDIT**: Attempted MultiEdit operation to .md file outside workflow  
- **BYPASS_CREATE_DOC**: Attempted document creation without `/create-doc`
- **SKIP_ALIGNMENT**: Attempted to skip `/align-doc` validation
- **SKIP_VERIFICATION**: Attempted to skip `/verify-doc` quality gates

## Log Structure
```json
{
  "timestamp": "2025-07-28T12:00:00Z",
  "violation_type": "DIRECT_WRITE",
  "user_request": "Original user request text",
  "attempted_file": "/path/to/file.md",
  "blocked_operation": "Write",
  "redirected_to": "/create-doc",
  "user_guided": true
}
```

## Compliance Tracking
- Real-time adherence monitoring
- Weekly compliance reports
- Violation pattern analysis
- User guidance optimization

## Enforcement Status
✅ **ACTIVE ENFORCEMENT** - All .md operations validated pre-execution