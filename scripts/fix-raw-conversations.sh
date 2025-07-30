#!/bin/bash
# fix-raw-conversations.sh - Workaround for Claude Code semantic organization non-compliance
# 
# PROBLEM: Claude Code ignores SEMANTIC_ORGANIZATION.md variables
# SOLUTION: This script restores semantic organization compliance
#
# Usage: ./scripts/fix-raw-conversations.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
# Source semantic organization configuration
# In a proper implementation, these would be read from SEMANTIC_ORGANIZATION.md
RAW_DIR="$PROJECT_ROOT/context/raw"
CONVERSATIONS_DIR="$PROJECT_ROOT/context/archive/conversations_processed"  # ${CONVERSATION_STORAGE}

echo "🔧 Semantic Organization Compliance Restoration"
echo "================================================="

# Check if raw directory exists
if [ ! -d "$RAW_DIR" ]; then
    echo "✅ No violations found - semantic organization is working"
    exit 0
fi

# Count files in raw directory
file_count=$(find "$RAW_DIR" -type f -name "*.md" | wc -l | tr -d ' ')

if [ "$file_count" -eq 0 ]; then
    echo "📁 Raw directory exists but is empty"
    rmdir "$RAW_DIR"
    echo "✅ Removed empty raw/ directory"
    exit 0
fi

echo "📋 Found $file_count conversation file(s) in raw/ directory"

# Ensure conversations directory exists
mkdir -p "$CONVERSATIONS_DIR"

# Move files
echo "🚚 Moving files from raw/ to conversations/..."
moved_files=0

for file in "$RAW_DIR"/*.md; do
    if [ -f "$file" ]; then
        filename=$(basename "$file")
        target="$CONVERSATIONS_DIR/$filename"
        
        # Check for conflicts
        if [ -f "$target" ]; then
            echo "⚠️  Conflict: $filename already exists in conversations/"
            timestamp=$(date +"%H%M%S")
            new_name="${filename%.md}_conflict_${timestamp}.md"
            target="$CONVERSATIONS_DIR/$new_name"
            echo "   Renaming to: $new_name"
        fi
        
        mv "$file" "$target"
        echo "   ✓ Moved: $filename"
        ((moved_files++))
    fi
done

# Remove raw directory
if rmdir "$RAW_DIR" 2>/dev/null; then
    echo "🗑️  Removed empty raw/ directory"
else
    echo "⚠️  Could not remove raw/ directory (may contain non-.md files)"
    ls -la "$RAW_DIR"
fi

echo ""
echo "✅ Cleanup completed successfully!"
echo "   📊 Files moved: $moved_files"
echo "   📂 Target: $CONVERSATIONS_DIR"

# Validation
final_count=$(find "$CONVERSATIONS_DIR" -type f -name "*.md" | wc -l | tr -d ' ')
echo "   📈 Total conversations now: $final_count"

if [ -d "$RAW_DIR" ]; then
    echo ""
    echo "⚠️  NOTE: raw/ directory still exists - manual cleanup may be needed"
else
    echo ""
    echo "🎉 System architecture is now consistent!"
fi