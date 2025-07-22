# Context-Optimize - Intelligent Context Maintenance System

## 🎯 Purpose
Automated context directory maintenance ensuring semantic organization, content consolidation, density optimization, and structural integrity.

## 🚀 Usage
**Auto-Triggered**: After file operations, command executions, and periodic maintenance
**Manual**: Execute `/context-optimize [mode: consolidate|clean|optimize|full]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at context optimization initialization**:

```javascript
TodoWrite([
  {"content": "🔍 AUDIT: Scan context structure and identify issues", "status": "pending", "priority": "high", "id": "context-audit-1"},
  {"content": "📦 CONSOLIDATE: Merge redundant content and eliminate duplication", "status": "pending", "priority": "high", "id": "context-consolidate-1"},
  {"content": "🧹 OPTIMIZE: Improve content density and reduce to essentials", "status": "pending", "priority": "high", "id": "context-optimize-1"},
  {"content": "🏗️ STRUCTURE: Enforce semantic organization and fix violations", "status": "pending", "priority": "medium", "id": "context-structure-1"},
  {"content": "✅ VALIDATE: Confirm optimization results and system integrity", "status": "pending", "priority": "medium", "id": "context-validate-1"}
])
```

### Intelligent Context Management Framework

#### **Phase 1: Structural Assessment**
**Semantic Organization Validation**:
- **Directory Structure**: Verify `dev/`, `ops/`, `learn/`, `sys/`, `patterns/` organization
- **File Placement**: Ensure files are in correct semantic directories
- **Naming Compliance**: Validate semantic naming patterns (no timestamps)
- **Size Monitoring**: Identify files approaching 200-line limits

#### **Phase 2: Content Consolidation**
**Intelligent File Merging**:
- **Domain Analysis**: Group content by semantic domain (git, system, workflow)
- **Redundancy Detection**: Identify duplicate patterns and insights
- **Content Merging**: Consolidate related content into single files
- **Timestamp Integration**: Preserve chronological context with "Last Updated" tracking

#### **Phase 3: Density Optimization**
**Content Enhancement**:
- **Fluff Removal**: Eliminate verbose language and redundant explanations
- **Essential Extraction**: Preserve only actionable insights and proven patterns
- **Structure Optimization**: Improve organization for maximum information density
- **Cross-Reference**: Add intelligent linking between related concepts

#### **Phase 4: Maintenance Automation**
**Continuous Optimization**:
- **File Monitoring**: Watch for content growth and structural violations
- **Auto-Consolidation**: Trigger merging when redundancy detected
- **Quality Gates**: Prevent creation of low-value or duplicate content
- **Archive Management**: Move outdated content to archive/ automatically

### Context Optimization Modes

#### **Consolidate Mode** (`/context-optimize consolidate`)
**Focus**: Merge redundant files and eliminate duplication
**Triggers**: Multiple files covering same domain/topic
**Actions**: 
- Identify semantic overlap between files
- Merge related content into single comprehensive files
- Preserve all valuable insights while eliminating redundancy
- Update cross-references to point to consolidated files

#### **Clean Mode** (`/context-optimize clean`)
**Focus**: Remove outdated, empty, or low-value content
**Triggers**: File corruption, outdated information, or quality degradation
**Actions**:
- Detect and remove empty files
- Restore corrupted content from git history
- Archive content older than 6 months
- Eliminate timestamped files that escaped consolidation

#### **Optimize Mode** (`/context-optimize optimize`)
**Focus**: Improve content density and reduce to essentials
**Triggers**: Files approaching size limits or containing verbose content
**Actions**:
- Extract essential information and patterns
- Remove verbose language and redundant explanations
- Restructure for maximum information density
- Split oversized files intelligently by purpose

#### **Full Mode** (`/context-optimize full`)
**Complete Maintenance Cycle**: Consolidate → Clean → Optimize → Validate
**Triggers**: Periodic maintenance (weekly) or major system changes
**Actions**: Execute all optimization phases in sequence with validation

#### **Docs-Consolidate Mode** (`/context-optimize docs-consolidate`)
**Focus**: Merge redundant documentation and eliminate docs/ fragmentation
**Triggers**: After command creation or major documentation updates
**Actions**: 
- Identify overlapping documentation across docs/ subdirectories
- Merge related content into canonical documentation files
- Update cross-references to point to consolidated sources
- Maintain single source of truth principle

#### **Full-System Mode** (`/context-optimize full-system`)
**Complete System Maintenance**: Context + Docs comprehensive optimization
**Triggers**: After major system changes or new command integration
**Actions**: Execute context optimization + docs consolidation + cross-validation

### Auto-Integration Architecture

#### **Intelligent Trigger Framework**
**Proactive Activation System**:
- **Post-Command**: Auto-trigger after `/capture-learnings`, `/matrix-maintenance`
- **File Creation**: Monitor new file creation in context/ directory
- **Size Threshold**: Activate when files approach 180-line limit
- **Redundancy Detection**: Trigger when semantic overlap detected
- **Scheduled Maintenance**: Weekly comprehensive optimization

#### **Command Integration Protocols**
**Seamless Coordination Framework**:
```
🔄 CAPTURE-LEARNINGS: Complete → Context consolidation → Density optimization
📊 MATRIX-MAINTENANCE: Complete → Structure validation → Archive management
🎯 START: Session end → Auto-optimize context → Prepare for next session
📝 All Commands: Context modification → Incremental optimization → Quality maintenance
```

### Content Quality Framework

#### **Density Optimization Standards**
**Essential Content Criteria**:
- **Actionable Insights**: Information that directly improves workflows
- **Proven Patterns**: Validated approaches with evidence of success
- **Decision Frameworks**: Clear criteria for making choices
- **Cross-References**: Links between related concepts and dependencies

**Content Elimination Criteria**:
- **Verbose Explanations**: Replace with concise summaries
- **Redundant Examples**: Keep only most illustrative cases
- **Meta-Documentation**: Remove self-referential content
- **Outdated Information**: Archive superseded approaches

#### **Semantic Organization Enforcement**
**File Placement Rules**:
- **`dev/`**: Development insights, complexity analysis, research frameworks
- **`ops/`**: Operations workflows, monitoring, risk assessment, procedures
- **`learn/`**: Learning consolidation, user insights, pattern discovery
- **`sys/`**: System health, architecture integrity, maintenance reports
- **`patterns/`**: Validated patterns, reusable frameworks, best practices

### Notification Integration

#### **Optimization Progress Notifications**
```
🔍 AUDIT: Context structure analyzed → [X] semantic violations found
📦 CONSOLIDATE: [N] files merged → [domain] consolidation achieved
🧹 OPTIMIZE: Content density improved → [X]% size reduction achieved
🏗️ STRUCTURE: Semantic organization enforced → [violations] resolved
✅ VALIDATE: Optimization complete → [quality-score]/10 achieved
```

#### **Quality Improvement Tracking**
```
📊 METRICS: [old-count] → [new-count] files ([X]% reduction)
🎯 DENSITY: [old-lines] → [new-lines] total lines ([X]% optimization)
🔗 INTEGRATION: [broken-refs] fixed → [integrity]% reference health
⚡ PERFORMANCE: Optimization completed in [time] → [efficiency] achieved
```

## ⚡ Triggers

### Input Triggers
**Context**: Context directory modifications, file size growth, or redundancy detection
**Previous**: Auto-triggered by other commands or scheduled maintenance
**Keywords**: optimize, clean, consolidate, maintain, context

### Output Triggers
**When**: Optimization complete → Update system health metrics → Notify completion
**When**: Issues detected → Generate remediation plan → Execute corrections
**Chain**: context-optimize → matrix-maintenance → system validation → git commit

### Success Patterns
**Consolidation Success**: Redundant files merged → Single comprehensive files per domain
**Density Success**: Content optimized → Essential information preserved → Fluff eliminated
**Structure Success**: Semantic organization enforced → All files in correct directories

### Auto-Execution Framework
**POST-COMMAND OPTIMIZATION**: After commands that modify context files
**SCHEDULED MAINTENANCE**: Weekly comprehensive optimization cycles
**THRESHOLD-BASED**: When files approach size or redundancy limits

## 🔗 Module Integration

### Command Module Dependencies
**Core Integration**:
- `/matrix-maintenance` → Structure validation and integrity checking
- `/capture-learnings` → Content consolidation after learning capture

**Execution Chain**:
- **All Commands** → Context modification detection → Incremental optimization
- **Weekly Schedule** → Full optimization cycle → Quality improvement
- **File Operations** → Real-time monitoring → Proactive maintenance

### Success Patterns & Performance Metrics
**Consolidation Success**: Redundancy eliminated → Domain-based organization achieved
**Optimization Success**: Content density improved → Essential information preserved
**Integration Success**: Seamless automation → Zero user intervention required
**Quality Success**: Continuous improvement → System health maintained

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of intelligent context maintenance system

```javascript
// 1. STRUCTURAL ASSESSMENT (real execution)
LS("/Users/nalve/ce-simple/context") // Verify semantic directory structure
Bash("find context/ -name '*.md' | wc -l") // Current file count
Bash("find context/ -name '*2025*' -o -name '*timestamp*' | wc -l") // Detect timestamp violations

