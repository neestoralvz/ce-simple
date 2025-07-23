# Comando: /analyze-security

> **Ubicación:** `.claude/commands/analyze-security.md`

Realiza auditoría de seguridad exhaustiva usando subagentes especializados en diferentes vectores de ataque

## PROTOCOLO DE EJECUCIÓN

### FASE 1: PREPARACIÓN DE AUDITORÍA

ESTABLECER alcance de seguridad:
- Nivel de profundidad (básico, estándar, penetración)
- Compliance requerido (OWASP, PCI DSS, GDPR)
- Tipos de vulnerabilidades a priorizar
- Contexto del dominio (fintech, salud, e-commerce)

### FASE 2: DESPLIEGUE DE AUDITORES DE SEGURIDAD

DESPLEGAR 6 SUBAGENTES AUDITORES EN PARALELO:

```bash
# USAR TASK TOOL PARA EJECUCIÓN PARALELA

TASK 1 - 🔐 Auditor de Código:
ESCANEAR:
- Inyecciones (SQL, NoSQL, LDAP, Command)
- XSS (Reflected, Stored, DOM-based)
- Deserialización insegura
- Uso de componentes vulnerables
ANALIZAR:
- Funciones peligrosas (eval, exec, etc.)
- Validación de inputs
- Sanitización de outputs
- Manejo de errores que exponen info
ENTREGAR: Vulnerabilidades por archivo y línea

TASK 2 - 🔑 Auditor de Autenticación:
REVISAR:
- Implementación de auth (JWT, OAuth, Sessions)
- Fortaleza de contraseñas
- Mecanismos de 2FA/MFA
- Gestión de sesiones
EVALUAR:
- Tokens expuestos o predecibles
- Session fixation/hijacking
- Privilege escalation paths
- Account enumeration
ENTREGAR: Matriz de riesgos de auth

TASK 3 - 🗝️ Auditor de Secretos:
BUSCAR:
- API keys hardcodeadas
- Passwords en código
- Certificados embebidos
- URLs de desarrollo/staging
VERIFICAR:
- .env files commiteados
- Configuraciones inseguras
- Tokens en logs
- Secrets en frontend
ENTREGAR: Lista de secretos expuestos

TASK 4 - 📦 Auditor de Dependencias:
ANALIZAR:
- Vulnerabilidades conocidas (CVEs)
- Dependencias desactualizadas
- Licencias problemáticas
- Supply chain risks
EJECUTAR:
- npm/yarn audit
- OWASP dependency check
- License compliance check
- Transitive dependencies scan
ENTREGAR: Reporte de vulnerabilidades con CVSS

TASK 5 - 🌐 Auditor de APIs:
EXAMINAR:
- Endpoints sin autenticación
- Rate limiting ausente
- CORS mal configurado
- Exposición de datos sensibles
PROBAR:
- Mass assignment vulnerabilities
- API versioning issues
- GraphQL specific attacks
- Broken object level authorization
ENTREGAR: Mapa de superficie de ataque

TASK 6 - 🏗️ Auditor de Infraestructura:
REVISAR:
- Configuraciones de seguridad
- Permisos de archivos/directorios
- Servicios expuestos innecesariamente
- Logs y monitoreo
EVALUAR:
- Headers de seguridad HTTP
- TLS/SSL configuración
- Firewall rules
- Container security
ENTREGAR: Postura de seguridad de infra

# CRÍTICO: TODAS LAS TASKS SE EJECUTAN EN PARALELO
```

### FASE 3: CONSOLIDACIÓN Y PRIORIZACIÓN

SINTETIZAR hallazgos por severidad:

```markdown
## 🔒 REPORTE DE SEGURIDAD CONSOLIDADO

### Resumen Ejecutivo
- **Total Vulnerabilidades**: [número]
- **Críticas**: [número] 🔴
- **Altas**: [número] 🟠
- **Medias**: [número] 🟡
- **Bajas**: [número] 🟢
- **Score de Seguridad**: [X]/100

### 🔴 VULNERABILIDADES CRÍTICAS (Fix inmediato)

#### 1. [Nombre de vulnerabilidad]
- **Ubicación**: [archivo:línea]
- **Tipo**: [OWASP Top 10 category]
- **CVSS Score**: [0-10]
- **Impacto**: [descripción del riesgo]
- **Explotabilidad**: [fácil/media/difícil]
- **Fix Recomendado**:
  ```javascript
  // Código vulnerable
  [ejemplo]
  
  // Código seguro
  [ejemplo corregido]
  ```

### 🟠 VULNERABILIDADES ALTAS

[Lista similar con menos urgencia]

### 🔐 Estado de Autenticación y Autorización
[Síntesis del auditor de auth]
- **Mecanismo Principal**: [JWT/Sessions/OAuth]
- **Fortalezas**: [qué está bien]
- **Debilidades**: [qué mejorar]
- **Recomendaciones**: [acciones específicas]

### 🗝️ Gestión de Secretos
[Síntesis del auditor de secretos]
- **Secretos Expuestos**: [cantidad y tipos]
- **Configuración Actual**: [cómo se manejan]
- **Mejoras Urgentes**: [qué cambiar ya]

### 📦 Análisis de Dependencias
[Síntesis del auditor de dependencias]
| Paquete | Versión | Vulnerabilidad | Severidad | Fix |
|---------|---------|----------------|-----------|-----|
| [nombre] | [ver] | [CVE-XXXX] | Critical | Update to X.X |

### 🌐 Superficie de Ataque API
[Síntesis del auditor de APIs]
- **Endpoints Totales**: [número]
- **Sin Autenticación**: [número] ⚠️
- **Sin Rate Limiting**: [número] ⚠️
- **Datos Sensibles Expuestos**: [lista]

### 🏗️ Seguridad de Infraestructura
[Síntesis del auditor de infra]
- **Headers de Seguridad**: [score]
- **TLS**: [versión y configuración]
- **Exposición de Servicios**: [lista]

### 📊 Matriz de Riesgo
```
         IMPACTO
    Bajo   Medio   Alto
