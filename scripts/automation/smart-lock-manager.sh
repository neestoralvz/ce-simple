#!/bin/bash

# Smart Lock Manager
# Advanced locking system with deadlock prevention and operation coordination
# Integrates with coordination-hub.sh for intelligent automation management

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
STATE_DIR="$PROJECT_ROOT/.automation-state"
LOCKS_DIR="$STATE_DIR/locks"
LOCK_REGISTRY="$STATE_DIR/lock-registry.json"
LOG_FILE="$STATE_DIR/lock-manager.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Logging functions
log_info() { echo -e "${BLUE}🔐${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_success() { echo -e "${GREEN}✅${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_warning() { echo -e "${YELLOW}⚠️${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }
log_error() { echo -e "${RED}❌${NC} [$(date '+%H:%M:%S')] $1" | tee -a "$LOG_FILE"; }

# Initialize lock system
initialize_locks() {
    mkdir -p "$LOCKS_DIR" "$STATE_DIR"
    
    # Initialize lock registry
    if [[ ! -f "$LOCK_REGISTRY" ]]; then
        cat > "$LOCK_REGISTRY" << EOF
{
  "active_locks": {},
  "lock_history": [],
  "deadlock_prevention": {
    "max_wait_time": 300,
    "stale_lock_timeout": 600,
    "priority_override": true
  },
  "statistics": {
    "locks_acquired": 0,
    "locks_released": 0,
    "deadlocks_prevented": 0,
    "stale_locks_cleaned": 0
  }
}
EOF
    fi
    
    log_info "Lock system initialized"
}

# Smart lock acquisition with deadlock prevention
smart_acquire_lock() {
    local operation="$1"
    local priority="${2:-normal}"
    local timeout="${3:-60}"
    local caller_pid="${4:-$$}"
    
    local lock_id="${operation}_${caller_pid}"
    local lock_file="$LOCKS_DIR/${lock_id}.lock"
    local wait_time=0
    
    log_info "Attempting to acquire lock: $operation (priority: $priority, timeout: ${timeout}s)"
    
    # Check for conflicting operations first
    if has_conflicting_locks "$operation" "$priority"; then
        handle_lock_conflict "$operation" "$priority" "$timeout"
        return $?
    fi
    
    # Main acquisition loop
    while [[ $wait_time -lt $timeout ]]; do
        if attempt_lock_creation "$lock_id" "$operation" "$priority" "$caller_pid"; then
            register_lock "$lock_id" "$operation" "$priority" "$caller_pid"
            increment_stat "locks_acquired"
            log_success "Lock acquired: $operation ($lock_id)"
            return 0
        fi
        
        # Clean stale locks during wait
        cleanup_stale_locks
        
        # Intelligent backoff based on priority
        local sleep_time=$(calculate_backoff_time "$priority" "$wait_time")
        sleep "$sleep_time"
        wait_time=$((wait_time + sleep_time))
        
        log_info "Waiting for lock: $operation (${wait_time}/${timeout}s elapsed)"
    done
    
    log_error "Failed to acquire lock: $operation (timeout after ${timeout}s)"
    return 1
}

# Check for conflicting operations
has_conflicting_locks() {
    local operation="$1"
    local priority="$2"
    
    # Define conflict matrix
    local conflicts=""
    case "$operation" in
        "roadmap_update")
            conflicts="file_modification git_commit claude_conversation"
            ;;
        "file_modification")
            conflicts="roadmap_update l2_modular_extraction"
            ;;
        "git_commit")
            conflicts="roadmap_update file_modification"
            ;;
        "claude_conversation")
            conflicts="roadmap_update"
            ;;
        "l2_modular_extraction")
            conflicts="file_modification roadmap_update"
            ;;
        "fswatch_validation")
            conflicts="file_modification"
            ;;
    esac
    
    # Check active locks for conflicts
    for conflict in $conflicts; do
        if has_active_lock_type "$conflict"; then
            local conflicting_priority=$(get_active_lock_priority "$conflict")
            
            # High priority can override lower priority operations
            if [[ "$priority" == "high" && "$conflicting_priority" != "high" ]]; then
                log_info "High priority override available for: $operation vs $conflict"
                continue
            fi
            
            log_warning "Conflicting lock detected: $operation conflicts with $conflict"
            return 0
        fi
    done
    
    return 1
}

# Handle lock conflicts intelligently
handle_lock_conflict() {
    local operation="$1"
    local priority="$2"
    local timeout="$3"
    
    log_info "Handling lock conflict for: $operation"
    
    # For high priority operations, attempt graceful interruption
    if [[ "$priority" == "high" ]]; then
        if attempt_graceful_interruption "$operation"; then
            log_success "Graceful interruption successful for: $operation"
            return 0
        fi
    fi
    
    # For emergency operations, force override
    if [[ "$priority" == "emergency" ]]; then
        force_lock_override "$operation"
        return 0
    fi
    
    # Standard conflict resolution - wait with intelligent backoff
    wait_for_conflict_resolution "$operation" "$timeout"
}

