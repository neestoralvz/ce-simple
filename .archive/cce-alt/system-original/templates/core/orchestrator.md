# Orchestrator Template - Especificación de Template

## 🎯 Propósito del Template

Template de documentación para la creación de orquestadores del sistema inteligente.

## 📋 Estructura del Template de Orquestador

### Secciones Obligatorias

```markdown
# [Nombre] Orchestrator

## 🎯 PURPOSE
[Descripción del propósito específico]

## 📊 COORDINATION PROTOCOL
[Protocolo de coordinación específico]

## 🚀 DEPLOYMENT STRATEGY
[Estrategia de despliegue de componentes]

## 📋 AGENT COORDINATION
[Coordinación con agentes especializados]

## 📊 MATHEMATICAL VERIFICATION
[Métricas y verificaciones requeridas]

## 🔗 INTERNAL REFERENCES
[Solo referencias dentro de components/]
```

### Patrones de Implementación

- **Coordinación jerárquica**: Max 4 targets simultáneos
- **Delegación especializada**: Task() deployment a agentes
- **Verificación matemática**: Métricas basadas en herramientas
- **Comunicación protocolar**: Formato de notificación compacto

### Reglas de Autocontención

- Solo referencias internas a `components/`
- Uso de interfaces para operaciones externas
- Información mínima necesaria en `components/shared/`

## 🔗 Referencias Internas

- [Universal Rules](../../protocols/orchestration/universal-rules.md)
- [Agent Template](./agent.md)
- [Protocol Template](./protocol.md)

---

*Template de especificación - Sistema documental autocontenido*