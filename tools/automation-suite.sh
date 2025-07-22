#!/bin/bash
# Automation Suite for Parallel AI Development
# Complete toolkit for managing parallel development workflows

set -e

PROJECT_DIR="/Users/nalve/ce-simple"
TREES_DIR="$PROJECT_DIR/trees"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Logging function
log() {
    echo -e "${GREEN}[$(date +'%H:%M:%S')]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function: Quick worktree creation
quick_tree() {
    local feature_name=$1
    local tree_name="feature-$feature_name"
    local tree_path="$TREES_DIR/$tree_name"
    
    if [ -z "$feature_name" ]; then
        error "Usage: quick_tree <feature-name>"
        return 1
    fi
    
    log "Creating worktree for feature: $feature_name"
    
    cd "$PROJECT_DIR"
    git worktree add -b "feature/$feature_name" "$tree_path" 2>/dev/null || {
        warn "Worktree might already exist"
    }
    
    # Sync coordination files
    if [ -f "$PROJECT_DIR/CLAUDE.md" ]; then
        cp "$PROJECT_DIR/CLAUDE.md" "$tree_path/" 2>/dev/null || true
    fi
    
    if [ -f "$PROJECT_DIR/.cursorrules" ]; then
        cp "$PROJECT_DIR/.cursorrules" "$tree_path/" 2>/dev/null || true
    fi
    
    log "✅ Worktree ready: $tree_path"
    log "💡 Use: cd $tree_path && claude-code"
}

# Function: Batch worktree creation
batch_trees() {
    local features=("$@")
    
    if [ ${#features[@]} -eq 0 ]; then
        features=("auth" "api" "ui" "docs" "testing" "optimization")
        log "Using default features: ${features[*]}"
    fi
    
    log "Creating ${#features[@]} worktrees in parallel..."
    
    for feature in "${features[@]}"; do
        quick_tree "$feature" &
    done
    
    wait
    log "✅ All worktrees created successfully"
}

# Function: Cleanup completed worktrees
cleanup_trees() {
    log "Cleaning up merged/completed worktrees..."
    
    cd "$PROJECT_DIR"
    
    # Get list of merged branches
    local merged_branches=$(git branch --merged main | grep -v main | grep -v '^\*' | xargs -n1 2>/dev/null || true)
    
    if [ -n "$merged_branches" ]; then
        echo "$merged_branches" | while read -r branch; do
            local tree_path="$TREES_DIR/$(basename "$branch")"
            if [ -d "$tree_path" ]; then
                log "Removing worktree: $tree_path"
                git worktree remove "$tree_path" --force 2>/dev/null || true
            fi
        done
    fi
    
    # Prune worktree metadata
    git worktree prune
    log "✅ Cleanup completed"
}

# Function: Sync files across worktrees
sync_files() {
    local files=("CLAUDE.md" ".cursorrules" ".env.example")
    
    log "Syncing coordination files across worktrees..."
    
    for tree_dir in "$TREES_DIR"/*; do
        if [ -d "$tree_dir" ]; then
            local tree_name=$(basename "$tree_dir")
            for file in "${files[@]}"; do
                if [ -f "$PROJECT_DIR/$file" ]; then
                    cp "$PROJECT_DIR/$file" "$tree_dir/" 2>/dev/null || true
                    log "Synced $file to $tree_name"
                fi
            done
        fi
    done
    
    log "✅ File sync completed"
}

# Function: Status overview
status_overview() {
    log "📊 Parallel Development Status Overview"
    echo ""
    
    # Worktree count
    local tree_count=$(ls -1d "$TREES_DIR"/* 2>/dev/null | wc -l || echo 0)
    echo "🌳 Active WorkTrees: $tree_count"
    
    # Git status
    cd "$PROJECT_DIR"
    git worktree list 2>/dev/null | while read -r line; do
        echo "  $line"
    done
    
    echo ""
    
    # Resource usage
    echo "💻 Resource Usage:"
    local disk_usage=$(du -sh "$TREES_DIR" 2>/dev/null | awk '{print $1}' || echo "0B")
    echo "  Trees Directory: $disk_usage"
    
    # Process count
    local processes=$(ps aux | grep -E "(claude|node)" | grep -v grep | wc -l || echo 0)
    echo "  AI/Node Processes: $processes"
}

# Function: Parallel command execution
parallel_exec() {
    local cmd="$1"
    shift
    local trees=("$@")
    
    if [ ${#trees[@]} -eq 0 ]; then
        trees=($(ls "$TREES_DIR" 2>/dev/null || true))
    fi
    
    log "Executing '$cmd' in ${#trees[@]} worktrees in parallel..."
    
    for tree in "${trees[@]}"; do
        local tree_path="$TREES_DIR/$tree"
        if [ -d "$tree_path" ]; then
            (
                cd "$tree_path"
                log "Executing in $tree: $cmd"
                eval "$cmd"
            ) &
        fi
    done
    
    wait
    log "✅ Parallel execution completed"
}

# Main command dispatcher
case "$1" in
    "quick")
        quick_tree "$2"
        ;;
    "batch")
        shift
        batch_trees "$@"
        ;;
    "cleanup")
        cleanup_trees
        ;;
    "sync")
        sync_files
        ;;
    "status")
        status_overview
        ;;
    "exec")
        shift
        parallel_exec "$@"
        ;;
    *)
        echo "🚀 Parallel Development Automation Suite"
        echo ""
        echo "Usage: $0 <command> [args...]"
        echo ""
        echo "Commands:"
        echo "  quick <name>     Create single worktree for feature"
        echo "  batch [names...] Create multiple worktrees (default: auth api ui docs testing optimization)"
        echo "  cleanup          Remove merged/completed worktrees"
        echo "  sync             Sync coordination files across worktrees"
        echo "  status           Show development status overview"
        echo "  exec <cmd>       Execute command in all worktrees in parallel"
        echo ""
        echo "Examples:"
        echo "  $0 quick user-auth"
        echo "  $0 batch auth api ui"
        echo "  $0 exec 'git status'"
        echo "  $0 status"
        ;;
esac