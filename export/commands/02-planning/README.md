# 02-planning - Planning & Architecture Commands

## Purpose
Strategic planning and architectural design for complex implementations. These commands transform discovery insights into actionable plans with clear execution strategies and risk assessment.

## Commands
- `/architect-solution` - Comprehensive solution architecture ✓ IMPLEMENTED
- `/plan-phases` - Multi-phase implementation planning ✓ IMPLEMENTED
- `/risk-assess` - Risk analysis and mitigation strategies ✓ IMPLEMENTED
- `/resource-plan` - Resource allocation and timeline estimation ✓ IMPLEMENTED
- `/strategy-optimize` - Plan optimization and refinement ✓ IMPLEMENTED

## Category Relations
- **Triggered by**: 01-discovery after context gathering
- **Feeds into**: 04-execution, 05-validation
- **Coordinates with**: 03-analysis for technical assessment
- **Uses**: 12-math for complexity calculations

## Usage Patterns
```
01-discovery/explore → 02-planning/architect → 02-planning/resource → 04-execution/implement
02-planning/risk-assess → 02-planning/strategy-optimize → 05-validation/prepare
02-planning/phases → 02-planning/resource → 03-analysis/complexity → 12-math/calculate
02-planning/strategy-optimize → 04-execution/coordinate → 05-validation/complete
```

## Planning Framework
- **Strategic Level**: High-level architecture and approach
- **Tactical Level**: Implementation phases and dependencies
- **Operational Level**: Detailed task breakdown and sequencing
- **Risk Level**: Mitigation strategies and contingency planning

## Architecture Patterns
- Modular design with clear interfaces
- Parallel execution optimization
- Dependency management and isolation
- Scalability and maintainability considerations

## Planning Outputs
- Architecture diagrams and specifications
- Phase-based implementation roadmaps
- Risk matrices with mitigation strategies
- Resource allocation and timeline estimates
- Optimized strategic plans with efficiency metrics
- Quality gates and validation checkpoints
- Budget estimates and ROI analysis
- Team coordination and communication structures

---
*Category 02: Bridge between discovery and execution*