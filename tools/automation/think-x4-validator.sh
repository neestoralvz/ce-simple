#!/bin/bash
# think-x4-validator.sh - Think x4 Analysis Validation Tool
# Part of Git Workflow Analysis Implementation
# Created: 2025-07-31

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"
LOG_FILE="${PROJECT_ROOT}/tools/automation/think-x4-validation.log"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
    echo -e "$1"
}

# Think x4 validation patterns
THINK_X4_PATTERNS=(
    "Think 1:"
    "Think 2:"
    "Think 3:" 
    "Think 4:"
    "THINK 1:"
    "THINK 2:"
    "THINK 3:"
    "THINK 4:"
)

# Validate Think x4 in file
validate_think_x4_in_file() {
    local file="$1"
    local found_patterns=0
    
    for pattern in "${THINK_X4_PATTERNS[@]}"; do
        if grep -q "$pattern" "$file"; then
            ((found_patterns++))
        fi
    done
    
    if [ $found_patterns -ge 4 ]; then
        return 0  # Valid Think x4
    else
        return 1  # Invalid Think x4
    fi
}

# Main validation function
validate_think_x4() {
    local target_file="$1"
    
    if [ ! -f "$target_file" ]; then
        log "${RED}ERROR: File not found: $target_file${NC}"
        return 1
    fi
    
    log "${BLUE}Validating Think x4 analysis in: $target_file${NC}"
    
    if validate_think_x4_in_file "$target_file"; then
        log "${GREEN}✓ Valid Think x4 analysis found${NC}"
        return 0
    else
        log "${YELLOW}⚠ Think x4 analysis incomplete or missing${NC}"
        log "${YELLOW}Expected patterns: Think 1-4 or THINK 1-4${NC}"
        return 1
    fi
}

# Interactive Think x4 prompt
prompt_think_x4_analysis() {
    local topic="$1"
    
    log "${BLUE}Think x4 Analysis Required for: $topic${NC}"
    echo
    echo "Please provide analysis from 4 perspectives:"
    echo "Think 1: [Primary perspective]"
    echo "Think 2: [Alternative perspective]" 
    echo "Think 3: [Risk/challenge perspective]"
    echo "Think 4: [Integration/synthesis perspective]"
    echo
}

# Usage function
usage() {
    echo "Usage: $0 [OPTIONS] [FILE]"
    echo
    echo "Options:"
    echo "  -v, --validate FILE    Validate Think x4 analysis in file"
    echo "  -p, --prompt TOPIC     Interactive Think x4 prompt for topic"
    echo "  -h, --help            Show this help message"
    echo
    echo "Examples:"
    echo "  $0 -v analysis.md"
    echo "  $0 -p 'Git workflow integration'"
}

# Main execution
main() {
    # Initialize log
    mkdir -p "$(dirname "$LOG_FILE")"
    
    case "${1:-}" in
        -v|--validate)
            if [ -z "${2:-}" ]; then
                echo "Error: File path required for validation"
                usage
                exit 1
            fi
            validate_think_x4 "$2"
            ;;
        -p|--prompt)
            if [ -z "${2:-}" ]; then
                echo "Error: Topic required for prompt"
                usage
                exit 1
            fi
            prompt_think_x4_analysis "$2"
            ;;
        -h|--help)
            usage
            ;;
        "")
            echo "Error: No arguments provided"
            usage
            exit 1
            ;;
        *)
            # Default to validation if file exists
            if [ -f "$1" ]; then
                validate_think_x4 "$1"
            else
                echo "Error: Unknown option or file not found: $1"
                usage
                exit 1
            fi
            ;;
    esac
}

# Execute main function with all arguments
main "$@"