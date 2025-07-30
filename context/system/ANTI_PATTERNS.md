# Anti-Patterns Documentation

**29/07/2025 16:30 CDMX** | Known system issues and workarounds

## CRITICAL ANTI-PATTERN: Claude Code Semantic Organization Non-Compliance

### **PROBLEM IDENTIFIED** 
Claude Code internamente ignora semantic organization variables y crea archivos fuera de ${CONVERSATION_STORAGE}.

### **MANIFESTATION**
- Comando `/workflows:close` no respeta ${CONVERSATION_STORAGE} variable
- Sistema ignora SEMANTIC_ORGANIZATION.md configuration
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
# Check for semantic organization violations
if [ -d "context/raw" ]; then
    mv context/raw/* ${CONVERSATION_STORAGE}/ 2>/dev/null
    rmdir context/raw
    echo "✅ Semantic organization compliance restored"
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
        mv context/raw/* ${CONVERSATION_STORAGE}/ 2>/dev/null
        rmdir context/raw
        echo "$(date): Auto-restored semantic organization compliance"
    fi
done
```

### **USER EDUCATION**

**EXPECTATION SETTING:**
> "System should automatically respect semantic organization. Any violation indicates SEMANTIC_ORGANIZATION.md is not being properly consulted."

**PREVENTION:** 
> Currently **NOT PREVENTABLE** - requires post-execution cleanup

### **ESCALATION PATH**
1. **Report to Claude Code team** - Internal hardcoding issue
2. **Request configuration option** for conversation storage path
3. **Feature request** for respecting project structure preferences

---

**STATUS**: REQUIRES SEMANTIC ORGANIZATION IMPLEMENTATION - Variables not being respected
**TRACKING**: Monitor future Claude Code releases for path configuration options
**IMPACT LEVEL**: MEDIUM - Manageable with workaround, but creates friction