# Attempt graceful interruption of lower priority operations
attempt_graceful_interruption() {
    local requesting_operation="$1"
    local interrupted_count=0
    
    # Send graceful interruption signals to compatible operations
    while IFS= read -r lock_entry; do
        local lock_data=$(echo "$lock_entry" | jq -r '.')
        local lock_operation=$(echo "$lock_data" | jq -r '.operation')
        local lock_pid=$(echo "$lock_data" | jq -r '.pid')
        local lock_priority=$(echo "$lock_data" | jq -r '.priority')
        
        if [[ "$lock_priority" != "high" && "$lock_priority" != "emergency" ]]; then
            if can_interrupt_operation "$lock_operation" "$requesting_operation"; then
                signal_graceful_interruption "$lock_pid" "$lock_operation"
                ((interrupted_count++))
            fi
        fi
    done < <(jq -r '.active_locks | to_entries[] | .value' "$LOCK_REGISTRY" 2>/dev/null || echo "")
    
    if [[ $interrupted_count -gt 0 ]]; then
        log_info "Sent graceful interruption to $interrupted_count operations"
        sleep 5  # Give time for graceful shutdown
        return 0
    fi
    
    return 1
}

# Check if operation can be interrupted
can_interrupt_operation() {
    local current_op="$1"
    local requesting_op="$2"
    
    # Define interruptible operations
    case "$current_op" in
        "roadmap_update"|"file_modification")
            [[ "$requesting_op" == "git_commit" || "$requesting_op" == "claude_conversation" ]]
            ;;
        "fswatch_validation")
            true  # fswatch can always be interrupted
            ;;
        *)
            false
            ;;
    esac
}

# Signal graceful interruption
signal_graceful_interruption() {
    local target_pid="$1"
    local operation="$2"
    
    log_info "Signaling graceful interruption to PID $target_pid ($operation)"
    
    # Create interruption signal file
    local signal_file="$STATE_DIR/interrupt_${target_pid}.signal"
    echo "{\"operation\": \"$operation\", \"timestamp\": \"$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")\"}" > "$signal_file"
    
    # Send SIGUSR1 for graceful interruption
    if kill -USR1 "$target_pid" 2>/dev/null; then
        log_info "Interruption signal sent to $target_pid"
    else
        log_warning "Failed to send signal to PID $target_pid (process may have ended)"
        # Clean up stale lock
        cleanup_process_locks "$target_pid"
    fi
}

# Smart lock release
smart_release_lock() {
    local operation="$1"
    local caller_pid="${2:-$$}"
    
    local lock_id="${operation}_${caller_pid}"
    local lock_file="$LOCKS_DIR/${lock_id}.lock"
    
    if [[ -f "$lock_file" ]]; then
        rm -f "$lock_file"
        unregister_lock "$lock_id"
        increment_stat "locks_released"
        log_success "Lock released: $operation ($lock_id)"
        
        # Notify waiting processes
        trigger_lock_release_notification "$operation"
        return 0
    else
        log_warning "Lock not found for release: $operation ($lock_id)"
        return 1
    fi
}

# Lock registry management
register_lock() {
    local lock_id="$1"
    local operation="$2"
    local priority="$3"
    local pid="$4"
    
    local temp_file=$(mktemp)
    local lock_data=$(cat <<EOF
{
  "operation": "$operation",
  "priority": "$priority",
  "pid": $pid,
  "acquired_at": "$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")",
  "lock_id": "$lock_id"
}
EOF
)
    
    jq ".active_locks[\"$lock_id\"] = $lock_data" "$LOCK_REGISTRY" > "$temp_file" && mv "$temp_file" "$LOCK_REGISTRY"
}

unregister_lock() {
    local lock_id="$1"
    local temp_file=$(mktemp)
    
    jq "del(.active_locks[\"$lock_id\"])" "$LOCK_REGISTRY" > "$temp_file" && mv "$temp_file" "$LOCK_REGISTRY"
}

# Utility functions
attempt_lock_creation() {
    local lock_id="$1"
    local operation="$2"
    local priority="$3"
    local pid="$4"
    
    local lock_file="$LOCKS_DIR/${lock_id}.lock"
    
    if mkdir "$lock_file" 2>/dev/null; then
        echo "$operation:$priority:$pid:$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")" > "$lock_file/metadata"
        return 0
    fi
    
    return 1
}

