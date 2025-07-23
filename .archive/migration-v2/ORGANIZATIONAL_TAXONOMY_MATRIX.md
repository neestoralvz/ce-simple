# Organizational Taxonomy Matrix - ce-simple

**Mission**: Optimal organization combining categories with file types for maximum clarity and minimal cognitive load.

## Current State Analysis

**File Distribution**:
- **Total Files**: 1,358 markdown files (428 active, 930 archived)
- **Scripts/Config**: 20 active files (.sh, .py, .js, .json, .yaml)
- **Structure**: Hierarchical categories with mixed file type placement
- **Challenge**: File type scattered across multiple locations without type-specific organization

## Core Taxonomy Matrix

### Primary Dimensions

| **CATEGORY** | **PURPOSE** | **FILE TYPES** | **ORGANIZATION PATTERN** |
|--------------|-------------|----------------|--------------------------|
| **Systems** | Active operational components | Commands (.md), Scripts (.sh), Config (.json) | Function-first, type-secondary |
| **Documentation** | Knowledge and guidance | Documentation (.md), Templates (.md) | Type-first, purpose-secondary |
| **Legacy** | Historical preservation | All types (.md, .sh, .json, .yaml) | Chronological + type grouping |
| **Templates** | Reusable patterns | Templates (.md), Schemas (.json), Scripts (.sh) | Type-exclusive organization |
| **Research** | Analysis and insights | Reports (.md), Data (.json), Logs (.txt) | Type + temporal organization |

### File Type Classification

| **TYPE** | **EXTENSION** | **PRIMARY LOCATION** | **SECONDARY LOCATIONS** | **ORGANIZATION RULE** |
|----------|---------------|---------------------|------------------------|----------------------|
| **Executable Commands** | .md | `/commands/` | - | Function-based hierarchy |
| **Documentation** | .md | `/docs/` | `/templates/` | Topic-based hierarchy |
| **Scripts** | .sh, .py, .js | `/scripts/` | `/commands/utils/` | Purpose-based grouping |
| **Configuration** | .json, .yaml, .yml | `/config/` | `/templates/config/` | System-based grouping |
| **Templates** | .md, .json, .sh | `/templates/` | - | Type-specific subdirectories |
| **Reports** | .md, .txt, .json | `/reports/` | `/docs/analysis/` | Temporal + type organization |
| **Archive** | All types | `/.archive/` | - | Original structure preserved |

## Optimal Directory Structure

```
ce-simple/
├── commands/                    # EXECUTABLE COMMANDS (.md)
│   ├── 00-core/                # System foundation
│   ├── 01-discovery/           # Analysis commands  
│   ├── 02-execution/           # Implementation commands
│   └── [functional-hierarchy]  # By workflow phase
│
├── scripts/                    # EXECUTABLE SCRIPTS
│   ├── automation/             # .sh automation scripts
│   ├── utilities/              # .py, .js utility scripts
│   └── deployment/             # Deployment scripts
│
├── config/                     # CONFIGURATION FILES
│   ├── system/                 # .json system configs
│   ├── templates/              # .yaml template configs
│   └── environments/           # Environment-specific configs
│
├── docs/                       # DOCUMENTATION (.md)
│   ├── guides/                 # User guides
│   ├── architecture/           # System architecture
│   ├── standards/              # Development standards
│   └── analysis/               # Research and analysis
│
├── templates/                  # REUSABLE TEMPLATES
│   ├── commands/               # .md command templates
│   ├── documentation/          # .md doc templates
│   ├── scripts/                # .sh script templates
│   └── config/                 # .json, .yaml config templates
│
├── reports/                    # ANALYSIS & REPORTS
│   ├── metrics/                # .json performance data
│   ├── analysis/               # .md analytical reports
│   └── logs/                   # .txt, .log system logs
│
└── .archive/                   # LEGACY PRESERVATION
    ├── [original-structure]    # Preserved as-is
    └── migration-logs/         # Migration tracking
```

## Category x File Type Placement Rules

### Rule Matrix

| **FILE TYPE** | **Systems** | **Documentation** | **Legacy** | **Templates** | **Research** |
|---------------|-------------|-------------------|------------|---------------|--------------|
| **Command (.md)** | `/commands/` | - | `/.archive/commands/` | `/templates/commands/` | - |
| **Doc (.md)** | - | `/docs/` | `/.archive/docs/` | `/templates/documentation/` | `/reports/analysis/` |
| **Script (.sh)** | `/scripts/automation/` | - | `/.archive/scripts/` | `/templates/scripts/` | - |
| **Config (.json)** | `/config/system/` | - | `/.archive/config/` | `/templates/config/` | `/reports/metrics/` |
| **Template (.md)** | - | - | `/.archive/templates/` | `/templates/` | - |
| **Report (.md)** | - | `/docs/analysis/` | `/.archive/reports/` | - | `/reports/analysis/` |
| **Data (.json)** | - | - | `/.archive/data/` | - | `/reports/metrics/` |

