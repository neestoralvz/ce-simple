# Troubleshooting Sistémico

## Derivación de Principios Establecidos
Basado en TRUTH_SOURCE.md: "necesitamos de alguna manera tambien definir esto como algo que no puede volver a pasar en nuestro sistema y ademas resolverlo" [L1:49] y detección sistémica proactiva para prevención.

## Problemas Sistémicos Comunes

### 1. Complejidad Acumulativa
**Síntomas Técnicos**:
- CLAUDE.md excede 200 líneas efectivas
- Número creciente de archivos en docs/ sin justificación clara
- Comandos empiezan a hacer "un poquito de todo"
- Referencias cruzadas complejas entre módulos

**Diagnóstico Automático**:
```bash
# Validación tamaño CLAUDE.md
wc -l CLAUDE.md | awk '{if($1 > 200) print "WARNING: CLAUDE.md exceeds 200 lines"}'

# Conteo archivos docs/
find docs/ -name "*.md" | wc -l

# Detección scope creep en comandos
grep -n "también\|además\|y también" .claude/commands/*.md
```

**Solución Sistémica**:
1. **Regeneración CLAUDE.md**: Aplicar validation.md framework
2. **Modularización forzada**: Mover detalles técnicos a docs/
3. **Command refactoring**: Restaurar responsabilidad única
4. **Content audit**: Eliminar duplicaciones y referencias innecesarias

### 2. Deriva de Autoridad
**Síntomas Técnicos**:
- Documentos que no referencian user-vision/TRUTH_SOURCE.md
- Decisiones técnicas que contradicen visión usuario
- Creación de nueva "autoridad" implícita
- Pérdida de trazabilidad a conversaciones originales

**Diagnóstico Automático**:
```bash
# Verificar referencias a autoridad suprema
grep -r "TRUTH_SOURCE.md" docs/
grep -r "user-vision" docs/

# Detectar contradicciones potenciales
grep -i "debería\|must\|required" docs/ | grep -v "user says\|usuario dice"
```

**Solución Sistémica**:
1. **Authority restoration**: Agregar referencias explícitas a TRUTH_SOURCE.md
2. **Contradiction resolution**: Alinear contenido con visión original
3. **Traceability addition**: Agregar citations directas de conversaciones usuario
4. **Validation enforcement**: Aplicar validation.md checks

### 3. Over-Engineering Sistémico
**Síntomas Técnicos**:
- Soluciones técnicas más complejas que problema original
- Metadata y estructuras técnicas innecesarias
- Comandos con interdependencias complejas
- Feature creep sin justificación de usuario

**Diagnóstico Automático**:
```bash
# Detectar over-complexity patterns
grep -r "framework\|architecture\|system\|structure" docs/ | wc -l
find .claude/commands/ -name "*.yaml" -o -name "*.json"  # Debería ser 0
grep -r "dependency\|require\|import" .claude/commands/
```

**Solución Sistémica**:
1. **Simplification audit**: Eliminar features no derivadas de visión usuario
2. **Command independence**: Quebrar interdependencias complejas
3. **Metadata removal**: Convertir a instrucciones puras natural language
4. **Core focus**: Volver a principios fundamentales en TRUTH_SOURCE.md

### 4. Command Scope Creep
**Síntomas Técnicos**:
- Comandos que mencionan responsabilidades de otros comandos
- "Solo una funcionalidad más" patterns
- Funciones mezcladas sin límites claros
- Loss de propósito único e inequívoco

**Diagnóstico Automático**:
```bash
# Detectar scope creep patterns en comandos
for cmd in .claude/commands/*.md; do
  echo "Analyzing $cmd for scope creep:"
  grep -n "también\|además\|and also\|plus" "$cmd"
done

# Verificar responsabilidad única
grep -r "responsible for" .claude/commands/ | wc -l  # Debería ser 9 (uno por comando)
```

**Solución Sistémica**:
1. **Scope audit**: Verificar cada comando contra responsabilidad original
2. **Separation enforcement**: Quebrar funciones mezcladas
3. **Anti-pattern removal**: Eliminar "un poquito de todo" patterns
4. **Clear boundaries**: Restaurar límites bien definidos

## Problemas de Integración

