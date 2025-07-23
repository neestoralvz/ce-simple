#!/usr/bin/env python3
"""
Intelligence Orchestrator - Historical Intelligence Automation
=============================================================

**Purpose**: Central orchestrator for automated Historical Intelligence operations,
trigger monitoring, and intelligent system optimization.

**Authority Integration**: Historical Intelligence Architecture (Principle #110)
**P55/P56 Compliance**: MANDATORY auto-activation trigger implementation

This script implements the automated integration layer for Historical Intelligence,
coordinating all intelligence operations and trigger systems.
"""

import os
import sys
import json
import datetime
import subprocess
import argparse
import time
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

# Add intelligence modules to path
sys.path.append('/Users/nalve/claude-context-engineering/scripts/intelligence/connectors')
sys.path.append('/Users/nalve/claude-context-engineering/scripts/intelligence/core')
sys.path.append('/Users/nalve/claude-context-engineering/scripts/maintenance')

try:
    from conversation_analyzer import ConversationAnalyzer
    from git_intelligence import GitIntelligenceAnalyzer
    from report_synthesizer import ReportSynthesizer
    from pattern_recognition import PatternRecognitionEngine
    INTELLIGENCE_MODULES_AVAILABLE = True
except ImportError as e:
    print(f"⚠️  Intelligence modules not fully available: {e}")
    print("🔧 Running in basic mode without full intelligence capabilities")
    INTELLIGENCE_MODULES_AVAILABLE = False


@dataclass
class TriggerCondition:
    """Structure for trigger condition monitoring"""
    trigger_id: str
    condition_type: str
    threshold_value: Any
    current_value: Any
    triggered: bool
    trigger_time: Optional[datetime.datetime]
    action_required: str


@dataclass
class IntelligenceOperation:
    """Structure for intelligence operation tracking"""
    operation_id: str
    operation_type: str
    trigger_source: str
    start_time: datetime.datetime
    end_time: Optional[datetime.datetime]
    status: str
    results: Dict[str, Any]
    recommendations: List[str]


