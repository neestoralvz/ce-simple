# Docs Optimize - CLAUDE.md and Standards Compliance Optimization

## 🎯 Purpose
Optimize CLAUDE.md according to official Anthropic standards, maintain date accuracy for temporal context, and ensure comprehensive compliance across documentation system.

## 🚀 Usage
Execute: `/docs-optimize [target]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at optimization initialization**:

```javascript
TodoWrite([
  {"content": "📄 CLAUDE_MD: Analyze CLAUDE.md against official Anthropic standards", "status": "pending", "priority": "high", "id": "optimize-claude-1"},
  {"content": "📅 DATES: Verify and update 'Last Updated: YYYY-MM-DD' temporal accuracy", "status": "pending", "priority": "high", "id": "optimize-dates-1"},
  {"content": "📏 COMPLIANCE: Execute system-wide standards compliance validation", "status": "pending", "priority": "high", "id": "optimize-compliance-1"},
  {"content": "⚡ TOKENS: Optimize token efficiency with content density enhancement", "status": "pending", "priority": "medium", "id": "optimize-tokens-1"},
  {"content": "🔗 INTEGRATION: Validate Claude Code workflow integration compatibility", "status": "pending", "priority": "medium", "id": "optimize-integration-1"}
])
```

**Standards-Driven Todos**: Add specific compliance todos based on violations discovered during standards analysis

### Optimization Protocol
1. **CLAUDE.MD ANALYSIS**: Evaluate against official Anthropic standards and token efficiency
2. **DATE MAINTENANCE**: Verify and update "Last Updated: YYYY-MM-DD" for temporal context accuracy
3. **STANDARDS COMPLIANCE**: Validate system-wide adherence to established policies
4. **TOKEN OPTIMIZATION**: Reduce cognitive load while maintaining information completeness
5. **STRUCTURE REFINEMENT**: Implement progressive disclosure and navigation optimization
6. **INTEGRATION VALIDATION**: Ensure compatibility with Claude Code workflows

### CLAUDE.md Optimization Framework
**Standards Compliance**: File hierarchy + content sections + import system + token efficiency validation

**Date Maintenance**: "Last Updated: YYYY-MM-DD" verification and temporal context accuracy

**Structure Analysis**: Line count + header assessment + reference density optimization

**Progressive Disclosure**: Extract complex details to referenced files while maintaining core functionality

### System-Wide Standards Compliance
**File Size Policy**: Commands ≤140 lines (optimal), ≤200 lines (maximum) with progressive disclosure for violations

**Cross-Reference Optimization**: ≤20 essential references with hub-based navigation and bidirectional flow

**Quality Assurance**: Authority clarification + link validation + navigation efficiency

### Token Efficiency Optimization
**Content Density**: Redundancy elimination + concept consolidation + essential focus prioritization

**Claude Code Integration**: Memory management + command integration + session efficiency optimization

### Quality Assurance Validation
**Success Metrics**: 30% content reduction + ≤2.5 cognitive steps + 100% compliance + seamless integration

**Systematic Verification**: CLAUDE.md standards compliance + date maintenance + size compliance + reference optimization + token efficiency + Claude Code integration

## ⚡ Triggers

### Input Triggers
**Context**: Post-consolidation system requiring standards optimization
**Previous**: `/docs-consolidate` → content unified, optimization needed
**Keywords**: optimize, CLAUDE.md, standards, compliance, token, efficiency

### Output Triggers
**When**: Optimization complete → `/docs-validate` for comprehensive verification
**When**: Complete workflow → `/docs-workflow` for automated full optimization
**When**: Complex issues discovered → `/docs-consolidate` for additional unification
**Chain**: audit → consolidate → optimize → validate (granular) OR audit → workflow (complete)

### Success Patterns
**CLAUDE.md Success**: Anthropic compliance achieved → Enhanced Claude Code integration
**Standards Success**: 100% system compliance → Automated validation enabled
**Efficiency Success**: Token optimization achieved → Improved operational performance

## 🔗 See Also

### Implementation Details
- `../docs/quality/docs-optimize-compliance.md` - Complete standards compliance and token efficiency protocols

### Related Commands
- Execute `/docs-workflow` for complete automated documentation optimization workflow
- Execute `/docs-audit` for comprehensive system analysis before optimization
- Execute `/docs-consolidate` for content unification prior to optimization
- Execute `/docs-validate` for post-optimization system verification

### Integration References
- `context/research/anthropic-claude-md-standards.md` - Official optimization criteria
- `../docs/documentation/writing-standards.md` - System compliance requirements
- `../docs/documentation/simplicity-principles.md` - Optimization implementation guidelines
- `context/discoveries/documentation-workflow-discoveries.md` - Optimization methodology

---

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of CLAUDE.md and standards compliance optimization

```javascript
// COMPREHENSIVE DOCUMENTATION OPTIMIZATION SYSTEM
// Execute CLAUDE.md and system-wide standards compliance

