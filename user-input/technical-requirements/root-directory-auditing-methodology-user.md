# Root Directory Auditing Methodology - User Vision

**Date**: 2025-07-26  
**Type**: Operational methodology - Sacred User Space  
**Status**: Essential project health maintenance

## User's Core Methodology Vision

**Fundamental Principle**: "Directorio raíz debe mantenerse limpio con solo archivos esenciales - revisión constante y reorganización automática"

## 4-Step Root Auditing Protocol (User Requirements)

### Step 1: Scan Complete (Detection)
**User Need**: "Escaneo completo de archivos en raíz para identificar elementos fuera de lugar"
- Regular scanning of root directory for non-essential files
- Automated detection of backup files, temporary files, misplaced documentation
- Identification of files that should belong in specialized directories
- Cataloging of files not referenced in CLAUDE.md navigation

### Step 2: Classify Location (Smart Routing)  
**User Need**: "Clasificación inteligente basada en tipo y propósito del archivo"
- Backup files → backups/ directory
- Documentation files → docs/ appropriate subdirectory  
- Command files → commands/ directory
- Configuration files → tools/ or root (if truly essential)
- Planning materials → planning/ directory
- User input → user-input/ directory

### Step 3: Relocate Safely (Preservation)
**User Need**: "Reubicación segura manteniendo todas las referencias internas"
- Move files to appropriate directories preserving content
- Update all references and links pointing to relocated files
- Maintain git history and avoid breaking external references
- Test functionality after relocation to ensure no breakage

### Step 4: Validate Structure (Quality Gate)
**User Need**: "Validar que CLAUDE.md refleje estructura actual y archivos esenciales"
- Verify CLAUDE.md references are current and accurate
- Ensure new files in docs/core/ are properly referenced
- Validate directory structure matches documented architecture
- Confirm root directory contains only essential files

## User's Quality Requirements

### Essential Root Files (User Definition)
**User Mandate**: "Solo archivos críticos para funcionamiento del sistema"
- CLAUDE.md (navigation and authority)
- rules/CLAUDE_RULES.md (partnership protocol)  
- README.md (project overview)
- mkdocs.yml (documentation generation)
- .gitignore (git configuration)
- package.json / requirements.txt (if applicable)

### Automatic Reorganization Criteria
**User Critical Requirements**:
- Backup files must move to backups/ directory
- Temporary analysis files belong in planning/ or docs/
- New documentation goes to appropriate docs/ subdirectory
- Command implementations belong in commands/ directory
- User specifications stay in user-input/ directory
- Tools and scripts belong in tools/ directory

## Success Criteria (User Definition)

**Root Cleanliness**: Maximum 6-8 files in root directory at any time
**Reference Integrity**: 100% of relocated files maintain working references
**Navigation Accuracy**: CLAUDE.md reflects all current essential structure
**Quality Maintenance**: Regular auditing prevents accumulation of misplaced files
**User Transparency**: Clear reporting of what was moved and why

## Automation Requirements (User Vision)

**Continuous Monitoring**: Regular scans detect new files in root immediately
**Smart Classification**: Automated file type detection and location recommendation  
**Safe Relocation**: Preserve references and maintain system functionality
**User Notification**: Clear reporting of changes made and rationale

---

**User Truth**: "Escaneo continuo, clasificación inteligente, reubicación segura, validación completa - mantener raíz limpia mientras preservamos funcionalidad."