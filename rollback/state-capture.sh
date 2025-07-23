#!/bin/bash

# State Capture System
# Comprehensive pre-migration state documentation
# Usage: ./state-capture.sh [snapshot-name]

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
STATE_DIR="$SCRIPT_DIR/state-snapshots"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
SNAPSHOT_NAME="${1:-complete-state-$TIMESTAMP}"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

log_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

log_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Create snapshot directory
SNAPSHOT_DIR="$STATE_DIR/$SNAPSHOT_NAME"
mkdir -p "$SNAPSHOT_DIR"

log_info "Creating comprehensive state snapshot: $SNAPSHOT_NAME"
cd "$PROJECT_ROOT"

# 1. File System Analysis
log_info "Analyzing file system structure..."

# Complete file inventory
find . -type f \( -name "*.md" -o -name "*.sh" -o -name "*.json" -o -name "*.txt" \) \
    ! -path "./.git/*" \
    ! -path "./rollback/state-snapshots/*" \
    ! -path "./rollback/logs/*" \
    | sort > "$SNAPSHOT_DIR/complete-file-inventory.txt"

# Directory structure with sizes
du -sh */ 2>/dev/null | sort -hr > "$SNAPSHOT_DIR/directory-sizes.txt" || true

# File count by type
echo "=== File Type Analysis ===" > "$SNAPSHOT_DIR/file-type-analysis.txt"
echo "Markdown files: $(find . -name "*.md" ! -path "./.git/*" | wc -l)" >> "$SNAPSHOT_DIR/file-type-analysis.txt"
echo "Shell scripts: $(find . -name "*.sh" ! -path "./.git/*" | wc -l)" >> "$SNAPSHOT_DIR/file-type-analysis.txt"
echo "JSON files: $(find . -name "*.json" ! -path "./.git/*" | wc -l)" >> "$SNAPSHOT_DIR/file-type-analysis.txt"
echo "Total tracked files: $(wc -l < "$SNAPSHOT_DIR/complete-file-inventory.txt")" >> "$SNAPSHOT_DIR/file-type-analysis.txt"

# 2. Content Checksums and Hashes
log_info "Computing file checksums and content hashes..."

# SHA256 checksums for all tracked files
while IFS= read -r file; do
    if [[ -f "$file" ]]; then
        sha256sum "$file" 2>/dev/null || echo "ERROR: $file"
    fi
done < "$SNAPSHOT_DIR/complete-file-inventory.txt" > "$SNAPSHOT_DIR/sha256-checksums.txt"

# MD5 checksums as backup
while IFS= read -r file; do
    if [[ -f "$file" ]]; then
        md5sum "$file" 2>/dev/null || echo "ERROR: $file"
    fi
done < "$SNAPSHOT_DIR/complete-file-inventory.txt" > "$SNAPSHOT_DIR/md5-checksums.txt"

# File sizes
while IFS= read -r file; do
    if [[ -f "$file" ]]; then
        echo "$(wc -c < "$file" 2>/dev/null || echo "0") $file"
    fi
done < "$SNAPSHOT_DIR/complete-file-inventory.txt" > "$SNAPSHOT_DIR/file-sizes.txt"

# 3. Git Repository State
log_info "Capturing git repository state..."

# Current status
git status --porcelain > "$SNAPSHOT_DIR/git-status.txt" 2>/dev/null || echo "No git status available" > "$SNAPSHOT_DIR/git-status.txt"

# Detailed git information
{
    echo "=== Git Repository State ==="
    echo "Current branch: $(git branch --show-current 2>/dev/null || echo 'detached')"
    echo "Current commit: $(git rev-parse HEAD 2>/dev/null || echo 'no commits')"
    echo "Remote URL: $(git remote get-url origin 2>/dev/null || echo 'no origin')"
    echo "Total commits: $(git rev-list --all --count 2>/dev/null || echo '0')"
    echo ""
    echo "=== Recent Commits ==="
    git log --oneline -10 2>/dev/null || echo "No commit history"
    echo ""
    echo "=== Branches ==="
    git branch -a 2>/dev/null || echo "No branches"
    echo ""
    echo "=== Remotes ==="
    git remote -v 2>/dev/null || echo "No remotes"
} > "$SNAPSHOT_DIR/git-detailed.txt"

# Git diff for staged changes
git diff --cached > "$SNAPSHOT_DIR/git-staged-diff.txt" 2>/dev/null || true

# Git diff for unstaged changes  
git diff > "$SNAPSHOT_DIR/git-unstaged-diff.txt" 2>/dev/null || true

# Stash list
git stash list > "$SNAPSHOT_DIR/git-stash-list.txt" 2>/dev/null || echo "No stashes" > "$SNAPSHOT_DIR/git-stash-list.txt"

# 4. Critical Files Analysis
log_info "Analyzing critical system files..."

# Critical files list
CRITICAL_FILES=(
    "CLAUDE.md"
    "README.md" 
    ".gitignore"
    ".session-info"
    "commands"
    "docs/core"
    "docs/standards"
    "rollback"
)

{
    echo "=== Critical Files Status ==="
    for file in "${CRITICAL_FILES[@]}"; do
        if [[ -e "$file" ]]; then
            if [[ -f "$file" ]]; then
                echo "FILE: $file ($(wc -l < "$file" 2>/dev/null || echo "0") lines)"
            elif [[ -d "$file" ]]; then
                echo "DIR:  $file ($(find "$file" -type f | wc -l) files)"
            fi
        else
            echo "MISSING: $file"
        fi
    done
} > "$SNAPSHOT_DIR/critical-files-status.txt"

# Create critical files backup
CRITICAL_BACKUP="$SNAPSHOT_DIR/critical-files-backup"
mkdir -p "$CRITICAL_BACKUP"

for file in "${CRITICAL_FILES[@]}"; do
    if [[ -e "$file" ]]; then
        if [[ -f "$file" ]]; then
            cp "$file" "$CRITICAL_BACKUP/"
        elif [[ -d "$file" ]]; then
            cp -r "$file" "$CRITICAL_BACKUP/"
        fi
    fi
done

# 5. Command System Analysis
log_info "Analyzing command system structure..."

if [[ -d "commands" ]]; then
    {
        echo "=== Command System Analysis ==="
        echo "Total commands: $(find commands -name "*.md" -type f | wc -l)"
        echo ""
        echo "=== Commands by Directory ==="
        find commands -type d | while read -r dir; do
            cmd_count=$(find "$dir" -maxdepth 1 -name "*.md" -type f | wc -l)
            if [[ $cmd_count -gt 0 ]]; then
                echo "$dir: $cmd_count commands"
            fi
        done
        echo ""
        echo "=== All Commands ==="
        find commands -name "*.md" -type f | sort
    } > "$SNAPSHOT_DIR/command-system-analysis.txt"
    
    # Command file sizes
    {
        echo "=== Command File Sizes ==="
        find commands -name "*.md" -type f | while read -r cmd; do
            lines=$(wc -l < "$cmd" 2>/dev/null || echo "0")
            echo "$lines lines: $cmd"
        done | sort -nr
    } > "$SNAPSHOT_DIR/command-file-sizes.txt"
else
    echo "Commands directory not found" > "$SNAPSHOT_DIR/command-system-analysis.txt"
fi

# 6. Documentation Analysis
log_info "Analyzing documentation structure..."

if [[ -d "docs" ]]; then
    {
        echo "=== Documentation Analysis ==="
        echo "Total docs: $(find docs -name "*.md" -type f | wc -l)"
        echo ""
        echo "=== Documentation Structure ==="
        tree docs 2>/dev/null || find docs -type d | sort
        echo ""
        echo "=== Documentation Files ==="
        find docs -name "*.md" -type f | sort
    } > "$SNAPSHOT_DIR/documentation-analysis.txt"
    
    # Doc file sizes
    {
        echo "=== Documentation File Sizes ==="
        find docs -name "*.md" -type f | while read -r doc; do
            lines=$(wc -l < "$doc" 2>/dev/null || echo "0")
            echo "$lines lines: $doc"
        done | sort -nr
    } > "$SNAPSHOT_DIR/documentation-file-sizes.txt"
else
    echo "Documentation directory not found" > "$SNAPSHOT_DIR/documentation-analysis.txt"
fi

# 7. System Environment
log_info "Capturing system environment..."

{
    echo "=== System Environment ==="
    echo "Date: $(date)"
    echo "User: $(whoami)"
    echo "PWD: $(pwd)"
    echo "OS: $(uname -a)"
    echo "Shell: $SHELL"
    echo ""
    echo "=== Disk Usage ==="
    du -sh . 2>/dev/null || echo "Cannot determine disk usage"
    echo ""
    echo "=== Git Version ==="
    git --version 2>/dev/null || echo "Git not available"
    echo ""
    echo "=== Environment Variables ==="
    env | grep -E "(GIT_|USER|HOME|PATH)" | sort
} > "$SNAPSHOT_DIR/system-environment.txt"

# 8. Archive Analysis (if exists)
if [[ -d ".archive" ]]; then
    log_info "Analyzing archive structure..."
    
    {
        echo "=== Archive Analysis ==="
        echo "Total archived files: $(find .archive -type f | wc -l)"
        echo "Archive size: $(du -sh .archive 2>/dev/null | cut -f1)"
        echo ""
        echo "=== Archive Structure ==="
        find .archive -type d | head -20
        echo ""
        echo "=== Recent Archive Files ==="
        find .archive -type f -name "*.md" | head -10
    } > "$SNAPSHOT_DIR/archive-analysis.txt"
else
    echo "No archive directory found" > "$SNAPSHOT_DIR/archive-analysis.txt"
fi

# 9. Create metadata file
log_info "Creating snapshot metadata..."

{
    echo "{"
    echo "  \"snapshot_name\": \"$SNAPSHOT_NAME\","
    echo "  \"timestamp\": \"$(date -Iseconds)\","
    echo "  \"created_by\": \"$(whoami)\","
    echo "  \"project_root\": \"$PROJECT_ROOT\","
    echo "  \"git_commit\": \"$(git rev-parse HEAD 2>/dev/null || echo 'no-git')\","
    echo "  \"git_branch\": \"$(git branch --show-current 2>/dev/null || echo 'no-branch')\","
    echo "  \"total_files\": $(wc -l < "$SNAPSHOT_DIR/complete-file-inventory.txt"),"
    echo "  \"total_commands\": $(find commands -name "*.md" -type f 2>/dev/null | wc -l),"
    echo "  \"total_docs\": $(find docs -name "*.md" -type f 2>/dev/null | wc -l),"
    echo "  \"disk_usage\": \"$(du -sh . 2>/dev/null | cut -f1)\","
    echo "  \"snapshot_size\": \"$(du -sh "$SNAPSHOT_DIR" 2>/dev/null | cut -f1)\","
    echo "  \"capture_script_version\": \"1.0.0\""
    echo "}"
} > "$SNAPSHOT_DIR/metadata.json"

# 10. Create integrity verification file
log_info "Creating integrity verification..."

{
    echo "=== Snapshot Integrity Verification ==="
    echo "Created: $(date)"
    echo "Files captured: $(wc -l < "$SNAPSHOT_DIR/complete-file-inventory.txt")"
    echo "Checksums computed: $(wc -l < "$SNAPSHOT_DIR/sha256-checksums.txt")"
    echo ""
    echo "=== Verification Checksums ==="
    echo "File inventory: $(sha256sum "$SNAPSHOT_DIR/complete-file-inventory.txt" | cut -d' ' -f1)"
    echo "SHA256 checksums: $(sha256sum "$SNAPSHOT_DIR/sha256-checksums.txt" | cut -d' ' -f1)"
    echo "Critical files backup: $(find "$CRITICAL_BACKUP" -type f | wc -l) files backed up"
    echo ""
    echo "=== Status ==="
    echo "Snapshot complete and verified"
} > "$SNAPSHOT_DIR/integrity-verification.txt"

# 11. Create snapshot summary
{
    echo "# State Snapshot Summary: $SNAPSHOT_NAME"
    echo ""
    echo "**Created**: $(date)"
    echo "**Location**: $SNAPSHOT_DIR"
    echo ""
    echo "## Captured Data"
    echo "- **Total Files**: $(wc -l < "$SNAPSHOT_DIR/complete-file-inventory.txt")"
    echo "- **Commands**: $(find commands -name "*.md" -type f 2>/dev/null | wc -l)"
    echo "- **Documentation**: $(find docs -name "*.md" -type f 2>/dev/null | wc -l)"
    echo "- **Git Commit**: $(git rev-parse --short HEAD 2>/dev/null || echo 'no-git')"
    echo "- **Git Branch**: $(git branch --show-current 2>/dev/null || echo 'no-branch')"
    echo ""
    echo "## Files Created"
    ls -la "$SNAPSHOT_DIR" | grep -v "^total" | tail -n +2 | while read -r line; do
        echo "- $(echo "$line" | awk '{print $9}')"
    done
    echo ""
    echo "## Restoration Command"
    echo '```bash'
    echo "./rollback-manager.sh rollback $SNAPSHOT_NAME complete"
    echo '```'
} > "$SNAPSHOT_DIR/snapshot-summary.md"

log_success "State snapshot created successfully: $SNAPSHOT_NAME"
log_info "Snapshot location: $SNAPSHOT_DIR"
log_info "Files captured: $(wc -l < "$SNAPSHOT_DIR/complete-file-inventory.txt")"
log_info "Snapshot size: $(du -sh "$SNAPSHOT_DIR" 2>/dev/null | cut -f1)"

echo ""
echo "Use './rollback-manager.sh rollback $SNAPSHOT_NAME' to restore this state"