// 1. CLAUDE.MD ANALYSIS AND OPTIMIZATION
// Comprehensive CLAUDE.md evaluation against Anthropic standards

Read("CLAUDE.md")                                              // Current CLAUDE.md analysis
Bash("wc -l CLAUDE.md")                                        // Current line count
Bash("wc -w CLAUDE.md")                                        // Current word count for token estimation

// CLAUDE.md structure validation
Grep("# CLAUDE.md|## [A-Z]|###|####", {path: "CLAUDE.md", output_mode: "content", -n: true}) // Header structure
Grep("Last Updated:|YYYY-MM-DD", {path: "CLAUDE.md", output_mode: "content"})              // Date maintenance
Grep("commands|slash|/[a-zA-Z-]+", {path: "CLAUDE.md", output_mode: "content", -C: 1})      // Command references

// 2. DATE MAINTENANCE AND TEMPORAL CONTEXT
// Verify and update "Last Updated: YYYY-MM-DD" accuracy

Bash("date '+%Y-%m-%d'")                                       // Current date for updates
Grep("Last Updated:|Updated:", {glob: "**/*.md", output_mode: "content", -n: true})         // All date references

// Date consistency validation
Write("context/discoveries/date-maintenance-[timestamp].md", `# Date Maintenance Analysis

## Current Date References
[All files with date stamps]

## Update Requirements
- CLAUDE.md Last Updated: [current_date]
- Files requiring date updates: [outdated_files]
- Temporal context accuracy: [accuracy_status]

## Date Update Plan
[Specific date corrections needed]
`)

// 3. SYSTEM-WIDE STANDARDS COMPLIANCE
// Comprehensive standards validation across all documentation

// File size compliance analysis
Bash("find . -name '*.md' -path './.claude/commands/*' -exec awk 'END{if(NR>140) print FILENAME \" optimal exceeded: \" NR}' {} +") // Command size
Bash("find . -name '*.md' -exec awk 'END{if(NR>200) print FILENAME \" maximum exceeded: \" NR}' {} +")                      // All files max

// Cross-reference density analysis
Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "**/*.md", output_mode: "count"})            // Count all references
Bash("find . -name '*.md' | wc -l")                                         // Total files for ratio
Bash("echo 'scale=1; [total_references] / [total_files]' | bc")             // References per file ratio

// 4. TOKEN EFFICIENCY OPTIMIZATION
// Content density enhancement and redundancy elimination

Grep("MANDATORY|CRITICAL|Execute:|Purpose:", {glob: "**/*.md", output_mode: "count"})      // Common phrases count
Grep("## Purpose|## Usage|## Implementation", {glob: "**/*.md", output_mode: "count"})     // Section repetition
Grep("behavioral reinforcement|TodoWrite", {glob: "**/*.md", output_mode: "count"})        // Framework repetition

// Content optimization analysis
Write("context/discoveries/token-optimization-[timestamp].md", `# Token Efficiency Analysis

## Current Token Metrics
- CLAUDE.md Word Count: [claude_words] words
- System Average File Size: [avg_file_size] lines
- Reference Density: [ref_density] refs/file
- Common Phrase Repetition: [repetition_score]%

## Optimization Opportunities
- Redundancy Elimination: [redundancy_potential]%
- Progressive Disclosure: [disclosure_candidates] files
- Content Consolidation: [consolidation_opportunities]

## Token Efficiency Targets
- CLAUDE.md Reduction: [target_reduction]%
- System-wide Optimization: [system_optimization]%
- Navigation Efficiency: ≤2.5 cognitive steps
`)

// 5. PROGRESSIVE DISCLOSURE APPLICATION
// Extract verbose content while maintaining functionality

Grep("EXECUTION LAYER|implementation details|complete framework", {glob: "**/*.md", output_mode: "files_with_matches"}) // Verbose sections
Bash("find . -name '*.md' -exec grep -l 'detailed.*implementation\\|comprehensive.*framework' {} +")                      // Extraction candidates

