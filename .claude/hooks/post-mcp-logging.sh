#!/bin/bash

# Post-MCP Tool Logging Hook
# Logs MCP tool usage and performance metrics for analysis and optimization
# Based on 2025 Claude Code hooks best practices

set -euo pipefail

# Configuration
HOOK_NAME="post-mcp-logging"
LOG_FILE="/Users/nalve/ce-simple/.claude/logs/hooks.log"
MCP_LOG_FILE="/Users/nalve/ce-simple/.claude/logs/mcp-operations.log"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# Parameters
TOOL_OUTPUT="$1"

# Logging function
log_message() {
    local level="$1"
    local message="$2"
    echo "[$TIMESTAMP] [$HOOK_NAME] [$level] $message" | tee -a "$LOG_FILE"
}

# Extract MCP tool information from environment
extract_mcp_info() {
    local tool_name="${CLAUDE_TOOL_NAME:-unknown}"
    local session_id="${CLAUDE_SESSION_ID:-none}"
    local execution_context="${CLAUDE_WORKFLOW_CONTEXT:-none}"
    
    echo "tool_name:$tool_name,session_id:$session_id,context:$execution_context"
}

# Analyze tool output for performance metrics
analyze_tool_output() {
    local output="$1"
    local output_length=${#output}
    local has_errors=false
    local execution_time="unknown"
    
    # Check for error indicators
    if echo "$output" | grep -qi "error\|failed\|exception\|timeout"; then
        has_errors=true
    fi
    
    # Try to extract execution time from output
    if echo "$output" | grep -q "took\|duration\|time"; then
        execution_time=$(echo "$output" | grep -oE "[0-9]+(\.[0-9]+)?\s*(ms|seconds?|minutes?)" | head -1 || echo "unknown")
    fi
    
    echo "length:$output_length,errors:$has_errors,time:$execution_time"
}

# Determine MCP tool category
categorize_mcp_tool() {
    local tool_name="$1"
    
    case "$tool_name" in
        *executeCode*)
            echo "code_execution"
            ;;
        *getDiagnostics*)
            echo "diagnostics"
            ;;
        *readFile*|*writeFile*)
            echo "file_operations"
            ;;
        *getProjectStructure*)
            echo "project_analysis"
            ;;
        *search*|*find*)
            echo "search_operations"
            ;;
        *)
            echo "general"
            ;;
    esac
}

# Extract context information
extract_context_info() {
    local context_info=""
    
    # Check for active workflow
    if [[ -f ".claude-workflow-active" ]]; then
        context_info+=",active_workflow:true"
    else
        context_info+=",active_workflow:false"
    fi
    
    # Check git state
    if git rev-parse --git-dir >/dev/null 2>&1; then
        local branch
        branch=$(git branch --show-current 2>/dev/null || echo "detached")
        context_info+=",git_branch:$branch"
        
        local changes
        changes=$(git status --porcelain | wc -l)
        context_info+=",git_changes:$changes"
    fi
    
    # Check system load
    local load_avg
    load_avg=$(uptime | awk -F'load average:' '{print $2}' | awk -F',' '{print $1}' | tr -d ' ')
    context_info+=",system_load:$load_avg"
    
    echo "$context_info"
}

# Generate performance score
calculate_performance_score() {
    local output_length="$1"
    local has_errors="$2"
    local execution_time="$3"
    
    local score=100
    
    # Penalize errors
    if [[ "$has_errors" == "true" ]]; then
        score=$((score - 50))
    fi
    
    # Penalize large outputs (may indicate inefficiency)
    if [[ "$output_length" -gt 10000 ]]; then
        score=$((score - 20))
    elif [[ "$output_length" -gt 5000 ]]; then
        score=$((score - 10))
    fi
    
    # Consider execution time if available
    if [[ "$execution_time" =~ ([0-9]+).*ms ]]; then
        local time_ms="${BASH_REMATCH[1]}"
        if [[ "$time_ms" -gt 5000 ]]; then
            score=$((score - 30))
        elif [[ "$time_ms" -gt 2000 ]]; then
            score=$((score - 15))
        fi
    elif [[ "$execution_time" =~ ([0-9]+).*second ]]; then
        local time_sec="${BASH_REMATCH[1]}"
        if [[ "$time_sec" -gt 10 ]]; then
            score=$((score - 40))
        elif [[ "$time_sec" -gt 5 ]]; then
            score=$((score - 25))
        fi
    fi
    
    # Ensure score is not negative
    if [[ "$score" -lt 0 ]]; then
        score=0
    fi
    
    echo "$score"
}

