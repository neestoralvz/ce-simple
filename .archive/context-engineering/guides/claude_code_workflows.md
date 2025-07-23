# Flujos de Trabajo con Claude Code - Guía Práctica

Esta guía presenta flujos de trabajo esenciales para maximizar el potencial de Claude Code en tus proyectos de desarrollo.

## Comprender nuevos códigos base

### Obtener una visión general rápida

**Escenario:** Acabas de unirte a un proyecto y necesitas entender su estructura.

**Pasos:**
1. **Navega al directorio raíz del proyecto**
   ```bash
   cd /path/to/project
   ```

2. **Inicia Claude Code**
   ```bash
   claude
   ```

3. **Solicita una visión general**
   ```
   > dame una visión general de este código base
   ```

4. **Profundiza en componentes específicos**
   ```
   > explica los patrones de arquitectura principales
   > ¿cuáles son los modelos de datos clave?
   > ¿cómo se maneja la autenticación?
   ```

**Consejos prácticos:**
- Comienza con preguntas amplias, luego específicas
- Pregunta sobre convenciones y patrones del proyecto
- Solicita un glosario de términos específicos

### Localizar código relevante

**Escenario:** Necesitas encontrar código relacionado con una funcionalidad específica.

**Pasos:**
1. **Solicita archivos relevantes**
   ```
   > encuentra los archivos que manejan la autenticación de usuarios
   ```

2. **Obtén contexto sobre interacciones**
   ```
   > ¿cómo funcionan juntos estos archivos de autenticación?
   ```

3. **Comprende el flujo de ejecución**
   ```
   > rastrea el proceso de login desde frontend hasta base de datos
   ```

**Consejos prácticos:**
- Sé específico sobre lo que buscas
- Usa el lenguaje técnico del proyecto

## Solucionar errores eficientemente

**Escenario:** Has encontrado un error y necesitas identificar y corregir su origen.

**Pasos:**
1. **Comparte el error con Claude**
   ```
   > estoy viendo un error cuando ejecuto npm test
   ```

2. **Solicita recomendaciones de solución**
   ```
   > sugiere formas de corregir el @ts-ignore en user.ts
   ```

3. **Aplica la corrección**
   ```
   > actualiza user.ts para agregar la verificación null que sugeriste
   ```

**Consejos prácticos:**
- Menciona el comando para reproducir el error
- Describe los pasos para reproducir el problema
- Indica si el error es intermitente o consistente

## Refactorizar código

**Escenario:** Necesitas actualizar código legacy a patrones modernos.

**Pasos:**
1. **Identifica código legacy**
   ```
   > encuentra el uso de APIs obsoletas en nuestro código base
   ```

2. **Obtén recomendaciones de refactorización**
   ```
   > sugiere cómo refactorizar utils.js para usar características modernas de JavaScript
   ```

3. **Aplica cambios de forma segura**
   ```
   > refactoriza utils.js para usar características ES2024 manteniendo el mismo comportamiento
   ```

4. **Verifica la refactorización**
   ```
   > ejecuta las pruebas para el código refactorizado
   ```

**Consejos prácticos:**
- Solicita explicaciones sobre los beneficios del enfoque moderno
- Mantén compatibilidad hacia atrás cuando sea necesario
- Refactoriza en incrementos pequeños y verificables

## Trabajar con pruebas

**Escenario:** Necesitas agregar pruebas para código sin cobertura.

**Pasos:**
1. **Identifica código sin pruebas**
   ```
   > encuentra funciones en NotificationsService.swift sin cobertura de pruebas
   ```

2. **Genera estructura de pruebas**
   ```
   > agrega pruebas para el servicio de notificaciones
   ```

3. **Añade casos de prueba significativos**
   ```
   > agrega casos de prueba para condiciones límite en el servicio de notificaciones
   ```

4. **Ejecuta y verifica pruebas**
   ```
   > ejecuta las nuevas pruebas y corrige cualquier falla
   ```

