# Process Lifecycle Management - Complete Process Control Configuration

**29/07/2025** | Consolidated process management patterns for comprehensive lifecycle control

## Process Lifecycle Control

### Process Startup Management
→ Ver context/examples/bash/background_processes.sh para funciones completas:
- start_background_monitoring()
- start_conversation_coordinator() 
- start_communication_daemon()
- stop_all_background_processes()

### Process Health Monitoring
```bash
# Comprehensive health check for all system processes
system_health_check() {
    echo "=== System Health Check ==="
    echo "Timestamp: $(date)"
    echo ""
    
    # Check background processes
    echo "Background Processes:"
    check_background_status
    echo ""
    
    # Check git state
    echo "Git State:"
    echo "- Current branch: $(git branch --show-current)"
    echo "- Uncommitted changes: $(git status --porcelain | wc -l)"
    echo "- Active worktrees: $(git worktree list | wc -l)"
    echo ""
    
    # Check shared state
    if [[ -d "shared_state" ]]; then
        echo "Shared State:"
        echo "- Tickets: $(wc -l < shared_state/tickets.md 2>/dev/null || echo 0)"
        echo "- Status file: $(test -f shared_state/status.md && echo "EXISTS" || echo "MISSING")"
        echo "- Convergence file: $(test -f shared_state/convergence.md && echo "EXISTS" || echo "MISSING")"
    else
        echo "Shared State: NOT INITIALIZED"
    fi
    echo ""
    
    return 0
}
```

### Process Recovery Management
```bash
# Restart failed processes automatically
restart_failed_processes() {
    echo "Checking for failed processes and restarting..."
    
    local -a pid_files=(
        "/tmp/background_monitor.pid"
        "/tmp/conversation_coordinator.pid"
        "/tmp/communication_daemon.pid"
    )
    
    local -a start_functions=(
        "start_background_monitoring"
        "start_conversation_coordinator"
        "start_communication_daemon"
    )
    
    local -a process_names=(
        "Background Monitor"
        "Conversation Coordinator"
        "Communication Daemon"
    )
    
    for i in "${!pid_files[@]}"; do
        local pid_file="${pid_files[$i]}"
        local start_function="${start_functions[$i]}"
        local process_name="${process_names[$i]}"
        
        if [[ -f "$pid_file" ]]; then
            local pid=$(cat "$pid_file")
            if ! kill -0 "$pid" 2>/dev/null; then
                echo "Restarting failed process: $process_name"
                rm -f "$pid_file"
                $start_function
            fi
        else
            echo "Starting missing process: $process_name"
            $start_function
        fi
    done
    
    return 0
}
```

## System Maintenance Patterns

### Regular Maintenance Tasks
```bash
# Daily maintenance routine
daily_maintenance() {
    echo "=== Daily Maintenance Routine ==="
    echo "Started: $(date)"
    
    # Health check
    system_health_check
    
    # Clean up old log files
    find /tmp -name "*_monitor.log" -mtime +7 -delete 2>/dev/null || true
    find /tmp -name "*_coordinator.log" -mtime +7 -delete 2>/dev/null || true
    find /tmp -name "*_daemon.log" -mtime +7 -delete 2>/dev/null || true
    
    # Restart any failed processes
    restart_failed_processes
    
    # Validate system coherence
    validate_system_coherence
    
    echo "Daily maintenance completed: $(date)"
    return 0
}
```

### System Coherence Validation
```bash
# Validate critical system files and structures
validate_system_coherence() {
    echo "=== System Coherence Validation ==="
    
    local validation_errors=0
    
    # Check critical files
    local -a critical_files=(
        "context/TRUTH_SOURCE.md"
        "CLAUDE.md"
        "context/system/organization.md"
    )
    
    for file in "${critical_files[@]}"; do
        if [[ ! -f "$file" ]]; then
            echo "❌ Critical file missing: $file"
            ((validation_errors++))
        else
            echo "✅ Critical file exists: $file"
        fi
    done
    
    # Check directory structure
    local -a critical_dirs=(
        "context/operational"
        "context/system"
        "context/examples"
    )
    
    for dir in "${critical_dirs[@]}"; do
        if [[ ! -d "$dir" ]]; then
            echo "❌ Critical directory missing: $dir"
            ((validation_errors++))
        else
            echo "✅ Critical directory exists: $dir"
        fi
    done
    
    # Report validation result
    if [[ $validation_errors -eq 0 ]]; then
        echo "✅ System coherence validated successfully"
    else
        echo "❌ System coherence validation failed: $validation_errors errors"
    fi
    
    return $validation_errors
}
```