# Log MCP operation
log_mcp_operation() {
    local tool_output="$1"
    
    # Extract information
    local mcp_info
    mcp_info=$(extract_mcp_info)
    
    local output_analysis
    output_analysis=$(analyze_tool_output "$tool_output")
    
    local tool_name
    tool_name=$(echo "$mcp_info" | cut -d',' -f1 | cut -d':' -f2)
    
    local tool_category
    tool_category=$(categorize_mcp_tool "$tool_name")
    
    local context_info
    context_info=$(extract_context_info)
    
    # Parse analysis results
    local output_length
    output_length=$(echo "$output_analysis" | cut -d',' -f1 | cut -d':' -f2)
    
    local has_errors
    has_errors=$(echo "$output_analysis" | cut -d',' -f2 | cut -d':' -f2)
    
    local execution_time
    execution_time=$(echo "$output_analysis" | cut -d',' -f3 | cut -d':' -f2)
    
    local performance_score
    performance_score=$(calculate_performance_score "$output_length" "$has_errors" "$execution_time")
    
    # Create comprehensive log entry
    cat >> "$MCP_LOG_FILE" << EOF
[$TIMESTAMP] MCP Operation Log
Tool: $tool_name
Category: $tool_category
Session: $(echo "$mcp_info" | cut -d',' -f2 | cut -d':' -f2)
Context: $(echo "$mcp_info" | cut -d',' -f3 | cut -d':' -f2)
Output Length: $output_length characters
Execution Time: $execution_time
Has Errors: $has_errors
Performance Score: $performance_score/100
System Context: $context_info
Output Preview: $(echo "$tool_output" | head -c 200 | tr '\n' ' ')...
---
EOF
    
    log_message "INFO" "MCP operation logged: $tool_name (score: $performance_score/100)"
}

# Update MCP usage statistics
update_mcp_statistics() {
    local tool_name="$1"
    local performance_score="$2"
    local stats_file="/Users/nalve/ce-simple/.claude/logs/mcp-statistics.json"
    
    # Create stats file if it doesn't exist
    if [[ ! -f "$stats_file" ]]; then
        cat > "$stats_file" << 'EOF'
{
    "last_updated": "",
    "total_operations": 0,
    "tools": {},
    "performance": {
        "average_score": 0,
        "high_performance_count": 0,
        "low_performance_count": 0
    }
}
EOF
    fi
    
    # Update statistics using Python for JSON manipulation
    python3 -c "
import json
import sys
from datetime import datetime

stats_file = '$stats_file'
tool_name = '$tool_name'
performance_score = int('$performance_score')

try:
    with open(stats_file, 'r') as f:
        stats = json.load(f)
    
    # Update general stats
    stats['last_updated'] = datetime.now().isoformat()
    stats['total_operations'] += 1
    
    # Update tool-specific stats
    if tool_name not in stats['tools']:
        stats['tools'][tool_name] = {
            'count': 0,
            'total_score': 0,
            'average_score': 0,
            'last_used': ''
        }
    
    tool_stats = stats['tools'][tool_name]
    tool_stats['count'] += 1
    tool_stats['total_score'] += performance_score
    tool_stats['average_score'] = tool_stats['total_score'] / tool_stats['count']
    tool_stats['last_used'] = datetime.now().isoformat()
    
    # Update performance categories
    if performance_score >= 80:
        stats['performance']['high_performance_count'] += 1
    elif performance_score <= 40:
        stats['performance']['low_performance_count'] += 1
    
    # Calculate overall average
    total_score = sum(tool_data['total_score'] for tool_data in stats['tools'].values())
    total_ops = stats['total_operations']
    stats['performance']['average_score'] = total_score / total_ops if total_ops > 0 else 0
    
    # Write updated stats
    with open(stats_file, 'w') as f:
        json.dump(stats, f, indent=2)
        
except Exception as e:
    print(f'Error updating MCP statistics: {e}', file=sys.stderr)
" 2>/dev/null || log_message "WARN" "Failed to update MCP statistics"
}

