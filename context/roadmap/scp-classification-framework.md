# SCP Classification Framework - Handoff Density & Difficulty System

**31/07/2025 CDMX** | Systematic classification for handoff planning and resource allocation

## AUTORIDAD SUPREMA
@context/architecture/core/truth-source.md → SCP Framework implements handoff classification per roadmap authority

## PRINCIPIO FUNDAMENTAL
**"SCP Classification enables strategic handoff design and optimal resource allocation"** - Every handoff classified by Scope, Coordination, and Processing complexity for precise planning and execution optimization.

## SCP CLASSIFICATION SYSTEM

### **S - SCOPE (Alcance del Impacto)**

#### **S1-FOCUSED** (Impacto Localizado)
- **Definición**: Un dominio específico, componentes limitados
- **Criterios**: ≤5 componentes afectados, 1 área funcional, cambios localizados
- **Características**: Impacto predecible, testing limitado, rollback sencillo
- **Ejemplos**: Optimización de archivo individual, corrección de referencias, cleanup puntual

#### **S2-CROSS** (Impacto Multi-Área)  
- **Definición**: 2-3 dominios relacionados, coordinación inter-componentes
- **Criterios**: 6-15 componentes afectados, 2-3 áreas funcionales, integración requerida
- **Características**: Impacto medible, testing multi-área, rollback coordinado
- **Ejemplos**: L2-MODULAR extraction, cross-reference updates, pattern implementations

#### **S3-SYSTEM** (Impacto Arquitectural)
- **Definición**: Sistema completo, cambios estructurales fundamentales
- **Criterios**: 15+ componentes afectados, arquitectura completa, cambios sistémicos
- **Características**: Impacto extenso, testing comprehensivo, rollback complejo
- **Ejemplos**: Core factorization, system-wide standardization, architectural migrations

### **C - COORDINATION (Nivel de Coordinación)**

#### **C1-INDEPENDENT** (Ejecución Independiente)
- **Definición**: Sin dependencias externas críticas
- **Criterios**: 0 dependencias bloqueantes, ejecución paralela posible, recursos auto-contenidos
- **Características**: Alta paralelización, scheduling flexible, riesgo de conflicto bajo
- **Ejemplos**: Cleanup independiente, documentación específica, optimizaciones aisladas

#### **C2-DEPENDENT** (Dependencias Limitadas)
- **Definición**: 1-2 dependencias claras y bien definidas  
- **Criterios**: 1-2 handoffs prerequisitos, secuencia definida, coordinación simple
- **Características**: Scheduling secuencial, dependencias rastreables, coordinación básica
- **Ejemplos**: Post-classification implementations, follow-up extractions, dependent optimizations

#### **C3-ORCHESTRATED** (Coordinación Compleja)
- **Definición**: Múltiples dependencias, coordinación activa requerida
- **Criterios**: 3+ dependencias, coordinación multi-handoff, sincronización crítica
- **Características**: Orchestration necesaria, scheduling complejo, coordinación continua
- **Ejemplos**: System testing, architectural transitions, complex integrations

### **P - PROCESSING (Complejidad de Procesamiento)**

#### **P1-DIRECT** (Implementación Directa)
- **Definición**: Patrones conocidos, ejecución estándar
- **Criterios**: Métodos establecidos, patrones repetibles, complejidad técnica baja
- **Características**: Ejecución predecible, time estimation precisa, riesgo técnico bajo
- **Ejemplos**: File optimizations, standard cleanups, template applications

#### **P2-EXTRACTION** (Procesamiento Modular)
- **Definición**: L2-MODULAR requerido, extracción y modularización
- **Criterios**: Decomposición necesaria, extracción de contenido, reestructuración requerida
- **Características**: Analysis intensivo, restructuring workflow, validation compleja
- **Ejemplos**: Large file extractions, modular decompositions, content reorganization

#### **P3-COORDINATION** (Procesamiento Complejo)
- **Definición**: Orquestación compleja, múltiples procesos coordinados
- **Criterios**: Workflow complejo, múltiples etapas, coordinación de procesos
- **Características**: Multi-phase execution, process orchestration, extensive validation
- **Ejemplos**: System factorization, architectural redesign, complex integrations

## MATRIZ DE COMBINACIONES SCP

### **Perfiles de Complejidad Típicos**

#### **Baja Complejidad** (Ejecución Rápida)
- **S1C1P1**: Handoffs triviales, 1-2 horas, paralelos
- **S1C2P1**: Handoffs simples con dependencias, 2-4 horas, secuenciales

#### **Complejidad Media** (Ejecución Estándar)  
- **S2C1P2**: Extracciones independientes, 4-8 horas, paralelos
- **S2C2P1**: Cross-component directos, 6-12 horas, coordinados
- **S1C1P3**: Localizados pero complejos, 8-16 horas, especializados

#### **Alta Complejidad** (Ejecución Especializada)
- **S2C2P2**: Standard complex handoffs, 1-2 días, coordinación media
- **S3C2P1**: System-wide directos, 1-3 días, coordinación simple
- **S2C3P2**: Multi-component orchestrated, 2-4 días, alta coordinación

#### **Complejidad Crítica** (Ejecución Intensiva)
- **S3C3P2**: System extractions, 3-5 días, máxima coordinación
- **S3C3P3**: Architectural transformations, 5-10 días, orchestration completa

## APLICACIÓN PRÁCTICA

### **En Creación de Handoffs**
1. **Pre-Analysis SCP**: Evaluar S-C-P antes de diseñar handoff
2. **Resource Planning**: Estimar tiempo/recursos según perfil SCP
3. **Strategy Selection**: Elegir approach óptimo basado en clasificación
4. **Quality Gates**: Definir validation apropiada para nivel de complejidad

### **En Ejecución de Handoffs**
1. **Batch Processing**: Agrupar handoffs similares por perfil SCP
2. **Parallel Execution**: Priorizar C1 handoffs para paralelización
3. **Resource Allocation**: Asignar recursos especializados según P-level
4. **Risk Management**: Aplicar safeguards apropiados según S-level

### **En Tracking de Progreso**
1. **Dashboard Integration**: Visual SCP distribution en roadmap
2. **Progress Prediction**: Estimación basada en historical SCP patterns
3. **Bottleneck Identification**: Detectar cuellos de botella por clasificación
4. **Success Pattern Replication**: Reutilizar strategies exitosos por perfil

## INTEGRATION REFERENCES

**Roadmap Authority**: ← @context/roadmap/ROADMAP_REGISTRY.md (handoff tracking)
**Dashboard Integration**: ←→ @context/roadmap/dashboard/ (visual tracking)
**Template System**: → handoff-creation-template-scp.md (creation integration)
**Pattern Database**: → scp-patterns-database.md (historical patterns)

---

**SCP FRAMEWORK DECLARATION**: Complete handoff classification system enabling strategic planning, resource optimization, and execution excellence through systematic Scope-Coordination-Processing analysis.

**EVOLUTION PATHWAY**: Framework evolves through handoff analysis → pattern recognition → optimization → strategic planning enhancement cycle.