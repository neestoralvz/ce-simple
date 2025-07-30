# Setup Validation Module

## Auto-Detection Logic Template
```bash
# Primary detection
if [ ! -d "./context" ]; then
    echo "No context structure detected - initializing project"
    setup_required=true
else
    echo "Context structure exists - validating completeness"
    setup_required=false
fi

# Secondary validation
required_files=(
    "./@context/architecture/core/truth-source.md"
    "./context/architecture/core/methodology.md"
    "./context/architecture/core/authority.md"
    "./context/vision/simplicity.md"
    "./context/architecture/claude_code/orchestration_protocols.md"
)

missing_files=()
for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        missing_files+=("$file")
        setup_required=true
    fi
done
```

## Validation Checklist
After setup, verify:
1. All required directories exist
2. Core context files are readable
3. CLAUDE.md references resolve correctly
4. Global commands can access local context structure

**Usage**: Standard validation protocol for project setup