# Generate alerts for performance issues
check_performance_alerts() {
    local tool_name="$1"
    local performance_score="$2"
    local has_errors="$3"
    
    # Alert for poor performance
    if [[ "$performance_score" -lt 30 ]]; then
        log_message "ALERT" "Poor MCP performance detected: $tool_name (score: $performance_score/100)"
        
        # Create alert file for monitoring system
        local alert_file="/Users/nalve/ce-simple/.claude/logs/alerts/mcp-performance-$(date +%Y%m%d-%H%M%S).alert"
        mkdir -p "$(dirname "$alert_file")"
        
        cat > "$alert_file" << EOF
Alert Type: MCP Performance
Tool: $tool_name
Score: $performance_score/100
Timestamp: $TIMESTAMP
Requires Investigation: Yes
EOF
    fi
    
    # Alert for errors
    if [[ "$has_errors" == "true" ]]; then
        log_message "ALERT" "MCP tool error detected: $tool_name"
    fi
}

# Main logging function
perform_mcp_logging() {
    log_message "INFO" "Starting MCP tool logging"
    
    # Extract tool information
    local tool_name="${CLAUDE_TOOL_NAME:-unknown}"
    local output_analysis
    output_analysis=$(analyze_tool_output "$TOOL_OUTPUT")
    
    # Parse analysis
    local output_length has_errors execution_time
    output_length=$(echo "$output_analysis" | cut -d',' -f1 | cut -d':' -f2)
    has_errors=$(echo "$output_analysis" | cut -d',' -f2 | cut -d':' -f2)
    execution_time=$(echo "$output_analysis" | cut -d',' -f3 | cut -d':' -f2)
    
    local performance_score
    performance_score=$(calculate_performance_score "$output_length" "$has_errors" "$execution_time")
    
    # Perform logging operations
    log_mcp_operation "$TOOL_OUTPUT"
    update_mcp_statistics "$tool_name" "$performance_score"
    check_performance_alerts "$tool_name" "$performance_score" "$has_errors"
    
    log_message "INFO" "MCP tool logging completed successfully"
}

# Error handling
handle_error() {
    local exit_code="$1"
    local error_message="$2"
    log_message "ERROR" "$error_message"
    
    # Post-tool hooks should not block operations
    case "$exit_code" in
        1)
            log_message "WARN" "MCP logging error (non-blocking): $error_message"
            ;;
        *)
            log_message "INFO" "MCP logging issue (continuing): $error_message"
            ;;
    esac
    
    # Always exit 0 for post-tool hooks
    exit 0
}

# Main execution
main() {
    # Create log directories
    mkdir -p "$(dirname "$LOG_FILE")"
    mkdir -p "$(dirname "$MCP_LOG_FILE")"
    
    # Validate input
    if [[ -z "$TOOL_OUTPUT" ]]; then
        handle_error 1 "No tool output provided for MCP logging"
    fi
    
    # Only proceed if this is an MCP tool
    if [[ "${CLAUDE_TOOL_NAME:-}" =~ ^mcp__ ]]; then
        perform_mcp_logging
    else
        log_message "INFO" "Non-MCP tool detected, skipping MCP-specific logging"
    fi
    
    # Success
    log_message "SUCCESS" "Post-MCP logging hook completed successfully"
    exit 0
}

# Trap signals for clean exit
trap 'log_message "WARN" "MCP logging interrupted"; exit 0' INT TERM

# Execute main function
main "$@"