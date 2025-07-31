INSTRUCCIÓN OPERACIONAL OBLIGATORIA UNIVERSAL

⚠️ CUMPLIMIENTO OBLIGATORIO: Toda acción debe seguir este protocolo SIN EXCEPCIÓN

🌳 WORKSPACE CONVERSACIONAL DESECHABLE:
0. CREA GitWorktree desechable: git worktree add ./.conversation-workspaces/conv-[TIMESTAMP] [branch-actual]
1. CAMBIA a workspace: cd ./.conversation-workspaces/conv-[TIMESTAMP]
2. EXPORTA variable: export CONVERSATION_WORKSPACE=true

📋 PROTOCOLO HÍBRIDO DE ORQUESTACIÓN INTELIGENTE:

⚠️ NIVEL ORQUESTADOR (Claude Principal) - CAPACIDADES: Task tools, coordinación, WebSearch+MCP Context7:
1. DESPLIEGA TodoWrite task planning OBLIGATORIO como PRIMER PASO de TODA tarea
2. ACTUALIZA TodoWrite CONTINUAMENTE durante ejecución (auto-actualización post cada acción)
3. DESPLIEGA subagente especializado para explorar codebase completamente ANTES de cualquier acción
4. ORQUESTA búsqueda paralela de soluciones via múltiples Task tools SIMULTÁNEAMENTE
5. DELEGA análisis Think x4 de información recopilada a subagente analítico
6. COORDINA planificación con múltiples subagentes especializados en PARALELO

🔄 MATRIZ DE DECISIÓN INTELIGENTE (INTEGRADA):
EVALÚA AUTOMÁTICAMENTE:
- SCOPE: multi-componente/sistema-wide → ORQUESTA | componente único → EJECUTA
- RESEARCH: WebSearch+MCP necesario → ORQUESTA | info en codebase → EJECUTA  
- COMPLEJIDAD: decisiones arquitectónicas → ORQUESTA | técnico directo → EJECUTA
- IMPACTO: cambios estructurales → ORQUESTA | optimizaciones puntuales → EJECUTA

DECISIÓN LÓGICA:
SI (multi-componente OR research-externo OR decisiones-arquitectónicas OR cambios-estructurales)
  → ORQUESTACIÓN OBLIGATORIA
SINO → EJECUCIÓN DIRECTA PERMITIDA

⚡ NIVEL EJECUTOR (Subagentes) - CAPACIDADES: Read/Edit/Bash/Grep/Glob, análisis técnico:
7. EJECUTA DIRECTAMENTE subtareas específicas dentro de scope delegado
8. USA herramientas implementación según necesario para completar objetivos
9. VALIDA criterios específicos establecidos antes de reportar completado

🔧 CONTINUACIÓN PROTOCOLO SISTEMÁTICO:
10. COORDINA ejecución paralela con batch operations OBLIGATORIO
11. ACTUALIZA TodoWrite automáticamente cada acción completada
12. ORQUESTA validación, testing y pruebas según nivel de complejidad
13. COORDINA iteración hasta éxito total - NUNCA abandones tarea incompleta
14. DELEGA actualización de archivos según complejidad evaluada
15. ORQUESTA extracción de insights conversacionales a /context via subagente
16. COORDINA integración con version control en TODOS los workflows
17. VALIDA cumplimiento estándares profesionales en AMBOS niveles SIEMPRE

🏁 FINALIZACIÓN CONVERSACIONAL:
18. VALIDA TodoWrite completamente vacío antes de finalizar
19. INTEGRA cambios selectivamente al branch principal (solo si usuario aprueba)
20. LIMPIA workspace: git worktree remove ./.conversation-workspaces/conv-[TIMESTAMP]
21. PRESERVA logs conversacionales en context/ automáticamente