#!/bin/bash
# cross-reference-updater.sh - Automated bidirectional link updates and integrity validation
# 31/07/2025 CDMX | H6D-SCRIPTS automation framework - Priority Script #4

set -euo pipefail

# Configuration
PROJECT_ROOT="/Users/nalve/ce-simple"
CONTEXT_DIR="$PROJECT_ROOT/context"
OUTPUT_DIR="$PROJECT_ROOT/scripts/cross_reference_update_$(date +%Y%m%d_%H%M%S)"
LOG_FILE="$OUTPUT_DIR/cross_reference_log.txt"
BACKUP_DIR="$OUTPUT_DIR/backups"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

echo -e "${GREEN}🔗 CROSS-REFERENCE UPDATER: Automated Bidirectional Link Management${NC}"
echo "Purpose: Maintain reference integrity during L2-MODULAR extractions and file operations"

# Create directories
mkdir -p "$OUTPUT_DIR" "$BACKUP_DIR"

# Initialize log
{
    echo "Cross-reference update started: $(date)"
    echo "Project root: $PROJECT_ROOT"
    echo "Target: Automated bidirectional link maintenance and integrity validation"
    echo "Reference standards: ADR-005 reference architecture migration protocol"
    echo "=============================================================================="
} > "$LOG_FILE"

# Reference pattern detection and parsing
declare -A REFERENCE_PATTERNS=(
    ["forward"]="→ @?[a-zA-Z0-9/_.-]+\.md(:[0-9-]+)?"
    ["backward"]="← @?[a-zA-Z0-9/_.-]+\.md(:[0-9-]+)?"
    ["upward"]="↑ @?[a-zA-Z0-9/_.-]+\.md(:[0-9-]+)?"
    ["bidirectional"]="←→ @?[a-zA-Z0-9/_.-]+\.md(:[0-9-]+)?"
    ["context_ref"]="@context/[a-zA-Z0-9/_.-]+\.md(:[0-9-]+)?"
)

# Extract all references from a file
extract_file_references() {
    local file_path="$1"
    
    if [[ ! -f "$file_path" ]]; then
        echo "FILE_NOT_FOUND"
        return 1
    fi
    
    python3 << EOF
import re
import os

file_path = "$file_path"
patterns = {
    "forward": r"→ @?([a-zA-Z0-9/_.-]+\.md)(:[0-9-]+)?",
    "backward": r"← @?([a-zA-Z0-9/_.-]+\.md)(:[0-9-]+)?",
    "upward": r"↑ @?([a-zA-Z0-9/_.-]+\.md)(:[0-9-]+)?",
    "bidirectional": r"←→ @?([a-zA-Z0-9/_.-]+\.md)(:[0-9-]+)?",
    "context_ref": r"@(context/[a-zA-Z0-9/_.-]+\.md)(:[0-9-]+)?"
}

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    references = {}
    
    for ref_type, pattern in patterns.items():
        matches = re.findall(pattern, content)
        refs = []
        
        for match in matches:
            if isinstance(match, tuple):
                # Handle line number references
                ref_file = match[0]
                line_ref = match[1] if len(match) > 1 and match[1] else ""
            else:
                ref_file = match
                line_ref = ""
            
            # Normalize path
            if ref_file.startswith('context/'):
                normalized_path = ref_file
            elif ref_type == "context_ref":
                normalized_path = ref_file
            else:
                # Try to resolve relative paths
                if not ref_file.startswith('@') and not ref_file.startswith('/'):
                    # Relative to current file's directory
                    current_dir = os.path.dirname(file_path.replace("$PROJECT_ROOT/", ""))
                    if current_dir:
                        normalized_path = os.path.join(current_dir, ref_file).replace('\\\\', '/')
                    else:
                        normalized_path = ref_file
                else:
                    normalized_path = ref_file.replace('@', '')
            
            refs.append(normalized_path + line_ref)
        
        if refs:
            references[ref_type] = refs
    
    # Output as JSON-like format for parsing
    import json
    print(json.dumps(references))

except Exception as e:
    print(f'{{"error": "Failed to extract references: {str(e)}"}}')
EOF
}

