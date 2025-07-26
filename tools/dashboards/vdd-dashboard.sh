#!/bin/bash

# VDD Metrics Dashboard - Token Economy Tracking
# Simple wrapper script for easier usage

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_ROOT="$( cd "$SCRIPT_DIR/.." && pwd )"
DASHBOARD_SCRIPT="$SCRIPT_DIR/vdd-metrics-dashboard.py"
CONFIG_FILE="$SCRIPT_DIR/../config/vdd-config.json"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_header() {
    echo -e "${BLUE}"
    echo "🎯 VDD METRICS DASHBOARD - TOKEN ECONOMY TRACKING"
    echo "=================================================="
    echo -e "${NC}"
}

print_usage() {
    echo "Usage: $0 [COMMAND] [OPTIONS]"
    echo ""
    echo "Commands:"
    echo "  run                    Generate single metrics report (default)"
    echo "  watch                  Continuous monitoring mode"
    echo "  json                   Output in JSON format"
    echo "  quick                  Quick summary (top issues only)"
    echo "  file <path>            Analyze specific file"
    echo "  help                   Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0                     # Basic metrics report"
    echo "  $0 watch               # Continuous monitoring"
    echo "  $0 json > metrics.json # Export to JSON"
    echo "  $0 quick               # Quick overview"
    echo "  $0 file docs/core/project-structure-current.md"
    echo ""
}

check_dependencies() {
    if ! command -v python3 &> /dev/null; then
        echo -e "${RED}Error: python3 is required but not installed.${NC}"
        exit 1
    fi
    
    if [ ! -f "$DASHBOARD_SCRIPT" ]; then
        echo -e "${RED}Error: Dashboard script not found at $DASHBOARD_SCRIPT${NC}"
        exit 1
    fi
}

run_dashboard() {
    local args=("$@")
    
    echo -e "${GREEN}🔍 Running VDD metrics analysis...${NC}"
    echo "Project: $(pwd)"
    echo "Config: $CONFIG_FILE"
    echo ""
    
    python3 "$DASHBOARD_SCRIPT" "${args[@]}"
}

case "${1:-run}" in
    "run"|"")
        print_header
        check_dependencies
        run_dashboard
        ;;
    
    "watch")
        print_header
        check_dependencies
        echo -e "${YELLOW}Starting continuous monitoring (Ctrl+C to stop)...${NC}"
        run_dashboard --watch
        ;;
    
    "json")
        check_dependencies
        run_dashboard --json
        ;;
    
    "quick")
        print_header
        check_dependencies
        echo -e "${GREEN}🚀 Quick VDD overview:${NC}"
        # Run and filter for just the summary sections
        python3 "$DASHBOARD_SCRIPT" | grep -A 20 "AGGREGATE METRICS SUMMARY\|TOP OPTIMIZATION OPPORTUNITIES"
        ;;
    
    "file")
        if [ -z "$2" ]; then
            echo -e "${RED}Error: Please specify a file path${NC}"
            echo "Usage: $0 file <path>"
            exit 1
        fi
        print_header
        check_dependencies
        run_dashboard --file "$2"
        ;;
    
    "help"|"-h"|"--help")
        print_header
        print_usage
        ;;
    
    *)
        echo -e "${RED}Error: Unknown command '$1'${NC}"
        echo ""
        print_usage
        exit 1
        ;;
esac