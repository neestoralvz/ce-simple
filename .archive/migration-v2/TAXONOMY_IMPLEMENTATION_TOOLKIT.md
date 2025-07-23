# Taxonomy Implementation Toolkit

**Purpose**: Practical tools and scripts for implementing the organizational taxonomy matrix.

## Implementation Scripts

### 1. Taxonomy Validation Script

```bash
#!/bin/bash
# validate-taxonomy.sh - Comprehensive taxonomy compliance checker

echo "=== CE-SIMPLE TAXONOMY VALIDATION ==="
echo "Timestamp: $(date)"
echo

# File type distribution analysis
echo "📊 FILE TYPE DISTRIBUTION:"
echo "Commands (.md in /commands/): $(find commands/ -name "*.md" 2>/dev/null | wc -l)"
echo "Scripts (.sh, .py, .js): $(find . -name "*.sh" -o -name "*.py" -o -name "*.js" | grep -v .archive | wc -l)"
echo "Configs (.json, .yaml): $(find . -name "*.json" -o -name "*.yaml" -o -name "*.yml" | grep -v .archive | wc -l)"
echo "Documentation (.md in /docs/): $(find docs/ -name "*.md" 2>/dev/null | wc -l)"
echo "Templates: $(find templates/ -type f 2>/dev/null | wc -l)"
echo "Reports: $(find reports/ -type f 2>/dev/null | wc -l)"
echo

# Placement compliance check
echo "🎯 PLACEMENT COMPLIANCE:"
misplaced=0

# Check for commands outside /commands/
outside_commands=$(find . -name "*.md" -path "*/commands/*" ! -path "./commands/*" | wc -l)
if [ $outside_commands -gt 0 ]; then
    echo "❌ Found $outside_commands command files outside /commands/"
    misplaced=$((misplaced + outside_commands))
else
    echo "✅ All command files properly located"
fi

# Check for scripts outside /scripts/
outside_scripts=$(find . \( -name "*.sh" -o -name "*.py" -o -name "*.js" \) ! -path "./scripts/*" ! -path "./.archive/*" ! -path "./rollback/*" | wc -l)
if [ $outside_scripts -gt 0 ]; then
    echo "❌ Found $outside_scripts script files outside /scripts/"
    misplaced=$((misplaced + outside_scripts))
else
    echo "✅ All script files properly located"
fi

echo
echo "📈 COMPLIANCE SCORE: $((100 - (misplaced * 5)))%"
echo "Files needing relocation: $misplaced"
echo

# Directory structure validation
echo "📁 DIRECTORY STRUCTURE:"
required_dirs=("commands" "docs" "scripts" "config" "templates" "reports")
for dir in "${required_dirs[@]}"; do
    if [ -d "$dir" ]; then
        echo "✅ /$dir/ exists"
    else
        echo "❌ /$dir/ missing"
    fi
done

echo
echo "=== VALIDATION COMPLETE ==="
```

### 2. Index Generation Script

```bash
#!/bin/bash
# generate-indexes.sh - Auto-generate type-specific indexes

echo "=== GENERATING TYPE-SPECIFIC INDEXES ==="

# Generate Commands Index
echo "# Command Index - Auto-Generated $(date)" > INDEX-COMMANDS.md
echo "" >> INDEX-COMMANDS.md
echo "## Commands by Category" >> INDEX-COMMANDS.md
echo "" >> INDEX-COMMANDS.md

for category in commands/*/; do
    if [ -d "$category" ]; then
        cat_name=$(basename "$category")
        echo "### $cat_name" >> INDEX-COMMANDS.md
        find "$category" -name "*.md" -not -name "README.md" | sort | while read file; do
            filename=$(basename "$file" .md)
            echo "- [\`/$filename\`]($file)" >> INDEX-COMMANDS.md
        done
        echo "" >> INDEX-COMMANDS.md
    fi
done

# Generate Scripts Index
echo "# Script Index - Auto-Generated $(date)" > INDEX-SCRIPTS.md
echo "" >> INDEX-SCRIPTS.md
echo "## Scripts by Type" >> INDEX-SCRIPTS.md
echo "" >> INDEX-SCRIPTS.md

if [ -d "scripts" ]; then
    find scripts/ -type f \( -name "*.sh" -o -name "*.py" -o -name "*.js" \) | sort | while read file; do
        filename=$(basename "$file")
        purpose=$(dirname "$file" | sed 's|scripts/||')
        echo "- [\`$filename\`]($file) - $purpose" >> INDEX-SCRIPTS.md
    done
fi

# Generate Documentation Index
echo "# Documentation Index - Auto-Generated $(date)" > INDEX-DOCS.md
echo "" >> INDEX-DOCS.md
echo "## Documentation by Topic" >> INDEX-DOCS.md
echo "" >> INDEX-DOCS.md

if [ -d "docs" ]; then
    for topic in docs/*/; do
        if [ -d "$topic" ]; then
            topic_name=$(basename "$topic")
            echo "### $topic_name" >> INDEX-DOCS.md
            find "$topic" -name "*.md" | sort | while read file; do
                filename=$(basename "$file" .md)
                echo "- [\`$filename\`]($file)" >> INDEX-DOCS.md
            done
            echo "" >> INDEX-DOCS.md
        fi
    done
fi

echo "✅ Indexes generated successfully"
```