### 5. Coordinación Quebrada Entre Comandos
**Síntomas Técnicos**:
- Comandos que fallan al coordinar con otros
- Duplicación de esfuerzos entre comandos
- State inconsistency entre sesiones
- Orquestación fallida master-subagent

**Diagnóstico Automático**:
```bash
# Verificar coordination patterns
grep -r "coordinates with\|coordina con" docs/workflows/
grep -r "handoff\|continuidad" handoff/

# Detectar duplicación efforts
for concept in "git" "validation" "documentation"; do
  echo "Commands mentioning $concept:"
  grep -r "$concept" .claude/commands/ | cut -d: -f1 | sort | uniq -c
done
```

**Solución Sistémica**:
1. **Coordination restoration**: Revisar integration_patterns.md
2. **Handoff repair**: Validar handoff/ directory functionality
3. **State synchronization**: Repair session continuity mechanisms
4. **Orchestration fix**: Restore master-subagent pattern clarity

### 6. Context Loss Entre Sesiones
**Síntomas Técnicos**:
- Pérdida de continuidad conversacional
- TRUTH_SOURCE.md no accesible en nuevas sesiones
- User vision no preservada across time
- Essential context missing en reinitializations

**Diagnóstico Automático**:
```bash
# Verificar continuity mechanisms
ls -la handoff/
grep -r "session" handoff/
test -f user-vision/TRUTH_SOURCE.md && echo "Authority available" || echo "ERROR: Authority missing"
```

**Solución Sistémica**:
1. **Context restoration**: Repair handoff/ protocol
2. **Authority accessibility**: Ensure TRUTH_SOURCE.md always loadable
3. **Continuity mechanisms**: Fix session-to-session preservation
4. **Essential context**: Maintain user narrative thread

## Prevention Automática

### Health Check Automático
**Implementación técnica periódica**:
```bash
#!/bin/bash
# System health validator
echo "Running system health check..."

# Check 1: CLAUDE.md size
lines=$(wc -l < CLAUDE.md)
if [ $lines -gt 200 ]; then
    echo "WARNING: CLAUDE.md has $lines lines (limit: 200)"
fi

# Check 2: Authority references
if ! grep -q "TRUTH_SOURCE.md" CLAUDE.md; then
    echo "ERROR: CLAUDE.md missing authority reference"
fi

# Check 3: Command independence
for cmd in .claude/commands/*.md; do
    if grep -q "yaml\|json\|metadata" "$cmd"; then
        echo "WARNING: $cmd contains technical metadata"
    fi
done

# Check 4: Docs modularization
docs_count=$(find docs/ -name "*.md" | wc -l)
if [ $docs_count -gt 15 ]; then
    echo "WARNING: docs/ has $docs_count files (complexity risk)"
fi
```

### Anti-Pattern Detection System
**Automated monitoring**:
- Scan para "solo una funcionalidad más" patterns
- Detect metadata creep en comandos
- Monitor file count growth sin justificación
- Track references sin authority backing

### Complexity Metrics Tracking
**Métricas continuas**:
- Lines effective en CLAUDE.md vs límite 200
- Number archivos docs/ vs threshold
- Cross-references entre módulos
- Command scope vs original responsibility
- Session continuity success rate

## Recovery Protocols

### Emergency Simplification
**Cuando sistema too complex**:
1. **Authority restoration**: Reload TRUTH_SOURCE.md como base
2. **Content audit**: Eliminar todo no derivado de visión usuario
3. **Command reset**: Restaurar responsabilidad única original
4. **Documentation cleanup**: Consolidar duplicaciones

### System Reset Protocol
**Último recurso cuando corruption sistémica**:
1. **Preserve user-vision/**: Never touch authority suprema
2. **Regenerate CLAUDE.md**: Fresh desde TRUTH_SOURCE.md
3. **Command restoration**: Reset a instrucciones puras originales
4. **Docs cleanup**: Mantener solo módulos esenciales

## Referencias a Autoridad
- user-vision/TRUTH_SOURCE.md líneas 153-157: Over-engineering prevention
- user-vision/TRUTH_SOURCE.md líneas 199-201: Health monitoring requirements
- docs/maintenance/validation.md: Validation framework completo
- docs/core/principles.md: Anti-complexity measures
- docs/workflows/coordination.md: Integration problem solutions