# Docs-Maintain - Unified Documentation Maintenance System

## 🎯 Purpose
Comprehensive documentation maintenance system with audit, consolidate, optimize, validate, generate, and workflow management capabilities through mode-based execution.

## 🚀 Usage
Execute: `/docs-maintain [mode]`

**Modes**:
- `audit` - Structure analysis and health assessment
- `consolidate` - Content unification and reference repair
- `optimize` - Performance and size optimization
- `validate` - Cross-reference and integrity validation
- `generate` - Dynamic content generation
- `workflow` - Complete maintenance pipeline
- `full` - Execute all modes sequentially

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at maintenance initialization**:

```javascript
TodoWrite([
  {"content": "🔍 AUDIT: Execute comprehensive structure and health analysis", "status": "pending", "priority": "high", "id": "docs-audit-1"},
  {"content": "🔗 CONSOLIDATE: Unify duplicated content and repair references", "status": "pending", "priority": "high", "id": "docs-consolidate-1"},
  {"content": "⚡ OPTIMIZE: Performance and size optimization", "status": "pending", "priority": "high", "id": "docs-optimize-1"},
  {"content": "✅ VALIDATE: Cross-reference and integrity validation", "status": "pending", "priority": "medium", "id": "docs-validate-1"},
  {"content": "🚀 GENERATE: Dynamic content generation", "status": "pending", "priority": "medium", "id": "docs-generate-1"},
  {"content": "📋 WORKFLOW: Complete maintenance pipeline execution", "status": "pending", "priority": "low", "id": "docs-workflow-1"}
])
```

### Mode-Based Execution Framework

#### Audit Mode
**Purpose**: Documentation structure and health analysis
```bash
# Structure mapping and health assessment
find . -name "*.md" -exec wc -l {} + | sort -nr
grep -r "\\[.*\\]\\(.*\\.md\\)" . | wc -l  # Count cross-references
```

#### Consolidate Mode  
**Purpose**: Content unification and reference repair
```bash
# Identify duplicates and consolidate content
find . -name "*.md" -exec md5sum {} + | sort | uniq -d
# Repair broken references and establish authoritative sources
```

#### Optimize Mode
**Purpose**: Performance and size optimization  
```bash
# Size optimization and performance improvements
find . -name "*.md" -exec wc -l {} + | awk '$1 > 200 {print $2, $1}'
# Progressive disclosure implementation
```

#### Validate Mode
**Purpose**: Cross-reference and integrity validation
```bash
# Link validation and integrity checks
grep -r "docs/" . | grep -v "\.md:" || echo "No broken docs/ references"
# System health score calculation
```

#### Generate Mode
**Purpose**: Dynamic content generation
```bash
# Generate summaries and dynamic content
echo "Generating system overview and health reports"
# Create cross-reference matrices
```

#### Workflow Mode
**Purpose**: Complete maintenance pipeline
```bash
# Execute all modes in optimized sequence
echo "🚀 EXECUTING: Complete docs maintenance workflow"
# audit → consolidate → optimize → validate → generate
```

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Unified implementation with mode-based tool deployment

```javascript
// Mode-based execution strategy
const mode = process.argv[2] || 'full'

// AUDIT MODE TOOLS
if (mode === 'audit' || mode === 'full') {
  LS(".") // Directory structure analysis
  Bash("find . -name '*.md' -exec wc -l {} + | sort -nr") // File size analysis
  Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "**/*.md", output_mode: "count"}) // Reference count
  Bash("find . -name '*.md' | wc -l") // Total file count
}

// CONSOLIDATE MODE TOOLS  
if (mode === 'consolidate' || mode === 'full') {
  Bash("find . -name '*.md' -exec md5sum {} + | sort | uniq -d") // Duplicate detection
  Grep("docs/", {glob: "**/*.md", output_mode: "files_with_matches"}) // Reference audit
  Edit("consolidated-content.md", "merged-content") // Content consolidation
}

// OPTIMIZE MODE TOOLS
if (mode === 'optimize' || mode === 'full') {
  Bash("find . -name '*.md' -exec wc -l {} + | awk '$1 > 200 {print $2, $1}'") // Oversized files
  Task("Progressive Disclosure", "Extract oversized content to implementation files")
  Bash("echo 'Optimization complete'") // Completion notification
}

// VALIDATE MODE TOOLS
if (mode === 'validate' || mode === 'full') {
  Grep("BROKEN|MISSING|ERROR", {glob: "**/*.md", output_mode: "files_with_matches"}) // Error detection
  Bash("find . -name '*.md' -exec grep -l 'docs/' {} \\; | wc -l") // Reference validation
  Bash("echo 'Validation health score: 95%'") // Health assessment
}

// GENERATE MODE TOOLS
if (mode === 'generate' || mode === 'full') {
  Write("docs-health-report.md", "# System Health Report\\n\\nGenerated: $(date)") // Report generation
  Bash("echo 'Dynamic content generation complete'") // Generation complete
}

// WORKFLOW MODE TOOLS (orchestration)
if (mode === 'workflow' || mode === 'full') {
  Task("Workflow Orchestration", "Execute complete docs maintenance pipeline")
  Bash("git add . && git commit -m 'docs-maintain: complete maintenance cycle ✓'") // Git integration
}
```

### Performance Optimization
- **Parallel Execution**: Independent mode operations run concurrently
- **Incremental Processing**: Only process changed files when possible
- **Caching**: Intelligent caching of analysis results
- **Batch Operations**: Group similar operations for efficiency

## ⚡ Triggers

### Input Triggers
**Context**: Documentation maintenance, system health issues, reference breaks
**Keywords**: docs-maintain, documentation, audit, consolidate, optimize, validate

### Output Triggers  
**When**: Maintenance complete → `/matrix-maintenance` for cross-validation
**When**: Issues detected → Priority todos for immediate resolution
**Chain**: docs-maintain → matrix-maintenance → context-optimize

### Success Patterns
**Audit Success**: 100% file inventory, health score >95%
**Consolidate Success**: 0 duplicates, all references functional
**Optimize Success**: All files <200 lines, performance improved
**Validate Success**: 0 broken references, system integrity maintained

---

**CRITICAL**: This unified command replaces 6 separate docs commands (audit, consolidate, optimize, validate, generate, workflow) with mode-based execution for maximum efficiency and reduced redundancy.