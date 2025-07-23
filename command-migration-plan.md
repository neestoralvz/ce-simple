# Command Migration Plan: Root Directory to 15-Category Taxonomy

**Generated**: 2025-07-23  
**Analysis**: 28 root-level commands mapped to 15-category taxonomy  
**Purpose**: Complete migration guide for category-based organization

## Executive Summary

**Current State**: 28 commands in root directory requiring migration to categories  
**Target State**: Commands properly distributed across 15 semantic categories  
**Migration Complexity**: 6 high-priority conflicts, 4 split recommendations, 2 merge opportunities

### Migration Statistics
- **Direct Mappings**: 18 commands (64%) with clear category assignments
- **Conflicts/Edge Cases**: 6 commands (21%) requiring manual review
- **Split Requirements**: 4 commands (14%) needing division across categories
- **Missing Categories**: 5 categories currently unpopulated

## Detailed Command Mappings

### 00-core: System Entry Points
**Population**: 2 additional commands (currently has 4)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `start.md` | Root → 00-core | **MIGRATE** | Primary entry point with orchestration logic |
| `enhanced-start.md` | Root → 00-core | **MIGRATE** | Advanced discovery entry point with Phase 0 assessment |

**Implementation**:
- Move both files to `commands/00-core/`
- Update CLAUDE.md references
- Validate orchestration trigger patterns

### 01-discovery: Information Gathering  
**Population**: 2 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `explore-codebase.md` | Root → 01-discovery | **MIGRATE** | Internal project analysis and investigation |
| `explore-web.md` | Root → 01-discovery | **MIGRATE** | External research and information gathering |

**Implementation**:
- Create complete discovery workflow chain
- Establish trigger relationships with 00-core
- Integrate with 13-search capabilities

