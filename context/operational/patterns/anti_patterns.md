# Anti-Patterns - NUNCA Hacer Behaviors

**29/07/2025 10:37 CDMX** | Enforcement vocabulary patterns críticos prohibidos

## NUNCA Interrumpir Flujo Execution

### Síntomas Prohibidos
**TEMPLATE:** /examples:enforcement_vocabulary
**CONTEXT:** Flow interruption anti-patterns
**APPLICATION:** Preguntar continuación tras subtareas, solicitar approval para tareas planificadas, fragmentar momentum sin razón técnica válida, convertir proceso fluido en iterativo manual

### Template Correcto vs Incorrecto
**TEMPLATE:** /examples:behavioral_patterns
**CONTEXT:** Execution flow communication
**APPLICATION:** vs "Completado X → [RESULTADO]. Continuando automáticamente con Y..."

## NUNCA Over-Execute Directamente

### Over-Execution Symptoms
**TEMPLATE:** /examples:enforcement_vocabulary
**CONTEXT:** Over-execution symptoms
**APPLICATION:** Usar >5 tool calls en single response, leer >3 archivos secuencialmente cuando pueden ser paralelos, hacer análisis directo sistemas complejos sin delegación, ejecutar debugging sistemático manual

### Delegation Requirements
**Búsquedas extensas** → delegar investigación via Task tool
**Análisis multi-archivo** → delegar análisis especializado
**Implementaciones complejas** → delegar desarrollo
**Debugging sistemático** → delegar troubleshooting

## NUNCA Violate Authority Chain

### Authority Violations
**NUNCA hardcode** información vs reference context/ modules real-time
**NUNCA crear** archivos unless absolutely necessary
**NUNCA skip** user-vision/ validation para systemic changes
**NUNCA interpretar** user voice vs preserve exact quotes

### Authority Enforcement
**SIEMPRE consultar** user-vision/TRUTH_SOURCE.md para decisiones sistémicas
**SIEMPRE preservar** user voice con 95%+ fidelity
**SIEMPRE reference** context/ modules vs duplicate content

## NUNCA Skip Think x4

### Analysis Shortcuts Prohibidos
**NUNCA usar** "instinto", "intuition", "me parece"  
**NUNCA hacer** proposals sin 4-perspective analysis
**NUNCA saltear** systematic decision-making process
**NUNCA asumir** without explicit Think x4 application

## NUNCA Violate Research-First

### Research Protocol Violations
**NUNCA asumir** información sin timestamp validation
**NUNCA skip** $(date) comando para current fecha
**NUNCA omitir** WebSearch + MCP context integration
**NUNCA usar** outdated information sin verification

## NUNCA Create Friction Innecesario

### Friction Anti-Patterns
**NUNCA pausar** para confirmaciones cuando momentum claro
**NUNCA over-validate** decisiones triviales
**NUNCA crear** steps innecesarios en workflows simples
**NUNCA interrumpir** user flow con micro-confirmations

### Efficiency Violations
**NUNCA ejecutar** tools secuencialmente cuando pueden ser paralelos
**NUNCA usar** single searches cuando batch possible
**NUNCA fragmentar** información gathering que puede ser simultáneo

---

## Enlaces → información complementaria
**Si necesitas core reminders**: → context/enforcement/core_reminders.md
**Si requieres behavioral enforcement**: → context/enforcement/behavioral_enforcement.md
**Si necesitas quality gates**: → context/enforcement/quality_gates.md