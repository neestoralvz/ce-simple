# Distillation Layers Module

## Layer 1: Quote Absorption Template
**If nuclei NOT exist**: Create initial nuclei: metodologia_socratica.md, arquitectura_comandos.md, autoridad_vision.md, evolucion_organica.md, simplicidad_belleza.md, flujos_trabajo.md

**Quote Format Template**:
```markdown
## Quote Original
> "texto exacto del usuario"
**Ref:** `/conversations/archivo.md:línea`

### Contexto Conversacional
[Contexto específico]
---
```

**Tracking Template**:
```markdown
## Conversations Processed
- archivo1.md
- archivo2.md
```

## Layer 2: Ultra-Dense Concentration Template
**Objective**: Fusionar múltiples quotes en insights concentrados y poderosos

**Format Template**:
```markdown
# Insight Concentrado: [Principio Core]

## Síntesis Ultra-Densa
[UN párrafo que concentra 10+ quotes en insight poderoso]

## Evidence Base (Layer 1 sources)
[Solo referencias, no repetir contenido]

## Implicaciones Ejecutables
[Consecuencias directas y actionables]
```

**Criteria**: Each Layer 2 file must concentrate 10x more value than sum of source quotes

## Layer 3: Executable Documentation Template
**Meta-concentration from Layer 2**:
- methodology_guide.md (fusión de insights metodológicos concentrados)
- architecture_principles.md (síntesis arquitectural ultra-densa)
- implementation_guide.md (guía ejecutable concentrada)
- quick_reference.md (máxima densidad práctica)

**Density Criteria**:
- Each line = maximum value/token ratio
- Eliminate redundancy and dispersion
- Immediate executable knowledge
- 100% signal, 0% noise

## Auto-Detection Template
```bash
# Primary: Compare timestamps
newest_conversation=$(ls -t /conversations/*.md | head -1)
newest_nuclei=$(ls -t /layer1/*.md | head -1)

# Secondary: Check processed lists
grep -h "^- " /layer1/*/## Conversations Processed | sort -u > processed.tmp
```

**Usage**: Iterative distillation with automatic convergence and completeness validation