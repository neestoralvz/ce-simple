---
description: "Genera documentación completa y actualizada del proyecto"
allowedTools: ["Read", "Write", "Grep", "Bash", "Glob"]
extendedThinking: true
---

# Generación de Documentación

Genera documentación completa y actualizada para el proyecto, incluyendo API docs, README, guías de desarrollo y arquitectura.

**Tipo de documentación**: $ARGUMENTS (api|readme|guides|all)

## Fase 1: Análisis del Proyecto

### Estructura del Proyecto
Identificar componentes principales:

@package.json
@tsconfig.json
@src/
@docs/

### Tecnologías y Frameworks
Detectar stack tecnológico para adaptar la documentación:
- Framework principal (React, Vue, Angular, etc.)
- Backend (Express, FastAPI, Spring, etc.)
- Base de datos utilizada
- Herramientas de build y testing

## Fase 2: Documentación de API

### Extracción de Endpoints
!find . -name "*.js" -o -name "*.ts" -o -name "*.py" | grep -E "(route|api|controller)" | head -10

### Generar API Documentation
```markdown
# API Documentation

## Base URL
\`\`\`
Production: https://api.example.com/v1
Staging: https://staging-api.example.com/v1
Development: http://localhost:3000/api/v1
\`\`\`

## Authentication
\`\`\`http
Authorization: Bearer <token>
\`\`\`

## Endpoints

### Users
#### GET /users
Retrieve all users with pagination.

**Parameters:**
- \`page\` (integer, optional): Page number (default: 1)
- \`limit\` (integer, optional): Items per page (default: 20)
- \`search\` (string, optional): Search term

**Response:**
\`\`\`json
{
  "data": [
    {
      "id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "created_at": "2024-01-01T00:00:00Z"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 5,
    "total_items": 100
  }
}
\`\`\`

#### POST /users
Create a new user.

**Request Body:**
\`\`\`json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "securepassword"
}
\`\`\`

**Response:**
\`\`\`json
{
  "id": 1,
  "name": "John Doe", 
  "email": "john@example.com",
  "created_at": "2024-01-01T00:00:00Z"
}
\`\`\`

### Error Responses
\`\`\`json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [
      {
        "field": "email",
        "message": "Email is required"
      }
    ]
  }
}
\`\`\`
```

### OpenAPI/Swagger Documentation
Si el proyecto usa Swagger/OpenAPI, generar documentación automática:

!if [ -f "swagger.json" ] || [ -f "openapi.json" ]; then
  echo "📋 Generando documentación desde OpenAPI spec..."
fi

## Fase 3: README Completo

### README.md Principal
```markdown
# Nombre del Proyecto

Descripción breve y clara del proyecto, qué problema resuelve y por qué es útil.

## 🚀 Quick Start

\`\`\`bash
# Clonar repositorio
git clone https://github.com/usuario/proyecto.git
cd proyecto

# Instalar dependencias
npm install

# Configurar environment
cp .env.example .env

# Iniciar desarrollo
npm run dev
\`\`\`

## 📋 Requisitos

- Node.js >= 18.0.0
- npm >= 9.0.0
- PostgreSQL >= 14
- Redis >= 6.0

## 🛠️ Instalación

### Desarrollo Local

1. **Clonar y configurar**
   \`\`\`bash
   git clone https://github.com/usuario/proyecto.git
   cd proyecto
   npm install
   \`\`\`

2. **Base de datos**
   \`\`\`bash
   # Iniciar PostgreSQL
   docker-compose up -d postgres
   
   # Ejecutar migraciones
   npm run db:migrate
   
   # Cargar datos de prueba
   npm run db:seed
   \`\`\`

3. **Variables de entorno**
   \`\`\`bash
   cp .env.example .env
   # Editar .env con tus configuraciones
   \`\`\`

4. **Iniciar aplicación**
   \`\`\`bash
   npm run dev
   \`\`\`

### Deployment con Docker

\`\`\`bash
# Build imagen
docker build -t proyecto .

# Ejecutar con docker-compose
docker-compose up -d
\`\`\`

## 🏗️ Arquitectura

### Stack Tecnológico
- **Frontend**: React 18 + TypeScript + Vite
- **Backend**: Node.js + Express + TypeScript
- **Base de datos**: PostgreSQL + Prisma ORM
- **Cache**: Redis
- **Testing**: Jest + React Testing Library
- **CI/CD**: GitHub Actions

### Estructura de Directorios
\`\`\`
src/
├── components/         # Componentes React reutilizables
├── pages/             # Páginas de la aplicación
├── hooks/             # Custom hooks
├── services/          # API calls y servicios
├── store/             # Estado global (Redux/Zustand)
├── utils/             # Funciones utilitarias
├── types/             # Definiciones TypeScript
└── tests/             # Tests y utilities
\`\`\`

## 📚 Documentación

- [📖 Guía de Desarrollo](docs/development.md)
- [🔧 API Documentation](docs/api.md)
- [🏛️ Arquitectura](docs/architecture.md)
- [🧪 Testing](docs/testing.md)
- [🚀 Deployment](docs/deployment.md)

## 🧪 Testing

\`\`\`bash
# Tests unitarios
npm run test

# Tests con coverage
npm run test:coverage

# Tests e2e
npm run test:e2e

# Linting
npm run lint

# Type checking
npm run type-check
\`\`\`

## 🚀 Scripts Disponibles

\`\`\`bash
npm run dev          # Desarrollo local
npm run build        # Build de producción
npm run start        # Iniciar aplicación built
npm run test         # Ejecutar tests
npm run lint         # Linting y formateo
npm run db:migrate   # Ejecutar migraciones DB
npm run db:seed      # Cargar datos de prueba
\`\`\`

## 🤝 Contribución

1. Fork el proyecto
2. Crear branch para feature (\`git checkout -b feature/AmazingFeature\`)
3. Commit cambios (\`git commit -m 'Add: AmazingFeature'\`)
4. Push al branch (\`git push origin feature/AmazingFeature\`)
5. Abrir Pull Request

### Convenciones

- **Commits**: Usar [Conventional Commits](https://conventionalcommits.org/)
- **Branches**: \`feature/\`, \`bugfix/\`, \`hotfix/\`
- **Code Style**: ESLint + Prettier configurados

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

## 👥 Equipo

- **Maintainer**: [@usuario](https://github.com/usuario)
- **Contributors**: [Ver todos](https://github.com/usuario/proyecto/contributors)

## 🔗 Links Útiles

- [Demo Live](https://proyecto.vercel.app)
- [Documentación Completa](https://docs.proyecto.com)
- [Issues](https://github.com/usuario/proyecto/issues)
- [Releases](https://github.com/usuario/proyecto/releases)
```

