# Comandos Técnicos

Nivel final de condensación. Comandos implementables de Claude Code que materializan los patrones identificados.

## Propósito

Transformar patrones abstractos en herramientas técnicas concretas que preservan y ejecutan la visión original del usuario.

## Proceso de Creación

1. **Análisis de Patrón**: Identificar elementos automatizables
2. **Diseño de Interfaz**: Cómo el usuario interactuará con el comando
3. **Implementación Técnica**: Código que ejecuta el patrón
4. **Validación de Fidelidad**: Verificar que mantiene la intención original

## Formato de Archivos

Nomenclatura: `[nombre-comando].md`

Ejemplo: `narrative-capture.md`

## Estructura Estándar

```markdown
# /[nombre-comando]

## Origen del Comando
- **Patrón Fuente**: [link a archivo pattern]
- **Síntesis Base**: [link a archivo synthesis] 
- **Narrativa Original**: [link a archivo raw]

## Propósito
[qué hace este comando y por qué existe]

## Uso

### Sintaxis
```
/[nombre-comando] [parámetros]
```

### Parámetros
- `[param1]`: [descripción]
- `[param2]`: [descripción]

### Ejemplos
```
/[nombre-comando] ejemplo1
/[nombre-comando] ejemplo2 --opcion
```

## Comportamiento

### Lo Que Hace
[descripción detallada del funcionamiento]

### Flujo de Ejecución
1. [paso 1]
2. [paso 2]
3. [paso n]

### Salidas Generadas
- [archivo/resultado 1]: [descripción]
- [archivo/resultado 2]: [descripción]

## Implementación Técnica

### Herramientas Utilizadas
[qué herramientas de Claude Code usa]

### Archivos Modificados/Creados
[qué archivos toca el comando]

### Dependencias
[otros comandos o sistemas necesarios]

## Preservación de Visión

### Elementos de la Narrativa Original
[cómo el comando mantiene la intención original]

### Validaciones Incluidas
[verificaciones para mantener fidelidad]

### Puntos de Consulta al Usuario
[cuándo y por qué consultar al usuario]

## Evolución y Mejora

### Métricas de Éxito
[cómo medir si el comando cumple su propósito]

### Posibles Extensiones
[cómo podría evolucionar]

### Retroalimentación
[cómo capturar feedback para mejorar]

## Conexiones
[relación con otros comandos del sistema]
```

## Principios de Implementación

1. **Fidelidad a la Visión**: El comando debe ejecutar la intención original
2. **Usabilidad Intuitiva**: Interfaz que refleja el pensamiento natural del usuario
3. **Automatización Inteligente**: Automatizar sin eliminar control humano necesario
4. **Evolución Orgánica**: Capacidad de adaptarse basado en uso real