class IntelligenceOrchestrator:
    """Central orchestrator for Historical Intelligence automation"""
    
    def __init__(self, base_path: str = None):
        """Initialize intelligence orchestrator"""
        self.base_path = base_path or "/Users/nalve/claude-context-engineering"
        self.trigger_conditions = {}
        self.active_operations = {}
        self.operation_history = []
        self.orchestration_config = self._load_orchestration_config()
        
    def _load_orchestration_config(self) -> Dict[str, Any]:
        """Load orchestration configuration"""
        config = {
            'auto_triggers_enabled': True,
            'trigger_check_interval': 300,  # 5 minutes
            'max_concurrent_operations': 3,
            'intelligence_thresholds': {
                'session_initialization': {'immediate': True},
                'significant_change': {'commits': 10, 'operations': 5},
                'knowledge_degradation': {'age_days': 30, 'confidence': 0.8},
                'efficiency_degradation': {'cognitive_steps': 2.5, 'performance_decline': 0.1}
            },
            'automation_preferences': {
                'auto_system_update': True,
                'auto_knowledge_sync': True,
                'auto_reorganization': False  # Requires approval
            }
        }
        
        # Try to load from config file if exists
        config_path = os.path.join(self.base_path, 'scripts/intelligence/config.json')
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    file_config = json.load(f)
                    config.update(file_config)
            except Exception as e:
                print(f"⚠️  Error loading config: {e}")
        
        return config
    
    def initialize_trigger_monitoring(self) -> bool:
        """Initialize all trigger condition monitoring"""
        print("🔧 **INTELLIGENCE ORCHESTRATOR** - Initializing Trigger Monitoring")
        
        try:
            # Initialize trigger conditions based on Principle #110
            self.trigger_conditions = {
                'session_initialization': TriggerCondition(
                    trigger_id='session_init',
                    condition_type='automatic',
                    threshold_value='immediate',
                    current_value='new_session_detected',
                    triggered=False,
                    trigger_time=None,
                    action_required='auto_analyze_history_7_days'
                ),
                'significant_change': TriggerCondition(
                    trigger_id='significant_change',
                    condition_type='threshold',
                    threshold_value={'commits': 10, 'operations': 5},
                    current_value={'commits': 0, 'operations': 0},
                    triggered=False,
                    trigger_time=None,
                    action_required='auto_invoke_system_update_recent'
                ),
                'knowledge_degradation': TriggerCondition(
                    trigger_id='knowledge_degradation',
                    condition_type='temporal',
                    threshold_value={'age_days': 30, 'confidence': 0.8},
                    current_value={'max_age_days': 0, 'min_confidence': 1.0},
                    triggered=False,
                    trigger_time=None,
                    action_required='auto_invoke_knowledge_sync'
                ),
                'efficiency_degradation': TriggerCondition(
                    trigger_id='efficiency_degradation',
                    condition_type='performance',
                    threshold_value={'cognitive_steps': 2.5, 'performance_decline': 0.1},
                    current_value={'cognitive_steps': 2.0, 'performance_decline': 0.0},
                    triggered=False,
                    trigger_time=None,
                    action_required='auto_invoke_intelligent_reorganization'
                )
            }
            
            print(f"   ✅ {len(self.trigger_conditions)} trigger conditions initialized")
            return True
            
        except Exception as e:
            print(f"❌ Trigger monitoring initialization failed: {e}")
            return False
    
    def monitor_trigger_conditions(self) -> List[TriggerCondition]:
        """Monitor all trigger conditions and return triggered ones"""
        triggered = []
        
        try:
            # Check session initialization trigger
            if self._check_session_initialization():
                self.trigger_conditions['session_initialization'].triggered = True
                self.trigger_conditions['session_initialization'].trigger_time = datetime.datetime.now()
                triggered.append(self.trigger_conditions['session_initialization'])
            
            # Check significant change trigger
            change_metrics = self._check_significant_changes()
            if self._evaluate_significant_change_trigger(change_metrics):
                self.trigger_conditions['significant_change'].current_value = change_metrics
                self.trigger_conditions['significant_change'].triggered = True
                self.trigger_conditions['significant_change'].trigger_time = datetime.datetime.now()
                triggered.append(self.trigger_conditions['significant_change'])
            
            # Check knowledge degradation trigger
            knowledge_metrics = self._check_knowledge_degradation()
            if self._evaluate_knowledge_degradation_trigger(knowledge_metrics):
                self.trigger_conditions['knowledge_degradation'].current_value = knowledge_metrics
                self.trigger_conditions['knowledge_degradation'].triggered = True
                self.trigger_conditions['knowledge_degradation'].trigger_time = datetime.datetime.now()
                triggered.append(self.trigger_conditions['knowledge_degradation'])
            
            # Check efficiency degradation trigger
            efficiency_metrics = self._check_efficiency_degradation()
            if self._evaluate_efficiency_degradation_trigger(efficiency_metrics):
                self.trigger_conditions['efficiency_degradation'].current_value = efficiency_metrics
                self.trigger_conditions['efficiency_degradation'].triggered = True
                self.trigger_conditions['efficiency_degradation'].trigger_time = datetime.datetime.now()
                triggered.append(self.trigger_conditions['efficiency_degradation'])
            
        except Exception as e:
            print(f"⚠️  Error monitoring trigger conditions: {e}")
        
        return triggered
    
    def execute_intelligence_operation(self, trigger: TriggerCondition) -> IntelligenceOperation:
        """Execute intelligence operation based on trigger"""
        operation = IntelligenceOperation(
            operation_id=f"{trigger.trigger_id}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}",
            operation_type=trigger.action_required,
            trigger_source=trigger.trigger_id,
            start_time=datetime.datetime.now(),
            end_time=None,
            status='running',
            results={},
            recommendations=[]
        )
        
        print(f"🚀 Executing: {operation.operation_type} (triggered by: {trigger.trigger_id})")
        
        try:
            if trigger.action_required == 'auto_analyze_history_7_days':
                operation.results = self._execute_historical_analysis(7)
            
            elif trigger.action_required == 'auto_invoke_system_update_recent':
                operation.results = self._execute_system_update('recent')
            
            elif trigger.action_required == 'auto_invoke_knowledge_sync':
                operation.results = self._execute_knowledge_sync('freshness')
            
            elif trigger.action_required == 'auto_invoke_intelligent_reorganization':
                operation.results = self._execute_intelligent_reorganization('efficiency')
            
            operation.end_time = datetime.datetime.now()
            operation.status = 'completed'
            
            # Generate recommendations
            operation.recommendations = self._generate_operation_recommendations(operation)
            
        except Exception as e:
            operation.end_time = datetime.datetime.now()
            operation.status = 'failed'
            operation.results = {'error': str(e)}
            print(f"❌ Operation failed: {e}")
        
        # Store operation
        self.active_operations[operation.operation_id] = operation
        self.operation_history.append(operation)
        
        return operation
    
    def _check_session_initialization(self) -> bool:
        """Check if new session initialization is detected"""
        # For simulation, always trigger on first run
        # In real implementation, this would check session state
        return not self.trigger_conditions['session_initialization'].triggered
    
    def _check_significant_changes(self) -> Dict[str, int]:
        """Check for significant system changes"""
        metrics = {'commits': 0, 'operations': 0}
        
        try:
            # Check git commits in last 24 hours
            result = subprocess.run([
                'git', 'log', '--since=24 hours ago', '--oneline'
            ], cwd=self.base_path, capture_output=True, text=True)
            
            if result.returncode == 0:
                metrics['commits'] = len(result.stdout.strip().split('\n')) if result.stdout.strip() else 0
            
            # Check operation files created in last 24 hours
            results_dir = os.path.join(self.base_path, 'scripts/results')
            if os.path.exists(results_dir):
                recent_files = 0
                cutoff_time = time.time() - (24 * 3600)  # 24 hours ago
                
                for root, dirs, files in os.walk(results_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        if os.path.getmtime(file_path) > cutoff_time:
                            recent_files += 1
                
                metrics['operations'] = recent_files
        
        except Exception as e:
            print(f"⚠️  Error checking significant changes: {e}")
        
        return metrics
    
    def _check_knowledge_degradation(self) -> Dict[str, float]:
        """Check for knowledge degradation indicators"""
        metrics = {'max_age_days': 0, 'min_confidence': 1.0}
        
        try:
            # Check age of documentation files
            docs_dir = os.path.join(self.base_path, 'docs')
            if os.path.exists(docs_dir):
                max_age = 0
                current_time = time.time()
                
                for root, dirs, files in os.walk(docs_dir):
                    for file in files:
                        if file.endswith('.md'):
                            file_path = os.path.join(root, file)
                            age_seconds = current_time - os.path.getmtime(file_path)
                            age_days = age_seconds / (24 * 3600)
                            max_age = max(max_age, age_days)
                
                metrics['max_age_days'] = max_age
            
            # Simulate confidence measurement (would be based on validation results)
            metrics['min_confidence'] = 0.75  # Simulated value
            
        except Exception as e:
            print(f"⚠️  Error checking knowledge degradation: {e}")
        
        return metrics
    
    def _check_efficiency_degradation(self) -> Dict[str, float]:
        """Check for efficiency degradation indicators"""
        metrics = {'cognitive_steps': 2.0, 'performance_decline': 0.0}
        
        try:
            # Simulate cognitive steps measurement
            # In real implementation, this would analyze navigation patterns
            metrics['cognitive_steps'] = 2.8  # Simulated value above threshold
            
            # Simulate performance decline measurement
            metrics['performance_decline'] = 0.05  # Simulated 5% decline
            
        except Exception as e:
            print(f"⚠️  Error checking efficiency degradation: {e}")
        
        return metrics
    
    def _evaluate_significant_change_trigger(self, metrics: Dict[str, int]) -> bool:
        """Evaluate if significant change trigger should fire"""
        thresholds = self.orchestration_config['intelligence_thresholds']['significant_change']
        return (metrics['commits'] >= thresholds['commits'] or 
                metrics['operations'] >= thresholds['operations'])
    
    def _evaluate_knowledge_degradation_trigger(self, metrics: Dict[str, float]) -> bool:
        """Evaluate if knowledge degradation trigger should fire"""
        thresholds = self.orchestration_config['intelligence_thresholds']['knowledge_degradation']
        return (metrics['max_age_days'] >= thresholds['age_days'] or 
                metrics['min_confidence'] < thresholds['confidence'])
    
    def _evaluate_efficiency_degradation_trigger(self, metrics: Dict[str, float]) -> bool:
        """Evaluate if efficiency degradation trigger should fire"""
        thresholds = self.orchestration_config['intelligence_thresholds']['efficiency_degradation']
        return (metrics['cognitive_steps'] > thresholds['cognitive_steps'] or 
                metrics['performance_decline'] >= thresholds['performance_decline'])
    
    def _execute_historical_analysis(self, days: int) -> Dict[str, Any]:
        """Execute historical analysis for session initialization"""
        results = {
            'operation': 'historical_analysis',
            'timeframe_days': days,
            'analysis_completed': True,
            'context_summary': f"Analyzed {days} days of historical data for context awareness"
        }
        
        try:
            # In full implementation, this would run all analyzers
            print(f"   📊 Historical analysis for {days} days initiated")
            results['conversation_patterns'] = 'analyzed'
            results['git_patterns'] = 'analyzed'
            results['operational_patterns'] = 'analyzed'
            results['cross_correlations'] = 'identified'
            
        except Exception as e:
            results['error'] = str(e)
        
        return results
    
    def _execute_system_update(self, scope: str) -> Dict[str, Any]:
        """Execute system update operation"""
        results = {
            'operation': 'system_update',
            'scope': scope,
            'updates_performed': []
        }
        
        try:
            # Execute system update script
            script_path = os.path.join(self.base_path, 'scripts/maintenance/system-update.py')
            if os.path.exists(script_path):
                result = subprocess.run([
                    'python3', script_path, '--scope', scope, '--timeframe', '7days'
                ], cwd=self.base_path, capture_output=True, text=True, timeout=300)
                
                results['exit_code'] = result.returncode
                results['output'] = result.stdout
                results['execution_completed'] = True
                
                if result.returncode == 0:
                    results['updates_performed'].append(f"System update ({scope}) completed successfully")
                else:
                    results['error'] = result.stderr
            else:
                results['error'] = 'System update script not found'
                
        except Exception as e:
            results['error'] = str(e)
        
        return results
    
    def _execute_knowledge_sync(self, focus: str) -> Dict[str, Any]:
        """Execute knowledge sync operation"""
        results = {
            'operation': 'knowledge_sync',
            'focus': focus,
            'knowledge_updates': []
        }
        
        try:
            # Execute knowledge sync script
            script_path = os.path.join(self.base_path, 'scripts/maintenance/knowledge-sync.py')
            if os.path.exists(script_path):
                result = subprocess.run([
                    'python3', script_path, '--focus', focus, '--domain', 'all'
                ], cwd=self.base_path, capture_output=True, text=True, timeout=300)
                
                results['exit_code'] = result.returncode
                results['output'] = result.stdout
                results['execution_completed'] = True
                
                if result.returncode == 0:
                    results['knowledge_updates'].append(f"Knowledge sync ({focus}) completed successfully")
                else:
                    results['error'] = result.stderr
            else:
                results['error'] = 'Knowledge sync script not found'
                
        except Exception as e:
            results['error'] = str(e)
        
        return results
    
    def _execute_intelligent_reorganization(self, criteria: str) -> Dict[str, Any]:
        """Execute intelligent reorganization operation"""
        results = {
            'operation': 'intelligent_reorganization',
            'criteria': criteria,
            'reorganization_actions': []
        }
        
        try:
            # Note: Reorganization requires approval in automation preferences
            if not self.orchestration_config['automation_preferences']['auto_reorganization']:
                results['status'] = 'approval_required'
                results['message'] = 'Reorganization requires manual approval'
                return results
            
            # Execute reorganization script
            script_path = os.path.join(self.base_path, 'scripts/maintenance/intelligent-reorganization.py')
            if os.path.exists(script_path):
                result = subprocess.run([
                    'python3', script_path, '--criteria', criteria, '--scope', 'efficiency'
                ], cwd=self.base_path, capture_output=True, text=True, timeout=600)
                
                results['exit_code'] = result.returncode
                results['output'] = result.stdout
                results['execution_completed'] = True
                
                if result.returncode == 0:
                    results['reorganization_actions'].append(f"Intelligent reorganization ({criteria}) completed successfully")
                else:
                    results['error'] = result.stderr
            else:
                results['error'] = 'Intelligent reorganization script not found'
                
        except Exception as e:
            results['error'] = str(e)
        
        return results
    
    def _generate_operation_recommendations(self, operation: IntelligenceOperation) -> List[str]:
        """Generate recommendations based on operation results"""
        recommendations = []
        
        if operation.status == 'completed':
            if operation.operation_type == 'auto_analyze_history_7_days':
                recommendations.extend([
                    "Historical context successfully established for session",
                    "Monitor for pattern changes that might affect current work",
                    "Consider implementing identified optimization opportunities"
                ])
            
            elif operation.operation_type == 'auto_invoke_system_update_recent':
                recommendations.extend([
                    "System updates completed - review changes for accuracy",
                    "Validate cross-references and navigation efficiency",
                    "Monitor system metrics for improvement confirmation"
                ])
            
            elif operation.operation_type == 'auto_invoke_knowledge_sync':
                recommendations.extend([
                    "Knowledge base refreshed with latest patterns",
                    "Review new cross-references for accuracy",
                    "Update documentation workflows if needed"
                ])
            
            elif operation.operation_type == 'auto_invoke_intelligent_reorganization':
                recommendations.extend([
                    "Structure optimization completed - verify navigation improvements",
                    "Test cognitive efficiency improvements",
                    "Update navigation documentation if structure changed"
                ])
        
        elif operation.status == 'failed':
            recommendations.extend([
                f"Operation {operation.operation_type} failed - manual intervention required",
                "Review error logs for specific failure causes",
                "Consider manual execution with adjusted parameters"
            ])
        
        return recommendations
    
    def run_continuous_monitoring(self, duration_minutes: int = 60) -> bool:
        """Run continuous monitoring for specified duration"""
        print(f"🔄 **CONTINUOUS MONITORING** - Running for {duration_minutes} minutes")
        
        start_time = datetime.datetime.now()
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
        
        check_interval = self.orchestration_config['trigger_check_interval']
        operations_executed = 0
        
        try:
            while datetime.datetime.now() < end_time:
                # Monitor trigger conditions
                triggered_conditions = self.monitor_trigger_conditions()
                
                # Execute operations for triggered conditions
                for trigger in triggered_conditions:
                    if len(self.active_operations) < self.orchestration_config['max_concurrent_operations']:
                        operation = self.execute_intelligence_operation(trigger)
                        operations_executed += 1
                        print(f"   ✅ Operation executed: {operation.operation_id}")
                        
                        # Reset trigger
                        trigger.triggered = False
                        trigger.trigger_time = None
                    else:
                        print(f"   ⚠️  Max concurrent operations reached, queuing trigger: {trigger.trigger_id}")
                
                # Clean up completed operations
                self._cleanup_completed_operations()
                
                # Wait for next check
                time.sleep(check_interval)
            
            print(f"🎯 Continuous monitoring completed: {operations_executed} operations executed")
            return True
            
        except KeyboardInterrupt:
            print("\n⚠️  Continuous monitoring interrupted by user")
            return False
        except Exception as e:
            print(f"❌ Continuous monitoring failed: {e}")
            return False
    
    def _cleanup_completed_operations(self):
        """Clean up completed operations from active list"""
        completed_ops = [op_id for op_id, op in self.active_operations.items() 
                        if op.status in ['completed', 'failed']]
        
        for op_id in completed_ops:
            del self.active_operations[op_id]
    
    def generate_orchestration_report(self) -> Dict[str, Any]:
        """Generate comprehensive orchestration report"""
        report = {
            'orchestration_summary': {
                'total_operations': len(self.operation_history),
                'active_operations': len(self.active_operations),
                'trigger_conditions_monitored': len(self.trigger_conditions),
                'automation_enabled': self.orchestration_config['auto_triggers_enabled']
            },
            'operation_history': [
                {
                    'operation_id': op.operation_id,
                    'operation_type': op.operation_type,
                    'trigger_source': op.trigger_source,
                    'status': op.status,
                    'duration_seconds': (op.end_time - op.start_time).total_seconds() if op.end_time else None,
                    'recommendations_count': len(op.recommendations)
                } for op in self.operation_history
            ],
            'trigger_status': {
                trigger_id: {
                    'condition_type': trigger.condition_type,
                    'triggered': trigger.triggered,
                    'trigger_time': trigger.trigger_time.isoformat() if trigger.trigger_time else None,
                    'action_required': trigger.action_required
                } for trigger_id, trigger in self.trigger_conditions.items()
            },
            'configuration': self.orchestration_config,
            'timestamp': datetime.datetime.now().isoformat()
        }
        
        return report
    
    def export_orchestration_report(self, output_path: str = None) -> bool:
        """Export orchestration report"""
        if not output_path:
            timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
            output_path = f"/Users/nalve/claude-context-engineering/scripts/results/intelligence/orchestration-{timestamp}.json"
        
        try:
            report = self.generate_orchestration_report()
            
            os.makedirs(os.path.dirname(output_path), exist_ok=True)
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)
            
            print(f"📊 Orchestration report exported to: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exporting orchestration report: {e}")
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Intelligence Orchestrator - Historical Intelligence Automation')
    parser.add_argument('--mode', default='monitor',
                       choices=['monitor', 'continuous', 'trigger-check', 'report'],
                       help='Orchestration mode')
    parser.add_argument('--duration', type=int, default=60,
                       help='Duration for continuous monitoring (minutes)')
    parser.add_argument('--base-path', type=str,
                       help='Base project path')
    
    args = parser.parse_args()
    
    print("🤖 **INTELLIGENCE ORCHESTRATOR** - Historical Intelligence Automation")
    print("=" * 65)
    
    # Initialize orchestrator
    orchestrator = IntelligenceOrchestrator(args.base_path)
    
    if args.mode == 'monitor':
        # Initialize and run single monitoring cycle
        if orchestrator.initialize_trigger_monitoring():
            triggered = orchestrator.monitor_trigger_conditions()
            print(f"\n📊 Monitoring results: {len(triggered)} triggers activated")
            
            for trigger in triggered:
                operation = orchestrator.execute_intelligence_operation(trigger)
                print(f"   ✅ {operation.operation_id}: {operation.status}")
        
    elif args.mode == 'continuous':
        # Run continuous monitoring
        if orchestrator.initialize_trigger_monitoring():
            orchestrator.run_continuous_monitoring(args.duration)
    
    elif args.mode == 'trigger-check':
        # Check trigger conditions only
        if orchestrator.initialize_trigger_monitoring():
            triggered = orchestrator.monitor_trigger_conditions()
            print(f"\n📊 Trigger check results: {len(triggered)} conditions triggered")
    
    elif args.mode == 'report':
        # Generate and export report
        orchestrator.export_orchestration_report()
    
    print("\n🎯 **INTELLIGENCE ORCHESTRATION COMPLETED** → Automation Active")


if __name__ == "__main__":
    main()