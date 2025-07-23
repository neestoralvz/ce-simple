---
description: "Configura pipeline completo de CI/CD con GitHub Actions"
allowedTools: ["Write", "Read", "Bash", "Grep"]
extendedThinking: true
---

# Setup CI/CD Pipeline

Configura un pipeline completo de CI/CD adaptado al proyecto actual.

**Tipo de proyecto/framework**: $ARGUMENTS

## Fase 1: Análisis del Proyecto

### Detectar Tecnologías
Identificar el stack tecnológico del proyecto:

@package.json
@requirements.txt  
@pom.xml
@Cargo.toml
@go.mod

### Estructura Actual
Revisar configuración existente:
- Scripts en package.json
- Tests configurados
- Build tools utilizados
- Variables de entorno

## Fase 2: Configuración GitHub Actions

### Workflow de CI (Continuous Integration)
```yaml
name: CI Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [18.x, 20.x]
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: ${{ matrix.node-version }}
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run linting
      run: npm run lint
    
    - name: Run tests
      run: npm run test:coverage
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        token: ${{ secrets.CODECOV_TOKEN }}
    
    - name: Build project
      run: npm run build
    
    - name: Run E2E tests
      run: npm run test:e2e
```

### Workflow de CD (Continuous Deployment)
```yaml
name: CD Pipeline

on:
  push:
    tags:
      - 'v*'
  workflow_dispatch:
    inputs:
      environment:
        description: 'Deployment environment'
        required: true
        default: 'staging'
        type: choice
        options:
        - staging
        - production

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ github.event.inputs.environment || 'production' }}
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Setup Node.js
      uses: actions/setup-node@v4
      with:
        node-version: '20.x'
        cache: 'npm'
    
    - name: Install dependencies
      run: npm ci
    
    - name: Build for production
      run: npm run build
      env:
        NODE_ENV: production
    
    - name: Deploy to staging
      if: github.event.inputs.environment == 'staging'
      run: |
        echo "Deploying to staging..."
        # Add staging deployment commands
    
    - name: Deploy to production
      if: github.event.inputs.environment == 'production' || startsWith(github.ref, 'refs/tags/')
      run: |
        echo "Deploying to production..."
        # Add production deployment commands
    
    - name: Notify Slack
      uses: 8398a7/action-slack@v3
      with:
        status: ${{ job.status }}
        channel: '#deployments'
      env:
        SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Fase 3: Scripts de Automatización

### Script de Build
```bash
#!/bin/bash
set -e

echo "🔧 Building project..."

# Install dependencies
npm ci

# Run linting
echo "🔍 Running linting..."
npm run lint

# Run tests
echo "🧪 Running tests..."
npm run test

# Build project
echo "📦 Building project..."
npm run build

echo "✅ Build completed successfully!"
```

### Script de Deployment
```bash
#!/bin/bash
set -e

ENVIRONMENT=${1:-staging}
VERSION=${2:-latest}

echo "🚀 Deploying to $ENVIRONMENT (version: $VERSION)"

# Validate environment
if [[ ! "$ENVIRONMENT" =~ ^(staging|production)$ ]]; then
  echo "❌ Invalid environment. Use 'staging' or 'production'"
  exit 1
fi

# Build for deployment
npm run build

# Deploy based on environment
case $ENVIRONMENT in
  staging)
    echo "📡 Deploying to staging..."
    # Add staging deployment logic
    ;;
  production)
    echo "🌟 Deploying to production..."
    # Add production deployment logic
    ;;
esac

echo "✅ Deployment to $ENVIRONMENT completed!"
```

## Fase 4: Configuración de Calidad

### Pre-commit Hooks
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.4.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-merge-conflict
  
  - repo: local
    hooks:
      - id: eslint
        name: eslint
        entry: npx eslint --fix
        language: node
        files: \.(js|jsx|ts|tsx)$
        additional_dependencies:
          - eslint
      
      - id: prettier
        name: prettier
        entry: npx prettier --write
        language: node
        files: \.(js|jsx|ts|tsx|json|md)$
        additional_dependencies:
          - prettier
      
      - id: tests
        name: tests
        entry: npm test
        language: node
        pass_filenames: false
        always_run: true
```

### Dependabot Configuration
```yaml
# .github/dependabot.yml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "weekly"
    reviewers:
      - "team-leads"
    assignees:
      - "maintainer"
    commit-message:
      prefix: "deps"
      include: "scope"
```

## Fase 5: Configuración de Ambientes

### Variables de Entorno
```bash
# .env.example
NODE_ENV=development
PORT=3000
DATABASE_URL=postgresql://user:pass@localhost:5432/db
REDIS_URL=redis://localhost:6379
API_KEY=your_api_key_here
JWT_SECRET=your_jwt_secret
```

### Docker Configuration
```dockerfile
# Dockerfile
FROM node:20-alpine AS base

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production

FROM base AS build
RUN npm ci
COPY . .
RUN npm run build

FROM base AS runtime
COPY --from=build /app/dist ./dist
EXPOSE 3000
CMD ["npm", "start"]
```

### Docker Compose para Development
```yaml
# docker-compose.yml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - DATABASE_URL=postgresql://postgres:password@db:5432/myapp
    depends_on:
      - db
      - redis
    volumes:
      - .:/app
      - /app/node_modules

  db:
    image: postgres:15-alpine
    environment:
      - POSTGRES_DB=myapp
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=password
    volumes:
      - postgres_data:/var/lib/postgresql/data
    ports:
      - "5432:5432"

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"

volumes:
  postgres_data:
```

## Fase 6: Monitoreo y Alertas

### Health Checks
```javascript
// health.js
const express = require('express');
const app = express();

app.get('/health', (req, res) => {
  const healthCheck = {
    uptime: process.uptime(),
    message: 'OK',
    timestamp: Date.now(),
    checks: {
      database: 'OK', // Add actual DB check
      redis: 'OK',     // Add actual Redis check
      external_api: 'OK' // Add external API checks
    }
  };
  res.status(200).json(healthCheck);
});

module.exports = app;
```

### Alerting Configuration
```yaml
# .github/workflows/alerts.yml
name: Alerts

on:
  workflow_run:
    workflows: ["CI Pipeline"]
    types:
      - completed

jobs:
  alert-on-failure:
    runs-on: ubuntu-latest
    if: ${{ github.event.workflow_run.conclusion == 'failure' }}
    
    steps:
    - name: Send failure notification
      uses: 8398a7/action-slack@v3
      with:
        status: failure
        channel: '#alerts'
        message: |
          🚨 CI Pipeline failed!
          Branch: ${{ github.event.workflow_run.head_branch }}
          Commit: ${{ github.event.workflow_run.head_sha }}
          Workflow: ${{ github.event.workflow_run.html_url }}
      env:
        SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Implementación

### Checklist de Setup
- [ ] Crear workflows de GitHub Actions
- [ ] Configurar secrets en GitHub
- [ ] Setup pre-commit hooks
- [ ] Configurar Dependabot
- [ ] Crear scripts de deployment
- [ ] Configurar monitoreo
- [ ] Documentar proceso de deployment
- [ ] Entrenar al equipo en nuevos workflows

### Secrets Requeridos
```
CODECOV_TOKEN          # Para coverage reports
SLACK_WEBHOOK          # Para notificaciones
DEPLOY_KEY             # Para deployment
DATABASE_URL           # Para tests de integración
API_KEYS               # Para servicios externos
```

### Próximos Pasos
1. Ejecutar pipeline en rama de prueba
2. Validar deployment en staging
3. Configurar alertas y monitoreo
4. Documentar proceso para el equipo
5. Establecer políticas de merge y deployment