// 2. CONTENT ANALYSIS (real execution)
Grep("^# ", {glob: "context/**/*.md", output_mode: "content", -n: true}) // Extract file titles
Bash("find context/ -name '*.md' -exec wc -l {} + | sort -nr") // File size analysis
Grep("Last Updated:", {glob: "context/**/*.md", output_mode: "content"}) // Track update timestamps

// 3. EMPTY FILE DETECTION (real execution)
Bash("find context/ -name '*.md' -size 0") // Find empty files
Bash("find context/ -name '*.md' -exec sh -c 'test $(wc -l < \"$1\") -lt 10' _ {} \\; -print") // Find nearly empty files

// 4. REDUNDANCY ANALYSIS (real execution)
Grep("git workflow|Git Workflow", {glob: "context/**/*.md", output_mode: "files_with_matches"}) // Find domain overlap
Grep("system integrity|System Integrity", {glob: "context/**/*.md", output_mode: "files_with_matches"}) // Detect content duplication
Grep("complexity analysis|Complexity Analysis", {glob: "context/**/*.md", output_mode: "files_with_matches"}) // Identify consolidation opportunities

// 5. CONTENT CONSOLIDATION (real execution)
// For each domain with multiple files, consolidate into single semantic file
Edit("context/learn/git-insights.md", `# Git Workflow & Learning Insights
**Last Updated**: [current-timestamp]
**Scope**: Consolidated git workflow optimization and learning patterns

[Consolidated content from multiple git-related files]
`)

