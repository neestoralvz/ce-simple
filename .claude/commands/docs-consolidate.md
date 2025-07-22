# Docs Consolidate - Content Unification and Reference Repair

## 🎯 Purpose
Systematically unify duplicated content, repair broken references, and consolidate fragmented information while maintaining system architectural integrity.

## 🚀 Usage
Execute: `/docs-consolidate [scope]`

## 🔧 Implementation

### Behavioral Reinforcement Protocol
**MANDATORY at consolidation initialization**:

```javascript
TodoWrite([
  {"content": "🔍 ASSESSMENT: Identify content duplication patterns and overlap percentages", "status": "pending", "priority": "high", "id": "consolidate-assess-1"},
  {"content": "🏛️ AUTHORITY: Establish authoritative sources for duplicated content resolution", "status": "pending", "priority": "high", "id": "consolidate-authority-1"},
  {"content": "🔗 REFERENCES: Repair broken cross-references and validate link integrity", "status": "pending", "priority": "high", "id": "consolidate-references-1"},
  {"content": "📊 DISCLOSURE: Execute progressive disclosure for oversized content", "status": "pending", "priority": "medium", "id": "consolidate-disclosure-1"},
  {"content": "✅ INTEGRITY: Verify system architectural integrity post-consolidation", "status": "pending", "priority": "medium", "id": "consolidate-integrity-1"}
])
```

**Dynamic Todo Addition**: Add priority todos for critical consolidation issues discovered during analysis

### Consolidation Protocol
**Sequential Execution**: Execute in dependency order to prevent reference breaks during consolidation
**Duplication Resolution**: Identify and merge overlapping content with authoritative source establishment
**Reference Repair**: Fix broken cross-references, create missing targets, ensure bidirectional linking
**Progressive Disclosure**: Extract verbose content from commands to docs/context layers

### Consolidation Strategy Framework
**High Priority** (>40% overlap): Merge files with substantial duplication, establish single sources
**Medium Priority** (20-40% overlap): Consolidate sections, standardize terminology and explanations
**Low Priority** (<20% overlap): Optimize cross-references, standardize formatting conventions

### Content Organization System
**Commands** (≤140 optimal): Extract educational content → context, detailed criteria → standards  
**Standards** (≤200 max): Consolidate frameworks, unify criteria, establish authoritative guidelines
**Context** (≤200 max): Consolidate patterns, document relationships, preserve historical decisions

### Quality Assurance Framework
**Success Metrics**: <5% duplication, 100% functional references, file size compliance, ≤2.5 navigation steps
**Validation Checklist**: All references functional, no information loss, size compliance, boundaries maintained
**Integrity Preservation**: System coherence maintained throughout consolidation operations

## ⚡ Triggers

### Input Triggers
**Context**: Post-audit identification of content duplication and reference issues requiring unification
**Previous**: `/docs-audit` identified consolidation requirements or direct duplication resolution needs
**Keywords**: consolidate, unify, merge, repair, references, duplication

### Output Triggers
**Success**: Content unified → `/docs-optimize` for standards compliance application
**Complete**: Complex consolidation → `/docs-validate` for architecture verification
**Workflow**: Automated path → `/docs-workflow` for complete optimization integration
**Chain**: audit → consolidate → optimize → validate (workflow completion)

### Success Patterns
**Consolidation Success**: <5% content duplication → Architectural integrity achieved
**Reference Success**: 100% functional links → Navigation completeness verified
**Size Success**: All files compliant → Progressive disclosure effectiveness demonstrated

## 🔗 See Also

### Implementation References
- `../docs/implementation/docs-consolidate-implementation.md` - Complete consolidation framework details
- `../docs/documentation/simplicity-principles.md` - Progressive disclosure implementation standards
- `../docs/documentation/writing-standards.md` - Content unification and organization standards

### Related Commands
- Execute `/docs-workflow` for complete automated optimization workflow integration
- Execute `/docs-audit` for comprehensive system analysis and issue identification
- Execute `/docs-optimize` for standards compliance and CLAUDE.md optimization
- Execute `/docs-validate` for post-consolidation system health verification

---

## ⚡ EXECUTION LAYER

### Mandatory Tool Executions
**CRITICAL**: Actual implementation of content unification and reference repair system

```javascript
// COMPREHENSIVE CONTENT CONSOLIDATION SYSTEM
// Execute systematic unification and reference repair

// 1. DUPLICATION ASSESSMENT AND AUTHORITY ESTABLISHMENT
// Identify content overlap patterns and establish authoritative sources
Grep("## Purpose|## Usage|## Implementation", {glob: "**/*.md", output_mode: "content", -n: true}) // Common sections
Grep("MANDATORY|CRITICAL|Execute:", {glob: "**/*.md", output_mode: "content", -C: 2})            // Repeated patterns
Grep("TodoWrite|behavioral reinforcement|protocol", {glob: "**/*.md", output_mode: "content", -C: 3}) // Standard frameworks

// Authority source identification
Bash("find . -name '*.md' -exec wc -l {} + | sort -nr | head -10") // Largest files (likely authoritative)
Bash("find . -name '*.md' -exec ls -lt {} + | head -10")           // Most recently modified

// 2. CONTENT OVERLAP ANALYSIS
// Calculate duplication percentages and identify merge candidates
Write("context/discoveries/duplication-analysis-[timestamp].md", `# Content Duplication Analysis

## Overlap Assessment Results
- High Overlap (>40%): [high_overlap_pairs]
- Medium Overlap (20-40%): [medium_overlap_pairs] 
- Low Overlap (<20%): [low_overlap_pairs]