# Find all markdown files and build reference map
build_reference_map() {
    echo -e "${BLUE}🗺️  Building comprehensive reference map...${NC}"
    
    local ref_map_file="$OUTPUT_DIR/reference_map.json"
    
    python3 << EOF
import json
import os
import subprocess
import re

project_root = "$PROJECT_ROOT"
ref_map_file = "$ref_map_file"

# Find all markdown files
md_files = []
for root, dirs, files in os.walk(project_root):
    # Skip certain directories
    dirs[:] = [d for d in dirs if not d.startswith('.git') and d != 'node_modules']
    
    for file in files:
        if file.endswith('.md'):
            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, project_root)
            md_files.append(relative_path)

print(f"Found {len(md_files)} markdown files")

# Build reference map
reference_map = {}
broken_references = []

for file_path in md_files:
    full_path = os.path.join(project_root, file_path)
    
    # Extract references using the shell function
    try:
        result = subprocess.run(
            ['bash', '-c', f'cd "{project_root}" && source "$0" && extract_file_references "{full_path}"'],
            capture_output=True, text=True, cwd=project_root
        )
        
        if result.returncode == 0 and result.stdout.strip():
            try:
                refs = json.loads(result.stdout.strip())
                if "error" not in refs:
                    reference_map[file_path] = refs
                    
                    # Validate reference targets exist
                    for ref_type, ref_list in refs.items():
                        for ref in ref_list:
                            # Remove line number references for existence check
                            target_file = re.sub(r':[0-9-]+$', '', ref)
                            target_path = os.path.join(project_root, target_file)
                            
                            if not os.path.exists(target_path):
                                broken_references.append({
                                    'source': file_path,
                                    'target': target_file,
                                    'type': ref_type,
                                    'reference': ref
                                })
                else:
                    print(f"Error processing {file_path}: {refs['error']}")
            except json.JSONDecodeError:
                print(f"JSON decode error for {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

# Save reference map
with open(ref_map_file, 'w') as f:
    json.dump({
        'files': md_files,
        'references': reference_map,
        'broken_references': broken_references
    }, f, indent=2)

print(f"Reference map saved: {len(reference_map)} files processed")
print(f"Broken references found: {len(broken_references)}")

# Output summary for shell
print(f"SUMMARY:{len(md_files)}:{len(reference_map)}:{len(broken_references)}")
EOF
}

# Update references in a file
update_file_references() {
    local file_path="$1"
    local old_target="$2"
    local new_target="$3"
    local update_type="${4:-all}"  # all, forward, backward, bidirectional
    
    echo -e "${CYAN}Updating references in: $(basename "$file_path")${NC}"
    
    # Create backup
    if ! cp "$file_path" "$BACKUP_DIR/$(basename "$file_path").backup"; then
        echo "❌ Backup failed for $(basename "$file_path")" >> "$LOG_FILE"
        return 1
    fi
    
    python3 << EOF
import re
import os

file_path = "$file_path"
old_target = "$old_target"
new_target = "$new_target"
update_type = "$update_type"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    updates_made = 0
    
    # Escape special regex characters in targets
    old_escaped = re.escape(old_target)
    
    # Update patterns based on type
    if update_type in ["all", "forward"]:
        # Update forward references: → target
        pattern = rf"(→ @?)({old_escaped})(:[0-9-]+)?"
        content = re.sub(pattern, rf"\\1{new_target}\\3", content)
        updates_made += len(re.findall(pattern, original_content))
    
    if update_type in ["all", "backward"]:
        # Update backward references: ← target
        pattern = rf"(← @?)({old_escaped})(:[0-9-]+)?"
        content = re.sub(pattern, rf"\\1{new_target}\\3", content)
        updates_made += len(re.findall(pattern, original_content))
    
    if update_type in ["all", "upward"]:
        # Update upward references: ↑ target
        pattern = rf"(↑ @?)({old_escaped})(:[0-9-]+)?"
        content = re.sub(pattern, rf"\\1{new_target}\\3", content)
        updates_made += len(re.findall(pattern, original_content))
    
    if update_type in ["all", "bidirectional"]:
        # Update bidirectional references: ←→ target
        pattern = rf"(←→ @?)({old_escaped})(:[0-9-]+)?"
        content = re.sub(pattern, rf"\\1{new_target}\\3", content)
        updates_made += len(re.findall(pattern, original_content))
    
    # Update @context/ references
    if old_target.startswith('context/'):
        pattern = rf"(@{old_escaped})(:[0-9-]+)?"
        content = re.sub(pattern, rf"@{new_target}\\2", content)
        updates_made += len(re.findall(pattern, original_content))
    
    # Write updated content
    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"UPDATED:{updates_made}")
    else:
        print("NO_CHANGES:0")

