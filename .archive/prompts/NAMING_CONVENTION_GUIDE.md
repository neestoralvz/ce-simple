# Guía de Convención de Nomenclatura para Prompts
## Estándares para el Nombrado de Archivos de Prompts de IA

---

### **1. Introducción**

Esta guía establece la convención de nomenclatura oficial para todos los archivos de prompts de IA dentro del proyecto. Su propósito es asegurar la **consistencia**, **organización** y **escalabilidad** de la colección de prompts, facilitando la localización, mantenimiento y evolución de los mismos.

Todos los nuevos prompts creados deben adherirse estrictamente a esta convención para ser incluidos en la colección oficial del proyecto.

---

### **2. Formato Estándar Obligatorio**

Todos los archivos de prompts DEBEN seguir el siguiente formato:

```
[dominio-abrev]_[funcion]_[complejidad]_v[version].md
```

### **2.1. Componentes del Formato**

#### **`[dominio-abrev]` - Abreviación del Dominio (Obligatorio)**
- **Longitud:** 2-4 caracteres en mayúsculas
- **Propósito:** Identifica el área temática principal del prompt
- **Beneficio:** Facilita la agrupación visual y el ordenamiento alfabético

#### **`[funcion]` - Descripción Funcional (Obligatorio)**
- **Formato:** Palabras en minúsculas separadas por guiones (`-`)
- **Propósito:** Describe específicamente la acción o entidad que maneja el prompt
- **Longitud Recomendada:** 2-4 palabras máximo
- **Ejemplos:** `planificador-sistemas`, `backend-desarrollo`, `analisis-requisitos`

#### **`[complejidad]` - Indicador de Complejidad (Obligatorio)**
- **Valores Permitidos:**
  - `L` - Bajo (Low): Prompts simples, tareas directas
  - `M` - Medio (Medium): Prompts con lógica moderada
  - `H` - Alto (High): Prompts complejos con múltiples fases
- **Propósito:** Ayuda en la selección apropiada según el nivel de experiencia requerido

#### **`v[version]` - Control de Versiones (Obligatorio)**
- **Formato:** `v` seguido de número entero (ej. `v1`, `v2`, `v3`)
- **Propósito:** Facilita el versionado y la evolución de prompts
- **Regla:** Incrementar la versión para cambios significativos en funcionalidad

---

### **3. Dominios Oficiales y Abreviaciones**

| Dominio | Abreviación | Descripción |
|---------|-------------|-------------|
| **Arquitectura** | `ARQ` | Planificación y diseño de sistemas |
| **Configuración** | `CFG` | Setup y configuración de entornos |
| **Desarrollo** | `DEV` | Implementación de código y features |
| **Consultoría** | `CON` | Análisis estratégico y requisitos |
| **Gestión de Proyectos** | `GPR` | Organización y estructura de proyectos |
| **Documentación** | `DOC` | Creación y mantenimiento de documentación |

### **3.1. Proceso para Nuevos Dominios**
Si se requiere un nuevo dominio:
1. Proponer abreviación de 2-4 caracteres
2. Verificar que no existe conflicto con dominios existentes
3. Documentar en esta guía antes de su uso
4. Actualizar la versión de esta guía

---

### **4. Reglas de Nomenclatura**

### **4.1. Reglas Obligatorias**
- ✅ **USAR** únicamente caracteres alfanuméricos, guiones (`-`) y guiones bajos (`_`)
- ✅ **USAR** formato exacto: `DOMINIO_funcion_COMPLEJIDAD_vVERSION.md`
- ✅ **USAR** abreviaciones de dominio en MAYÚSCULAS
- ✅ **USAR** funciones en minúsculas con guiones como separadores
- ✅ **USAR** complejidad en MAYÚSCULAS (L, M, H)

### **4.2. Reglas Prohibidas**
- ❌ **NO USAR** espacios en los nombres de archivo
- ❌ **NO USAR** caracteres especiales (@, #, %, etc.)
- ❌ **NO USAR** tildes o caracteres no ASCII
- ❌ **NO USAR** abreviaciones de dominio no oficiales
- ❌ **NO USAR** números en la función (usar versiones en su lugar)

---

### **5. Ejemplos de Nomenclatura Correcta**

| Nombre de Archivo | Explicación |
|------------------|-------------|
| `ARQ_planificador-sistemas_H_v1.md` | Arquitectura, planificador de sistemas, alta complejidad, versión 1 |
| `CFG_entorno-setup_M_v2.md` | Configuración, setup de entorno, complejidad media, versión 2 |
| `DEV_api-rest_H_v1.md` | Desarrollo, API REST, alta complejidad, versión 1 |
| `DOC_generador-readme_L_v1.md` | Documentación, generador de README, baja complejidad, versión 1 |

---

### **6. Proceso de Versionado**

### **6.1. Cuándo Incrementar la Versión**
- **Cambios Mayores:** Modificación significativa en la funcionalidad o estructura
- **Nuevas Capacidades:** Adición de nuevas secciones o protocolos
- **Cambios de Interfaz:** Modificación en formatos de entrada o salida
- **Refactorizaciones Importantes:** Reestructuración completa del prompt

### **6.2. Cuándo NO Incrementar la Versión**
- Correcciones menores de texto o gramática
- Ajustes en metadatos YAML (author, last_updated)
- Correcciones de formato o estilo
- Actualización de ejemplos sin cambio de lógica

---

### **7. Validación y Herramientas**

### **7.1. Lista de Verificación para Nuevos Prompts**
- [ ] ¿El nombre sigue el formato exacto `[dominio]_[funcion]_[complejidad]_v[version].md`?
- [ ] ¿La abreviación de dominio está en la lista oficial?
- [ ] ¿La función describe claramente el propósito del prompt?
- [ ] ¿El nivel de complejidad es apropiado (L/M/H)?
- [ ] ¿La versión comienza en v1 para prompts nuevos?

### **7.2. Patrón Regex para Validación**
```regex
^(ARQ|CFG|DEV|CON|GPR|DOC)_[a-z-]+_(L|M|H)_v[0-9]+\.md$
```

---

### **8. Mantenimiento de la Convención**

### **8.1. Responsabilidades**
- **Desarrolladores:** Seguir la convención al crear nuevos prompts
- **Revisores:** Verificar cumplimiento en pull requests
- **Mantenedores:** Actualizar esta guía cuando sea necesario

### **8.2. Proceso de Cambios a la Convención**
1. Proponer cambio con justificación técnica
2. Evaluar impacto en archivos existentes
3. Actualizar guía y herramientas de validación
4. Comunicar cambios al equipo
5. Migrar archivos existentes si es necesario

---

**Fecha de Creación:** 2025-06-27  
**Versión de la Guía:** 1.0.0  
**Estado:** Oficial - Aprobado para Uso  
**Próxima Revisión:** 2025-12-27