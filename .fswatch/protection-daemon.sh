#!/bin/bash

# CE-Simple Protection Daemon
# Continuous file system monitoring for project structure enforcement

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
LOG_FILE="$PROJECT_ROOT/.fswatch/logs/protection.log"
VALIDATORS_DIR="$PROJECT_ROOT/.fswatch/validators"
PID_FILE="$PROJECT_ROOT/.fswatch/protection-daemon.pid"

# Logging function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Signal handlers
cleanup() {
    log "🛡️ Protection daemon shutting down..."
    rm -f "$PID_FILE"
    exit 0
}

trap cleanup SIGTERM SIGINT

# Create PID file
echo $$ > "$PID_FILE"

log "🛡️ Guardian Protection Daemon starting..."
log "📁 Monitoring: $PROJECT_ROOT"
log "📝 Logging to: $LOG_FILE"

# Main monitoring loop
fswatch \
    --recursive \
    --event Created \
    --event Updated \
    --event Renamed \
    --exclude="\.git/.*" \
    --exclude="\.fswatch/.*" \
    --exclude="node_modules/.*" \
    --exclude=".*\.tmp" \
    --exclude=".*\.swp" \
    --exclude=".*\.DS_Store" \
    "$PROJECT_ROOT" | while read -r changed_file; do
    
    log "📋 File change detected: $changed_file"
    
    # Root protection check
    if [[ "$changed_file" == "$PROJECT_ROOT"/*.* && ! "$changed_file" =~ /CLAUDE\.md$|/README\.md$ ]]; then
        log "⚠️  ROOT VIOLATION: Unauthorized file in root - $changed_file"
        
        # Run root structure validator
        if [[ -x "$VALIDATORS_DIR/root-structure-validator.sh" ]]; then
            "$VALIDATORS_DIR/root-structure-validator.sh" "$changed_file" 2>&1 | tee -a "$LOG_FILE"
        fi
    fi
    
    # File size validation for .md files
    if [[ "$changed_file" =~ \.md$ && -f "$changed_file" ]]; then
        line_count=$(wc -l < "$changed_file" 2>/dev/null || echo "0")
        if [[ $line_count -gt 80 ]]; then
            log "⚠️  SIZE VIOLATION: File exceeds 80 lines ($line_count) - $changed_file"
            
            # Run file size validator
            if [[ -x "$VALIDATORS_DIR/file-size-validator.sh" ]]; then
                "$VALIDATORS_DIR/file-size-validator.sh" "$changed_file" "$line_count" 2>&1 | tee -a "$LOG_FILE"
            fi
        fi
    fi
    
    # Standards compliance check
    if [[ -x "$VALIDATORS_DIR/standards-validator.sh" ]]; then
        "$VALIDATORS_DIR/standards-validator.sh" "$changed_file" 2>&1 | tee -a "$LOG_FILE"
    fi
    
done

# This should never be reached, but cleanup if it is
cleanup