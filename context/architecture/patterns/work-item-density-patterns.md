# Work Item Density Patterns - Task Complexity Assessment Authority

**31/07/2025 CDMX** | Systematic framework for work item complexity evaluation and split recommendations

## AUTORIDAD SUPREMA
↑ @context/architecture/patterns.md → work-item-density-patterns.md implements task complexity assessment per roadmap optimization requirements

## PRINCIPIO FUNDAMENTAL
**"Task density determines work item viability - systematic assessment prevents over-complex handoffs"** - Framework complementario a L2-MODULAR focusing on task complexity vs file line count.

## WORK ITEM DENSITY FRAMEWORK

### Core Density Metrics
**Density Assessment Protocol**:
- **Task Count**: Number of distinct subtasks/objectives within work item
- **Documentation Lines**: Size of work item documentation as complexity proxy
- **Timeline Estimate**: Expected execution duration for work item
- **Cross-Domain Impact**: Number of system areas affected by work item

### Density Classification System
```
DENSITY LEVELS:
├── V.High: ~15+ tasks → 🔴 SPLIT REQUIRED
├── High: ~10-12 tasks → ⚠️ DENSE WARNING  
├── Med-Hi: ~8-9 tasks → ⚠️ WATCH COMPLEXITY
├── Medium: ~4-7 tasks → ✅ GOOD DENSITY
└── Low: ~2-3 tasks → ✅ OPTIMAL SIZE
```

### Split Recommendations Matrix
| Density | Task Count | Timeline | Split Recommendation | Action Required |
|---------|------------|----------|---------------------|-----------------|
| **V.High** | ~15+ | >5 days | 🔴 **SPLIT** | Immediate division into sub-handoffs |
| **High** | ~10-12 | 3-5 days | ⚠️ **Dense** | Monitor complexity, consider split |
| **Med-Hi** | ~8-9 | 2-3 days | ⚠️ **Watch** | Track for complexity growth |
| **Medium** | ~4-7 | 1-2 days | ✅ **Good** | Optimal handoff size |
| **Low** | ~2-3 | <1 day | ✅ **Good** | May combine with related work |

## EMPIRICAL VALIDATION EVIDENCE

### Validated Success Cases
**P0-EMERGENCY Split**: V.High (15 tasks) → P0A-CRITICAL + P0B-CLEANUP (6 tasks each)
- **Result**: P0A achieved 100% completion vs original 51%
- **Benefits**: Clear separation, independent progress tracking, focused execution

**P0B-CLEANUP Parallel Split**: V.High bottleneck → 4 concurrent handoffs  
- **Timeline**: 5-day sequential → 2-day parallel (60% reduction)
- **Bottleneck Resolution**: 157 violations → 0 enabling pipeline unblock
- **Resource Optimization**: Domain separation enables parallel processing

**Pattern Validation**: High density (12+ tasks) = Dense but completable; Medium (4-7) = Optimal; Low (2-3) = Efficient

## INTEGRATION & APPLICATION

### L2-MODULAR Complementarity
**L2-MODULAR**: File size violations (>80 lines) → Extract to modules
**Density Patterns**: Task complexity violations (>7 tasks) → Split to sub-handoffs
**Synergy**: Combined file-based + task-based assessment provides complete optimization

### Application Protocol
1. **Assessment**: Count tasks, estimate timeline, analyze documentation, map impact
2. **Decision**: Apply classification → Use matrix → User consultation → Implementation
3. **Validation**: Monitor completion rates, verify reduction, update thresholds

## INTEGRATION REFERENCES

### ←→ @context/architecture/patterns/l2-modular-extraction-patterns.md
**Connection**: Complementary methodologies - file-based vs task-based complexity assessment
**Protocol**: Combined application for complete work item optimization

### ←→ @context/architecture/patterns/organic_evolution_patterns.md  
**Connection**: Metrics-driven system evolution through density assessment
**Protocol**: Density patterns inform organic system structure evolution

### ← @context/architecture/patterns.md
**Authority Source**: Pattern ecosystem authority validates work item density methodology

---
**DENSITY PATTERNS AUTHORITY**: This framework provides systematic task complexity assessment complementing existing methodologies through empirical validation and practical application protocols.

**EVOLUTION PATHWAY**: Density assessment → split recommendations → empirical validation → pattern refinement