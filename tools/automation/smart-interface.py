#!/usr/bin/env python3
"""
Smart Interface Components for Predictive Command System
Provides contextual help, smart completion, and workflow optimization
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import argparse

# Add predictive engine to path
sys.path.append(str(Path(__file__).parent))
from predictive_engine import PredictiveSystem, get_smart_suggestions, record_usage


class SmartCommandInterface:
    """Interactive command interface with predictive capabilities"""
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.system = PredictiveSystem(base_path)
        self.session_commands = []
        self.current_context = ""
    
    def start_session(self, context: str = ""):
        """Start a new predictive session"""
        self.current_context = context
        self.session_commands = []
        
        print("🧠 Smart Command Interface Active")
        if context:
            print(f"📋 Context: {context}")
        
        # Get initial recommendations
        recommendations = self.system.get_recommendations(context)
        if recommendations:
            print("\n💡 Suggested commands to get started:")
            self._display_recommendations(recommendations[:3])
    
    def update_context(self, new_context: str):
        """Update current context and get fresh recommendations"""
        self.current_context = new_context
        
        print(f"\n📋 Context updated: {new_context}")
        
        recommendations = self.system.get_recommendations(
            new_context, self.session_commands[-3:]  # Last 3 commands
        )
        
        if recommendations:
            print("\n💡 Updated suggestions:")
            self._display_recommendations(recommendations[:2])
    
    def get_command_suggestions(self, partial_command: str = "") -> List[Dict]:
        """Get suggestions for command completion"""
        recommendations = self.system.get_recommendations(
            self.current_context, self.session_commands
        )
        
        # Filter by partial command if provided
        if partial_command:
            recommendations = [
                rec for rec in recommendations 
                if rec.command.startswith(partial_command.lstrip('/'))
            ]
        
        return recommendations
    
    def record_command_execution(self, command: str, success: bool = True, 
                               execution_time: float = 0.0, user_feedback: str = None):
        """Record command execution for learning"""
        # Clean command name
        clean_command = command.lstrip('/')
        
        # Add to session history
        self.session_commands.append(clean_command)
        
        # Record for learning
        self.system.record_command_usage(
            clean_command, self.current_context, success, execution_time, user_feedback
        )
        
        # Provide contextual suggestions after execution
        self._suggest_next_commands(clean_command)
    
    def _suggest_next_commands(self, executed_command: str):
        """Suggest follow-up commands after execution"""
        recommendations = self.system.get_recommendations(
            self.current_context, self.session_commands
        )
        
        # Focus on integration opportunities
        relevant_recs = []
        for rec in recommendations:
            if executed_command in rec.integration_opportunities or rec.confidence > 0.6:
                relevant_recs.append(rec)
        
        if relevant_recs:
            print(f"\n🔗 Suggested follow-ups after /{executed_command}:")
            self._display_recommendations(relevant_recs[:2])
    
    def _display_recommendations(self, recommendations: List):
        """Display recommendations in a user-friendly format"""
        for i, rec in enumerate(recommendations, 1):
            confidence_bar = "▓" * int(rec.confidence * 10) + "░" * (10 - int(rec.confidence * 10))
            print(f"  {i}. /{rec.command}")
            print(f"     {confidence_bar} {rec.confidence:.1%} confidence")
            print(f"     💭 {rec.reasoning}")
            
            if rec.integration_opportunities:
                print(f"     🔗 Pairs well with: {', '.join(f'/{cmd}' for cmd in rec.integration_opportunities[:2])}")
            print()
    
    def analyze_workflow_efficiency(self) -> Dict:
        """Analyze current session workflow for optimization opportunities"""
        if len(self.session_commands) < 2:
            return {"message": "Need more commands to analyze workflow"}
        
        # Get patterns from system
        patterns = self.system.export_patterns()
        
        analysis = {
            "commands_executed": len(self.session_commands),
            "unique_commands": len(set(self.session_commands)),
            "efficiency_score": len(set(self.session_commands)) / len(self.session_commands),
            "optimization_suggestions": []
        }
        
        # Check for missed integration opportunities
        for i, command in enumerate(self.session_commands[:-1]):
            next_command = self.session_commands[i + 1]
            
            # Look for better sequences in patterns
            for pattern in patterns.get('sequences', []):
                seq_parts = pattern['sequence'].split('->')
                if len(seq_parts) >= 2 and seq_parts[0] == command:
                    if seq_parts[1] != next_command and pattern['frequency'] > 2:
                        analysis["optimization_suggestions"].append({
                            "type": "sequence_optimization",
                            "message": f"After /{command}, /{seq_parts[1]} is used {pattern['frequency']} times more often than /{next_command}",
                            "suggested_command": seq_parts[1]
                        })
        
        return analysis
    
    def export_session_summary(self) -> Dict:
        """Export summary of current session for handoff"""
        return {
            "session_id": datetime.now().strftime("%Y-%m-%d_%H-%M"),
            "context": self.current_context,
            "commands_executed": self.session_commands,
            "workflow_analysis": self.analyze_workflow_efficiency(),
            "timestamp": datetime.now().isoformat()
        }


class WorkflowOptimizer:
    """Analyzes and suggests workflow optimizations"""
    
    def __init__(self, system: PredictiveSystem):
        self.system = system
    
    def analyze_user_patterns(self) -> Dict:
        """Analyze user's command patterns for optimization"""
        patterns = self.system.export_patterns()
        
        analysis = {
            "most_used_commands": [],
            "efficient_sequences": [],
            "improvement_opportunities": [],
            "success_rates": {}
        }
        
        # Most used commands
        for stat in patterns.get('command_stats', [])[:5]:
            analysis["most_used_commands"].append({
                "command": stat['command'],
                "usage_count": stat['usage_count'],
                "success_rate": stat['success_rate']
            })
        
        # Efficient sequences
        for seq in patterns.get('sequences', [])[:5]:
            if seq['frequency'] > 2:
                analysis["efficient_sequences"].append({
                    "sequence": seq['sequence'].replace('->', ' → /'),
                    "frequency": seq['frequency'],
                    "success_rate": seq.get('success_rate', 0.8)
                })
        
        # Identify improvement opportunities
        for stat in patterns.get('command_stats', []):
            if stat['success_rate'] < 0.7 and stat['usage_count'] > 3:
                analysis["improvement_opportunities"].append({
                    "command": stat['command'],
                    "issue": "Low success rate",
                    "suggestion": "Consider reviewing command usage patterns or providing additional context"
                })
        
        return analysis
    
    def suggest_workflow_templates(self, goal: str) -> List[Dict]:
        """Suggest workflow templates based on goals"""
        templates = {
            "documentation": {
                "name": "Documentation Workflow",
                "commands": ["analyze", "create-doc", "align-doc", "verify-doc"],
                "description": "Complete documentation creation and validation process"
            },
            "implementation": {
                "name": "Implementation Workflow", 
                "commands": ["analyze", "implement", "test", "debug", "refactor"],
                "description": "Full development cycle from analysis to optimization"
            },
            "session_management": {
                "name": "Session Management",
                "commands": ["start", "extract-insights", "process-layer", "session-close"],
                "description": "Optimal session lifecycle management"
            },
            "exploration": {
                "name": "Exploration Workflow",
                "commands": ["explore", "analyze", "contextflow-agent", "extract-insights"],
                "description": "Deep exploration and learning process"
            }
        }
        
        # Match goal to templates
        goal_lower = goal.lower()
        relevant_templates = []
        
        for key, template in templates.items():
            if any(keyword in goal_lower for keyword in key.split('_')):
                relevant_templates.append(template)
        
        # If no specific match, return most popular patterns
        if not relevant_templates:
            patterns = self.system.export_patterns()
            for seq in patterns.get('sequences', [])[:3]:
                if seq['frequency'] > 2:
                    commands = seq['sequence'].split('->')
                    relevant_templates.append({
                        "name": f"Learned Pattern: {' → '.join(commands)}",
                        "commands": commands,
                        "description": f"Frequently used sequence (used {seq['frequency']} times)",
                        "type": "learned_pattern"
                    })
        
        return relevant_templates


