# Reglas de Gobernanza para Claude Code

**Estas reglas deben seguirse en todo momento.**

Documento que define principios operativos obligatorios para todas las instancias de IA, garantizando comportamiento consistente, ejecución robusta y colaboración segura en todas las tareas y servicios.

---

## Estándares de Calidad de Código

### Manejo de Errores
- **Implementa manejo estructurado de errores** con modos de falla específicos
- **Verifica precondiciones** antes de ejecutar operaciones críticas o irreversibles
- **Incluye mecanismos de timeout y cancelación** para operaciones de larga duración

### Documentación de Código
- **Cada función debe incluir un docstring** conciso y orientado al propósito
- **Verifica existencia y permisos** antes de operaciones de archivos y rutas
- **Valida entradas** antes del procesamiento crítico

### Principios de Implementación
```python
# ✅ Ejemplo correcto
def process_data(file_path: str) -> dict:
    """
    Procesa datos del archivo especificado.
    
    Args:
        file_path: Ruta al archivo de datos
        
    Returns:
        Diccionario con datos procesados
        
    Raises:
        FileNotFoundError: Si el archivo no existe
        PermissionError: Si no hay permisos de lectura
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Archivo no encontrado: {file_path}")
    
    if not os.access(file_path, os.R_OK):
        raise PermissionError(f"Sin permisos de lectura: {file_path}")
    
    # Procesamiento con timeout
    with timeout(30):
        return _process_file_content(file_path)
```

---

## Protocolos de Documentación

### Sincronización y Consistencia
- **Documentación sincronizada** con cambios de código—sin referencias obsoletas
- **Jerarquías de encabezados consistentes** en archivos Markdown
- **Snippets de código ejecutables** y probados que reflejen casos de uso reales

### Estructura Obligatoria
Cada documento debe incluir claramente:
1. **Propósito** - ¿Para qué sirve?
2. **Uso** - ¿Cómo se utiliza?
3. **Parámetros** - ¿Qué entradas requiere?
4. **Ejemplos** - Casos prácticos de implementación

### Claridad Técnica
- **Términos técnicos explicados** inline o enlazados a definición canónica
- **Ejemplos ejecutables** que funcionen sin modificaciones
- **Referencias actualizadas** sin enlaces rotos

---

## Reglas de Gestión de Tareas

### Definición de Tareas
- **Tareas claras, específicas y accionables**—evita ambigüedad
- **Asignación explícita** de agente responsable con etiqueta
- **Tareas complejas divididas** en subtareas atómicas y rastreables

### Gestión y Seguimiento
- **Sin conflictos** con comportamiento validado del sistema existente
- **Revisión obligatoria** para tareas relacionadas con seguridad
- **Actualización de estado** en archivo compartido de tareas
- **Dependencias explícitamente declaradas** entre tareas

### Escalación
**Los agentes deben escalar** tareas ambiguas, contradictorias o sin alcance definido para clarificación.

---

## Directrices de Cumplimiento de Seguridad

### Protección de Credenciales
- ❌ **Credenciales hardcodeadas estrictamente prohibidas**
- ✅ **Usar mecanismos de almacenamiento seguro**

### Validación de Entradas
```python
# ✅ Validación correcta
def validate_input(data: str) -> str:
    """Valida y sanitiza entrada de usuario."""
    if not isinstance(data, str):
        raise TypeError("Entrada debe ser string")
    
    # Sanitizar entrada
    sanitized = html.escape(data.strip())
    
    # Validar longitud
    if len(sanitized) > MAX_INPUT_LENGTH:
        raise ValueError("Entrada excede longitud máxima")
    
    return sanitized
```

### Operaciones Seguras
- **Evita eval, llamadas shell no sanitizadas** o vectores de inyección de comandos
- **Principio de menor privilegio** para operaciones de archivos y procesos
- **Log de operaciones sensibles** excluyendo valores de datos sensibles
- **Verificación de permisos** antes de acceder servicios o rutas protegidas

---

## Requisitos de Ejecución de Procesos

### Logging y Monitoreo
- **Log todas las acciones** con severidad apropiada (INFO, WARNING, ERROR)
- **Reportes de error claros** y legibles para humanos
- **Indicadores de progreso** para tareas de larga duración

### Gestión de Recursos
- **Respetar límites de recursos** del sistema (memoria, CPU)
- **Lógica de reintentos** con backoff exponencial y límites de falla
- **Checkpoints** para operaciones extensas

```python
# ✅ Ejemplo de retry con backoff
import time
from functools import wraps

def retry_with_backoff(max_retries=3, base_delay=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    delay = base_delay * (2 ** attempt)
                    logging.warning(f"Intento {attempt + 1} falló: {e}. Reintentando en {delay}s")
                    time.sleep(delay)
        return wrapper
    return decorator
```

---

## Principios Operativos Fundamentales

### Integridad de Datos
- **Nunca usar datos mock, fallback o sintéticos** en tareas de producción
- **Actuar basado en evidencia verificable**, no suposiciones
- **Decisiones rastreables** a logs, datos o archivos de configuración

### Validación y Testing
- **Lógica de manejo de errores** diseñada con principios test-first
- **Validación explícita de precondiciones** antes de operaciones destructivas o de alto impacto
- **Evidencia verificable** para todas las decisiones

---

## Principios de Filosofía de Diseño

