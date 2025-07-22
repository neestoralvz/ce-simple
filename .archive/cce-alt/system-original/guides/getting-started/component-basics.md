# Component Basics - Fundamentos de Componentes

## 🎯 INTRODUCCIÓN A LOS COMPONENTES

**Propósito**: Guía introductoria que explica los fundamentos del sistema de componentes, diseñada para usuarios que comienzan con el ecosistema inteligente.

### ¿Qué son los Componentes?
Los componentes son unidades especializadas de funcionalidad que trabajan juntas para formar un ecosistema inteligente. Hay 88 componentes en total, organizados en 3 tipos principales.

## 📋 TIPOS DE COMPONENTES

### 🚀 Agentes (46 componentes)
**Función**: Ejecutan tareas específicas directamente
**Características**:
- Acceso a TODAS las herramientas de Claude Code
- Especialización por protocolo, no por herramienta
- Ejecución directa de operaciones

```markdown
Ejemplo de Agente:
🚀 [L2:Agent] file-operations
├── Puede usar: Read, Write, Edit, Bash, LS, Glob, Grep
├── Especialización: Protocolos de manipulación de archivos
└── Propósito: Operaciones del sistema de archivos
```

### 🎭 Orquestadores (20 componentes)
**Función**: Coordinan otros componentes sin ejecutar directamente
**Características**:
- Coordinar máximo 4 componentes a la vez
- Delegar toda ejecución a agentes
- Gestión jerárquica ilimitada

```markdown
Ejemplo de Orquestador:
🎭 [L1:Orch] quality-assurance
├── Coordina: file-operations, quality-verification, standards-auditor
├── No ejecuta: Delega todo a los agentes
└── Propósito: Coordinación de calidad
```

### 📊 Comportamientos (22 componentes)
**Función**: Protocolos reutilizables aplicables a otros componentes
**Características**:
- Se aplican a agentes y orquestadores
- Mejoran operaciones existentes
- Reutilizables en múltiples contextos

```markdown
Ejemplo de Comportamiento:
📊 [L2:Behav] mathematical-verification
├── Aplica a: Cualquier componente que genere métricas
├── Mejora: Añade verificación matemática automática
└── Propósito: Garantizar precisión matemática
```

## 🚀 CONCEPTOS FUNDAMENTALES

### Jerarquía del Sistema
```
L0: Orchestrator-Zero (Coordinador Maestro)
 ↓
L1: Orquestadores de Dominio (máx 4)
 ↓  
L2: Agentes Especializados (máx 4 por orquestador)
```

### Límites Cognitivos
- **Máximo 4 targets**: Cada orquestador coordina máximo 4 componentes
- **Contexto 70%**: Rango operacional óptimo
- **Handoff 90%**: Transferencia automática cuando sea necesario

### Verificación Matemática
Todas las operaciones deben ser verificadas matemáticamente:
```markdown
📊 [LX:TYPE] MathVer | Tool: [herramienta] → [resultado] | Metric: [valor] | State: [VÁLIDO/INVÁLIDO]
```

## 🎭 COMPONENTES ESENCIALES PARA EMPEZAR

### 6 Agentes Básicos (Debes Conocer)
```markdown
1. file-operations → Operaciones de archivos
2. data-analysis → Análisis y verificación matemática
3. pattern-search → Búsqueda y descubrimiento
4. web-intelligence → Investigación web  
5. system-control → Control del sistema
6. quality-verification → Verificación de calidad
```

### 4 Orquestadores Clave
```markdown
1. zero-unified-complete → Coordinación maestra
2. quality-assurance → Gestión de calidad
3. documentation-coordination → Gestión de documentación
4. exploration-intelligence → Coordinación de investigación
```

### 6 Comportamientos Críticos
```markdown
1. coherence-system-unified → Mantenimiento de coherencia
2. mathematical-verification-system-unified → Verificación matemática
3. component-evolution → Auto-mejora de componentes
4. emergency-response → Gestión de emergencias
5. context-tracking → Optimización de contexto
6. parallel-operations → Ejecución paralela
```

## 🔧 CÓMO USAR COMPONENTES

### Sintaxis Básica de Despliegue
```markdown
Task("ruta/del/componente", "descripción de la tarea")

Ejemplos:
Task("components/agents/file-operations", "Validar estructura de archivos")
Task("components/orchestrators/quality-assurance", "Coordinar calidad")
```

### Patrones de Uso Simples

#### Tarea Simple (1-2 Componentes)
```markdown
Problema: "Verificar que un archivo existe"
Solución: 
🚀 Deploy file-operations → Verificación directa
```

#### Tarea Media (3-5 Componentes)
```markdown
Problema: "Validar la calidad de varios archivos"
Solución:
🎭 Deploy quality-assurance → 
├── file-operations (verificar existencia)
├── cross-reference-validator (verificar enlaces)
└── quality-verification (validar calidad)
```

#### Tarea Compleja (6+ Componentes)
```markdown
Problema: "Análisis completo del sistema"  
Solución:
🎭 Deploy zero-unified-complete →
├── L1: quality-assurance (4 agentes)
├── L1: exploration-intelligence (4 agentes)
└── L1: documentation-coordination (4 agentes)
```

## 📊 VERIFICACIÓN Y CALIDAD

### Cómo Leer Notificaciones
```markdown
📊 [L1:Quality] Deploy | agents:3 | mission:validation | State: ACTIVE

Desglose:
├── L1 → Nivel jerárquico (L1 = orquestador)
├── Quality → Tipo de componente
├── Deploy → Acción realizada
├── agents:3 → 3 agentes desplegados
├── mission:validation → Propósito
└── State: ACTIVE → Estado actual
```

### Verificación Matemática Básica
```markdown
📊 [L2:Agent] MathVer | Tool: Read → success | Files: 5 | State: VALID

Interpretación:
├── Herramienta usada: Read
├── Resultado: success (éxito)
├── Métrica: 5 archivos procesados
└── Estado: VALID (verificado matemáticamente)
```

## 🎯 PRIMEROS PASOS RECOMENDADOS

### Secuencia de Aprendizaje
1. **Familiarízate** con los 6 agentes básicos
2. **Practica** despliegue de agentes individuales
3. **Aprende** coordinación con orquestadores simples
4. **Experimenta** con comportamientos aplicados
5. **Domina** patrones de uso comunes

### Ejercicios Prácticos
```markdown
Ejercicio 1: Deploy file-operations para leer un archivo
Ejercicio 2: Use quality-assurance para validar varios archivos
Ejercicio 3: Apply mathematical-verification behavior
Ejercicio 4: Coordinate parallel-operations con múltiples agentes
```

## 🔗 Próximos Pasos

Una vez domines estos fundamentos:
- [First Steps](./first-steps.md) - Primeros pasos prácticos (próximamente)
- [Common Patterns](./common-patterns.md) - Patrones de uso comunes (próximamente)
- [Advanced Playbook](../advanced/component-playbook.md) - Guía completa avanzada

---

*Fundamentos esenciales para comenzar con el sistema de componentes del ecosistema inteligente*