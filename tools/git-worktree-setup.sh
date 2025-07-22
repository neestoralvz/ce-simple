#!/bin/bash
# Git WorkTree Parallel Setup Script for ce-simple
# Aggressive parallelization implementation

set -e

PROJECT="ce-simple"
BASE_DIR="/Users/nalve/ce-simple"

echo "🚀 Setting up parallel Git WorkTree environment for $PROJECT"

# Create trees directory if it doesn't exist
mkdir -p "$BASE_DIR/trees"

# Parallel WorkTree creation for different development streams
echo "📁 Creating parallel development environments..."

# Development stream 1: Command optimization
git worktree add -b optimize/explore-web "$BASE_DIR/trees/optimize-web" 2>/dev/null || echo "optimize-web worktree exists"

# Development stream 2: Parallel implementation
git worktree add -b implement/parallel-tools "$BASE_DIR/trees/parallel-tools" 2>/dev/null || echo "parallel-tools worktree exists"

# Development stream 3: Automation scripts  
git worktree add -b automate/workflows "$BASE_DIR/trees/automation" 2>/dev/null || echo "automation worktree exists"

# Development stream 4: Documentation updates
git worktree add -b docs/parallel-guide "$BASE_DIR/trees/documentation" 2>/dev/null || echo "documentation worktree exists"

# Create coordination files for AI agents
cat > "$BASE_DIR/trees/CLAUDE.md" << 'EOF'
# Parallel Development Coordination

## Active WorkTrees
- optimize-web: Optimizing explore-web command for 16 parallel searches
- parallel-tools: Implementing aggressive parallelization tools
- automation: Creating workflow automation scripts
- documentation: Updating documentation with parallel patterns

## AI Agent Coordination
Each worktree should focus on its specific domain without cross-contamination.
Use shared context in this file for coordination needs.
EOF

# Sync coordination file to all worktrees
for tree in optimize-web parallel-tools automation documentation; do
  if [ -d "$BASE_DIR/trees/$tree" ]; then
    cp "$BASE_DIR/trees/CLAUDE.md" "$BASE_DIR/trees/$tree/"
    echo "✅ Synced coordination to $tree"
  fi
done

# List all worktrees
echo "📋 Active WorkTrees:"
git worktree list

echo "🎯 Parallel development environment ready!"
echo "💡 Use: cd trees/[worktree-name] && claude-code"