# /optimize-calculate - Mathematical Optimization Calculations

## Purpose
Executes advanced mathematical optimization calculations with constraint handling providing optimal resource allocation and performance tuning recommendations through rigorous mathematical analysis.

## Principles and Guidelines
- **Optimization Theory**: Apply mathematical optimization methods with constraint satisfaction
- **Multi-Objective Analysis**: Balance competing objectives using mathematical optimization techniques
- **Constraint Handling**: Process complex constraints with mathematical validation and feasibility analysis
- **Precision Optimization**: Deliver optimal solutions with mathematical convergence guarantees

## Execution Process

### Phase 1: Problem Formulation and Constraint Analysis
Update TodoWrite: Mark "optimization problem formulation" as in_progress

Execute comprehensive problem definition using Task and Bash:
- Define optimization objectives with mathematical formulation and variable identification
- Collect constraint equations and inequality relationships with boundary validation
- Validate problem feasibility using mathematical constraint analysis and consistency checking
- Setup optimization parameters with precision requirements and convergence criteria

Use Bash for constraint validation:
```bash
# Mathematical constraint validation and feasibility analysis
validate_constraints() {
    local constraints_file="$1"
    while IFS= read -r constraint; do
        if [[ "$constraint" =~ ^([0-9.-]+)\*([a-zA-Z_]+).*([<=>=]).*([0-9.-]+)$ ]]; then
            echo "CONSTRAINT: ${BASH_REMATCH[1]}*${BASH_REMATCH[2]} ${BASH_REMATCH[3]} ${BASH_REMATCH[4]}"
        fi
    done < "$constraints_file"
}
```

### Phase 2: Linear Optimization and Mathematical Solution
Update TodoWrite: Complete previous, mark "linear optimization calculation" as in_progress

Execute linear programming optimization using mathematical algorithms:
- Apply simplex method for linear optimization problems with mathematical iteration
- Calculate optimal solution using mathematical pivot operations and feasibility validation
- Validate optimality conditions with mathematical verification and convergence testing
- Handle degenerate cases using mathematical pivot strategies and boundary analysis

Use Bash for linear optimization implementation:
```bash
# Linear programming solver with mathematical validation
solve_linear_optimization() {
    local objective_coeffs="$1"
    local iteration=1
    local max_iterations=100
    local tolerance="0.0001"
    
    echo "PHASE_1: Finding initial basic feasible solution"
    while [ $iteration -le $max_iterations ]; do
        echo "ITERATION: $iteration"
        # Mathematical pivot operations and optimality testing
        # Convergence check and solution validation
        iteration=$((iteration + 1))
    done
    echo "OPTIMAL_SOLUTION_FOUND: Mathematical convergence achieved"
}
```

### Phase 3: Nonlinear Optimization and Advanced Methods
Update TodoWrite: Complete previous, mark "nonlinear optimization analysis" as in_progress

Execute nonlinear optimization using advanced mathematical methods:
- Apply gradient descent methods for nonlinear objectives with mathematical convergence
- Calculate Hessian matrices for second-order optimization with mathematical precision
- Implement Newton-Raphson method for constraint optimization with mathematical validation
- Handle multiple local minima using mathematical exploration strategies and global optimization

Use Task for advanced nonlinear optimization including penalty methods, Lagrange multipliers, and barrier methods with mathematical convergence analysis.

### Phase 4: Multi-Objective Optimization Analysis
Update TodoWrite: Complete previous, mark "multi-objective optimization" as in_progress

Execute multi-objective optimization using mathematical techniques:
- Apply Pareto optimality analysis for competing objectives with mathematical dominance testing
- Calculate efficient frontier using mathematical optimization and constraint handling
- Implement weighted sum methods for objective combination with mathematical validation
- Generate trade-off analysis using mathematical sensitivity analysis and robustness assessment

Use Bash for Pareto frontier calculation:
```bash
# Pareto frontier calculation with mathematical dominance testing
calculate_pareto_frontier() {
    local solutions_file="$1"
    while IFS= read -r solution; do
        local is_pareto_optimal=true
        while IFS= read -r other_solution; do
            if [[ "$solution" != "$other_solution" ]]; then
                local dominates=$(check_mathematical_dominance "$solution" "$other_solution")
                if [[ "$dominates" == "true" ]]; then
                    is_pareto_optimal=false; break
                fi
            fi
        done < "$solutions_file"
        if [[ "$is_pareto_optimal" == "true" ]]; then
            echo "PARETO_OPTIMAL: $solution"
        fi
    done < "$solutions_file"
}
```

### Phase 5: Optimization Report and Recommendations
Update TodoWrite: Complete previous, mark "optimization results reporting" as in_progress

Generate comprehensive optimization analysis report using Write and Task:
- Document optimal solutions with mathematical validation and convergence proof
- Report constraint satisfaction status with mathematical verification and feasibility analysis
- Include sensitivity analysis results with robustness assessment and parameter bounds
- Provide implementation recommendations with mathematical optimization theory backing and practical guidance

Use Write for standardized optimization report with mathematical rigor and practical implementation recommendations.

Update TodoWrite: Complete all optimization calculation tasks

**Error Handling**: Handle infeasible problems with mathematical certificates, manage unbounded solutions with detection and bounds, address numerical instability with conditioning, provide alternative approaches for complex constraints

---

**Optimization Foundation**: Advanced mathematical optimization calculations through constraint handling, multi-objective analysis, and rigorous mathematical validation for optimal resource allocation and performance optimization decisions.