# Customization Guide - Configuration Authority

**31/07/2025 CDMX** | Complete customization and configuration guide

## AUTORIDAD SUPREMA
hooks/README.md → customization-guide.md implements complete customization authority per hooks system

## PRINCIPIO FUNDAMENTAL
**"Flexible customization enabling project-specific protection configurations"** - Comprehensive customization framework with clear guidelines.

## CUSTOMIZATION GUIDELINES

### **Adding Exclusions**
Edit hook scripts to add file/directory exclusions:
```bash
# In root-protection.sh, add to allowed files:
"newfile.md"|"special-case.txt")

# In size-validation.sh, add to exclusion function:
[[ "$file" =~ /my-special-dir/ ]] && return 0
```

### **Adjusting Enforcement Levels**
Modify `project-protection.json`:
```json
{
  "project": {
    "enforcement_level": "warn",  // "info", "warn", "error"
    "max_file_lines": 80,         // Adjust line limit
    "fail_on_error": false        // Set to true for strict mode
  }
}
```

### **Creating Custom Hooks**
1. Create new script in `.claude/hooks/`
2. Make executable: `chmod +x new-script.sh`
3. Add to `project-protection.json` events
4. Test thoroughly before deployment

## CONFIGURATION FRAMEWORK

### **Project-Specific Adaptation**
Customization system enables project-specific protection requirements while maintaining system integrity and consistency.

### **Enforcement Flexibility**
Multiple enforcement levels provide flexibility from informational guidance to strict validation based on project needs.

## INTEGRATION REFERENCES
**Authority Source**: ← @../README.md (hooks system authority)
**Troubleshooting**: ← troubleshooting.md (issue resolution)
**System Integration**: → system-integration.md (coordination with other systems)

---
**CUSTOMIZATION DECLARATION**: Complete customization framework providing flexible configuration and project-specific adaptation while maintaining system integrity.