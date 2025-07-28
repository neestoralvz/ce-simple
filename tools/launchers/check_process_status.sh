#!/bin/bash
# CE-Simple Process Status Checker
# Claude Code integration for background process management

set -e

# Configuration
MONITOR_DIR="/Users/nalve/ce-simple/data/monitoring"
PID_FILE="$MONITOR_DIR/health_monitor.pid"
STATUS_FILE="$MONITOR_DIR/health_status.json"
LOG_FILE="$MONITOR_DIR/health_monitor.log"

# Function to check if process is running by PID
check_pid() {
    local pid_file="$1"
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if ps -p "$pid" > /dev/null 2>&1; then
            echo "$pid"
            return 0
        else
            return 1
        fi
    else
        return 1
    fi
}

# Function to get process info
get_process_info() {
    local pid="$1"
    if [ -n "$pid" ]; then
        ps -p "$pid" -o pid,ppid,cmd,etime,pcpu,pmem | tail -n +2
    fi
}

# Function to get system overview
get_system_overview() {
    echo "=== CE-Simple System Status Overview ==="
    echo "Timestamp: $(date -Iseconds)"
    echo ""
    
    # Health Monitor Status
    echo "🔍 Health Monitor:"
    if pid=$(check_pid "$PID_FILE"); then
        echo "  Status: ✅ RUNNING (PID: $pid)"
        echo "  Process Info:"
        get_process_info "$pid" | sed 's/^/    /'
        
        # Show memory/CPU usage
        local mem_usage=$(ps -p "$pid" -o pmem --no-headers | tr -d ' ')
        local cpu_usage=$(ps -p "$pid" -o pcpu --no-headers | tr -d ' ')
        echo "  Resource Usage: CPU: ${cpu_usage}%, Memory: ${mem_usage}%"
        
        # Check log file size and recent activity
        if [ -f "$LOG_FILE" ]; then
            local log_size=$(du -h "$LOG_FILE" | cut -f1)
            local last_log=$(tail -n 1 "$LOG_FILE" 2>/dev/null || echo "No recent logs")
            echo "  Log Size: $log_size"
            echo "  Last Activity: $last_log"
        fi
    else
        echo "  Status: ❌ NOT RUNNING"
        if [ -f "$STATUS_FILE" ]; then
            echo "  Last Status:"
            cat "$STATUS_FILE" | sed 's/^/    /'
        fi
    fi
    
    echo ""
    
    # Related Python processes
    echo "🐍 Python Processes (CE-Simple related):"
    local py_processes=$(ps aux | grep -E "(system-health|monitoring|claude)" | grep -v grep | grep -v "$0")
    if [ -n "$py_processes" ]; then
        echo "$py_processes" | while read line; do
            echo "  $line"
        done
    else
        echo "  No related Python processes found"
    fi
    
    echo ""
    
    # Database status
    echo "💾 Database Status:"
    local db_file="$MONITOR_DIR/health.db"
    if [ -f "$db_file" ]; then
        local db_size=$(du -h "$db_file" | cut -f1)
        echo "  Health DB: ✅ EXISTS ($db_size)"
        
        # Try to get record count (if sqlite3 is available)
        if command -v sqlite3 >/dev/null 2>&1; then
            local record_count=$(sqlite3 "$db_file" "SELECT COUNT(*) FROM health_metrics;" 2>/dev/null || echo "N/A")
            echo "  Records: $record_count health metrics"
        fi
    else
        echo "  Health DB: ❌ NOT FOUND"
    fi
    
    echo ""
    
    # File system status
    echo "📁 Monitoring Files:"
    for file in "$PID_FILE" "$STATUS_FILE" "$LOG_FILE"; do
        if [ -f "$file" ]; then
            local size=$(du -h "$file" | cut -f1)
            local mod_time=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$file")
            echo "  ✅ $(basename "$file"): $size (modified: $mod_time)"
        else
            echo "  ❌ $(basename "$file"): NOT FOUND"
        fi
    done
}

