# Anthropic CLAUDE.md Standards Research

## 🎯 Purpose
Consolidated research on official Anthropic documentation standards for CLAUDE.md files and Claude Code integration.

## 📋 OFFICIAL REQUIREMENTS

### File Hierarchy and Priority
**Official Anthropic specification**:
1. **Global User Memory**: `~/.claude/CLAUDE.md` - Personal preferences across all projects
2. **Project Memory**: `./CLAUDE.md` - Team-shared project instructions (recommended)
3. **Directory-Specific**: Subdirectory CLAUDE.md files for granular context
4. **Local Override**: `CLAUDE.local.md` for personal, non-committed instructions

**Memory Loading Priority**: Claude reads recursively from current working directory up to (but not including) root directory. Most specific, nested files take priority when relevant.

### Required Content Structure
**Essential Sections (Anthropic recommended)**:
```markdown
# Tech Stack
- Framework: [Your framework and version]
- Language: [Programming language and version]  
- Styling: [CSS framework/approach]

# Bash Commands
- npm run build: Build the project
- npm run typecheck: Run the typechecker
- npm run test: Run all tests

# Code Style
- Use ES modules (import/export) syntax
- Destructure imports when possible
- Use 2-space indentation

# Project Structure  
- src/app: Next.js App Router pages
- src/components: Reusable React components
- src/lib: Core utilities and API clients

# Workflow
- Typecheck after making changes
- Prefer running single tests for performance
- Do not edit files in src/legacy directory
```

## 🔧 IMPORT SYSTEM

### Import Functionality
**Official Capabilities**:
- Supports `@path/to/import` syntax for both relative and absolute paths
- Maximum 5 import hops allowed to prevent infinite loops
- Imports not evaluated inside code spans/blocks
- Example: `See @README for project overview and @package.json for available commands`

### Import Best Practices
- Use for referencing existing documentation vs duplicating content
- Maintain import chain health through regular validation
- Prefer specific sections over entire file imports

## 📏 TOKEN OPTIMIZATION

### Context Window Management
**Technical Constraints**:
- **Maximum Context Window**: 200,000+ tokens (~150,000 words or 500 pages)
- **Memory Impact**: All CLAUDE.md content consumes context window space at session start
- **Optimization Principle**: Keep files lean as they're loaded beginning of each session

### Efficiency Guidelines
**Content Strategy**:
- **Concise Content**: Focus on essential information only
- **Structured Format**: Use markdown hierarchy for efficient parsing
- **Ad-hoc References**: Use `@docs/filename.md` references vs inline content
- **Regular Review**: Periodically clean and optimize memory files

## ✅ COMPLIANCE VALIDATION

### Quality Standards Checklist
**Essential Requirements**:
- [ ] File placed in appropriate location (project root recommended)
- [ ] Contains project-specific bash commands
- [ ] Includes code style guidelines
- [ ] Documents project structure
- [ ] Specifies tech stack and versions
- [ ] Uses clear markdown formatting

**Content Quality Standards**:
- [ ] Instructions are specific ("Use 2-space indentation" vs "Format code properly")
- [ ] Content structured with descriptive headings
- [ ] Related memories grouped as bullet points
- [ ] No extensive content without iteration testing
- [ ] Emphasis added where needed ("IMPORTANT", "YOU MUST")

**Integration Standards**:
- [ ] File committed to version control (team sharing)
- [ ] Regular updates via `#` key additions
- [ ] Periodic review and refinement
- [ ] Import statements tested and functional
- [ ] Memory content validated with `/memory` command

## 🚫 ANTIPATTERN PREVENTION

### Content Antipatterns
**Avoid These Patterns**:
1. **Over-Documentation**: Including every possible detail instead of essentials
2. **Vague Instructions**: Ambiguous requirements that assume Claude will infer context
3. **Mixed Concerns**: Combining multiple unrelated topics in one file
4. **Static Content**: Never updating or iterating on memory effectiveness

### Technical Antipatterns
**System Integration Issues**:
1. **Token Waste**: Extensive content that doesn't improve Claude's performance
2. **Poor Hierarchy**: Flat structure without markdown organization
3. **Import Loops**: Circular references in import statements
4. **Version Control Issues**: Not committing team-relevant memories

### Workflow Antipatterns
**Development Process Issues**:
1. **One-and-Done**: Writing memory once without testing effectiveness
2. **Inconsistent Terminology**: Using different terms for the same concepts
3. **Missing Context**: Assuming Claude knows project-specific conventions
4. **Neglected Maintenance**: Outdated instructions that harm performance

## 🔧 OPTIMIZATION FRAMEWORK

### Performance Optimization
**Iterative Improvement Strategy**:
- **Iterative Refinement**: Regularly test and improve instruction effectiveness
- **Prompt Engineering**: Use proven prompt engineering techniques within memories
- **Context Management**: Monitor context usage with `/memory` command
- **Progressive Enhancement**: Start minimal and add only proven-effective content

### Integration Tools
**Claude Code Built-in Tools**:
- **`/memory`**: Open memory files in system editor
- **`#` key**: Quick memory addition during sessions
- **`/init`**: Bootstrap CLAUDE.md for new projects
- **`/clear`**: Clear context to prevent token waste

### Validation Methods
**Effectiveness Measurement**:
- **A/B Testing**: Compare Claude performance with different memory versions
- **Team Reviews**: Regular team assessment of memory effectiveness
- **Success Tracking**: Monitor task completion rates and code quality
- **Iteration Cycles**: Systematic improvement based on usage patterns

## 📊 APPLICATION TO CE-SIMPLE

### Current Compliance Assessment
**ce-simple CLAUDE.md Status**:
- **Location**: ✅ Project root placement correct
- **Structure**: ⚠️ Mixed abstraction levels detected
- **Content**: ⚠️ 102 lines with 23% potentially redundant content
- **Cross-References**: ❌ Excessive internal linking (47 references)
- **Token Efficiency**: ⚠️ Optimization opportunities identified

### Optimization Recommendations
**Priority Improvements**:
1. **Reduce Cognitive Load**: 30% content consolidation target
2. **Implement Progressive Disclosure**: Move complex sections to referenced files
3. **Establish Clear Entry Point Hierarchy**: Streamline navigation flow
4. **Optimize Cross-Reference Density**: Reduce from 47 to ≤20 essential references

### Integration with System Standards
**Alignment with ce-simple Principles**:
- Apply simplicity-first framework to CLAUDE.md content
- Use ≤140 line optimal target (vs Anthropic's flexible approach)
- Implement anti-fragmentation principles in memory structure
- Maintain bidirectional reference network health

---

**CRITICAL INTEGRATION INSIGHT**: Anthropic's official standards emphasize effectiveness and iteration over rigid structure, aligning well with ce-simple's simplicity-first and context-optimization principles.