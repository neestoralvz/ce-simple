#!/bin/bash

# Auto Git Commit Hook - Phase 1 Implementation
# Claude Code PostToolUse hook wrapper for automatic git commits
# Integrates with existing post-edit-coordinated.hook functionality

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/logs/auto-git-commit.log"
POST_EDIT_HOOK="$PROJECT_ROOT/.claude/hooks/post-edit-coordinated.hook"

# Logging functions
log_info() { echo "[$(date '+%H:%M:%S')] 🔧 $1" | tee -a "$LOG_FILE"; }
log_success() { echo "[$(date '+%H:%M:%S')] ✅ $1" | tee -a "$LOG_FILE"; }
log_warning() { echo "[$(date '+%H:%M:%S')] ⚠️ $1" | tee -a "$LOG_FILE"; }
log_error() { echo "[$(date '+%H:%M:%S')] ❌ $1" | tee -a "$LOG_FILE"; }

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

log_info "Auto-git-commit hook triggered by Claude Code"

# Get tool usage context from Claude Code environment
EDITED_FILE="${CLAUDE_EDITED_FILE:-${1:-}}"
TOOL_NAME="${CLAUDE_TOOL_NAME:-${2:-Edit}}"
TOOL_RESULT="${CLAUDE_TOOL_RESULT:-success}"

if [[ -z "$EDITED_FILE" ]]; then
    log_warning "No edited file specified, checking for recent changes"
    EDITED_FILE=$(git diff --name-only HEAD | head -1 || echo "unknown")
fi

log_info "Processing file: $EDITED_FILE (tool: $TOOL_NAME, result: $TOOL_RESULT)"

# Enable auto-commit for this execution
export CLAUDE_AUTO_COMMIT=true
export CLAUDE_EDIT_TYPE="$TOOL_NAME"
export CLAUDE_LINES_CHANGED="1"

# Check if post-edit hook exists and is executable
if [[ -x "$POST_EDIT_HOOK" ]]; then
    log_info "Delegating to coordinated post-edit hook with auto-commit enabled"
    
    # Execute the existing sophisticated post-edit hook
    if "$POST_EDIT_HOOK" "$EDITED_FILE"; then
        log_success "Coordinated post-edit hook completed successfully"
        
        # Verify commit was created
        if git log --oneline -1 | grep -q "Claude Code"; then
            log_success "Auto-commit completed via coordinated system"
        else
            log_warning "No new commit detected, may indicate no changes or hook disabled"
        fi
    else
        log_error "Coordinated post-edit hook failed"
        
        # Fallback: Simple git commit
        log_info "Attempting fallback simple commit"
        if [[ -n "$EDITED_FILE" && -f "$EDITED_FILE" ]]; then
            git add "$EDITED_FILE" 2>/dev/null || true
            
            commit_msg="Auto-commit: $EDITED_FILE via Claude Code

🔧 Tool: $TOOL_NAME  
📄 File: $EDITED_FILE
🤖 Generated with Claude Code

Co-Authored-By: Claude <noreply@anthropic.com>"
            
            if git commit -m "$commit_msg" 2>/dev/null; then
                log_success "Fallback commit completed"
            else
                log_warning "No changes to commit or commit failed"
            fi
        fi
    fi
else
    log_error "Post-edit coordinated hook not found or not executable: $POST_EDIT_HOOK"
    log_error "Hook integration incomplete - manual setup required"
    exit 1
fi

log_info "Auto-git-commit hook completed"