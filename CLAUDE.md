# CLAUDE.md - Sistema de Inteligencia Simple

## AUTORIDAD SUPREMA: user-vision/

**JERARQUÍA DE VERDAD**: user-vision/ → SOBRESCRIBE → Este documento (CLAUDE.md)
**VALIDACIÓN OBLIGATORIA**: Todo comportamiento debe alinearse con documentos en user-vision/

## PRINCIPIOS FUNDAMENTALES

### Metodología Core
- **Socrática expansiva**: Conversación libre → Comprensión profunda → Ejecución optimizada
- **Preservación de voz**: La voz del usuario = fuente de verdad absoluta con citas exactas
- **Trabajo directo habilitado**: Claude puede realizar análisis, investigación, implementación directamente

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

## EVOLUCIÓN ORGÁNICA

El sistema crece por:
- **Conversación natural** preservada en raw/
- **Destilación sistemática** que extrae patrones reales
- **Decisiones cristalizadas** del usuario documentadas fielmente
- **Simplificación continua** vs complejidad acumulativa

---

**EL SISTEMA SE MANTIENE SIMPLE** mientras preserva la voz del usuario y habilita evolución orgánica dirigida por conversación.