B │  🟢     🟢      🟡
a │  
j │  🟢     🟡      🟠
o │
  │  🟡     🟠      🔴
A │
l │  🟠     🔴      🔴
t │
o └─────────────────────
  PROBABILIDAD
```

### 🛡️ Plan de Remediación Priorizado

#### Fase 1: Crítico (0-7 días)
1. [Fix SQL injection en login.js]
2. [Actualizar dependencia crítica X]
3. [Implementar rate limiting]

#### Fase 2: Alto (1-2 semanas)
1. [Mejorar validación de inputs]
2. [Implementar CSP headers]
3. [Rotar todos los secretos]

#### Fase 3: Medio (1 mes)
1. [Refactorizar autenticación]
2. [Implementar logging de seguridad]
3. [Agregar tests de seguridad]

### 🔍 Herramientas Recomendadas
- **SAST**: [SonarQube/Semgrep]
- **DAST**: [OWASP ZAP/Burp Suite]
- **Dependency Scanning**: [Snyk/Dependabot]
- **Secret Scanning**: [TruffleHog/GitLeaks]
```

### FASE 4: GENERACIÓN DE ARTEFACTOS

CREAR documentación de seguridad:
```bash
# Crear reporte detallado
mkdir -p security/reports
cp [reporte] security/reports/audit-[fecha].md

# Generar checklist de seguridad
echo "[checklist]" > security/security-checklist.md

# Crear tickets/issues
# Para cada vulnerabilidad crítica/alta
```

## VARIANTES DEL COMANDO

### Auditoría Enfocada
```bash
/analyze-security --focus=authentication
# Solo analiza auth y autorización

/analyze-security --focus=dependencies
# Solo vulnerabilidades en dependencias

/analyze-security --compliance=PCI-DSS
# Auditoría específica para compliance
```

### Auditoría Continua
```bash
/analyze-security --mode=ci
# Versión ligera para CI/CD

/analyze-security --baseline=security/last-audit.json
# Compara con auditoría anterior

/analyze-security --fail-on=critical
# Falla si encuentra vulnerabilidades críticas
```

## INTEGRACIÓN CON OTROS COMANDOS

Este comando es invocado por:
- **`/create-claude`**: Para proyectos sensibles (fintech, salud)
- **`/generate-prp`**: Antes de features que manejan datos sensibles
- **`/pre-deploy`**: Como gate de seguridad antes de producción
- **`/security-review`**: En pull requests automáticamente

## OUTPUT EJEMPLO

```markdown
🔒 Auditoría de Seguridad completada en 68 segundos

PROYECTO: FinanceAI App
VULNERABILIDADES: 23 total (3 críticas, 5 altas)
SCORE: 42/100 (Necesita atención urgente)

🔴 CRÍTICAS:
1. SQL Injection en services/user.js:45
2. Hardcoded API key en config/stripe.js:12
3. No rate limiting en /api/transfer

🟠 ALTAS:
1. JWT secret débil (< 256 bits)
2. bcrypt rounds = 5 (mínimo 10)
3. CORS permite cualquier origen

⚡ ACCIÓN INMEDIATA:
Ejecutar `/generate-prp security-critical-fixes.md`
para plan de remediación urgente.
```

## MEJORES PRÁCTICAS

1. **Ejecutar regularmente**: Mínimo mensual, idealmente en cada PR
2. **Automatizar en CI/CD**: Fallar builds con vulnerabilidades críticas
3. **Tracking de métricas**: Evolución del score de seguridad
4. **Educación del equipo**: Compartir hallazgos y prevención
5. **Defense in depth**: No depender de una sola capa de seguridad