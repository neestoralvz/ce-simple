# Universal Orchestrator Rules - Especificaciones

## 🎯 Propósito Documental

Este documento especifica las reglas universales que deben seguir todos los orquestadores del sistema, como documentación para desarrolladores y arquitectos.

## 📋 Especificaciones de Reglas Universales

### Principios Fundamentales
- Los orquestadores coordinan, no ejecutan directamente
- Delegación a agentes especializados
- Cumplimiento de límites cognitivos (max 4 targets)
- Verificación matemática obligatoria

### Reglas de Coordinación
- Despliegue jerárquico dinámico
- Comunicación protocolar estricta
- Autocontención de referencias
- Notificación en formato compacto

### Patrones de Implementación
- Task() para despliegue de componentes
- Validación antes de ejecución
- Handoff automático en 90% contexto
- Evolución continua del sistema

## 🔗 Referencias Internas

- [Communication Protocols](../communication/protocol.md)
- [System Management](../system-management/cognitive-limits.md)
- [Implementation Protocols](../implementation/agent-execution.md)

## 📊 Notas de Implementación

Esta es la **especificación documental** de las reglas. La implementación ejecutable se encuentra en `components/protocols/` siguiendo la arquitectura dual autocontenida.

---

*Documento de especificación - Parte del sistema documental autocontenido*