### KISS (Keep It Simple, Stupid)
- ✅ **Soluciones directas** y fáciles de entender
- ❌ **Evita sobre-ingeniería** o abstracción innecesaria
- 🎯 **Prioriza legibilidad** y mantenibilidad del código

### YAGNI (You Aren't Gonna Need It)
- ✅ **Solo requisitos inmediatos** y entregables
- ❌ **No agregues características especulativas** a menos que sea explícitamente requerido
- 🎯 **Minimiza deuda técnica** a largo plazo

### Principios SOLID

| Principio | Descripción | Aplicación |
|-----------|-------------|------------|
| **Single Responsibility** | Cada módulo/función hace una sola cosa | Una función = un propósito claro |
| **Open-Closed** | Abierto para extensión, cerrado para modificación | Usar interfaces y herencia |
| **Liskov Substitution** | Clases derivadas sustituibles por base | Mantener contratos de interfaz |
| **Interface Segregation** | Interfaces específicas vs generales | Múltiples interfaces pequeñas |
| **Dependency Inversion** | Depender de abstracciones, no implementaciones | Inyección de dependencias |

---

## Directrices de Extensión del Sistema

### Nuevos Agentes
- **Conformidad con interfaces existentes** de logging y estructuras de tareas
- **Funciones utilitarias** probadas unitariamente y revisadas por pares
- **Cambios de configuración** reflejados en manifiesto del sistema con sellos de versión

### Compatibilidad
- **Mantener compatibilidad hacia atrás** a menos que esté justificado y documentado
- **Evaluación de impacto en rendimiento** para todos los cambios
- **Versionado adecuado** para cambios significativos

---

## Procedimientos de Aseguramiento de Calidad

### Revisión Obligatoria
**Un agente revisor debe revisar** todos los cambios que involucren:
- 🔒 Seguridad
- ⚙️ Configuración del sistema  
- 👥 Roles de agentes

### Estándares de Salida
- **Documentación revisada** por claridad, consistencia y corrección técnica
- **Salida orientada al usuario** (logs, mensajes, errores) clara, no técnica y accionable
- **Mensajes de error** que sugieran rutas de remediación o pasos diagnósticos
- **Plan de rollback** para todas las actualizaciones importantes

---

## Reglas de Testing y Simulación

### Cobertura de Testing
- **Lógica nueva incluye** pruebas unitarias y de integración
- **Datos simulados claramente marcados** y nunca promovidos a producción
- **Todas las pruebas pasan** en pipelines de integración continua
- **Cobertura de código superior** a umbrales definidos (ej. 85%)

### Gestión de Testing
```python
# ✅ Ejemplo de test structure
import unittest
from unittest.mock import patch, MagicMock

class TestProcessData(unittest.TestCase):
    def setUp(self):
        """Configuración para cada test."""
        self.test_data_path = "/tmp/test_data.json"
        self.mock_data = {"test": "data"}
    
    def test_process_valid_file(self):
        """Test con archivo válido."""
        with patch('os.path.exists', return_value=True), \
             patch('os.access', return_value=True):
            result = process_data(self.test_data_path)
            self.assertIsInstance(result, dict)
    
    def test_process_missing_file(self):
        """Test con archivo faltante."""
        with patch('os.path.exists', return_value=False):
            with self.assertRaises(FileNotFoundError):
                process_data(self.test_data_path)
    
    def tearDown(self):
        """Limpieza después de cada test."""
        # Limpiar archivos temporales
        pass
```

### Logging de Testing
- **Resultados de test** en logs separados, no logs de producción
- **Pruebas de regresión** definidas y ejecutadas para actualizaciones de alto impacto
- **Datos de test marcados** claramente para evitar confusión con producción

---

## Seguimiento de Cambios y Gobernanza

### Documentación de Cambios
- **Cambios de configuración o reglas** documentados en manifiesto del sistema y changelog
- **Registro de fuente, timestamp y justificación** al modificar assets compartidos
- **Incremento de versión interna** del sistema cuando sea aplicable

### Planes de Contingencia
- **Plan de rollback o deshacer** definido para cada cambio importante
- **Trails de auditoría preservados** para todas las operaciones que modifican tareas
- **Versionado semántico** para cambios críticos

### Ejemplo de Changelog
```markdown
## [v2.1.0] - 2024-07-09

### Agregado
- Nuevo sistema de validación de entradas
- Timeout configurable para operaciones de larga duración

### Cambiado
- Mejorado manejo de errores en processing de archivos
- Actualizada documentación de APIs

### Corregido
- Resuelto memory leak en operaciones concurrentes

### Seguridad
- Fortalecida validación de permisos de archivos
```

---

## Métricas de Cumplimiento

**Indicadores de éxito para estas reglas:**

- 🎯 **100% de funciones** con docstrings apropiados
- 🔒 **0 credenciales hardcodeadas** en codebase
- 📊 **>85% cobertura de código** en tests
- ⚡ **<5% fallos** en operaciones críticas
- 📝 **Documentación actualizada** en <24h de cambios de código
- 🔄 **Planes de rollback** para 100% de cambios mayores

**Herramientas de monitoreo recomendadas:**
- Linting automático (pylint, flake8)
- Análisis de seguridad (bandit, safety)
- Cobertura de tests (coverage.py)
- Documentación automática (sphinx, mkdocs)