# Root Directory Auditing Protocols - System Rule

**Updated**: 2025-07-26 | **Authority**: Project health | **Scope**: Root directory management

## Root Directory Auditing Rule

**MANDATORY for project health**: Regular audit and cleanup of root directory to maintain clean project structure.

## When to Apply This Rule

**IF root directory work** → Any work involving:
- File placement assessment
- Directory organization 
- Project structure maintenance
- Repository cleanup operations
- New file creation decisions

## Auditing Protocol

### 4-Step SCAN → CLASSIFY → RELOCATE → VALIDATE Process

#### Step 1: SCAN
- **Regular audit** of root directory for misplaced files
- **Systematic review** of all root-level items
- **Identification** of files that don't belong in root
- **Documentation** of current root directory state

#### Step 2: CLASSIFY  
- **Determine correct location** based on file type and purpose
- **Apply directory structure standards** for placement decisions
- **Consider file relationships** and logical groupings
- **Reference existing organization patterns** for consistency

#### Step 3: RELOCATE
- **Move files** to appropriate directories maintaining references
- **Update all internal links** to reflect new locations
- **Preserve file integrity** during relocation process
- **Maintain git history** and avoid unnecessary file renames

#### Step 4: VALIDATE
- **Verify CLAUDE.md** reflects current structure and new files
- **Test all references** to ensure they work correctly
- **Confirm proper categorization** of relocated files
- **Document changes** in appropriate tracking systems

## Critical Files Protocol

### Root Directory Allowlist
**ONLY these files belong in root:**
- `CLAUDE.md` - Project navigation and instructions
- `rules/CLAUDE_RULES.md` - Partnership protocol and core rules
- `README.md` - Repository overview and setup
- `mkdocs.yml` - Documentation site configuration

### Enforcement Standards
- **Zero tolerance** for misplaced files in root
- **Immediate relocation** when violations discovered
- **Reference integrity** maintained during moves
- **Documentation updates** required for all changes

### Health Metrics
- **Root file count**: ≤4 critical files only
- **Misplacement rate**: 0% tolerance
- **Reference accuracy**: 100% working links
- **Structure compliance**: Full adherence to directory standards

---

**Authority Reference**: [root-directory-auditing-methodology-user.md](../user-input/technical-requirements/root-directory-auditing-methodology-user.md)

**Auditing Truth**: Clean root directory structure enables immediate project comprehension and maintains professional repository standards.