# Document Workflow Enforcement Module

## WORKFLOW OBLIGATORIO DOCUMENTOS

### ENFORCEMENT TOTAL - NO EXCEPCIONES PERMITIDAS

1. **`/create-doc`** - Content Specialist deployment (NUNCA crear documentos directamente)
2. **`/align-doc`** - Architecture Validator deployment (OBLIGATORIO architecture validation)
3. **`/verify-doc`** - Quality Assurance deployment (OBLIGATORIO quality gates)

**Auto-chaining**: Workflow secuencial automático con confirmación usuario.
**Violation**: Crear documentos fuera de este workflow está PROHIBIDO.

## ENFORCEMENT MECHANISM - ACTIVE BLOCKING

### PRE-EXECUTION VALIDATION REQUIRED

Antes de CUALQUIER operación Write/MultiEdit/NotebookEdit para archivos .md:

```
IF (operation == Write/MultiEdit/NotebookEdit/Edit AND file_extension == .md) {
    IF (current_context NOT IN ["/create-doc workflow", "/edit-doc workflow"]) {
        BLOCK_OPERATION()
        LOG_VIOLATION(user_request, attempted_file, timestamp, operation_type)
        IF (file_exists) {
            REDIRECT_TO_EDIT_WORKFLOW()
        } ELSE {
            REDIRECT_TO_CREATE_WORKFLOW()
        }
        RETURN enforcement_message
    }
}
```

### BLOCKING CONDITIONS
- Direct Write operations to .md files outside approved workflows
- MultiEdit operations to .md files outside workflow
- Edit operations to .md files outside `/edit-doc` workflow
- Any document creation bypassing `/create-doc`
- Any document editing bypassing `/edit-doc`
- Commands attempting direct file creation or modification

### REDIRECTION PROTOCOL

#### For New Document Creation
```
VIOLATION DETECTED: Direct document creation attempted

REQUIRED RESEARCH-FIRST CREATE WORKFLOW:
1. RESEARCH PHASE: WebSearch + MCP Context7 con fecha $(date)
2. Execute `/create-doc [document_type] [description]`
3. System auto-chains to `/align-doc` for validation
4. System auto-chains to `/verify-doc` for quality gates

Redirecting to research-first `/create-doc`...
```

#### For Existing Document Editing
```
VIOLATION DETECTED: Direct document editing attempted

REQUIRED RESEARCH-FIRST EDIT WORKFLOW:
1. RESEARCH PHASE: WebSearch + MCP Context7 con fecha $(date)
2. Execute `/edit-doc [file_path] [edit_description]`
3. System auto-chains to `/align-edit` for validation
4. System auto-chains to `/verify-edit` for quality gates

Redirecting to research-first `/edit-doc`...
```

#### Universal Enforcement
```
ENFORCEMENT: All .md file operations MUST follow approved workflows.
USER VOICE PRESERVED: Your content will be captured and processed through proper workflow.
CHOICE AUTOMATIC: System detects file existence and routes to appropriate workflow.
```

## VIOLATION LOGGING
- Track all bypass attempts in `/data/workflow-violations/`
- Record: timestamp, user_request, attempted_file, violation_type, operation_type
- Generate compliance reports for system optimization
- Pattern analysis for both create and edit workflow improvements
- Separate tracking for creation vs edit violations

## ENFORCEMENT EXCEPTIONS
- System-generated files during workflow execution
- Approved architectural modifications
- Emergency system maintenance (requires explicit override)

## COMPLIANCE VERIFICATION
- Real-time workflow adherence monitoring
- Automated compliance scoring
- Violation trend analysis
- User guidance optimization based on common violations

## ENFORCEMENT INTEGRATION
- **CREATE WORKFLOW**: `/create-doc`, `/align-doc`, `/verify-doc` fully operational
- **EDIT WORKFLOW**: `/edit-doc`, `/align-edit`, `/verify-edit` fully operational  
- **MAINTENANCE WORKFLOW**: `/maintain-docs` for proactive document health
- Violation logging active in `/data/workflow-violations/`
- Auto-redirection messages provide clear user guidance
- System preserves user voice while enforcing proper workflow
- Intelligent routing based on file existence (create vs edit)
- Emergency override available for system maintenance only

## ENFORCEMENT STATUS: ✅ ACTIVE - ENHANCED WITH EDIT WORKFLOW
All .md file operations validated pre-execution with intelligent routing:
- **NEW FILES**: Auto-redirect to `/create-doc` workflow
- **EXISTING FILES**: Auto-redirect to `/edit-doc` workflow  
- **MAINTENANCE**: `/maintain-docs` for proactive document health
- **COMPLETE COVERAGE**: Create, Edit, and Maintenance workflows fully integrated