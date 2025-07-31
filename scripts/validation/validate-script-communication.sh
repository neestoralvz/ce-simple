#!/bin/bash
# validate-script-communication.sh - Validate scripts compliance with silent communication protocol
# 31/07/2025 CDMX | Communication protocol enforcement

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
SCRIPTS_DIR="$PROJECT_ROOT/scripts"
OUTPUT_FILE="$PROJECT_ROOT/scripts/communication_violations_$(date +%Y%m%d_%H%M%S).txt"

# Silent script - no user notifications (Claude Code communicates results)

# Find scripts with communication violations
find_communication_violations() {
    local violations=0
    
    # Pattern 1: echo statements with user messages
    while IFS= read -r line; do
        echo "$line" >> "$OUTPUT_FILE"
        ((violations++))
    done < <(grep -rn "echo.*[\"'].*[A-Za-z]" "$SCRIPTS_DIR" --include="*.sh" | grep -v "echo.*\$\|echo.*date\|echo.*technical\|echo.*log" || true)
    
    # Pattern 2: Colored output for users
    while IFS= read -r line; do
        echo "$line" >> "$OUTPUT_FILE"
        ((violations++))
    done < <(grep -rn "\\033\[.*m.*echo\|echo.*\\033\[.*m" "$SCRIPTS_DIR" --include="*.sh" || true)
    
    # Pattern 3: Progress indicators
    while IFS= read -r line; do
        echo "$line" >> "$OUTPUT_FILE"
        ((violations++))
    done < <(grep -rn "echo.*===\|echo.*---\|echo.*🔍\|echo.*📈\|echo.*✅" "$SCRIPTS_DIR" --include="*.sh" || true)
    
    echo "$violations"
}

# Main execution
violations_count=$(find_communication_violations)
echo "$violations_count|$OUTPUT_FILE|$(date)"