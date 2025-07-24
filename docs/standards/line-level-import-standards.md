# Line-Level Import Standards

**Updated**: 2025-07-24 | **Authority**: Context management foundation | **Limit**: 100 lines

## Core Import Strategies

### Full File Import (`@file.md`)
**Use When**: Complete file context required | File ≤100 lines | High usage frequency (>70% sessions)
**Example**: `@docs/core/project-structure-current.md`
**Token Impact**: Entire file loaded always | High token cost | Complete context available

### Line Range Import (`@file.md:15-30`) 
**Use When**: Specific section needed | File >100 lines | Concept extraction required
**Example**: `@docs/rules/documentation-standards.md:25-45` (core principles only)
**Token Impact**: Reduced token cost | Precise context | Self-contained sections

### Multiple Range Import (`@file.md:5-10,25-35`)
**Use When**: Non-contiguous sections needed | Skip irrelevant content | Complex concept assembly
**Example**: `@docs/core/pts-framework.md:1-15,45-60` (definition + implementation)
**Token Impact**: Optimal precision | Complex maintenance | Maximum context efficiency

### Single Line Import (`@file.md:42`)
**Use When**: Specific definition needed | Quick reference | Minimal context required
**Example**: `@docs/standards/import-criteria.md:25` (decision threshold)
**Token Impact**: Minimal cost | Risk of incomplete context | Precise targeting

## Decision Framework

### Import Selection Criteria
**Full File**: Essential understanding + ≤100 lines + >70% usage + standalone concept
**Line Range**: Specific procedures + >100 lines + section independence + clear boundaries  
**Multiple Range**: Complex assembly + scattered concepts + context optimization + maintenance acceptable
**Single Line**: Definition only + minimal context + quick reference + high precision

### Context Coherence Requirements
**Semantic Completeness**: Lines understandable without additional context | **Boundary Integrity**: Complete thoughts/procedures | **Reference Stability**: Stable line numbers | **Authority Preservation**: Maintain authoritative context

## Implementation Standards

### Line Range Format
```markdown
## Section Title
@path/to/file.md:15-30
```
**Requirements**: Start-end line numbers | Complete sections | Clear boundaries | Self-contained content

### Context Annotation
```markdown
## Section Title  
**Context**: Core implementation procedures from methodology guide
@docs/implementation/methodology-implementation.md:45-75
```
**Purpose**: Explain why specific lines chosen | Provide context for imported content | Aid maintenance

### Maintenance Protocols
**Line Stability**: Organize files with stable line structures | Minimize line number changes | Use section-based organization
**Reference Updates**: When files change, validate all line references | Update ranges if content shifts | Maintain semantic integrity
**Validation**: Regular checks for line reference accuracy | Automated tools for reference validation | Broken reference detection

## Context Economy Optimization

### Token Cost Analysis
**Full File (100 lines)**: 100 tokens always loaded | Complete context | High cost
**Line Range (15 lines)**: 15 tokens | Focused context | 85% cost reduction
**Multiple Range (25 lines)**: 25 tokens | Optimized assembly | 75% cost reduction  
**Single Line (1 line)**: 1 token | Minimal context | 99% cost reduction

### Usage Pattern Optimization
**Daily Use (>70% sessions)**: Full file import justified | Always available | High value
**Task-Specific (30-70% sessions)**: Line range import optimal | Conditional loading | Balanced efficiency
**Rare Use (<30% sessions)**: Reference only | On-demand access | Maximum economy

## Quality Standards

### Quality Standards
**Line Selection**: Complete concepts | Context independence | Boundary clarity | Reference stability  
**Maintenance**: Reference validation | Content stability | Update protocols | Quality gates

## Integration with System Architecture

### Three-Layer Architecture
**Layer 1 (Concept)**: `@file.md:1-25` (essential understanding only)
**Layer 2 (Implementation)**: `@file.md:30-75` (detailed procedures)
**Layer 3 (Verification)**: `@file.md:80-100` (quality gates only)

### Conditional Loading Enhancement
**Documentation Work**: `@standards.md:15-35` (core principles)
**Command Development**: `@templates.md:20-50` (essential patterns)
**Architecture Decisions**: `@framework.md:10-30,60-80` (key concepts + implementation)

### Authority Hierarchy Integration
**Vision Level**: Full file imports (complete authority context)
**Rules Level**: Line range imports (specific behavioral guidance)
**Implementation Level**: Multiple range imports (optimized technical context)
**Navigation Level**: Single line imports (quick reference definitions)

---

**Principle**: Line-level import precision optimizes context economy while preserving semantic completeness, enabling intelligent loading strategies that match actual usage patterns with maximum efficiency