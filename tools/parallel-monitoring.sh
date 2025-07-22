#!/bin/bash
# Parallel Development Monitoring Script
# Real-time monitoring of multiple AI agents and worktrees

PROJECT_DIR="/Users/nalve/ce-simple"
TREES_DIR="$PROJECT_DIR/trees"

echo "🔍 Parallel Development Monitor Starting..."

# Function to check worktree status
check_worktree_status() {
    local tree_name=$1
    local tree_path="$TREES_DIR/$tree_name"
    
    if [ -d "$tree_path" ]; then
        cd "$tree_path"
        local branch=$(git branch --show-current)
        local status=$(git status --porcelain | wc -l)
        local last_commit=$(git log -1 --format="%cr" 2>/dev/null || echo "No commits")
        
        echo "📁 $tree_name:"
        echo "  Branch: $branch"
        echo "  Changes: $status files modified"  
        echo "  Last activity: $last_commit"
        echo ""
    fi
}

# Function to monitor system resources
monitor_resources() {
    echo "💻 System Resources:"
    
    # Memory usage
    local mem_usage=$(ps aux | awk '{sum+=$6} END {print sum/1024}')
    echo "  Memory: ${mem_usage%.*} MB"
    
    # CPU load
    local cpu_load=$(uptime | awk -F'load average:' '{print $2}' | awk '{print $1}')
    echo "  CPU Load: $cpu_load"
    
    # Disk usage of trees directory
    if [ -d "$TREES_DIR" ]; then
        local disk_usage=$(du -sh "$TREES_DIR" 2>/dev/null | awk '{print $1}')
        echo "  Trees Directory: $disk_usage"
    fi
    echo ""
}

# Function to check for running Claude processes
check_claude_processes() {
    echo "🤖 Active AI Processes:"
    
    local claude_processes=$(ps aux | grep -i claude | grep -v grep | wc -l)
    local node_processes=$(ps aux | grep -E "(node|npm)" | grep -v grep | wc -l)
    
    echo "  Claude-related: $claude_processes processes"
    echo "  Node/NPM: $node_processes processes"
    echo ""
}

# Function to display git worktree list
display_worktrees() {
    echo "🌳 Active WorkTrees:"
    cd "$PROJECT_DIR"
    git worktree list 2>/dev/null || echo "  No worktrees found"
    echo ""
}

# Main monitoring loop
main_monitor() {
    clear
    echo "================================="
    echo "🚀 PARALLEL DEVELOPMENT MONITOR"
    echo "================================="
    echo "Project: ce-simple"
    echo "Time: $(date)"
    echo "================================="
    echo ""
    
    # Check each known worktree
    for tree in optimize-web parallel-tools automation documentation; do
        check_worktree_status "$tree"
    done
    
    display_worktrees
    monitor_resources
    check_claude_processes
    
    echo "================================="
    echo "💡 Commands:"
    echo "  Ctrl+C to exit"
    echo "  ./parallel-monitoring.sh to refresh"
    echo "================================="
}

# Execute monitoring
main_monitor

# Optional: Continuous monitoring mode
if [ "$1" = "--watch" ]; then
    echo "👁️  Starting continuous monitoring (Ctrl+C to stop)..."
    while true; do
        sleep 10
        clear
        main_monitor
    done
fi