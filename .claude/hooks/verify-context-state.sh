#!/bin/bash

# Context State Verification Hook
# Ensures proper context state before command execution
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="verify-context-state"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
CONTEXT_STATE_FILE="/Users/nalve/ce-simple/.claude/context-state.json"
PROJECT_ROOT="/Users/nalve/ce-simple"

# Tool name from parameters
TOOL_NAME="$1"

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
            echo "HOOK_ERROR: Context state verification failed"
            echo "GUIDANCE: $error_message"
            echo "RESOLUTION: Check system state and context preservation"
            echo "REFERENCE: Ensure proper session continuity and context loading"
            ;;
        2)
            echo "HOOK_WARNING: Context state warning"
            echo "GUIDANCE: $error_message"
            ;;
        3)
            echo "HOOK_SKIP: Operation skipped due to context requirements"
            echo "GUIDANCE: $error_message"
            ;;
    esac
    
    exit "$exit_code"
}

# Initialize context state if it doesn't exist
initialize_context_state() {
    if [[ ! -f "$CONTEXT_STATE_FILE" ]]; then
        log_message "INFO" "Initializing context state file: $CONTEXT_STATE_FILE"
        
        # Create initial context state
        cat > "$CONTEXT_STATE_FILE" << 'EOF'
{
    "session": {
        "id": "",
        "start_time": "",
        "last_activity": "",
        "active": false
    },
    "workflow": {
        "current_command": "",
        "context": "",
        "chain_state": "none",
        "last_operation": ""
    },
    "system": {
        "project_root": "",
        "git_branch": "",
        "git_status": "clean",
        "working_directory": ""
    },
    "context_preservation": {
        "user_voice_captured": false,
        "research_completed": false,
        "subagent_state": "none",
        "handoff_loaded": false
    },
    "performance": {
        "token_economy_score": 0,
        "last_optimization": "",
        "efficiency_metrics": {}
    },
    "last_updated": ""
}
EOF
        
        # Set initial values
        jq --arg project_root "$PROJECT_ROOT" \
           --arg working_dir "$(pwd)" \
           --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
           '.system.project_root = $project_root | 
            .system.working_directory = $working_dir | 
            .last_updated = $timestamp' \
           "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
           mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
    fi
    
    log_message "INFO" "Context state file initialized"
}

# Load current context state
load_context_state() {
    if [[ ! -f "$CONTEXT_STATE_FILE" ]]; then
        initialize_context_state
    fi
    
    # Validate JSON structure
    if ! jq empty "$CONTEXT_STATE_FILE" 2>/dev/null; then
        log_message "WARN" "Invalid context state JSON, reinitializing"
        rm -f "$CONTEXT_STATE_FILE"
        initialize_context_state
    fi
    
    log_message "INFO" "Context state loaded successfully"
}

# Verify session continuity
verify_session_continuity() {
    local tool_name="$1"
    
    log_message "INFO" "Verifying session continuity for tool: $tool_name"
    
    # Check if session is active
    local session_active
    session_active=$(jq -r '.session.active' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "false")
    
    if [[ "$session_active" != "true" ]]; then
        # For critical operations, require active session
        case "$tool_name" in
            "mcp__ide__executeCode"|"WebSearch"|"Write"|"Edit"|"MultiEdit")
                log_message "WARN" "Critical operation attempted without active session"
                handle_error 2 "No active session for critical operation: $tool_name"
                ;;
            *)
                log_message "INFO" "Non-critical operation, session not required: $tool_name"
                ;;
        esac
    fi
    
    # Check session age
    local last_activity
    last_activity=$(jq -r '.session.last_activity' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "")
    
    if [[ -n "$last_activity" ]]; then
        local current_time
        current_time=$(date +%s)
        local last_activity_time
        last_activity_time=$(date -d "$last_activity" +%s 2>/dev/null || echo "0")
        local time_diff=$((current_time - last_activity_time))
        
        # Warn if session is stale (>1 hour)
        if [[ $time_diff -gt 3600 ]]; then
            log_message "WARN" "Session appears stale (last activity: $last_activity)"
            handle_error 2 "Stale session detected - consider session refresh"
        fi
    fi
    
    log_message "INFO" "Session continuity verified"
}

