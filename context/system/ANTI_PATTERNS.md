# Anti-Patterns Documentation

**29/07/2025 16:30 CDMX** | Known system issues and workarounds

## CRITICAL ANTI-PATTERN: Claude Code Hardcoded "raw" Path

### **PROBLEM IDENTIFIED** 
Claude Code internamente crea archivos de conversación en `context/raw/` independientemente de configuración del proyecto.

### **MANIFESTATION**
- Comando `/workflows:close` crea archivo en `context/raw/`
- Carpeta `raw/` se recrea automáticamente aunque se elimine
- Comportamiento **NO configurable** en archivos accesibles

### **ROOT CAUSE INVESTIGATION**
✅ **Verified NOT in**: 
- `.claude/settings.toml` - Sin referencias path conversation
- `.claude/settings.local.json` - Solo permissions, no paths
- Command files (commands/*.md) - No hardcoding detectado
- Scripts directory - No referencias problematicas
- Environment variables - No configuración relevante

❌ **LIKELY SOURCE**: Claude Code binary/interno behavior

### **IMPACT**
- **Architectural inconsistency** permanente
- **Manual intervention** requerida después cada session close
- **User confusion** sobre location correcta de conversations

### **WORKAROUND PROTOCOL**

#### **Immediate Response** (Post-close cleanup)
```bash
# After each /workflows:close execution:
if [ -d "context/raw" ]; then
    mv context/raw/* context/conversations/ 2>/dev/null
    rmdir context/raw
    echo "✅ Raw cleanup completed"
fi
```

#### **Monitoring Script** (Optional automation)
```bash
#!/bin/bash
# .claude/hooks/raw-cleanup.sh
# Auto-cleanup if raw directory detected

while inotifywait -q -e create context/; do
    if [ -d "context/raw" ]; then
        sleep 1  # Allow file write completion
        mv context/raw/* context/conversations/ 2>/dev/null
        rmdir context/raw
        echo "$(date): Auto-moved files from raw/ to conversations/"
    fi
done
```

### **USER EDUCATION**

**EXPECTATION SETTING:**
> "After using `/workflows:close`, manually move any files from `context/raw/` to `context/conversations/` and remove the raw directory. This is a known limitation of Claude Code's internal behavior."

**PREVENTION:** 
> Currently **NOT PREVENTABLE** - requires post-execution cleanup

### **ESCALATION PATH**
1. **Report to Claude Code team** - Internal hardcoding issue
2. **Request configuration option** for conversation storage path
3. **Feature request** for respecting project structure preferences

---

**STATUS**: UNRESOLVED - Requires vendor fix or configuration option
**TRACKING**: Monitor future Claude Code releases for path configuration options
**IMPACT LEVEL**: MEDIUM - Manageable with workaround, but creates friction