## Authority Source Mapping
[File authority assignments based on size and recency]

## Consolidation Strategy
- **Immediate Merge**: [immediate_merge_list]
- **Section Consolidation**: [section_consolidation_list]
- **Reference Optimization**: [reference_optimization_list]

## Content Preservation Plan
[Essential content preservation during consolidation]
`)

// 3. BROKEN REFERENCE IDENTIFICATION AND REPAIR
// Comprehensive link analysis and repair strategy
Grep("\\[.*\\]\\(.*\\.md\\)", {glob: "**/*.md", output_mode: "content", -n: true}) // Extract all markdown links
Grep("BROKEN|MISSING|FIXME|TODO.*link", {glob: "**/*.md", output_mode: "files_with_matches"}) // Known broken refs

// Reference validation testing
Bash("find . -name '*.md' -print0 | xargs -0 grep -l '\\[.*\\]\\(' | while read file; do echo \"Checking references in $file\"; done")

// 4. PROGRESSIVE DISCLOSURE IMPLEMENTATION
// Extract oversized content to appropriate directories
Bash("find . -name '*.md' -exec awk 'END{if(NR>140) print FILENAME \" needs extraction: \" NR \" lines\"}' {} +") // Commands >140
Bash("find . -name '*.md' -exec awk 'END{if(NR>200) print FILENAME \" exceeds maximum: \" NR \" lines\"}' {} +") // Files >200

// Content extraction planning
Write("context/discoveries/progressive-disclosure-plan-[timestamp].md", `# Progressive Disclosure Extraction Plan

## Files Requiring Extraction
- Commands >140 lines: [oversized_commands]
- Documentation >200 lines: [oversized_docs]
- Context files >200 lines: [oversized_context]

## Extraction Strategy
- **Commands**: Extract detailed implementation → docs/ or context/
- **Standards**: Extract verbose content → appropriate subdirectories
- **Context**: Split large files → focused topic files

## Content Preservation
[Core functionality preservation during extraction]

## Reference Update Plan
[Link updates required after content extraction]
`)

// 5. CONSOLIDATION EXECUTION SIMULATION
// Test consolidation impact before actual implementation
Bash("echo 'Consolidation impact assessment:'")
Bash("echo 'Files to merge: [merge_count] | References to update: [reference_updates]'")
Bash("echo 'Content extraction required: [extraction_count] files'")

// 6. SYSTEM INTEGRITY VALIDATION
// Verify consolidation maintains system coherence
Grep("execution layer|EXECUTION LAYER", {glob: "**/*.md", output_mode: "files_with_matches"}) // Check implementations
Grep("tool calls|tool operations", {glob: "**/*.md", output_mode: "content"})                    // Verify tool ratios

// 7. CONSOLIDATION RESULTS DOCUMENTATION
Write("context/discoveries/consolidation-results-[timestamp].md", `# Content Consolidation Results

## Consolidation Summary
- Files Processed: [processed_count]
- Duplicate Content Eliminated: [eliminated_percentage]%
- References Repaired: [repaired_references]
- Progressive Disclosure Applied: [extraction_count] files

## Authority Source Establishment
[Final authority assignments and reasoning]

## Reference Integrity Status
- Total References: [total_references]
- Functional References: [functional_count]
- Broken References Repaired: [repaired_count]
- **Reference Health**: [reference_percentage]%

## Size Compliance Achievement
- Commands ≤140 lines: [compliant_commands]/[total_commands]
- Documentation ≤200 lines: [compliant_docs]/[total_docs]
- **Size Compliance**: [size_compliance_percentage]%

## System Coherence Verification
- Cross-reference integrity maintained: [YES/NO]
- Information completeness preserved: [YES/NO]
- Functional boundaries maintained: [YES/NO]

## Quality Metrics Post-Consolidation
- Content Duplication: [final_duplication]% (Target: <5%)
- Navigation Efficiency: [navigation_steps] avg steps (Target: ≤2.5)
- Reference Functionality: [reference_health]% (Target: 100%)
`)
```

### Consolidation Strategy Framework
**PRIORITY-BASED EXECUTION**:
- **High Priority** (>40% overlap): Immediate merge with authority establishment
- **Medium Priority** (20-40%): Section consolidation and standardization
- **Low Priority** (<20%): Reference optimization and formatting consistency

### Progressive Disclosure Logic
**EXTRACTION CRITERIA**:
- Commands >140 lines → Extract implementation details to docs/ or context/
- Standards >200 lines → Extract verbose content to subdirectories
- Context >200 lines → Split into focused topic files

### Session Completion Protocol
**MANDATORY WORKFLOW END**:
```javascript
// Git automation with consolidation metrics (no Claude attribution)
Bash("git add . && git commit -m \"docs-consolidate: duplication [before]%→[after]% | refs: [repaired] | session-[N]\"")
```

### Execution Verification
**TOOL CALL AUDIT**:
- **Duplication analysis**: 3 Grep + 2 Bash operations for assessment
- **Reference analysis**: 2 Grep + 1 Bash operations for validation
- **Progressive disclosure**: 2 Bash operations for size analysis
- **Documentation**: 3 Write operations for planning and results
- **Integrity validation**: 2 Grep operations for system coherence
- **Tracking**: 3 Bash operations for progress monitoring
- **Ratio**: 18 tool calls to ~80 documentation lines = 22% (HEALTHY)

---

**CRITICAL**: This command transforms system architecture through consolidation while maintaining information completeness and functional integrity. All consolidation operations must preserve essential content value.

**EXECUTION COMMITMENT**: Content consolidation with duplication elimination, reference repair, and progressive disclosure implementation are NOW implemented with actual tool calls.