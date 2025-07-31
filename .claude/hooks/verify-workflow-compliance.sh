#!/bin/bash

# verify-workflow-compliance.sh - CLAUDE.md Workflow Compliance Hook
# AUTHORITY: CLAUDE.md protocol enforcement + contradiction detection
# Performance: <100ms for PreToolUse hook compliance

set -euo pipefail

# Logging setup
HOOK_LOG="/Users/nalve/ce-simple/.claude/logs/hooks.log"
mkdir -p "$(dirname "$HOOK_LOG")"

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [verify-workflow-compliance] $1" >> "$HOOK_LOG"
}

# Function to extract file path from tool input
extract_file_path() {
    local tool_input="$1"
    
    if echo "$tool_input" | grep -q "file_path"; then
        echo "$tool_input" | grep -o '"file_path":\s*"[^"]*"' | sed 's/"file_path":\s*"//; s/"//'
    else
        echo ""
    fi
}

# Function to validate /core protocol execution
validate_core_protocol() {
    local session_log="/tmp/claude_session_tools.log"
    
    # Check if TodoWrite was used (indicates /core protocol execution)
    if [[ -f "$session_log" ]]; then
        if grep -q "TodoWrite" "$session_log" 2>/dev/null; then
            log_message "✅ /core protocol compliance detected (TodoWrite found)"
            return 0
        fi
    fi
    
    log_message "⚠️ /core protocol may not have been executed (no TodoWrite detected)"
    echo "⚠️ WORKFLOW COMPLIANCE WARNING: /core protocol should be executed first"
    echo "CLAUDE.md requirement: EJECUTA /core OBLIGATORIO como PRIMER paso absoluto SIEMPRE"
    return 2  # Warning, but continue operation
}

# Function to detect reference pattern contradictions
detect_reference_contradictions() {
    local file_path="$1"
    local tool_input="$2"
    
    # Check for mixed @context/ and context/ patterns in the input
    local has_at_context=$(echo "$tool_input" | grep -c "@context/" || echo "0")
    local has_context=$(echo "$tool_input" | grep -c "context/" || echo "0")
    
    if [[ "$has_at_context" -gt 0 ]] && [[ "$has_context" -gt 0 ]]; then
        log_message "❌ Reference pattern contradiction detected in: $file_path"
        echo "❌ REFERENCE CONTRADICTION DETECTED"
        echo "File: $file_path"
        echo "Mixed patterns found: @context/ and context/"
        echo "CLAUDE.md requirement: Consistent reference patterns"
        echo ""
        echo "🤔 USER CONSULTATION REQUIRED:"
        echo "Which reference pattern should be used?"
        echo "A) @context/ pattern"
        echo "B) context/ pattern"
        echo "Please specify your preference for consistent usage."
        return 1
    fi
    
    return 0
}

# Function to validate semantic pattern recognition
validate_semantic_patterns() {
    local file_path="$1"
    local tool_input="$2"
    
    # Check if operating on markdown files in specific patterns
    if [[ "$file_path" == *".md" ]]; then
        local filename=$(basename "$file_path")
        
        # Detect potential semantic pattern misalignment
        case "$filename" in
            *architecture*|*pattern*|*methodology*)
                if ! echo "$tool_input" | grep -q "architecture\|pattern\|methodology"; then
                    log_message "⚠️ Semantic pattern mismatch for: $file_path"
                    echo "⚠️ SEMANTIC PATTERN WARNING"
                    echo "File: $file_path (architecture/pattern content)"
                    echo "Consider loading appropriate context per CLAUDE.md semantic triggers"
                fi
                ;;
            *vision*|*authority*)
                if ! echo "$tool_input" | grep -q "vision\|authority\|user"; then
                    log_message "⚠️ Vision/authority content pattern detected: $file_path"
                    echo "⚠️ AUTHORITY CONTENT DETECTED"
                    echo "File: $file_path (vision/authority content)"
                    echo "Ensure user authority preservation per CLAUDE.md requirements"
                fi
                ;;
        esac
    fi
    
    return 0
}

# Main validation logic
main() {
    local tool_input="${1:-}"
    local file_paths="${2:-}"
    
    log_message "Validating workflow compliance for tool: $CLAUDE_TOOL_NAME"
    
    # Extract file path
    local file_path
    file_path=$(extract_file_path "$tool_input")
    
    if [[ -z "$file_path" ]] && [[ -n "$file_paths" ]]; then
        file_path="$file_paths"
    fi
    
    if [[ -z "$file_path" ]]; then
        log_message "⚠️ No file path found, skipping workflow validation"
        exit 0
    fi
    
    log_message "Validating workflow compliance for: $file_path"
    
    # Validate /core protocol execution
    validate_core_protocol
    
    # Detect reference contradictions
    if ! detect_reference_contradictions "$file_path" "$tool_input"; then
        exit 1  # Block operation for contradiction resolution
    fi
    
    # Validate semantic patterns
    validate_semantic_patterns "$file_path" "$tool_input"
    
    log_message "✅ Workflow compliance validation completed for: $file_path"
    exit 0
}

# Execute main function
main "$@"