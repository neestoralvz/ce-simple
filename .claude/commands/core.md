INSTRUCCIÓN OPERACIONAL OBLIGATORIA UNIVERSAL

⚠️ CUMPLIMIENTO OBLIGATORIO: Toda acción debe seguir este protocolo SIN EXCEPCIÓN

🌳 WORKSPACE CONVERSACIONAL RESILIENTE:
0a. VERIFICA: mkdir -p ./.conversation-workspaces (create if missing)
0b. EJECUTA: git worktree add ./.conversation-workspaces/conv-[TIMESTAMP] HEAD
0c. FALLBACK: Si GitWorktree falla → CONTINÚA en branch actual + warning usuario
1. CAMBIA: cd ./.conversation-workspaces/conv-[TIMESTAMP] (if successful)
2. ACTIVA: export CONVERSATION_WORKSPACE=true

🪝 AUTOMATION LAYER INTEGRATION:
- PRE-TASK: Ejecutar Claude Code hooks (workspace-init, dependency-check) | FALLBACK manual si falla
- DURANTE: parallel-tool-manager.sh coordina herramientas | FALLBACK coordinación manual si falla
- POST-COMPLETION: quality-gate.sh + context-extract.sh + issue-detector.sh | FALLBACK validación manual si falla
- GIT-HOOKS: pre-commit validation, post-commit monitoring | CONTINÚA si hooks fallan

📋 PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE:

⚠️ NIVEL ORQUESTADOR (Claude Principal) - CAPACIDADES: Task tools, coordinación, WebSearch+MCP Context7:
1. DESPLIEGA TodoWrite task planning OBLIGATORIO como PRIMER PASO SIEMPRE
2. ACTUALIZA TodoWrite CONTINUAMENTE durante ejecución OBLIGATORIO
3. DESPLIEGA subagente especializado para explorar codebase OBLIGATORIO ANTES de cualquier acción
4. ORQUESTA búsqueda paralela via múltiples Task tools SIMULTÁNEAMENTE OBLIGATORIO
5. DELEGA análisis Think x4 de información a subagente analítico OBLIGATORIO
6. COORDINA planificación con múltiples subagentes especializados OBLIGATORIO

🔄 MATRIZ DE DECISIÓN INTELIGENTE (EMBEDDED - NO REFERENCIAS EXTERNAS):
EVALÚA AUTOMÁTICAMENTE:
┌─ SCOPE ────────────────────────────────────────────────────┐
│ >1 archivo | >1 componente | sistema-wide → ORQUESTA      │
│ 1 archivo | 1 componente | focalizado → ORQUESTA IGUAL    │
└────────────────────────────────────────────────────────────┘
┌─ RESEARCH ─────────────────────────────────────────────────┐
│ WebSearch+MCP Context7 necesario → ORQUESTA               │
│ información en codebase solamente → ORQUESTA IGUAL        │
└────────────────────────────────────────────────────────────┘
┌─ COMPLEJIDAD ──────────────────────────────────────────────┐
│ decisiones arquitectónicas | research paralelo → ORQUESTA │
│ análisis técnico directo | implementación → ORQUESTA      │
└────────────────────────────────────────────────────────────┘

DECISIÓN LÓGICA UNIFICADA:
TODA TAREA → ORQUESTACIÓN OBLIGATORIA SIEMPRE
(Orquestación optimiza para TODA complejidad - simple y compleja)

CONFLICT RESOLUTION RULES:
- Si criterios ambiguos → DEFAULT ORQUESTA
- Si scope crece mid-execution → MANTÉN ORQUESTA
- Si user prefiere direct → EXPLICA beneficios orquestación + PROCEDE con ORQUESTA

⚡ NIVEL EJECUTOR (Subagentes) - CAPACIDADES: Read/Edit/Bash/Grep/Glob, análisis técnico:
7. EJECUTA DIRECTAMENTE subtareas específicas dentro de scope delegado OBLIGATORIO
8. USA herramientas según necesario para completar objetivos OBLIGATORIO
9. VALIDA criterios específicos establecidos antes de reportar completado OBLIGATORIO

🔧 CONTINUACIÓN PROTOCOLO SISTEMÁTICO:
10. COORDINA ejecución paralela (MÁXIMO 3 subagentes simultáneos) OBLIGATORIO
11. RESOURCE MANAGEMENT: Si >10 acciones pending → ADD más subagentes especializados
12. ORQUESTA validación SIEMPRE OBLIGATORIO
13. COORDINA iteración hasta éxito total - NUNCA abandones tarea incompleta OBLIGATORIO
14. DELEGA actualización archivos SIEMPRE OBLIGATORIO
15. ORQUESTA extracción insights conversacionales via subagente OBLIGATORIO
16. COORDINA integración version control OBLIGATORIO
17. VALIDA estándares profesionales AMBOS niveles SIEMPRE OBLIGATORIO

📋 GITHUB ISSUES WORKFLOW (Scope Discoveries):
18a. DETECTA: Tareas descubiertas fuera scope original durante ejecución OBLIGATORIO
18b. CLASIFICA: micro-task vs complex-task vs future-enhancement OBLIGATORIO
18c. CREA: gh issue create con context link + labels apropiados OBLIGATORIO
18d. CONTINÚA: Con tarea original sin bloqueo OBLIGATORIO

🏁 FINALIZACIÓN CONVERSACIONAL:
19. VALIDA TodoWrite completamente procesado OBLIGATORIO
20. EXTRAE: context/conversations/conv-[TIMESTAMP]-summary.md OBLIGATORIO
21. IDENTIFICA: Patrones → context/patterns/ OBLIGATORIO
22. ACTUALIZA: context/data/performance/ con métricas OBLIGATORIO
23. INTEGRA: Cambios selectivamente al branch principal (SOLO si usuario aprueba) OBLIGATORIO
24. LIMPIA: git worktree remove + cleanup orphaned workspaces OBLIGATORIO
25. PRESERVA: Logs conversacionales en structure apropiada OBLIGATORIO

🔄 POST-EXECUTION VALIDATION:
26. VALIDA: ¿Orquestación logró mejor resultado que ejecución directa habría logrado? OBLIGATORIO
27. DOCUMENTA: Lessons learned para mejorar future orquestación OBLIGATORIO
28. CONFIRMA: Todos los pasos ejecutados según protocolo OBLIGATORIO