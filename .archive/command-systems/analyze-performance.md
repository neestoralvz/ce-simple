# Comando: /analyze-performance

> **Ubicación:** `.claude/commands/analyze-performance.md`

Analiza el rendimiento del sistema usando profilers especializados que identifican bottlenecks y oportunidades de optimización

## PROTOCOLO DE EJECUCIÓN

### FASE 1: CONFIGURACIÓN DE ANÁLISIS

DEFINIR parámetros de performance:
- Métricas objetivo (latencia, throughput, memoria)
- Entorno de análisis (desarrollo, staging, producción)
- Carga esperada (usuarios concurrentes, RPS)
- SLAs/SLOs actuales si existen

### FASE 2: DESPLIEGUE DE PROFILERS ESPECIALIZADOS

DESPLEGAR 6 SUBAGENTES PROFILERS EN PARALELO:

```bash
# USAR TASK TOOL PARA EJECUCIÓN PARALELA

TASK 1 - ⚡ Profiler de Backend:
MEDIR:
- Tiempo de respuesta por endpoint
- Queries de base de datos lentas
- CPU y memoria por proceso
- I/O operations (disk, network)
ANALIZAR:
- Hot paths en el código
- N+1 queries
- Memory leaks
- Blocking operations
IDENTIFICAR:
- Funciones que consumen más CPU
- Endpoints más lentos
- Queries sin índices
ENTREGAR: Perfil detallado con flamegraphs

TASK 2 - 🎨 Profiler de Frontend:
EVALUAR:
- First Contentful Paint (FCP)
- Largest Contentful Paint (LCP)
- Time to Interactive (TTI)
- Cumulative Layout Shift (CLS)
ANALIZAR:
- Bundle size y tree shaking
- Render performance
- JavaScript execution time
- Network waterfall
DETECTAR:
- Componentes que re-renderizan excesivamente
- Assets no optimizados
- Third-party scripts bloqueantes
ENTREGAR: Lighthouse report + recomendaciones

TASK 3 - 🗄️ Profiler de Base de Datos:
EXAMINAR:
- Query execution plans
- Índices faltantes o no utilizados
- Lock contention
- Connection pool usage
MEDIR:
- Queries más lentas (top 20)
- Tablas más grandes sin particionamiento
- Cache hit ratio
- Transacciones largas
OPTIMIZAR:
- Sugerir índices necesarios
- Identificar queries para optimizar
- Recomendar particionamiento
ENTREGAR: Plan de optimización de DB

TASK 4 - 🔄 Profiler de Caché:
ANALIZAR:
- Hit/miss ratio por tipo de cache
- TTL configuration
- Cache invalidation patterns
- Memory usage
EVALUAR:
- Redis/Memcached performance
- CDN cache effectiveness
- Browser cache headers
- Application-level caching
IDENTIFICAR:
- Datos no cacheados que deberían
- Over-caching (datos stale)
- Cache stampede risks
ENTREGAR: Estrategia de caching mejorada

TASK 5 - 🌐 Profiler de Red:
MEDIR:
- Latencia entre servicios
- Bandwidth usage
- Connection pooling
- DNS lookup time
ANALIZAR:
- API payload sizes
- Compression usage
- Keep-alive connections
- HTTP/2 adoption
DETECTAR:
- Chatty APIs (muchas llamadas pequeñas)
- Missing compression
- Inefficient protocols
ENTREGAR: Optimizaciones de red

TASK 6 - 📊 Profiler de Infraestructura:
MONITOREAR:
- CPU usage por servicio
- Memory patterns
- Disk I/O
- Container/VM metrics
EVALUAR:
- Auto-scaling configuration
- Resource limits
- Load balancer health
- Service mesh overhead
IDENTIFICAR:
- Over/under provisioning
- Resource contention
- Inefficient deployments
ENTREGAR: Recomendaciones de infra

# EJECUTAR TODAS LAS TASKS SIMULTÁNEAMENTE
```

### FASE 3: SÍNTESIS Y PRIORIZACIÓN

CONSOLIDAR métricas y generar plan de acción:

```markdown
## ⚡ ANÁLISIS DE PERFORMANCE COMPLETO

### Resumen Ejecutivo
- **Performance Score**: [X]/100
- **P95 Latencia**: [XXXms]
- **Throughput**: [XXXX RPS]
- **Principales Bottlenecks**: [top 3]

### 📊 Métricas Clave

#### Backend Performance
| Métrica | Actual | Target | Status |
|---------|--------|--------|--------|
| P50 Latencia | 45ms | 50ms | ✅ |
| P95 Latencia | 320ms | 200ms | ❌ |
| P99 Latencia | 890ms | 500ms | ❌ |
| CPU Usage | 78% | 70% | ⚠️ |
| Memory Usage | 3.2GB | 4GB | ✅ |

#### Frontend Performance
| Métrica | Desktop | Mobile | Target |
|---------|---------|---------|--------|
| LCP | 2.1s | 4.2s | <2.5s |
| FID | 45ms | 120ms | <100ms |
| CLS | 0.05 | 0.12 | <0.1 |
| TTI | 3.4s | 6.8s | <3.8s |

### 🔥 Top Bottlenecks Identificados

#### 1. Queries N+1 en API de usuarios
- **Impacto**: +200ms en P95
- **Ubicación**: `services/user/getProfile.js`
- **Solución**:
  ```javascript
  // Actual (N+1)
  const users = await User.findAll();
  for (const user of users) {
    user.posts = await Post.findByUserId(user.id);
  }
  
  // Optimizado
  const users = await User.findAll({
    include: [{
      model: Post,
      as: 'posts'
    }]
  });
  ```

#### 2. Bundle JavaScript demasiado grande
- **Impacto**: +2s en TTI mobile
- **Tamaño actual**: 1.2MB (350KB gzipped)
- **Solución**:
  - Code splitting por ruta
  - Lazy loading de componentes pesados
  - Tree shaking de lodash
  - Eliminar moment.js por date-fns

#### 3. Falta de índices en queries frecuentes
- **Impacto**: +150ms en queries de búsqueda
- **Queries afectadas**: 5 queries principales
- **Solución**:
  ```sql
  -- Índices recomendados
  CREATE INDEX idx_users_email_active ON users(email, active);
  CREATE INDEX idx_posts_user_created ON posts(user_id, created_at DESC);
  CREATE INDEX idx_orders_status_date ON orders(status, order_date);
  ```

### 🗄️ Optimizaciones de Base de Datos
[Síntesis del profiler de DB]

#### Queries Más Lentas
1. **getUserDashboardData**: 890ms avg
   - Missing index on analytics table
   - Suggestion: Materialized view

2. **searchProducts**: 450ms avg
   - Full table scan
   - Suggestion: Full-text search index

#### Plan de Índices
```sql
-- Prioridad Alta
CREATE INDEX CONCURRENTLY idx_analytics_user_date 
ON analytics(user_id, created_date) 
WHERE deleted_at IS NULL;

