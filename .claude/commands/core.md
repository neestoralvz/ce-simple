INSTRUCCIÓN OPERACIONAL OBLIGATORIA UNIVERSAL

⚠️ CUMPLIMIENTO OBLIGATORIO: Toda acción debe seguir este protocolo SIN EXCEPCIÓN

🚀 MICRO-TASK FAST TRACK (≤5 tool calls OR single-file changes):
- SKIP GitWorktree → ejecutar directamente en branch actual
- SKIP orquestación → usar herramientas directas (Read/Edit/Bash)
- TodoWrite mínimo (1-2 items máximo)
- Finalización simplificada

🌳 WORKSPACE CONVERSACIONAL RESILIENTE:
0a. VERIFICA: mkdir -p ./.conversation-workspaces (create if missing)
0b. EJECUTA: git worktree add ./.conversation-workspaces/conv-[TIMESTAMP] HEAD
0c. FALLBACK: Si GitWorktree falla → CONTINÚA en branch actual + warning usuario
1. CAMBIA: cd ./.conversation-workspaces/conv-[TIMESTAMP] (if successful)
2. ACTIVA: export CONVERSATION_WORKSPACE=true

🪝 AUTOMATION LAYER INTEGRATION:
- PRE-TASK: Ejecutar Claude Code hooks automáticamente (workspace-init, dependency-check)
- DURANTE: parallel-tool-manager.sh coordina herramientas simultáneas
- POST-COMPLETION: quality-gate.sh + context-extract.sh + issue-detector.sh
- GIT-HOOKS: pre-commit validation, post-commit monitoring automático

📋 PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE:

⚠️ NIVEL ORQUESTADOR (Claude Principal) - CAPACIDADES: Task tools, coordinación, WebSearch+MCP Context7:
1. DESPLIEGA TodoWrite task planning OBLIGATORIO como PRIMER PASO
2. ACTUALIZA TodoWrite adaptativamente: micro-task (completion only), simple-task (cada 2-3 acciones), complex-task (continuo)
3. DESPLIEGA subagente especializado para explorar codebase ANTES de cualquier acción
4. ORQUESTA búsqueda paralela via múltiples Task tools SIMULTÁNEAMENTE
5. DELEGA análisis Think x4 de información a subagente analítico
6. COORDINA planificación con múltiples subagentes especializados

🔄 MATRIZ DE DECISIÓN INTELIGENTE (EMBEDDED - NO REFERENCIAS EXTERNAS):
EVALÚA AUTOMÁTICAMENTE:
┌─ SCOPE ────────────────────────────────────────────────────┐
│ multi-componente | sistema-wide | >1 archivo → ORQUESTA   │
│ componente único | archivo único | focalizado → EJECUTA    │
└────────────────────────────────────────────────────────────┘
┌─ RESEARCH ─────────────────────────────────────────────────┐
│ WebSearch+MCP Context7 necesario → ORQUESTA               │
│ información en codebase solamente → EJECUTA               │
└────────────────────────────────────────────────────────────┘
┌─ COMPLEJIDAD ──────────────────────────────────────────────┐
│ decisiones arquitectónicas | research paralelo → ORQUESTA │
│ análisis técnico directo | implementación → EJECUTA       │
└────────────────────────────────────────────────────────────┘

DECISIÓN LÓGICA:
SI (multi-componente OR research-externo OR decisiones-arquitectónicas OR >5 tool calls estimados)
  → ORQUESTACIÓN OBLIGATORIA
SINO → EJECUCIÓN DIRECTA PERMITIDA

⚡ NIVEL EJECUTOR (Subagentes) - CAPACIDADES: Read/Edit/Bash/Grep/Glob, análisis técnico:
7. EJECUTA DIRECTAMENTE subtareas específicas dentro de scope delegado
8. USA herramientas según necesario para completar objetivos
9. VALIDA criterios antes de reportar completado

🔧 CONTINUACIÓN PROTOCOLO SISTEMÁTICO:
10. COORDINA ejecución paralela (MÁXIMO 3 subagentes simultáneos)
11. RESOURCE MANAGEMENT: STOP si >10 acciones pending, fallback a ejecución directa
12. ORQUESTA validación según complejidad evaluada
13. COORDINA iteración hasta éxito total - NUNCA abandones tarea incompleta
14. DELEGA actualización archivos según matriz de decisión
15. ORQUESTA extracción insights conversacionales via subagente
16. COORDINA integración version control
17. VALIDA estándares profesionales AMBOS niveles SIEMPRE

📋 GITHUB ISSUES WORKFLOW (Scope Discoveries):
18a. DETECTA: Tareas descubiertas fuera scope original durante ejecución
18b. CLASIFICA: micro-task vs complex-task vs future-enhancement  
18c. CREA: gh issue create con context link + labels apropiados
18d. CONTINÚA: Con tarea original sin bloqueo

🏁 FINALIZACIÓN CONVERSACIONAL:
19. VALIDA TodoWrite apropiadamente completado (no necesariamente vacío)
20. EXTRAE: context/conversations/conv-[TIMESTAMP]-summary.md
21. IDENTIFICA: Patrones → context/patterns/ si aplicable
22. ACTUALIZA: context/data/performance/ con métricas si relevante
23. INTEGRA: Cambios selectivamente al branch principal (SOLO si usuario aprueba)
24. LIMPIA: git worktree remove + cleanup orphaned workspaces automático
25. PRESERVA: Logs conversacionales en structure apropiada