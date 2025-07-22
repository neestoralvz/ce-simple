# Matrix Storage Format Specification

**Version**: 1.0  
**Last Updated**: 2025-07-22  
**Format Standard**: JSON with YAML compatibility  
**Schema Version**: matrix-v1.0

## Overview

Matrix storage format provides structured dependency tracking, health monitoring, and cross-reference validation for ce-simple command systems. Core emphasis on performance, integrity, and progressive disclosure.

## Core Format Standards

### Primary Storage: JSON
**Rationale**: Universal parsing support, schema validation, efficient processing

```json
{
  "matrix_metadata": {
    "version": "1.0",
    "schema_version": "matrix-v1.0", 
    "generated_timestamp": "2025-07-22T14:30:00Z",
    "generator_version": "ce-simple-v1.2.3"
  },
  "project_summary": {
    "health_score": 87.5,
    "total_files_scanned": 2847,
    "critical_issues_count": 3,
    "warning_issues_count": 12
  },
  "dependency_graph": {
    "nodes": [...],
    "edges": [...]
  },
  "validation_results": {...},
  "risk_analysis": {...}
}
```

### Alternative Format: YAML
**Usage**: Documentation, manual review, configuration templates

```yaml
matrix_metadata:
  version: "1.0"
  schema_version: "matrix-v1.0"
  generated_timestamp: "2025-07-22T14:30:00Z"

project_summary:
  health_score: 87.5
  total_files: 2847
  issues:
    critical: 3
    warning: 12
```

## Storage Structure

### Directory Organization
```
.matrix/
├── current/
│   ├── dependency-matrix.json          # Latest complete matrix
│   ├── dependency-matrix.yaml          # Human-readable version
│   ├── health-summary.json             # Quick health overview
│   └── validation-report.json          # Latest validation results
├── history/
│   └── [timestamped snapshots]
├── cache/
│   └── [performance optimization files]
├── exports/
│   ├── graphviz/                       # DOT files for visualization
│   ├── csv/                           # Tabular data exports
│   └── reports/                       # Generated HTML reports
└── config/
    ├── matrix-config.json             # Configuration settings
    ├── exclusion-rules.json           # File/pattern exclusions
    └── validation-rules.json          # Custom validation rules
```

## Key Components

### Dependency Graph Structure
- **Nodes**: Files, modules, components with metadata
- **Edges**: Relationships, dependencies, imports/exports
- **Weights**: Dependency strength, critical path indicators
- **Risk Scores**: Calculated risk levels per component

### Validation Framework
- **Broken Dependencies**: Missing files, invalid paths
- **Orphaned Files**: Unused components, cleanup candidates  
- **Circular Dependencies**: Loop detection and resolution
- **Missing Documentation**: Coverage analysis and recommendations

### Health Monitoring
- **Health Score**: Composite metric (0-100) for project stability
- **Critical Issues**: System-halting problems requiring immediate attention
- **Warning Issues**: Performance or maintenance concerns
- **Risk Analysis**: Critical paths, vulnerability assessments

## Data Integrity

### Integrity Verification
- **Checksums**: SHA-256 file verification
- **Schema Validation**: Structural integrity checks
- **Referential Integrity**: Cross-reference consistency
- **Consistency Checks**: Node-edge relationship validation

### Version Control Integration
- **Git Integration**: Commit tracking, branch awareness
- **Change Tracking**: Diff generation, impact analysis
- **Rollback Capability**: Point-in-time recovery support
- **History Retention**: Configurable retention policies

## Export Formats

### Supported Export Types
- **GraphViz DOT**: Dependency visualization graphs
- **CSV**: Tabular data for spreadsheet analysis
- **HTML Reports**: Interactive web-based dashboards
- **YAML**: Human-readable configuration templates

### Import Compatibility
- **package.json**: NPM dependency imports
- **requirements.txt**: Python package imports
- **go.mod**: Go module imports
- **Third-party matrices**: Generic JSON format imports

## Performance Standards

### Performance Targets
- **Matrix Write**: <500ms for 10MB files
- **Matrix Read**: <200ms for 10MB files
- **Memory Usage**: <500MB for 50k files
- **Concurrent Access**: Multi-reader, single-writer pattern

### Scalability Limits
- **Maximum Nodes**: 1,000,000
- **Maximum Edges**: 5,000,000
- **Maximum File Size**: 1GB
- **History Retention**: 2 years configurable

## Reference Documentation

**Detailed Technical Specifications**: [`matrix-storage-technical-specs.md`](matrix-storage-technical-specs.md)  
**Comprehensive Examples**: [`matrix-storage-examples.md`](matrix-storage-examples.md)  
**Performance Specifications**: [`matrix-storage-performance-specs.md`](matrix-storage-performance-specs.md)  

---

**Format Status**: Production ready  
**Compatibility**: Backward compatible with schema versioning  
**Validation**: JSON Schema available for automated validation  
**Integration**: REST API and webhook support included