# Test Driven Development Protocols

**Authority**: User mandate via CLAUDE_RULES Technical Standards | **Purpose**: Test Driven Development using Red-Green-Refactor cycle for ALL code implementation in Claude Code system

## When to Apply
**Code implementation** → Function/method implementation, class/component creation, algorithm development, business logic, API endpoints, data processing, utilities

## TDD Core Methodology

### Red-Green-Refactor Cycle (Mandatory)
**RED Phase**: Write failing test FIRST (before implementation), test defines expected behavior, ensure failure for right reason, apply Think×4 to test design
**GREEN Phase**: Write minimal code to make test pass, focus on functionality not optimization, ensure complete test passage
**REFACTOR Phase**: Improve code quality while maintaining test passage, apply PTS Framework validation (12 components), optimize for readability/maintainability

### PTS Framework Integration for TDD
**Technical Cluster**: Directness (≤3 steps per test), Precision (100% test accuracy), Sufficiency (complete coverage, minimal code), Excellence (impeccable test quality)
**Communication Cluster**: Exactitude (exact test specifications), Sobriety (zero embellishments), Structure (logical organization), Conciseness (maximum value per test)
**Cognitive Cluster**: Clarity (immediate comprehension), Coherence (test suite consistency), Effectiveness (measurable results), Pragmatism (real-world scenarios)

### Think×4 Application to TDD
**Test Design Analysis** (Required Before Implementation):
**Think**: Basic test requirements and immediate scenarios
**Think Hard**: Edge cases, error conditions, integration implications  
**Think Harder**: System-wide impact, performance considerations, maintainability
**Ultra Think**: Comprehensive test strategy with optimal coverage architecture

## Implementation Standards

### Test Structure Requirements
**Given-When-Then Format**: Clear setup, action, assertion structure
**Descriptive Names**: Test names clearly describe expected behavior
**Single Responsibility**: Each test validates one specific behavior
**Independence**: Tests run independently without interdependencies

### Test Coverage Standards
**Function Coverage**: 100% function execution required
**Branch Coverage**: All conditional paths tested
**Edge Cases**: Boundary conditions and error scenarios mandatory
**Integration Points**: All external dependencies and interfaces tested

### Test Quality Gates
**Test First**: No implementation without corresponding test
**All Green**: All tests pass before code integration
**Refactor Safety**: Refactoring only when all tests pass
**Documentation**: Tests serve as living documentation

## VDD Architecture Integration

### Command Development with TDD
**Self-Contained Commands**: Tests embedded/referenced within ≤80 line limit
**Parallel Execution**: Tests support Task Tool parallel execution
**Autocontainment**: All test dependencies included within command scope

### Sub-Agent TDD Compliance
**Individual Testing**: Each sub-agent implements TDD for code tasks
**Transparency**: Test results visible to user before synthesis
**Parallel Execution**: Multiple agents run tests simultaneously

## Success Criteria
**Implementation**: 100% TDD compliance for all code implementation
**Test Quality**: All tests pass PTS validation (12/12 components)
**Coverage**: ≥95% code coverage with meaningful tests
**Maintainability**: Tests enable confident refactoring and evolution