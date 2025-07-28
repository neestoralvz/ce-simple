#!/bin/bash

# End Performance Timer Hook
# Completes performance timing and logs metrics for analysis
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="end-performance-timer"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
PERFORMANCE_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/performance.log"
METRICS_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/performance-metrics.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
TOOL_NAME="$1"
TOOL_OUTPUT="$2"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Get high precision timestamp
get_precision_timestamp() {
    python3 -c "import time; print(f'{time.time():.6f}')" 2>/dev/null || date +%s
}

# Find matching timer file
find_timer_file() {
    local tool_name="$1"
    local timer_id="${CLAUDE_PERFORMANCE_TIMER_ID:-}"
    
    # Try to find timer file by ID first
    if [[ -n "$timer_id" ]] && [[ -f "/tmp/claude-performance-timer-$timer_id.json" ]]; then
        echo "/tmp/claude-performance-timer-$timer_id.json"
        return 0
    fi
    
    # Fall back to finding by tool name (get most recent)
    local timer_file
    timer_file=$(find /tmp -name "claude-performance-timer-${tool_name,,}-*.json" -type f -printf '%T@ %p\n' 2>/dev/null | sort -nr | head -1 | cut -d' ' -f2 || echo "")
    
    if [[ -n "$timer_file" ]] && [[ -f "$timer_file" ]]; then
        echo "$timer_file"
        return 0
    fi
    
    return 1
}

# Calculate performance metrics
calculate_metrics() {
    local timer_file="$1"
    local end_timestamp="$2"
    local tool_output="$3"
    
    python3 -c "
import json
import time
import sys
from datetime import datetime

timer_file = '$timer_file'
end_timestamp = float('$end_timestamp')
tool_output = '''$tool_output'''

try:
    # Load timer data
    with open(timer_file, 'r') as f:
        timer_data = json.load(f)
    
    start_timestamp = timer_data['start_timestamp']
    
    # Calculate basic metrics
    duration = end_timestamp - start_timestamp
    duration_ms = duration * 1000
    
    # Analyze tool output
    output_length = len(tool_output)
    output_lines = tool_output.count('\n') + 1
    has_errors = any(keyword in tool_output.lower() for keyword in ['error', 'failed', 'exception', 'timeout'])
    
    # Calculate performance score
    score = 100
    
    # Penalize long execution times
    expected_duration = 3.0  # Default 3 seconds
    tool_category = timer_data.get('tool_context', {}).get('tool_category', 'general')
    
    if tool_category == 'network_operation':
        expected_duration = 5.0
    elif tool_category == 'file_operation':
        expected_duration = 1.0
    elif tool_category == 'search_operation':
        expected_duration = 2.0
    
    if duration > expected_duration * 2:
        score -= 40
    elif duration > expected_duration:
        score -= 20
    
    # Penalize errors
    if has_errors:
        score -= 30
    
    # Penalize excessive output (may indicate inefficiency)
    if output_length > 50000:
        score -= 20
    elif output_length > 20000:
        score -= 10
    
    # Bonus for fast execution
    if duration < expected_duration * 0.5:
        score += 10
    
    # Ensure score is in valid range
    score = max(0, min(100, score))
    
    # Create metrics object
    metrics = {
        'timer_id': timer_data['timer_id'],
        'tool_name': timer_data['tool_name'],
        'start_timestamp': start_timestamp,
        'end_timestamp': end_timestamp,
        'duration_seconds': round(duration, 6),
        'duration_ms': round(duration_ms, 2),
        'expected_duration': expected_duration,
        'performance_score': score,
        'output_analysis': {
            'length': output_length,
            'lines': output_lines,
            'has_errors': has_errors
        },
        'system_context': timer_data.get('system_context', {}),
        'tool_context': timer_data.get('tool_context', {}),
        'session_id': timer_data.get('session_id', 'unknown'),
        'workflow_context': timer_data.get('workflow_context', 'none'),
        'completed_at': datetime.fromtimestamp(end_timestamp).isoformat()
    }
    
    # Output metrics as JSON
    print(json.dumps(metrics, indent=2))
    
except FileNotFoundError:
    print(f'Timer file not found: {timer_file}', file=sys.stderr)
    sys.exit(1)
except Exception as e:
    print(f'Error calculating metrics: {e}', file=sys.stderr)
    sys.exit(1)
"
}

