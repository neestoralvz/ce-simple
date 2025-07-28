# ContextFlow - User Journeys

## Journey 1: Desarrollador + Nueva Tecnología

**Contexto**: Implementar WebRTC, sin experiencia previa

**Flow Optimizado**:
```
Usuario: "Necesito video llamadas en mi app"
ContextFlow: "¿1:1 o grupales?"
Usuario: "1:1, escalable"
ContextFlow: "¿Infraestructura actual maneja signaling real-time?"

SUGGESTED:
/explore-webrtc - Architecture options
/assess-infra - Current capabilities  
/research-signaling - Compare solutions
```

**Consolidación**: Cada comando actualiza context, sugiere próximos pasos basándose en hallazgos

**Outcome**: Implementación funcional + conocimiento transferible

---

## Journey 2: Investigador + Dataset Complejo

**Contexto**: 2M+ registros financieros, sospecha fraude

**Flow Optimizado**:
```
Usuario: "Datos financieros para analizar"
ContextFlow: "¿Patrones específicos o exploración?"
Usuario: "Posible fraude, incierto qué buscar"
ContextFlow: "¿Datos etiquetados disponibles?"

SUGGESTED:
/explore-structure - Data overview
/analyze-anomalies - Pattern detection
/detect-outliers - Statistical approach
```

**Refinamiento**: Análisis refina hipótesis, comandos especializan

**Outcome**: Metodología estructurada + herramientas reutilizables

---

## Journey 3: Equipo Greenfield

**Contexto**: Startup MVP, stack indefinido, restricciones tiempo

**Flow Optimizado**:
```
Usuario: "Decidir stack tecnológico"  
ContextFlow: "¿Prioridad: velocidad, escalabilidad, o presupuesto?"
Usuario: "Velocidad al mercado crítica"
ContextFlow: "¿Experiencia equipo en stack específico?"

ORCHESTRATED:
/assess-skills - Team capabilities
/compare-stacks - Options analysis
/estimate-velocity - Development speed
/plan-mvp - Architecture minimal
```

**Outcome**: Proyecto inicializado + convenciones + workflows optimizados

---

## Journey 4: Production Bug

**Contexto**: Error intermitente, múltiples servicios, presión tiempo

**Flow Optimizado**:
```
Usuario: "Error producción no reproducible"
ContextFlow: "¿Todos usuarios o segmentos específicos?"
Usuario: "Solo enterprise, patrones uso específicos"
ContextFlow: "¿Logs + métricas servicios disponibles?"

COORDINATED:
/analyze-patterns - Error correlation
/trace-requests - Flow analysis  
/identify-causes - Root cause
/validate-fix - Hypothesis testing
```

**Outcome**: Problema resuelto + documentación + conocimiento retenido

---

## Patrones Comunes

### Entrada Socrática
- Preguntas concisas revelan contexto
- Validación comprensión rápida
- Refinamiento iterativo objetivos

### Auto-Sugerencia
- Comandos sugieren próximos pasos lógicos
- Adaptación contexto emergente
- Escalabilidad simple → complejo

### Consolidación
- Context actualización continua
- Conocimiento densificación
- Patrones generalización reutilización