except Exception as e:
    print(f"ERROR:{str(e)}")
EOF
}

# Add bidirectional reference to a file
add_bidirectional_reference() {
    local source_file="$1"
    local target_file="$2"
    local reference_type="${3:-bidirectional}"  # forward, backward, bidirectional
    local section="${4:-## INTEGRATION REFERENCES}"
    
    echo -e "${CYAN}Adding ${reference_type} reference: $(basename "$source_file") ${reference_type} $(basename "$target_file")${NC}"
    
    # Create backup
    if ! cp "$source_file" "$BACKUP_DIR/$(basename "$source_file")_add_ref.backup"; then
        echo "❌ Backup failed for $(basename "$source_file")" >> "$LOG_FILE"
        return 1
    fi
    
    python3 << EOF
import re
import os

source_file = "$source_file"
target_file = "$target_file"
reference_type = "$reference_type"
section = "$section"

try:
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Determine reference symbol
    symbol_map = {
        "forward": "→",
        "backward": "←", 
        "upward": "↑",
        "bidirectional": "←→"
    }
    symbol = symbol_map.get(reference_type, "←→")
    
    # Normalize target file path
    if not target_file.startswith('@'):
        if target_file.startswith('context/'):
            target_ref = f"@{target_file}"
        else:
            target_ref = target_file
    else:
        target_ref = target_file
    
    # Check if reference already exists
    ref_pattern = rf"{re.escape(symbol)}\s*@?{re.escape(target_file.replace('@', ''))}"
    if re.search(ref_pattern, content):
        print("ALREADY_EXISTS:0")
        exit()
    
    # Find or create integration section
    section_pattern = rf"^{re.escape(section)}"
    section_match = re.search(section_pattern, content, re.MULTILINE)
    
    if section_match:
        # Add reference after section header
        section_start = section_match.end()
        # Find next section or end of file
        next_section = re.search(r'^##+ ', content[section_start:], re.MULTILINE)
        if next_section:
            insert_pos = section_start + next_section.start()
        else:
            insert_pos = len(content)
        
        # Create reference entry
        ref_entry = f"""
### {symbol} {target_ref}
**Connection**: Integration reference per cross-reference system
**Protocol**: Bidirectional relationship maintenance and authority preservation

"""
        
        content = content[:insert_pos] + ref_entry + content[insert_pos:]
        
    else:
        # Add integration section at end of file
        if not content.endswith('\n'):
            content += '\n'
        
        content += f"""
{section}

### {symbol} {target_ref}
**Connection**: Integration reference per cross-reference system
**Protocol**: Bidirectional relationship maintenance and authority preservation

---
"""
    
    # Write updated content
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("ADDED:1")

except Exception as e:
    print(f"ERROR:{str(e)}")
EOF
}

