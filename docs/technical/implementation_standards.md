# Implementation Standards - Stack Técnico y Patrones

## Derivación de Autoridad
Basado en user-vision/TRUTH_SOURCE.md: "no te voy a decir como hacer las cosas, tu debes de decidirlo de acuerdo a mi vision y lo que te digo" [L1:67]

## Stack Tecnológico Autorizado

### Lenguajes Principales
- **Bash**: Para comandos del sistema y orchestración
- **Markdown**: Para toda documentación
- **JSON**: Para configuración y data interchange
- **YAML**: Solo para configs Claude Code específicas

### Herramientas Core
- **Claude Code CLI**: Interface principal
- **Git**: Control de versiones y coordinación
- **ripgrep (rg)**: Para búsquedas en código
- **find/ls**: Para navegación de archivos

### Prohibido Usar
- Frameworks complejos (React, Vue, Angular para este proyecto)
- Bases de datos pesadas (PostgreSQL, MySQL para comandos simples)
- Microservicios architecture
- Docker containers (mantener simplicidad)

## Patrones de Implementación

### Estructura de Archivos
```
comando_name/
├── main.md           # Comando principal
├── utils.sh          # Utilidades específicas (solo si necesario)
└── README.md         # Solo si comando complejo
```

### Patrón de Comando Simple
```bash
#!/bin/bash
# Comando: nombre_comando
# Propósito: [descripción una línea]
# Autoridad: user-vision/TRUTH_SOURCE.md

# Validación entrada
# Lógica principal
# Output limpio
```

### Manejo de Paths
- **SIEMPRE** usar paths absolutos en scripts
- **SIEMPRE** validar existencia antes de usar
- **PREFERIR** relative paths en documentación

### Pattern Matching
- **USAR** ripgreg (rg) para búsquedas
- **EVITAR** grep tradicional
- **PREFERIR** glob patterns sobre find cuando sea posible

## Principios de Implementación

### Responsabilidad Única
Cada archivo/comando debe hacer UNA cosa bien. Si hace más de una cosa, dividir.

### Zero Dependencies Externas
Solo usar herramientas que ya están en el sistema o que Claude Code provee.

### Fail Fast
Validar inputs al inicio. Si algo está mal, fallar inmediatamente con mensaje claro.

### Idempotencia
Comandos deben poder ejecutarse múltiples veces sin efectos secundarios negativos.

## File Size Guidelines

### Límites Específicos
- **CLAUDE.md**: ≤200 líneas (actualmente 79)
- **Comandos individuales**: ≤100 líneas
- **Docs técnicos**: ≤150 líneas
- **user-vision/ layers**: Sin límite (preservar voz completa)

### Cuando Exceder Límites
1. Validar que realmente necesitas más líneas
2. Considerar factorización en módulos
3. Documentar razón específica en el archivo
4. Challenge automático si excede 150% del límite

## Output Standards

### Comandos Interactivos
- Output conciso, máximo 4 líneas explicativas
- Mostrar progress solo para operaciones >5 segundos
- Usar markdown formatting para legibilidad CLI

### Logs y Debug
- **NUNCA** logs automáticos a archivos
- **SOLO** output a stdout/stderr
- Debug info solo cuando explícitamente solicitado

### Error Messages
- Específicos, no genéricos
- Incluir path/línea cuando sea relevante
- Sugerir solución cuando sea obvio

## Performance Guidelines

### Token Economy
- **Conversación**: Sin restricciones (fase discovery)
- **Implementación**: Optimizar para contexto eficiente
- **Referencias**: Usar paths específicos vs cargar archivos completos

### File Operations
- Leer archivos específicos vs cargar directorios completos
- Usar grep/rg con patterns precisos
- Batch operations cuando sea posible

## Integration Patterns

### Claude Code Tools
- **Preferir** Read tool vs bash cat
- **Preferir** Glob tool vs bash find
- **Usar** Edit tool para cambios precisos
- **EVITAR** Write tool para archivos existentes

### Git Integration
- Commits descriptivos que referencien decisiones
- Branches para cambios sistémicos
- Tags para versiones estables de arquitectura

## Referencias de Autoridad
- user-vision/TRUTH_SOURCE.md líneas 109-127: Golden Authority Rule
- user-vision/TRUTH_SOURCE.md líneas 44-51: Metodología sin restricciones
- docs/core/principles.md: Simplicidad rector
- docs/maintenance/validation.md: Quality gates