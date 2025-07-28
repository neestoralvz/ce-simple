# Sistema de Índice de Narrativas

Mantiene la trazabilidad completa entre todos los niveles de condensación y las conexiones entre narrativas.

## Propósito

Crear una red de conocimiento que permita:
- Rastrear el origen de cualquier comando hasta su narrativa original
- Identificar conexiones entre diferentes narrativas
- Facilitar la expansión lateral del conocimiento
- Mantener la integridad del sistema de destilación

## Estructura del Índice

### Archivo Principal: `master-index.json`

```json
{
  "narratives": {
    "narrative_id": {
      "metadata": {
        "title": "string",
        "date": "YYYY-MM-DD",
        "capture_method": "super_whisper|text|other",
        "status": "raw|synthesized|patterned|commandized"
      },
      "files": {
        "raw": "path/to/raw/file.md",
        "synthesis": "path/to/synthesis/file.md",
        "patterns": ["path/to/pattern1.md", "path/to/pattern2.md"],
        "commands": ["path/to/command1.md", "path/to/command2.md"]
      },
      "themes": ["theme1", "theme2", "theme3"],
      "connections": ["other_narrative_id1", "other_narrative_id2"],
      "key_concepts": ["concept1", "concept2"],
      "evolution_log": [
        {
          "date": "YYYY-MM-DD",
          "action": "created|synthesized|patterned|commandized",
          "description": "what happened"
        }
      ]
    }
  },
  "themes_index": {
    "theme_name": {
      "description": "what this theme covers",
      "narratives": ["narrative_id1", "narrative_id2"],
      "related_themes": ["related_theme1", "related_theme2"]
    }
  },
  "patterns_index": {
    "pattern_name": {
      "description": "what this pattern does",
      "source_narratives": ["narrative_id1"],
      "related_patterns": ["pattern1", "pattern2"],
      "commands_generated": ["command1", "command2"]
    }
  },
  "commands_index": {
    "command_name": {
      "description": "what this command does",
      "source_pattern": "pattern_name",
      "source_narrative": "narrative_id",
      "usage_stats": {
        "created": "YYYY-MM-DD",
        "last_used": "YYYY-MM-DD",
        "usage_count": 0
      }
    }
  }
}
```

### Archivos de Conexiones: `connections/`

Para cada narrativa, un archivo que documenta sus conexiones:
- `narrative_[id]_connections.md`

## Operaciones del Índice

### Crear Nueva Narrativa
1. Generar ID único (timestamp + hash de contenido)
2. Crear entrada en master-index.json
3. Inicializar archivo de conexiones

### Procesar Condensación
1. Actualizar status en índice
2. Agregar referencias a archivos generados
3. Identificar y documentar conexiones emergentes

### Buscar y Consultar
1. Por tema
2. Por concepto clave
3. Por conexiones
4. Por patrón o comando

### Mantener Integridad
1. Validar que todos los archivos referenciados existen
2. Verificar consistencia de conexiones bidireccionales
3. Actualizar estadísticas de uso

## Comandos de Índice

### `/narrative-index search [término]`
Buscar narrativas por término

### `/narrative-index trace [comando]`
Rastrear un comando hasta su narrativa original

### `/narrative-index connections [narrative_id]`
Mostrar conexiones de una narrativa

### `/narrative-index stats`
Estadísticas del sistema completo

## Red de Conocimiento

El índice facilita la **expansión lateral** permitiendo:
- Identificar patrones que emergen de múltiples narrativas
- Descubrir conexiones no obvias entre conceptos
- Generar ideas creativas desde las relaciones
- Construir una base de conocimiento que evoluciona orgánicamente

## Principios de Indexación

1. **Trazabilidad Completa**: Todo comando debe rastrearse a su narrativa original
2. **Conexiones Bidireccionales**: Si A se conecta con B, B se conecta con A
3. **Evolución Documentada**: Cada cambio se registra con contexto
4. **Integridad Verificable**: El sistema puede auto-validar su consistencia