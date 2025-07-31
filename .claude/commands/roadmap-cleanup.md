# Comando: /roadmap-cleanup

**Propósito**: Depuración automática de work items completados en el dashboard del roadmap

## AUTORIDAD SUPREMA
User request: "hay que hacer que al actualizarse los work items vaya depurando la lista de completados"

## FUNCIÓN PRINCIPAL
Sistema automático que detecta items completados (✅ COMPLETED) y los archiva manteniendo solo elementos activos en el dashboard para reducir cognitive load y mantener focus en trabajo pendiente.

## EJECUCIÓN

### Comando Base
```bash
# Ejecutar depuración automática
./scripts/batch-processing/roadmap-cleanup-automation.sh
```

### Funcionalidad Automática
1. **Backup Safety**: Crea backup completo antes de cualquier modificación
2. **Detección Completados**: Identifica items con status ✅ COMPLETED
3. **Archive System**: Mueve completados a `/context/roadmap/archive/by-completion-date/`
4. **Dashboard Regeneration**: Actualiza los 3 registries con solo items activos
5. **Metrics Update**: Actualiza conteos y progress percentages

### Dashboard Modules Actualizados
- **work-items-registry.md**: Solo items IN PROGRESS + READY + BLOCKED
- **critical-issues-registry.md**: Solo issues activos sin completados
- **next-actions-registry.md**: Solo acciones prioritarias ejecutables
- **ROADMAP_REGISTRY.md**: Summary actualizado con metrics de cleanup

## BENEFICIOS ACHIEVED

### Cognitive Load Reduction
- **Antes**: 35+ items (muchos completados saturando vista)
- **Después**: ~12-13 items activos (focus en trabajo pendiente)
- **Reducción**: 65% menos noise, 100% más clarity

### Focus Enhancement
- **Clear Priorities**: Inmediata visibilidad de trabajo ejecutable
- **Historical Preservation**: Completados preservados en archive system
- **Progress Tracking**: Métricas accuradas de completion vs active work

### Automated Maintenance
- **Status Detection**: Auto-detecta cambios ✅ COMPLETED
- **Archive Management**: Organización automática por fecha
- **Dashboard Sync**: Regeneración automática de registries

## ARCHIVE SYSTEM

### Estructura Organizada
```
/context/roadmap/archive/
├── by-completion-date/
│   ├── 20250731_150854/
│   │   └── completed_items_extracted.md
│   └── [timestamp]/
└── by-category/ (future)
```

### Safety Protocols
- **Complete Backup**: Backup antes de cualquier operación
- **Rollback Capability**: Restauración completa si needed
- **Audit Trail**: Log completo de todas las operaciones

## USO PRÁCTICO

### Trigger Manual
Ejecutar cuando se detecten multiple completions para cleanup batch

### Trigger Automático (Future)
Hook integration para auto-cleanup cuando items change to COMPLETED

### Integration con Git
Archive timestamps coordinan con git commits para traceability completa

---

**COMANDO DECLARATION**: Sistema de depuración automática que mantiene dashboard clean y focused mientras preserva historical completions en archive system organizado.

**NEXT EVOLUTION**: Claude hooks integration para auto-trigger cuando se detecten status changes a COMPLETED.