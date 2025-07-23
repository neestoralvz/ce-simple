#!/bin/bash

# Script to update broken links in functional README files

# Define the functional directory
FUNCTIONAL_DIR="/Users/nalve/claude-context-engineering/docs/commands/functional"

echo "🔧 Updating README links in functional directories..."

# Function to update Spanish directory references to English
update_spanish_references() {
    local file="$1"
    echo "  📝 Updating Spanish references in $(basename "$file")..."
    
    # Update Spanish directory names to English
    sed -i '' 's|\.\.\/colaboracion\/|../collaboration/|g' "$file"
    sed -i '' 's|\.\.\/documentacion\/|../documentation/|g' "$file"
    sed -i '' 's|\.\.\/ejecucion\/|../execution/|g' "$file"
    sed -i '' 's|\.\.\/exploracion\/|../exploration/|g' "$file"
    sed -i '' 's|\.\.\/inteligencia\/|../intelligence/|g' "$file"
    sed -i '' 's|\.\.\/navegacion\/|../navigation/|g' "$file"
    sed -i '' 's|\.\.\/optimizacion\/|../optimization/|g' "$file"
    sed -i '' 's|\.\.\/verificacion\/|../verification/|g' "$file"
    sed -i '' 's|\.\.\/desarrollo-personal\/|../personal-development/|g' "$file"
    sed -i '' 's|\.\.\/herramientas-especializadas\/|../specialized-tools/|g' "$file"
    
    # Update Spanish link text
    sed -i '' 's|\*\*\[Colaboración\]|\*\*\[Collaboration\]|g' "$file"
    sed -i '' 's|\*\*\[Documentación\]|\*\*\[Documentation\]|g' "$file"
    sed -i '' 's|\*\*\[Ejecución\]|\*\*\[Execution\]|g' "$file"
    sed -i '' 's|\*\*\[Exploración\]|\*\*\[Exploration\]|g' "$file"
    sed -i '' 's|\*\*\[Inteligencia\]|\*\*\[Intelligence\]|g' "$file"
    sed -i '' 's|\*\*\[Navegación\]|\*\*\[Navigation\]|g' "$file"
    sed -i '' 's|\*\*\[Optimización\]|\*\*\[Optimization\]|g' "$file"
    sed -i '' 's|\*\*\[Verificación\]|\*\*\[Verification\]|g' "$file"
    sed -i '' 's|\*\*\[Decisión\]|\*\*\[Decision\]|g' "$file"
}

# Function to update command links to correct knowledge paths
update_command_links() {
    local file="$1"
    echo "  🔗 Updating command links in $(basename "$file")..."
    
    # Update behavioral command links
    sed -i '' 's|\.\.\/\.\.\/behavioral\/|../../../knowledge/commands/|g' "$file"
    
    # Update executable command links  
    sed -i '' 's|\.\.\/\.\.\/executable\/|../../../knowledge/commands/|g' "$file"
    
    # Update core command links
    sed -i '' 's|\.\.\/\.\.\/core\/|../../../knowledge/commands/|g' "$file"
    
    # Update shared command links to correct relative path
    sed -i '' 's|\.\.\/\.\.\/shared\/|../shared/|g' "$file"
}

# Function to fix navigation links
update_navigation_links() {
    local file="$1"
    echo "  🧭 Updating navigation links in $(basename "$file")..."
    
    # Fix Technical View links (should point to parent commands directory)
    sed -i '' 's|\[Technical View\](\.\.\/README\.md)|\[Technical View\](../../README.md)|g' "$file"
    
    # Fix Cross-Reference Mapping links
    sed -i '' 's|\[Cross-Reference Mapping\](\.\.\/CROSS_REFERENCE_MAPPING\.md)|\[Cross-Reference Mapping\](../cross-reference-mapping.md)|g' "$file"
}

# Process all README files in functional subdirectories
find "$FUNCTIONAL_DIR" -name "README.md" -not -path "$FUNCTIONAL_DIR/README.md" | while read -r readme_file; do
    echo "🔄 Processing: $readme_file"
    
    # Create backup
    cp "$readme_file" "$readme_file.backup"
    
    # Apply updates
    update_spanish_references "$readme_file"
    update_command_links "$readme_file"
    update_navigation_links "$readme_file"
    
    echo "  ✅ Updated: $(basename "$readme_file")"
done

echo "🎯 README link updates completed!"
echo "📁 Backup files created with .backup extension"
echo "🔍 Please verify the changes and remove backup files if satisfied"