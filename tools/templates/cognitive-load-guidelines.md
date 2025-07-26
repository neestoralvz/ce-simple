# Cognitive Load Management Guidelines

**Purpose**: Maintain optimal cognitive performance by controlling information density in core system files
**Authority**: Technical framework implementing PTS principles

## Core Principle

**Cognitive Load Optimization**: Minimize automatic context while maximizing accessibility to detailed information through intelligent referencing.

## File Size Limits & Rationale

### Automatic Context Files (Always Loaded)
- **CLAUDE.md**: ≤50 lines (navigation only)
- **CLAUDE_RULES.md**: ≤100 lines (essential rules only)
- **Total Automatic Context**: ≤150 lines

### Rationale
- **LLM Performance**: Reduced token consumption in initial context
- **Focus Maintenance**: Essential information immediately accessible
- **Cognitive Clarity**: No information overload during decision-making
- **Response Quality**: Better attention to user requests vs. system overhead

## Content Distribution Strategy

### What Goes in Automatic Context
- **Essential Rules**: Non-negotiable governance principles
- **Navigation Structure**: Clear paths to detailed information
- **Critical Decisions**: Information needed for immediate choices
- **Authority Hierarchy**: Who/what has final say on conflicts

### What Gets Referenced
- **Detailed Processes**: Step-by-step implementation guides
- **Examples**: Code samples, command templates, use cases
- **Historical Context**: Background, evolution, learnings
- **Specialized Knowledge**: Domain-specific technical details

## Template Compliance Framework

### Section Length Discipline
- **Hard Limits**: Each template section has maximum line count
- **Content Density**: Maximum information value per line
- **Reference Efficiency**: Clear, actionable paths to details
- **No Redundancy**: Single source of truth maintained

### Quality Gates
1. **Pre-Edit Validation**: Check line count before changes
2. **Content Audit**: Ensure no details leak into core files
3. **Reference Verification**: All @docs/ links functional
4. **Cognitive Test**: Can I maintain focus after reading?

## Reference System Standards

### Link Format
- **Local References**: @docs/path/file.md
- **Section References**: @docs/path/file.md#section
- **Command References**: /command-name
- **External References**: Full URLs only when necessary

### Reference Quality
- **Descriptive**: Reader knows what they'll find
- **Actionable**: Clear next steps provided
- **Maintained**: Links checked and updated regularly
- **Hierarchical**: Authority level of referenced content clear

## Cognitive Load Indicators

### Warning Signs (Stop & Refactor)
- Taking >2 minutes to find essential information
- Multiple files needed to understand basic concepts
- Repeated information across different files
- Feeling overwhelmed when reading core files
- Losing track of user requests while processing context

### Health Indicators (System Working)
- Essential decisions made within 30 seconds
- Clear path to detailed information when needed
- No duplicate information in core files
- Comfortable cognitive load during conversations
- Maintained focus on user objectives

## Maintenance Protocol

### Regular Audits (Monthly)
1. **Line Count Check**: Verify templates within limits
2. **Reference Validation**: Ensure all links functional
3. **Content Migration**: Move growing details to appropriate docs/
4. **Cognitive Performance**: Self-assess focus and response quality

### Emergency Interventions (When Load Exceeds)
1. **Immediate Archiving**: Move non-essential content to docs/
2. **Reference Conversion**: Replace inline details with links
3. **Structure Simplification**: Reduce hierarchy levels
4. **Template Reapplication**: Force compliance with original templates

## Success Metrics

### Quantitative
- **Context Size**: ≤150 lines total automatic context
- **Response Time**: Essential decisions within 30 seconds
- **Reference Efficiency**: ≤3 clicks to find detailed information
- **Link Maintenance**: >95% functional reference links

### Qualitative
- **Focus Maintenance**: Sustained attention on user objectives
- **Decision Quality**: Consistent application of principles
- **Navigation Ease**: Intuitive path to needed information
- **Cognitive Comfort**: No overwhelm during normal operations

## Implementation Strategy

### Phase 1: Template Creation ✓
- Core file templates with strict limits
- Section-by-section line budgets
- Reference standards established

### Phase 2: Content Migration (Next)
- Detailed content moved to docs/ structure
- References updated and verified
- Core files compressed to template compliance

### Phase 3: Monitoring & Maintenance (Ongoing)
- Regular cognitive load assessments
- Template compliance monitoring
- Continuous optimization based on usage patterns

---

**Implementation Note**: These guidelines ensure that the ce-simple system maintains technical sophistication while remaining cognitively manageable for both LLM processing and human collaboration.