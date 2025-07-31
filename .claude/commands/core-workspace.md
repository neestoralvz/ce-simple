# /core-workspace - Workspace Setup & Environment Preparation

**FUNCIÓN**: Standalone workspace creation + embedded automation layer integration

## EMBEDDED WORKSPACE CREATION PROTOCOL

**WORKSPACE SETUP AUTOCONTENIDO**:
```bash
# Embedded workspace creation logic (zero external dependencies)
create_conversation_workspace() {
    local timestamp="${1:-$(date +%Y%m%d_%H%M%S)}"
    local workspace_base_dir="./.conversation-workspaces"
    local workspace_name="conv-$timestamp"
    local workspace_path="$workspace_base_dir/$workspace_name"
    
    echo "🌳 Creating conversation workspace: $workspace_name"
    
    # Ensure base directory exists
    if [[ ! -d "$workspace_base_dir" ]]; then
        mkdir -p "$workspace_base_dir"
        echo "✅ Created workspace base directory: $workspace_base_dir"
    fi
    
    # Check if workspace already exists
    if [[ -d "$workspace_path" ]]; then
        echo "⚠️ Workspace already exists: $workspace_path"
        echo "$workspace_path"
        return 0
    fi
    
    # Try git worktree creation first
    if git worktree add "$workspace_path" HEAD 2>/dev/null; then
        echo "✅ Git worktree created: $workspace_path"
    else
        echo "⚠️ Git worktree creation failed, using fallback directory"
        mkdir -p "$workspace_path"
        echo "FALLBACK_WORKSPACE=true" > "$workspace_path/.workspace-info"
        echo "CREATED=$(date -Iseconds)" >> "$workspace_path/.workspace-info"
        echo "ORIGINAL_DIR=$(pwd)" >> "$workspace_path/.workspace-info"
    fi
    
    # Set up workspace environment
    cat > "$workspace_path/.env" << EOF
CONVERSATION_WORKSPACE=true
WORKSPACE_NAME=$workspace_name
WORKSPACE_PATH=$workspace_path
WORKSPACE_CREATED=$(date -Iseconds)
ORIGINAL_BRANCH=$(git branch --show-current 2>/dev/null || echo "unknown")
EOF
    
    echo "✅ Conversation workspace ready: $workspace_path"
    echo "$workspace_path"
}

# Embedded parallel coordination logic
setup_parallel_coordination() {
    local max_parallel=3
    echo "🔧 Setting up parallel coordination (max: $max_parallel)"
    
    # Simple process management without external scripts
    export MAX_PARALLEL_TOOLS=$max_parallel
    export COORDINATION_ACTIVE=true
    echo "✅ Coordination variables set"
}

# Main workspace setup execution
setup_workspace() {
    local workspace_path
    workspace_path=$(create_conversation_workspace)
    
    if [[ -n "$workspace_path" ]] && [[ -d "$workspace_path" ]]; then
        # Activate workspace environment
        if [[ -f "$workspace_path/.env" ]]; then
            source "$workspace_path/.env"
            export CONVERSATION_WORKSPACE WORKSPACE_NAME WORKSPACE_PATH WORKSPACE_CREATED
        fi
        
        # Change to workspace directory
        cd "$workspace_path" || {
            echo "❌ Failed to change to workspace directory"
            return 1
        }
        
        setup_parallel_coordination
        echo "🎯 Workspace activated: $(pwd)"
        return 0
    else
        echo "❌ Workspace setup failed"
        return 1
    fi
}

# Execute workspace setup
setup_workspace
```

**EMBEDDED CLEANUP FUNCTIONS**:
```bash
# Embedded workspace cleanup (standalone)
cleanup_workspace() {
    local workspace_path="$1"
    local force="${2:-false}"
    
    if [[ ! -d "$workspace_path" ]]; then
        echo "Workspace does not exist: $workspace_path"
        return 0
    fi
    
    echo "🧹 Cleaning up workspace: $workspace_path"
    
    # Check if it's a git worktree
    if git worktree list 2>/dev/null | grep -q "$workspace_path"; then
        # Check for uncommitted changes unless force cleanup
        if [[ "$force" != "true" ]]; then
            if ! git -C "$workspace_path" diff --quiet 2>/dev/null || ! git -C "$workspace_path" diff --cached --quiet 2>/dev/null; then
                echo "⚠️ Workspace has uncommitted changes, use 'force' to cleanup anyway"
                return 1
            fi
        fi
        
        # Remove git worktree
        if git worktree remove "$workspace_path" --force 2>/dev/null; then
            echo "✅ Git worktree removed: $workspace_path"
        else
            echo "⚠️ Failed to remove git worktree, removing directory manually"
            rm -rf "$workspace_path"
        fi
    else
        # Regular directory cleanup
        rm -rf "$workspace_path"
        echo "✅ Directory removed: $workspace_path"
    fi
    
    return 0
}
```

**INTEGRATION**: Completely self-contained workspace management with embedded git worktree creation and parallel coordination setup