# Check workflow context consistency
verify_workflow_context() {
    local tool_name="$1"
    
    log_message "INFO" "Verifying workflow context consistency"
    
    # Get current workflow state
    local current_command
    local workflow_context
    current_command=$(jq -r '.workflow.current_command' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "")
    workflow_context=$(jq -r '.workflow.context' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "")
    
    # Check for workflow mismatches
    case "$tool_name" in
        "Write"|"Edit"|"MultiEdit")
            if [[ "$workflow_context" =~ \.md$ ]] && [[ "$workflow_context" != *"/create-doc"* ]] && [[ "$workflow_context" != *"/edit-doc"* ]]; then
                log_message "WARN" "Document operation outside approved workflow context"
                handle_error 2 "Document operation context mismatch"
            fi
            ;;
        "mcp__ide__executeCode")
            # Check if notebook context is properly established
            local notebook_context
            notebook_context=$(jq -r '.context_preservation.notebook_state // "unknown"' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "unknown")
            if [[ "$notebook_context" == "unknown" ]]; then
                log_message "WARN" "MCP code execution without established notebook context"
            fi
            ;;
    esac
    
    log_message "INFO" "Workflow context consistency verified"
}

# Verify context preservation state
verify_context_preservation() {
    local tool_name="$1"
    
    log_message "INFO" "Verifying context preservation state"
    
    # Check user voice preservation state
    local user_voice_captured
    user_voice_captured=$(jq -r '.context_preservation.user_voice_captured' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "false")
    
    # For operations that modify system state, ensure user voice is captured
    case "$tool_name" in
        "Write"|"Edit"|"MultiEdit"|"Bash")
            if [[ "$user_voice_captured" != "true" ]]; then
                log_message "WARN" "System modification without captured user voice"
                # Don't block, but log for monitoring
            fi
            ;;
    esac
    
    # Check research completion state
    local research_completed
    research_completed=$(jq -r '.context_preservation.research_completed' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "false")
    
    # For major operations, verify research-first protocol
    case "$tool_name" in
        "WebSearch"|"Task")
            # These tools often initiate research - update state
            jq '.context_preservation.research_completed = true | 
                .last_updated = now | 
                .session.last_activity = now' \
                "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
                mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
            ;;
    esac
    
    log_message "INFO" "Context preservation state verified"
}

# Check system state consistency
verify_system_state() {
    local tool_name="$1"
    
    log_message "INFO" "Verifying system state consistency"
    
    # Check project root consistency
    local stored_project_root
    stored_project_root=$(jq -r '.system.project_root' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "")
    
    if [[ -n "$stored_project_root" ]] && [[ "$stored_project_root" != "$PROJECT_ROOT" ]]; then
        log_message "WARN" "Project root mismatch: stored=$stored_project_root, current=$PROJECT_ROOT"
        # Update project root
        jq --arg project_root "$PROJECT_ROOT" \
           '.system.project_root = $project_root' \
           "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
           mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
    fi
    
    # Check working directory
    local current_dir="$(pwd)"
    local stored_working_dir
    stored_working_dir=$(jq -r '.system.working_directory' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "")
    
    if [[ "$stored_working_dir" != "$current_dir" ]]; then
        log_message "INFO" "Working directory changed: $stored_working_dir -> $current_dir"
        # Update working directory
        jq --arg working_dir "$current_dir" \
           '.system.working_directory = $working_dir' \
           "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
           mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
    fi
    
    # Check git state if in git repository
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
        local current_branch
        current_branch=$(git branch --show-current 2>/dev/null || echo "detached")
        
        local stored_branch
        stored_branch=$(jq -r '.system.git_branch' "$CONTEXT_STATE_FILE" 2>/dev/null || echo "")
        
        if [[ "$stored_branch" != "$current_branch" ]]; then
            log_message "INFO" "Git branch changed: $stored_branch -> $current_branch"
            # Update git branch
            jq --arg branch "$current_branch" \
               '.system.git_branch = $branch' \
               "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
               mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
        fi
    fi
    
    log_message "INFO" "System state consistency verified"
}

