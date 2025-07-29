#!/usr/bin/env bash
# Git Worktree Management Scripts - Extracted from context/user-vision/layer3/implementation_guide.md and operations/

# Create conversation-specific branch with timestamp
create_conversation_branch() {
    local timestamp=$(date +%Y%m%d_%H%M)
    local conversation_id="${1:-default}"
    local branch_name="conversation-${conversation_id}-${timestamp}"
    
    echo "Creating conversation branch: $branch_name"
    git worktree add "../${branch_name}" -b "$branch_name"
    
    return 0
}

# Setup parallel execution environment
setup_parallel_conversations() {
    local task_count="${1:-2}"
    
    echo "Setting up $task_count parallel conversation branches"
    
    for i in $(seq 1 "$task_count"); do
        local branch_name="task-branch-$i"
        echo "Creating branch: $branch_name"
        git worktree add "../$branch_name" "task-$i"
    done
    
    return 0
}

# Background status monitoring
start_background_monitoring() {
    echo "Starting background git monitoring..."
    
    # Monitor git status with background process
    while true; do
        git status --porcelain | tee /tmp/git_status_monitor.log
        sleep 30
    done &
    
    local monitor_pid=$!
    echo "Background monitor started with PID: $monitor_pid"
    echo "$monitor_pid" > /tmp/git_monitor.pid
    
    return 0
}

# Stop background monitoring
stop_background_monitoring() {
    if [[ -f /tmp/git_monitor.pid ]]; then
        local pid=$(cat /tmp/git_monitor.pid)
        echo "Stopping background monitor (PID: $pid)"
        kill "$pid" 2>/dev/null
        rm -f /tmp/git_monitor.pid
    fi
    
    return 0
}

# Inter-conversation communication via shared files
send_ticket() {
    local message="$1"
    local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    
    echo "[$timestamp] ticket: $message" >> shared_state/tickets.md
    echo "Ticket sent: $message"
    
    return 0
}

# Quick setup for parallel conversations
quick_parallel_setup() {
    echo "Quick setup for parallel conversations"
    
    # Create shared state directory
    mkdir -p shared_state
    
    # Initialize communication files
    touch shared_state/tickets.md
    touch shared_state/status.md
    touch shared_state/priorities.md
    touch shared_state/convergence.md
    
    echo "Parallel conversation environment ready"
    
    return 0
}

# Cleanup worktrees
cleanup_conversation_branches() {
    echo "Cleaning up conversation branches..."
    
    # List and remove worktrees
    git worktree list | grep -E "(conversation-|task-)" | while read -r path branch _; do
        echo "Removing worktree: $path ($branch)"
        git worktree remove "$path" --force
        git branch -D "$branch" 2>/dev/null || true
    done
    
    return 0
}

# Validate branch isolation
validate_branch_isolation() {
    local current_branch=$(git branch --show-current)
    echo "Current branch isolation: $current_branch"
    
    # Check for uncommitted changes
    if ! git diff-index --quiet HEAD --; then
        echo "WARNING: Uncommitted changes detected in $current_branch"
        return 1
    fi
    
    echo "Branch isolation validated"
    return 0
}