cleanup_stale_locks() {
    local cleaned=0
    local stale_timeout=600  # 10 minutes
    local current_time=$(date +%s)
    
    for lock_file in "$LOCKS_DIR"/*.lock; do
        [[ ! -d "$lock_file" ]] && continue
        
        local lock_time=$(stat -f %m "$lock_file" 2>/dev/null || echo "0")
        local age=$((current_time - lock_time))
        
        if [[ $age -gt $stale_timeout ]]; then
            local lock_id=$(basename "$lock_file" .lock)
            log_warning "Cleaning stale lock: $lock_id (age: ${age}s)"
            
            rm -rf "$lock_file"
            unregister_lock "$lock_id"
            ((cleaned++))
        fi
    done
    
    if [[ $cleaned -gt 0 ]]; then
        increment_stat "stale_locks_cleaned" "$cleaned"
        log_info "Cleaned $cleaned stale locks"
    fi
}

cleanup_process_locks() {
    local target_pid="$1"
    local cleaned=0
    
    # Clean file locks
    for lock_file in "$LOCKS_DIR"/*_${target_pid}.lock; do
        [[ ! -d "$lock_file" ]] && continue
        
        local lock_id=$(basename "$lock_file" .lock)
        log_info "Cleaning lock for dead process: $lock_id (PID: $target_pid)"
        
        rm -rf "$lock_file"
        unregister_lock "$lock_id"
        ((cleaned++))
    done
    
    # Clean registry entries
    local temp_file=$(mktemp)
    jq "del(.active_locks[] | select(.pid == $target_pid))" "$LOCK_REGISTRY" > "$temp_file" && mv "$temp_file" "$LOCK_REGISTRY"
    
    if [[ $cleaned -gt 0 ]]; then
        log_info "Cleaned $cleaned locks for process $target_pid"
    fi
}

# Helper functions
has_active_lock_type() {
    local operation_type="$1"
    jq -e ".active_locks | to_entries[] | select(.value.operation == \"$operation_type\")" "$LOCK_REGISTRY" >/dev/null 2>&1
}

get_active_lock_priority() {
    local operation_type="$1"
    jq -r ".active_locks | to_entries[] | select(.value.operation == \"$operation_type\") | .value.priority" "$LOCK_REGISTRY" 2>/dev/null | head -1
}

calculate_backoff_time() {
    local priority="$1"
    local wait_time="$2"
    
    case "$priority" in
        "high"|"emergency")
            echo "1"  # Fast retry for high priority
            ;;
        "normal")
            echo "2"  # Standard retry
            ;;
        "low")
            echo "5"  # Slower retry for low priority
            ;;
        *)
            echo "2"
            ;;
    esac
}

increment_stat() {
    local stat_name="$1"
    local increment="${2:-1}"
    local temp_file=$(mktemp)
    
    jq ".statistics[\"$stat_name\"] = (.statistics[\"$stat_name\"] // 0) + $increment" "$LOCK_REGISTRY" > "$temp_file" && mv "$temp_file" "$LOCK_REGISTRY"
}

trigger_lock_release_notification() {
    local operation="$1"
    local notification_file="$STATE_DIR/lock_release_${operation}.notify"
    
    echo "$(date -u +"%Y-%m-%dT%H:%M:%S.%fZ")" > "$notification_file"
    
    # Clean up notification after 30 seconds
    (sleep 30 && rm -f "$notification_file") &
}

# Status and monitoring functions
show_lock_status() {
    echo -e "${BLUE}🔐 Smart Lock Manager Status${NC}"
    echo
    
    if [[ -f "$LOCK_REGISTRY" ]]; then
        echo -e "${GREEN}Active Locks:${NC}"
        jq -r '.active_locks | to_entries[] | "\(.key): \(.value.operation) (\(.value.priority) priority, PID \(.value.pid))"' "$LOCK_REGISTRY" 2>/dev/null || echo "None"
        
        echo
        echo -e "${BLUE}Statistics:${NC}"
        jq -r '.statistics | to_entries[] | "\(.key): \(.value)"' "$LOCK_REGISTRY" 2>/dev/null || echo "No statistics available"
    else
        echo "Lock system not initialized"
    fi
}

# Main lock manager function
manage_lock() {
    local action="$1"
    shift
    
    initialize_locks
    
    case "$action" in
        "acquire")
            local operation="$1"
            local priority="${2:-normal}"
            local timeout="${3:-60}"
            smart_acquire_lock "$operation" "$priority" "$timeout"
            ;;
        "release") 
            local operation="$1"
            smart_release_lock "$operation"
            ;;
        "status")
            show_lock_status
            ;;
        "cleanup")
            cleanup_stale_locks
            ;;
        "cleanup-pid")
            local pid="$1"
            cleanup_process_locks "$pid"
            ;;
        *)
            echo "Usage: $0 {acquire|release|status|cleanup|cleanup-pid} [args...]"
            echo "  acquire <operation> [priority] [timeout]"
            echo "  release <operation>"
            echo "  status"
            echo "  cleanup"
            echo "  cleanup-pid <pid>"
            exit 1
            ;;
    esac
}

# Script execution
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    manage_lock "$@"
fi