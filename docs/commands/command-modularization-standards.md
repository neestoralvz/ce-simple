# Command Modularization

## Purpose
Maintain 150-line command limits while preserving full functionality through progressive disclosure.

## Core Principles

### Progressive Disclosure
Complex details move to referenced files, not inline expansion.

### Modularization Triggers
Modularize when command exceeds:
- 150 lines total
- Complex tool specifications
- Multiple detailed examples

## Modularization Strategies

### Implementation Extraction
Move detailed tool implementations to separate files.

Structure:
- Main command: Essential structure and core tool calls
- Implementation file: Detailed specifications and automation logic

Example: `command-maintain.md` (95 lines) with consolidated implementation details

### Usage Documentation Separation
Extract comprehensive examples to dedicated files.

Structure:
- Main command: Basic usage only
- Usage file: Detailed examples and troubleshooting

### Framework Documentation
Extract complex frameworks to dedicated files.

Structure:
- Main command: Framework reference only
- Framework file: Detailed methodology and algorithms

## Modularization Process

### Content Analysis
Identify commands exceeding 150 lines and analyze sections for extraction potential.

### Content Classification
Keep in main command:
- Purpose
- Basic usage
- Core implementation steps
- Essential tool calls

Extract to implementation file:
- Detailed tool specifications
- Complex automation logic
- Error handling procedures
- Advanced configuration

Extract to usage file:
- Comprehensive examples
- Edge case scenarios
- Troubleshooting procedures

### Reference Integration
Command file references: `See command-name-details.md for detailed specifications`

Standards:
- Bidirectional references
- Consistent naming: `command-name-[suffix].md`
- Clear purpose for each extracted file

## Quality Standards

### Size Targets
- Main command: ≤150 lines
- Implementation file: ≤200 lines
- Usage file: ≤150 lines
- Framework file: ≤200 lines

### Content Requirements
Main command retains:
- Complete functional capability
- Essential tool calls
- Clear workflow understanding
- Autonomous execution ability

Extracted files provide:
- Comprehensive detail without duplication
- Clear relationship to main command
- Self-contained reference value

### Validation Checklist
- Main command ≤150 lines
- Functionality preserved
- References accurate and bidirectional
- No content duplication
- Clear extraction rationale

## Implementation Tools

### Automated Modularization
Create implementation files automatically by extracting detailed sections and replacing with references.

### Reference Maintenance
Validate all command references to ensure no broken links exist.

## Success Metrics

### Effectiveness Measures
- Size reduction: Commands >150 lines → ≤150 lines
- Functionality preservation: 100% capability retention
- Reference integrity: 0 broken links
- Improved cognitive load management

### Quality Indicators
- Main command understandable independently
- Implementation files provide complete detail
- Updates possible to extracted content
- Implementation patterns reusable across commands

## System Integration

### Standards Compliance
Aligns with 150-line limits while preserving functionality through progressive disclosure.

### Template Compatibility
Modularized commands follow standard template with consistent structure and clear cross-references.

---

**Command modularization preserves functionality within 150-line limits while maintaining autonomous execution capability.**