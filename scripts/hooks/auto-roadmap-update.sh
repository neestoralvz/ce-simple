#!/bin/bash

# Auto Roadmap Update Hook - Phase 1 Implementation  
# Claude Code Stop hook wrapper for automatic roadmap synchronization
# Integrates with existing post-conversation-coordinated.hook functionality

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
LOG_FILE="$PROJECT_ROOT/.claude/hooks/logs/auto-roadmap-update.log"
POST_CONVERSATION_HOOK="$PROJECT_ROOT/.claude/hooks/post-conversation-coordinated.hook"
ROADMAP_UPDATE_SCRIPT="$PROJECT_ROOT/scripts/integration/roadmap-update.sh"

# Logging functions
log_info() { echo "[$(date '+%H:%M:%S')] 📊 $1" | tee -a "$LOG_FILE"; }
log_success() { echo "[$(date '+%H:%M:%S')] ✅ $1" | tee -a "$LOG_FILE"; }
log_warning() { echo "[$(date '+%H:%M:%S')] ⚠️ $1" | tee -a "$LOG_FILE"; }
log_error() { echo "[$(date '+%H:%M:%S')] ❌ $1" | tee -a "$LOG_FILE"; }

# Ensure log directory exists
mkdir -p "$(dirname "$LOG_FILE")"

log_info "Auto-roadmap-update hook triggered by Claude Code Stop event"

# Get conversation context from Claude Code environment
CONVERSATION_ID="${CLAUDE_CONVERSATION_ID:-$(date +%s)}"
FILES_MODIFIED="${CLAUDE_FILES_MODIFIED:-0}"
CONVERSATION_SUMMARY="${CLAUDE_CONVERSATION_SUMMARY:-'Conversation completed'}"

log_info "Conversation ID: $CONVERSATION_ID, Files modified: $FILES_MODIFIED"

# Strategy 1: Use existing post-conversation coordinated hook
if [[ -x "$POST_CONVERSATION_HOOK" ]]; then
    log_info "Delegating to coordinated post-conversation hook for comprehensive updates"
    
    # Set environment for coordinated execution
    export CLAUDE_CONVERSATION_ID="$CONVERSATION_ID"
    export CLAUDE_FILES_MODIFIED="$FILES_MODIFIED"
    export CLAUDE_CONVERSATION_SUMMARY="$CONVERSATION_SUMMARY"
    
    # Execute the existing sophisticated post-conversation hook
    if "$POST_CONVERSATION_HOOK"; then
        log_success "Coordinated post-conversation hook completed (includes roadmap sync)"
    else
        log_warning "Coordinated post-conversation hook encountered issues, trying direct roadmap update"
        
        # Fallback to direct roadmap update
        if [[ -x "$ROADMAP_UPDATE_SCRIPT" ]]; then
            log_info "Executing direct coordinated roadmap update"
            "$ROADMAP_UPDATE_SCRIPT" --coordinated
            log_success "Direct roadmap update completed"
        else
            log_error "Direct roadmap update script not available"
        fi
    fi
    
elif [[ -x "$ROADMAP_UPDATE_SCRIPT" ]]; then
    # Strategy 2: Use roadmap update script directly
    log_info "Post-conversation hook not available, using direct roadmap update"
    
    if "$ROADMAP_UPDATE_SCRIPT" --coordinated; then
        log_success "Direct coordinated roadmap update completed"
    else
        log_warning "Coordinated roadmap update failed, trying standard mode"
        
        # Final fallback: standard roadmap update
        if "$ROADMAP_UPDATE_SCRIPT"; then
            log_success "Standard roadmap update completed"
        else
            log_error "All roadmap update attempts failed"
        fi
    fi
    
else
    log_error "No roadmap update mechanisms available"
    log_error "Expected files:"
    log_error "  - $POST_CONVERSATION_HOOK"
    log_error "  - $ROADMAP_UPDATE_SCRIPT"
    log_error "Hook integration incomplete - manual setup required"
    exit 1
fi

# Verify roadmap was updated
if [[ -f "$PROJECT_ROOT/context/roadmap/last_update_report.md" ]]; then
    last_update=$(stat -f "%Sm" -t "%H:%M:%S" "$PROJECT_ROOT/context/roadmap/last_update_report.md" 2>/dev/null || echo "unknown")
    log_success "Roadmap update verified - last update at: $last_update"
else
    log_warning "Could not verify roadmap update - report file not found"
fi

log_info "Auto-roadmap-update hook completed"