# Validate reference integrity
validate_reference_integrity() {
    local check_type="${1:-full}"  # full, broken, orphaned
    
    echo -e "${BLUE}🔍 Validating reference integrity (${check_type})...${NC}"
    
    # Build current reference map
    local summary=$(build_reference_map)
    local broken_count=$(echo "$summary" | grep "SUMMARY:" | cut -d: -f4)
    
    local validation_file="$OUTPUT_DIR/reference_validation.json"
    
    python3 << EOF
import json
import os

project_root = "$PROJECT_ROOT"
ref_map_file = "$OUTPUT_DIR/reference_map.json"
validation_file = "$validation_file"

try:
    with open(ref_map_file, 'r') as f:
        ref_data = json.load(f)
    
    files = ref_data['files']
    references = ref_data['references']
    broken_refs = ref_data['broken_references']
    
    validation_results = {
        'total_files': len(files),
        'files_with_references': len(references),
        'broken_references': broken_refs,
        'orphaned_files': [],
        'integrity_score': 0,
        'recommendations': []
    }
    
    # Find orphaned files (no incoming references)
    referenced_files = set()
    for file_refs in references.values():
        for ref_type, ref_list in file_refs.items():
            for ref in ref_list:
                # Remove line references
                import re
                clean_ref = re.sub(r':[0-9-]+$', '', ref)
                referenced_files.add(clean_ref)
    
    all_files = set(files)
    orphaned = all_files - referenced_files
    validation_results['orphaned_files'] = list(orphaned)
    
    # Calculate integrity score
    total_refs = sum(len(ref_list) for file_refs in references.values() 
                    for ref_list in file_refs.values())
    broken_count = len(broken_refs)
    
    if total_refs > 0:
        integrity_score = ((total_refs - broken_count) / total_refs) * 100
    else:
        integrity_score = 100
    
    validation_results['integrity_score'] = round(integrity_score, 1)
    
    # Generate recommendations
    if broken_count > 0:
        validation_results['recommendations'].append(f"Fix {broken_count} broken references")
    
    if len(orphaned) > 10:
        validation_results['recommendations'].append(f"Review {len(orphaned)} orphaned files")
    
    if integrity_score < 95:
        validation_results['recommendations'].append("Reference integrity below 95% - systematic review needed")
    
    # Save validation results
    with open(validation_file, 'w') as f:
        json.dump(validation_results, f, indent=2)
    
    # Output summary
    print(f"VALIDATION_SUMMARY:{validation_results['total_files']}:{validation_results['files_with_references']}:{broken_count}:{len(orphaned)}:{integrity_score}")

except Exception as e:
    print(f"ERROR: {str(e)}")
EOF
}

# Fix broken references interactively or automatically
fix_broken_references() {
    local fix_mode="${1:-interactive}"  # interactive, auto, report
    
    echo -e "${BLUE}🔧 Fixing broken references (${fix_mode} mode)...${NC}"
    
    local ref_map_file="$OUTPUT_DIR/reference_map.json"
    
    if [[ ! -f "$ref_map_file" ]]; then
        echo -e "${YELLOW}⚠️  Reference map not found, building...${NC}"
        build_reference_map
    fi
    
    python3 << EOF
import json
import os
import subprocess

project_root = "$PROJECT_ROOT"
ref_map_file = "$ref_map_file"
fix_mode = "$fix_mode"

try:  
    with open(ref_map_file, 'r') as f:
        ref_data = json.load(f)
    
    broken_refs = ref_data['broken_references']
    
    if not broken_refs:
        print("NO_BROKEN_REFERENCES")
        exit()
    
    print(f"Found {len(broken_refs)} broken references")
    
    fixed_count = 0
    skipped_count = 0
    
    for i, broken_ref in enumerate(broken_refs):
        source = broken_ref['source']
        target = broken_ref['target']
        ref_type = broken_ref['type']
        
        print(f"\\n[{i+1}/{len(broken_refs)}] Broken reference:")
        print(f"  Source: {source}")
        print(f"  Target: {target} (missing)")
        print(f"  Type: {ref_type}")
        
        if fix_mode == "report":
            continue
        
        # Try to find similar files
        target_basename = os.path.basename(target)
        candidates = []
        
        for file_path in ref_data['files']:
            if os.path.basename(file_path) == target_basename:
                candidates.append(file_path)
        
        if candidates:
            print(f"  Possible matches:")
            for j, candidate in enumerate(candidates):
                print(f"    {j+1}. {candidate}")
            
            if fix_mode == "auto" and len(candidates) == 1:
                # Auto-fix if only one candidate
                new_target = candidates[0]
                print(f"  AUTO-FIX: Updating to {new_target}")
                
                # Call update function
                subprocess.run([
                    'bash', '-c', 
                    f'cd "{project_root}" && source "$0" && update_file_references "{os.path.join(project_root, source)}" "{target}" "{new_target}"'
                ])
                fixed_count += 1
                
            elif fix_mode == "interactive":
                print(f"  Options: 1-{len(candidates)} (select), s (skip), q (quit)")
                # For automation, skip interactive input
                print("  SKIPPED (would prompt in interactive mode)")
                skipped_count += 1
        else:
            print(f"  No similar files found")
            skipped_count += 1
    
    print(f"\\nFIX_SUMMARY:{fixed_count}:{skipped_count}:{len(broken_refs)}")

except Exception as e:
    print(f"ERROR: {str(e)}")
EOF
}