# Capture performance baseline delta
capture_performance_delta() {
    local timer_id="$1"
    local baseline_file="/tmp/claude-performance-baseline-$timer_id.json"
    local delta_file="/tmp/claude-performance-delta-$timer_id.json"
    
    if [[ ! -f "$baseline_file" ]]; then
        log_message "WARN" "Performance baseline file not found: $baseline_file"
        return 1
    fi
    
    # Capture end state and calculate delta
    python3 -c "
import json
import psutil
import time
from datetime import datetime

baseline_file = '$baseline_file'
delta_file = '$delta_file'

try:
    # Load baseline
    with open(baseline_file, 'r') as f:
        baseline = json.load(f)
    
    # Capture current state
    current = {
        'timestamp': time.time(),
        'cpu_percent': psutil.cpu_percent(interval=0.1),
        'memory_percent': psutil.virtual_memory().percent,
        'disk_io': dict(psutil.disk_io_counters()._asdict()) if psutil.disk_io_counters() else {},
        'network_io': dict(psutil.net_io_counters()._asdict()) if psutil.net_io_counters() else {},
        'process_count': len(psutil.pids()),
        'load_average': psutil.getloadavg() if hasattr(psutil, 'getloadavg') else [0, 0, 0]
    }
    
    # Calculate deltas
    delta = {
        'time_elapsed': current['timestamp'] - baseline['timestamp'],
        'cpu_delta': current['cpu_percent'] - baseline.get('cpu_percent', 0),
        'memory_delta': current['memory_percent'] - baseline.get('memory_percent', 0),
        'process_delta': current['process_count'] - baseline.get('process_count', 0),
        'baseline': baseline,
        'current': current
    }
    
    # Calculate I/O deltas if available
    if baseline.get('disk_io') and current.get('disk_io'):
        delta['disk_read_delta'] = current['disk_io'].get('read_bytes', 0) - baseline['disk_io'].get('read_bytes', 0)
        delta['disk_write_delta'] = current['disk_io'].get('write_bytes', 0) - baseline['disk_io'].get('write_bytes', 0)
    
    if baseline.get('network_io') and current.get('network_io'):
        delta['network_sent_delta'] = current['network_io'].get('bytes_sent', 0) - baseline['network_io'].get('bytes_sent', 0)
        delta['network_recv_delta'] = current['network_io'].get('bytes_recv', 0) - baseline['network_io'].get('bytes_recv', 0)
    
    # Save delta
    with open(delta_file, 'w') as f:
        json.dump(delta, f, indent=2)
    
    print('Performance delta captured')
    
except ImportError:
    # Fallback if psutil not available
    delta = {
        'fallback': True,
        'message': 'psutil not available - no delta calculated'
    }
    with open(delta_file, 'w') as f:
        json.dump(delta, f, indent=2)
    print('Basic delta captured')
    
except Exception as e:
    print(f'Error capturing delta: {e}')
" 2>/dev/null || log_message "WARN" "Failed to capture performance delta"
}

# Log performance metrics
log_performance_metrics() {
    local metrics_json="$1"
    
    # Extract key metrics for logging
    local duration score tool_name timer_id
    duration=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['duration_seconds'])")
    score=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['performance_score'])")
    tool_name=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['tool_name'])")
    timer_id=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['timer_id'])")
    
    # Log to performance log
    cat >> "$PERFORMANCE_LOG_FILE" << EOF
[$TIMESTAMP] TIMER_END
Tool: $tool_name
Timer ID: $timer_id
Duration: ${duration}s
Performance Score: $score/100
Output Length: $(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['output_analysis']['length'])")
Has Errors: $(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print('yes' if data['output_analysis']['has_errors'] else 'no')")
Session: $(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['session_id'])")
---
EOF
    
    # Log full metrics to detailed log
    cat >> "$METRICS_LOG_FILE" << EOF
[$TIMESTAMP] PERFORMANCE_METRICS
$metrics_json
---
EOF
    
    log_message "INFO" "Performance metrics logged: $tool_name (${duration}s, score: $score/100)"
}

