# Sacred User Space Protection Protocols

**Date**: 2025-07-26 | **Type**: Conditional Rule | **Authority**: CLAUDE_RULES.md Perpetual Rule #4 | **Status**: Active Protection System

## Rule Purpose

Provides technical enforcement protocols for absolute protection of Sacred User Space (user-input/ directory) against any accidental or intentional modifications during system operations, ensuring 100% preservation of user vision authority.

## Trigger Conditions

**ACTIVATE when ANY of these operations detected**:
- File system operations targeting user-input/ directory
- Read/Write/Edit tool invocations with user-input/ paths
- Task Tool deployments that might access user-input/ content
- Git operations affecting user-input/ files
- Batch operations or automated scripts touching user-input/

## Protection Protocols

### 1. Pre-Operation Validation (BLOCKING)
**BEFORE any tool invocation**:
- Scan all file paths for user-input/ references
- Validate operation type (READ allowed, WRITE/EDIT blocked)
- Confirm Sacred User Space protection requirements
- Block progression if modification risk detected

### 2. Operation Monitoring (REAL-TIME)
**DURING any system operation**:
- Monitor file system access patterns
- Track all tool invocations and path targets
- Detect unauthorized user-input/ access attempts
- Trigger immediate termination if violations detected

### 3. Violation Response (IMMEDIATE)
**IF user-input/ modification attempted**:
1. **IMMEDIATE STOP**: Terminate current operation immediately
2. **ROLLBACK**: Restore any modified user-input/ files to original state
3. **ALERT**: Report violation with specific operation details
4. **BLOCK**: Prevent continuation until violation resolved
5. **AUDIT**: Log incident for system improvement

## Authorized Operations

### ✅ ALLOWED Operations
- **READ operations**: Reading user-input/ files for reference and authority validation
- **REFERENCE operations**: Creating cross-references (@user-input/file.md patterns)
- **AUTHORITY validation**: Checking compliance with user vision and requirements
- **INTEGRATION**: Incorporating user-input/ guidance into implementation planning

### 🛑 BLOCKED Operations  
- **WRITE operations**: Creating new files in user-input/ directory
- **EDIT operations**: Modifying existing user-input/ file content
- **DELETE operations**: Removing user-input/ files or directories
- **MOVE operations**: Relocating user-input/ files or changing structure
- **METADATA changes**: Altering user-input/ file permissions or attributes

## Technical Implementation

### File Path Detection
```bash
# Pattern matching for user-input/ protection
if [file_path contains "user-input/"]:
    if [operation_type in ["WRITE", "EDIT", "DELETE", "MOVE"]]:
        BLOCK_OPERATION()
        TRIGGER_VIOLATION_RESPONSE()
    else:
        ALLOW_READ_ONLY()
```

### Tool Integration Protocols
- **Read Tool**: Monitor file_path parameter for user-input/ references
- **Write Tool**: Block if file_path targets user-input/ directory
- **Edit Tool**: Block if file_path targets user-input/ files
- **MultiEdit Tool**: Scan all edit operations for user-input/ violations
- **Task Tool**: Validate sub-agent operations don't target user-input/

### Authority Reference Patterns
**CORRECT referencing approach**:
```markdown
**Authority**: [user-input/vision/core-mission-concept.md](user-input/vision/core-mission-concept.md)
**User Requirements**: See user-input/technical-requirements/technical-architecture-user.md
**Sacred User Space**: user-input/ directory maintains absolute authority
```

## Violation Examples & Responses

### Example 1: Accidental Edit Attempt
**Violation**: `Edit(file_path="/Users/nalve/ce-simple/user-input/vision/core-mission-concept.md", ...)`
**Response**: IMMEDIATE BLOCK → "VIOLATION: Sacred User Space modification attempted. Operation terminated. User-input/ files are read-only for reference purposes only."

### Example 2: Batch Operation Risk
**Violation**: Task Tool deployment with broad file modification scope including user-input/
**Response**: PRE-EMPTIVE BLOCK → "VIOLATION PREVENTION: Operation scope includes Sacred User Space. Modify operation to exclude user-input/ directory before proceeding."

### Example 3: Template Application Overreach
**Violation**: Template compliance automation targeting user-input/ files
**Response**: SELECTIVE BLOCK → "PROTECTION ACTIVE: Template compliance skipped for Sacred User Space. User-input/ files maintain original structure by design."

## Integration with System Rules

### Authority Hierarchy Enforcement
- Maintains user-input/ as ABSOLUTE AUTHORITY (Level 1)
- Prevents authority inversion through technical protection
- Ensures user vision remains uncompromised source of truth

### Quality Gate Integration
- Sacred User Space protection is mandatory quality gate
- All operations must pass user-input/ protection validation
- No exceptions or overrides permitted for protection protocols

### Error Recovery Protocols
- Automated rollback capability for any user-input/ modifications
- Git-based recovery with timestamp preservation
- Comprehensive audit trail for protection system validation

## Maintenance & Evolution

### Protection System Updates
- Protection protocols evolve only through user-input/ authority
- Technical implementation updates require user vision alignment
- No automated changes to protection system without explicit user approval

### Monitoring & Reporting
- Regular audits of protection system effectiveness
- Incident reporting with improvement recommendations
- User notification of protection system status and any attempted violations

---

**Protection Guarantee**: Sacred User Space (user-input/) maintains 100% integrity through technical enforcement preventing any unauthorized modifications while enabling authorized reference and authority validation operations.