**Consejos prácticos:**
- Solicita pruebas que cubran casos límite y condiciones de error
- Pide tanto pruebas unitarias como de integración cuando sea apropiado
- Haz que Claude explique la estrategia de pruebas

## Crear pull requests

**Escenario:** Necesitas crear un pull request bien documentado.

**Pasos:**
1. **Resume tus cambios**
   ```
   > resume los cambios que hice al módulo de autenticación
   ```

2. **Genera un PR con Claude**
   ```
   > crear un pr
   ```

3. **Revisa y refina**
   ```
   > mejora la descripción del PR con más contexto sobre las mejoras de seguridad
   ```

4. **Añade detalles de pruebas**
   ```
   > agrega información sobre cómo se probaron estos cambios
   ```

**Consejos prácticos:**
- Pide directamente a Claude que cree un PR
- Revisa el PR generado antes de enviarlo
- Solicita que destaque riesgos potenciales o consideraciones

## Manejar documentación

**Escenario:** Necesitas agregar o actualizar documentación para tu código.

**Pasos:**
1. **Identifica código sin documentar**
   ```
   > encuentra funciones sin comentarios JSDoc apropiados en el módulo auth
   ```

2. **Genera documentación**
   ```
   > agrega comentarios JSDoc a las funciones sin documentar en auth.js
   ```

3. **Revisa y mejora**
   ```
   > mejora la documentación generada con más contexto y ejemplos
   ```

4. **Verifica documentación**
   ```
   > verifica si la documentación sigue nuestros estándares del proyecto
   ```

**Consejos prácticos:**
- Especifica el estilo de documentación que deseas (JSDoc, docstrings, etc.)
- Solicita ejemplos en la documentación
- Pide documentación para APIs públicas, interfaces y lógica compleja

## Trabajar con imágenes

**Escenario:** Necesitas trabajar con imágenes en tu código base y quieres ayuda de Claude para analizar contenido visual.

**Métodos para agregar imágenes:**
1. Arrastra y suelta una imagen en la ventana de Claude Code
2. Copia una imagen y pégala en la CLI con Ctrl+V
3. Proporciona una ruta de imagen a Claude: "Analiza esta imagen: /ruta/a/tu/imagen.png"

**Ejemplos de análisis:**
```
> ¿Qué muestra esta imagen?
> Describe los elementos de UI en esta captura de pantalla
> ¿Hay elementos problemáticos en este diagrama?
> Aquí hay una captura del error. ¿Qué lo está causando?
> Genera CSS para coincidir con este diseño mockup
```

**Consejos prácticos:**
- Usa imágenes cuando las descripciones de texto serían poco claras
- Incluye capturas de pantalla de errores, diseños UI o diagramas para mejor contexto
- Puedes trabajar con múltiples imágenes en una conversación

## Referenciar archivos y directorios

Usa `@` para incluir rápidamente archivos o directorios sin esperar a que Claude los lea.

**Ejemplos:**
```
> Explica la lógica en @src/utils/auth.js
> ¿Cuál es la estructura de @src/components?
> Muéstrame los datos de @github:repos/owner/repo/issues
```

**Consejos prácticos:**
- Las rutas pueden ser relativas o absolutas
- Las referencias de archivo agregan CLAUDE.md al contexto
- Las referencias de directorio muestran listados, no contenidos
- Puedes referenciar múltiples archivos en un solo mensaje

## Usar pensamiento extendido

**Escenario:** Trabajas en decisiones arquitectónicas complejas, errores desafiantes o planificación de implementaciones que requieren razonamiento profundo.

**Cuándo usar:**
- Planificar cambios arquitectónicos complejos
- Depurar problemas intrincados
- Crear planes de implementación para nuevas características
- Entender códigos base complejos
- Evaluar compensaciones entre diferentes enfoques

