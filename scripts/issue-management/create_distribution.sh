#!/bin/bash

# Distribution Package Creator
# Creates a ready-to-distribute .tar.gz package of the command system

set -e

echo "📦 Creating Distribution Package..."

# Configuration
EXPORT_DIR="export"
PACKAGE_NAME="claude-command-system"
VERSION="1.0.0"
DIST_DIR="dist"

# Clean previous distributions
echo "🧹 Cleaning previous distributions..."
rm -rf "$DIST_DIR"
mkdir -p "$DIST_DIR"

# Validate export first
if [ -d "$EXPORT_DIR" ]; then
    cd "$EXPORT_DIR"
    python3 validate_export.py
    cd ..
else
    exit 1
fi

# Create package directory
PACKAGE_DIR="$DIST_DIR/$PACKAGE_NAME-$VERSION"
mkdir -p "$PACKAGE_DIR"

# Copy export contents
cp -r "$EXPORT_DIR"/* "$PACKAGE_DIR/"

# Create distribution info
cat > "$PACKAGE_DIR/DISTRIBUTION.md" << EOF
# Claude Command System Distribution

**Version**: $VERSION
**Created**: $(date)
**Source**: ce-simple project

## What's Included

- Complete command library (27+ commands)
- Universal CLAUDE.md dispatcher
- Installation script for easy setup
- Comprehensive documentation
- Context templates for customization

## Quick Installation

1. Extract this package to your project root
2. Run: \`./install.sh\`
3. Customize \`context/TRUTH_SOURCE.md\` with your project vision
4. Start using: \`/workflows:start\`

## System Requirements

- Claude Code CLI
- Git repository (recommended)
- Basic understanding of Claude conversations

## Support

See \`docs/\` for complete documentation including:
- Command reference
- Customization guide  
- Quick start guide
- Troubleshooting tips

---

**Note**: This is a portable extraction of the ce-simple command system.
All ce-simple specific references have been removed for universal compatibility.
EOF

# Create archive
echo "📦 Creating archive..."
cd "$DIST_DIR"
tar -czf "$PACKAGE_NAME-$VERSION.tar.gz" "$PACKAGE_NAME-$VERSION/"
cd ..

# Create checksums
echo "🔐 Creating checksums..."
cd "$DIST_DIR"
shasum -a 256 "$PACKAGE_NAME-$VERSION.tar.gz" > "$PACKAGE_NAME-$VERSION.sha256"
cd ..

# Validation summary
echo ""
echo "🔐 Checksum: $DIST_DIR/$PACKAGE_NAME-$VERSION.sha256"
echo ""

# Show package contents
tar -tzf "$DIST_DIR/$PACKAGE_NAME-$VERSION.tar.gz" | head -20
if [ $(tar -tzf "$DIST_DIR/$PACKAGE_NAME-$VERSION.tar.gz" | wc -l) -gt 20 ]; then
    echo "... and $(( $(tar -tzf "$DIST_DIR/$PACKAGE_NAME-$VERSION.tar.gz" | wc -l) - 20 )) more files"
fi

echo ""
echo "🚀 Ready for distribution!"
echo ""
echo "Usage for recipients:"
echo "1. Extract: tar -xzf $PACKAGE_NAME-$VERSION.tar.gz"
echo "2. Install: cd $PACKAGE_NAME-$VERSION && ./install.sh"
echo "3. Customize: Edit context/TRUTH_SOURCE.md"
echo "4. Use: /workflows:start"