# Function to get detailed status
get_detailed_status() {
    get_system_overview
    
    echo ""
    echo "=== Detailed Analysis ==="
    
    # Port usage (if monitoring uses ports)
    echo ""
    echo "🔌 Network Status:"
    local ports=$(lsof -i -P | grep -E "(python|Claude)" | grep LISTEN || echo "No listening ports found")
    if [ "$ports" != "No listening ports found" ]; then
        echo "$ports" | sed 's/^/  /'
    else
        echo "  $ports"
    fi
    
    # Recent log analysis
    if [ -f "$LOG_FILE" ]; then
        echo ""
        echo "📋 Recent Log Activity (last 10 lines):"
        tail -n 10 "$LOG_FILE" | sed 's/^/  /'
    fi
    
    # System resource overview
    echo ""
    echo "⚡ System Resources:"
    echo "  Load Average: $(uptime | awk -F'load average:' '{print $2}')"
    echo "  Memory Usage: $(top -l 1 | grep "PhysMem" | awk '{print $2}' | tr -d ',')"
    echo "  Disk Space: $(df -h . | tail -1 | awk '{print $4 " available of " $2}')"
}

# Function for JSON output (for Claude Code integration)
get_json_status() {
    local status="stopped"
    local pid=""
    local uptime=""
    local memory=""
    local cpu=""
    
    if pid=$(check_pid "$PID_FILE"); then
        status="running"
        local process_info=$(ps -p "$pid" -o etime,pcpu,pmem --no-headers)
        uptime=$(echo "$process_info" | awk '{print $1}')
        cpu=$(echo "$process_info" | awk '{print $2}')
        memory=$(echo "$process_info" | awk '{print $3}')
    fi
    
    # Database info
    local db_exists="false"
    local db_size="0"
    local record_count="0"
    
    if [ -f "$MONITOR_DIR/health.db" ]; then
        db_exists="true"
        db_size=$(stat -f%z "$MONITOR_DIR/health.db" 2>/dev/null || echo "0")
        if command -v sqlite3 >/dev/null 2>&1; then
            record_count=$(sqlite3 "$MONITOR_DIR/health.db" "SELECT COUNT(*) FROM health_metrics;" 2>/dev/null || echo "0")
        fi
    fi
    
    cat << EOF
{
    "timestamp": "$(date -Iseconds)",
    "health_monitor": {
        "status": "$status",
        "pid": "$pid",
        "uptime": "$uptime",
        "cpu_percent": "$cpu",
        "memory_percent": "$memory"
    },
    "database": {
        "exists": $db_exists,
        "size_bytes": $db_size,
        "health_records": $record_count
    },
    "files": {
        "pid_file_exists": $([ -f "$PID_FILE" ] && echo "true" || echo "false"),
        "log_file_exists": $([ -f "$LOG_FILE" ] && echo "true" || echo "false"),
        "status_file_exists": $([ -f "$STATUS_FILE" ] && echo "true" || echo "false")
    }
}
EOF
}

# Function for compact status (one line)
get_compact_status() {
    if pid=$(check_pid "$PID_FILE"); then
        local uptime=$(ps -p "$pid" -o etime --no-headers | tr -d ' ')
        echo "✅ Health Monitor: RUNNING (PID: $pid, Uptime: $uptime)"
    else
        echo "❌ Health Monitor: STOPPED"
    fi
}

# Main command handling
case "${1:-overview}" in
    overview|status)
        get_system_overview
        ;;
    detailed)
        get_detailed_status
        ;;
    json)
        get_json_status
        ;;
    compact)
        get_compact_status
        ;;
    pid)
        if pid=$(check_pid "$PID_FILE"); then
            echo "$pid"
        else
            echo "0"
            exit 1
        fi
        ;;
    running)
        if check_pid "$PID_FILE" >/dev/null; then
            echo "true"
            exit 0
        else
            echo "false"
            exit 1
        fi
        ;;
    *)
        echo "Usage: $0 {overview|detailed|json|compact|pid|running}"
        echo ""
        echo "CE-Simple Process Status Checker"
        echo "Provides status information for background processes"
        echo ""
        echo "Commands:"
        echo "  overview  - System overview (default)"
        echo "  detailed  - Detailed status with logs and resources"
        echo "  json      - JSON formatted status (for Claude Code)"
        echo "  compact   - One-line status summary"
        echo "  pid       - Return PID if running (exit 1 if not)"
        echo "  running   - Return true/false if process is running"
        echo ""
        echo "Integration with Claude Code:"
        echo "  Use 'json' or 'compact' modes for programmatic access"
        exit 1
        ;;
esac