## Fase 4: Guías de Desarrollo

### Development Guide
```markdown
# Guía de Desarrollo

## Setup del Entorno

### Herramientas Recomendadas
- **Editor**: VS Code con extensiones recomendadas
- **Terminal**: iTerm2 (Mac) / Windows Terminal
- **Git GUI**: GitHub Desktop o GitKraken
- **Database**: TablePlus o pgAdmin

### Extensiones VS Code
\`\`\`json
{
  "recommendations": [
    "esbenp.prettier-vscode",
    "bradlc.vscode-tailwindcss",
    "ms-vscode.vscode-typescript-next",
    "bradlc.vscode-tailwindcss",
    "prisma.prisma"
  ]
}
\`\`\`

## Workflow de Desarrollo

### 1. Configuración Inicial
\`\`\`bash
# Instalar dependencies globales
npm install -g @commitlint/cli husky

# Setup hooks
npm run prepare
\`\`\`

### 2. Crear Nueva Feature
\`\`\`bash
# Crear branch desde main
git checkout main
git pull origin main
git checkout -b feature/nueva-funcionalidad

# Desarrollar y hacer commits frecuentes
git add .
git commit -m "feat: agregar nueva funcionalidad"

# Push y crear PR
git push -u origin feature/nueva-funcionalidad
\`\`\`

### 3. Code Review Process
1. Abrir PR con template completo
2. Asignar reviewers apropiados
3. Pasar todas las validaciones CI
4. Resolver comentarios de review
5. Merge después de aprobación

## Convenciones de Código

### TypeScript
- Usar interfaces para objetos
- Evitar \`any\`, usar tipos específicos
- Preferir \`const\` sobre \`let\`
- Usar optional chaining cuando corresponda

### React
- Componentes funcionales con hooks
- Props tipadas con interfaces
- Usar memo() para optimización cuando necesario
- Custom hooks para lógica reutilizable

### CSS/Styling
- Tailwind CSS para styling
- CSS Modules para estilos específicos
- Variables CSS para theming
- Mobile-first responsive design

### Testing
- Tests unitarios para toda lógica de negocio
- Tests de integración para flujos críticos
- Mocks para APIs externas
- Snapshots solo cuando necesario

## Debugging

### Herramientas de Debug
\`\`\`javascript
// Debug en desarrollo
console.log('Debug info:', data);

// React DevTools
// Redux DevTools
// Network tab para API calls
\`\`\`

### Logs en Producción
\`\`\`javascript
// Usar logger estructurado
import { logger } from '@/utils/logger';

logger.info('User action', { userId, action });
logger.error('API Error', { error, context });
\`\`\`

## Performance

### Optimizaciones React
- Lazy loading de componentes
- Code splitting por rutas
- Memoización de cálculos costosos
- Virtualización para listas largas

### Bundle Optimization
\`\`\`bash
# Analizar bundle size
npm run build:analyze

# Tree shaking verification
npm run bundle:tree-shake
\`\`\`

## Troubleshooting

### Problemas Comunes
1. **Node modules corruptos**: \`rm -rf node_modules && npm install\`
2. **Cache de build**: \`npm run clean && npm run build\`
3. **TypeScript errors**: \`npm run type-check\`
4. **Linting issues**: \`npm run lint:fix\`
```

