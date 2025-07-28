---
contextflow:
  purpose: "Utility centralizada para timestamps con zona horaria Ciudad de México"
  type: "utility"
  reusable: true
---

# Timestamp Utility - Ciudad de México

## Función Core
Generar timestamps consistentes usando timezone Ciudad de México (UTC-6) via bash tools.

## Implementación Bash
```bash
# Timestamp format: YYYY-MM-DD_HH-MM
TIMESTAMP_MX=$(TZ='America/Mexico_City' date +"%Y-%m-%d_%H-%M")

# Timestamp format: YYYY-MM-DD HH:MM
TIMESTAMP_MX_READABLE=$(TZ='America/Mexico_City' date +"%Y-%m-%d %H:%M")

# Timestamp format: YYYY-MM-DD_HH-MM-SS (para archivos únicos)
TIMESTAMP_MX_PRECISE=$(TZ='America/Mexico_City' date +"%Y-%m-%d_%H-%M-%S")
```

## Uso en Commands
```markdown
# En cualquier command que necesite timestamp:
**Generar timestamp**: 
```bash
TIMESTAMP=$(TZ='America/Mexico_City' date +"%Y-%m-%d_%H-%M")
```

# Para handoffs:
```bash
HANDOFF_FILE="/handoff/${TIMESTAMP}_[tema-descriptivo].md"
```

# Para narrativas:
```bash
NARRATIVE_FILE="/narratives/raw/conversations/${TIMESTAMP}_[tema].md"
```
```

## Formatos Disponibles

### Archivos (guión bajo)
- **Standard**: `2025-07-28_22-00`
- **Precise**: `2025-07-28_22-00-45`

### Display (legible)
- **Readable**: `2025-07-28 22:00`
- **Full**: `2025-07-28 22:00:45`

## Integration Pattern
```bash
# Task tool deployment con timestamp:
Task(
  description="Generate handoff with real timestamp",
  prompt="Crear handoff usando timestamp: $(TZ='America/Mexico_City' date +'%Y-%m-%d_%H-%M')"
)
```

---

**Self-contained**: Esta utility no depende de archivos externos
**Reusable**: Disponible para todos los commands via import interno