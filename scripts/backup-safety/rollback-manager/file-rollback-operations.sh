#!/bin/bash
# file-rollback-operations.sh - Single file rollback operations with integrity verification
# Part of rollback-manager.sh L2-MODULAR extraction
# Authority: @context/architecture/patterns/l2-modular-extraction-patterns.md

set -euo pipefail

# Rollback single file
rollback_single_file() {
    local original_file="$1"
    local backup_file="$2"
    local verify_hash="${3:-true}"
    
    echo -e "${CYAN}Rolling back: $(basename "$original_file")${NC}"
    
    if [[ ! -f "$backup_file" ]]; then
        echo -e "${RED}❌ Backup file not found: $backup_file${NC}"
        return 1
    fi
    
    # Verify backup integrity if requested
    if [[ "$verify_hash" == "true" ]]; then
        local backup_hash=$(sha256sum "$backup_file" | cut -d' ' -f1)
        echo "Backup hash: $backup_hash"
    fi
    
    # Create recovery backup of current state
    local recovery_backup="${original_file}.recovery_$(date +%Y%m%d_%H%M%S)"
    if [[ -f "$original_file" ]]; then
        cp "$original_file" "$recovery_backup"
        echo "Current state backed up to: $(basename "$recovery_backup")"
    fi
    
    # Perform rollback
    if cp "$backup_file" "$original_file"; then
        echo -e "${GREEN}✅ Rollback successful: $(basename "$original_file")${NC}"
        
        # Log rollback
        {
            echo "FILE_ROLLBACK: $(date)"
            echo "  Original: $original_file"
            echo "  Backup: $backup_file"
            echo "  Recovery backup: $recovery_backup"
            echo "  Status: SUCCESS"
            echo "  ---"
        } >> "$LOG_FILE"
        
        return 0
    else
        echo -e "${RED}❌ Rollback failed: $(basename "$original_file")${NC}"
        
        # Log failure
        {
            echo "FILE_ROLLBACK: $(date)"
            echo "  Original: $original_file"
            echo "  Backup: $backup_file"
            echo "  Status: FAILED"
            echo "  ---"
        } >> "$LOG_FILE"
        
        return 1
    fi
}