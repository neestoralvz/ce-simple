# Background Process Configurations - Persistent Monitoring & Coordination

**29/07/2025** | Consolidated background process configurations for multi-conversation coordination

## Process Management Functions

### Background System Monitoring
```bash
start_background_monitoring() {
    echo "Starting background monitoring system..."
    
    local monitor_log="/tmp/background_monitor.log"
    local pid_file="/tmp/background_monitor.pid"
    
    # Background monitoring function
    background_monitor() {
        while true; do
            local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            
            # System status monitoring
            echo "[$timestamp] System Status Check" >> "$monitor_log"
            echo "  - Git status: $(git status --porcelain | wc -l) files changed" >> "$monitor_log"
            echo "  - Working directory: $(pwd)" >> "$monitor_log"
            echo "  - Current branch: $(git branch --show-current 2>/dev/null)" >> "$monitor_log"
            
            # Inter-conversation state monitoring
            if [[ -d "shared_state" ]]; then
                echo "  - Shared state directory: EXISTS" >> "$monitor_log"
                echo "  - Tickets pending: $(wc -l < shared_state/tickets.md 2>/dev/null || echo 0)" >> "$monitor_log"
            fi
            
            # Sleep for monitoring interval
            sleep 60
        done
    }
    
    # Start background monitoring
    background_monitor &
    local monitor_pid=$!
    
    echo "$monitor_pid" > "$pid_file"
    echo "Background monitoring started with PID: $monitor_pid"
    echo "Log file: $monitor_log"
    
    return 0
}
```

### Conversation Coordinator
```bash
start_conversation_coordinator() {
    echo "Starting conversation coordinator..."
    
    local coordinator_log="/tmp/conversation_coordinator.log"
    local coordinator_pid_file="/tmp/conversation_coordinator.pid"
    
    # Coordinator function
    conversation_coordinator() {
        while true; do
            local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            echo "[$timestamp] Conversation Coordinator Check" >> "$coordinator_log"
            
            # Check for new tickets
            if [[ -f "shared_state/tickets.md" ]]; then
                local ticket_count=$(grep -c "ticket:" shared_state/tickets.md 2>/dev/null || echo 0)
                echo "  - Active tickets: $ticket_count" >> "$coordinator_log"
            fi
            
            # Monitor conversation branches
            local active_branches=$(git branch --list | grep -E "(conversation-|task-)" | wc -l)
            echo "  - Active conversation branches: $active_branches" >> "$coordinator_log"
            
            # Check for convergence readiness
            if [[ -f "shared_state/convergence.md" ]]; then
                echo "  - Convergence coordination: ACTIVE" >> "$coordinator_log"
            fi
            
            sleep 30
        done
    }
    
    # Start coordinator
    conversation_coordinator &
    local coordinator_pid=$!
    
    echo "$coordinator_pid" > "$coordinator_pid_file"
    echo "Conversation coordinator started with PID: $coordinator_pid"
    echo "Log file: $coordinator_log"
    
    return 0
}
```

### Inter-Conversation Communication Daemon
```bash
start_communication_daemon() {
    echo "Starting inter-conversation communication daemon..."
    
    local daemon_log="/tmp/communication_daemon.log"
    local daemon_pid_file="/tmp/communication_daemon.pid"
    
    # Communication daemon function
    communication_daemon() {
        while true; do
            local timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            
            # Process pending tickets
            if [[ -f "shared_state/tickets.md" ]]; then
                local new_tickets=$(grep -c "\[$timestamp" shared_state/tickets.md 2>/dev/null || echo 0)
                if [[ $new_tickets -gt 0 ]]; then
                    echo "[$timestamp] Processing $new_tickets new tickets" >> "$daemon_log"
                fi
            fi
            
            # Update shared status
            if [[ -f "shared_state/status.md" ]]; then
                echo "[$timestamp] Updating shared status" >> "$daemon_log"
                # Update status file with current information
                {
                    echo "# Current State Across Conversations"
                    echo ""
                    echo "## System State"
                    echo "- Last update: $timestamp"
                    echo "- Active processes: $(pgrep -f "background_monitor\\|conversation_coordinator\\|communication_daemon" | wc -l)"
                    echo "- Current branch: $(git branch --show-current 2>/dev/null)"
                } > shared_state/status.md.tmp && mv shared_state/status.md.tmp shared_state/status.md
            fi
            
            sleep 15
        done
    }
    
    # Start daemon
    communication_daemon &
    local daemon_pid=$!
    
    echo "$daemon_pid" > "$daemon_pid_file"
    echo "Communication daemon started with PID: $daemon_pid"
    echo "Log file: $daemon_log"
    
    return 0
}
```

## Process Lifecycle Management

### Stop All Background Processes
```bash
stop_all_background_processes() {
    echo "Stopping all background processes..."
    
    local -a pid_files=(
        "/tmp/background_monitor.pid"
        "/tmp/conversation_coordinator.pid"
        "/tmp/communication_daemon.pid"
    )
    
    for pid_file in "${pid_files[@]}"; do
        if [[ -f "$pid_file" ]]; then
            local pid=$(cat "$pid_file")
            echo "Stopping process (PID: $pid)"
            kill "$pid" 2>/dev/null
            rm -f "$pid_file"
        fi
    done
    
    echo "All background processes stopped"
    return 0
}
```

### Status Check for All Processes
```bash
check_background_status() {
    echo "Checking background process status..."
    
    local -a pid_files=(
        "/tmp/background_monitor.pid"
        "/tmp/conversation_coordinator.pid"
        "/tmp/communication_daemon.pid"
    )
    
    local -a process_names=(
        "Background Monitor"
        "Conversation Coordinator"
        "Communication Daemon"
    )
    
    for i in "${!pid_files[@]}"; do
        local pid_file="${pid_files[$i]}"
        local process_name="${process_names[$i]}"
        
        if [[ -f "$pid_file" ]]; then
            local pid=$(cat "$pid_file")
            if kill -0 "$pid" 2>/dev/null; then
                echo "✓ $process_name: RUNNING (PID: $pid)"
            else
                echo "✗ $process_name: DEAD (PID file exists but process not running)"
            fi
        else
            echo "✗ $process_name: NOT STARTED (no PID file)"
        fi
    done
    
    return 0
}
```

## Integration Architecture

### Background Intelligence Pattern
- **Persistent monitoring**: System state awareness across conversations
- **Inter-conversation coordination**: Background processes manage communication
- **Ultra-orchestrator support**: User coordinates N parallel agents
- **Resource coordination**: Prevent conflicts between parallel executions

### Orchestration Commands Integration
- **`/workflows:debug`** → Systematic resolution + background process management
- **`/maintain`** → System maintenance + git worktree coordination
- **Background Intelligence**: Persistent monitoring processes coordinate conversations

---
**Source Consolidation**: Extracted from context/examples/bash/background_processes.sh + context/operational/operations/architecture_implementation.md + context/operational/operations/workflow_execution.md

**Usage**: Apply these configurations to enable persistent monitoring and coordination across multi-conversation parallel executions.