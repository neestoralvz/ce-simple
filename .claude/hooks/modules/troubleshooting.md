# Troubleshooting - Issues & Solutions Authority

**31/07/2025 CDMX** | Complete troubleshooting guide and solutions

## AUTORIDAD SUPREMA
hooks/README.md → troubleshooting.md implements complete troubleshooting authority per hooks system

## PRINCIPIO FUNDAMENTAL
**"Systematic problem resolution with clear diagnostic and solution pathways"** - Comprehensive troubleshooting with proven solutions.

## STATUS MONITORING

### **System Status Checks**
```bash
# Check if hooks are active
ls -la .claude/hooks/

# View protection log
tail -f .claude/hooks/protection.log

# Test individual components
./.claude/hooks/authority-validation.sh
./.claude/hooks/root-protection.sh "/path/to/test/file"
```

## COMMON ISSUES & SOLUTIONS

### **Hook Not Executing**
**Symptoms**: No protection messages during file operations
**Solution**: 
- Verify `.claude/hooks/project-protection.json` exists
- Check script permissions: `chmod +x .claude/hooks/*.sh`
- Verify Claude Code hooks are enabled in settings

### **Performance Issues**
**Symptoms**: Slow response during file operations
**Solution**:
- Check hook execution times in logs
- Verify scripts aren't hanging on file operations
- Reduce timeout values in `project-protection.json` if needed

### **False Positives**
**Symptoms**: Legitimate files being flagged or moved
**Solution**:
- Edit exclusion patterns in individual hook scripts
- Update `allowed_root_files` in `project-protection.json`
- Adjust enforcement levels from "warn" to "info"

### **Authority Warnings**
**Symptoms**: Authority drift warnings during session start
**Solution**:
- Review files containing "override.*authority" patterns
- Verify authority chains in core files are intact
- Run manual authority validation: `./.claude/hooks/authority-validation.sh`

## INTEGRATION REFERENCES
**Authority Source**: ← @../README.md (hooks system authority)
**Components**: ← components.md (component configuration)
**Customization**: → customization-guide.md (advanced customization)

---
**TROUBLESHOOTING DECLARATION**: Complete problem resolution system providing systematic diagnostic and solution pathways for all hook system issues.