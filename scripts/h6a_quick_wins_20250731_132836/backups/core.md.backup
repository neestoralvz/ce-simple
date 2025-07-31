INSTRUCCIÓN OPERACIONAL OBLIGATORIA UNIVERSAL

⚠️ CUMPLIMIENTO OBLIGATORIO: Toda acción debe seguir este protocolo SIN EXCEPCIÓN

🌳 WORKSPACE CONVERSACIONAL RESILIENTE:
0a. EJECUTA: scripts/conversation-workspace.sh create OBLIGATORIO
0b. OBTÉN: workspace_path del output del script anterior
0c. EJECUTA: source $workspace_path/.env && cd $workspace_path OBLIGATORIO
0d. FALLBACK: Si workspace falla → CONTINÚA en directorio actual + warning usuario

🪝 AUTOMATION LAYER INTEGRATION:
- PRE-TASK: Ejecutar .claude/hooks/ validation scripts | FALLBACK manual si falla
- DURANTE: scripts/parallel-tool-manager.sh coordina herramientas | FALLBACK coordinación manual si falla
- POST-COMPLETION: scripts/quality-gate.sh + scripts/context-extract.sh + scripts/issue-detector.sh | FALLBACK validación manual si falla
- GIT-HOOKS: pre-commit validation, post-commit monitoring | CONTINÚA si hooks fallan

📋 PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE:

⚠️ NIVEL ORQUESTADOR (Claude Principal) - CAPACIDADES: Task tools, coordinación, WebSearch+MCP Context7:
1. EVALÚA MODE: Si plan mode → SKIP TodoWrite hasta plan approval | Si execution mode → DESPLIEGA TodoWrite OBLIGATORIO
2. ACTUALIZA TodoWrite CONTINUAMENTE durante ejecución (SOLO en execution mode) OBLIGATORIO
3. DESPLIEGA subagente especializado para explorar codebase ANTES de acciones críticas OBLIGATORIO
4. ORQUESTA búsqueda paralela via múltiples Task tools CUANDO complejidad lo justifique OBLIGATORIO
5. DELEGA análisis Think x4 de información a subagente analítico PARA decisiones complejas OBLIGATORIO
6. COORDINA planificación con múltiples subagentes especializados SEGÚN necesidad OBLIGATORIO

🔄 MATRIZ DE DECISIÓN INTELIGENTE (EMBEDDED - NO REFERENCIAS EXTERNAS):
EVALÚA AUTOMÁTICAMENTE:
┌─ SCOPE ────────────────────────────────────────────────────┐
│ >1 archivo | >1 componente | sistema-wide → ORQUESTA      │
│ 1 archivo simple | análisis directo → DIRECT EXECUTION    │
└────────────────────────────────────────────────────────────┘
┌─ RESEARCH ─────────────────────────────────────────────────┐
│ WebSearch+MCP Context7 necesario → ORQUESTA               │
│ información simple en codebase → DIRECT EXECUTION         │
└────────────────────────────────────────────────────────────┘
┌─ COMPLEJIDAD ──────────────────────────────────────────────┐
│ decisiones arquitectónicas | research paralelo → ORQUESTA │
│ análisis simple | lectura directa → DIRECT EXECUTION      │
└────────────────────────────────────────────────────────────┘

DECISIÓN LÓGICA INTELIGENTE:
ORQUESTA → Complex multi-component tasks, architectural decisions, parallel research
DIRECT → Simple analysis, single file operations, straightforward queries

CONFLICT RESOLUTION RULES:
- Si criterios ambiguos → EVALUATE complejidad real y DECIDE apropiadamente
- Si scope crece mid-execution → UPGRADE a orquestación
- Si user prefiere approach → RESPECT user preference + SUGGEST optimizations

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

📋 GITHUB ISSUES WORKFLOW (Enhanced Scope Management):
18a. DETECTA: Tareas descubiertas fuera scope durante ejecución + %scope expansion OBLIGATORIO
18b. EVALÚA: Si scope expansion >20% → automatic issue creation OBLIGATORIO
18c. CLASIFICA: micro-task vs complex-task vs future-enhancement con priority assessment OBLIGATORIO
18d. PLAN MODE: Documenta issues en plan para user approval | EXECUTION MODE: scripts/issue-detector.sh create OBLIGATORIO
18e. NOTIFICA: "Issue documented/created para [task] - continuando con plan original" OBLIGATORIO
18f. CONTINÚA: Con tarea original sin bloqueo, issues quedan para follow-up OBLIGATORIO

🏁 FINALIZACIÓN CONVERSACIONAL:
19. VALIDA TodoWrite completamente procesado OBLIGATORIO
20. EXTRAE: context/conversations/conv-[TIMESTAMP]-summary.md OBLIGATORIO
21. CAPTURA CONTEXTO: Usar slash command q-context para extraer insights + IDENTIFICA: Patrones → context/patterns/ OBLIGATORIO
22. ACTUALIZA: context/data/performance/ con métricas OBLIGATORIO
23. INTEGRA: Cambios selectivamente al branch principal (SOLO si usuario aprueba) OBLIGATORIO
24. LIMPIA: git worktree remove + cleanup orphaned workspaces OBLIGATORIO
25. PRESERVA: Logs conversacionales en structure apropiada OBLIGATORIO

🔄 POST-EXECUTION VALIDATION:
26. VALIDA: ¿Orquestación logró mejor resultado que ejecución directa habría logrado? OBLIGATORIO
27. DOCUMENTA: Lessons learned para mejorar future orquestación OBLIGATORIO
28. CONFIRMA: Todos los pasos ejecutados según protocolo OBLIGATORIO

🔗 VALIDACIÓN DE COHERENCIA CONTEXTUAL:
28.5a. EJECUTA: scripts/validate-context-coherence.sh validate OBLIGATORIO
28.5b. DETECTA: Cambios en protocolos, metodologías o estructuras relevantes OBLIGATORIO
28.5c. VALIDA: Enlaces condicionales en CLAUDE.md funcionan correctamente OBLIGATORIO
28.5d. VERIFICA: Semantic triggers mantienen cohesión con context real OBLIGATORIO
28.5e. ACTUALIZA: CLAUDE.md si hay inconsistencias detectadas OBLIGATORIO
28.5f. CONFIRMA: Todos los @context/ references son válidos y accesibles OBLIGATORIO

🎯 CONVERSATION COMPLETION ASSESSMENT:
29a. VERIFICA: TodoWrite 100% completado - no pending/in_progress tasks OBLIGATORIO
29b. CONFIRMA: Contexto capturado exitosamente + patrones identificados OBLIGATORIO
29c. VALIDA: Todas las tareas fuera scope convertidas a issues OBLIGATORIO
29d. EVALÚA: No errores críticos pendientes de resolución OBLIGATORIO
29e. NOTIFICA: Si 4 criterios ✅ → "🎯 CONVERSACIÓN COMPLETADA - Lista para cierre" OBLIGATORIO
29f. REPORTA: Summary metrics (tasks completed, issues created, context captured) OBLIGATORIO
