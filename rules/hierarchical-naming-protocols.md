# Hierarchical Naming Protocols - System Rule

**Updated**: 2025-07-26 | **Authority**: System architecture | **Scope**: All file/directory naming

## Hierarchical Naming Convention Rule

**MANDATORY for all file/directory creation, renaming, or organization work**: Systematic naming for complete directory/file hierarchy.

## When to Apply This Rule

**IF hierarchical naming needed** → Any work involving:
- File or directory creation
- Renaming operations  
- Organization or restructuring work
- New category establishment
- Reference system maintenance

## Naming Convention Standards

### Directory Pattern
- **Format**: `[number]-[code]-[purpose]/`
- **Examples**: `01-fnd-foundations/`, `02-std-standards/`
- **Purpose**: Clear ordering + category identification
- **Implementation**: Sequential numbering for logical hierarchy

### File Pattern  
- **Format**: `[category-code]-[specific-purpose].md`
- **Code MUST match parent directory code**  
- **Examples**: `fnd-pts-framework.md`, `std-command-governance.md`
- **Purpose**: Instant category recognition + hierarchical consistency

### Category Codes
- **fnd** = Foundations | **std** = Standards | **com** = Communication
- **pro** = Protocols | **per** = Performance | **inf** = Infrastructure

## Enforcement Protocol

### Quality Gates
- **Pre-Creation**: No creation without pattern compliance
- **Auto-Correction**: Immediate rename when non-compliance discovered  
- **Reference Updates**: All internal links updated during renaming
- **Scalability**: New categories follow same [number]-[code]-[purpose] pattern

### Implementation Standards
- **Consistency**: All files within directory must use matching category code
- **Scalability**: Pattern accommodates unlimited category expansion
- **Recognition**: Instant identification of file category and hierarchy level
- **Maintenance**: Automated tools can validate and correct naming violations

### Validation Process
1. **Scan**: Check all files/directories for pattern compliance
2. **Identify**: Mark non-compliant items for correction
3. **Rename**: Apply correct pattern maintaining content integrity
4. **Update**: Modify all references to reflect new names
5. **Verify**: Confirm all links and references work correctly

---

**Naming Truth**: Systematic hierarchical naming enables instant navigation, category recognition, and scalable file organization across the entire VDD framework.