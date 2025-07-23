#!/usr/bin/env python3
"""
Operational Reports Intelligence Synthesizer - Historical Intelligence Phase 1
============================================================================

**Purpose**: Parse and synthesize operational reports and system metrics for 
pattern recognition and optimization intelligence extraction.

**Authority Integration**: Historical Intelligence Architecture (Principle #110)
**P55/P56 Compliance**: MANDATORY operational intelligence integration

This script implements Tier 1 operational reports intelligence analysis for 
/system-update, /knowledge-sync, and /intelligent-reorganization commands.
"""

import os
import json
import glob
import datetime
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import argparse
from collections import defaultdict, Counter


@dataclass
class OperationalPattern:
    """Structure for operational pattern analysis"""
    pattern_type: str
    frequency: int
    success_rate: float
    performance_metrics: Dict[str, float]
    trend_analysis: Dict[str, Any]
    related_components: List[str]
    optimization_potential: float


@dataclass
class ReportIntelligenceResults:
    """Complete operational intelligence analysis results"""
    analysis_period: str
    total_reports: int
    system_health_trends: Dict[str, Any]
    compliance_patterns: List[OperationalPattern]
    performance_analysis: Dict[str, float]
    optimization_opportunities: List[str]
    degradation_alerts: List[str]
    success_patterns: List[str]
    metadata: Dict[str, Any]


