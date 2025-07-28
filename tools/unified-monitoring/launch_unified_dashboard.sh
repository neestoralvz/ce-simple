#!/bin/bash

# launch_unified_dashboard.sh
# Launcher script for the Unified Visual Dashboard
# Integrates both monitoring systems: Health daemon + Orchestration hooks

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Configuration
DASHBOARD_PORT=8766
HTML_FILE="$SCRIPT_DIR/unified_dashboard.html"
PYTHON_SCRIPT="$SCRIPT_DIR/unified_dashboard.py"
HEALTH_DAEMON_STATUS="$PROJECT_ROOT/data/monitoring/health_daemon_status.json"
ORCHESTRATION_DB="$PROJECT_ROOT/data/orchestration/conversations.db"

print_header() {
    echo -e "${CYAN}╔══════════════════════════════════════════════════════════════╗${NC}"
    echo -e "${CYAN}║                                                              ║${NC}"
    echo -e "${CYAN}║  🎯 UNIFIED VISUAL DASHBOARD - DUAL MONITORING INTEGRATION  ║${NC}"
    echo -e "${CYAN}║                                                              ║${NC}"
    echo -e "${CYAN}║  Combines: Health Daemon + Orchestration + Hooks + Git      ║${NC}"
    echo -e "${CYAN}║                                                              ║${NC}"
    echo -e "${CYAN}╚══════════════════════════════════════════════════════════════╝${NC}"
    echo ""
}

check_prerequisites() {
    echo -e "${BLUE}🔍 Checking prerequisites...${NC}"
    
    # Check Python availability
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}❌ Python3 not found. Please install Python 3.7+${NC}"
        exit 1
    fi
    
    # Check required Python packages
    python3 -c "import asyncio, websockets, json, sqlite3" 2>/dev/null || {
        echo -e "${YELLOW}⚠️  Installing required Python packages...${NC}"
        pip3 install websockets asyncio-compat 2>/dev/null || {
            echo -e "${RED}❌ Failed to install required packages. Please run: pip3 install websockets${NC}"
            exit 1
        }
    }
    
    # Check if unified dashboard files exist
    if [[ ! -f "$PYTHON_SCRIPT" ]]; then
        echo -e "${RED}❌ Unified dashboard Python script not found: $PYTHON_SCRIPT${NC}"
        exit 1
    fi
    
    if [[ ! -f "$HTML_FILE" ]]; then
        echo -e "${RED}❌ Unified dashboard HTML file not found: $HTML_FILE${NC}"
        exit 1
    fi
    
    echo -e "${GREEN}✅ Prerequisites check passed${NC}"
    echo ""
}

check_monitoring_systems() {
    echo -e "${BLUE}🏥 Checking monitoring systems status...${NC}"
    
    # Check Health Daemon
    if [[ -f "$HEALTH_DAEMON_STATUS" ]]; then
        local health_pid=$(jq -r '.pid // empty' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "")
        if [[ -n "$health_pid" ]] && ps -p "$health_pid" > /dev/null 2>&1; then
            local health_score=$(jq -r '.health_score // 0' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "0")
            local cycle_count=$(jq -r '.cycle_count // 0' "$HEALTH_DAEMON_STATUS" 2>/dev/null || echo "0")
            echo -e "${GREEN}✅ Health Daemon Active - PID: $health_pid, Score: $health_score, Cycle: $cycle_count${NC}"
        else
            echo -e "${YELLOW}⚠️  Health Daemon not running or PID invalid${NC}"
        fi
    else
        echo -e "${YELLOW}⚠️  Health Daemon status file not found${NC}"
    fi
    
    # Check Orchestration Database
    if [[ -f "$ORCHESTRATION_DB" ]]; then
        local active_conversations=$(sqlite3 "$ORCHESTRATION_DB" "SELECT COUNT(*) FROM conversation_registry WHERE status = 'active';" 2>/dev/null || echo "0")
        local pending_tasks=$(sqlite3 "$ORCHESTRATION_DB" "SELECT COUNT(*) FROM conversation_tasks WHERE status = 'pending';" 2>/dev/null || echo "0")
        echo -e "${GREEN}✅ Orchestration System Active - $active_conversations conversations, $pending_tasks pending tasks${NC}"
    else
        echo -e "${YELLOW}⚠️  Orchestration database not found${NC}"
    fi
    
    # Check Hooks System
    local hooks_dir="$PROJECT_ROOT/.claude/hooks"
    if [[ -d "$hooks_dir" ]]; then
        local hooks_count=$(find "$hooks_dir" -name "*.sh" | wc -l)
        echo -e "${GREEN}✅ Hooks System Available - $hooks_count hook scripts${NC}"
    else
        echo -e "${YELLOW}⚠️  Hooks system directory not found${NC}"
    fi
    
    echo ""
}