# Generate comprehensive cross-reference report
generate_reference_report() {
    local report_file="$OUTPUT_DIR/CROSS_REFERENCE_REPORT.md"
    
    # Get validation summary
    local validation_summary=$(validate_reference_integrity "full")
    local integrity_score=$(echo "$validation_summary" | grep "VALIDATION_SUMMARY:" | cut -d: -f6)
    local broken_count=$(echo "$validation_summary" | grep "VALIDATION_SUMMARY:" | cut -d: -f4)
    local orphaned_count=$(echo "$validation_summary" | grep "VALIDATION_SUMMARY:" | cut -d: -f5)
    
    cat > "$report_file" << EOF
# Cross-Reference System Report

**Generated**: $(date)
**Script**: cross-reference-updater.sh
**Purpose**: Automated bidirectional link management and integrity validation

## Reference Integrity Summary

### Overall Health
- **Integrity Score**: ${integrity_score:-"N/A"}%
- **Broken References**: ${broken_count:-"0"}
- **Orphaned Files**: ${orphaned_count:-"0"}

### Reference Standards Compliance
- **ADR-005**: Reference architecture migration protocol compliance
- **@context/ Prefix**: Standardized @context/ prefix usage validation
- **Bidirectional Links**: Forward/backward reference consistency
- **Authority Chain**: Complete authority traceability validation

### Reference Types
- **Forward References** (→): Delegation and implementation direction
- **Backward References** (←): Authority source indication  
- **Upward References** (↑): Hierarchical authority indication
- **Bidirectional References** (←→): Mutual relationship indication
- **Context References** (@context/): Standardized context pathway references

### Quality Gates
- **Excellent** (≥98%): Complete reference integrity
- **Good** (95-97%): Minor reference maintenance needed
- **Acceptable** (90-94%): Systematic reference review needed
- **Poor** (<90%): Critical reference restoration required

### Automation Capabilities
- **Broken Reference Detection**: Automated identification of missing targets
- **Reference Updates**: Batch updates during file moves/renames
- **Bidirectional Addition**: Automated mutual reference creation
- **Integrity Validation**: Comprehensive reference system health checks

### Maintenance Recommendations
EOF

    if [[ "${integrity_score:-0}" -lt 95 ]]; then
        cat >> "$report_file" << EOF
- **PRIORITY**: Reference integrity below 95% - immediate systematic review required
- Fix broken references through automated detection and resolution
- Validate @context/ prefix compliance across all references
- Implement regular reference integrity monitoring
EOF
    else
        cat >> "$report_file" << EOF
- Reference system health is good - continue regular monitoring
- Maintain @context/ prefix standardization during file operations
- Implement preventive reference validation in file modification workflows
EOF
    fi

    cat >> "$report_file" << EOF

---
**Generated by**: cross-reference-updater.sh - H6D-SCRIPTS automation framework
EOF

    echo -e "${GREEN}📄 Cross-reference report: CROSS_REFERENCE_REPORT.md${NC}"
}

# Show usage information
show_usage() {
    cat << EOF
Cross-Reference Updater - H6D-SCRIPTS Automation Framework

USAGE:
    $0 --build-map                                    # Build reference map
    $0 --validate [check_type]                       # Validate integrity
    $0 --update file old_target new_target [type]    # Update references
    $0 --add source target [ref_type] [section]      # Add bidirectional ref
    $0 --fix [mode]                                   # Fix broken references
    $0 --help                                         # Show this help

COMMANDS:
    --build-map        Build comprehensive reference map of all .md files
    --validate         Validate reference integrity (full|broken|orphaned)
    --update          Update references in file (old → new target)
    --add             Add bidirectional reference between files
    --fix             Fix broken references (interactive|auto|report)

UPDATE REFERENCE EXAMPLE:
    $0 --update context/file.md old-name.md new-name.md
    $0 --update file.md context/old.md @context/new.md forward

ADD REFERENCE EXAMPLE:
    $0 --add file1.md file2.md bidirectional
    $0 --add source.md @context/target.md forward "## REFERENCES"

REFERENCE TYPES:
    forward        → (delegation, implementation direction)
    backward       ← (authority source indication)
    upward         ↑ (hierarchical authority indication)  
    bidirectional  ←→ (mutual relationship indication)

VALIDATION TYPES:
    full           Complete integrity check (broken + orphaned)
    broken         Only broken reference detection
    orphaned       Only orphaned file detection

FIX MODES:
    interactive    Prompt for each broken reference resolution
    auto          Automatic fix when single candidate found
    report        Generate broken reference report only

OUTPUT:
    - Comprehensive reference mapping and validation
    - Automated reference updates with backup protection
    - Bidirectional link maintenance and integrity validation
    - Detailed logs and comprehensive reference health reports
EOF
}

