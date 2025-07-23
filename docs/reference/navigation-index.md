# Navigation Index

**Purpose**: Comprehensive navigation guide for predictable file location across the project.

## Directory Structure Overview

```
ce-simple/
├── commands/           # Executable slash commands (.md)
├── automation/         # Scripts and automated systems
│   ├── core/          # Python intelligence systems
│   ├── scripts/       # Shell operational scripts
│   ├── testing/       # Validation and test scripts
│   └── config/        # Configuration files
├── docs/              # Documentation system
│   ├── active/        # Current specifications (≤150 lines)
│   ├── implementation/# Detailed implementation guides
│   ├── standards/     # Consolidated standards
│   └── reference/     # Cross-reference matrices
├── templates/         # Unified template system
│   ├── commands/      # Command templates
│   ├── documents/     # Documentation templates
│   ├── workflows/     # Process templates
│   ├── validation/    # QA templates
│   ├── automation/    # Script templates
│   ├── standards/     # Standard templates
│   └── integration/   # Integration templates
└── .archive/          # Legacy system preservation
```

## Predictable Location Patterns

### File Type → Location Rules

| File Type | Extension | Primary Location | Secondary Locations |
|-----------|-----------|------------------|-------------------|
| **Executable Commands** | `.md` | `commands/{category}/` | - |
| **Python Scripts** | `.py` | `automation/core/` | `automation/testing/` |
| **Shell Scripts** | `.sh` | `automation/scripts/` | `automation/testing/` |
| **JavaScript** | `.js` | `automation/scripts/` | `automation/scripts/web/` |
| **Configuration** | `.json`, `.yaml`, `.toml` | `automation/config/` | - |
| **Documentation** | `.md` | `docs/active/` | `docs/implementation/`, `docs/standards/` |
| **Templates** | `.md`, `.py`, `.sh` | `templates/{category}/` | - |

### Content Purpose → Subdirectory Rules

| Content Purpose | Primary Location | Pattern |
|----------------|------------------|---------|
| **Intelligence Systems** | `automation/core/` | `*orchestrat*`, `*intelligence*`, `*governance*` |
| **Operational Scripts** | `automation/scripts/` | `*git*`, `*deploy*`, `*setup*` |
| **Test Systems** | `automation/testing/` | `*test*`, `*validation*` |
| **Current Specs** | `docs/active/` | `*spec*`, current procedures |
| **Detailed Guides** | `docs/implementation/` | `*implementation*`, `*guide*` |
| **Standards** | `docs/standards/` | `*standard*`, `*policy*` |
| **Navigation** | `docs/reference/` | `*index*`, `*matrix*`, `README` |

## Quick Navigation Patterns

### By File Type
```bash
# Find all Python intelligence systems
find automation/core -name "*.py"

# Find all operational shell scripts  
find automation/scripts -name "*.sh"

# Find all current documentation specs
find docs/active -name "*.md"

# Find all implementation guides
find docs/implementation -name "*implementation*"
```

### By Purpose
```bash
# Find orchestration systems
find automation/core -name "*orchestrat*"

# Find validation systems
find automation/testing -name "*test*" -o -name "*validation*"

# Find standards documentation
find docs/standards -name "*standard*"

# Find templates by category
find templates -name "*template*"
```

### By Integration Point
```bash
# Command system integration
find commands -name "*.md" | head -10
find docs/commands -name "*implementation*"

# Automation system integration  
find automation -type f -executable
find docs/implementation -name "*automation*"

# Documentation system integration
find docs -name "README.md"
find templates/documents -name "*template*"
```

## Naming Conventions

### File Naming Patterns
- **Commands**: `{purpose}-{action}.md`
- **Scripts**: `{system}-{function}.py`, `{operation}-{action}.sh`
- **Documentation**: `{topic}-{type}.md`
- **Templates**: `{category}-{purpose}-template.{ext}`

### Directory Naming Patterns
- **Type-first**: Primary categorization by file type
- **Purpose-second**: Secondary categorization by content purpose
- **Consistent structure**: Parallel organization across categories

## Predictability Validation

**Target**: >95% file location predictability  
**Validation**: `automation/testing/taxonomy-validator.py`  
**Classification**: `automation/scripts/taxonomy-classifier.py`

## Integration Points

- **Commands → Documentation**: `commands/{category}/ ↔ docs/commands/`
- **Automation → Templates**: `automation/ ↔ templates/automation/`
- **Documentation → Standards**: `docs/ ↔ docs/standards/`
- **All Systems → Reference**: `docs/reference/` (navigation hub)

## Evolution Patterns

**File Lifecycle**:
1. **Creation**: Use appropriate template from `templates/{category}/`
2. **Development**: Place in predicted location based on type and purpose
3. **Documentation**: Create corresponding docs in `docs/implementation/`
4. **Standards**: Extract patterns to `docs/standards/`
5. **Reference**: Update navigation in `docs/reference/`

**Continuous Improvement**:
- Regular validation with taxonomy validator
- Pattern extraction and template updates
- Navigation index maintenance
- Predictability optimization