-- Prioridad Media
CREATE INDEX idx_products_search 
ON products USING gin(to_tsvector('english', name || ' ' || description));
```

### 🔄 Estrategia de Caching
[Síntesis del profiler de caché]

#### Cache Hit Ratios Actuales
- Redis: 67% (objetivo: 85%)
- CDN: 45% (objetivo: 70%)
- Browser: 23% (objetivo: 60%)

#### Mejoras Recomendadas
1. **Redis**:
   - Aumentar TTL para datos de usuario: 5min → 15min
   - Implementar cache warming para dashboards
   - Cache de queries agregadas

2. **CDN**:
   - Configurar cache para assets estáticos
   - Implementar cache keys inteligentes
   - Edge caching para APIs geo-distribuidas

### 🌐 Optimizaciones de Red
[Síntesis del profiler de red]
- Implementar compression Brotli (30% mejor que gzip)
- Reducir payloads de API (pagination, field selection)
- HTTP/2 push para critical resources
- Connection pooling para microservicios

### 📈 Plan de Optimización Priorizado

#### Sprint 1 (Quick Wins) - Ganancia esperada: 40%
1. [ ] Agregar índices faltantes (2h)
2. [ ] Implementar eager loading para N+1 (4h)
3. [ ] Habilitar Brotli compression (1h)
4. [ ] Aumentar cache TTLs (1h)

#### Sprint 2 (Frontend) - Ganancia esperada: 30%
1. [ ] Code splitting por rutas (8h)
2. [ ] Optimizar imágenes con next-gen formats (4h)
3. [ ] Lazy load componentes pesados (6h)
4. [ ] Implementar service worker (8h)

#### Sprint 3 (Backend) - Ganancia esperada: 25%
1. [ ] Refactorizar queries lentas (12h)
2. [ ] Implementar connection pooling (6h)
3. [ ] Optimizar serialización JSON (4h)
4. [ ] Agregar cache warming (8h)

### 🎯 Impacto Proyectado
Con todas las optimizaciones implementadas:
- P95 Latencia: 320ms → 140ms (-56%)
- LCP Mobile: 4.2s → 2.3s (-45%)
- Throughput: +65% capacidad
- Costo infra: -30% por optimización de recursos
```

### FASE 4: MONITOREO CONTINUO

ESTABLECER métricas de seguimiento:
```bash
# Configurar dashboards
mkdir -p monitoring/performance
cp [métricas] monitoring/performance/baseline.json

# Alertas automáticas
echo "[alertas]" > monitoring/alerts/performance.yaml
```

## VARIANTES DEL COMANDO

### Análisis Específico
```bash
/analyze-performance --component=api
# Solo analiza performance del API

/analyze-performance --type=frontend
# Solo métricas de frontend

/analyze-performance --env=production
# Análisis en ambiente específico
```

### Análisis Comparativo
```bash
/analyze-performance --compare-with=last-week
# Compara con período anterior

/analyze-performance --load-test
# Ejecuta con carga simulada

/analyze-performance --profile=memory
# Enfoque en memory leaks
```

## INTEGRACIÓN CON OTROS COMANDOS

Este comando es invocado por:
- **`/refactor-smart`**: Para medir impacto de refactoring
- **`/pre-deploy`**: Validar que no hay regresiones
- **`/generate-prp`**: Para features que requieren performance
- **`/scale-planning`**: Para decisiones de infraestructura

## OUTPUT EJEMPLO

```markdown
⚡ Análisis de Performance completado en 92 segundos

PROYECTO: E-commerce Platform
SCORE: 68/100 (Necesita optimización)
P95: 320ms (target: 200ms)

🔥 TOP 3 BOTTLENECKS:
1. N+1 queries en cart API (+180ms)
2. Uncompressed assets (+1.5s load)
3. No connection pooling (+80ms)

💰 ROI ESTIMADO:
- Quick wins: -40% latencia en 1 sprint
- Conversión estimada: +2.3%
- Ahorro infra: $1,200/mes

🎯 ACCIÓN RECOMENDADA:
Ejecutar `/generate-prp performance-quick-wins.md`
```

## HERRAMIENTAS COMPLEMENTARIAS

1. **APM**: NewRelic, DataDog, AppDynamics
2. **Profiling**: Chrome DevTools, pprof, flamegraphs
3. **Load Testing**: k6, JMeter, Gatling
4. **Monitoring**: Prometheus + Grafana
5. **Real User Monitoring**: Google Analytics, Sentry