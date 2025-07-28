#!/usr/bin/env python3
"""
Claude Code Predictive Analytics Engine
Machine learning models for predicting optimal Task tool deployment and workflow patterns
"""

import json
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Dict, List, Any, Tuple
import sqlite3
import datetime
from dataclasses import dataclass
import pickle

try:
    from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import StandardScaler, LabelEncoder
    from sklearn.metrics import mean_squared_error, r2_score
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False

@dataclass
class TaskPrediction:
    """Prediction for optimal Task tool deployment"""
    task_type: str
    predicted_execution_time: float
    confidence_score: float
    optimal_parallel_count: int
    suggested_prompt_pattern: str

@dataclass
class WorkflowPrediction:
    """Prediction for workflow optimization"""
    workflow_type: str
    predicted_completion_time: float
    recommended_task_sequence: List[str]
    efficiency_score: float
    claude_code_optimizations: Dict[str, Any]

class ClaudeCodePredictiveEngine:
    """
    Predictive analytics specifically for Claude Code CLI operations
    Uses machine learning to optimize Task tool deployment and workflow patterns
    """
    
    def __init__(self, workspace_path: str = "/Users/nalve/ce-simple"):
        self.workspace = Path(workspace_path)
        self.db_path = self.workspace / "data" / "claude-code-metrics.db"
        self.models_path = self.workspace / "data" / "predictive-models"
        self.models_path.mkdir(exist_ok=True)
        
        # Initialize models
        self.task_execution_model = None
        self.parallel_efficiency_model = None
        self.workflow_optimization_model = None
        self.scaler = StandardScaler()
        self.label_encoders = {}
        
        if not SKLEARN_AVAILABLE:
            print("Warning: sklearn not available. Using fallback prediction methods.")
    
    def collect_training_data(self) -> pd.DataFrame:
        """Collect historical data for training Claude Code specific models"""
        if not self.db_path.exists():
            return pd.DataFrame()
            
        with sqlite3.connect(self.db_path) as conn:
            # Collect task tool metrics
            task_query = """
                SELECT 
                    task_type,
                    execution_time,
                    token_usage,
                    success_rate,
                    parallel_efficiency,
                    datetime(timestamp) as timestamp
                FROM task_tool_metrics
                ORDER BY timestamp DESC
                LIMIT 1000
            """
            
            task_df = pd.read_sql_query(task_query, conn)
            
            # Collect command performance
            command_query = """
                SELECT 
                    command_name,
                    context_loading_time,
                    decision_tree_accuracy,
                    user_satisfaction,
                    datetime(timestamp) as timestamp
                FROM command_performance
                ORDER BY timestamp DESC
                LIMIT 1000
            """
            
            command_df = pd.read_sql_query(command_query, conn)
            
            # Collect workflow data
            workflow_query = """
                SELECT 
                    workflow_type,
                    steps_completed,
                    total_time,
                    claude_code_specific_metrics,
                    datetime(timestamp) as timestamp
                FROM workflow_efficiency
                ORDER BY timestamp DESC
                LIMIT 1000
            """
            
            workflow_df = pd.read_sql_query(workflow_query, conn)
            
        return self._merge_training_data(task_df, command_df, workflow_df)
    
    def _merge_training_data(self, task_df: pd.DataFrame, 
                           command_df: pd.DataFrame, 
                           workflow_df: pd.DataFrame) -> pd.DataFrame:
        """Merge different data sources for comprehensive training dataset"""
        # Create time-based features
        for df in [task_df, command_df, workflow_df]:
            if not df.empty and 'timestamp' in df.columns:
                df['timestamp'] = pd.to_datetime(df['timestamp'])
                df['hour'] = df['timestamp'].dt.hour
                df['day_of_week'] = df['timestamp'].dt.dayofweek
        
        # Merge on timestamp windows (group by 5-minute intervals)
        training_data = []
        
        # Process task data
        if not task_df.empty:
            for _, row in task_df.iterrows():
                training_data.append({
                    'task_type': row.get('task_type', 'unknown'),
                    'execution_time': row.get('execution_time', 0),
                    'token_usage': row.get('token_usage', 0),
                    'success_rate': row.get('success_rate', 0),
                    'parallel_efficiency': row.get('parallel_efficiency', 0),
                    'hour': row.get('hour', 12),
                    'day_of_week': row.get('day_of_week', 1),
                    'data_source': 'task_tools'
                })
        
        return pd.DataFrame(training_data)
    
    def train_models(self):
        """Train machine learning models for Claude Code predictions"""
        training_data = self.collect_training_data()
        
        if training_data.empty:
            print("No training data available. Using default models.")
            self._create_fallback_models()
            return
        
        if SKLEARN_AVAILABLE:
            self._train_sklearn_models(training_data)
        else:
            self._create_fallback_models()
    
    def _train_sklearn_models(self, data: pd.DataFrame):
        """Train sklearn models for prediction"""
        try:
            # Prepare features
            feature_columns = ['token_usage', 'hour', 'day_of_week']
            
            # Encode categorical variables
            if 'task_type' in data.columns:
                self.label_encoders['task_type'] = LabelEncoder()
                data['task_type_encoded'] = self.label_encoders['task_type'].fit_transform(data['task_type'])
                feature_columns.append('task_type_encoded')
            
            # Features and targets
            X = data[feature_columns].fillna(0)
            
            if X.empty or len(X) < 10:
                self._create_fallback_models()
                return
            
            # Scale features
            X_scaled = self.scaler.fit_transform(X)
            
            # Train execution time prediction model
            if 'execution_time' in data.columns:
                y_execution = data['execution_time'].fillna(0)
                if len(y_execution.unique()) > 1:
                    X_train, X_test, y_train, y_test = train_test_split(
                        X_scaled, y_execution, test_size=0.2, random_state=42
                    )
                    
                    self.task_execution_model = RandomForestRegressor(n_estimators=50, random_state=42)
                    self.task_execution_model.fit(X_train, y_train)
                    
                    # Evaluate
                    y_pred = self.task_execution_model.predict(X_test)
                    r2 = r2_score(y_test, y_pred)
                    print(f"Task execution model R²: {r2:.3f}")
            
            # Train parallel efficiency model
            if 'parallel_efficiency' in data.columns:
                y_parallel = data['parallel_efficiency'].fillna(0)
                if len(y_parallel.unique()) > 1:
                    X_train, X_test, y_train, y_test = train_test_split(
                        X_scaled, y_parallel, test_size=0.2, random_state=42
                    )
                    
                    self.parallel_efficiency_model = GradientBoostingRegressor(n_estimators=50, random_state=42)
                    self.parallel_efficiency_model.fit(X_train, y_train)
                    
                    # Evaluate
                    y_pred = self.parallel_efficiency_model.predict(X_test)
                    r2 = r2_score(y_test, y_pred)
                    print(f"Parallel efficiency model R²: {r2:.3f}")
            
            # Save models
            self._save_models()
            
        except Exception as e:
            print(f"Error training sklearn models: {e}")
            self._create_fallback_models()
    
    def _create_fallback_models(self):
        """Create simple fallback models when sklearn is not available or data is insufficient"""
        # Simple heuristic-based models
        self.fallback_rules = {
            'task_execution_time': {
                'research': 3.0,
                'architecture': 2.5,
                'content': 2.0,
                'voice-preservation': 1.5,
                'quality': 2.0,
                'default': 2.5
            },
            'parallel_efficiency': {
                'research': 0.8,
                'architecture': 0.75,
                'content': 0.85,
                'voice-preservation': 0.9,
                'quality': 0.8,
                'default': 0.8
            }
        }
    
    def predict_task_performance(self, task_type: str, token_usage: int, 
                               hour: int = 12, day_of_week: int = 1) -> TaskPrediction:
        """Predict optimal Task tool deployment for Claude Code"""
        if SKLEARN_AVAILABLE and self.task_execution_model is not None:
            return self._predict_with_sklearn(task_type, token_usage, hour, day_of_week)
        else:
            return self._predict_with_fallback(task_type, token_usage)
    
    def _predict_with_sklearn(self, task_type: str, token_usage: int, 
                            hour: int, day_of_week: int) -> TaskPrediction:
        """Make predictions using trained sklearn models"""
        try:
            # Prepare features
            features = [token_usage, hour, day_of_week]
            
            # Encode task type if encoder exists
            if 'task_type' in self.label_encoders:
                try:
                    task_encoded = self.label_encoders['task_type'].transform([task_type])[0]
                    features.append(task_encoded)
                except ValueError:
                    # Unknown task type, use default encoding
                    features.append(0)
            
            # Scale features
            features_scaled = self.scaler.transform([features])
            
            # Predict execution time
            if self.task_execution_model:
                execution_time = self.task_execution_model.predict(features_scaled)[0]
                confidence = min(0.9, max(0.3, 1.0 - (execution_time / 10.0)))  # Confidence based on complexity
            else:
                execution_time = self.fallback_rules['task_execution_time'].get(task_type, 2.5)
                confidence = 0.6
            
            # Predict parallel efficiency
            if self.parallel_efficiency_model:
                parallel_efficiency = self.parallel_efficiency_model.predict(features_scaled)[0]
            else:
                parallel_efficiency = self.fallback_rules['parallel_efficiency'].get(task_type, 0.8)
            
            # Calculate optimal parallel count
            optimal_parallel = max(1, min(5, int(parallel_efficiency * 5)))
            
            # Generate prompt pattern suggestion
            prompt_pattern = self._generate_prompt_pattern(task_type, token_usage)
            
            return TaskPrediction(
                task_type=task_type,
                predicted_execution_time=max(0.5, execution_time),
                confidence_score=confidence,
                optimal_parallel_count=optimal_parallel,
                suggested_prompt_pattern=prompt_pattern
            )
            
        except Exception as e:
            print(f"Error in sklearn prediction: {e}")
            return self._predict_with_fallback(task_type, token_usage)
    
    def _predict_with_fallback(self, task_type: str, token_usage: int) -> TaskPrediction:
        """Make predictions using fallback heuristic models"""
        execution_time = self.fallback_rules['task_execution_time'].get(task_type, 2.5)
        parallel_efficiency = self.fallback_rules['parallel_efficiency'].get(task_type, 0.8)
        
        # Adjust for token usage
        token_factor = min(2.0, token_usage / 1000)
        execution_time *= token_factor
        
        optimal_parallel = max(1, min(5, int(parallel_efficiency * 5)))
        prompt_pattern = self._generate_prompt_pattern(task_type, token_usage)
        
        return TaskPrediction(
            task_type=task_type,
            predicted_execution_time=execution_time,
            confidence_score=0.6,  # Medium confidence for heuristic
            optimal_parallel_count=optimal_parallel,
            suggested_prompt_pattern=prompt_pattern
        )
    
    def _generate_prompt_pattern(self, task_type: str, token_usage: int) -> str:
        """Generate optimal prompt pattern for Claude Code Task tools"""
        patterns = {
            'research': f"Research specialist: Investigate {{topic}} focusing on Claude Code CLI specific implementations. Target {token_usage} tokens.",
            'architecture': f"Architecture validator: Validate {{component}} consistency with Claude Code ecosystem. Analyze {token_usage} token context.",
            'content': f"Content optimizer: Optimize {{content}} for Claude Code token economy. Limit to {token_usage} tokens.",
            'voice-preservation': f"Voice preservation specialist: Maintain exact user intent in {{content}} for Claude Code workflow.",
            'quality': f"Quality assurance: Validate {{output}} against Claude Code standards and requirements."
        }
        
        return patterns.get(task_type, f"General-purpose specialist: Process {{task}} for Claude Code context with {token_usage} token efficiency.")
    
    def predict_workflow_optimization(self, workflow_type: str, 
                                    current_steps: List[str]) -> WorkflowPrediction:
        """Predict optimal workflow patterns for Claude Code operations"""
        # Analyze current workflow
        step_complexity = sum(len(step.split()) for step in current_steps)
        estimated_time = step_complexity * 0.5  # Base estimate
        
        # Generate optimized task sequence
        optimized_sequence = self._optimize_task_sequence(workflow_type, current_steps)
        
        # Calculate efficiency score
        efficiency_score = self._calculate_workflow_efficiency(workflow_type, optimized_sequence)
        
        # Claude Code specific optimizations
        claude_code_optimizations = {
            'parallel_tasks': min(len(optimized_sequence), 5),
            'context_loading_strategy': 'progressive',
            'task_tool_utilization': efficiency_score,
            'token_economy_compliance': True
        }
        
        return WorkflowPrediction(
            workflow_type=workflow_type,
            predicted_completion_time=estimated_time,
            recommended_task_sequence=optimized_sequence,
            efficiency_score=efficiency_score,
            claude_code_optimizations=claude_code_optimizations
        )
    
    def _optimize_task_sequence(self, workflow_type: str, current_steps: List[str]) -> List[str]:
        """Optimize task sequence for Claude Code efficiency"""
        optimization_rules = {
            'document_creation': [
                'content_specialist_deploy',
                'architecture_validation_parallel',
                'quality_assurance_concurrent'
            ],
            'research_workflow': [
                'research_specialist_web_search',
                'pattern_analysis_parallel',
                'insights_consolidation'
            ],
            'implementation_workflow': [
                'architecture_validation',
                'parallel_implementation_tasks',
                'quality_verification'
            ]
        }
        
        return optimization_rules.get(workflow_type, current_steps)
    
    def _calculate_workflow_efficiency(self, workflow_type: str, task_sequence: List[str]) -> float:
        """Calculate predicted workflow efficiency score"""
        base_scores = {
            'document_creation': 0.85,
            'research_workflow': 0.90,
            'implementation_workflow': 0.80,
            'analysis_workflow': 0.88
        }
        
        base_score = base_scores.get(workflow_type, 0.75)
        
        # Bonus for parallel tasks
        parallel_bonus = min(0.15, len(task_sequence) * 0.03)
        
        return min(1.0, base_score + parallel_bonus)
    
    def _save_models(self):
        """Save trained models to disk"""
        if SKLEARN_AVAILABLE:
            try:
                models_data = {
                    'task_execution_model': self.task_execution_model,
                    'parallel_efficiency_model': self.parallel_efficiency_model,
                    'scaler': self.scaler,
                    'label_encoders': self.label_encoders
                }
                
                with open(self.models_path / 'claude_code_models.pkl', 'wb') as f:
                    pickle.dump(models_data, f)
                    
                print("Models saved successfully")
            except Exception as e:
                print(f"Error saving models: {e}")
    
    def load_models(self):
        """Load previously trained models"""
        model_file = self.models_path / 'claude_code_models.pkl'
        
        if model_file.exists() and SKLEARN_AVAILABLE:
            try:
                with open(model_file, 'rb') as f:
                    models_data = pickle.load(f)
                
                self.task_execution_model = models_data.get('task_execution_model')
                self.parallel_efficiency_model = models_data.get('parallel_efficiency_model')
                self.scaler = models_data.get('scaler', StandardScaler())
                self.label_encoders = models_data.get('label_encoders', {})
                
                print("Models loaded successfully")
            except Exception as e:
                print(f"Error loading models: {e}")
                self._create_fallback_models()
        else:
            self._create_fallback_models()
    
    def generate_optimization_report(self) -> Dict[str, Any]:
        """Generate comprehensive optimization report for Claude Code operations"""
        current_time = datetime.datetime.now()
        
        # Sample predictions for common task types
        task_types = ['research', 'architecture', 'content', 'voice-preservation', 'quality']
        predictions = {}
        
        for task_type in task_types:
            pred = self.predict_task_performance(task_type, 1500, current_time.hour, current_time.weekday())
            predictions[task_type] = {
                'execution_time': pred.predicted_execution_time,
                'confidence': pred.confidence_score,
                'optimal_parallel': pred.optimal_parallel_count,
                'prompt_pattern': pred.suggested_prompt_pattern
            }
        
        # Workflow predictions
        workflow_pred = self.predict_workflow_optimization('document_creation', ['draft', 'review', 'finalize'])
        
        report = {
            'timestamp': current_time.isoformat(),
            'task_predictions': predictions,
            'workflow_optimization': {
                'type': workflow_pred.workflow_type,
                'completion_time': workflow_pred.predicted_completion_time,
                'sequence': workflow_pred.recommended_task_sequence,
                'efficiency': workflow_pred.efficiency_score,
                'claude_code_optimizations': workflow_pred.claude_code_optimizations
            },
            'system_recommendations': self._generate_system_recommendations()
        }
        
        # Save report
        report_path = self.workspace / "data" / "claude-code-predictions.json"
        with open(report_path, 'w') as f:
            json.dump(report, f, indent=2)
        
        return report
    
    def _generate_system_recommendations(self) -> List[str]:
        """Generate system-wide optimization recommendations"""
        return [
            "Use parallel Task tools for research and architecture validation",
            "Optimize token usage by pre-calculating context requirements",
            "Implement progressive context loading for complex workflows",
            "Monitor Task tool success rates and adjust prompt patterns",
            "Utilize workflow predictions for session planning",
            "Track parallel execution efficiency for optimization opportunities"
        ]

if __name__ == "__main__":
    # Initialize predictive engine
    engine = ClaudeCodePredictiveEngine()
    
    # Load existing models or train new ones
    engine.load_models()
    engine.train_models()
    
    # Generate predictions
    prediction = engine.predict_task_performance('research', 2000, 14, 2)
    print(f"Task Prediction: {prediction}")
    
    workflow_pred = engine.predict_workflow_optimization('document_creation', ['draft', 'review', 'publish'])
    print(f"Workflow Prediction: {workflow_pred}")
    
    # Generate full report
    report = engine.generate_optimization_report()
    print("Optimization report generated")
    print(f"Report saved to: {engine.workspace}/data/claude-code-predictions.json")