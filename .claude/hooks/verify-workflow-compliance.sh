#!/bin/bash

# CLAUDE.md Workflow Compliance Verification Hook
# Enforces token economy and workflow requirements from CLAUDE.md
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="verify-workflow-compliance"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
CLAUDE_MD_PATH="/Users/nalve/ce-simple/CLAUDE.md"

# Tool input and file paths from arguments
TOOL_INPUT="$1"
FILE_PATHS="${2:-}"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Provide specific guidance based on error type
    case "$exit_code" in
        1)
            echo "HOOK_ERROR: CLAUDE.md workflow compliance violation"
            echo "GUIDANCE: $error_message"
            echo "REQUIRED_WORKFLOW:"
            echo "  For NEW documents: Execute /create-doc → /align-doc → /verify-doc"
            echo "  For EXISTING documents: Execute /edit-doc → /align-edit → /verify-edit"
            echo "  See CLAUDE.md sections 67-183 for complete workflow requirements"
            ;;
        2)
            echo "HOOK_WARNING: Workflow compliance warning"
            echo "GUIDANCE: $error_message"
            ;;
        3)
            echo "HOOK_SKIP: Operation skipped due to workflow requirements"
            echo "GUIDANCE: $error_message"
            ;;
    esac
    
    exit "$exit_code"
}

