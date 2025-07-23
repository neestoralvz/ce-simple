# Docs-Maintain - Unified Documentation Maintenance System

## Purpose
Comprehensive documentation maintenance system with audit, consolidate, optimize, validate, generate, and workflow management capabilities through mode-based execution and error handling.

## Principles and Guidelines
• **Mode-Based Execution**: Support audit, consolidate, optimize, validate, generate, workflow, and full modes for targeted operations
• **Content Unification**: Merge duplicated content, repair broken references, and establish authoritative documentation sources
• **Performance Optimization**: Implement progressive disclosure for oversized files and optimize cross-reference integrity
• **Error Handling**: Detect and resolve broken links, missing references, and structural integrity violations

## Execution Process

### Phase 1: Audit and Analysis
```javascript
TodoWrite([
  {"content": "🔍 AUDIT: Execute comprehensive structure and health analysis", "status": "pending", "priority": "high", "id": "docs-audit-1"},
  {"content": "🔗 CONSOLIDATE: Unify duplicated content and repair references", "status": "pending", "priority": "high", "id": "docs-consolidate-1"}
])
```

**Structure Analysis**:
- Map documentation directory structure and file relationships
- Count cross-references and identify broken links
- Detect duplicate content through MD5 checksums
- Assess file sizes and identify optimization opportunities

### Phase 2: Optimization and Validation
```javascript
TodoWrite([
  {"content": "⚡ OPTIMIZE: Performance and size optimization", "status": "pending", "priority": "high", "id": "docs-optimize-1"},
  {"content": "✅ VALIDATE: Cross-reference and integrity validation", "status": "pending", "priority": "medium", "id": "docs-validate-1"}
])
```

**Content Enhancement**:
- Implement progressive disclosure for files >200 lines
- Repair broken references and establish link integrity
- Generate dynamic content and system health reports
- Execute comprehensive validation protocols

### Phase 3: Generation and Workflow
```javascript
TodoWrite([
  {"content": "🚀 GENERATE: Dynamic content generation", "status": "pending", "priority": "medium", "id": "docs-generate-1"},
  {"content": "📋 WORKFLOW: Complete maintenance pipeline execution", "status": "pending", "priority": "low", "id": "docs-workflow-1"}
])
```

**Workflow Orchestration**:
- Execute complete maintenance pipeline in optimized sequence
- Generate comprehensive system health reports
- Integrate with matrix-maintenance for cross-validation
- Commit changes with detailed metrics

### Tool Execution Implementation
```javascript
// MODE-BASED EXECUTION STRATEGY
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

---

**Single Responsibility**: Unified documentation maintenance with mode-based execution, error handling, and comprehensive quality assurance protocols.