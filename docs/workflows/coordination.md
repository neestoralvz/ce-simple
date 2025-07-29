# Coordinación Entre Comandos

## Modelo de Orquestación

### Principio Fundamental
"Algo de lo que no hemos hablado y es muy importante porque es la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes"

El sistema opera bajo un modelo de orquestación donde el agente principal coordina subagentes especializados (comandos) en lugar de hacer todo directamente.

## Patrones de Coordinación

### Coordinación Secuencial
```
/start → /explore → /debug → /git → /close
```
**Caso de uso**: Resolver un problema específico del codebase
**Flujo**: Inicializar → Investigar → Solucionar → Versionar → Cerrar

### Coordinación Paralela
```
/partner (validador continuo) + /maintain (monitor de salud)
```
**Caso de uso**: Validación y mantenimiento durante cualquier operación
**Flujo**: Ejecución simultánea de validación y monitoreo

### Coordinación Condicional
```
IF (cambios sistémicos) THEN /distill → CLAUDE.md update
IF (documentación requerida) THEN /docs
IF (decisión arquitectural) THEN /partner validation
```

## Integraciones Específicas

### /git como Integrador Universal
**Coordina con**: TODOS los comandos
**Responsabilidad**: Commits inteligentes contextualizados
**Patrón**: Cualquier comando puede activar /git para versionar cambios

### /partner como Validator Continuo  
**Coordina con**: TODOS los comandos
**Responsabilidad**: Validación de decisiones arquitecturales
**Patrón**: Puede interrumpir cualquier flujo para validar simplicity/alignment

### /distill como Sistema Evolutivo
**Coordina con**: /close (captura) → procesamiento batch
**Responsabilidad**: Evolución orgánica del sistema  
**Patrón**: Procesa conversaciones acumuladas → actualiza CLAUDE.md

### /maintain como Health Monitor
**Coordina con**: TODOS los comandos
**Responsabilidad**: Salud sistémica y consistencia
**Patrón**: Monitoreo continuo + corrección preventiva

## Flujos de Comunicación

### Comunicación Explícita
Los comandos se coordinan a través de:
- **Referencias directas**: "Necesito que /git maneje este commit"
- **Estado compartido**: user-vision/ como fuente de verdad común
- **Handoff files**: Transferencia de contexto entre comandos

### Comunicación Implícita
- **Patrones establecidos**: /start siempre al inicio, /close siempre al final
- **Triggers automáticos**: Cambios sistémicos → /distill automático
- **Validaciones de fondo**: /partner validando decisiones continuamente

## Casos de Uso Comunes

### Desarrollo de Nueva Funcionalidad
```
/start → context loading
/partner → architectural validation  
/explore → codebase understanding
/docs → documentation creation
/debug → testing and refinement
/git → version control
/close → session capture
```

### Resolución de Bug
```
/start → problem identification
/explore → bug investigation  
/debug → solution implementation
/git → fix commit
/maintain → system health check
/close → resolution documentation
```

### Evolución del Sistema
```
Conversaciones acumuladas → /distill → processing
TRUTH_SOURCE.md → updated authority
CLAUDE.md → auto-regeneration
/maintain → consistency validation
/git → evolutionary commit
```

### Planificación Arquitectural
```
/start → context preparation
/partner → continuous validation
User conversation → natural planning
/docs → decision documentation  
/git → architectural commit
/close → planning capture
```

## Principios de Coordinación

### Autonomía con Colaboración
Cada comando mantiene autonomía funcional pero colabora cuando es necesario. No hay dependencias rígidas, solo coordinación inteligente.

### Contexto Compartido
user-vision/ sirve como contexto compartido que todos los comandos pueden consultar para mantener coherencia.

### Escalamiento Orgánico
La coordinación se vuelve más sofisticada orgánicamente a medida que el sistema evoluciona, sin complejidad planificada.

### Simplicidad Preservada
La coordinación nunca debe agregar complejidad innecesaria. Preferir patrones simples y explícitos sobre arquitecturas complejas.

## Anti-Patrones

### Avoid: Dependencias Rígidas
Los comandos NO deben requerir otros comandos para funcionar básicamente.

### Avoid: Coordinación Compleja
No crear sistemas de coordinación que requieran configuración compleja o metadata.

### Avoid: Estado Compartido Mutable
user-vision/ es readonly para comandos. Solo el usuario y /distill pueden modificarlo.

### Avoid: Over-Orchestration  
No sobre-orquestar. Permitir que la coordinación emerja naturalmente del uso.

---

**PRINCIPIO RECTOR**: Coordinación simple, natural y orgánica que habilita poder colectivo sin complejidad sistémica.