start_dashboard_server() {
    echo -e "${PURPLE}🚀 Starting Unified Dashboard Server on port $DASHBOARD_PORT...${NC}"
    echo ""
    
    # Check if port is already in use
    if lsof -Pi :$DASHBOARD_PORT -sTCP:LISTEN -t >/dev/null 2>&1; then
        echo -e "${YELLOW}⚠️  Port $DASHBOARD_PORT is already in use. Attempting to kill existing process...${NC}"
        local existing_pid=$(lsof -ti:$DASHBOARD_PORT)
        if [[ -n "$existing_pid" ]]; then
            kill -9 "$existing_pid" 2>/dev/null || true
            sleep 2
        fi
    fi
    
    # Create logs directory
    mkdir -p "$PROJECT_ROOT/.claude/logs"
    
    # Start the Python WebSocket server
    echo -e "${BLUE}📡 Launching WebSocket server...${NC}"
    cd "$SCRIPT_DIR"
    python3 "$PYTHON_SCRIPT" serve &
    local server_pid=$!
    
    # Wait a moment for server to start
    sleep 3
    
    # Check if server started successfully
    if ps -p $server_pid > /dev/null 2>&1; then
        echo -e "${GREEN}✅ Dashboard server started successfully (PID: $server_pid)${NC}"
        
        # Store PID for cleanup
        echo $server_pid > "$PROJECT_ROOT/.claude/logs/unified-dashboard.pid"
        
        # Open dashboard in browser
        local dashboard_url="file://$HTML_FILE"
        echo -e "${CYAN}🌐 Opening unified dashboard in browser...${NC}"
        echo -e "${CYAN}📊 Dashboard URL: $dashboard_url${NC}"
        echo -e "${CYAN}🔌 WebSocket Server: ws://localhost:$DASHBOARD_PORT${NC}"
        echo ""
        
        # Try to open in default browser
        if command -v open &> /dev/null; then
            open "$dashboard_url"
        elif command -v xdg-open &> /dev/null; then
            xdg-open "$dashboard_url"
        else
            echo -e "${YELLOW}⚠️  Please manually open: $dashboard_url${NC}"
        fi
        
        echo -e "${GREEN}🎯 UNIFIED DASHBOARD IS NOW RUNNING!${NC}"
        echo ""
        echo -e "${CYAN}Real-time monitoring active for:${NC}"
        echo -e "${CYAN}  • Health Daemon (PID tracking)${NC}"
        echo -e "${CYAN}  • Orchestration System (conversation coordination)${NC}"
        echo -e "${CYAN}  • Hooks System (progress reporting)${NC}"
        echo -e "${CYAN}  • Git Correlation (evidence tracking)${NC}"
        echo ""
        echo -e "${YELLOW}Press Ctrl+C to stop the dashboard server${NC}"
        
        # Wait for server or handle Ctrl+C
        trap "cleanup_and_exit $server_pid" INT TERM
        wait $server_pid
        
    else
        echo -e "${RED}❌ Failed to start dashboard server${NC}"
        exit 1
    fi
}

cleanup_and_exit() {
    local server_pid=$1
    echo ""
    echo -e "${YELLOW}🛑 Stopping Unified Dashboard...${NC}"
    
    # Kill server process
    if [[ -n "$server_pid" ]] && ps -p $server_pid > /dev/null 2>&1; then
        kill -TERM $server_pid 2>/dev/null || kill -9 $server_pid 2>/dev/null
    fi
    
    # Clean up PID file
    rm -f "$PROJECT_ROOT/.claude/logs/unified-dashboard.pid"
    
    echo -e "${GREEN}✅ Dashboard stopped cleanly${NC}"
    exit 0
}

show_usage() {
    echo "Usage: $0 [command]"
    echo ""
    echo "Commands:"
    echo "  start     - Start the unified dashboard (default)"
    echo "  status    - Show current system status"
    echo "  stop      - Stop running dashboard"
    echo "  check     - Check prerequisites and monitoring systems"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 start"
    echo "  $0 status"
    echo "  $0 check"
}

stop_dashboard() {
    echo -e "${YELLOW}🛑 Stopping Unified Dashboard...${NC}"
    
    local pid_file="$PROJECT_ROOT/.claude/logs/unified-dashboard.pid"
    if [[ -f "$pid_file" ]]; then
        local pid=$(cat "$pid_file")
        if [[ -n "$pid" ]] && ps -p $pid > /dev/null 2>&1; then
            kill -TERM $pid 2>/dev/null || kill -9 $pid 2>/dev/null
            echo -e "${GREEN}✅ Dashboard stopped (PID: $pid)${NC}"
        else
            echo -e "${YELLOW}⚠️  Dashboard process not found${NC}"
        fi
        rm -f "$pid_file"
    else
        echo -e "${YELLOW}⚠️  No running dashboard found${NC}"
    fi
}

show_status() {
    echo -e "${BLUE}📊 Getting unified system status...${NC}"
    python3 "$PYTHON_SCRIPT" status 2>/dev/null || {
        echo -e "${RED}❌ Failed to get status. Dashboard server may not be running.${NC}"
        exit 1
    }
}

# Main script execution
main() {
    local command="${1:-start}"
    
    case "$command" in
        "start")
            print_header
            check_prerequisites
            check_monitoring_systems
            start_dashboard_server
            ;;
        "stop")
            stop_dashboard
            ;;
        "status")
            show_status
            ;;
        "check")
            print_header
            check_prerequisites
            check_monitoring_systems
            ;;
        "help"|"-h"|"--help")
            show_usage
            ;;
        *)
            echo -e "${RED}❌ Unknown command: $command${NC}"
            echo ""
            show_usage
            exit 1
            ;;
    esac
}

# Execute main function
main "$@"