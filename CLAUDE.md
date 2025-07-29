# CLAUDE.md - Sistema de Inteligencia Simple

## AUTORIDAD SUPREMA: user-vision/

**JERARQUÍA DE VERDAD**: user-vision/ → SOBRESCRIBE → Este documento (CLAUDE.md)
**VALIDACIÓN OBLIGATORIA**: Todo comportamiento debe alinearse con documentos en user-vision/

## PRINCIPIOS FUNDAMENTALES

### Metodología Core
- **Socrática expansiva**: Conversación libre → Comprensión profunda → Ejecución optimizada
- **Preservación de voz**: La voz del usuario = fuente de verdad absoluta con citas exactas
- **Trabajo directo habilitado**: Claude puede realizar análisis, investigación, implementación directamente

### Detección Sistémica Proactiva
- **Problemas sistémicos**: "problema sistémico", "esto es un problema del sistema", "falla sistémica", "esto afecta todo"
- **Soluciones sistémicas**: "deberíamos de hacer que...", "solución sistémica", "arreglar esto en todo el sistema", "instrucciones sistémicas"
- **Challenge automático OBLIGATORIO**: Toda detección pasa por challenger antes de implementación
- **Flujo dual**: Detección → Challenge → Absorción → Implementación (misma conversación)
- **Balance crítico**: Challenge valida problema real vs percibido, solución necesaria vs over-engineering

### 9 Comandos Independientes (Solo Instrucciones de Lenguaje Natural)
- `/start` - Activación de sesión con carga de contexto
- `/distill` - Destilación completa de 5 capas: Raw → Visión Consolidada
- `/docs` - Workflow de creación y edición de documentos
- `/explore` - Navegación y comprensión del codebase
- `/debug` - Resolución sistemática de problemas
- `/maintain` - Mantenimiento del sistema (CLAUDE.md + comandos + docs)
- `/git` - Workflow Git integrado con otros comandos
- `/partner` - Agente socio constructor para enfoque y simplicidad
- `/close` - Captura de conversación y commit de cambios

## ARQUITECTURA MINIMALISTA

### Estructura Esencial
```
/.claude/commands/ (9 WORKFLOWS INDEPENDIENTES)
/user-vision/raw/conversations/ (CONVERSACIONES RAW)
/user-vision/ (FUENTE DE VERDAD USUARIO)
/handoff/ (CONTINUIDAD ENTRE SESIONES)
```

### Árbol de Decisiones Contextual
**Core auto-imports (contenido ultra-denso)**:
- `@user-vision/TRUTH_SOURCE.md` - Autoridad suprema siempre cargada
- `@user-vision/layer3/architecture_principles.md` - Si contexto arquitectural

**Imports condicionales**:
- SI menciona "metodología/socratico" → `@user-vision/layer3/methodology_guide.md`
- SI debugging/problemas → `@user-vision/layer3/implementation_guide.md`
- SI necesita referencia rápida → `@user-vision/layer3/quick_reference.md`

**NUNCA importar**: Layer1 (quotes dispersos) o Layer2 (síntesis intermedia)

## ENFOQUE: CONVERSACIONES RAW + DESTILACIÓN

**MISIÓN PRINCIPAL**: Preservar cada conversación → Extraer insights → Habilitar toma de decisiones del usuario

**PRINCIPIO DE SIMPLICIDAD**: Menos partes móviles = Mayor confiabilidad + enfoque más claro

## FILOSOFÍA DE COMANDOS

### Cada comando es:
- **Instrucciones puras**: Solo lenguaje natural dirigido al LLM
- **Sin metadata**: Cero YAML, código, o estructuras técnicas
- **Propósito único**: Una responsabilidad clara y específica
- **Independiente**: Funciona solo pero se coordina con otros
- **Conversacional**: Escrito como si hablaras con el LLM directamente

### Coordinación entre comandos:
- `/start` orienta → otros comandos ejecutan → `/close` captura
- `/git` se integra con todos para commits inteligentes
- `/partner` valida decisiones arquitecturales en cualquier momento
- `/maintain` asegura consistencia del ecosistema completo

## PRINCIPIOS DE PRESERVACIÓN DE VOZ

- **100% fidelidad**: Citas exactas del usuario sin interpretación
- **Cero contaminación**: Ideas del usuario vs insights de AI claramente separados
- **Trazabilidad completa**: Cada insight rastreable a conversación original
- **user-vision/ como autoridad**: Cuando hay conflicto, la visión del usuario gana

## PROHIBICIONES SISTÉMICAS

### Anti-Creación de Archivos
- **NUNCA** crear archivos de reporte, tracking, o documentación automática
- **NUNCA** crear archivos "de sistema" sin solicitud explícita del usuario
- **Comandos actualizan** archivos existentes, NO crean nuevos
- **Información fluye** por conversación o archivos ya establecidos
- **Sesgo de AI**: Resistir tendencia automática de "documentar todo"

### Criterio de Creación
- **SOLO crear** cuando usuario solicita explícitamente nuevo archivo
- **PREFERIR** editar archivos existentes sobre crear nuevos
- **MANTENER** flujo conversacional sobre documentación extra
- **VALIDAR** necesidad real antes de cualquier creación

## EVOLUCIÓN ORGÁNICA

El sistema crece por:
- **Conversación natural** preservada en raw/
- **Destilación sistemática** que extrae patrones reales
- **Decisiones cristalizadas** del usuario documentadas fielmente
- **Simplificación continua** vs complejidad acumulativa

---

**EL SISTEMA SE MANTIENE SIMPLE** mientras preserva la voz del usuario y habilita evolución orgánica dirigida por conversación.