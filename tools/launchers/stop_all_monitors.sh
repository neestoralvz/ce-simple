#!/bin/bash
# CE-Simple Monitor Shutdown Script
# Gracefully stops all background monitoring processes

set -e

# Configuration
MONITOR_DIR="/Users/nalve/ce-simple/data/monitoring"
TOOLS_DIR="/Users/nalve/ce-simple/tools"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to stop process by PID file
stop_by_pidfile() {
    local name=$1
    local pid_file=$2
    
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if ps -p "$pid" > /dev/null 2>&1; then
            print_status $YELLOW "Stopping $name (PID: $pid)..."
            
            # Try graceful shutdown
            kill "$pid"
            
            # Wait for graceful shutdown
            local count=0
            while ps -p "$pid" > /dev/null 2>&1 && [ $count -lt 10 ]; do
                sleep 1
                ((count++))
                echo -n "."
            done
            echo ""
            
            # Force kill if still running
            if ps -p "$pid" > /dev/null 2>&1; then
                print_status $YELLOW "Force killing $name..."
                kill -9 "$pid"
                sleep 1
            fi
            
            # Verify stopped
            if ! ps -p "$pid" > /dev/null 2>&1; then
                print_status $GREEN "✅ $name stopped successfully"
                rm -f "$pid_file"
                return 0
            else
                print_status $RED "❌ Failed to stop $name"
                return 1
            fi
        else
            print_status $YELLOW "$name PID file exists but process not running (cleaning up)"
            rm -f "$pid_file"
            return 0
        fi
    else
        print_status $YELLOW "$name is not running (no PID file)"
        return 0
    fi
}

# Function to find and kill processes by pattern
kill_by_pattern() {
    local pattern=$1
    local name=$2
    
    local pids=$(ps aux | grep -E "$pattern" | grep -v grep | grep -v "$0" | awk '{print $2}')
    
    if [ -n "$pids" ]; then
        print_status $YELLOW "Found $name processes: $pids"
        echo "$pids" | while read pid; do
            if [ -n "$pid" ]; then
                print_status $YELLOW "Stopping $name process (PID: $pid)..."
                kill "$pid"
                sleep 2
                
                # Force kill if still running
                if ps -p "$pid" > /dev/null 2>&1; then
                    kill -9 "$pid"
                fi
            fi
        done
        print_status $GREEN "✅ $name processes stopped"
    else
        print_status $YELLOW "$name processes not found"
    fi
}

# Function to stop all monitoring services
stop_all_monitors() {
    print_status $GREEN "🛑 CE-Simple Monitor Shutdown Initiated"
    echo "Timestamp: $(date -Iseconds)"
    echo ""
    
    # Stop health monitor
    print_status $GREEN "📊 Stopping Health Monitor..."
    stop_by_pidfile "Health Monitor" "$MONITOR_DIR/health_monitor.pid"
    
    # Stop efficiency dashboard if running
    print_status $GREEN "📈 Stopping Efficiency Dashboard..."
    stop_by_pidfile "Efficiency Dashboard" "$MONITOR_DIR/dashboard.pid"
    
    # Stop any other monitoring processes
    print_status $GREEN "🔍 Searching for other CE-Simple processes..."
    
    # Kill any system-health.py processes
    kill_by_pattern "system-health\.py" "System Health"
    
    # Kill any dashboard processes
    kill_by_pattern "efficiency-dashboard\.py" "Dashboard"
    
    # Kill any monitoring processes
    kill_by_pattern "claude-code.*monitor" "Claude Code Monitor"
    
    # Kill any other CE-Simple related processes
    kill_by_pattern "ce-simple.*\.py" "CE-Simple Python"
    
    echo ""
    print_status $GREEN "🧹 Cleanup Operations..."
    
    # Clean up stale PID files
    local pid_files=$(find "$MONITOR_DIR" -name "*.pid" 2>/dev/null || true)
    if [ -n "$pid_files" ]; then
        echo "$pid_files" | while read pid_file; do
            if [ -f "$pid_file" ]; then
                local pid=$(cat "$pid_file" 2>/dev/null || echo "")
                if [ -n "$pid" ] && ! ps -p "$pid" > /dev/null 2>&1; then
                    print_status $YELLOW "Removing stale PID file: $(basename "$pid_file")"
                    rm -f "$pid_file"
                fi
            fi
        done
    fi
    
    # Update status files
    local status_files=$(find "$MONITOR_DIR" -name "*status*.json" 2>/dev/null || true)
    if [ -n "$status_files" ]; then
        echo "$status_files" | while read status_file; do
            if [ -f "$status_file" ]; then
                local service_name=$(basename "$status_file" .json | sed 's/_status//')
                cat > "$status_file" << EOF
{
    "status": "stopped",
    "stopped_at": "$(date -Iseconds)",
    "stopped_by": "stop_all_monitors.sh",
    "reason": "manual_shutdown"
}
EOF
                print_status $GREEN "Updated status file: $(basename "$status_file")"
            fi
        done
    fi
    
    echo ""
    print_status $GREEN "📋 Final Status Check..."
    
    # Verify no CE-Simple processes are running
    local remaining=$(ps aux | grep -E "(system-health|efficiency-dashboard|claude.*monitor)" | grep -v grep | grep -v "$0")
    if [ -n "$remaining" ]; then
        print_status $RED "⚠️  Some processes may still be running:"
        echo "$remaining" | sed 's/^/  /'
        echo ""
        print_status $YELLOW "You may need to manually kill these processes"
    else
        print_status $GREEN "✅ All CE-Simple monitoring processes stopped"
    fi
    
    # Show disk space freed (if any large log files were cleaned)
    local log_size=$(du -sh "$MONITOR_DIR" 2>/dev/null | cut -f1 || echo "N/A")
    print_status $GREEN "📁 Monitoring directory size: $log_size"
    
    echo ""
    print_status $GREEN "🎯 Shutdown Complete!"
    print_status $YELLOW "To restart monitoring, run:"
    echo "  ./tools/launchers/start_health_monitor.sh start"
}

