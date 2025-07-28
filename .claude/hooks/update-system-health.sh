#!/bin/bash

# Update System Health Hook
# Updates system health metrics after significant operations
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="update-system-health"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
HEALTH_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/system-health-updates.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
TOOL_ARGS="$1"
TOOL_OUTPUT="$2"

# Health monitoring paths
HEALTH_SCRIPT="/Users/nalve/ce-simple/tools/monitoring/system-health.py"
HEALTH_DATA_DIR="/Users/nalve/ce-simple/data/monitoring"
HEALTH_DB="$HEALTH_DATA_DIR/health.db"
DAEMON_STATUS="$HEALTH_DATA_DIR/health_daemon_status.json"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Determine if operation is significant
is_significant_operation() {
    local tool_args="$1"
    local tool_output="$2"
    
    # Check for operations that significantly impact system state
    case "$tool_args" in
        *python*|*node*|*npm*|*docker*|*git*)
            return 0  # Significant
            ;;
        *)
            # Check output size as indicator of significance
            local output_length=${#tool_output}
            if [[ "$output_length" -gt 1000 ]]; then
                return 0  # Significant based on output size
            fi
            ;;
    esac
    
    return 1  # Not significant
}

# Extract operation category
categorize_operation() {
    local tool_args="$1"
    
    case "$tool_args" in
        *git*)
            echo "git_operation"
            ;;
        *python*)
            echo "python_execution"
            ;;
        *node*|*npm*)
            echo "node_operation"
            ;;
        *docker*)
            echo "docker_operation"
            ;;
        *compile*|*build*)
            echo "build_operation"
            ;;
        *test*)
            echo "test_execution"
            ;;
        *)
            echo "general_operation"
            ;;
    esac
}

# Check system resource impact
assess_resource_impact() {
    local tool_args="$1"
    local tool_output="$2"
    
    # Initialize impact score (0-100, higher = more impact)
    local impact_score=10  # Base score
    
    # Check for resource-intensive operations
    case "$tool_args" in
        *compile*|*build*|*webpack*|*babel*)
            impact_score=80
            ;;
        *test*|*npm*|*pip*)
            impact_score=60
            ;;
        *docker*|*container*)
            impact_score=70
            ;;
        *python*|*node*)
            impact_score=40
            ;;
        *git*)
            impact_score=20
            ;;
    esac
    
    # Adjust based on output indicators
    if echo "$tool_output" | grep -qi "error\|failed\|exception"; then
        impact_score=$((impact_score + 20))  # Errors increase impact
    fi
    
    if echo "$tool_output" | grep -qi "memory\|cpu\|resource"; then
        impact_score=$((impact_score + 15))  # Resource mentions
    fi
    
    # Output length factor
    local output_length=${#tool_output}
    if [[ "$output_length" -gt 10000 ]]; then
        impact_score=$((impact_score + 10))
    elif [[ "$output_length" -gt 5000 ]]; then
        impact_score=$((impact_score + 5))
    fi
    
    # Cap at 100
    if [[ "$impact_score" -gt 100 ]]; then
        impact_score=100
    fi
    
    echo "$impact_score"
}

# Gather current system metrics
gather_system_metrics() {
    python3 -c "
import json
import psutil
import time
import os
from datetime import datetime

try:
    metrics = {
        'timestamp': time.time(),
        'datetime': datetime.now().isoformat(),
        'cpu': {
            'percent': psutil.cpu_percent(interval=0.5),
            'count': psutil.cpu_count(),
            'load_avg': list(psutil.getloadavg()) if hasattr(psutil, 'getloadavg') else [0, 0, 0]
        },
        'memory': {
            'percent': psutil.virtual_memory().percent,
            'available': psutil.virtual_memory().available,
            'total': psutil.virtual_memory().total,
            'used': psutil.virtual_memory().used
        },
        'disk': {
            'percent': psutil.disk_usage('/').percent,
            'free': psutil.disk_usage('/').free,
            'total': psutil.disk_usage('/').total
        },
        'processes': len(psutil.pids()),
        'boot_time': psutil.boot_time()
    }
    
    # Add I/O stats if available
    if psutil.disk_io_counters():
        disk_io = psutil.disk_io_counters()
        metrics['disk_io'] = {
            'read_bytes': disk_io.read_bytes,
            'write_bytes': disk_io.write_bytes,
            'read_count': disk_io.read_count,
            'write_count': disk_io.write_count
        }
    
    if psutil.net_io_counters():
        net_io = psutil.net_io_counters()
        metrics['network_io'] = {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
            'packets_sent': net_io.packets_sent,
            'packets_recv': net_io.packets_recv
        }
    
    print(json.dumps(metrics, indent=2))
    
except ImportError:
    # Fallback if psutil not available
    metrics = {
        'timestamp': time.time(),
        'datetime': datetime.now().isoformat(),
        'fallback': True,
        'load_avg': os.getloadavg() if hasattr(os, 'getloadavg') else [0, 0, 0],
        'message': 'psutil not available - using basic metrics'
    }
    print(json.dumps(metrics, indent=2))
    
except Exception as e:
    error_metrics = {
        'timestamp': time.time(),
        'datetime': datetime.now().isoformat(),
        'error': str(e),
        'message': 'Failed to gather system metrics'
    }
    print(json.dumps(error_metrics, indent=2))
" 2>/dev/null || echo '{"error": "Failed to gather metrics", "timestamp": '$(date +%s)'}'
}

