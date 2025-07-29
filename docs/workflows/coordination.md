# Coordinación Entre Comandos

## Modelo de Orquestación

### Principio Fundamental
"Algo de lo que no hemos hablado y es muy importante porque es la manera principal en la que se tiene que comportar el agente principal SIEMPRE es la de ser orquestado de subagentes"

El sistema opera bajo un modelo de orquestación donde el agente principal coordina subagentes especializados (comandos) en lugar de hacer todo directamente.

## Patrones de Coordinación

### Coordinación Secuencial
```
/workflows:start → /workflows:explore → /workflows:debug → /actions:git → /workflows:close
```
**Caso de uso**: Resolver un problema específico del codebase
**Flujo**: Inicializar → Investigar → Solucionar → Versionar → Cerrar

### Coordinación Paralela
```
/roles:partner (validador continuo) + /maintain (monitor de salud)
```
**Caso de uso**: Validación y mantenimiento durante cualquier operación
**Flujo**: Ejecución simultánea de validación y monitoreo

### Coordinación Condicional
```
IF (cambios sistémicos) THEN /workflows:distill → CLAUDE.md update
IF (documentación requerida) THEN /actions:docs
IF (decisión arquitectural) THEN /roles:partner validation
```

## Integraciones Específicas

### /actions:git como Integrador Universal
**Coordina con**: TODOS los comandos
**Responsabilidad**: Commits inteligentes contextualizados
**Patrón**: Cualquier comando puede activar /actions:git para versionar cambios

### /roles:partner como Validator Continuo  
**Coordina con**: TODOS los comandos
**Responsabilidad**: Validación de decisiones arquitecturales
**Patrón**: Puede interrumpir cualquier flujo para validar simplicity/alignment

### /workflows:distill como Sistema Evolutivo
**Coordina con**: /workflows:close (captura) → procesamiento batch
**Responsabilidad**: Evolución orgánica del sistema  
**Patrón**: Procesa conversaciones acumuladas → actualiza CLAUDE.md

### /maintain como Health Monitor
**Coordina con**: TODOS los comandos
**Responsabilidad**: Salud sistémica y consistencia
**Patrón**: Monitoreo continuo + corrección preventiva

## Flujos de Comunicación

### Comunicación Explícita
Los comandos se coordinan a través de:
- **Referencias directas**: "Necesito que /actions:git maneje este commit"
- **Estado compartido**: user-vision/ como fuente de verdad común
- **Handoff files**: Transferencia de contexto entre comandos

### Comunicación Implícita
- **Patrones establecidos**: /workflows:start siempre al inicio, /workflows:close siempre al final
- **Triggers automáticos**: Cambios sistémicos → /workflows:distill automático
- **Validaciones de fondo**: /roles:partner validando decisiones continuamente

## Casos de Uso Comunes

### Desarrollo de Nueva Funcionalidad
```
/workflows:start → context loading
/roles:partner → architectural validation  
/workflows:explore → codebase understanding
/actions:docs → documentation creation
/workflows:debug → testing and refinement
/actions:git → version control
/workflows:close → session capture
```

### Resolución de Bug
```
/workflows:start → problem identification
/workflows:explore → bug investigation  
/workflows:debug → solution implementation
/actions:git → fix commit
/maintain → system health check
/workflows:close → resolution documentation
```

### Evolución del Sistema
```
Conversaciones acumuladas → /workflows:distill → processing
TRUTH_SOURCE.md → updated authority
CLAUDE.md → auto-regeneration
/maintain → consistency validation
/actions:git → evolutionary commit
```

### Planificación Arquitectural
```
/workflows:start → context preparation
/roles:partner → continuous validation
User conversation → natural planning
/actions:docs → decision documentation  
/actions:git → architectural commit
/workflows:close → planning capture
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
user-vision/ es readonly para comandos. Solo el usuario y /workflows:distill pueden modificarlo.

### Avoid: Over-Orchestration  
No sobre-orquestar. Permitir que la coordinación emerja naturalmente del uso.

---

**PRINCIPIO RECTOR**: Coordinación simple, natural y orgánica que habilita poder colectivo sin complejidad sistémica.