# Function to emergency kill all
emergency_kill() {
    print_status $RED "🚨 EMERGENCY SHUTDOWN - Force killing all processes"
    
    # Force kill by pattern (no graceful shutdown)
    pkill -9 -f "system-health" 2>/dev/null || true
    pkill -9 -f "efficiency-dashboard" 2>/dev/null || true
    pkill -9 -f "claude.*monitor" 2>/dev/null || true
    
    # Clean up all PID files
    rm -f "$MONITOR_DIR"/*.pid 2>/dev/null || true
    
    print_status $GREEN "✅ Emergency shutdown complete"
}

# Function to show what would be stopped
dry_run() {
    print_status $GREEN "🔍 DRY RUN - What would be stopped:"
    echo ""
    
    if [ -f "$MONITOR_DIR/health_monitor.pid" ]; then
        local pid=$(cat "$MONITOR_DIR/health_monitor.pid")
        if ps -p "$pid" > /dev/null 2>&1; then
            echo "  ✅ Health Monitor (PID: $pid)"
        else
            echo "  🧹 Health Monitor (stale PID file)"
        fi
    else
        echo "  ❌ Health Monitor (not running)"
    fi
    
    local other_processes=$(ps aux | grep -E "(system-health|dashboard|claude.*monitor)" | grep -v grep | grep -v "$0")
    if [ -n "$other_processes" ]; then
        echo "  📋 Other CE-Simple processes:"
        echo "$other_processes" | sed 's/^/    /'
    fi
    
    echo ""
    print_status $YELLOW "Run without --dry-run to execute shutdown"
}

# Main command handling
case "${1:-stop}" in
    stop|shutdown)
        stop_all_monitors
        ;;
    emergency|force)
        emergency_kill
        ;;
    dry-run|--dry-run)
        dry_run
        ;;
    *)
        echo "Usage: $0 {stop|emergency|dry-run}"
        echo ""
        echo "CE-Simple Monitor Shutdown Script"
        echo "Gracefully stops all background monitoring processes"
        echo ""
        echo "Commands:"
        echo "  stop      - Graceful shutdown of all monitors (default)"
        echo "  emergency - Force kill all processes immediately"
        echo "  dry-run   - Show what would be stopped without doing it"
        echo ""
        echo "Files managed:"
        echo "  PID files: $MONITOR_DIR/*.pid"
        echo "  Status:    $MONITOR_DIR/*status*.json"
        echo "  Logs:      $MONITOR_DIR/*.log"
        exit 1
        ;;
esac