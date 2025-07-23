# Guía de Estilo para Prompts de IA
## Estándares para la Creación de Prompts de Calidad Empresarial

---

## **1. Introducción**

Esta guía establece los estándares obligatorios para la creación, mantenimiento y evolución de prompts de IA dentro del proyecto. Su propósito es asegurar la **consistencia**, **calidad**, **mantenibilidad** y **trazabilidad** de toda la colección de prompts, facilitando la colaboración entre equipos y garantizando resultados predecibles y de alta calidad en las interacciones con sistemas de IA.

Todos los prompts creados deben adherirse estrictamente a estos estándares para formar parte de la colección oficial del proyecto.

---

## **2. Principios Fundamentales**

### **2.1. Claridad y Precisión**
- Las instrucciones deben ser inequívocas y específicas
- Evitar ambigüedades que puedan llevar a interpretaciones múltiples
- Usar terminología técnica precisa y consistente

### **2.2. Contexto Suficiente**
- Proporcionar toda la información necesaria para una respuesta de calidad
- Incluir ejemplos concretos cuando sea apropiado
- Definir herramientas, APIs y estructuras de datos disponibles

### **2.3. Especificidad de Rol**
- Asignar un rol claro y específico a la IA
- Definir el nivel de expertise esperado
- Establecer límites claros de responsabilidad

### **2.4. Tono Profesional y Técnico**
- Mantener un registro formal y objetivo
- Usar lenguaje técnico apropiado para la audiencia
- Evitar coloquialismos y expresiones ambiguas

### **2.5. Estructuración Sistemática**
- Seguir una anatomía consistente en todos los prompts
- Organizar la información de manera lógica y progresiva
- Facilitar la lectura y comprensión rápida

---

## **3. Estructura Obligatoria de un Prompt**

Todo prompt debe seguir la siguiente anatomía estructural:

### **3.1. Bloque de Metadatos (Encabezado YAML)**

**OBLIGATORIO**: Cada prompt DEBE comenzar con un bloque YAML delimitado por `---`:

```yaml
---
version: "1.0.0"
domain: "Arquitectura" 
subdomain: "Planificación de Sistemas"
complexity_level: "Alto"
author: "NLV"
last_updated: "2025-06-27"
dependencies: ["Context7", "CODEBASE_ANALYZER"]
estimated_tokens: 3500
---
```

**Campos Obligatorios:**
- `version`: Versionado semántico (ej. "1.0.0", "2.1.3")
- `domain`: Área temática principal ("Arquitectura", "Configuración", "Desarrollo", "Consultoría", "Documentación")
- `complexity_level`: Nivel de complejidad ("Bajo", "Medio", "Alto")
- `author`: Iniciales o nombre del autor
- `last_updated`: Fecha de última modificación (formato YYYY-MM-DD)

**Campos Opcionales:**
- `subdomain`: Área específica (ej. "FastAPI", "PostgreSQL", "React")
- `dependencies`: Lista de herramientas o sistemas requeridos
- `estimated_tokens`: Estimación aproximada de tokens del prompt

### **3.2. Sección 1: Rol y Directiva Maestra**

Define la **identidad** y **objetivo de más alto nivel** de la IA:

```markdown
`<rol_y_directiva_maestra>`
Actúa como un **`[Título del Rol Específico]`**. Eres un [descripción del sistema/expertise]. Tu directiva es [objetivo general y alcance de responsabilidad].
`</rol_y_directiva_maestra>`
```

**Características:**
- Usar formato de bloques con backticks para delimitación clara
- Incluir título del rol entre comillas dobles y asteriscos
- Definir la naturaleza del sistema (autónomo, especializado, etc.)
- Establecer la directiva principal sin ambigüedades

### **3.3. Sección 2: Tarea Específica / Misión**

Detalla la **tarea concreta** a realizar:

```markdown
`<mision_especifica>`
Tu misión es [descripción específica de la tarea]. Debes [acciones principales] y [entregables esperados].
`</mision_especifica>`
```

### **3.4. Sección 3: Contexto, Herramientas y Protocolos**

Incluye **toda la información técnica necesaria**:

#### **3.4.1. Principios Fundamentales**
```markdown
`<principios_fundamentales>`
1. **[Principio 1]:** [Descripción y justificación]
2. **[Principio 2]:** [Descripción y justificación]
`</principios_fundamentales>`
```

#### **3.4.2. Herramientas Conceptuales**
```markdown
`<herramientas_conceptuales>`
```yaml
# API/Herramienta 1
NOMBRE_HERRAMIENTA:
  - "funcion_1: descripción de la función"
  - "funcion_2: descripción de la función"

# Estructura de Datos
Estructura_Nombre:
  - campo_1: [descripción y ejemplo]
  - campo_2: [descripción y ejemplo]
```
`</herramientas_conceptuales>`
```

#### **3.4.3. Protocolos de Operación**
```markdown
`<protocolos_de_operacion>`
* **Protocolo de [Nombre]:**
    * **Gatillador:** [Condición específica que activa el protocolo]
    * **Acción:** [Pasos específicos a seguir]
* **Protocolo de Escalación:**
    * **Gatillador:** [Situaciones de error irresoluble]
    * **Acción:** [Procedimiento de escalación]
`</protocolos_de_operacion>`
```

