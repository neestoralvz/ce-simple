#!/bin/bash
# rollback-manager.sh - L2-MODULAR Hub: Enhanced automated rollback capabilities
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - L2-MODULAR extraction
# Authority: @context/architecture/patterns/l2-modular-extraction-patterns.md

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
OUTPUT_DIR="$PROJECT_ROOT/scripts/rollback_management_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/rollback_log.txt"
ROLLBACK_INDEX="$OUTPUT_DIR/rollback_index.json"

# Colors
RED='\033[0;31m'; GREEN='\033[0;32m'; BLUE='\033[0;34m'; CYAN='\033[0;36m'; NC='\033[0m'

echo -e "${GREEN}🔄 ROLLBACK MANAGER: L2-MODULAR Hub System${NC}"
mkdir -p "$OUTPUT_DIR"

# Initialize log
{
    echo "Rollback management started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: L2-MODULAR rollback system with specialized modules"
    echo "==============================================================================="
} > "$LOG_FILE"

# Rollback operation types
declare -A ROLLBACK_TYPES=(["file"]="Single file rollback" ["batch"]="Batch rollback" ["git"]="Git rollback")

# Load specialized modules
MODULE_DIR="$SCRIPT_DIR/rollback-manager"
source "$MODULE_DIR/backup-index-management.sh"
source "$MODULE_DIR/file-rollback-operations.sh"
source "$MODULE_DIR/batch-rollback-operations.sh"
source "$MODULE_DIR/git-rollback-operations.sh"
source "$MODULE_DIR/rollback-validation.sh"
source "$MODULE_DIR/rollback-reporting.sh"

# Main execution function
main() {
    [[ $# -eq 0 || "$1" == "--help" ]] && { show_usage; exit 0; }
    
    case "$1" in
        --index)
            [[ $# -lt 2 ]] && { echo -e "${RED}❌ Usage: $0 --index backup_dir [operation] [description]${NC}"; exit 1; }
            create_backup_index "$2" "${3:-unknown}" "${4:-Backup operation}" && echo -e "${GREEN}✅ Backup index created${NC}" || { echo -e "${RED}❌ Failed${NC}"; exit 1; }
            ;;
        --file)
            [[ $# -lt 3 ]] && { echo -e "${RED}❌ Usage: $0 --file original backup [verify_hash]${NC}"; exit 1; }
            rollback_single_file "$2" "$3" "${4:-true}" && echo -e "${GREEN}✅ File rollback completed${NC}" || { echo -e "${RED}❌ Failed${NC}"; exit 1; }
            ;;
        --batch)
            [[ $# -lt 2 ]] && { echo -e "${RED}❌ Usage: $0 --batch index_file [mode] [pattern]${NC}"; exit 1; }
            rollback_batch_operation "$2" "${3:-interactive}" "${4:-.*}"; echo -e "${GREEN}✅ Batch rollback completed${NC}"
            ;;
        --git)
            [[ $# -lt 3 ]] && { echo -e "${RED}❌ Usage: $0 --git type target [scope]${NC}"; exit 1; }
            git_rollback_operation "$2" "$3" "${4:-all}" && echo -e "${GREEN}✅ Git rollback completed${NC}" || { echo -e "${RED}❌ Failed${NC}"; exit 1; }
            ;;
        --validate)
            validate_rollback_integrity "${2:-basic}" "${3:-}"; echo -e "${GREEN}✅ Validation completed${NC}"
            ;;
        *) echo -e "${RED}❌ Unknown option: $1${NC}"; show_usage; exit 1 ;;
    esac
    
    # Generate report for all operations except help
    [[ "$1" != "--help" ]] && {
        generate_rollback_report
        echo -e "\n${GREEN}📁 Output: $OUTPUT_DIR${NC}"
        echo -e "${GREEN}📄 Log: $LOG_FILE${NC}"
        [[ -f "$ROLLBACK_INDEX" ]] && echo -e "${GREEN}📋 Index: $ROLLBACK_INDEX${NC}"
    }
}

# Execute main function
main "$@"