**Niveles de profundidad:**
- `"piensa"` → pensamiento extendido básico
- `"piensa más"`, `"piensa mucho"`, `"piensa más profundo"` → pensamiento más profundo

**Ejemplo:**
```
> Necesito implementar un nuevo sistema de autenticación usando OAuth2 para nuestra API. Piensa profundamente sobre el mejor enfoque para implementar esto en nuestro código base.
```

## Reanudar conversaciones previas

Claude Code ofrece dos opciones para reanudar conversaciones:

**Continuar la conversación más reciente:**
```bash
claude --continue
```

**Mostrar selector de conversaciones:**
```bash
claude --resume
```

**En modo no interactivo:**
```bash
claude --continue --print "Continúa con mi tarea"
```

**Características:**
- El historial se almacena localmente
- Se restaura todo el contexto anterior
- Se preserva el uso de herramientas y resultados

## Ejecutar sesiones paralelas con Git worktrees

**Escenario:** Necesitas trabajar en múltiples tareas simultáneamente con aislamiento completo de código.

**Pasos:**
1. **Crear un nuevo worktree**
   ```bash
   git worktree add ../project-feature-a -b feature-a
   ```

2. **Ejecutar Claude Code en cada worktree**
   ```bash
   cd ../project-feature-a
   claude
   ```

3. **Gestionar worktrees**
   ```bash
   git worktree list
   git worktree remove ../project-feature-a
   ```

**Beneficios:**
- Cada worktree tiene estado de archivos independiente
- Cambios en un worktree no afectan otros
- Perfecto para sesiones paralelas de Claude Code

## Usar Claude como utilidad estilo Unix

### Integrar en scripts de verificación

**Ejemplo en package.json:**
```json
{
  "scripts": {
    "lint:claude": "claude -p 'eres un linter. revisa los cambios vs. main y reporta problemas relacionados con errores tipográficos. reporta nombre de archivo y número de línea en una línea, y descripción del problema en la segunda línea.'"
  }
}
```

### Usar pipes para procesamiento de datos

```bash
cat build-error.txt | claude -p 'explica concisamente la causa raíz de este error de compilación' > output.txt
```

### Controlar formato de salida

**Formatos disponibles:**
- `--output-format text` (por defecto): solo respuesta de texto
- `--output-format json`: array JSON de mensajes con metadatos
- `--output-format stream-json`: objetos JSON en tiempo real

```bash
cat code.py | claude -p 'analiza este código por errores' --output-format json > analysis.json
```

## Crear comandos slash personalizados

### Comandos específicos del proyecto

**Crear directorio de comandos:**
```bash
mkdir -p .claude/commands
```

**Crear comando:**
```bash
echo "Analiza el rendimiento de este código y sugiere tres optimizaciones específicas:" > .claude/commands/optimize.md
```

**Usar comando:**
```
> /optimize
```

### Comandos con argumentos

**Crear comando con marcador \$ARGUMENTS:**
```bash
echo "Encuentra y corrige el issue #\$ARGUMENTS siguiendo estos pasos: 1. Entiende el issue 2. Localiza el código relevante 3. Implementa solución 4. Agrega pruebas 5. Prepara descripción de PR" > .claude/commands/fix-issue.md
```

**Usar con argumentos:**
```
> /fix-issue 123
```

### Comandos personales

**Crear en directorio home:**
```bash
mkdir -p ~/.claude/commands
echo "Revisa este código por vulnerabilidades de seguridad, enfocándote en:" > ~/.claude/commands/security-review.md
```

**Características:**
- Comandos personales muestran "(user)" en la descripción
- Solo disponibles para ti, no compartidos con el equipo
- Funcionan en todos tus proyectos

---

## Recursos adicionales

- **Documentación completa:** https://docs.anthropic.com
- **Documentación de prompting:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- **Soporte:** https://support.anthropic.com
- **Implementación de referencia:** https://github.com/anthropics/claude-code/tree/main/.devcontainer