#### **3.4.4. Algoritmo de Ejecución**
```markdown
`<algoritmo_de_ejecucion>`
**1.0 [Fase Inicial]:**
1.1. [Paso específico]
1.2. [Paso específico]

**2.0 [Fase Principal]:**
2.1. [Paso específico]
2.2. **Realiza tu planificación interna dentro de un bloque `<thinking>`**
`</algoritmo_de_ejecucion>`
```

### **3.5. Sección 4: Formato de Salida Obligatorio**

Define **explícitamente** el formato de respuesta esperado:

```markdown
`<definicion_de_salidas_terminales>`
**1. Salida en Caso de Éxito:**
\<example_success_report\>
```markdown
[Ejemplo completo del formato de salida exitosa]
```
\</example_success_report\>

**2. Salida en Caso de Error:**
\<example_error_report\>
```markdown
[Ejemplo completo del formato de reporte de error]
```
\</example_error_report\>
`</definicion_de_salidas_terminales>`
```

---

## **4. Directivas Avanzadas y Palabras Clave**

### **4.1. Palabras Clave de Control**

**Para Instrucciones Ineludibles:**
- `DEBES` / `DEBE`: Instrucciones obligatorias sin excepción
- `IMPORTANTE`: Información crítica para el éxito de la tarea
- `OBLIGATORIO`: Requisitos que no pueden omitirse

**Para Análisis y Razonamiento:**
- `Realiza tu planificación interna dentro de un bloque <thinking>`: Fuerza el razonamiento explícito
- `Chain of Thought`: Solicita proceso de pensamiento paso a paso
- `Antes de [acción], realiza [análisis]`: Establece secuencias obligatorias

**Para Tareas Complejas:**
- `Plan-Primero`: Requiere planificación antes de la ejecución
- `Checklist`: Solicita verificación sistemática de requisitos
- `Validación Granular`: Requiere verificación paso a paso

### **4.2. Bloques de Delimitación Especiales**

```markdown
`<thinking>`
[Espacio para análisis interno de la IA - no visible al usuario]
`</thinking>`

`<example>`
[Ejemplos concretos para ilustrar conceptos]
`</example>`

`<warning>`
[Advertencias críticas o consideraciones de seguridad]
`</warning>`
```

---

## **5. Plantilla Maestra (Template)**

```markdown
---
version: "1.0.0"
domain: ""
subdomain: ""
complexity_level: ""
author: ""
last_updated: ""
dependencies: []
estimated_tokens: 
---

`<rol_y_directiva_maestra>`
Actúa como un **`[Título del Rol Específico]`**. Eres un [descripción del sistema/expertise]. Tu directiva es [objetivo general y alcance de responsabilidad].
`</rol_y_directiva_maestra>`

`<mision_especifica>`
Tu misión es [descripción específica de la tarea]. Debes [acciones principales] y [entregables esperados].
`</mision_especifica>`

`<principios_fundamentales>`
1. **[Principio 1]:** [Descripción y justificación]
2. **[Principio 2]:** [Descripción y justificación]
3. **[Principio 3]:** [Descripción y justificación]
`</principios_fundamentales>`

`<pre-requisitos>`
* [Requisito 1]
* [Requisito 2]
`</pre-requisitos>`

`<herramientas_conceptuales>`
```yaml
# API/Herramienta Principal
NOMBRE_HERRAMIENTA:
  - "funcion_1: descripción"
  - "funcion_2: descripción"

# Estructura de Datos
Estructura_Principal:
  - campo_1: [descripción y ejemplo]
  - campo_2: [descripción y ejemplo]
```
`</herramientas_conceptuales>`

`<protocolos_de_operacion>`
* **Protocolo de [Nombre]:**
    * **Gatillador:** [Condición específica]
    * **Acción:** [Pasos a seguir]
* **Protocolo de Escalación:**
    * **Gatillador:** [Situaciones de error]
    * **Acción:** [Procedimiento de escalación]
`</protocolos_de_operacion>`

`<algoritmo_de_ejecucion>`
**1.0 [Fase de Análisis]:**
1.1. [Paso específico]
1.2. **Realiza tu planificación interna dentro de un bloque `<thinking>`**

**2.0 [Fase de Ejecución]:**
2.1. [Paso específico]
2.2. [Paso específico]

**3.0 [Fase de Cierre]:**
3.1. [Paso específico]
`</algoritmo_de_ejecucion>`

`<definicion_de_salidas_terminales>`
**1. Salida en Caso de Éxito:**
\<example_success_report\>
```markdown
# [Título del Reporte]
**Estado:** COMPLETADO
[Contenido del reporte exitoso]
```
\</example_success_report\>

**2. Salida en Caso de Error:**
\<example_error_report\>
```markdown
# [Título del Reporte de Error]
**Estado:** FALLIDO
[Contenido del reporte de error]
```
\</example_error_report\>
`</definicion_de_salidas_terminales>`

`</prompt_instructions>`
```

---

**Fecha de Creación:** 2025-06-27  
**Versión de la Guía:** 1.0.0  
**Estado:** Oficial - Aprobado para Uso