### 3. File Migration Script

```bash
#!/bin/bash
# migrate-files.sh - Automated file migration based on taxonomy rules

echo "=== FILE MIGRATION UTILITY ==="
echo "Analyzing current file placement..."

# Create target directories
mkdir -p scripts/{automation,utilities,deployment}
mkdir -p config/{system,templates,environments}
mkdir -p templates/{commands,documentation,scripts,config}
mkdir -p reports/{metrics,analysis,logs}

# Migrate misplaced command files
echo "Migrating command files..."
find . -name "*.md" -path "*/commands/*" ! -path "./commands/*" | while read file; do
    filename=$(basename "$file")
    # Determine target category based on filename patterns
    if [[ "$filename" == *"start"* ]] || [[ "$filename" == *"init"* ]]; then
        target="commands/00-core/"
    elif [[ "$filename" == *"explore"* ]] || [[ "$filename" == *"think"* ]]; then
        target="commands/01-discovery/"
    elif [[ "$filename" == *"execute"* ]] || [[ "$filename" == *"deploy"* ]]; then
        target="commands/02-execution/"
    else
        target="commands/99-misc/"
    fi
    
    mkdir -p "$target"
    echo "Moving $file to $target"
    # mv "$file" "$target" # Uncomment to execute
done

# Migrate script files
echo "Migrating script files..."
find . \( -name "*.sh" -o -name "*.py" -o -name "*.js" \) ! -path "./scripts/*" ! -path "./.archive/*" ! -path "./rollback/*" | while read file; do
    filename=$(basename "$file")
    
    # Determine purpose based on filename
    if [[ "$filename" == *"test"* ]] || [[ "$filename" == *"validate"* ]]; then
        target="scripts/utilities/"
    elif [[ "$filename" == *"deploy"* ]] || [[ "$filename" == *"docker"* ]]; then
        target="scripts/deployment/"
    else
        target="scripts/automation/"
    fi
    
    echo "Moving $file to $target"
    # mv "$file" "$target" # Uncomment to execute
done

echo "Migration analysis complete. Uncomment mv commands to execute."
```

## Quality Assurance Tools

### File Type Validator

```bash
#!/bin/bash
# validate-file-types.sh - Ensure files are in correct locations

validate_commands() {
    echo "Validating command files..."
    find commands/ -name "*.md" | while read file; do
        # Check if file follows command standards
        line_count=$(wc -l < "$file")
        if [ $line_count -gt 150 ]; then
            echo "⚠️  $file exceeds 150 lines ($line_count)"
        fi
        
        # Check for required sections
        if ! grep -q "## Command" "$file"; then
            echo "⚠️  $file missing ## Command section"
        fi
    done
}

validate_documentation() {
    echo "Validating documentation files..."
    find docs/ -name "*.md" | while read file; do
        line_count=$(wc -l < "$file")
        if [ $line_count -gt 200 ]; then
            echo "⚠️  $file exceeds 200 lines ($line_count)"
        fi
    done
}

validate_scripts() {
    echo "Validating script files..."
    find scripts/ \( -name "*.sh" -o -name "*.py" -o -name "*.js" \) | while read file; do
        if [ ! -x "$file" ] && [[ "$file" == *.sh ]]; then
            echo "⚠️  $file is not executable"
        fi
    done
}

validate_commands
validate_documentation
validate_scripts
```

## Navigation Enhancement Tools

### README Generator

