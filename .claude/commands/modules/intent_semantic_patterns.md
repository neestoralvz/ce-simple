# Intent Semantic Patterns Module

## Project Type Detection Template
**API/Backend:** "API", "backend", "server", "endpoints", "microservice" → `p-init api-service`
**Frontend:** "landing", "website", "frontend", "UI", "interfaz", "página" → `p-init web-frontend`
**Full-Stack:** "web app", "aplicación web", "fullstack", "completa" → `p-init web-app`
**CLI:** "CLI", "command line", "terminal", "script", "herramienta" → `p-init cli-tool`
**Mobile:** "mobile", "app móvil", "iOS", "Android", "celular" → `p-init mobile-app`

## Intent Classification Template
### Initialization Intent
**Keywords:** "quiero hacer", "necesito crear", "empezar", "iniciar", "nuevo proyecto"
**Action:** Project type detection → `p-init [detected-type]`
**Confidence threshold:** 80% for auto-execution

### Status/Help Intent  
**Keywords:** "perdido", "¿qué hago?", "estado", "progreso", "help", "ayuda"
**Action:** Route to `p-status` or help system

### Continuation Intent
**Keywords:** "continuar", "seguir", "retomar", "donde quedé", "siguiente paso"
**Action:** Route to `p-focus` + `p-status`

### Advancement Intent
**Keywords:** "terminé", "completé", "siguiente fase", "avanzar", "listo"
**Action:** Route to `p-gate` for layer validation

## Technology Stack Hints
**Backend tech:** "Node.js", "Python", "Django", "Express" → api-service
**Frontend tech:** "React", "Vue", "Angular", "HTML/CSS" → web-frontend  
**Mobile tech:** "React Native", "Flutter", "Swift", "Kotlin" → mobile-app
**CLI tech:** "Bash", "Python script", "Node CLI" → cli-tool

## Domain-Specific Recognition
**E-commerce:** "tienda", "shop", "ecommerce" → web-app with specific templates
**Analytics:** "dashboard", "métricas", "análisis" → web-app with data focus
**Automation:** "automatizar", "script", "batch" → cli-tool
**Content:** "blog", "CMS", "contenido" → web-frontend or web-app

**Usage**: Semantic pattern matching for intelligent command routing