## Fase 5: Documentación de Arquitectura

### Architecture Documentation
```markdown
# Arquitectura del Sistema

## Overview

El sistema está diseñado como una aplicación web moderna con arquitectura de capas separando claramente frontend, backend y datos.

## Diagramas de Arquitectura

### Arquitectura de Alto Nivel
\`\`\`
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Backend       │    │   Database      │
│   (React)       │◄──►│   (Node.js)     │◄──►│   (PostgreSQL)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   CDN/Static    │    │   Redis Cache   │    │   File Storage  │
│   Assets        │    │                 │    │   (S3/Local)    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
\`\`\`

### Flujo de Datos
\`\`\`
User Action → Frontend → API Call → Backend → Database → Response → Frontend → UI Update
\`\`\`

## Componentes Principales

### Frontend (React + TypeScript)
- **Responsabilidad**: Interfaz de usuario e interacciones
- **Tecnologías**: React 18, TypeScript, Tailwind CSS
- **Patrones**: Component composition, Custom hooks, State management

### Backend (Node.js + Express)
- **Responsabilidad**: API REST, lógica de negocio, autenticación
- **Tecnologías**: Express, TypeScript, Prisma ORM
- **Patrones**: Layered architecture, Dependency injection, Middleware

### Base de Datos (PostgreSQL)
- **Responsabilidad**: Persistencia de datos, integridad referencial
- **Tecnologías**: PostgreSQL 14+, Prisma migrations
- **Patrones**: Normalized schema, Indexes optimization

### Cache (Redis)
- **Responsabilidad**: Cache de sesiones, datos frecuentes
- **Tecnologías**: Redis 6+
- **Patrones**: Cache-aside, Write-through

## Patrones de Diseño

### Frontend Patterns
- **Container/Presenter**: Separación de lógica y presentación
- **Custom Hooks**: Reutilización de lógica stateful
- **Compound Components**: Componentes complejos modulares

### Backend Patterns
- **Repository Pattern**: Abstracción de acceso a datos
- **Service Layer**: Lógica de negocio centralizada
- **Middleware Pattern**: Cross-cutting concerns

### Data Patterns
- **Active Record**: Con Prisma ORM
- **Unit of Work**: Transacciones coordinadas
- **Query Object**: Queries complejas encapsuladas

## Seguridad

### Autenticación y Autorización
- JWT tokens para autenticación
- Role-based access control (RBAC)
- Rate limiting en endpoints críticos
- Input validation y sanitization

### Datos Sensibles
- Encriptación de passwords con bcrypt
- Variables de entorno para secrets
- HTTPS en producción
- SQL injection prevention con ORM

## Escalabilidad

### Horizontal Scaling
- Stateless backend design
- Load balancer ready
- Database connection pooling
- CDN para assets estáticos

### Performance Optimizations
- Database indexing strategy
- Query optimization con Prisma
- Frontend code splitting
- Image optimization y lazy loading

## Monitoreo y Observabilidad

### Logging
- Structured logging con Winston
- Log levels apropiados
- Error tracking con Sentry
- Performance metrics

### Metrics
- Response time monitoring
- Error rate tracking
- Database performance
- User behavior analytics

## Deployment Architecture

### Environments
- **Development**: Local con Docker Compose
- **Staging**: Cloud deployment con CI/CD
- **Production**: Multi-region deployment

### Infrastructure
\`\`\`
┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   CDN           │
│   (nginx/AWS)   │    │   (CloudFront)  │
└─────────┬───────┘    └─────────────────┘
          │
    ┌─────▼─────┐
    │   App     │
    │ Instances │
    └─────┬─────┘
          │
    ┌─────▼─────┐    ┌─────────────────┐
    │ Database  │    │   Redis         │
    │ (RDS)     │    │   (ElastiCache) │
    └───────────┘    └─────────────────┘
\`\`\`

## API Design

### RESTful Principles
- Resource-based URLs
- HTTP methods apropiados
- Status codes consistentes
- JSON response format

### API Versioning
- URL path versioning (/api/v1/)
- Backward compatibility
- Deprecation strategy
- Documentation versionada

## Próximas Mejoras

### Short Term
- [ ] Implementar real-time features con WebSockets
- [ ] Mejorar cache strategy
- [ ] Agregar más tests de integración

### Long Term
- [ ] Microservices migration
- [ ] GraphQL API
- [ ] Event-driven architecture
- [ ] Machine learning integration
```

## Implementación

### Checklist de Documentación
- [ ] README.md actualizado
- [ ] API documentation generada
- [ ] Guías de desarrollo escritas
- [ ] Documentación de arquitectura
- [ ] Ejemplos de código incluidos
- [ ] Screenshots y diagramas agregados
- [ ] Links internos verificados
- [ ] Documentación versionada

### Mantenimiento de Docs
- Actualizar con cada release major
- Revisar links y ejemplos regularmente
- Solicitar feedback del equipo
- Mantener sincronización con código actual