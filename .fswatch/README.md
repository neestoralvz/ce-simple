# CE-Simple Guardian Protection System

**Sistema de protección continua para estructura de proyecto y enforcement de estándares**

## 🛡️ Overview

El Guardian Protection System implementa monitoreo continuo en tiempo real usando `fswatch` + `launchd` para:

- **Root Protection**: Prevenir archivos no autorizados en la raíz del proyecto
- **File Size Enforcement**: Detectar archivos >80 líneas que requieren factorización
- **Standards Compliance**: Validar estándares de proyecto automáticamente
- **Auto-remediation**: Mover archivos automáticamente a ubicaciones correctas

## 🚀 Installation

```bash
# Install the Guardian Protection System
./.fswatch/install.sh
```

El sistema se instala como un servicio de `launchd` que se ejecuta automáticamente.

## 📋 Components

### Core Daemon
- **`protection-daemon.sh`**: Script principal que usa `fswatch` para monitoreo continuo
- **`com.ce-simple.protection.plist`**: Configuración de launchd para persistencia

### Validators
- **`root-structure-validator.sh`**: Protege la raíz del proyecto, auto-mueve archivos incorrectos
- **`file-size-validator.sh`**: Detecta violaciones de 80 líneas, sugiere factorización
- **`standards-validator.sh`**: Valida compliance con estándares de proyecto

### Management Scripts
- **`install.sh`**: Instala y configura el sistema completo
- **`uninstall.sh`**: Remueve el servicio preservando logs

## 🔧 Management Commands

```bash
# Check service status
launchctl list | grep com.ce-simple.protection

# View live logs
tail -f .fswatch/logs/protection.log

# View violations
tail -f .fswatch/logs/violations.log

# Stop service temporarily
launchctl unload ~/Library/LaunchAgents/com.ce-simple.protection.plist

# Start service
launchctl load ~/Library/LaunchAgents/com.ce-simple.protection.plist

# Complete removal
./.fswatch/uninstall.sh
```

## 📊 Monitoring & Logs

### Log Files
- **`protection.log`**: Actividad principal del Guardian
- **`violations.log`**: Registro de violaciones detectadas
- **`daemon-output.log`**: Output del daemon
- **`daemon-error.log`**: Errores del daemon

### Guardian Actions
- 🛡️ **Guardian active**: Sistema funcionando
- ⚠️ **Violation detected**: Problema encontrado
- ✅ **Corrected**: Acción correctiva aplicada

## 🎯 Auto-Remediation

### Root Protection
Archivos detectados en root son automáticamente movidos:
- `*REPORT*` → `context/archive/processing_reports/`
- `*VALIDATION*` → `context/archive/processing_reports/`
- `*.md` → `context/archive/`
- `*.log` → `.fswatch/logs/`

### File Size Violations
Archivos >80 líneas en directories específicos generan notificaciones para factorización manual.

### Standards Enforcement
Valida:
- Authority chains en archivos arquitectónicos
- Enforcement vocabulary density
- Content duplication indicators

## 🚨 Troubleshooting

### Service Not Starting
```bash
# Check system logs
tail -f .fswatch/logs/daemon-error.log

# Verify fswatch installation
which fswatch

# Test manually
./.fswatch/protection-daemon.sh
```

### High CPU Usage
El daemon usa ~150MB RAM y CPU mínima en estado normal. Si hay problemas:
```bash
# Check excluded directories
grep -E "exclude|git" .fswatch/protection-daemon.sh

# Verify fswatch is not monitoring unnecessary files
lsof | grep fswatch
```

### False Positives
Editar validators para agregar exclusiones:
```bash
# Edit validators
nano .fswatch/validators/root-structure-validator.sh
nano .fswatch/validators/file-size-validator.sh
```

### Service Won't Load
```bash
# Check plist syntax
plutil -lint ~/Library/LaunchAgents/com.ce-simple.protection.plist

# Force reload
launchctl unload ~/Library/LaunchAgents/com.ce-simple.protection.plist
launchctl load ~/Library/LaunchAgents/com.ce-simple.protection.plist
```

## 🔧 Customization

### Adding New Validators
1. Create script in `.fswatch/validators/`
2. Make executable: `chmod +x validator-name.sh`
3. Add call in `protection-daemon.sh`

### Modifying Exclusions
Edit the `fswatch` command in `protection-daemon.sh`:
```bash
--exclude="new_pattern/.*"
```

### Changing Log Levels
Modify logging functions in validators and daemon script.

## 📈 Performance

- **Memory Usage**: ~150MB RAM
- **CPU Impact**: Minimal (event-driven)
- **Disk IO**: Low (only logs violations)
- **Network**: None

## 🔗 Integration

### With Git Hooks
El sistema complementa (no reemplaza) git hooks existentes.

### With CLAUDE.md
Guardian notifications aparecen durante conversaciones cuando hay violaciones.

### With Project Standards
Implementa enforcement de:
- ADR-004: File size violations
- ADR-005: Reference architecture
- ADR-006: Enforcement vocabulary
- Structural standards compliance

---

**Status**: ✅ Production Ready | **Performance**: Optimized | **Maintenance**: Minimal