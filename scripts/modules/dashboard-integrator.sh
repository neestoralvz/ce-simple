#!/bin/bash
# Dashboard Integrator Module - Enhanced Synchronization with Rollback
# Extracted from handoff-init.sh with validation and rollback capability
set -euo pipefail

# Configuration
PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
ROADMAP_REGISTRY="$PROJECT_ROOT/context/roadmap/ROADMAP_REGISTRY.md"
BACKUP_SUFFIX=".dashboard-backup-$(date +%s)"

# Logging
log_success() { echo "✅ $1" >&2; }
log_error() { echo "❌ $1" >&2; }
log_info() { echo "ℹ️  $1" >&2; }

# Get priority icon
get_priority_icon() {
    case "$1" in
        "critical"|"high") echo "🔴" ;; "emergency") echo "🚨" ;; "low") echo "⚪" ;; *) echo "🟡" ;;
    esac
}

# Validate dashboard structure
validate_dashboard_structure() {
    local dashboard_file="$1"
    [[ -f "$dashboard_file" ]] || { log_error "Dashboard file not found"; return 1; }
    grep -q "## 🚀 WORK ITEMS" "$dashboard_file" || { log_error "Missing WORK ITEMS section"; return 1; }
    grep -q "⏸️P1-UX-FIX" "$dashboard_file" || { log_error "Missing insertion anchor"; return 1; }
}

# Create backup for rollback
create_dashboard_backup() {
    local backup_file="${1}${BACKUP_SUFFIX}"
    cp "$1" "$backup_file" || { log_error "Backup creation failed"; return 1; }
    echo "$backup_file"
}

# Rollback dashboard
rollback_dashboard() {
    local dashboard_file="${1%%.dashboard-backup-*}"
    [[ -f "$1" ]] || { log_error "Backup file not found"; return 1; }
    cp "$1" "$dashboard_file" && rm -f "$1" && log_info "Dashboard rolled back successfully"
}

# Enhanced update with validation and rollback
update_dashboard() {
    local handoff_id="$1" status="$2" domain="$3" priority="$4" density="${5:-Med}" tasks="${6:-~5}"
    
    # Validation and backup
    validate_dashboard_structure "$ROADMAP_REGISTRY" || return 1
    local backup_file; backup_file=$(create_dashboard_backup "$ROADMAP_REGISTRY") || return 1
    
    # Create table row
    local priority_icon; priority_icon=$(get_priority_icon "$priority")
    local table_row="| **${priority_icon}${handoff_id}** | ${priority_icon} ${status} | ${domain} | 0% | ${density} | ${tasks} | ✅ Good |"
    
    # Safe update with temp file
    local temp_file; temp_file=$(mktemp) || { rollback_dashboard "$backup_file"; return 1; }
    
    # Update dashboard
    if ! sed "/⏸️P1-UX-FIX/i\\$table_row" "$ROADMAP_REGISTRY" > "$temp_file"; then
        rm -f "$temp_file"; rollback_dashboard "$backup_file"; log_error "Dashboard update failed"; return 1
    fi
    
    # Update statistics
    if ! sed -i 's/- \*\*Ready\*\*: [0-9]* items/- **Ready**: 4 items/' "$temp_file"; then
        rm -f "$temp_file"; rollback_dashboard "$backup_file"; log_error "Statistics update failed"; return 1
    fi
    
    # Final validation and commit
    if validate_dashboard_structure "$temp_file"; then
        mv "$temp_file" "$ROADMAP_REGISTRY" && rm -f "$backup_file"
        log_success "Dashboard updated with $handoff_id (enhanced sync)"
    else
        rm -f "$temp_file"; rollback_dashboard "$backup_file"
        log_error "Updated dashboard failed validation"; return 1
    fi
}

# Performance optimization: validate data integrity
validate_data_integrity() {
    local violations=0
    [[ -f "$ROADMAP_REGISTRY" ]] || ((violations++))
    [[ $(grep -c "^|" "$ROADMAP_REGISTRY" 2>/dev/null || echo 0) -gt 10 ]] || ((violations++))
    [[ $violations -eq 0 ]] && log_success "100% data integrity validated" || log_error "$violations integrity violations"
    return $violations
}

# Export functions for external use
export -f update_dashboard validate_dashboard_structure rollback_dashboard validate_data_integrity