class PerformanceMonitor:
    """Monitors and reports on predictive system performance"""
    
    def __init__(self, system: PredictiveSystem):
        self.system = system
        self.metrics_file = system.base_path / "tools" / "automation" / "performance_metrics.json"
    
    def record_prediction_accuracy(self, predicted_commands: List[str], 
                                 executed_command: str, context: str):
        """Record accuracy of predictions"""
        accuracy = 1.0 if executed_command in predicted_commands else 0.0
        
        metrics = self._load_metrics()
        metrics["predictions"].append({
            "timestamp": datetime.now().isoformat(),
            "predicted": predicted_commands,
            "executed": executed_command,
            "accuracy": accuracy,
            "context_length": len(context)
        })
        
        self._save_metrics(metrics)
    
    def get_performance_stats(self) -> Dict:
        """Get current performance statistics"""
        metrics = self._load_metrics()
        predictions = metrics.get("predictions", [])
        
        if not predictions:
            return {"message": "No prediction data available"}
        
        total_predictions = len(predictions)
        accurate_predictions = sum(p["accuracy"] for p in predictions)
        
        return {
            "total_predictions": total_predictions,
            "accuracy_rate": accurate_predictions / total_predictions,
            "recent_accuracy": self._calculate_recent_accuracy(predictions),
            "performance_trend": self._calculate_trend(predictions)
        }
    
    def _load_metrics(self) -> Dict:
        """Load metrics from file"""
        if self.metrics_file.exists():
            with open(self.metrics_file, 'r') as f:
                return json.load(f)
        return {"predictions": [], "created": datetime.now().isoformat()}
    
    def _save_metrics(self, metrics: Dict):
        """Save metrics to file"""
        self.metrics_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.metrics_file, 'w') as f:
            json.dump(metrics, f, indent=2)
    
    def _calculate_recent_accuracy(self, predictions: List[Dict]) -> float:
        """Calculate accuracy over recent predictions"""
        recent = predictions[-20:]  # Last 20 predictions
        if not recent:
            return 0.0
        return sum(p["accuracy"] for p in recent) / len(recent)
    
    def _calculate_trend(self, predictions: List[Dict]) -> str:
        """Calculate performance trend"""
        if len(predictions) < 10:
            return "insufficient_data"
        
        first_half = predictions[:len(predictions)//2]
        second_half = predictions[len(predictions)//2:]
        
        first_accuracy = sum(p["accuracy"] for p in first_half) / len(first_half)
        second_accuracy = sum(p["accuracy"] for p in second_half) / len(second_half)
        
        if second_accuracy > first_accuracy + 0.1:
            return "improving"
        elif second_accuracy < first_accuracy - 0.1:
            return "declining"
        else:
            return "stable"


# CLI Interface
def main():
    """Command line interface for predictive system"""
    parser = argparse.ArgumentParser(description="Smart Command Interface")
    parser.add_argument("--mode", choices=["interactive", "suggest", "analyze", "init"], 
                       default="suggest", help="Operation mode")
    parser.add_argument("--context", type=str, default="", help="Current context")
    parser.add_argument("--command", type=str, help="Command for completion suggestions")
    parser.add_argument("--record", type=str, help="Record command execution")
    parser.add_argument("--success", action="store_true", help="Command was successful")
    
    args = parser.parse_args()
    
    if args.mode == "init":
        print("🔄 Initializing predictive system...")
        system = PredictiveSystem()
        system.initialize_system()
        print("✅ System initialized with historical data")
        
    elif args.mode == "interactive":
        interface = SmartCommandInterface()
        interface.start_session(args.context)
        
        print("\nInteractive mode - Type 'help' for commands, 'quit' to exit")
        while True:
            try:
                user_input = input("\n> ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    summary = interface.export_session_summary()
                    print(f"\n📊 Session Summary: {summary['commands_executed']}")
                    break
                    
                elif user_input.lower() == 'help':
                    print("Commands:")
                    print("  context <text>  - Update context")
                    print("  suggest         - Get command suggestions")
                    print("  analyze         - Analyze current workflow")
                    print("  quit           - Exit interactive mode")
                    
                elif user_input.startswith('context '):
                    new_context = user_input[8:]
                    interface.update_context(new_context)
                    
                elif user_input == 'suggest':
                    recs = interface.get_command_suggestions()
                    if recs:
                        interface._display_recommendations(recs[:3])
                    else:
                        print("No suggestions available")
                        
                elif user_input == 'analyze':
                    analysis = interface.analyze_workflow_efficiency()
                    print(f"\n📊 Workflow Analysis:")
                    print(f"Commands executed: {analysis['commands_executed']}")
                    print(f"Efficiency score: {analysis['efficiency_score']:.2%}")
                    
                elif user_input.startswith('/'):
                    # Simulate command execution
                    command = user_input[1:]
                    interface.record_command_execution(command)
                    
                else:
                    print("Unknown command. Type 'help' for available commands.")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
                
    elif args.mode == "suggest":
        suggestions = get_smart_suggestions(args.context, [])
        if suggestions:
            print("💡 Smart Suggestions:")
            for i, suggestion in enumerate(suggestions[:3], 1):
                print(f"  {i}. /{suggestion['command']} ({suggestion['confidence']:.1%})")
                print(f"     {suggestion['reasoning']}")
        else:
            print("No suggestions available for current context")
            
    elif args.mode == "analyze":
        system = PredictiveSystem()
        optimizer = WorkflowOptimizer(system)
        analysis = optimizer.analyze_user_patterns()
        
        print("📊 User Pattern Analysis:")
        print("\nMost Used Commands:")
        for cmd in analysis["most_used_commands"]:
            print(f"  /{cmd['command']} - {cmd['usage_count']} uses ({cmd['success_rate']:.1%} success)")
        
        print("\nEfficient Sequences:")
        for seq in analysis["efficient_sequences"]:
            print(f"  /{seq['sequence']} - used {seq['frequency']} times")


if __name__ == "__main__":
    main()