class ReportSynthesizer:
    """Core operational reports intelligence engine"""
    
    def __init__(self, base_path: str = None):
        """Initialize synthesizer with base project path"""
        self.base_path = base_path or "/Users/nalve/claude-context-engineering"
        self.reports_cache = {}
        self.analysis_results = None
        
    def find_operational_reports(self) -> Dict[str, List[str]]:
        """Find all operational reports and result files"""
        report_sources = {
            'operations_reports': [],
            'script_results': [],
            'compliance_reports': [],
            'performance_reports': [],
            'governance_reports': []
        }
        
        # Operations reports
        ops_pattern = os.path.join(self.base_path, "operations/reports/**/*.md")
        report_sources['operations_reports'] = glob.glob(ops_pattern, recursive=True)
        
        # Script results  
        results_pattern = os.path.join(self.base_path, "scripts/results/**/*.json")
        report_sources['script_results'] = glob.glob(results_pattern, recursive=True)
        
        # Compliance reports
        compliance_pattern = os.path.join(self.base_path, "scripts/results/compliance/**/*.json")
        report_sources['compliance_reports'] = glob.glob(compliance_pattern, recursive=True)
        
        # Performance reports
        perf_pattern = os.path.join(self.base_path, "scripts/results/**/performance*.json")
        report_sources['performance_reports'] = glob.glob(perf_pattern, recursive=True)
        
        # Governance reports
        gov_pattern = os.path.join(self.base_path, "scripts/results/governance/**/*.json")
        report_sources['governance_reports'] = glob.glob(gov_pattern, recursive=True)
        
        # Log files for additional context
        log_pattern = os.path.join(self.base_path, "scripts/results/**/*.log")
        log_files = glob.glob(log_pattern, recursive=True)
        report_sources['log_files'] = log_files
        
        total_files = sum(len(files) for files in report_sources.values())
        print(f"📊 Archivos de reportes encontrados: {total_files}")
        
        return report_sources
    
    def parse_json_report(self, file_path: str) -> Optional[Dict[str, Any]]:
        """Parse JSON report file safely"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                data['_source_file'] = file_path
                data['_file_mtime'] = os.path.getmtime(file_path)
                return data
        except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
            print(f"⚠️  Error parsing {file_path}: {e}")
            return None
    
    def parse_markdown_report(self, file_path: str) -> Dict[str, Any]:
        """Parse markdown report for key metrics and patterns"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Extract key metrics using regex patterns
            metrics = {}
            
            # Success/completion patterns
            success_patterns = re.findall(r'(✅|COMPLETED?|SUCCESS|ACHIEVED)\s*:?\s*([^\n]+)', content, re.IGNORECASE)
            metrics['success_indicators'] = [match[1].strip() for match in success_patterns]
            
            # Error/warning patterns
            error_patterns = re.findall(r'(❌|ERROR|FAILED?|WARNING)\s*:?\s*([^\n]+)', content, re.IGNORECASE)
            metrics['error_indicators'] = [match[1].strip() for match in error_patterns]
            
            # Numeric metrics
            number_patterns = re.findall(r'(\d+(?:\.\d+)?)\s*(%|percent|commits|files|commands)', content, re.IGNORECASE)
            metrics['numeric_metrics'] = [(float(match[0]), match[1]) for match in number_patterns]
            
            # Performance indicators
            perf_patterns = re.findall(r'(performance|efficiency|speed|optimization)\s*:?\s*([^\n]+)', content, re.IGNORECASE)
            metrics['performance_indicators'] = [match[1].strip() for match in perf_patterns]
            
            metrics['_source_file'] = file_path
            metrics['_file_mtime'] = os.path.getmtime(file_path)
            metrics['_content_length'] = len(content)
            
            return metrics
            
        except (FileNotFoundError, PermissionError) as e:
            print(f"⚠️  Error parsing markdown {file_path}: {e}")
            return {}
    
    def analyze_system_health_trends(self, reports: Dict[str, List[str]]) -> Dict[str, Any]:
        """Analyze system health trends from reports"""
        health_trends = {
            'compliance_score_trend': [],
            'performance_trend': [],
            'error_frequency': defaultdict(int),
            'success_frequency': defaultdict(int),
            'component_health': defaultdict(list)
        }
        
        # Process JSON reports
        for report_file in reports.get('script_results', []):
            report_data = self.parse_json_report(report_file)
            if not report_data:
                continue
            
            # Extract compliance scores
            if 'compliance' in report_data or 'score' in report_data:
                score = self._extract_numeric_value(report_data, ['compliance_score', 'score', 'success_rate'])
                if score is not None:
                    timestamp = report_data.get('timestamp', os.path.getmtime(report_file))
                    health_trends['compliance_score_trend'].append({
                        'timestamp': timestamp,
                        'score': score,
                        'source': os.path.basename(report_file)
                    })
            
            # Extract performance metrics
            if 'performance' in report_data or 'timing' in report_data:
                perf_value = self._extract_numeric_value(report_data, ['execution_time', 'duration', 'performance_score'])
                if perf_value is not None:
                    timestamp = report_data.get('timestamp', os.path.getmtime(report_file))
                    health_trends['performance_trend'].append({
                        'timestamp': timestamp,
                        'value': perf_value,
                        'source': os.path.basename(report_file)
                    })
        
        # Process markdown reports
        for report_file in reports.get('operations_reports', []):
            report_data = self.parse_markdown_report(report_file)
            
            # Count success/error indicators
            for indicator in report_data.get('success_indicators', []):
                health_trends['success_frequency'][indicator[:50]] += 1
            
            for indicator in report_data.get('error_indicators', []):
                health_trends['error_frequency'][indicator[:50]] += 1
        
        return health_trends
    
    def identify_compliance_patterns(self, reports: Dict[str, List[str]]) -> List[OperationalPattern]:
        """Identify compliance patterns from reports"""
        patterns = []
        
        # Process compliance reports
        compliance_data = []
        for report_file in reports.get('compliance_reports', []):
            report_data = self.parse_json_report(report_file)
            if report_data:
                compliance_data.append(report_data)
        
        # Analyze P55/P56 compliance patterns
        p55_p56_scores = []
        for report in compliance_data:
            if 'p55' in str(report).lower() or 'p56' in str(report).lower():
                score = self._extract_numeric_value(report, ['compliance_score', 'score', 'success_rate'])
                if score is not None:
                    p55_p56_scores.append(score)
        
        if p55_p56_scores:
            avg_score = sum(p55_p56_scores) / len(p55_p56_scores)
            pattern = OperationalPattern(
                pattern_type="P55/P56 Compliance",
                frequency=len(p55_p56_scores),
                success_rate=avg_score,
                performance_metrics={'average_score': avg_score, 'report_count': len(p55_p56_scores)},
                trend_analysis={'scores': p55_p56_scores},
                related_components=['commands', 'execution', 'tool_calls'],
                optimization_potential=1.0 - avg_score
            )
            patterns.append(pattern)
        
        # Analyze mathematical validation patterns
        math_validation_scores = []
        for report in compliance_data:
            if 'math' in str(report).lower() or 'formula' in str(report).lower():
                score = self._extract_numeric_value(report, ['validation_score', 'success_rate', 'accuracy'])
                if score is not None:
                    math_validation_scores.append(score)
        
        if math_validation_scores:
            avg_score = sum(math_validation_scores) / len(math_validation_scores)
            pattern = OperationalPattern(
                pattern_type="Mathematical Validation",
                frequency=len(math_validation_scores),
                success_rate=avg_score,
                performance_metrics={'average_accuracy': avg_score},
                trend_analysis={'scores': math_validation_scores},
                related_components=['verification', 'formulas', 'core'],
                optimization_potential=1.0 - avg_score
            )
            patterns.append(pattern)
        
        return patterns
    
    def analyze_performance_metrics(self, reports: Dict[str, List[str]]) -> Dict[str, float]:
        """Analyze performance metrics from reports"""
        performance_data = {
            'average_execution_time': 0.0,
            'success_rate': 0.0,
            'error_rate': 0.0,
            'optimization_score': 0.0,
            'throughput': 0.0
        }
        
        execution_times = []
        success_counts = 0
        total_operations = 0
        
        # Process performance reports
        for report_file in reports.get('performance_reports', []):
            report_data = self.parse_json_report(report_file)
            if not report_data:
                continue
            
            # Extract execution times
            exec_time = self._extract_numeric_value(report_data, ['execution_time', 'duration', 'time'])
            if exec_time is not None:
                execution_times.append(exec_time)
            
            # Count successes and operations
            if 'success' in report_data or 'passed' in report_data:
                success_counts += 1
            total_operations += 1
        
        # Calculate metrics
        if execution_times:
            performance_data['average_execution_time'] = sum(execution_times) / len(execution_times)
        
        if total_operations > 0:
            performance_data['success_rate'] = success_counts / total_operations
            performance_data['error_rate'] = 1.0 - performance_data['success_rate']
        
        # Calculate optimization score (composite metric)
        performance_data['optimization_score'] = (
            performance_data['success_rate'] * 0.6 +
            (1.0 - min(performance_data['average_execution_time'] / 10.0, 1.0)) * 0.4
        )
        
        return performance_data
    
    def identify_optimization_opportunities(self, health_trends: Dict[str, Any], 
                                          patterns: List[OperationalPattern]) -> List[str]:
        """Identify optimization opportunities from analysis"""
        opportunities = []
        
        # Compliance-based opportunities
        for pattern in patterns:
            if pattern.success_rate < 0.9:
                opportunities.append(
                    f"{pattern.pattern_type} score ({pattern.success_rate:.2f}) below target - optimization needed"
                )
            
            if pattern.optimization_potential > 0.2:
                opportunities.append(
                    f"{pattern.pattern_type} has {pattern.optimization_potential:.2f} optimization potential"
                )
        
        # Error frequency opportunities
        error_freq = health_trends.get('error_frequency', {})
        if error_freq:
            top_errors = sorted(error_freq.items(), key=lambda x: x[1], reverse=True)[:3]
            for error, count in top_errors:
                if count > 5:
                    opportunities.append(f"Recurring error pattern: '{error}' ({count} occurrences)")
        
        # Performance opportunities
        perf_trend = health_trends.get('performance_trend', [])
        if len(perf_trend) > 5:
            recent_perf = [p['value'] for p in perf_trend[-5:]]
            avg_recent = sum(recent_perf) / len(recent_perf)
            if avg_recent > 5.0:  # Assuming seconds
                opportunities.append(f"Recent performance degradation detected: {avg_recent:.2f}s average")
        
        # Success pattern opportunities
        success_freq = health_trends.get('success_frequency', {})
        if success_freq:
            opportunities.append("Successful patterns identified for replication across system")
        
        return opportunities
    
    def detect_degradation_patterns(self, health_trends: Dict[str, Any]) -> List[str]:
        """Detect system degradation patterns"""
        degradation_alerts = []
        
        # Compliance score degradation
        compliance_trend = health_trends.get('compliance_score_trend', [])
        if len(compliance_trend) >= 3:
            recent_scores = [t['score'] for t in compliance_trend[-3:]]
            if len(recent_scores) >= 2 and recent_scores[-1] < recent_scores[0] * 0.9:
                degradation_alerts.append(f"Compliance score declining: {recent_scores[0]:.2f} → {recent_scores[-1]:.2f}")
        
        # Performance degradation
        perf_trend = health_trends.get('performance_trend', [])
        if len(perf_trend) >= 3:
            recent_times = [t['value'] for t in perf_trend[-3:]]
            if len(recent_times) >= 2 and recent_times[-1] > recent_times[0] * 1.2:
                degradation_alerts.append(f"Performance degrading: {recent_times[0]:.2f}s → {recent_times[-1]:.2f}s")
        
        # Error frequency increase
        error_freq = health_trends.get('error_frequency', {})
        high_error_count = sum(1 for count in error_freq.values() if count > 10)
        if high_error_count > 3:
            degradation_alerts.append(f"High error frequency detected: {high_error_count} error types with >10 occurrences")
        
        return degradation_alerts
    
    def extract_success_patterns(self, health_trends: Dict[str, Any]) -> List[str]:
        """Extract successful operational patterns"""
        success_patterns = []
        
        # High success rate patterns
        success_freq = health_trends.get('success_frequency', {})
        top_successes = sorted(success_freq.items(), key=lambda x: x[1], reverse=True)[:5]
        
        for success, count in top_successes:
            if count > 3:
                success_patterns.append(f"Successful pattern: '{success}' ({count} occurrences)")
        
        # Stable compliance patterns
        compliance_trend = health_trends.get('compliance_score_trend', [])
        if compliance_trend:
            high_compliance = [t for t in compliance_trend if t['score'] > 0.9]
            if len(high_compliance) > len(compliance_trend) * 0.7:
                success_patterns.append("Consistent high compliance scores maintained")
        
        # Performance stability
        perf_trend = health_trends.get('performance_trend', [])
        if perf_trend:
            stable_perf = [t for t in perf_trend if t['value'] < 2.0]  # Under 2 seconds
            if len(stable_perf) > len(perf_trend) * 0.8:
                success_patterns.append("Stable performance metrics maintained")
        
        return success_patterns
    
    def _extract_numeric_value(self, data: Dict[str, Any], keys: List[str]) -> Optional[float]:
        """Extract numeric value from nested dictionary"""
        for key in keys:
            if key in data:
                value = data[key]
                if isinstance(value, (int, float)):
                    return float(value)
                elif isinstance(value, str):
                    # Try to extract number from string
                    match = re.search(r'(\d+(?:\.\d+)?)', value)
                    if match:
                        return float(match.group(1))
        return None
    
    def generate_operational_intelligence(self, timeframe_days: int = 30) -> ReportIntelligenceResults:
        """Generate comprehensive operational intelligence analysis"""
        print(f"📊 **OPERATIONAL INTELLIGENCE ANALYSIS** → Análisis de reportes ({timeframe_days} días)")
        
        # Find all reports
        reports = self.find_operational_reports()
        total_reports = sum(len(files) for files in reports.values())
        
        if total_reports == 0:
            print("⚠️  No se encontraron reportes operacionales")
            return ReportIntelligenceResults(
                f"últimos {timeframe_days} días", 0, {}, [], {}, [], [], [], {}
            )
        
        print(f"📋 Total de reportes analizados: {total_reports}")
        
        # Analyze operational patterns
        health_trends = self.analyze_system_health_trends(reports)
        compliance_patterns = self.identify_compliance_patterns(reports)
        performance_analysis = self.analyze_performance_metrics(reports)
        optimization_opportunities = self.identify_optimization_opportunities(health_trends, compliance_patterns)
        degradation_alerts = self.detect_degradation_patterns(health_trends)
        success_patterns = self.extract_success_patterns(health_trends)
        
        results = ReportIntelligenceResults(
            analysis_period=f"últimos {timeframe_days} días",
            total_reports=total_reports,
            system_health_trends=health_trends,
            compliance_patterns=compliance_patterns,
            performance_analysis=performance_analysis,
            optimization_opportunities=optimization_opportunities,
            degradation_alerts=degradation_alerts,
            success_patterns=success_patterns,
            metadata={
                'analysis_timestamp': datetime.datetime.now().isoformat(),
                'report_sources': {k: len(v) for k, v in reports.items()},
                'base_path': self.base_path
            }
        )
        
        self.analysis_results = results
        return results
    
    def export_analysis_results(self, output_path: str) -> bool:
        """Export operational intelligence results to JSON"""
        if not self.analysis_results:
            print("❌ No hay resultados de análisis para exportar")
            return False
        
        try:
            # Convert dataclasses to dict for JSON serialization
            export_data = {
                'analysis_period': self.analysis_results.analysis_period,
                'total_reports': self.analysis_results.total_reports,
                'system_health_trends': self.analysis_results.system_health_trends,
                'compliance_patterns': [
                    {
                        'pattern_type': p.pattern_type,
                        'frequency': p.frequency,
                        'success_rate': p.success_rate,
                        'performance_metrics': p.performance_metrics,
                        'trend_analysis': p.trend_analysis,
                        'related_components': p.related_components,
                        'optimization_potential': p.optimization_potential
                    } for p in self.analysis_results.compliance_patterns
                ],
                'performance_analysis': self.analysis_results.performance_analysis,
                'optimization_opportunities': self.analysis_results.optimization_opportunities,
                'degradation_alerts': self.analysis_results.degradation_alerts,
                'success_patterns': self.analysis_results.success_patterns,
                'metadata': self.analysis_results.metadata
            }
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Resultados de operational intelligence exportados a: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exportando resultados: {e}")
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Análisis de Operational Intelligence')
    parser.add_argument('--timeframe', '-t', type=int, default=30,
                       help='Período de análisis en días (default: 30)')
    parser.add_argument('--output', '-o', type=str,
                       help='Archivo de salida para resultados (JSON)')
    parser.add_argument('--base-path', type=str,
                       help='Ruta base del proyecto')
    
    args = parser.parse_args()
    
    print("📊 **OPERATIONAL INTELLIGENCE SYNTHESIZER** - Fase 1 Implementación")
    print("=" * 60)
    
    # Initialize synthesizer
    synthesizer = ReportSynthesizer(args.base_path)
    
    # Generate intelligence
    results = synthesizer.generate_operational_intelligence(args.timeframe)
    
    # Display summary
    print("\n📊 **RESUMEN DE ANÁLISIS OPERACIONAL**:")
    print(f"⟳ Reportes analizados: {results.total_reports}")
    print(f"⟳ Período: {results.analysis_period}")
    print(f"⟳ Patrones de compliance: {len(results.compliance_patterns)}")
    print(f"⟳ Oportunidades de optimización: {len(results.optimization_opportunities)}")
    print(f"⟳ Alertas de degradación: {len(results.degradation_alerts)}")
    print(f"⟳ Patrones de éxito: {len(results.success_patterns)}")
    
    if results.performance_analysis:
        print(f"⟳ Score de optimización: {results.performance_analysis.get('optimization_score', 0):.2f}")
    
    # Export results if requested
    if args.output:
        synthesizer.export_analysis_results(args.output)
    else:
        # Default output location
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        default_output = f"/Users/nalve/claude-context-engineering/scripts/results/intelligence/operational-intelligence-{timestamp}.json"
        os.makedirs(os.path.dirname(default_output), exist_ok=True)
        synthesizer.export_analysis_results(default_output)
    
    print("\n🎯 **ANÁLISIS OPERACIONAL COMPLETADO** → Inteligencia operacional lista para integración")


if __name__ == "__main__":
    main()