# Migration Guide: ce-simple v1.0 → v2.0

## Purpose
Comprehensive guide for migrating from monolithic command structure to the 15-category modular architecture.

## Migration Overview

### What's Changing
**v1.0**: Single-file commands with embedded logic (~/commands/*.md)
**v2.0**: Category-organized command modules (~/commands/00-14/*)

### Benefits of Migration
- **50% faster command discovery** through predictable categorization
- **3x better orchestration** via cross-category coordination
- **Unlimited scalability** through modular architecture
- **Enhanced learning** from category-based pattern recognition

## Pre-Migration Assessment

### Inventory Current Commands
```bash
# Identify all existing commands
find commands/ -name "*.md" -not -path "*/0*/" | sort

# Analyze command complexity and dependencies
grep -r "Task\|Orchestrat\|Execute" commands/*.md
```

### Categorization Mapping
Map existing commands to new category structure:

**Core Operations** → `00-core/`
- start.md, enhanced-start.md, system-monitor.md

**Discovery & Research** → `01-discovery/`  
- explore-codebase.md, explore-web.md, think-layers.md

**Development** → `04-execution/`
- command-create.md, agent-orchestration.md

**Maintenance** → `07-maintenance/`
- command-maintain.md, matrix-maintenance.md, context-optimize.md

**Git Operations** → `09-git/`
- worktree-start.md, worktree-close.md, worktree-cleanup.md

**Learning** → `08-learning/`
- capture-learnings.md

## Migration Process

### Phase 1: Structure Preparation
1. **Create Category Directories**
```bash
mkdir -p commands/{00..14}-{core,discovery,planning,analysis,execution,validation,documentation,maintenance,learning,git,standards,meta,math,search,utils}
```

2. **Generate Category READMEs**
Each category needs README.md with:
- Purpose and scope definition
- Command list and descriptions
- Cross-category relationships
- Usage patterns and examples

### Phase 2: Command Migration

#### Step 1: Identify Command Category
Use decision matrix:
```yaml
Command Analysis:
  Primary Function:
    - Entry point/orchestration → 00-core
    - Information gathering → 01-discovery  
    - Task breakdown → 02-planning
    - Deep analysis → 03-analysis
    - Implementation → 04-execution
    - Quality assurance → 05-validation
    - Documentation → 06-documentation
    - System maintenance → 07-maintenance
    - Learning/patterns → 08-learning
    - Version control → 09-git
    - Standards/compliance → 10-standards
    - System evolution → 11-meta
    - Calculations → 12-math
    - Search/discovery → 13-search
    - Utilities/helpers → 14-utils
```

#### Step 2: Update Command Structure
Transform each command:

**Before (v1.0)**:
```markdown
# Command Name
[All logic embedded]
[No category awareness]
[Monolithic structure]
```

**After (v2.0)**:
```markdown
# Command Name

## Category: XX-category-name
## Relations: Dependencies and triggers
## Usage Pattern: Clear workflow description

[Focused, category-aware logic]
[Cross-category orchestration]
[Standardized interfaces]
```

#### Step 3: Update Cross-References
- Replace direct command calls with category-aware orchestration
- Update documentation references to new locations
- Verify all internal links and dependencies

### Phase 3: System Integration

#### Update Core Entry Points
Modify primary commands (start, enhanced-start) to:
- Recognize new category structure
- Use category-aware orchestration
- Maintain backward compatibility during transition

#### Validation Framework
Create validation commands in `05-validation/`:
- Migration completeness checker
- Cross-reference integrity validator  
- Performance regression detector

#### Documentation Updates
Update all documentation:
- CLAUDE.md command paths
- Core architecture references
- Tutorial and example code

## Migration Timeline

### Week 1: Preparation
- Complete pre-migration assessment
- Create category structure
- Generate category READMEs

### Week 2: Core Migration  
- Migrate 00-core commands
- Update primary entry points
- Test basic orchestration

### Week 3: Command Categories
- Migrate discovery, execution, maintenance commands
- Update cross-references and dependencies
- Validate category relationships

### Week 4: Specialization
- Migrate remaining specialized commands
- Complete documentation updates
- Final validation and testing

## Compatibility Strategy

### Backward Compatibility
Maintain old command locations temporarily:
```markdown
# Legacy Command (Deprecated)
**DEPRECATED**: This command has moved to `XX-category/command-name.md`

[Redirect logic to new location]
[Migration notice for users]
```

### Gradual Migration
- Keep both systems running during transition
- Provide clear migration notices
- Monitor usage patterns and user feedback

## Validation Checklist

### Structure Validation
- [ ] All 15 categories created with READMEs
- [ ] Commands properly categorized
- [ ] No orphaned command files
- [ ] Category relationships documented

### Functionality Validation  
- [ ] All commands execute successfully
- [ ] Cross-category orchestration working
- [ ] Performance meets or exceeds v1.0
- [ ] Learning and pattern recognition active

### Documentation Validation
- [ ] All references updated to new structure
- [ ] Cross-references integrity verified
- [ ] Tutorial and examples functional
- [ ] Migration documentation complete

## Rollback Plan

### Emergency Rollback
If critical issues arise:
1. Revert to v1.0 structure immediately
2. Analyze failure points and root causes
3. Address issues before re-attempting migration
4. Update migration procedures based on learnings

### Rollback Triggers
- Performance degradation >20%
- Command execution failures >5%
- User workflow disruption
- Critical cross-reference breaks

## Post-Migration Optimization

### Performance Monitoring
Track key metrics:
- Command discovery time (<30 seconds target)
- Orchestration efficiency (parallel execution rate)
- Cross-category coordination success rate
- User satisfaction and adoption rate

### Continuous Improvement
- Monitor category utilization patterns
- Identify optimization opportunities
- Gather user feedback and iterate
- Evolve architecture based on learnings

---

**Migration Success**: When all commands operate efficiently within the 15-category structure, providing enhanced orchestration capabilities while maintaining full backward compatibility.

**Next Steps**: Begin with [category-taxonomy.md](category-taxonomy.md) for detailed category specifications and [architecture-v2-overview.md](core/architecture-v2-overview.md) for system understanding.