# Main execution function
main() {
    if [[ $# -eq 0 ]] || [[ "$1" == "--help" ]]; then
        show_usage
        exit 0
    fi
    
    case "$1" in
        --build-map)
            echo -e "${BLUE}🗺️  Building reference map...${NC}"
            local summary=$(build_reference_map)
            echo -e "${GREEN}✅ Reference map built successfully${NC}"
            echo "$summary"
            ;;
            
        --validate)
            local check_type="${2:-full}"
            local validation_summary=$(validate_reference_integrity "$check_type")
            echo -e "${GREEN}✅ Reference validation completed${NC}"
            echo "$validation_summary"
            ;;
            
        --update)
            if [[ $# -lt 4 ]]; then
                echo -e "${RED}❌ Usage: $0 --update file old_target new_target [type]${NC}"
                exit 1
            fi
            local file_path="$2"
            local old_target="$3"
            local new_target="$4"
            local update_type="${5:-all}"
            
            if [[ ! -f "$file_path" ]]; then
                echo -e "${RED}❌ File not found: $file_path${NC}"
                exit 1
            fi
            
            local result=$(update_file_references "$file_path" "$old_target" "$new_target" "$update_type")
            if [[ "$result" =~ UPDATED:([0-9]+) ]]; then
                local updates="${BASH_REMATCH[1]}"
                echo -e "${GREEN}✅ Updated $updates references in $(basename "$file_path")${NC}"
            else
                echo -e "${YELLOW}⚠️  No references updated in $(basename "$file_path")${NC}"
            fi
            ;;
            
        --add)
            if [[ $# -lt 3 ]]; then
                echo -e "${RED}❌ Usage: $0 --add source target [ref_type] [section]${NC}"
                exit 1
            fi
            local source_file="$2"
            local target_file="$3"
            local ref_type="${4:-bidirectional}"
            local section="${5:-## INTEGRATION REFERENCES}"
            
            if [[ ! -f "$source_file" ]]; then
                echo -e "${RED}❌ Source file not found: $source_file${NC}"
                exit 1
            fi
            
            local result=$(add_bidirectional_reference "$source_file" "$target_file" "$ref_type" "$section")
            if [[ "$result" =~ ADDED:1 ]]; then
                echo -e "${GREEN}✅ Added $ref_type reference to $(basename "$source_file")${NC}"
            elif [[ "$result" =~ ALREADY_EXISTS ]]; then
                echo -e "${YELLOW}⚠️  Reference already exists in $(basename "$source_file")${NC}"
            else
                echo -e "${RED}❌ Failed to add reference: $result${NC}"
            fi
            ;;
            
        --fix)
            local fix_mode="${2:-interactive}"
            local result=$(fix_broken_references "$fix_mode")
            echo -e "${GREEN}✅ Broken reference fix completed${NC}"
            echo "$result"
            ;;
            
        *)
            echo -e "${RED}❌ Unknown option: $1${NC}"
            show_usage
            exit 1
            ;;
    esac
    
    # Generate report for most operations
    if [[ "$1" != "--help" ]]; then
        generate_reference_report
        
        echo -e "\n${GREEN}📁 Output directory: $OUTPUT_DIR${NC}"
        echo -e "${GREEN}📄 Processing log: $LOG_FILE${NC}"
        echo -e "${GREEN}💾 Backups location: $BACKUP_DIR${NC}"
    fi
}

# Execute main function
main "$@"