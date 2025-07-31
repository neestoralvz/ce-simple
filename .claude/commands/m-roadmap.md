# m-roadmap - Intelligent Dashboard Updates

**31/07/2025 00:00 CDMX** | Complete automated roadmap synchronization system

Sincroniza automáticamente el ROADMAP_REGISTRY.md con el estado real del proyecto, analizando progreso de work items, estado de issues, métricas de violaciones y dependencias.

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → m-roadmap implements systematic dashboard synchronization per user vision

## Objetivos:
- Sincronizar automáticamente con GitHub issues (estado, títulos, nuevos issues)
- Analizar progreso real de work items basado en cambios del repositorio
- Actualizar contadores de violaciones y métricas de progreso
- Detectar desbloqueos automáticos basados en progreso real
- Mantener todas las tablas y secciones del dashboard actualizadas
- **NUEVO**: Sincronizar dashboard modular en @context/roadmap/dashboard/

## Funcionalidades principales:

### 1. Sincronización GitHub Issues
- Obtener estado actual de todos los issues (OPEN/CLOSED)
- Detectar nuevos issues creados desde última actualización
- Actualizar títulos si han cambiado
- Mantener categorización existente (Critical, Work-Specific, Independent, etc.)

### 2. Análisis de Work Items
- Detectar work items completados por validación de archivos
- Calcular progreso real basado en commits y cambios
- Identificar cuándo work items pasan de BLOCKED a READY
- Actualizar porcentajes de progreso con datos reales

### 3. Validación de Violaciones
- Ejecutar analyze_violations.sh para obtener métricas actuales
- Actualizar contadores de violaciones restantes
- Calcular progreso de P0B-CLEANUP basado en violaciones reales
- Identificar cuándo P0B está listo para completarse

### 4. Análisis de Dependencias
- Actualizar estado de bloqueos basado en progreso real
- Identificar work items que pueden desbloquearse
- Detectar nuevas oportunidades de paralelización
- Mantener lógica de ejecución sequencial/paralela

### 5. Sincronización Dashboard Modular
- Actualizar work-items-registry.md con progreso actual de work items
- Sincronizar critical-issues-registry.md con estado de GitHub issues
- Actualizar next-actions-registry.md con próximas prioridades basadas en dependencias
- Validar consistencia entre dashboard principal y modular

## Flujo de ejecución:
1. **Backup**: Crear respaldo del dashboard actual y archivos modulares
2. **GitHub Sync**: Sincronizar con issues remotos
3. **File Analysis**: Analizar estado de archivos y violaciones
4. **Progress Calculation**: Calcular progreso real de work items
5. **Dependency Update**: Actualizar bloqueos y dependencias
6. **Dashboard Generation**: Generar nuevo ROADMAP_REGISTRY.md
7. **Modular Dashboard Sync**: Actualizar archivos del dashboard modular
8. **Change Report**: Reportar cambios y nuevos estados (incluye dashboard modular)
9. **Validation**: Validar integridad de dashboard principal y modular

## IMPLEMENTATION STATUS ✅

### Script Implementation
- **Location**: `scripts/roadmap-update.sh`
- **Status**: Fully implemented and enhanced
- **Version**: 2.0 with comprehensive automation

### Usage:
```bash
# Run from project root
./scripts/roadmap-update.sh

# Get help
./scripts/roadmap-update.sh --help
```

### Output Files:
- **Updated Dashboard**: `@context/roadmap/ROADMAP_REGISTRY.md`
- **Backup**: `@context/roadmap/backups/ROADMAP_REGISTRY_[timestamp].md`
- **Update Report**: `@context/roadmap/last_update_report.md`
- **Modular Dashboard**: `@context/roadmap/dashboard/work-items-registry.md`
- **Modular Dashboard**: `@context/roadmap/dashboard/critical-issues-registry.md`
- **Modular Dashboard**: `@context/roadmap/dashboard/next-actions-registry.md`