# Calculate health score based on metrics and operation impact
calculate_health_score() {
    local metrics_json="$1"
    local impact_score="$2"
    local operation_category="$3"
    
    python3 -c "
import json
import sys

metrics_json = '''$metrics_json'''
impact_score = int('$impact_score')
operation_category = '$operation_category'

try:
    metrics = json.loads(metrics_json)
    
    # Start with base score
    health_score = 100
    
    # Penalize high resource usage
    if 'cpu' in metrics and 'percent' in metrics['cpu']:
        cpu_percent = metrics['cpu']['percent']
        if cpu_percent > 90:
            health_score -= 30
        elif cpu_percent > 70:
            health_score -= 20
        elif cpu_percent > 50:
            health_score -= 10
    
    if 'memory' in metrics and 'percent' in metrics['memory']:
        memory_percent = metrics['memory']['percent']
        if memory_percent > 90:
            health_score -= 25
        elif memory_percent > 80:
            health_score -= 15
        elif memory_percent > 70:
            health_score -= 10
    
    if 'disk' in metrics and 'percent' in metrics['disk']:
        disk_percent = metrics['disk']['percent']
        if disk_percent > 95:
            health_score -= 20
        elif disk_percent > 90:
            health_score -= 15
        elif disk_percent > 85:
            health_score -= 10
    
    # Factor in operation impact
    impact_penalty = impact_score * 0.3  # Scale impact to health penalty
    health_score -= impact_penalty
    
    # Adjust based on operation category
    category_adjustments = {
        'git_operation': -2,
        'python_execution': -5,
        'node_operation': -8,
        'docker_operation': -10,
        'build_operation': -15,
        'test_execution': -5,
        'general_operation': 0
    }
    
    health_score += category_adjustments.get(operation_category, 0)
    
    # Ensure score is in valid range
    health_score = max(0, min(100, health_score))
    
    print(f'{health_score:.1f}')
    
except Exception as e:
    print('75.0')  # Default health score if calculation fails
"
}

# Update health database
update_health_database() {
    local health_score="$1"
    local metrics_json="$2"
    local operation_category="$3"
    local impact_score="$4"
    
    # Create health data directory if needed
    mkdir -p "$HEALTH_DATA_DIR"
    
    # Use Python to update SQLite database
    python3 -c "
import sqlite3
import json
import time
from datetime import datetime

db_path = '$HEALTH_DB'
health_score = float('$health_score')
metrics_json = '''$metrics_json'''
operation_category = '$operation_category'
impact_score = int('$impact_score')

try:
    # Connect to database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS health_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL NOT NULL,
            datetime TEXT NOT NULL,
            health_score REAL NOT NULL,
            operation_category TEXT,
            impact_score INTEGER,
            system_metrics TEXT,
            trigger_source TEXT
        )
    ''')
    
    # Insert new record
    cursor.execute('''
        INSERT INTO health_metrics 
        (timestamp, datetime, health_score, operation_category, impact_score, system_metrics, trigger_source)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        time.time(),
        datetime.now().isoformat(),
        health_score,
        operation_category,
        impact_score,
        metrics_json,
        'hooks_system'
    ))
    
    conn.commit()
    conn.close()
    
    print(f'Health database updated: score={health_score}, category={operation_category}')
    
except Exception as e:
    print(f'Error updating health database: {e}')
" 2>/dev/null || log_message "WARN" "Failed to update health database"
}

# Update daemon status
update_daemon_status() {
    local health_score="$1"
    
    if [[ -f "$DAEMON_STATUS" ]]; then
        # Update daemon status with new health score
        python3 -c "
import json
from datetime import datetime

daemon_file = '$DAEMON_STATUS'
health_score = float('$health_score')

try:
    # Load current status
    with open(daemon_file, 'r') as f:
        status = json.load(f)
    
    # Update health score and timestamp
    status['health_score'] = health_score
    status['last_update'] = datetime.now().isoformat()
    
    # Write updated status
    with open(daemon_file, 'w') as f:
        json.dump(status, f, indent=2)
    
    print(f'Daemon status updated with health score: {health_score}')
    
except Exception as e:
    print(f'Error updating daemon status: {e}')
" 2>/dev/null || log_message "WARN" "Failed to update daemon status"
    fi
}

