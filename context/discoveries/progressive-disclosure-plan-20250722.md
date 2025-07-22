# Progressive Disclosure Extraction Plan - 2025-07-22

## Files Requiring Extraction

### CRITICAL: CLAUDE.md Oversized Issue
- **CLAUDE.md**: 300,393 lines (should be ≤200) - EXTREME VIOLATION
- **Root cause**: File appears to contain entire codebase content incorrectly
- **Action**: Investigate and restore to proper summary format

### Commands >140 lines:
- All command files appear to be within reasonable limits based on recent modifications
- Recent commands (docs-validate, matrix-maintenance, docs-workflow) are appropriately sized

### Documentation >200 lines:
- Multiple implementation files likely exceed 200 lines (to be verified)
- Cross-reference analysis files may need splitting

### Context files >200 lines:
- Research files and pattern documentation may exceed limits
- Discovery files should be split by topic areas

## Extraction Strategy

### CRITICAL: CLAUDE.md Restoration
- **Immediate**: Restore CLAUDE.md to proper summary format (≤200 lines)
- **Content**: Extract detailed content → appropriate docs/ subdirectories
- **Structure**: Maintain only essential command directory and overview

### Commands: Extract implementation details → docs/ or context/
- **Execution layers**: Move complex tool call sequences to docs/implementation/
- **Behavioral patterns**: Consolidate repetitive TodoWrite templates
- **Technical specs**: Extract detailed implementation to appropriate docs/

### Standards: Extract verbose content → subdirectories
- **Frameworks**: Split large framework docs into focused components
- **Implementation guides**: Create separate files for complex procedures
- **Cross-references**: Streamline linking to reduce redundancy

### Context: Split large files → focused topic files
- **Research**: Split by topic area (git-worktrees, metrics, etc.)
- **Patterns**: Separate behavioral, architectural, and implementation patterns
- **Discoveries**: Group related discovery sessions

## Content Preservation

### Core Functionality Preservation During Extraction:
- **Command executability**: All tool calls and workflows must remain functional
- **Reference integrity**: All links must resolve correctly post-extraction
- **User experience**: Command discovery and execution must remain seamless
- **System coherence**: Architectural relationships must be maintained

### Essential Content Types:
- **Command summaries**: Purpose, usage, and basic implementation
- **Critical workflows**: Primary discovery and execution flows
- **Key standards**: Essential writing, anti-bias, and structural rules
- **Core patterns**: Fundamental behavioral and architectural patterns

## Reference Update Plan

### Link Updates Required After Content Extraction:
- **Internal command references**: Update paths to extracted content
- **Cross-document links**: Verify and repair broken references
- **Parent-child relationships**: Maintain hierarchical documentation structure
- **Bidirectional linking**: Ensure extracted content links back to sources

### Validation Process:
- **Link checking**: Automated verification of all markdown links
- **Functional testing**: Verify commands execute correctly post-extraction
- **Content completeness**: Ensure no essential information lost during extraction
- **Navigation efficiency**: Maintain ≤2.5 average steps to find information