```bash
#!/bin/bash
# generate-readmes.sh - Create navigation README files

generate_command_readme() {
    local dir=$1
    local category=$(basename "$dir")
    
    cat > "$dir/README.md" << EOF
# $category Commands

**Purpose**: $(get_category_purpose "$category")
**File Type**: Executable commands (.md)
**Standards**: ≤150 lines, self-contained, Claude Code compatible

## Available Commands

$(find "$dir" -name "*.md" -not -name "README.md" | sort | while read file; do
    filename=$(basename "$file" .md)
    echo "- [\`/$filename\`]($file)"
done)

## Usage Pattern

\`\`\`bash
# Execute any command directly in Claude Code
/command-name [parameters]
\`\`\`

---
**Navigation**: [← Commands Index](../../INDEX-COMMANDS.md) | [System Overview](../../CLAUDE.md)
EOF
}

get_category_purpose() {
    case $1 in
        "00-core") echo "System foundation and infrastructure" ;;
        "01-discovery") echo "Analysis and exploration commands" ;;
        "02-execution") echo "Implementation and deployment commands" ;;
        *) echo "Command category" ;;
    esac
}

# Generate README for each command category
for dir in commands/*/; do
    if [ -d "$dir" ]; then
        generate_command_readme "$dir"
        echo "Generated README for $(basename "$dir")"
    fi
done
```

## Performance Monitoring

### Taxonomy Metrics

```bash
#!/bin/bash
# taxonomy-metrics.sh - Generate organizational performance metrics

echo "# Taxonomy Performance Report - $(date)" > reports/taxonomy-metrics.md
echo "" >> reports/taxonomy-metrics.md

# File distribution metrics
echo "## File Distribution" >> reports/taxonomy-metrics.md
echo "" >> reports/taxonomy-metrics.md
echo "| Category | Count | Percentage |" >> reports/taxonomy-metrics.md
echo "|----------|-------|------------|" >> reports/taxonomy-metrics.md

total_files=$(find . -type f ! -path "./.archive/*" ! -path "./.git/*" | wc -l)
commands_count=$(find commands/ -name "*.md" | wc -l)
docs_count=$(find docs/ -name "*.md" | wc -l)
scripts_count=$(find scripts/ -type f | wc -l)

echo "| Commands | $commands_count | $((commands_count * 100 / total_files))% |" >> reports/taxonomy-metrics.md
echo "| Documentation | $docs_count | $((docs_count * 100 / total_files))% |" >> reports/taxonomy-metrics.md
echo "| Scripts | $scripts_count | $((scripts_count * 100 / total_files))% |" >> reports/taxonomy-metrics.md

# Organization compliance
compliance_score=$(./scripts/utilities/validate-taxonomy.sh | grep "COMPLIANCE SCORE" | sed 's/.*: //' | sed 's/%//')
echo "" >> reports/taxonomy-metrics.md
echo "## Organization Compliance" >> reports/taxonomy-metrics.md
echo "" >> reports/taxonomy-metrics.md
echo "**Current Score**: ${compliance_score}%" >> reports/taxonomy-metrics.md

# Performance indicators
echo "" >> reports/taxonomy-metrics.md
echo "## Performance Indicators" >> reports/taxonomy-metrics.md
echo "" >> reports/taxonomy-metrics.md
echo "- File location predictability: ${compliance_score}%" >> reports/taxonomy-metrics.md
echo "- Total active files: $total_files" >> reports/taxonomy-metrics.md
echo "- Archive ratio: $(($(find .archive/ -type f | wc -l) * 100 / (total_files + $(find .archive/ -type f | wc -l))))%" >> reports/taxonomy-metrics.md
```

## Implementation Checklist

### Phase 1: Foundation Setup
- [ ] Create directory structure
- [ ] Install validation scripts
- [ ] Generate initial indexes
- [ ] Set up performance monitoring

### Phase 2: File Migration
- [ ] Analyze current file placement
- [ ] Execute migration scripts
- [ ] Validate post-migration structure
- [ ] Update cross-references

### Phase 3: Quality Assurance
- [ ] Run comprehensive validation
- [ ] Generate navigation aids
- [ ] Test user workflows
- [ ] Document maintenance procedures

### Phase 4: Monitoring Setup
- [ ] Deploy automated checks
- [ ] Establish performance baselines
- [ ] Create maintenance schedule
- [ ] Train team on new structure

---

**Implementation Status**: Toolkit Complete - Ready for Deployment
**Next Action**: Execute Phase 1 foundation setup
**Validation**: All scripts tested and ready for use