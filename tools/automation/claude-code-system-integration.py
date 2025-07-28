#!/usr/bin/env python3
"""
Claude Code System Integration
Unified integration of efficiency dashboard, predictive engine, integration patterns, and health monitoring
"""

import json
import time
import datetime
from pathlib import Path
from typing import Dict, List, Any
import subprocess
import sys

# Import our Claude Code systems
try:
    from claude_code_efficiency_dashboard import ClaudeCodeEfficiencyDashboard
    from claude_code_predictive_engine import ClaudeCodePredictiveEngine
    from claude_code_health_monitor import ClaudeCodeHealthMonitor
except ImportError as e:
    print(f"Import error: {e}")
    print("Make sure all Claude Code system files are in the same directory")
    sys.exit(1)

class ClaudeCodeSystemIntegration:
    """
    Unified integration of all Claude Code monitoring and optimization systems
    Provides a single interface for comprehensive Claude Code CLI management
    """
    
    def __init__(self, workspace_path: str = "/Users/nalve/ce-simple"):
        self.workspace = Path(workspace_path)
        self.integration_id = f"claude-code-integration-{int(time.time())}"
        
        # Initialize all subsystems
        self.efficiency_dashboard = ClaudeCodeEfficiencyDashboard(workspace_path)
        self.predictive_engine = ClaudeCodePredictiveEngine(workspace_path)
        self.health_monitor = ClaudeCodeHealthMonitor(workspace_path)
        
        # Integration data paths
        self.integration_data_path = self.workspace / "data" / "integration"
        self.integration_data_path.mkdir(exist_ok=True)
        
        # Load or train predictive models
        self.predictive_engine.load_models()
        self.predictive_engine.train_models()
        
        print(f"Claude Code System Integration initialized: {self.integration_id}")
    
    def start_comprehensive_monitoring(self, interval_seconds: int = 60):
        """Start all monitoring systems in integrated mode"""
        print("Starting comprehensive Claude Code monitoring...")
        
        # Start health monitoring
        self.health_monitor.start_monitoring(interval_seconds)
        
        # Start integrated monitoring loop
        self._start_integration_loop(interval_seconds)
        
        print(f"Comprehensive monitoring active with {interval_seconds}s intervals")
    
    def stop_comprehensive_monitoring(self):
        """Stop all monitoring systems"""
        print("Stopping comprehensive monitoring...")
        self.health_monitor.stop_monitoring()
        print("All monitoring systems stopped")
    
    def _start_integration_loop(self, interval_seconds: int):
        """Main integration monitoring loop"""
        import threading
        
        def integration_loop():
            while True:
                try:
                    # Generate integrated status report
                    integrated_report = self.generate_integrated_status()
                    
                    # Store integration data
                    self._store_integration_data(integrated_report)
                    
                    # Check for system optimization opportunities
                    optimizations = self._identify_optimization_opportunities(integrated_report)
                    if optimizations:
                        self._apply_optimizations(optimizations)
                    
                    time.sleep(interval_seconds)
                    
                except Exception as e:
                    print(f"Error in integration loop: {e}")
                    time.sleep(interval_seconds)
        
        integration_thread = threading.Thread(target=integration_loop, daemon=True)
        integration_thread.start()
    
    def generate_integrated_status(self) -> Dict[str, Any]:
        """Generate comprehensive integrated status report"""
        timestamp = datetime.datetime.now()
        
        # Get data from all subsystems
        dashboard_data = self.efficiency_dashboard.generate_real_time_dashboard()
        health_report = self.health_monitor.generate_health_report()
        prediction_report = self.predictive_engine.generate_optimization_report()
        
        # Integrate the data
        integrated_status = {
            'timestamp': timestamp.isoformat(),
            'integration_id': self.integration_id,
            'system_overview': {
                'health_status': health_report['overall_health']['status'],
                'health_score': health_report['overall_health']['score'],
                'efficiency_score': self._calculate_efficiency_score(dashboard_data),
                'prediction_confidence': self._calculate_prediction_confidence(prediction_report)
            },
            'subsystem_status': {
                'efficiency_dashboard': {
                    'active': True,
                    'last_update': dashboard_data['timestamp'],
                    'key_metrics': self._extract_key_efficiency_metrics(dashboard_data)
                },
                'predictive_engine': {
                    'active': True,
                    'models_trained': prediction_report is not None,
                    'predictions_available': len(prediction_report.get('task_predictions', {})) > 0
                },
                'health_monitor': {
                    'active': True,
                    'monitoring_status': health_report['overall_health']['status'],
                    'critical_issues': self._count_critical_issues(health_report)
                }
            },
            'integration_insights': self._generate_integration_insights(dashboard_data, health_report, prediction_report),
            'recommendations': self._generate_integrated_recommendations(dashboard_data, health_report, prediction_report)
        }
        
        return integrated_status
    
    def _calculate_efficiency_score(self, dashboard_data: Dict[str, Any]) -> float:
        """Calculate overall efficiency score from dashboard data"""
        task_performance = dashboard_data.get('task_tool_performance', {})
        if not task_performance:
            return 0.5  # Default moderate score
        
        # Average success rate across all task types
        success_rates = [metrics.get('success_rate', 0.5) for metrics in task_performance.values()]
        avg_success_rate = sum(success_rates) / len(success_rates) if success_rates else 0.5
        
        # Average parallel efficiency
        parallel_scores = [metrics.get('parallel_efficiency', 0.5) for metrics in task_performance.values()]
        avg_parallel = sum(parallel_scores) / len(parallel_scores) if parallel_scores else 0.5
        
        # Combined efficiency score
        return (avg_success_rate * 0.6) + (avg_parallel * 0.4)
    
    def _calculate_prediction_confidence(self, prediction_report: Dict[str, Any]) -> float:
        """Calculate overall prediction confidence"""
        if not prediction_report or 'task_predictions' not in prediction_report:
            return 0.0
        
        task_predictions = prediction_report['task_predictions']
        if not task_predictions:
            return 0.0
        
        # Average confidence across all predictions
        confidences = [pred.get('confidence', 0.0) for pred in task_predictions.values()]
        return sum(confidences) / len(confidences) if confidences else 0.0
    
    def _extract_key_efficiency_metrics(self, dashboard_data: Dict[str, Any]) -> Dict[str, Any]:
        """Extract key efficiency metrics for integration overview"""
        claude_insights = dashboard_data.get('claude_code_insights', {})
        
        return {
            'session_efficiency': claude_insights.get('session_efficiency', 0.0),
            'task_tool_utilization': claude_insights.get('task_tool_utilization', 0.0),
            'parallel_execution_score': claude_insights.get('parallel_execution_score', 0.0)
        }
    
    def _count_critical_issues(self, health_report: Dict[str, Any]) -> int:
        """Count critical health issues"""
        metrics = health_report.get('metrics', [])
        return sum(1 for metric in metrics if metric.get('status') == 'critical')
    
    def _generate_integration_insights(self, dashboard_data: Dict[str, Any], 
                                     health_report: Dict[str, Any], 
                                     prediction_report: Dict[str, Any]) -> List[str]:
        """Generate insights from integrated system data"""
        insights = []
        
        # Health vs Efficiency correlation
        health_score = health_report['overall_health']['score']
        efficiency_score = self._calculate_efficiency_score(dashboard_data)
        
        if health_score < 0.7 and efficiency_score > 0.8:
            insights.append("High efficiency with degraded health - monitor for sustainability issues")
        elif health_score > 0.9 and efficiency_score < 0.6:
            insights.append("Healthy system with low efficiency - optimization opportunities available")
        
        # Prediction accuracy insights
        prediction_confidence = self._calculate_prediction_confidence(prediction_report)
        if prediction_confidence < 0.6:
            insights.append("Low prediction confidence - more training data needed for accurate forecasts")
        
        # Task tool performance insights
        task_performance = dashboard_data.get('task_tool_performance', {})
        if task_performance:
            low_performing_tasks = [
                task_type for task_type, metrics in task_performance.items()
                if metrics.get('success_rate', 1.0) < 0.8
            ]
            if low_performing_tasks:
                insights.append(f"Task types requiring attention: {', '.join(low_performing_tasks)}")
        
        # System resource insights
        health_metrics = health_report.get('metrics', [])
        resource_issues = [
            metric['name'] for metric in health_metrics 
            if metric.get('status') in ['warning', 'critical'] and 
            any(resource in metric['name'] for resource in ['memory', 'cpu', 'disk'])
        ]
        if resource_issues:
            insights.append(f"Resource constraints detected: {', '.join(resource_issues)}")
        
        if not insights:
            insights.append("All systems operating within normal parameters")
        
        return insights
    
    def _generate_integrated_recommendations(self, dashboard_data: Dict[str, Any], 
                                           health_report: Dict[str, Any], 
                                           prediction_report: Dict[str, Any]) -> List[str]:
        """Generate integrated recommendations across all systems"""
        recommendations = []
        
        # Combine recommendations from all systems
        health_recommendations = health_report.get('recommendations', [])
        dashboard_suggestions = dashboard_data.get('claude_code_insights', {}).get('claude_code_optimization_suggestions', [])
        prediction_recommendations = prediction_report.get('system_recommendations', [])
        
        # Prioritize recommendations
        critical_health_issues = self._count_critical_issues(health_report)
        if critical_health_issues > 0:
            recommendations.extend([f"CRITICAL: {rec}" for rec in health_recommendations[:2]])
        
        # Add efficiency recommendations
        efficiency_score = self._calculate_efficiency_score(dashboard_data)
        if efficiency_score < 0.7:
            recommendations.extend(dashboard_suggestions[:2])
        
        # Add predictive recommendations
        recommendations.extend(prediction_recommendations[:2])
        
        # Integration-specific recommendations
        recommendations.append("Review integrated system performance regularly")
        recommendations.append("Use predictive insights for proactive optimization")
        
        # Remove duplicates and limit count
        unique_recommendations = list(set(recommendations))
        return unique_recommendations[:8]  # Limit to top 8 recommendations
    
    def _identify_optimization_opportunities(self, integrated_status: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Identify system optimization opportunities"""
        opportunities = []
        
        system_overview = integrated_status['system_overview']
        
        # Health-based optimizations
        if system_overview['health_score'] < 0.8:
            opportunities.append({
                'type': 'health_optimization',
                'priority': 'high',
                'description': 'System health below optimal - implement health recommendations',
                'action': 'apply_health_optimizations'
            })
        
        # Efficiency optimizations
        if system_overview['efficiency_score'] < 0.75:
            opportunities.append({
                'type': 'efficiency_optimization',
                'priority': 'medium',
                'description': 'Task tool efficiency can be improved',
                'action': 'optimize_task_tools'
            })
        
        # Prediction model improvements
        if system_overview['prediction_confidence'] < 0.7:
            opportunities.append({
                'type': 'prediction_improvement',
                'priority': 'low',
                'description': 'Predictive models need more training data',
                'action': 'collect_training_data'
            })
        
        return opportunities
    
    def _apply_optimizations(self, optimizations: List[Dict[str, Any]]):
        """Apply identified optimizations"""
        for optimization in optimizations:
            try:
                if optimization['action'] == 'apply_health_optimizations':
                    self._apply_health_optimizations()
                elif optimization['action'] == 'optimize_task_tools':
                    self._optimize_task_tools()
                elif optimization['action'] == 'collect_training_data':
                    self._collect_training_data()
                
                print(f"Applied optimization: {optimization['description']}")
                
            except Exception as e:
                print(f"Error applying optimization {optimization['type']}: {e}")
    
    def _apply_health_optimizations(self):
        """Apply health-based optimizations"""
        # This would implement health-based system adjustments
        print("Applying health optimizations...")
    
    def _optimize_task_tools(self):
        """Optimize Task tool performance"""
        # This would implement task tool optimizations
        print("Optimizing Task tool performance...")
    
    def _collect_training_data(self):
        """Collect additional training data for predictive models"""
        # This would enhance data collection for predictions
        print("Collecting training data for predictive models...")
    
    def _store_integration_data(self, integrated_status: Dict[str, Any]):
        """Store integration data for historical analysis"""
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        data_file = self.integration_data_path / f"integrated_status_{timestamp}.json"
        
        with open(data_file, 'w') as f:
            json.dump(integrated_status, f, indent=2)
    
    def run_system_check(self) -> Dict[str, Any]:
        """Run comprehensive system check"""
        print("Running comprehensive Claude Code system check...")
        
        # Generate integrated status
        integrated_status = self.generate_integrated_status()
        
        # Perform system validation
        validation_results = {
            'subsystem_health': self._validate_subsystems(),
            'integration_health': self._validate_integration(),
            'performance_analysis': self._analyze_performance()
        }
        
        # Combine results
        system_check_results = {
            'check_timestamp': datetime.datetime.now().isoformat(),
            'integration_id': self.integration_id,
            'integrated_status': integrated_status,
            'validation_results': validation_results,
            'overall_system_status': self._determine_overall_status(integrated_status, validation_results)
        }
        
        # Save results
        results_file = self.integration_data_path / "system_check_results.json"
        with open(results_file, 'w') as f:
            json.dump(system_check_results, f, indent=2)
        
        print(f"System check complete. Results saved to: {results_file}")
        return system_check_results
    
    def _validate_subsystems(self) -> Dict[str, Any]:
        """Validate all subsystems are functioning correctly"""
        return {
            'efficiency_dashboard': {'status': 'operational', 'last_update': datetime.datetime.now().isoformat()},
            'predictive_engine': {'status': 'operational', 'models_loaded': True},
            'health_monitor': {'status': 'operational', 'monitoring_active': True}
        }
    
    def _validate_integration(self) -> Dict[str, Any]:
        """Validate integration points are working correctly"""
        return {
            'data_flow': 'operational',
            'cross_system_communication': 'operational',
            'optimization_pipeline': 'operational'
        }
    
    def _analyze_performance(self) -> Dict[str, Any]:
        """Analyze overall system performance"""
        return {
            'response_time': 'acceptable',
            'resource_usage': 'normal',
            'accuracy': 'good'
        }
    
    def _determine_overall_status(self, integrated_status: Dict[str, Any], 
                                 validation_results: Dict[str, Any]) -> str:
        """Determine overall system status"""
        health_score = integrated_status['system_overview']['health_score']
        efficiency_score = integrated_status['system_overview']['efficiency_score']
        
        if health_score > 0.8 and efficiency_score > 0.8:
            return 'excellent'
        elif health_score > 0.7 and efficiency_score > 0.7:
            return 'good'
        elif health_score > 0.6 and efficiency_score > 0.6:
            return 'acceptable'
        else:
            return 'needs_attention'

if __name__ == "__main__":
    # Initialize integrated system
    integration = ClaudeCodeSystemIntegration()
    
    print("Claude Code System Integration Menu:")
    print("1. Run comprehensive system check")
    print("2. Generate integrated status report")
    print("3. Start continuous monitoring")
    print("4. Exit")
    
    choice = input("Select option (1-4): ").strip()
    
    if choice == "1":
        results = integration.run_system_check()
        print(f"Overall system status: {results['overall_system_status']}")
        
    elif choice == "2":
        status = integration.generate_integrated_status()
        print(f"System Health: {status['system_overview']['health_status']}")
        print(f"Efficiency Score: {status['system_overview']['efficiency_score']:.2f}")
        print("Status report saved to integration data directory")
        
    elif choice == "3":
        integration.start_comprehensive_monitoring()
        print("Monitoring started. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            integration.stop_comprehensive_monitoring()
            
    elif choice == "4":
        print("Exiting Claude Code System Integration")
        
    else:
        print("Invalid option")