// 6. CLAUDE CODE INTEGRATION VALIDATION
// Ensure compatibility with Claude Code workflows

Grep("claude code|Claude Code|memory|session|context", {glob: "**/*.md", output_mode: "content"})  // Integration references
Grep("tool calls|tool operations|execution layer", {glob: "**/*.md", output_mode: "content"})      // Implementation patterns

// Claude Code compatibility assessment
Write("context/discoveries/claude-code-integration-[timestamp].md", `# Claude Code Integration Assessment

## Current Integration Status
- Memory Management References: [memory_refs]
- Tool Implementation Coverage: [tool_coverage]%
- Session Context Handling: [context_handling]
- Workflow Compatibility: [workflow_compatibility]%

## Integration Optimization
- Memory Efficiency Improvements: [memory_improvements]
- Context Management Enhancement: [context_enhancements]
- Tool Call Optimization: [tool_optimizations]

## Compatibility Validation
[Claude Code workflow integration verification]
`)

// 7. OPTIMIZATION RESULTS AND METRICS
// Document comprehensive optimization outcomes

Write("context/discoveries/optimization-results-[timestamp].md", `# Documentation Optimization Results

## CLAUDE.md Optimization
- Original Size: [original_lines] lines, [original_words] words
- Optimized Size: [optimized_lines] lines, [optimized_words] words
- Reduction Achieved: [reduction_percentage]%
- Date Updated: [current_date]
- Standards Compliance: [compliance_status]

## System-wide Standards Compliance
- Files Within Size Limits: [compliant_files]/[total_files]
- Reference Density Optimized: [ref_density_optimized]
- Token Efficiency Gain: [efficiency_gain]%
- Progressive Disclosure Applied: [disclosure_files] files

## Quality Metrics Post-Optimization
- Navigation Efficiency: [navigation_score] cognitive steps
- Content Density: [content_density]%
- Standards Adherence: [standards_percentage]%
- Claude Code Compatibility: [compatibility_score]%

## Optimization Success Criteria
- 30% Content Reduction: [ACHIEVED/NOT_ACHIEVED]
- ≤2.5 Cognitive Steps: [ACHIEVED/NOT_ACHIEVED]
- 100% Compliance: [ACHIEVED/NOT_ACHIEVED]
- Seamless Integration: [ACHIEVED/NOT_ACHIEVED]
`)

// 8. VALIDATION AND SUCCESS METRICS
Bash("echo 'scale=1; ([optimized_size] * 100) / [original_size]' | bc")     // Size reduction percentage
Bash("echo 'scale=1; ([compliant_files] * 100) / [total_files]' | bc")     // Compliance percentage
Bash("echo 'Optimization complete: [reduction]% size reduction achieved'")
```

### CLAUDE.md Optimization Framework
**ANTHROPIC STANDARDS COMPLIANCE**:
- File hierarchy validation and content section optimization
- Import system efficiency and token optimization
- Date maintenance accuracy for temporal context
- Progressive disclosure for content density

### Token Efficiency Strategy
**OPTIMIZATION TECHNIQUES**:
- Redundancy elimination across repetitive sections
- Concept consolidation and essential focus prioritization
- Progressive disclosure for verbose implementation details
- Navigation optimization for cognitive efficiency

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with optimization metrics
Bash("git add . && git commit -m \"docs-optimize: size [before]→[after] | compliance: [N]% ✓session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **CLAUDE.md analysis**: 1 Read + 2 Bash + 3 Grep operations
- **Date maintenance**: 1 Bash + 1 Grep + 1 Write operations
- **Standards validation**: 3 Bash + 1 Grep operations
- **Token optimization**: 3 Grep + 1 Write operations
- **Progressive disclosure**: 2 Grep + 1 Bash operations
- **Integration validation**: 2 Grep + 1 Write operations
- **Results documentation**: 1 Write operation
- **Success metrics**: 3 Bash operations
- **Ratio**: 22 tool calls to ~95 documentation lines = 23% (HEALTHY)

---

**CRITICAL**: This command ensures maximum system effectiveness through standards compliance and token optimization while maintaining complete functional integrity and Claude Code compatibility.

**EXECUTION COMMITMENT**: CLAUDE.md optimization, date maintenance, standards compliance, and token efficiency are NOW implemented with actual tool calls.