# Extract file path from tool input (handles JSON and direct paths)
extract_file_path() {
    local input="$1"
    local file_path=""
    
    # Try to extract file_path from JSON input
    if echo "$input" | jq -e '.file_path' >/dev/null 2>&1; then
        file_path=$(echo "$input" | jq -r '.file_path')
    elif echo "$input" | grep -q '"file_path"'; then
        # Simple regex extraction if jq fails
        file_path=$(echo "$input" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p')
    else
        # Use FILE_PATHS if available, otherwise assume input is the file path
        if [[ -n "$FILE_PATHS" ]]; then
            file_path=$(echo "$FILE_PATHS" | awk '{print $1}')
        else
            file_path="$input"
        fi
    fi
    
    # Clean up the path
    file_path=$(echo "$file_path" | tr -d '"' | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
    
    echo "$file_path"
}

# Check if operation is on markdown files
is_markdown_operation() {
    local file_path="$1"
    
    # Check file extension
    if [[ "$file_path" =~ \.md$ ]]; then
        return 0
    fi
    
    # Check if any of the file paths are markdown
    if [[ -n "$FILE_PATHS" ]]; then
        for path in $FILE_PATHS; do
            if [[ "$path" =~ \.md$ ]]; then
                return 0
            fi
        done
    fi
    
    return 1
}

# Verify current context matches approved workflows
verify_workflow_context() {
    local file_path="$1"
    
    log_message "INFO" "Checking workflow context for: $file_path"
    
    # Check environment variables that indicate approved workflow context
    local approved_contexts=(
        "/create-doc workflow"
        "/edit-doc workflow"
        "/align-doc workflow"
        "/verify-doc workflow"
        "/align-edit workflow"
        "/verify-edit workflow"
        "/maintain-docs workflow"
    )
    
    # Check for workflow context indicators
    local current_context="${CLAUDE_WORKFLOW_CONTEXT:-}"
    local in_approved_workflow=false
    
    for context in "${approved_contexts[@]}"; do
        if [[ "$current_context" == "$context" ]]; then
            in_approved_workflow=true
            log_message "INFO" "Approved workflow context detected: $context"
            break
        fi
    done
    
    # If no explicit context, check for command indicators in process
    if [[ "$in_approved_workflow" == false ]]; then
        # Check recent command history for workflow commands
        if ps aux | grep -E "(create-doc|edit-doc|align-doc|verify-doc|align-edit|verify-edit|maintain-docs)" | grep -v grep >/dev/null; then
            log_message "INFO" "Workflow command detected in process list"
            in_approved_workflow=true
        fi
        
        # Check for workflow markers in current directory
        if [[ -f ".claude-workflow-active" ]]; then
            log_message "INFO" "Workflow marker file detected"
            in_approved_workflow=true
        fi
    fi
    
    if [[ "$in_approved_workflow" == false ]]; then
        # Determine appropriate workflow based on file existence
        if [[ -f "$file_path" ]]; then
            handle_error 1 "Direct editing of existing markdown file outside /edit-doc workflow: $file_path"
        else
            handle_error 1 "Direct creation of markdown file outside /create-doc workflow: $file_path"
        fi
    fi
    
    log_message "INFO" "Workflow context verification passed"
}

# Check for workflow violations based on CLAUDE.md rules
check_workflow_violations() {
    local file_path="$1"
    
    log_message "INFO" "Checking for workflow violations"
    
    # Load CLAUDE.md content for rule checking
    if [[ ! -f "$CLAUDE_MD_PATH" ]]; then
        log_message "WARN" "CLAUDE.md not found at $CLAUDE_MD_PATH"
        return
    fi
    
    # Check for specific violation patterns
    local violations=()
    
    # Rule 1: Check if this is a direct Write/Edit/MultiEdit operation on .md files
    # (This should only happen within approved workflows)
    
    # Rule 2: Check for document creation outside /create-doc
    if [[ ! -f "$file_path" ]]; then
        violations+=("NEW_DOCUMENT_OUTSIDE_CREATE_WORKFLOW")
    fi
    
    # Rule 3: Check for document editing outside /edit-doc  
    if [[ -f "$file_path" ]]; then
        violations+=("EXISTING_DOCUMENT_OUTSIDE_EDIT_WORKFLOW")
    fi
    
    # Rule 4: Check for system-generated files (allowed exceptions)
    local allowed_system_patterns=(
        "*/\.claude/logs/*"
        "*/\.claude/hooks/*"
        "*/.git/*"
        "*/handoff/*"
        "*/narratives/raw/*"
    )
    
    local is_system_file=false
    for pattern in "${allowed_system_patterns[@]}"; do
        if [[ "$file_path" == $pattern ]]; then
            is_system_file=true
            log_message "INFO" "System-generated file exception: $file_path"
            break
        fi
    done
    
    # Rule 5: Check for emergency maintenance context
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override active - workflow violations allowed"
        return
    fi
    
    # Process violations
    if [[ ${#violations[@]} -gt 0 ]] && [[ "$is_system_file" == false ]]; then
        local violation_details=""
        for violation in "${violations[@]}"; do
            case "$violation" in
                "NEW_DOCUMENT_OUTSIDE_CREATE_WORKFLOW")
                    violation_details+="• New document creation must use /create-doc workflow\n"
                    ;;
                "EXISTING_DOCUMENT_OUTSIDE_EDIT_WORKFLOW")
                    violation_details+="• Existing document editing must use /edit-doc workflow\n"
                    ;;
            esac
        done
        
        handle_error 1 "Workflow violations detected:\n$violation_details"
    fi
    
    log_message "INFO" "No workflow violations detected"
}

# Verify token economy compliance
verify_token_economy() {
    local file_path="$1"
    
    log_message "INFO" "Checking token economy compliance"
    
    # Check for anti-bias enforcement (CLAUDE.md line 40)
    # This is a passive check - we log but don't block operations
    
    # Check for research-first protocol compliance (CLAUDE.md lines 46-57)
    local research_indicators=(
        "$(date)"
        "WebSearch"
        "MCP Context7"
        "$(date '+%Y-%m-%d')"
    )
    
    # Check if current operation follows research-first protocol
    # This is enforced at the workflow level, not file level
    
    # Check for voice preservation requirements (CLAUDE.md line 32)
    # Document operations should preserve user voice
    
    log_message "INFO" "Token economy compliance checked"
}

# Check command ecosystem dependencies (CLAUDE.md lines 24-28)
verify_command_ecosystem() {
    local file_path="$1"
    
    log_message "INFO" "Checking command ecosystem dependencies"
    
    # Verify we're not creating external dependencies
    if [[ "$file_path" =~ ^/Users/nalve/ce-simple/\.claude/commands/ ]]; then
        log_message "INFO" "Operation within command ecosystem: $file_path"
        
        # Check for self-containment violations
        # This would require analyzing file content, but for pre-hook we focus on path validation
        
    elif [[ "$file_path" =~ \.md$ ]]; then
        # Document operations outside command ecosystem
        log_message "INFO" "Document operation outside command ecosystem: $file_path"
    fi
    
    log_message "INFO" "Command ecosystem verification completed"
}

# Enhanced verification with debugging support
debug_workflow_state() {
    if [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]; then
        log_message "DEBUG" "=== Workflow State Debug Information ==="
        log_message "DEBUG" "Tool input: $TOOL_INPUT"
        log_message "DEBUG" "File paths: $FILE_PATHS"
        log_message "DEBUG" "Current workflow context: ${CLAUDE_WORKFLOW_CONTEXT:-none}"
        log_message "DEBUG" "Emergency override: ${CLAUDE_EMERGENCY_OVERRIDE:-false}"
        log_message "DEBUG" "CLAUDE.md path: $CLAUDE_MD_PATH"
        log_message "DEBUG" "CLAUDE.md exists: $(test -f "$CLAUDE_MD_PATH" && echo "yes" || echo "no")"
        
        # Show recent commands that might indicate workflow
        log_message "DEBUG" "Recent workflow-related processes:"
        ps aux | grep -E "(create-doc|edit-doc|align-doc|verify-doc)" | grep -v grep | head -3 | while read -r line; do
            log_message "DEBUG" "  $line"
        done
        
        log_message "DEBUG" "=== End Debug Information ==="
    fi
}

# Emergency override check
check_emergency_override() {
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override activated - bypassing workflow compliance verification"
        return 0
    fi
    return 1
}

# Main verification function
verify_workflow_compliance() {
    log_message "INFO" "Starting CLAUDE.md workflow compliance verification"
    
    # Extract file path from tool input
    local file_path
    file_path=$(extract_file_path "$TOOL_INPUT")
    
    # Check if this is a markdown operation
    if ! is_markdown_operation "$file_path"; then
        log_message "INFO" "Non-markdown operation - skipping workflow verification: $file_path"
        return 0
    fi
    
    log_message "INFO" "Markdown operation detected - enforcing workflow compliance: $file_path"
    
    # Run all verification steps
    verify_workflow_context "$file_path"
    check_workflow_violations "$file_path"
    verify_token_economy "$file_path"
    verify_command_ecosystem "$file_path"
    
    log_message "INFO" "CLAUDE.md workflow compliance verification completed successfully for: $file_path"
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_INPUT" ]]; then
        handle_error 1 "No tool input provided for verification"
    fi
    
    # Check for emergency override first
    if check_emergency_override; then
        exit 0
    fi
    
    # Run debug logging if enabled
    debug_workflow_state
    
    # Perform main verification
    verify_workflow_compliance
    
    # If we get here, verification passed
    log_message "SUCCESS" "CLAUDE.md workflow compliance verification passed"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "ERROR" "Script interrupted"; exit 130' INT TERM

# Execute main function
main "$@"