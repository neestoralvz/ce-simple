#!/bin/bash

# HANDOFF 7: Backup Cascade Cleanup Script
# Automated cleanup of cascading backup files with safety checks

set -euo pipefail

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${GREEN}HANDOFF 7: BACKUP CASCADE CLEANUP${NC}"
echo "Automated cleanup of cascading backup files..."

# Safety parameters
WORKING_DIR="/Users/nalve/ce-simple/context"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
LOG_FILE="/Users/nalve/ce-simple/scripts/cleanup_log_${TIMESTAMP}.txt"
DRY_RUN=${1:-"false"}

# Create log file
echo "Backup Cascade Cleanup Log - $(date)" > "$LOG_FILE"
echo "Working Directory: $WORKING_DIR" >> "$LOG_FILE"
echo "Dry Run Mode: $DRY_RUN" >> "$LOG_FILE"
echo "----------------------------------------" >> "$LOG_FILE"

# Function to identify backup cascade files
identify_backup_cascades() {
    echo -e "${YELLOW}Identifying backup cascade files...${NC}"
    
    # Find files with multiple _BACKUP_ patterns (cascading backups)
    find "$WORKING_DIR" -name "*_BACKUP_*_BACKUP_*" -type f | sort > /tmp/backup_cascades.txt
    
    # Count files
    local cascade_count=$(wc -l < /tmp/backup_cascades.txt)
    
    echo -e "${BLUE}Found $cascade_count cascading backup files${NC}"
    echo "Found $cascade_count cascading backup files" >> "$LOG_FILE"
    
    return 0
}

# Function to categorize files by location
categorize_by_location() {
    echo -e "${YELLOW}Categorizing files by location...${NC}"
    
    # Archive files (safe to delete)
    grep "/archive/" /tmp/backup_cascades.txt > /tmp/archive_backups.txt || touch /tmp/archive_backups.txt
    
    # Emergency backup directories (safe to delete)
    grep "/emergency_backups_" /tmp/backup_cascades.txt > /tmp/emergency_backups.txt || touch /tmp/emergency_backups.txt
    
    # Active system files (require manual review)
    grep -v "/archive/" /tmp/backup_cascades.txt | grep -v "/emergency_backups_" > /tmp/active_backups.txt || touch /tmp/active_backups.txt
    
    local archive_count=$(wc -l < /tmp/archive_backups.txt)
    local emergency_count=$(wc -l < /tmp/emergency_backups.txt)
    local active_count=$(wc -l < /tmp/active_backups.txt)
    
    echo -e "${GREEN}Archive files: $archive_count${NC}"
    echo -e "${GREEN}Emergency backup dirs: $emergency_count${NC}"
    echo -e "${YELLOW}Active system files: $active_count${NC}"
    
    echo "Archive files: $archive_count" >> "$LOG_FILE"
    echo "Emergency backup dirs: $emergency_count" >> "$LOG_FILE"
    echo "Active system files: $active_count" >> "$LOG_FILE"
}

# Function to safely delete files
safe_delete() {
    local file_list="$1"
    local category="$2"
    
    if [[ ! -f "$file_list" ]] || [[ ! -s "$file_list" ]]; then
        echo -e "${YELLOW}No $category files to delete${NC}"
        return 0
    fi
    
    local count=$(wc -l < "$file_list")
    echo -e "${YELLOW}Processing $count $category files...${NC}"
    
    while IFS= read -r file; do
        if [[ -f "$file" ]]; then
            if [[ "$DRY_RUN" == "true" ]]; then
                echo -e "${BLUE}[DRY RUN] Would delete: $file${NC}"
                echo "[DRY RUN] Would delete: $file" >> "$LOG_FILE"
            else
                echo -e "${GREEN}Deleting: $file${NC}"
                echo "Deleting: $file" >> "$LOG_FILE"
                rm -f "$file"
            fi
        else
            echo -e "${RED}File not found: $file${NC}"
            echo "File not found: $file" >> "$LOG_FILE"
        fi
    done < "$file_list"
}

# Function to calculate space savings
calculate_savings() {
    echo -e "${YELLOW}Calculating space savings...${NC}"
    
    local total_size=0
    
    for list_file in /tmp/archive_backups.txt /tmp/emergency_backups.txt; do
        if [[ -f "$list_file" ]] && [[ -s "$list_file" ]]; then
            while IFS= read -r file; do
                if [[ -f "$file" ]]; then
                    local size=$(stat -f%z "$file" 2>/dev/null || echo 0)
                    total_size=$((total_size + size))
                fi
            done < "$list_file"
        fi
    done
    
    local size_mb=$((total_size / 1024 / 1024))
    echo -e "${GREEN}Estimated space savings: ${size_mb}MB${NC}"
    echo "Estimated space savings: ${size_mb}MB" >> "$LOG_FILE"
}

# Main execution
main() {
    echo -e "${BLUE}Starting backup cascade cleanup...${NC}"
    
    # Safety check
    if [[ ! -d "$WORKING_DIR" ]]; then
        echo -e "${RED}Error: Working directory $WORKING_DIR not found${NC}"
        exit 1
    fi
    
    # Step 1: Identify backup cascades
    identify_backup_cascades
    
    # Step 2: Categorize by location
    categorize_by_location
    
    # Step 3: Calculate potential savings
    calculate_savings
    
    # Step 4: Process archive files (safest)
    echo -e "${YELLOW}Processing archive backup cascades...${NC}"
    safe_delete "/tmp/archive_backups.txt" "archive"
    
    # Step 5: Process emergency backup directories
    echo -e "${YELLOW}Processing emergency backup cascades...${NC}"
    safe_delete "/tmp/emergency_backups.txt" "emergency backup"
    
    # Step 6: Report active system files (manual review required)
    if [[ -f "/tmp/active_backups.txt" ]] && [[ -s "/tmp/active_backups.txt" ]]; then
        local active_count=$(wc -l < /tmp/active_backups.txt)
        echo -e "${YELLOW}WARNING: $active_count active system backup cascades found - manual review required${NC}"
        echo "Active system files requiring manual review:" >> "$LOG_FILE"
        cat /tmp/active_backups.txt >> "$LOG_FILE"
    fi
    
    # Cleanup temp files
    rm -f /tmp/backup_cascades.txt /tmp/archive_backups.txt /tmp/emergency_backups.txt /tmp/active_backups.txt
    
    echo -e "${GREEN}Backup cascade cleanup completed!${NC}"
    echo -e "${BLUE}Log file: $LOG_FILE${NC}"
    
    return 0
}

# Execute main function
main "$@"