### Placement Decision Tree

```
File Type Decision Tree:
├── Is it executable? 
│   ├── Command (.md) → /commands/[function]/
│   └── Script (.sh, .py, .js) → /scripts/[purpose]/
├── Is it configuration?
│   └── Config (.json, .yaml) → /config/[system]/
├── Is it a template?
│   └── Template (any type) → /templates/[type]/
├── Is it documentation?
│   └── Doc (.md) → /docs/[topic]/
├── Is it analysis/data?
│   └── Report/Data → /reports/[type]/
└── Is it historical?
    └── Any type → /.archive/[original-path]/
```

## Navigation Strategy

### Type-First Navigation

**Primary Access Points**:
- **Commands**: `/commands/` - Direct functional access
- **Scripts**: `/scripts/` - Executable automation tools  
- **Documentation**: `/docs/` - Knowledge base access
- **Templates**: `/templates/` - Reusable pattern library
- **Reports**: `/reports/` - Analysis and metrics
- **Archive**: `/.archive/` - Historical reference

### Cross-Reference System

**Index Files** (auto-generated):
- `/INDEX-COMMANDS.md` - All executable commands by type
- `/INDEX-SCRIPTS.md` - All scripts by purpose and type
- `/INDEX-DOCS.md` - All documentation by topic and type
- `/INDEX-TEMPLATES.md` - All templates by type and purpose
- `/INDEX-REPORTS.md` - All reports by date and type

**Navigation Aids**:
- Type-specific README files in each directory
- Cross-references between related file types
- Automated link validation and maintenance

## Type-Specific Consolidation Workflows

### Command Consolidation (.md)
1. **Identify**: Find all command files across locations
2. **Categorize**: Group by functional workflow phase
3. **Standardize**: Apply 150-line limit and structure standards
4. **Relocate**: Move to appropriate `/commands/` subdirectory
5. **Link**: Update cross-references and index files

### Script Consolidation (.sh, .py, .js)
1. **Audit**: Catalog all executable scripts
2. **Purpose Analysis**: Group by automation purpose
3. **Deduplicate**: Merge similar functionality
4. **Relocate**: Move to `/scripts/[purpose]/`
5. **Document**: Create usage documentation

### Documentation Consolidation (.md)
1. **Content Analysis**: Categorize by topic and purpose
2. **Quality Assessment**: Apply documentation standards
3. **Hierarchy Design**: Create logical topic structure
4. **Consolidation**: Merge redundant documentation
5. **Cross-Link**: Establish navigation connections

### Configuration Consolidation (.json, .yaml)
1. **System Mapping**: Group by target system
2. **Template Extraction**: Identify reusable patterns
3. **Validation**: Ensure schema compliance
4. **Organization**: Move to `/config/[system]/`
5. **Documentation**: Create configuration guides

## Maintenance Framework

### Automated Maintenance

**File Type Monitoring**:
```bash
# Daily type distribution check
find . -type f -name "*.md" | wc -l > /reports/metrics/md-count.txt
find . -type f -name "*.sh" | wc -l > /reports/metrics/script-count.txt
find . -type f -name "*.json" | wc -l > /reports/metrics/config-count.txt
```

**Organization Validation**:
```bash
# Weekly structure compliance check
./scripts/automation/validate-taxonomy.sh
```

**Index Generation**:
```bash
# Auto-generate type-specific indexes
./scripts/automation/generate-indexes.sh
```

### Manual Maintenance Schedule

**Weekly**:
- Validate file type placement compliance
- Update cross-reference indexes
- Review new file categorization

**Monthly**:
- Analyze type distribution trends
- Optimize directory structure
- Archive outdated files

**Quarterly**:
- Complete taxonomy review
- Update placement rules
- Performance optimization

## Implementation Roadmap

### Phase 1: Foundation (Week 1)
- [ ] Create new directory structure
- [ ] Implement placement decision tree
- [ ] Develop automated validation scripts

### Phase 2: Migration (Week 2-3)
- [ ] Command file consolidation
- [ ] Script organization and cleanup
- [ ] Documentation restructuring

### Phase 3: Optimization (Week 4)
- [ ] Cross-reference system implementation
- [ ] Navigation aid creation
- [ ] Performance monitoring setup

### Phase 4: Maintenance (Ongoing)
- [ ] Automated monitoring deployment
- [ ] Regular validation procedures
- [ ] Continuous optimization

## Success Metrics

**Organization Efficiency**:
- File location predictability: >95%
- Cross-reference accuracy: >98%
- Navigation time reduction: >50%

**Maintenance Overhead**:
- Automated validation coverage: >90%
- Manual maintenance time: <2 hours/week
- Organization drift rate: <5%/month

**User Experience**:
- File discovery time: <30 seconds
- Type identification accuracy: >95%
- Navigation satisfaction: >4.5/5

---

**Implementation Status**: Design Complete - Ready for Implementation
**Next Action**: Execute Phase 1 foundation setup
**Validation**: Automated compliance checking ready