### 02-planning: Strategic Design
**Population**: 1 command (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `agent-orchestration.md` | Root → 02-planning | **MIGRATE** | Master orchestrator for coordination strategy |

**Rationale**: Despite name suggesting execution, primary function is planning and strategy coordination, not direct agent management.

### 03-analysis: Deep Examination
**Population**: 4 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `think-layers.md` | Root → 03-analysis | **MIGRATE** | Progressive cognitive analysis (L1-L4 thinking) |
| `complexity-assess.md` | Root → 03-analysis | **MIGRATE** | Mathematical complexity calculation engine |
| `problem-solving.md` | Root → 03-analysis | **MIGRATE** | Universal systematic problem resolution |
| `analyze-parallel.md` | Root → 03-analysis | **MIGRATE** | Parallelization opportunity detection |

**Special Consideration**: `analyze-parallel-implementation.md` → **SPLIT RECOMMENDATION**
- Analysis portions → 03-analysis  
- Implementation recommendations → 04-execution

### 04-execution: Implementation Hub
**Population**: 2 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `agent-coordinate.md` | Root → 04-execution | **MIGRATE** | Agent coordination strategy implementation |
| `agent-deploy.md` | Root → 04-execution | **MIGRATE** | Pure agent deployment coordination |

**Additional Population**:
- Implementation portions from `analyze-parallel-implementation.md`
- Execution components from orchestration workflows

### 05-validation: Quality Assurance
**Population**: 0 additional commands (currently has 4 validation commands)

**Current Status**: Well-populated with validate-* commands
**Recommendation**: No root-level commands require migration to this category

### 06-documentation: Knowledge Management
**Population**: 2 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `capture-learnings.md` | Root → 06-documentation | **MIGRATE** | Learning capture and pattern documentation |
| `docs-maintain.md` | Root → 06-documentation | **MIGRATE** | Comprehensive documentation maintenance |

### 07-maintenance: System Upkeep
**Population**: 4 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `matrix-maintenance.md` | Root → 07-maintenance | **MIGRATE** | Cross-reference matrix maintenance |
| `context-optimize.md` | Root → 07-maintenance | **MIGRATE** | Context directory maintenance and optimization |
| `worktree-cleanup.md` | Root → 07-maintenance | **MIGRATE** | Git worktree maintenance and cleanup |
| `system-monitor.md` | Root → 07-maintenance | **MIGRATE** | System health monitoring and performance |

### 08-learning: Knowledge Evolution
**Population**: 0 commands (currently has 0)

**Status**: Currently unpopulated
**Recommendation**: Consider splitting `capture-learnings.md`
- Pattern capture → 06-documentation
- System evolution → 08-learning

### 09-git: Version Control Excellence
**Population**: 2 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `worktree-start.md` | Root → 09-git | **MIGRATE** | Session initialization with git worktree |
| `worktree-close.md` | Root → 09-git | **MIGRATE** | Session completion with merge decisions |

**Integration**: Forms complete git workflow with existing `worktree-cleanup.md`

### 10-standards: Governance Framework
**Population**: 0 commands (currently has 0)

**Status**: Currently unpopulated
**Opportunity**: Standards enforcement components from maintenance commands

### 11-meta: System Evolution
**Population**: 2 commands (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `command-create.md` | Root → 11-meta | **MIGRATE** | Systematic command development system |
| `command-maintain.md` | Root → 11-meta | **MIGRATE** | Automated command system maintenance |

### 12-math: Computational Excellence
**Population**: 1 command (currently has 0)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `load-balance.md` | Root → 12-math | **MIGRATE** | Resource distribution analysis and optimization |

**Additional Candidates**:
- Mathematical components from `complexity-assess.md` (if split)
- Performance calculation elements from monitoring commands

### 13-search: Information Discovery
**Population**: 0 commands (currently has 1 README)

**Status**: Currently minimal population
**Opportunity**: Search components from discovery and analysis commands

### 14-utils: Common Operations
**Population**: 3 commands (currently has 5)

| Command | Current Status | Migration Decision | Justification |
|---------|---------------|-------------------|---------------|
| `system-monitor-agents.md` | Root → 14-utils | **MIGRATE** | Agent health monitoring utilities |
| `performance-track.md` | Root → 14-utils | **MIGRATE** | Performance metrics collection utilities |
| `result-consolidate.md` | Root → 14-utils | **MIGRATE** | Result integration and reporting utilities |

## Conflict Analysis and Edge Cases

### HIGH-PRIORITY CONFLICTS

#### 1. `agent-orchestration.md` - Planning vs Execution
**Conflict**: Could belong to 02-planning or 04-execution
**Analysis**: Primary function is coordination strategy development
**Decision**: 02-planning (strategy coordination trumps execution management)
**Manual Review**: Recommended due to naming ambiguity

#### 2. `analyze-parallel-implementation.md` - Split Required
**Conflict**: Analysis vs Execution components in single command
**Decision**: **SPLIT COMMAND**
- Analysis portions → 03-analysis (`analyze-parallel.md`)
- Implementation → 04-execution (`parallel-implementation.md`)
**Justification**: Violates single responsibility principle

#### 3. `system-monitor.md` - Maintenance vs Utils
**Conflict**: Could belong to 07-maintenance or 14-utils
**Analysis**: Primary function is system health monitoring
**Decision**: 07-maintenance (system upkeep responsibility)
**Alternative**: Could be split between categories

#### 4. `context-optimize.md` - Maintenance vs Documentation
**Conflict**: Context maintenance vs documentation management
**Analysis**: Context directory is system infrastructure
**Decision**: 07-maintenance (system upkeep focus)

#### 5. `capture-learnings.md` - Documentation vs Learning
**Conflict**: Pattern documentation vs knowledge evolution
**Analysis**: Primary function is documentation creation
**Decision**: 06-documentation (documentation creation focus)
**Alternative**: Could enable 08-learning population

#### 6. `complexity-assess.md` - Analysis vs Math
**Conflict**: Analysis function vs mathematical computation
**Analysis**: Mathematical calculation engine supporting analysis
**Decision**: 03-analysis (analysis context trumps computation method)
**Alternative**: Mathematical components could populate 12-math

### MEDIUM-PRIORITY EDGE CASES

#### 1. `git-worktree.md` vs Worktree Commands
**Status**: Command appears missing from analysis
**Action Required**: Verify if `git-worktree.md` exists and analyze

#### 2. Load Balancing Classification
**Current**: 12-math assignment
**Alternative**: Could belong to 04-execution or 07-maintenance
**Justification**: Resource optimization is mathematical analysis

#### 3. Result Consolidation Utility
**Current**: 14-utils assignment
**Alternative**: Could belong to 06-documentation
**Justification**: Result integration is utility function, not documentation creation

## Missing Category Opportunities

### Categories Requiring Population

#### 08-learning: Knowledge Evolution
**Current**: Empty
**Opportunities**:
- Learning evolution components from `capture-learnings.md`
- System adaptation patterns from maintenance commands
- Meta-learning elements from orchestration commands

#### 10-standards: Governance Framework
**Current**: Empty  
**Opportunities**:
- Standards enforcement from `command-maintain.md`
- Compliance components from monitoring commands
- Quality governance from validation workflows

#### 13-search: Information Discovery
**Current**: Minimal (README only)
**Opportunities**:
- Search components from `explore-web.md`
- Information retrieval from discovery commands
- Content indexing from documentation maintenance

## Implementation Strategy

### Phase 1: Direct Migrations (18 commands)
**Priority**: High
**Risk**: Low
**Actions**:
1. Move commands with clear category assignments
2. Update CLAUDE.md references
3. Validate cross-command triggers

### Phase 2: Conflict Resolution (6 commands)
**Priority**: High  
**Risk**: Medium
**Actions**:
1. Manual review of conflicted assignments
2. Split commands where single responsibility violated
3. Create implementation files for extracted components

### Phase 3: Category Population (5 categories)
**Priority**: Medium
**Risk**: Low  
**Actions**:
1. Create commands for empty categories
2. Extract components from existing commands
3. Establish category-specific workflows

### Phase 4: Integration Testing
**Priority**: High
**Risk**: Medium
**Actions**:
1. Validate all cross-category triggers
2. Test workflow chains post-migration
3. Update documentation and references

## Validation Checklist

### Pre-Migration Validation
- [ ] All 28 root commands analyzed
- [ ] Category assignments justified
- [ ] Conflict resolution strategies defined
- [ ] Split/merge requirements documented

### Post-Migration Validation  
- [ ] All commands successfully migrated
- [ ] CLAUDE.md updated with new structure
- [ ] Cross-references validated and updated
- [ ] Workflow triggers tested and functional
- [ ] Documentation consistency verified

### Success Metrics
- **Migration Completeness**: 100% of root commands migrated
- **Category Population**: 10+ categories populated (target: 12+)
- **Workflow Integrity**: 95%+ of triggers functional post-migration
- **Documentation Accuracy**: 100% of references updated

---

**Migration Readiness**: HIGH - Clear assignments for 64% of commands, defined resolution for conflicts
**Implementation Risk**: MEDIUM - 6 conflicts require manual review, 4 splits needed
**Expected Outcome**: Well-organized 15-category system with improved discoverability and maintainability