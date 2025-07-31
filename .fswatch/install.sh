#!/bin/bash

# CE-Simple Protection System Installer
# Sets up continuous file system monitoring and enforcement

set -euo pipefail

PROJECT_ROOT="/Users/nalve/ce-simple"
FSWATCH_DIR="$PROJECT_ROOT/.fswatch"
PLIST_NAME="com.ce-simple.protection"
LAUNCHD_DIR="$HOME/Library/LaunchAgents"

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

# Check if fswatch is installed
check_dependencies() {
    log "Checking dependencies..."
    
    if ! command -v fswatch &> /dev/null; then
        error "fswatch is not installed. Installing via Homebrew..."
        if command -v brew &> /dev/null; then
            brew install fswatch
            success "fswatch installed successfully"
        else
            error "Homebrew not found. Please install fswatch manually: brew install fswatch"
            exit 1
        fi
    else
        success "fswatch is already installed"
    fi
}

# Create log directory
setup_logging() {
    log "Setting up logging..."
    mkdir -p "$FSWATCH_DIR/logs"
    touch "$FSWATCH_DIR/logs/protection.log"
    touch "$FSWATCH_DIR/logs/violations.log"
    touch "$FSWATCH_DIR/logs/daemon-output.log"
    touch "$FSWATCH_DIR/logs/daemon-error.log"
    success "Logging directories created"
}

# Install launchd service
install_service() {
    log "Installing launchd service..."
    
    # Create LaunchAgents directory if it doesn't exist
    mkdir -p "$LAUNCHD_DIR"
    
    # Copy plist file
    cp "$FSWATCH_DIR/$PLIST_NAME.plist" "$LAUNCHD_DIR/"
    success "Service plist copied to $LAUNCHD_DIR"
    
    # Load the service
    launchctl load "$LAUNCHD_DIR/$PLIST_NAME.plist" 2>/dev/null || {
        warning "Service might already be loaded, attempting to unload and reload..."
        launchctl unload "$LAUNCHD_DIR/$PLIST_NAME.plist" 2>/dev/null || true
        sleep 1
        launchctl load "$LAUNCHD_DIR/$PLIST_NAME.plist"
    }
    
    success "Guardian Protection Service loaded and running"
}

# Verify installation
verify_installation() {
    log "Verifying installation..."
    
    # Check if service is loaded
    if launchctl list | grep -q "$PLIST_NAME"; then
        success "Service is loaded and running"
    else
        error "Service failed to load"
        return 1
    fi
    
    # Test file creation detection (create and remove a test file)
    local test_file="$PROJECT_ROOT/test-guardian-detection.tmp"
    echo "test" > "$test_file"
    sleep 2
    rm -f "$test_file"
    
    # Check if logs were created
    if [[ -s "$FSWATCH_DIR/logs/protection.log" ]]; then
        success "Guardian is actively monitoring file changes"
    else
        warning "Guardian logs are empty - service might need more time to start"
    fi
}

# Show status and usage
show_status() {
    echo
    log "🛡️ CE-Simple Guardian Protection System Status"
    echo "============================================="
    
    if launchctl list | grep -q "$PLIST_NAME"; then
        success "Status: ACTIVE and monitoring"
    else
        error "Status: INACTIVE"
    fi
    
    echo
    echo "📁 Monitoring: $PROJECT_ROOT"
    echo "📋 Log files:"
    echo "   • Protection: $FSWATCH_DIR/logs/protection.log"
    echo "   • Violations: $FSWATCH_DIR/logs/violations.log"
    echo "   • System: $FSWATCH_DIR/logs/daemon-output.log"
    echo
    echo "🔧 Management commands:"
    echo "   • View logs: tail -f $FSWATCH_DIR/logs/protection.log"
    echo "   • Stop service: launchctl unload $LAUNCHD_DIR/$PLIST_NAME.plist"
    echo "   • Start service: launchctl load $LAUNCHD_DIR/$PLIST_NAME.plist"
    echo "   • Check status: launchctl list | grep $PLIST_NAME"
    echo
}

main() {
    log "🛡️ Installing CE-Simple Guardian Protection System..."
    echo
    
    check_dependencies
    setup_logging
    install_service
    
    sleep 3  # Give service time to start
    
    verify_installation
    show_status
    
    echo
    success "🎉 Guardian Protection System installed successfully!"
    success "Your project is now protected by continuous monitoring"
    echo
}

main "$@"