# Trigger health monitoring script
trigger_health_monitoring() {
    if [[ -f "$HEALTH_SCRIPT" ]]; then
        log_message "INFO" "Triggering system health monitoring script"
        
        # Run health script in background
        python3 "$HEALTH_SCRIPT" >/dev/null 2>&1 &
        local health_pid=$!
        
        log_message "INFO" "Health monitoring triggered (PID: $health_pid)"
    else
        log_message "WARN" "Health monitoring script not found: $HEALTH_SCRIPT"
    fi
}

# Generate health update report
generate_health_report() {
    local operation_category="$1"
    local impact_score="$2"
    local health_score="$3"
    local tool_args="$4"
    
    cat >> "$HEALTH_LOG_FILE" << EOF
[$TIMESTAMP] HEALTH_UPDATE
Operation: $operation_category
Command: $tool_args
Impact Score: $impact_score/100
Health Score: $health_score/100
Session: ${CLAUDE_SESSION_ID:-unknown}
Workflow: ${CLAUDE_WORKFLOW_CONTEXT:-none}
Triggered By: post-tool-hook
---
EOF
}

# Check for health alerts
check_health_alerts() {
    local health_score="$1"
    local operation_category="$2"
    local impact_score="$3"
    
    # Alert thresholds
    local critical_threshold=25
    local warning_threshold=50
    
    if (( $(echo "$health_score < $critical_threshold" | bc -l 2>/dev/null || echo "0") )); then
        log_message "CRITICAL" "System health critical: $health_score/100 after $operation_category"
        
        # Create critical alert
        local alert_file="/Users/nalve/ce-simple/.claude/logs/alerts/health-critical-$(date +%Y%m%d-%H%M%S).alert"
        mkdir -p "$(dirname "$alert_file")"
        
        cat > "$alert_file" << EOF
Alert Type: Critical System Health
Health Score: $health_score/100
Operation: $operation_category
Impact Score: $impact_score/100
Timestamp: $TIMESTAMP
Requires Immediate Attention: Yes
Suggested Actions: Check system resources, restart if necessary
EOF
        
    elif (( $(echo "$health_score < $warning_threshold" | bc -l 2>/dev/null || echo "0") )); then
        log_message "WARN" "System health warning: $health_score/100 after $operation_category"
    fi
}

# Main system health update function
update_system_health() {
    local tool_args="$1"
    local tool_output="$2"
    
    log_message "INFO" "Updating system health metrics"
    
    # Check if this is a significant operation
    if ! is_significant_operation "$tool_args" "$tool_output"; then
        log_message "INFO" "Operation not significant enough for health update"
        return 0
    fi
    
    # Categorize the operation
    local operation_category
    operation_category=$(categorize_operation "$tool_args")
    
    # Assess resource impact
    local impact_score
    impact_score=$(assess_resource_impact "$tool_args" "$tool_output")
    
    log_message "INFO" "Operation: $operation_category, Impact: $impact_score/100"
    
    # Gather current system metrics
    local metrics_json
    metrics_json=$(gather_system_metrics)
    
    # Calculate new health score
    local health_score
    health_score=$(calculate_health_score "$metrics_json" "$impact_score" "$operation_category")
    
    log_message "INFO" "Calculated health score: $health_score/100"
    
    # Update health database and daemon status
    update_health_database "$health_score" "$metrics_json" "$operation_category" "$impact_score"
    update_daemon_status "$health_score"
    
    # Generate report and check for alerts
    generate_health_report "$operation_category" "$impact_score" "$health_score" "$tool_args"
    check_health_alerts "$health_score" "$operation_category" "$impact_score"
    
    # Trigger health monitoring script for comprehensive analysis
    trigger_health_monitoring
    
    log_message "SUCCESS" "System health update completed: $health_score/100"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Health update should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "Health update error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "Health update issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for health update hooks
    exit 0
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$HEALTH_LOG_FILE")"
    mkdir -p "$HEALTH_DATA_DIR"
    
    # Validate input
    if [[ -z "$TOOL_ARGS" ]] || [[ -z "$TOOL_OUTPUT" ]]; then
        handle_error 1 "Missing tool arguments or output for health update"
    fi
    
    # Update system health
    update_system_health "$TOOL_ARGS" "$TOOL_OUTPUT"
    
    # Success
    log_message "SUCCESS" "System health update hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "System health update interrupted"; exit 0' INT TERM

# Execute main function
main "$@"