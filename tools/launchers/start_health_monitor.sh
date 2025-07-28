#!/bin/bash
# CE-Simple Health Monitor External Launcher
# Solves Claude Code background process limitation

set -e

# Configuration
MONITOR_SCRIPT="/Users/nalve/ce-simple/tools/monitoring/system-health.py"
PID_FILE="/Users/nalve/ce-simple/data/monitoring/health_monitor.pid"
LOG_FILE="/Users/nalve/ce-simple/data/monitoring/health_monitor.log"
STATUS_FILE="/Users/nalve/ce-simple/data/monitoring/health_status.json"

# Create directories if they don't exist
mkdir -p "$(dirname "$PID_FILE")"
mkdir -p "$(dirname "$LOG_FILE")"

# Function to check if monitor is already running
is_running() {
    if [ -f "$PID_FILE" ]; then
        local pid=$(cat "$PID_FILE")
        if ps -p "$pid" > /dev/null 2>&1; then
            return 0  # Running
        else
            rm -f "$PID_FILE"  # Cleanup stale PID file
            return 1  # Not running
        fi
    else
        return 1  # Not running
    fi
}

# Function to start monitor
start_monitor() {
    if is_running; then
        echo "Health monitor is already running (PID: $(cat "$PID_FILE"))"
        exit 0
    fi
    
    echo "Starting CE-Simple health monitor..."
    
    # Start monitor in daemon mode
    nohup python3 "$MONITOR_SCRIPT" daemon > "$LOG_FILE" 2>&1 &
    local pid=$!
    
    # Save PID
    echo "$pid" > "$PID_FILE"
    
    # Wait a moment to ensure it started successfully
    sleep 2
    
    if is_running; then
        echo "✅ Health monitor started successfully (PID: $pid)"
        echo "📄 Log file: $LOG_FILE"
        echo "📊 Status file: $STATUS_FILE"
        
        # Write initial status
        cat > "$STATUS_FILE" << EOF
{
    "status": "running",
    "pid": $pid,
    "started_at": "$(date -Iseconds)",
    "log_file": "$LOG_FILE",
    "monitor_script": "$MONITOR_SCRIPT"
}
EOF
    else
        echo "❌ Failed to start health monitor"
        rm -f "$PID_FILE"
        exit 1
    fi
}

# Function to stop monitor
stop_monitor() {
    if ! is_running; then
        echo "Health monitor is not running"
        exit 0
    fi
    
    local pid=$(cat "$PID_FILE")
    echo "Stopping health monitor (PID: $pid)..."
    
    kill "$pid"
    
    # Wait for graceful shutdown
    local count=0
    while ps -p "$pid" > /dev/null 2>&1 && [ $count -lt 10 ]; do
        sleep 1
        ((count++))
    done
    
    # Force kill if still running
    if ps -p "$pid" > /dev/null 2>&1; then
        echo "Force killing monitor..."
        kill -9 "$pid"
    fi
    
    # Cleanup
    rm -f "$PID_FILE"
    
    # Update status file
    cat > "$STATUS_FILE" << EOF
{
    "status": "stopped",
    "stopped_at": "$(date -Iseconds)",
    "last_pid": $pid
}
EOF
    
    echo "✅ Health monitor stopped"
}

# Function to show status
show_status() {
    if is_running; then
        local pid=$(cat "$PID_FILE")
        echo "✅ Health monitor is running (PID: $pid)"
        echo "📄 Log: $LOG_FILE"
        echo "📊 Status: $STATUS_FILE"
        
        # Show recent log entries
        if [ -f "$LOG_FILE" ]; then
            echo ""
            echo "Recent log entries:"
            tail -n 5 "$LOG_FILE"
        fi
    else
        echo "❌ Health monitor is not running"
        if [ -f "$STATUS_FILE" ]; then
            echo "Last status:"
            cat "$STATUS_FILE"
        fi
    fi
}

# Function to restart monitor
restart_monitor() {
    echo "Restarting health monitor..."
    stop_monitor
    sleep 1
    start_monitor
}

# Main command handling
case "${1:-start}" in
    start)
        start_monitor
        ;;
    stop)
        stop_monitor
        ;;
    restart)
        restart_monitor
        ;;
    status)
        show_status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        echo ""
        echo "CE-Simple Health Monitor External Launcher"
        echo "Manages background health monitoring outside Claude Code limitations"
        echo ""
        echo "Commands:"
        echo "  start   - Start health monitor daemon"
        echo "  stop    - Stop health monitor daemon"
        echo "  restart - Restart health monitor daemon" 
        echo "  status  - Show current status"
        echo ""
        echo "Files:"
        echo "  PID:    $PID_FILE"
        echo "  Log:    $LOG_FILE"
        echo "  Status: $STATUS_FILE"
        exit 1
        ;;
esac