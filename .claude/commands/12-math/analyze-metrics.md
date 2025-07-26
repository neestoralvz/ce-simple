# /analyze-metrics - Performance & Quality Metrics Analysis

## Purpose
Orchestrates comprehensive performance and quality metrics analysis with statistical validation providing quantitative assessment for system optimization and decision-making processes.

## Principles and Guidelines
- **Statistical Rigor**: Apply statistical validation with confidence intervals and significance testing
- **Multi-Domain Analysis**: Assess performance, quality, efficiency, and reliability metrics
- **Trend Detection**: Identify patterns and anomalies using mathematical analysis techniques
- **Actionable Insights**: Generate quantified recommendations with mathematical backing

## Execution Process

### Phase 1: Data Collection and Preprocessing
Update TodoWrite: Mark "metrics data collection" as in_progress

Execute comprehensive data gathering using Read, Bash, and Grep:
- Collect performance metrics (execution time, memory usage, throughput)
- Gather quality indicators (error rates, success ratios, compliance scores)
- Extract efficiency measurements (resource utilization, processing rates)
- Assess reliability data (uptime, failure rates, recovery times)

Use Bash for data validation and preprocessing:
```bash
# Data validation with statistical preprocessing
validate_numeric_data() {
    local data_file="$1"
    awk '{if($1 ~ /^[0-9]+\.?[0-9]*$/) sum+=$1; count++} END {print sum/count}' "$data_file"
}

# Outlier detection using IQR method
detect_outliers() {
    local dataset="$1"
    sort -n "$dataset" | awk '{data[NR]=$1} END {
        q1_pos = int((NR+1)*0.25); q3_pos = int((NR+1)*0.75)
        q1 = data[q1_pos]; q3 = data[q3_pos]; iqr = q3 - q1
        lower = q1 - 1.5*iqr; upper = q3 + 1.5*iqr
        for(i=1; i<=NR; i++) if(data[i] < lower || data[i] > upper) print data[i]
    }'
}
```

### Phase 2: Statistical Analysis and Validation
Update TodoWrite: Complete previous, mark "statistical metrics analysis" as in_progress

Execute mathematical analysis using Task and Bash:
- Calculate descriptive statistics (mean, median, standard deviation, variance)
- Perform distribution analysis and normality testing
- Apply confidence interval calculations for metric reliability
- Execute correlation analysis between different metric categories

Use Bash for statistical calculations:
```bash
# Comprehensive statistical analysis with 4-decimal precision
calculate_statistics() {
    local dataset="$1"
    local count=$(wc -l < "$dataset")
    local mean=$(awk '{sum+=$1} END {printf "%.4f", sum/NR}' "$dataset")
    local variance=$(awk -v mean="$mean" '{sum+=($1-mean)^2} END {printf "%.4f", sum/(NR-1)}' "$dataset")
    local std_dev=$(echo "scale=4; sqrt($variance)" | bc)
    local confidence_margin=$(echo "scale=4; 1.96 * $std_dev / sqrt($count)" | bc)
    
    echo "MEAN: $mean"
    echo "STD_DEV: $std_dev"
    echo "CONFIDENCE_INTERVAL: $(echo "$mean - $confidence_margin" | bc) to $(echo "$mean + $confidence_margin" | bc)"
}
```

### Phase 3: Performance Trend Analysis
Update TodoWrite: Complete previous, mark "performance trend analysis" as in_progress

Execute trend identification using mathematical analysis:
- Analyze time series patterns using moving averages and trend lines
- Calculate performance degradation or improvement rates
- Identify seasonal patterns and cyclical behaviors
- Assess metric stability using coefficient of variation

Use Task for trend analysis with mathematical precision:
- Apply linear regression for trend identification
- Calculate correlation coefficients between metrics and time
- Perform change point detection for performance shifts
- Generate predictive trend extrapolation with uncertainty bounds

### Phase 4: Quality Assessment and Scoring
Update TodoWrite: Complete previous, mark "quality metrics assessment" as in_progress

Execute quality quantification using standardized metrics:
- Calculate composite quality scores using weighted averages
- Assess metric reliability using statistical measures
- Determine performance benchmarks based on historical data
- Generate quality grades with mathematical justification

Use Bash for quality scoring:
```bash
# Quality scoring with weighted metrics assessment
calculate_quality_score() {
    local performance_weight=0.35
    local reliability_weight=0.30
    local efficiency_weight=0.20
    local compliance_weight=0.15
    
    local composite_score=$(echo "scale=4; $performance_score * $performance_weight + 
                                         $reliability_score * $reliability_weight + 
                                         $efficiency_score * $efficiency_weight + 
                                         $compliance_score * $compliance_weight" | bc)
    
    # Convert to letter grade with threshold boundaries
    if (( $(echo "$composite_score >= 9.0000" | bc -l) )); then
        grade="A+"
    elif (( $(echo "$composite_score >= 8.0000" | bc -l) )); then
        grade="A"
    elif (( $(echo "$composite_score >= 7.0000" | bc -l) )); then
        grade="B"
    else
        grade="C"
    fi
}
```

### Phase 5: Report Generation and Recommendations
Update TodoWrite: Complete previous, mark "metrics analysis reporting" as in_progress

Generate comprehensive metrics analysis report using Write and Task:
- Document statistical analysis results with confidence measures
- Report performance trends with mathematical trend analysis
- Include quality assessment scores with statistical validation
- Provide optimization recommendations based on quantitative analysis

Use Write for standardized metrics report with statistical validation and actionable insights.

Update TodoWrite: Complete all metrics analysis tasks

**Error Handling**: Estimate missing data points using statistical interpolation, validate anomalous readings with outlier detection, handle insufficient data with partial analysis, provide confidence bounds for all statistical measures

---

**Analytical Foundation**: Performance and quality metrics analysis through statistical validation, trend detection, and quantified assessment generation for data-driven optimization decisions.