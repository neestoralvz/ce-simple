# Context-Optimize - Intelligent Context Maintenance System

## Purpose
Automated context directory maintenance ensuring semantic organization, content consolidation, density optimization, and structural integrity through intelligent analysis and systematic optimization.

## Principles and Guidelines
• **Semantic Organization**: Maintain `dev/`, `ops/`, `learn/`, `sys/`, `patterns/` directory structure with proper file placement
• **Content Consolidation**: Merge redundant files with >70% overlap while preserving unique insights and proven patterns  
• **Density Optimization**: Remove verbose language, extract actionable insights, maximize information per line ratio
• **Structural Integrity**: Enforce 200-line limits, eliminate timestamp violations, maintain cross-reference health

## Execution Process

### Phase 1: Structural Assessment
```javascript
TodoWrite([
  {"content": "🔍 AUDIT: Scan context structure and identify semantic violations", "status": "pending", "priority": "high", "id": "context-audit-1"},
  {"content": "📦 CONSOLIDATE: Merge redundant content and eliminate duplication", "status": "pending", "priority": "high", "id": "context-consolidate-1"}
])
```

**Directory Structure Validation**:
- Verify semantic organization compliance
- Identify misplaced files requiring relocation  
- Detect timestamp violations in naming patterns
- Monitor files approaching 200-line limits

### Phase 2: Content Analysis and Consolidation
**Intelligent File Merging**:
- Group content by semantic domain (git, system, workflow)
- Detect redundancy patterns and duplicate insights
- Consolidate related content into comprehensive files
- Preserve chronological context with "Last Updated" tracking

### Phase 3: Optimization and Validation
```javascript
TodoWrite([
  {"content": "🧹 OPTIMIZE: Improve content density and reduce to essentials", "status": "pending", "priority": "high", "id": "context-optimize-1"},
  {"content": "✅ VALIDATE: Confirm optimization results and system integrity", "status": "pending", "priority": "medium", "id": "context-validate-1"}
])
```

**Content Enhancement**:
- Remove verbose explanations and redundant text
- Extract essential patterns and actionable insights  
- Improve organization for maximum information density
- Add intelligent cross-references between concepts
- Execute quality validation and integrity checks

### Tool Execution Implementation
```javascript
// STRUCTURAL ASSESSMENT
LS("/Users/nalve/ce-simple/context") // Verify semantic directory structure
Bash("find context/ -name '*.md' | wc -l") // Current file count
Bash("find context/ -name '*2025*' -o -name '*timestamp*' | wc -l") // Detect violations

// CONTENT ANALYSIS
Grep("^# ", {glob: "context/**/*.md", output_mode: "content", -n: true}) // Extract titles
Bash("find context/ -name '*.md' -exec wc -l {} + | sort -nr") // Size analysis
Grep("Last Updated:", {glob: "context/**/*.md", output_mode: "content"}) // Track updates

// REDUNDANCY DETECTION
Grep("git workflow|Git Workflow", {glob: "context/**/*.md", output_mode: "files_with_matches"})
Grep("system integrity|System Integrity", {glob: "context/**/*.md", output_mode: "files_with_matches"})

// CONTENT CONSOLIDATION
Edit("context/learn/git-insights.md", `# Git Workflow & Learning Insights\n**Last Updated**: [timestamp]\n\n[Consolidated content]`)
Edit("context/sys/system-health.md", `# System Health & Integrity\n**Last Updated**: [timestamp]\n\n[Consolidated content]`)

// DENSITY OPTIMIZATION
Grep("\\bvery\\b|\\breally\\b|\\bobviously\\b", {glob: "context/**/*.md", output_mode: "content"})
Edit("context/patterns/essential-patterns.md", `# Essential Problem-Solving Patterns\n[Optimized content]`)

// STRUCTURE ENFORCEMENT
Bash("find context/ -name '*.md' -path '*/wrong-dir/*' -exec mv {} context/correct-dir/ \\;")
Bash("find context/ -name '*-20[0-9][0-9]-*' -exec rm {} \\;")

// VALIDATION & METRICS
Bash("find context/ -name '*.md' | wc -l") // Final count
Grep("BROKEN|MISSING|ERROR", {glob: "{context,docs}/**/*.md", output_mode: "files_with_matches"})

// GIT INTEGRATION
Bash("git add . && git commit -m \"context-optimize: [mode] | quality: [score]/10 ✓session\"")
```

---

**Single Responsibility**: Context directory maintenance through semantic organization, content consolidation, and density optimization with automated quality assurance.