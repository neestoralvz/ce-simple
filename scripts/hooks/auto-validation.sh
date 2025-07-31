#!/bin/bash

# Auto Validation Hook - Phase 1 Implementation
# Claude Code PreToolUse hook wrapper for automatic validation before operations  
# Integrates with existing validation scripts and coordination system

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/logs/auto-validation.log"
VALIDATION_SCRIPT="$PROJECT_ROOT/scripts/validation/validate_integrity.sh"
QUICK_VALIDATE="$PROJECT_ROOT/scripts/quick_validate.sh"
COORDINATION_HUB="$PROJECT_ROOT/scripts/automation/coordination-hub.sh"

# Logging functions
log_info() { echo "[$(date '+%H:%M:%S')] 🔍 $1" | tee -a "$LOG_FILE"; }
log_success() { echo "[$(date '+%H:%M:%S')] ✅ $1" | tee -a "$LOG_FILE"; }
log_warning() { echo "[$(date '+%H:%M:%S')] ⚠️ $1" | tee -a "$LOG_FILE"; }
log_error() { echo "[$(date '+%H:%M:%S')] ❌ $1" | tee -a "$LOG_FILE"; }

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

log_info "Auto-validation hook triggered by Claude Code PreToolUse event"

# Get tool context from Claude Code environment
TOOL_NAME="${CLAUDE_TOOL_NAME:-${1:-unknown}}"
TARGET_FILE="${CLAUDE_TARGET_FILE:-${2:-}}"
OPERATION_TYPE="${CLAUDE_OPERATION_TYPE:-${3:-general}}"

log_info "Tool: $TOOL_NAME, Target: $TARGET_FILE, Operation: $OPERATION_TYPE"

# Coordinate with automation system
if [[ -x "$COORDINATION_HUB" ]]; then
    log_info "Registering pre-tool validation event with coordination hub"
    "$COORDINATION_HUB" event "pre_tool_validation" "$TOOL_NAME:$TARGET_FILE" "low" &
fi

# Strategy 1: Quick validation for most operations
if [[ -x "$QUICK_VALIDATE" ]]; then
    log_info "Running quick validation checks"
    
    if "$QUICK_VALIDATE" 2>/dev/null; then
        log_success "Quick validation passed"
        validation_result="success"
    else
        log_warning "Quick validation detected issues"
        validation_result="warning"
    fi
else
    log_warning "Quick validation script not available"
    validation_result="unavailable"
fi

# Strategy 2: Enhanced validation for critical operations
case "$TOOL_NAME" in
    "Write"|"MultiEdit"|"Edit")
        if [[ -n "$TARGET_FILE" && "$TARGET_FILE" =~ \.(md|sh)$ ]]; then
            log_info "Critical file operation detected, running enhanced validation"
            
            # Check if target file would violate size constraints
            if [[ -f "$TARGET_FILE" ]]; then
                line_count=$(wc -l < "$TARGET_FILE" 2>/dev/null || echo "0")
                if [[ $line_count -gt 70 ]]; then
                    log_warning "Target file approaching size limit: $line_count lines"
                    log_warning "Consider L2-modular extraction before editing"
                fi
            fi
            
            # Run integrity validation for critical files
            if [[ -x "$VALIDATION_SCRIPT" ]]; then
                log_info "Running integrity validation"
                if "$VALIDATION_SCRIPT" --quiet 2>/dev/null; then
                    log_success "Integrity validation passed"
                else
                    log_warning "Integrity validation found issues (not blocking)"
                fi
            fi
        fi
        ;;
    "Bash")
        log_info "Script execution detected, verifying project context"
        # Basic safety check for script execution
        if [[ -n "$TARGET_FILE" && ! "$TARGET_FILE" =~ ^/Users/nalve/ce-simple/ ]]; then
            log_error "Script execution outside project root detected"
            log_error "Blocked for security: $TARGET_FILE"
            exit 1
        fi
        ;;
    *)
        log_info "Standard validation for tool: $TOOL_NAME"
        ;;
esac

# Report validation status
case "$validation_result" in
    "success")
        log_success "Pre-tool validation completed successfully"
        exit 0
        ;;
    "warning")
        log_warning "Pre-tool validation completed with warnings (proceeding)"
        exit 0
        ;;
    "unavailable")
        log_warning "Validation tools unavailable (proceeding without validation)"
        exit 0
        ;;
    *)
        log_info "Validation status: $validation_result"
        exit 0
        ;;
esac