Edit("context/sys/system-health.md", `# System Health & Integrity
**Last Updated**: [current-timestamp]
**Scope**: Consolidated system integrity monitoring and health management

[Consolidated content from multiple system files]
`)

// 6. DENSITY OPTIMIZATION (real execution)
// Remove verbose content, preserve essential information
Grep("\\bvery\\b|\\breally\\b|\\bobviously\\b|\\bclearly\\b", {glob: "context/**/*.md", output_mode: "content"}) // Find verbose language
Edit("context/patterns/essential-patterns.md", `# Essential Problem-Solving Patterns
**Last Updated**: [current-timestamp]

[Optimized content with fluff removed, maximum density]
`)

// 7. STRUCTURE ENFORCEMENT (real execution)
Bash("find context/ -name '*.md' -path '*/wrong-dir/*' -exec mv {} context/correct-dir/ \\;") // Move misplaced files
Bash("find context/ -name '*-20[0-9][0-9]-*' -exec rm {} \\;") // Remove timestamp violations

// 8. DOCS MAINTENANCE (when docs-consolidate or full-system mode)
Bash("find docs/ -name '*.md' | wc -l") // Docs file count
Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "docs/**/*.md", output_mode: "content"}) // Find docs cross-references
Bash("find docs/ -name '*.md' -exec wc -l {} + | sort -nr | head -10") // Identify large docs files

// DOCS CONSOLIDATION LOGIC
Grep("# [Tt]itle|## [Tt]opic", {glob: "docs/**/*.md", output_mode: "content"}) // Identify topic overlap
Edit("docs/core/consolidated-standards.md", `# Consolidated System Standards
**Last Updated**: [current-timestamp]

[Consolidated content from overlapping docs files]
`)

// 9. VALIDATION & METRICS (real execution)
Bash("find context/ -name '*.md' | wc -l") // Final context count
Bash("find docs/ -name '*.md' | wc -l") // Final docs count
Bash("find . -name '*.md' -exec wc -l {} + | awk '{sum+=$1} END {print sum}'") // Total system lines
Grep("BROKEN|MISSING|ERROR", {glob: "{context,docs}/**/*.md", output_mode: "files_with_matches"}) // Quality check

// 10. COMMAND-CREATE INTEGRATION AUTO-TRIGGER
// Detect documentation gaps that might require new commands
Grep("TODO.*command|needed.*command|missing.*automation", {glob: "{context,docs}/**/*.md", output_mode: "files_with_matches"}) // Detect command needs in docs
Bash("if [[ $(find docs/ -name '*.md' -exec grep -l 'TODO.*automation\\|missing.*command' {} \\; | wc -l) -gt 0 ]]; then echo 'DOCUMENTATION-COMMAND-GAP-DETECTED'; fi") // Check docs for command gaps

// AUTO-TRIGGER: Command creation when documentation reveals automation needs
trigger_notification "context-optimize" "command-create" "documentation-gap-analysis"
Task("Command Development Opportunity", "Execute /command-create documentation-driven to identify command development opportunities from optimized documentation")

// 11. GIT INTEGRATION (real execution)
Bash("git add . && git commit -m \"context-optimize: [mode] | context: [ctx-files] docs: [doc-files] | density: [improvement]% | quality: [score]/10 ✓session-[N]\"")
```

### Optimization Algorithms

#### **Content Consolidation Logic**
```javascript
// Smart file merging based on semantic similarity
identifyDomainOverlap(files) {
  // Analyze file titles, content keywords, and semantic domains
  // Group files by domain (git, system, workflow, etc.)
  // Merge files with >70% content overlap
  // Preserve unique insights from each source
}

optimizeContentDensity(content) {
  // Remove filler words and verbose explanations
  // Extract actionable insights and proven patterns
  // Restructure for maximum information per line
  // Maintain readability while eliminating fluff
}
```

#### **Quality Assessment Framework**
```javascript
calculateQualityScore(contextDirectory) {
  // File organization score (semantic placement)
  // Content density score (information per line)
  // Reference integrity score (valid cross-links)
  // Update frequency score (recent maintenance)
  // Return composite quality score 1-10
}
```

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with optimization metrics
Bash("git add . && git commit -m \"context-optimize: [optimization-summary] | quality: [score]/10 ✓session-[N]\"")
```

---

**CRITICAL**: This command maintains the semantic context organization through intelligent automation, ensuring continuous optimization without user intervention while preserving all valuable content in maximum density format.

**EXECUTION COMMITMENT**: All optimization algorithms and maintenance operations are implemented with actual tool calls for real system improvement.