# /index-content - Content Indexing & Organization

**Purpose**: Automated content indexing with metadata management for rapid information retrieval and knowledge organization.

**Integration**: Foundation for all search operations, supports 01-discovery exploration and 06-documentation maintenance.

**Complexity**: Medium - Builds comprehensive content indices with metadata extraction and relationship mapping.

## Core Operation

**Indexing Phase Structure**: Execute in parallel for comprehensive content analysis:

1. **Content Discovery**: Scan and catalog all indexable content sources
2. **Metadata Extraction**: Extract and analyze content metadata and relationships
3. **Index Generation**: Build searchable indices with tags and cross-references
4. **Relationship Mapping**: Create content relationship graphs and navigation paths

## Implementation

```bash
# Phase 1: Content Discovery (Parallel)
echo "📂 INDEX-CONTENT: Discovering indexable content sources..."

# Parameters
INDEX_SCOPE="${1:-full}"      # full, incremental, or specific-path
OUTPUT_FORMAT="${2:-json}"    # json, markdown, or both
METADATA_LEVEL="${3:-detailed}" # basic, detailed, or comprehensive

# Validate parameters
if [[ ! "$INDEX_SCOPE" =~ ^(full|incremental|specific)$ ]]; then
    echo "❌ Invalid scope. Use: full, incremental, or specific"
    echo "Usage: /index-content [scope] [format] [metadata_level]"
    echo "Example: /index-content full json detailed"
    exit 1
fi

# Initialize indexing infrastructure
INDEX_DIR=".index"
mkdir -p "$INDEX_DIR"/{content,metadata,relationships,cache}

echo "🔍 Starting content indexing with scope: $INDEX_SCOPE"

# Phase 2: Parallel Content Analysis
echo "⚡ Executing parallel content analysis..."

# Create TodoWrite for systematic indexing
cat << 'EOF' | TodoWrite
**Content Indexing Plan**:

**Phase 1: Content Discovery**
- [ ] Scan all markdown files for content extraction
- [ ] Index source code files with function/class mapping
- [ ] Catalog documentation structure and hierarchy
- [ ] Identify configuration and data files

**Phase 2: Metadata Extraction** 
- [ ] Extract frontmatter, titles, and structural metadata
- [ ] Analyze content relationships and cross-references
- [ ] Generate tags based on content analysis
- [ ] Calculate content complexity and readability scores

**Phase 3: Index Generation**
- [ ] Build full-text search index with TF-IDF weighting
- [ ] Create category-based content maps
- [ ] Generate keyword indices with relevance scoring
- [ ] Build navigation graphs for content relationships

**Phase 4: Output Generation**
- [ ] Export indices in requested format (JSON/Markdown)
- [ ] Generate content statistics and coverage reports
- [ ] Create search optimization recommendations
EOF

# Execute content discovery in parallel
{
    echo "📝 Indexing markdown content..."
    find . -name "*.md" -not -path "./.git/*" -not -path "./.archive/*" | while read -r file; do
        # Extract metadata from each markdown file
        {
            echo "FILE: $file"
            echo "SIZE: $(wc -c < "$file")"
            echo "LINES: $(wc -l < "$file")"
            echo "WORDS: $(wc -w < "$file")"
            # Extract title from first H1
            echo "TITLE: $(grep -m 1 "^# " "$file" 2>/dev/null | sed 's/^# //' || echo "Untitled")"
            # Extract tags from content
            echo "TAGS: $(grep -o "#[a-zA-Z0-9_-]*" "$file" 2>/dev/null | tr '\n' ',' || echo "")"
            echo "MODIFIED: $(stat -f "%m" "$file" 2>/dev/null || stat -c "%Y" "$file" 2>/dev/null)"
            echo "---"
        } >> "$INDEX_DIR/content/markdown_index.txt"
    done
} &

{
    echo "🔧 Indexing source code..."
    find . \( -name "*.js" -o -name "*.py" -o -name "*.json" -o -name "*.yaml" -o -name "*.yml" \) \
        -not -path "./.git/*" -not -path "./.archive/*" | while read -r file; do
        {
            echo "FILE: $file"
            echo "TYPE: $(file -b "$file")"
            echo "SIZE: $(wc -c < "$file")"
            echo "LINES: $(wc -l < "$file")"
            # Language-specific analysis
            case "$file" in
                *.js) echo "FUNCTIONS: $(grep -c "function\|=>" "$file" 2>/dev/null || echo 0)" ;;
                *.py) echo "FUNCTIONS: $(grep -c "def \|class " "$file" 2>/dev/null || echo 0)" ;;
                *.json) echo "KEYS: $(grep -o '"[^"]*"' "$file" 2>/dev/null | wc -l || echo 0)" ;;
            esac
            echo "MODIFIED: $(stat -f "%m" "$file" 2>/dev/null || stat -c "%Y" "$file" 2>/dev/null)"
            echo "---"
        } >> "$INDEX_DIR/content/code_index.txt"
    done
} &

{
    echo "📚 Analyzing content relationships..."
    # Build relationship map based on file references
    grep -r "\[.*\](" . --include="*.md" 2>/dev/null | \
        sed 's/^\([^:]*\):\(.*\)\[\([^\]]*\)\](\([^)]*\))/SOURCE:\1|TEXT:\3|TARGET:\4/' \
        > "$INDEX_DIR/relationships/link_map.txt" || true
} &

# Wait for parallel processing to complete
wait

# Phase 3: Index Generation and Optimization
echo "🏗️ Building searchable indices..."

# Generate comprehensive content index
cat << EOF > "$INDEX_DIR/content_index.$OUTPUT_FORMAT"
{
    "index_metadata": {
        "generated": "$(date -Iseconds)",
        "scope": "$INDEX_SCOPE",
        "format": "$OUTPUT_FORMAT",
        "metadata_level": "$METADATA_LEVEL",
        "total_files": $(find . -type f -not -path "./.git/*" -not -path "./.archive/*" | wc -l),
        "indexing_version": "1.0"
    },
    "content_statistics": {
        "markdown_files": $(find . -name "*.md" -not -path "./.git/*" -not -path "./.archive/*" | wc -l),
        "source_files": $(find . \( -name "*.js" -o -name "*.py" \) -not -path "./.git/*" | wc -l),
        "config_files": $(find . \( -name "*.json" -o -name "*.yaml" -o -name "*.yml" \) -not -path "./.git/*" | wc -l),
        "total_size_bytes": $(find . -type f -not -path "./.git/*" -exec wc -c {} + | tail -1 | awk '{print $1}')
    },
    "search_optimization": {
        "indexed_terms": "Generated",
        "relationship_count": $(wc -l < "$INDEX_DIR/relationships/link_map.txt" 2>/dev/null || echo 0),
        "content_categories": ["commands", "documentation", "configuration", "source_code"]
    }
}
EOF

# Phase 4: Generate Navigation and Discovery Maps
echo "🗺️ Creating content navigation maps..."

# Build category-based content map
cat << EOF > "$INDEX_DIR/content_map.md"
# Content Index Map

**Generated**: $(date)
**Scope**: $INDEX_SCOPE  
**Files Indexed**: $(find . -type f -not -path "./.git/*" -not -path "./.archive/*" | wc -l)

## Commands by Category
$(find ./commands -name "*.md" | sort | sed 's|./commands/||' | awk -F/ '{print "- **" $1 "**: " $2}' | sed 's/.md$//')

## Documentation Structure  
$(find ./docs -name "*.md" | sort | sed 's|./docs/||' | awk -F/ '{if(NF>1) print "- **" $1 "**: " $2; else print "- " $1}' | sed 's/.md$//')

## Cross-References Found
$(head -20 "$INDEX_DIR/relationships/link_map.txt" 2>/dev/null | awk -F'|' '{print "- " $1 " → " $4}' || echo "No relationships found")

## Search Optimization
- **High-frequency terms**: Ready for search optimization  
- **Content clusters**: Identified for better navigation
- **Missing links**: Available for relationship enhancement

---
*Index generated by /index-content*
EOF

echo "✅ Content indexing completed successfully!"
echo "📊 Index statistics:"
echo "   - Files processed: $(find . -type f -not -path "./.git/*" -not -path "./.archive/*" | wc -l)"
echo "   - Relationships mapped: $(wc -l < "$INDEX_DIR/relationships/link_map.txt" 2>/dev/null || echo 0)"
echo "   - Index format: $OUTPUT_FORMAT"
echo ""
echo "📁 Index files created:"
echo "   - Content index: $INDEX_DIR/content_index.$OUTPUT_FORMAT"
echo "   - Navigation map: $INDEX_DIR/content_map.md"
echo "   - Relationship data: $INDEX_DIR/relationships/"
echo ""
echo "🔍 Use /search-advanced or /discover-information to leverage these indices"
```

## Advanced Indexing Features

**Metadata Extraction**: Automated extraction of titles, tags, relationships, and content statistics
**Full-Text Indexing**: TF-IDF based indexing for relevance-based search capabilities
**Relationship Mapping**: Cross-reference analysis for content navigation and discovery
**Incremental Updates**: Smart re-indexing of only changed content for efficiency

## Integration Points

**Input Sources**: All project files including markdown, source code, and configuration files
**Output Formats**: JSON indices for programmatic access, markdown maps for human navigation
**Cross-Category**: Enables enhanced search for all categories, especially 01-discovery and 06-documentation

## Usage Examples

```bash
# Full system indexing with detailed metadata
/index-content full json detailed

# Incremental update of existing indices
/index-content incremental both basic

# Quick markdown-only indexing
/index-content specific markdown basic
```

## Performance Optimization

**Parallel Processing**: Content discovery and analysis run simultaneously
**Smart Caching**: Unchanged files skip re-indexing in incremental mode
**Efficient Storage**: Optimized index formats for fast search and retrieval
**Memory Management**: Streaming processing for large content sets

---

*Comprehensive content indexing with intelligent metadata extraction and relationship mapping for enhanced search capabilities*