# Update context state based on tool usage
update_context_state() {
    local tool_name="$1"
    
    log_message "INFO" "Updating context state for tool: $tool_name"
    
    # Update last operation and timestamp
    jq --arg tool_name "$tool_name" \
       --arg timestamp "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
       '.workflow.last_operation = $tool_name | 
        .last_updated = $timestamp | 
        .session.last_activity = $timestamp' \
       "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
       mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
    
    # Tool-specific state updates
    case "$tool_name" in
        "WebSearch")
            jq '.context_preservation.research_completed = true' \
               "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
               mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
            ;;
        "Task")
            jq '.context_preservation.subagent_state = "active"' \
               "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
               mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
            ;;
        "Write"|"Edit"|"MultiEdit")
            jq '.workflow.chain_state = "document_operation"' \
               "$CONTEXT_STATE_FILE" > "${CONTEXT_STATE_FILE}.tmp" && \
               mv "${CONTEXT_STATE_FILE}.tmp" "$CONTEXT_STATE_FILE"
            ;;
    esac
    
    log_message "INFO" "Context state updated successfully"
}

# Enhanced verification with debugging support
debug_context_state() {
    if [[ "${CLAUDE_DEBUG_HOOKS:-false}" == "true" ]]; then
        log_message "DEBUG" "=== Context State Debug Information ==="
        log_message "DEBUG" "Tool name: $TOOL_NAME"
        log_message "DEBUG" "Context state file: $CONTEXT_STATE_FILE"
        log_message "DEBUG" "Context state exists: $(test -f "$CONTEXT_STATE_FILE" && echo "yes" || echo "no")"
        
        if [[ -f "$CONTEXT_STATE_FILE" ]]; then
            log_message "DEBUG" "Current context state:"
            jq -r 'to_entries[] | "  \(.key): \(.value)"' "$CONTEXT_STATE_FILE" | head -10 | while read -r line; do
                log_message "DEBUG" "$line"
            done
        fi
        
        log_message "DEBUG" "Current working directory: $(pwd)"
        log_message "DEBUG" "Project root: $PROJECT_ROOT"
        log_message "DEBUG" "=== End Debug Information ==="
    fi
}

# Emergency override check
check_emergency_override() {
    if [[ "${CLAUDE_EMERGENCY_OVERRIDE:-false}" == "true" ]]; then
        log_message "WARN" "Emergency override activated - bypassing context state verification"
        return 0
    fi
    return 1
}

# Main verification function
verify_context_state() {
    log_message "INFO" "Starting context state verification for tool: $TOOL_NAME"
    
    # Load current context state
    load_context_state
    
    # Run verification steps
    verify_session_continuity "$TOOL_NAME"
    verify_workflow_context "$TOOL_NAME"
    verify_context_preservation "$TOOL_NAME"
    verify_system_state "$TOOL_NAME"
    
    # Update context state
    update_context_state "$TOOL_NAME"
    
    log_message "INFO" "Context state verification completed successfully for: $TOOL_NAME"
}

# Main execution
main() {
    # Create log directory if it doesn't exist
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$CONTEXT_STATE_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_NAME" ]]; then
        handle_error 1 "No tool name provided for verification"
    fi
    
    # Check for emergency override first
    if check_emergency_override; then
        exit 0
    fi
    
    # Run debug logging if enabled
    debug_context_state
    
    # Perform main verification
    verify_context_state
    
    # If we get here, verification passed
    log_message "SUCCESS" "Context state verification passed for: $TOOL_NAME"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "ERROR" "Script interrupted"; exit 130' INT TERM

# Execute main function
main "$@"