# Update performance statistics
update_performance_statistics() {
    local metrics_json="$1"
    local stats_file="/Users/nalve/ce-simple/.claude/logs/performance-statistics.json"
    
    # Create stats file if it doesn't exist
    if [[ ! -f "$stats_file" ]]; then
        cat > "$stats_file" << 'EOF'
{
    "last_updated": "",
    "total_operations": 0,
    "tools": {},
    "performance": {
        "average_duration": 0,
        "average_score": 0,
        "fast_operations": 0,
        "slow_operations": 0,
        "error_operations": 0
    },
    "trends": {
        "last_24h": [],
        "daily_averages": {}
    }
}
EOF
    fi
    
    # Update statistics
    python3 -c "
import json
import sys
from datetime import datetime, date

stats_file = '$stats_file'
metrics_json = '''$metrics_json'''

try:
    # Load current stats
    with open(stats_file, 'r') as f:
        stats = json.load(f)
    
    # Parse metrics
    metrics = json.loads(metrics_json)
    tool_name = metrics['tool_name']
    duration = metrics['duration_seconds']
    score = metrics['performance_score']
    has_errors = metrics['output_analysis']['has_errors']
    
    # Update general stats
    stats['last_updated'] = datetime.now().isoformat()
    stats['total_operations'] += 1
    
    # Update tool-specific stats
    if tool_name not in stats['tools']:
        stats['tools'][tool_name] = {
            'count': 0,
            'total_duration': 0,
            'total_score': 0,
            'average_duration': 0,
            'average_score': 0,
            'error_count': 0,
            'last_used': ''
        }
    
    tool_stats = stats['tools'][tool_name]
    tool_stats['count'] += 1
    tool_stats['total_duration'] += duration
    tool_stats['total_score'] += score
    tool_stats['average_duration'] = tool_stats['total_duration'] / tool_stats['count']
    tool_stats['average_score'] = tool_stats['total_score'] / tool_stats['count']
    tool_stats['last_used'] = datetime.now().isoformat()
    
    if has_errors:
        tool_stats['error_count'] += 1
    
    # Update performance categories
    if duration < 1.0:
        stats['performance']['fast_operations'] += 1
    elif duration > 5.0:
        stats['performance']['slow_operations'] += 1
    
    if has_errors:
        stats['performance']['error_operations'] += 1
    
    # Calculate overall averages
    total_duration = sum(tool_data['total_duration'] for tool_data in stats['tools'].values())
    total_score = sum(tool_data['total_score'] for tool_data in stats['tools'].values())
    total_ops = stats['total_operations']
    
    stats['performance']['average_duration'] = total_duration / total_ops if total_ops > 0 else 0
    stats['performance']['average_score'] = total_score / total_ops if total_ops > 0 else 0
    
    # Update trends (last 24h)
    trend_entry = {
        'timestamp': datetime.now().isoformat(),
        'tool': tool_name,
        'duration': duration,
        'score': score,
        'has_errors': has_errors
    }
    
    stats['trends']['last_24h'].append(trend_entry)
    # Keep only last 100 entries
    if len(stats['trends']['last_24h']) > 100:
        stats['trends']['last_24h'] = stats['trends']['last_24h'][-100:]
    
    # Update daily averages
    today = date.today().isoformat()
    if today not in stats['trends']['daily_averages']:
        stats['trends']['daily_averages'][today] = {
            'count': 0,
            'total_duration': 0,
            'total_score': 0,
            'error_count': 0
        }
    
    daily = stats['trends']['daily_averages'][today]
    daily['count'] += 1
    daily['total_duration'] += duration
    daily['total_score'] += score
    if has_errors:
        daily['error_count'] += 1
    
    # Calculate daily averages
    daily['average_duration'] = daily['total_duration'] / daily['count']
    daily['average_score'] = daily['total_score'] / daily['count']
    
    # Write updated stats
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
    
    print('Performance statistics updated')
    
except Exception as e:
    print(f'Error updating performance statistics: {e}', file=sys.stderr)
" 2>/dev/null || log_message "WARN" "Failed to update performance statistics"
}

