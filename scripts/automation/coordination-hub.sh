#!/bin/bash

# Automation Coordination Hub
# Central coordination system for git hooks, claude hooks, and fswatch automation
# Prevents conflicts and coordinates intelligent updates

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
STATE_DIR="$PROJECT_ROOT/.automation-state"
LOCK_FILE="$STATE_DIR/coordination.lock"
EVENT_QUEUE="$STATE_DIR/event-queue.log"
STATUS_FILE="$STATE_DIR/coordination-status.json"
LOG_FILE="$STATE_DIR/coordination.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Logging functions
log_info() { echo -e "${BLUE}🔧${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_success() { echo -e "${GREEN}✅${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_warning() { echo -e "${YELLOW}⚠️${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_error() { echo -e "${RED}❌${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }

# Initialize state directory
initialize_state() {
    mkdir -p "$STATE_DIR"
    
    # Initialize status file if it doesn't exist
    if [[ ! -f "$STATUS_FILE" ]]; then
        cat > "$STATUS_FILE" << EOF
{
  "coordination_active": true,
  "last_roadmap_update": null,
  "active_operations": [],
  "event_queue_size": 0,
  "startup_time": "$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")"
}
EOF
    fi
    
    # Initialize event queue
    [[ ! -f "$EVENT_QUEUE" ]] && touch "$EVENT_QUEUE"
    
    log_info "Coordination system initialized"
}

# Lock management functions
acquire_lock() {
    local operation="$1"
    local timeout="${2:-30}"
    local wait_time=0
    
    while [[ $wait_time -lt $timeout ]]; do
        if mkdir "$LOCK_FILE" 2>/dev/null; then
            echo "$operation:$$:$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")" > "$LOCK_FILE/operation"
            log_info "Lock acquired for: $operation"
            return 0
        fi
        
        # Check if lock is stale (older than 5 minutes)
        if [[ -f "$LOCK_FILE/operation" ]]; then
            local lock_time=$(stat -f %m "$LOCK_FILE" 2>/dev/null || echo "0")
            local current_time=$(date +%s)
            local age=$((current_time - lock_time))
            
            if [[ $age -gt 300 ]]; then
                log_warning "Removing stale lock (age: ${age}s)"
                rm -rf "$LOCK_FILE"
                continue
            fi
        fi
        
        log_info "Waiting for lock... ($wait_time/${timeout}s)"
        sleep 1
        ((wait_time++))
    done
    
    log_error "Failed to acquire lock for: $operation"
    return 1
}

release_lock() {
    if [[ -d "$LOCK_FILE" ]]; then
        rm -rf "$LOCK_FILE"
        log_info "Lock released"
    fi
}

# Event queue management
queue_event() {
    local event_type="$1"
    local event_data="$2"
    local priority="${3:-normal}"
    
    local event_json=$(cat <<EOF
{
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")",
  "type": "$event_type",
  "data": "$event_data",
  "priority": "$priority",
  "status": "queued"
}
EOF
)
    
    echo "$event_json" >> "$EVENT_QUEUE"
    update_status "event_queue_size" "$(wc -l < "$EVENT_QUEUE" | tr -d ' ')"
    log_info "Event queued: $event_type ($priority priority)"
}

process_event_queue() {
    local batch_size="${1:-5}"
    local processed=0
    
    if [[ ! -f "$EVENT_QUEUE" || ! -s "$EVENT_QUEUE" ]]; then
        return 0
    fi
    
    log_info "Processing event queue (batch size: $batch_size)"
    
    # Process events in FIFO order
    local temp_queue=$(mktemp)
    local temp_processing=$(mktemp)
    trap "rm -f '$temp_queue' '$temp_processing'" EXIT
    
    # Take first batch_size events
    head -n "$batch_size" "$EVENT_QUEUE" > "$temp_processing"
    tail -n +$((batch_size + 1)) "$EVENT_QUEUE" > "$temp_queue" || true
    
    # Process each event
    while IFS= read -r event_json && [[ $processed -lt $batch_size ]]; do
        if [[ -n "$event_json" ]]; then
            process_single_event "$event_json"
            ((processed++))
        fi
    done < "$temp_processing"
    
    # Update queue file
    mv "$temp_queue" "$EVENT_QUEUE"
    update_status "event_queue_size" "$(wc -l < "$EVENT_QUEUE" | tr -d ' ')"
    
    log_success "Processed $processed events"
    return $processed
}

process_single_event() {
    local event_json="$1"
    local event_type=$(echo "$event_json" | jq -r '.type // "unknown"')
    local event_data=$(echo "$event_json" | jq -r '.data // ""')
    
    log_info "Processing event: $event_type"
    
    case "$event_type" in
        "roadmap_update")
            coordinate_roadmap_update "$event_data"
            ;;
        "file_change")
            coordinate_file_change "$event_data"
            ;;
        "git_commit")
            coordinate_git_commit "$event_data"
            ;;
        "claude_conversation")
            coordinate_claude_conversation "$event_data"
            ;;
        *)
            log_warning "Unknown event type: $event_type"
            ;;
    esac
}

