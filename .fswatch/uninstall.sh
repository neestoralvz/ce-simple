#!/bin/bash

# CE-Simple Protection System Uninstaller
# Removes continuous file system monitoring

set -euo pipefail

PLIST_NAME="com.ce-simple.protection"
LAUNCHD_DIR="$HOME/Library/LaunchAgents"
PROJECT_ROOT="/Users/nalve/ce-simple"
FSWATCH_DIR="$PROJECT_ROOT/.fswatch"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log() {
    echo -e "${BLUE}[$(date '+%H:%M:%S')]${NC} $1"
}

success() {
    echo -e "${GREEN}✅${NC} $1"
}

warning() {
    echo -e "${YELLOW}⚠️${NC} $1"
}

error() {
    echo -e "${RED}❌${NC} $1"
}

# Stop and unload service
stop_service() {
    log "Stopping Guardian Protection Service..."
    
    if launchctl list | grep -q "$PLIST_NAME"; then
        launchctl unload "$LAUNCHD_DIR/$PLIST_NAME.plist" 2>/dev/null || {
            warning "Service might already be stopped"
        }
        success "Service stopped"
    else
        warning "Service was not running"
    fi
}

# Remove service files
remove_service() {
    log "Removing service files..."
    
    if [[ -f "$LAUNCHD_DIR/$PLIST_NAME.plist" ]]; then
        rm "$LAUNCHD_DIR/$PLIST_NAME.plist"
        success "Service plist removed from LaunchAgents"
    else
        warning "Service plist not found in LaunchAgents"
    fi
}

# Archive logs before removal
archive_logs() {
    log "Archiving logs..."
    
    if [[ -d "$FSWATCH_DIR/logs" ]] && [[ "$(ls -A "$FSWATCH_DIR/logs")" ]]; then
        local archive_dir="$PROJECT_ROOT/context/archive/guardian-logs-$(date '+%Y%m%d_%H%M%S')"
        mkdir -p "$archive_dir"
        cp -r "$FSWATCH_DIR/logs/"* "$archive_dir/" 2>/dev/null || true
        success "Logs archived to: $archive_dir"
    else
        warning "No logs to archive"
    fi
}

# Verify removal
verify_removal() {
    log "Verifying removal..."
    
    if ! launchctl list | grep -q "$PLIST_NAME"; then
        success "Service successfully removed from launchd"
    else
        error "Service still appears to be loaded"
        return 1
    fi
    
    if [[ ! -f "$LAUNCHD_DIR/$PLIST_NAME.plist" ]]; then
        success "Service files successfully removed"
    else
        error "Service files still present"
        return 1
    fi
}

# Show removal options
show_options() {
    echo
    log "🗑️ Guardian Protection System Removal Options"
    echo "============================================="
    echo
    echo "This will:"
    echo "• Stop the Guardian protection service"
    echo "• Remove the launchd service configuration"
    echo "• Archive existing logs to context/archive/"
    echo "• Keep the .fswatch/ directory and scripts for future use"
    echo
    echo "The system can be reinstalled later by running: .fswatch/install.sh"
    echo
    read -p "Continue with removal? (y/N): " -n 1 -r
    echo
    
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        log "Removal cancelled"
        exit 0
    fi
}

main() {
    log "🗑️ Uninstalling CE-Simple Guardian Protection System..."
    echo
    
    show_options
    
    archive_logs
    stop_service
    remove_service
    
    sleep 2  # Give system time to clean up
    
    verify_removal
    
    echo
    success "🎉 Guardian Protection System successfully removed"
    success "Scripts remain in .fswatch/ directory for future use"
    echo
    log "To reinstall: run .fswatch/install.sh"
    echo
}

main "$@"