# Generate performance alerts
check_performance_alerts() {
    local metrics_json="$1"
    
    # Extract key metrics for alert checking
    local duration score has_errors tool_name
    duration=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['duration_seconds'])")
    score=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['performance_score'])")
    has_errors=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['output_analysis']['has_errors'])")
    tool_name=$(echo "$metrics_json" | python3 -c "import json, sys; data=json.load(sys.stdin); print(data['tool_name'])")
    
    # Alert for poor performance
    if (( $(echo "$score < 30" | bc -l 2>/dev/null || echo "0") )); then
        log_message "ALERT" "Poor performance detected: $tool_name (score: $score/100, duration: ${duration}s)"
        
        # Create alert file
        local alert_file="/Users/nalve/ce-simple/.claude/logs/alerts/performance-$(date +%Y%m%d-%H%M%S).alert"
        mkdir -p "$(dirname "$alert_file")"
        
        cat > "$alert_file" << EOF
Alert Type: Performance Issue
Tool: $tool_name
Score: $score/100
Duration: ${duration}s
Has Errors: $has_errors
Timestamp: $TIMESTAMP
Metrics: $metrics_json
EOF
    fi
    
    # Alert for extremely slow operations
    if (( $(echo "$duration > 10.0" | bc -l 2>/dev/null || echo "0") )); then
        log_message "ALERT" "Slow operation detected: $tool_name (${duration}s)"
    fi
}

# Cleanup timer files
cleanup_timer_files() {
    local timer_file="$1"
    local timer_id="$2"
    
    # Remove timer file
    if [[ -f "$timer_file" ]]; then
        rm -f "$timer_file"
        log_message "INFO" "Timer file cleaned up: $timer_file"
    fi
    
    # Remove baseline file
    local baseline_file="/tmp/claude-performance-baseline-$timer_id.json"
    if [[ -f "$baseline_file" ]]; then
        rm -f "$baseline_file"
    fi
    
    # Remove delta file
    local delta_file="/tmp/claude-performance-delta-$timer_id.json"
    if [[ -f "$delta_file" ]]; then
        rm -f "$delta_file"
    fi
    
    # Clean environment
    unset CLAUDE_PERFORMANCE_TIMER_ID
    unset CLAUDE_HIGH_PRECISION_TIMING
}

# Main performance timer end function
end_performance_timer() {
    local tool_name="$1"
    local tool_output="$2"
    
    log_message "INFO" "Ending performance timer for: $tool_name"
    
    # Find matching timer file
    local timer_file
    if ! timer_file=$(find_timer_file "$tool_name"); then
        log_message "WARN" "No timer file found for $tool_name - may have been cleaned up or never started"
        return 0
    fi
    
    # Get end timestamp
    local end_timestamp
    end_timestamp=$(get_precision_timestamp)
    
    # Extract timer ID from file
    local timer_id
    timer_id=$(basename "$timer_file" .json | sed 's/claude-performance-timer-//')
    
    # Capture performance delta
    capture_performance_delta "$timer_id"
    
    # Calculate metrics
    log_message "INFO" "Calculating performance metrics for timer: $timer_id"
    local metrics_json
    if ! metrics_json=$(calculate_metrics "$timer_file" "$end_timestamp" "$tool_output"); then
        log_message "ERROR" "Failed to calculate performance metrics"
        return 1
    fi
    
    # Log metrics and update statistics
    log_performance_metrics "$metrics_json"
    update_performance_statistics "$metrics_json"
    check_performance_alerts "$metrics_json"
    
    # Cleanup timer files
    cleanup_timer_files "$timer_file" "$timer_id"
    
    log_message "SUCCESS" "Performance timer completed for: $tool_name"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Performance timer should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "Performance timer error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "Performance timer issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for performance hooks
    exit 0
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$PERFORMANCE_LOG_FILE")"
    mkdir -p "$(dirname "$METRICS_LOG_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_NAME" ]] || [[ -z "$TOOL_OUTPUT" ]]; then
        handle_error 1 "Missing tool name or output for performance timer end"
    fi
    
    # End performance timer
    end_performance_timer "$TOOL_NAME" "$TOOL_OUTPUT"
    
    # Success
    log_message "SUCCESS" "End performance timer hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "End performance timer interrupted"; exit 0' INT TERM

# Execute main function
main "$@"