# Coordination functions
coordinate_roadmap_update() {
    local trigger_source="$1"
    
    if acquire_lock "roadmap_update" 60; then
        log_info "Coordinating roadmap update (triggered by: $trigger_source)"
        
        # Check if roadmap update is needed
        if should_update_roadmap; then
            # Execute roadmap update with coordination awareness
            if "$PROJECT_ROOT/scripts/integration/roadmap-update.sh" --coordinated; then
                update_status "last_roadmap_update" "$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")"
                log_success "Roadmap update completed"
            else
                log_error "Roadmap update failed"
            fi
        else
            log_info "Roadmap update not needed"
        fi
        
        release_lock
    else
        # Re-queue with lower priority if lock acquisition fails
        queue_event "roadmap_update" "$trigger_source" "low"
        log_warning "Roadmap update re-queued due to lock timeout"
    fi
}

coordinate_file_change() {
    local changed_file="$1"
    
    log_info "Coordinating file change: $changed_file"
    
    # Determine if this change should trigger updates
    if [[ "$changed_file" =~ context/roadmap/.*\.md$ ]]; then
        # Roadmap file changed - might need dashboard sync
        queue_event "roadmap_update" "file_change:$changed_file" "high"
    elif [[ "$changed_file" =~ \.md$ && $(wc -l < "$changed_file" 2>/dev/null || echo "0") -gt 80 ]]; then
        # Markdown file exceeds size limit
        log_warning "File size violation detected: $changed_file"
        # Could trigger L2-modular extraction
    fi
}

coordinate_git_commit() {
    local commit_data="$1"
    
    log_info "Coordinating git commit: $commit_data"
    
    # Check if commit affects roadmap-relevant files
    local files_changed=$(git diff --name-only HEAD~1 HEAD 2>/dev/null || echo "")
    
    if echo "$files_changed" | grep -q "context/roadmap\|\.claude/\|scripts/"; then
        queue_event "roadmap_update" "git_commit:$commit_data" "normal"
    fi
}

coordinate_claude_conversation() {
    local conversation_data="$1"
    
    log_info "Coordinating Claude conversation completion"
    
    # Queue roadmap update after conversation
    queue_event "roadmap_update" "claude_conversation:$conversation_data" "normal"
}

# Helper functions
should_update_roadmap() {
    local last_update=$(get_status "last_roadmap_update")
    
    if [[ "$last_update" == "null" ]]; then
        return 0  # Never updated
    fi
    
    # Check if enough time has passed (minimum 30 seconds between updates)
    local last_update_ts=$(date -j -f "%Y-%m-%dT%H:%M:%S" "${last_update%.*}" "+%s" 2>/dev/null || echo "0")
    local current_ts=$(date "+%s")
    local time_diff=$((current_ts - last_update_ts))
    
    if [[ $time_diff -lt 30 ]]; then
        log_info "Roadmap updated recently (${time_diff}s ago), skipping"
        return 1
    fi
    
    return 0
}

get_status() {
    local key="$1"
    jq -r ".$key // null" "$STATUS_FILE" 2>/dev/null || echo "null"
}

update_status() {
    local key="$1"
    local value="$2"
    local temp_file=$(mktemp)
    
    jq ".$key = \"$value\"" "$STATUS_FILE" > "$temp_file" && mv "$temp_file" "$STATUS_FILE"
}

# Main coordination function
coordinate() {
    local action="$1"
    shift
    
    initialize_state
    
    case "$action" in
        "event")
            local event_type="$1"
            local event_data="${2:-}"
            local priority="${3:-normal}"
            queue_event "$event_type" "$event_data" "$priority"
            ;;
        "process")
            process_event_queue "${1:-5}"
            ;;
        "status")
            cat "$STATUS_FILE" | jq .
            ;;
        "lock")
            local operation="$1"
            acquire_lock "$operation" "${2:-30}"
            ;;
        "unlock")
            release_lock
            ;;
        *)
            echo "Usage: $0 {event|process|status|lock|unlock} [args...]"
            exit 1
            ;;
    esac
}

# Script execution
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    coordinate "$@"
fi