# Command Modularization - Progressive Disclosure Framework

## 🎯 Purpose
Define and implement command modularization strategies using Progressive Disclosure to maintain 150-line command limits while preserving full functionality.

## 🚀 Core Modularization Principles

### Progressive Disclosure Philosophy
**Definition**: Complex details → referenced files, not inline expansion  
**Source**: `docs/core/architectural-principles.md` - Simplicity First Framework  
**Goal**: Maintain cognitive load below 150 lines per command while providing comprehensive functionality

### Modularization Triggers
**MANDATORY when command exceeds**:
- **File Size**: >150 lines total
- **Complexity Score**: >7.0 rating
- **Implementation Detail**: Extensive tool call specifications
- **Usage Examples**: Multiple detailed scenarios

## 🔧 Modularization Strategies

### Strategy 1: Implementation Extraction
**Pattern**: Move detailed tool implementations to separate files
**Structure**:
```
command-name.md (≤150 lines)
├─ Essential command structure
├─ Core tool calls only  
└─ Reference to implementation file

docs/commands/command-name-implementation.md
├─ Detailed tool specifications
├─ Complex automation logic
├─ Error handling procedures
└─ Advanced configuration options
```

**Example Applied**:
- `command-maintain.md` (95 lines) → Core functionality
- `command-maintain-implementation.md` → Detailed specifications

### Strategy 2: Usage Documentation Separation
**Pattern**: Extract comprehensive usage examples and scenarios
**Structure**:
```
command-name.md (core)
└─ Basic usage only

docs/commands/command-name-usage.md
├─ Detailed examples
├─ Edge case scenarios
├─ Integration patterns
└─ Troubleshooting guide
```

### Strategy 3: Framework Documentation
**Pattern**: Extract complex frameworks to dedicated files
**Structure**:
```
command-name.md (core)
└─ Framework reference only

docs/commands/command-name-framework.md
├─ Detailed methodology
├─ Decision matrices
├─ Algorithms and logic
└─ Performance considerations
```

## 📋 Modularization Process

### Phase 1: Content Analysis
```bash
# Identify modularization candidates
wc -l .claude/commands/*.md | awk '$1>150 {print $2, $1 " lines"}' 

# Analyze content sections for extraction potential
grep -n "^### " command-file.md | while read line; do
  echo "Section: $line - Evaluate for extraction"
done
```

### Phase 2: Content Classification
**KEEP in main command**:
- 🎯 Purpose (essential)
- 🚀 Usage (basic format only)
- 🔧 Implementation (core steps only)
- ⚡ Triggers (essential flow only)
- Essential tool calls (simplified)

**EXTRACT to implementation file**:
- Detailed tool specifications
- Complex automation logic
- Extensive error handling
- Advanced configuration
- Performance optimization details

**EXTRACT to usage file**:
- Comprehensive examples
- Edge case scenarios
- Integration patterns
- Troubleshooting procedures

### Phase 3: Reference Integration
**Command File References**:
```markdown
## 🔧 Implementation
**CORE AUTOMATION**: Essential tool calls for basic functionality
**REFERENCE**: `docs/commands/command-name-implementation.md` for detailed specifications
**ADVANCED**: `docs/commands/command-name-framework.md` for methodology details
```

**Cross-Reference Standards**:
- **Bidirectional**: Implementation files reference back to main command
- **Consistent Naming**: `command-name-[suffix].md` pattern
- **Clear Purpose**: Each extracted file has specific focus

## 🎯 Quality Standards

### Size Targets After Modularization
- **Main Command**: ≤150 lines (target: 90-120 lines)
- **Implementation File**: ≤200 lines maximum
- **Usage File**: ≤150 lines maximum
- **Framework File**: ≤200 lines maximum

### Content Quality Requirements
**Main Command Must Retain**:
- Complete functional capability
- All essential tool calls
- Clear workflow understanding
- Autonomous execution ability

**Extracted Files Must Provide**:
- Comprehensive detail without duplication
- Clear relationship to main command
- Self-contained reference value
- Enhanced understanding of complex aspects

### Validation Checklist
- [ ] Main command ≤150 lines
- [ ] Functionality preserved
- [ ] References accurate and bidirectional  
- [ ] No content duplication
- [ ] Clear extraction rationale
- [ ] Enhanced cognitive load management

## 🔧 Implementation Tools

### Automated Modularization Support
```bash
# Extract implementation details automatically
extract_implementation() {
  local command_file="$1"
  local base_name=$(basename "$command_file" .md)
  
  # Create implementation file
  echo "# ${base_name^} Implementation Details" > "docs/commands/${base_name}-implementation.md"
  
  # Extract detailed sections
  sed -n '/### Detailed/,/^###/p' "$command_file" >> "docs/commands/${base_name}-implementation.md"
  
  # Replace in original with reference
  sed -i 's/### Detailed.*/### Implementation\n**REFERENCE**: `docs\/commands\/'$base_name'-implementation.md` for detailed specifications/' "$command_file"
}
```

### Reference Maintenance
```bash
# Validate all command references
validate_references() {
  grep -r "docs/commands/" .claude/commands/ | while IFS=: read file reference; do
    ref_file=$(echo "$reference" | grep -o 'docs/commands/[^`]*')
    if [ ! -f "$ref_file" ]; then
      echo "BROKEN REFERENCE: $file → $ref_file"
    fi
  done
}
```

## 📊 Success Metrics

### Modularization Effectiveness
- **Size Reduction**: Commands >150 lines → ≤150 lines
- **Functionality Preservation**: 100% capability retention
- **Reference Integrity**: 0 broken links
- **User Experience**: Improved cognitive load management

### Quality Indicators
- **Clarity**: Main command understandable independently
- **Completeness**: Implementation files provide full detail
- **Maintainability**: Updates can be made to extracted content
- **Reusability**: Implementation patterns applicable to other commands

## 🔗 Integration with System Standards

### Compliance with Writing Standards
**Alignment**: `docs/core/writing-standards.md` 150-line limits
**Enhancement**: Progressive disclosure improves density without sacrificing functionality

### Template Compatibility
**Structure**: Modularized commands follow standard template
**Extensions**: Implementation files use consistent structure
**References**: Clear integration with existing cross-reference system

### Anti-Bias Compliance
**Preservation**: Modularization maintains evidence-based processing
**Enhancement**: Extracted details allow more comprehensive analysis
**Validation**: References maintain exploration protocol compliance

---

**CRITICAL**: Command modularization through Progressive Disclosure enables functionality preservation within 150-line limits while maintaining comprehensive system capabilities. All modularized commands must retain full autonomous execution ability.