## Integration Protocols

### Session Lifecycle Integration
```bash
# Session start protocol with process management
session_start_protocol() {
    echo "=== Session Start Protocol ==="
    
    # Initialize shared state if needed
    if [[ ! -d "shared_state" ]]; then
        quick_parallel_setup
    fi
    
    # Start background processes
    start_all_background_processes
    
    # Validate system readiness
    system_health_check
    
    echo "Session start protocol completed"
    return 0
}

# Session close protocol with cleanup
session_close_protocol() {
    echo "=== Session Close Protocol ==="
    
    # Stop all background processes
    stop_all_background_processes
    
    # Clean up conversation branches if specified
    if [[ "${1:-}" == "cleanup" ]]; then
        cleanup_conversation_branches
    fi
    
    # Archive shared state
    if [[ -d "shared_state" ]]; then
        local archive_name="shared_state_$(date +%Y%m%d_%H%M%S)"
        mv shared_state "$archive_name"
        echo "Shared state archived as: $archive_name"
    fi
    
    echo "Session close protocol completed"
    return 0
}
```

### Emergency Procedures
```bash
# Complete system reset for emergency situations
emergency_system_reset() {
    echo "=== EMERGENCY SYSTEM RESET ==="
    echo "WARNING: This will stop all processes and clean up all state"
    
    # Stop everything
    stop_all_background_processes
    
    # Clean up all conversation branches
    cleanup_conversation_branches
    
    # Remove shared state
    rm -rf shared_state 2>/dev/null || true
    
    # Clean up temporary files
    rm -f /tmp/*_monitor.* /tmp/*_coordinator.* /tmp/*_daemon.* 2>/dev/null || true
    
    # Validate system is clean
    if [[ $(git worktree list | wc -l) -eq 1 ]] && [[ ! -d "shared_state" ]]; then
        echo "✅ Emergency reset completed successfully"
    else
        echo "❌ Emergency reset may be incomplete"
        return 1
    fi
    
    return 0
}
```

## Quality Gates and Monitoring

### Process Performance Monitoring
```bash
# Monitor process performance metrics
monitor_process_performance() {
    echo "=== Process Performance Monitoring ==="
    
    # Check log file sizes
    for log_file in /tmp/*_{monitor,coordinator,daemon}.log; do
        if [[ -f "$log_file" ]]; then
            local size=$(du -h "$log_file" | cut -f1)
            echo "Log file $log_file: $size"
        fi
    done
    
    # Check process resource usage
    local background_processes=$(pgrep -f "background_monitor|conversation_coordinator|communication_daemon")
    if [[ -n "$background_processes" ]]; then
        echo "Active background processes:"
        ps -p $background_processes -o pid,pcpu,pmem,comm 2>/dev/null || echo "No processes found"
    fi
    
    return 0
}
```

### Automatic Quality Assurance
```bash
# Continuous quality assurance for process management
continuous_quality_assurance() {
    echo "Starting continuous quality assurance..."
    
    while true; do
        # Check every 5 minutes
        sleep 300
        
        # Restart failed processes
        restart_failed_processes
        
        # Monitor performance
        monitor_process_performance
        
        # Validate system coherence periodically
        if [[ $(($(date +%s) % 3600)) -lt 300 ]]; then
            validate_system_coherence
        fi
    done
}
```

---
**Source Consolidation**: Extracted from context/examples/bash/background_processes.sh + context/operational/enforcement/anti_monolithic_prevention.md + context/examples/templates/workflow_actions.md

**Usage**: Apply these lifecycle management patterns to maintain robust process control across multi-conversation parallel executions with comprehensive monitoring and recovery capabilities.