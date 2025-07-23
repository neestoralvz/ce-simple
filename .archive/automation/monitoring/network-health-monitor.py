#!/usr/bin/env python3
"""
Predictive Network Health Monitoring System
Real-Time Cross-Reference Intelligence Network Analytics

This module provides sophisticated predictive analytics for monitoring
the health and evolution of the Context Engineering cross-reference
intelligence network with real-time optimization recommendations.
"""

import json
import sys
import time
import pickle
import statistics
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional
from collections import defaultdict, deque
from datetime import datetime, timedelta
from dataclasses import dataclass, asdict
import networkx as nx
import threading
from concurrent.futures import ThreadPoolExecutor

@dataclass
class NetworkHealthMetric:
    """Network health measurement at a point in time"""
    timestamp: datetime
    density: float
    avg_path_length: float
    clustering_coefficient: float
    connectivity_score: float
    quality_index: float
    efficiency_ratio: float
    stability_measure: float
    growth_potential: float

@dataclass
class HealthTrend:
    """Health trend analysis over time"""
    metric_name: str
    current_value: float
    trend_direction: str  # 'improving', 'declining', 'stable'
    trend_strength: float  # 0.0 to 1.0
    predicted_value: float
    confidence: float
    alert_level: str

@dataclass
class NetworkAlert:
    """Network health alert with predictions"""
    alert_type: str
    severity: str
    message: str
    affected_components: List[str]
    predicted_impact: str
    recommended_actions: List[str]
    auto_resolvable: bool
    timestamp: datetime

@dataclass
class OptimizationRecommendation:
    """Network optimization recommendation with predictive impact"""
    recommendation_type: str
    priority: str
    description: str
    predicted_benefit: float
    implementation_effort: str
    risk_level: str
    target_components: List[str]
    success_probability: float

class NetworkHealthMonitor:
    """Predictive network health monitoring and optimization system"""
    
    def __init__(self, knowledge_path: str = None):
        self.knowledge_path = Path(knowledge_path or "/Users/nalve/claude-context-engineering")
        self.cache_path = self.knowledge_path / "scripts" / "cache" / "network_health"
        self.cache_path.mkdir(parents=True, exist_ok=True)
        
        # Historical data storage
        self.health_history = deque(maxlen=1000)  # Keep last 1000 measurements
        self.trend_cache = {}
        self.alert_cache = defaultdict(list)
        
        # Monitoring configuration
        self.monitoring_interval = 300  # 5 minutes
        self.prediction_window = 7  # Days
        self.trend_analysis_window = 30  # Measurements
        
        # Health thresholds
        self.health_thresholds = {
            'density': {'critical': 0.70, 'warning': 0.80, 'good': 0.85},
            'avg_path_length': {'critical': 4.0, 'warning': 3.5, 'good': 3.0},
            'clustering_coefficient': {'critical': 0.60, 'warning': 0.70, 'good': 0.75},
            'connectivity_score': {'critical': 0.70, 'warning': 0.80, 'good': 0.90},
            'quality_index': {'critical': 0.75, 'warning': 0.85, 'good': 0.90},
            'efficiency_ratio': {'critical': 0.70, 'warning': 0.80, 'good': 0.85},
            'stability_measure': {'critical': 0.75, 'warning': 0.85, 'good': 0.90},
            'growth_potential': {'critical': 0.50, 'warning': 0.60, 'good': 0.70}
        }
        
        # Predictive model parameters
        self.prediction_weights = {
            'recent_trend': 0.4,
            'historical_average': 0.3,
            'seasonal_pattern': 0.2,
            'external_factors': 0.1
        }
        
        # Load historical data
        self._load_historical_data()
        
        # Initialize network graph
        self.network_graph = None
        self._load_network_graph()
    
    def _load_historical_data(self):
        """Load historical network health data"""
        history_file = self.cache_path / "health_history.pkl"
        if history_file.exists():
            try:
                with open(history_file, 'rb') as f:
                    self.health_history = pickle.load(f)
                print(f"📊 Loaded {len(self.health_history)} historical measurements")
            except Exception as e:
                print(f"⚠️ Could not load history: {e}")
                self.health_history = deque(maxlen=1000)
    
    def _save_historical_data(self):
        """Save historical network health data"""
        history_file = self.cache_path / "health_history.pkl"
        try:
            with open(history_file, 'wb') as f:
                pickle.dump(self.health_history, f)
        except Exception as e:
            print(f"⚠️ Could not save history: {e}")
    
    def _load_network_graph(self):
        """Load the current network graph structure"""
        try:
            # Import network analyzer
            sys.path.append(str(self.knowledge_path / "scripts" / "analytics"))
            from network_intelligence_analyzer import NetworkIntelligenceAnalyzer
            
            analyzer = NetworkIntelligenceAnalyzer(str(self.knowledge_path / "knowledge"))
            if analyzer.load_principle_network():
                self.network_graph = analyzer.graph
                print(f"🕸️ Loaded network with {len(self.network_graph.nodes())} nodes")
                return True
        except Exception as e:
            print(f"❌ Could not load network graph: {e}")
        
        return False
    
    def measure_current_health(self) -> NetworkHealthMetric:
        """Measure current network health metrics"""
        if not self.network_graph:
            raise ValueError("Network graph not loaded")
        
        timestamp = datetime.now()
        
        # Basic topology metrics
        density = nx.density(self.network_graph)
        
        # Path analysis
        if nx.is_connected(self.network_graph):
            avg_path_length = nx.average_shortest_path_length(self.network_graph)
        else:
            # Use largest connected component
            largest_cc = max(nx.connected_components(self.network_graph), key=len)
            subgraph = self.network_graph.subgraph(largest_cc)
            avg_path_length = nx.average_shortest_path_length(subgraph)
        
        # Clustering coefficient
        clustering_coefficient = nx.average_clustering(self.network_graph)
        
        # Advanced metrics
        connectivity_score = self._calculate_connectivity_score()
        quality_index = self._calculate_quality_index()
        efficiency_ratio = self._calculate_efficiency_ratio()
        stability_measure = self._calculate_stability_measure()
        growth_potential = self._calculate_growth_potential()
        
        return NetworkHealthMetric(
            timestamp=timestamp,
            density=density,
            avg_path_length=avg_path_length,
            clustering_coefficient=clustering_coefficient,
            connectivity_score=connectivity_score,
            quality_index=quality_index,
            efficiency_ratio=efficiency_ratio,
            stability_measure=stability_measure,
            growth_potential=growth_potential
        )
    
    def _calculate_connectivity_score(self) -> float:
        """Calculate network connectivity quality score"""
        if not self.network_graph.nodes():
            return 0.0
        
        # Node connectivity analysis
        node_connectivity = []
        for node in self.network_graph.nodes():
            degree = self.network_graph.degree(node)
            max_possible = len(self.network_graph.nodes()) - 1
            connectivity = degree / max_possible if max_possible > 0 else 0
            node_connectivity.append(connectivity)
        
        # Average connectivity
        avg_connectivity = statistics.mean(node_connectivity)
        
        # Connectivity distribution (prefer more even distribution)
        connectivity_variance = statistics.variance(node_connectivity) if len(node_connectivity) > 1 else 0
        distribution_score = max(0.0, 1.0 - connectivity_variance * 5)  # Penalize high variance
        
        return (avg_connectivity * 0.7 + distribution_score * 0.3)
    
    def _calculate_quality_index(self) -> float:
        """Calculate overall network quality index"""
        quality_factors = []
        
        # Edge weight quality
        edge_weights = [data.get('weight', 0.5) for _, _, data in self.network_graph.edges(data=True)]
        if edge_weights:
            avg_weight = statistics.mean(edge_weights)
            quality_factors.append(avg_weight * 0.3)
        
        # Centrality distribution
        centrality = nx.degree_centrality(self.network_graph)
        if centrality:
            centrality_values = list(centrality.values())
            centrality_balance = 1.0 - statistics.stdev(centrality_values) if len(centrality_values) > 1 else 1.0
            quality_factors.append(centrality_balance * 0.4)
        
        # Triangle density (good connectivity patterns)
        triangles = sum(nx.triangles(self.network_graph).values()) / 3
        possible_triangles = len(self.network_graph.nodes()) * (len(self.network_graph.nodes()) - 1) * (len(self.network_graph.nodes()) - 2) / 6
        triangle_ratio = triangles / possible_triangles if possible_triangles > 0 else 0
        quality_factors.append(min(triangle_ratio * 2, 1.0) * 0.3)  # Moderate triangle density is good
        
        return sum(quality_factors) if quality_factors else 0.0
    
    def _calculate_efficiency_ratio(self) -> float:
        """Calculate network efficiency ratio"""
        if not self.network_graph.nodes():
            return 0.0
        
        # Calculate actual vs theoretical optimal efficiency
        actual_edges = self.network_graph.number_of_edges()
        nodes = len(self.network_graph.nodes())
        
        # Theoretical minimum for connectivity (spanning tree)
        min_edges = nodes - 1 if nodes > 0 else 0
        
        # Theoretical maximum for complete graph
        max_edges = nodes * (nodes - 1) / 2 if nodes > 1 else 0
        
        if max_edges <= min_edges:
            return 0.0
        
        # Efficiency = how well we use edges (not too few, not too many)
        if actual_edges < min_edges:
            return 0.0  # Disconnected
        elif actual_edges > max_edges * 0.8:
            return 0.5  # Too dense
        else:
            # Optimal range calculation
            optimal_range = max_edges * 0.4  # Target around 40% of max density
            distance_from_optimal = abs(actual_edges - optimal_range)
            efficiency = max(0.0, 1.0 - (distance_from_optimal / optimal_range))
            return efficiency
    
    def _calculate_stability_measure(self) -> float:
        """Calculate network stability measure"""
        stability_factors = []
        
        # Degree distribution stability
        degrees = [self.network_graph.degree(node) for node in self.network_graph.nodes()]
        if degrees:
            degree_cv = statistics.stdev(degrees) / statistics.mean(degrees) if statistics.mean(degrees) > 0 else 0
            degree_stability = max(0.0, 1.0 - degree_cv)  # Lower coefficient of variation = more stable
            stability_factors.append(degree_stability * 0.4)
        
        # Clustering stability
        clustering_values = list(nx.clustering(self.network_graph).values())
        if clustering_values:
            clustering_cv = statistics.stdev(clustering_values) / statistics.mean(clustering_values) if statistics.mean(clustering_values) > 0 else 0
            clustering_stability = max(0.0, 1.0 - clustering_cv)
            stability_factors.append(clustering_stability * 0.3)
        
        # Core structure stability (measure of hub robustness)
        centrality = nx.degree_centrality(self.network_graph)
        if centrality:
            top_nodes = sorted(centrality.items(), key=lambda x: x[1], reverse=True)[:5]
            top_centrality = [x[1] for x in top_nodes]
            if len(top_centrality) > 1:
                hub_stability = 1.0 - (max(top_centrality) - min(top_centrality))
                stability_factors.append(hub_stability * 0.3)
        
        return sum(stability_factors) if stability_factors else 0.0
    
    def _calculate_growth_potential(self) -> float:
        """Calculate network growth potential"""
        if not self.network_graph.nodes():
            return 0.0
        
        growth_factors = []
        
        # Edge addition potential
        current_edges = self.network_graph.number_of_edges()
        nodes = len(self.network_graph.nodes())
        max_possible_edges = nodes * (nodes - 1) / 2
        
        if max_possible_edges > 0:
            edge_potential = (max_possible_edges - current_edges) / max_possible_edges
            # Moderate potential is best (not too sparse, not too dense)
            if edge_potential > 0.8:
                edge_score = 0.9  # High potential
            elif edge_potential > 0.5:
                edge_score = 1.0  # Optimal potential
            elif edge_potential > 0.2:
                edge_score = 0.7  # Limited potential
            else:
                edge_score = 0.3  # Low potential
            
            growth_factors.append(edge_score * 0.4)
        
        # Isolated node integration potential
        isolated_nodes = [node for node in self.network_graph.nodes() if self.network_graph.degree(node) < 2]
        isolation_potential = len(isolated_nodes) / len(self.network_graph.nodes())
        growth_factors.append(isolation_potential * 0.3)
        
        # Bridge opportunity potential
        bridges = list(nx.bridges(self.network_graph))
        bridge_potential = min(len(bridges) / 10.0, 1.0)  # More bridges = more growth opportunities
        growth_factors.append(bridge_potential * 0.3)
        
        return sum(growth_factors) if growth_factors else 0.0
    
    def analyze_trends(self) -> List[HealthTrend]:
        """Analyze health trends and predict future values"""
        trends = []
        
        if len(self.health_history) < 5:
            return trends  # Need minimum data for trend analysis
        
        # Extract recent measurements
        recent_metrics = list(self.health_history)[-self.trend_analysis_window:]
        
        # Analyze each metric
        metric_names = [
            'density', 'avg_path_length', 'clustering_coefficient',
            'connectivity_score', 'quality_index', 'efficiency_ratio',
            'stability_measure', 'growth_potential'
        ]
        
        for metric_name in metric_names:
            trend = self._analyze_metric_trend(metric_name, recent_metrics)
            if trend:
                trends.append(trend)
        
        return trends
    
    def _analyze_metric_trend(self, metric_name: str, measurements: List[NetworkHealthMetric]) -> Optional[HealthTrend]:
        """Analyze trend for a specific metric"""
        if len(measurements) < 3:
            return None
        
        # Extract values
        values = [getattr(m, metric_name) for m in measurements]
        timestamps = [m.timestamp for m in measurements]
        
        # Calculate trend direction and strength
        trend_direction, trend_strength = self._calculate_trend_direction(values)
        
        # Predict future value
        predicted_value = self._predict_future_value(values, timestamps)
        
        # Calculate confidence
        confidence = self._calculate_prediction_confidence(values)
        
        # Determine alert level
        alert_level = self._determine_trend_alert_level(metric_name, values[-1], trend_direction, trend_strength)
        
        return HealthTrend(
            metric_name=metric_name,
            current_value=values[-1],
            trend_direction=trend_direction,
            trend_strength=trend_strength,
            predicted_value=predicted_value,
            confidence=confidence,
            alert_level=alert_level
        )
    
    def _calculate_trend_direction(self, values: List[float]) -> Tuple[str, float]:
        """Calculate trend direction and strength"""
        if len(values) < 2:
            return 'stable', 0.0
        
        # Linear regression slope
        n = len(values)
        x_values = list(range(n))
        
        # Calculate slope
        x_mean = statistics.mean(x_values)
        y_mean = statistics.mean(values)
        
        numerator = sum((x_values[i] - x_mean) * (values[i] - y_mean) for i in range(n))
        denominator = sum((x_values[i] - x_mean) ** 2 for i in range(n))
        
        if denominator == 0:
            return 'stable', 0.0
        
        slope = numerator / denominator
        
        # Determine direction
        if abs(slope) < 0.001:
            direction = 'stable'
        elif slope > 0:
            direction = 'improving'
        else:
            direction = 'declining'
        
        # Calculate strength (0 to 1)
        strength = min(abs(slope) * 100, 1.0)  # Scale slope to 0-1 range
        
        return direction, strength
    
    def _predict_future_value(self, values: List[float], timestamps: List[datetime]) -> float:
        """Predict future value using weighted prediction model"""
        if len(values) < 2:
            return values[-1] if values else 0.0
        
        current_value = values[-1]
        
        # Recent trend prediction
        recent_trend = (values[-1] - values[-3]) / 2 if len(values) >= 3 else 0
        trend_prediction = current_value + recent_trend
        
        # Historical average prediction
        historical_avg = statistics.mean(values)
        
        # Seasonal pattern (simplified - look for weekly patterns)
        seasonal_prediction = current_value
        
        # External factors (simplified - assume stability)
        external_prediction = current_value
        
        # Weighted combination
        predicted_value = (
            trend_prediction * self.prediction_weights['recent_trend'] +
            historical_avg * self.prediction_weights['historical_average'] +
            seasonal_prediction * self.prediction_weights['seasonal_pattern'] +
            external_prediction * self.prediction_weights['external_factors']
        )
        
        # Ensure reasonable bounds
        min_value = min(values) * 0.8
        max_value = max(values) * 1.2
        predicted_value = max(min_value, min(predicted_value, max_value))
        
        return predicted_value
    
    def _calculate_prediction_confidence(self, values: List[float]) -> float:
        """Calculate confidence in prediction"""
        if len(values) < 3:
            return 0.5
        
        # Variance-based confidence
        variance = statistics.variance(values)
        variance_confidence = max(0.0, 1.0 - variance * 10)  # Lower variance = higher confidence
        
        # Trend consistency confidence
        recent_changes = [values[i] - values[i-1] for i in range(1, len(values))]
        if recent_changes:
            change_variance = statistics.variance(recent_changes)
            consistency_confidence = max(0.0, 1.0 - change_variance * 50)
        else:
            consistency_confidence = 0.5
        
        # Data quantity confidence
        quantity_confidence = min(len(values) / 20.0, 1.0)  # More data = higher confidence
        
        overall_confidence = (
            variance_confidence * 0.4 +
            consistency_confidence * 0.4 +
            quantity_confidence * 0.2
        )
        
        return overall_confidence
    
    def _determine_trend_alert_level(self, metric_name: str, current_value: float, 
                                   trend_direction: str, trend_strength: float) -> str:
        """Determine alert level for trend"""
        thresholds = self.health_thresholds.get(metric_name, {})
        
        # Check current value against thresholds
        if current_value < thresholds.get('critical', 0):
            return 'CRITICAL'
        elif current_value < thresholds.get('warning', 0):
            if trend_direction == 'declining' and trend_strength > 0.5:
                return 'HIGH'
            else:
                return 'MEDIUM'
        elif current_value < thresholds.get('good', 1):
            if trend_direction == 'declining' and trend_strength > 0.3:
                return 'MEDIUM'
            else:
                return 'LOW'
        else:
            if trend_direction == 'declining' and trend_strength > 0.7:
                return 'MEDIUM'
            else:
                return 'NONE'
    
    def generate_alerts(self, trends: List[HealthTrend]) -> List[NetworkAlert]:
        """Generate network health alerts based on trends"""
        alerts = []
        
        for trend in trends:
            if trend.alert_level in ['CRITICAL', 'HIGH', 'MEDIUM']:
                alert = self._create_trend_alert(trend)
                if alert:
                    alerts.append(alert)
        
        # Add system-wide alerts
        system_alerts = self._generate_system_alerts(trends)
        alerts.extend(system_alerts)
        
        return alerts
    
    def _create_trend_alert(self, trend: HealthTrend) -> Optional[NetworkAlert]:
        """Create alert for specific trend"""
        if trend.alert_level == 'NONE':
            return None
        
        # Generate alert message
        messages = {
            'density': f"Network density {trend.trend_direction} ({trend.current_value:.3f})",
            'avg_path_length': f"Average path length {trend.trend_direction} ({trend.current_value:.2f})",
            'clustering_coefficient': f"Clustering coefficient {trend.trend_direction} ({trend.current_value:.3f})",
            'connectivity_score': f"Connectivity quality {trend.trend_direction} ({trend.current_value:.3f})",
            'quality_index': f"Network quality index {trend.trend_direction} ({trend.current_value:.3f})",
            'efficiency_ratio': f"Network efficiency {trend.trend_direction} ({trend.current_value:.3f})",
            'stability_measure': f"Network stability {trend.trend_direction} ({trend.current_value:.3f})",
            'growth_potential': f"Growth potential {trend.trend_direction} ({trend.current_value:.3f})"
        }
        
        message = messages.get(trend.metric_name, f"Metric {trend.metric_name} showing concerning trend")
        
        # Generate predictions and recommendations
        if trend.trend_direction == 'declining':
            predicted_impact = f"May reach {trend.predicted_value:.3f} if trend continues"
            recommended_actions = self._get_improvement_recommendations(trend.metric_name)
        else:
            predicted_impact = f"Expected to improve to {trend.predicted_value:.3f}"
            recommended_actions = ["Monitor continued improvement", "Maintain current practices"]
        
        return NetworkAlert(
            alert_type='TREND_ALERT',
            severity=trend.alert_level,
            message=message,
            affected_components=[trend.metric_name],
            predicted_impact=predicted_impact,
            recommended_actions=recommended_actions,
            auto_resolvable=trend.alert_level == 'LOW',
            timestamp=datetime.now()
        )
    
    def _generate_system_alerts(self, trends: List[HealthTrend]) -> List[NetworkAlert]:
        """Generate system-wide alerts"""
        alerts = []
        
        # Multiple declining metrics alert
        declining_metrics = [t for t in trends if t.trend_direction == 'declining' and t.trend_strength > 0.3]
        if len(declining_metrics) >= 3:
            alerts.append(NetworkAlert(
                alert_type='SYSTEM_DEGRADATION',
                severity='HIGH',
                message=f"Multiple network metrics declining simultaneously ({len(declining_metrics)} metrics)",
                affected_components=[t.metric_name for t in declining_metrics],
                predicted_impact="Overall network health may deteriorate significantly",
                recommended_actions=[
                    "Comprehensive network analysis required",
                    "Review recent changes and their impact",
                    "Consider network restructuring"
                ],
                auto_resolvable=False,
                timestamp=datetime.now()
            ))
        
        # Low confidence predictions alert
        low_confidence_trends = [t for t in trends if t.confidence < 0.4]
        if len(low_confidence_trends) >= 2:
            alerts.append(NetworkAlert(
                alert_type='PREDICTION_UNCERTAINTY',
                severity='MEDIUM',
                message=f"High uncertainty in trend predictions ({len(low_confidence_trends)} metrics)",
                affected_components=[t.metric_name for t in low_confidence_trends],
                predicted_impact="Network evolution may be unpredictable",
                recommended_actions=[
                    "Increase monitoring frequency",
                    "Collect more data points",
                    "Review prediction models"
                ],
                auto_resolvable=True,
                timestamp=datetime.now()
            ))
        
        return alerts
    
    def _get_improvement_recommendations(self, metric_name: str) -> List[str]:
        """Get improvement recommendations for specific metric"""
        recommendations = {
            'density': [
                "Add strategic cross-references between related principles",
                "Review principle relationships for missing connections",
                "Enhance documentation linking"
            ],
            'avg_path_length': [
                "Create bridge connections between distant principle clusters",
                "Add hub principles to reduce path lengths",
                "Review network topology for optimization opportunities"
            ],
            'clustering_coefficient': [
                "Strengthen connections within principle clusters",
                "Create triangular relationships where appropriate",
                "Review semantic relationships for enhancement"
            ],
            'connectivity_score': [
                "Balance connection distribution across principles",
                "Address isolated or poorly connected principles",
                "Enhance bidirectional linking"
            ],
            'quality_index': [
                "Review and improve connection quality",
                "Strengthen weak cross-references",
                "Remove or improve low-value connections"
            ],
            'efficiency_ratio': [
                "Optimize connection density",
                "Remove redundant connections",
                "Add missing strategic connections"
            ],
            'stability_measure': [
                "Balance degree distribution",
                "Strengthen hub principle connections",
                "Improve network resilience"
            ],
            'growth_potential': [
                "Identify and connect isolated principles",
                "Create bridge opportunities",
                "Plan strategic network expansion"
            ]
        }
        
        return recommendations.get(metric_name, ["Review metric-specific optimization strategies"])
    
    def generate_optimization_recommendations(self, current_health: NetworkHealthMetric, 
                                           trends: List[HealthTrend]) -> List[OptimizationRecommendation]:
        """Generate network optimization recommendations"""
        recommendations = []
        
        # Analyze each metric for optimization opportunities
        for trend in trends:
            if trend.current_value < self.health_thresholds[trend.metric_name].get('good', 1.0):
                rec = self._create_optimization_recommendation(trend, current_health)
                if rec:
                    recommendations.append(rec)
        
        # Sort by predicted benefit and priority
        recommendations.sort(key=lambda x: (x.priority == 'HIGH', x.predicted_benefit), reverse=True)
        
        return recommendations
    
    def _create_optimization_recommendation(self, trend: HealthTrend, 
                                         current_health: NetworkHealthMetric) -> Optional[OptimizationRecommendation]:
        """Create optimization recommendation for specific trend"""
        metric_name = trend.metric_name
        current_value = trend.current_value
        
        # Calculate predicted benefit
        target_value = self.health_thresholds[metric_name].get('good', 1.0)
        potential_improvement = target_value - current_value
        predicted_benefit = min(potential_improvement / target_value, 1.0) if target_value > 0 else 0.0
        
        # Determine priority
        if trend.alert_level in ['CRITICAL', 'HIGH']:
            priority = 'HIGH'
        elif trend.alert_level == 'MEDIUM':
            priority = 'MEDIUM'
        else:
            priority = 'LOW'
        
        # Generate specific recommendations
        rec_data = self._get_specific_recommendation(metric_name, current_value, predicted_benefit)
        
        return OptimizationRecommendation(
            recommendation_type=rec_data['type'],
            priority=priority,
            description=rec_data['description'],
            predicted_benefit=predicted_benefit,
            implementation_effort=rec_data['effort'],
            risk_level=rec_data['risk'],
            target_components=rec_data['targets'],
            success_probability=self._calculate_success_probability(metric_name, predicted_benefit)
        )
    
    def _get_specific_recommendation(self, metric_name: str, current_value: float, 
                                   predicted_benefit: float) -> Dict[str, Any]:
        """Get specific recommendation details for metric"""
        recommendations = {
            'density': {
                'type': 'CONNECTION_ENHANCEMENT',
                'description': f"Increase network density from {current_value:.3f} by adding strategic cross-references",
                'effort': 'MEDIUM',
                'risk': 'LOW',
                'targets': ['principle-cross-reference-network', 'documentation-linking-framework']
            },
            'avg_path_length': {
                'type': 'PATH_OPTIMIZATION',
                'description': f"Reduce average path length from {current_value:.2f} by creating bridge connections",
                'effort': 'HIGH',
                'risk': 'MEDIUM',
                'targets': ['network-topology', 'bridge-principles']
            },
            'clustering_coefficient': {
                'type': 'CLUSTER_STRENGTHENING',
                'description': f"Improve clustering from {current_value:.3f} by enhancing principle group connections",
                'effort': 'MEDIUM',
                'risk': 'LOW',
                'targets': ['principle-clusters', 'semantic-relationships']
            },
            'connectivity_score': {
                'type': 'CONNECTIVITY_BALANCING',
                'description': f"Improve connectivity score from {current_value:.3f} by balancing connection distribution",
                'effort': 'HIGH',
                'risk': 'MEDIUM',
                'targets': ['isolated-principles', 'hub-principles']
            }
        }
        
        return recommendations.get(metric_name, {
            'type': 'GENERAL_OPTIMIZATION',
            'description': f"Improve {metric_name} from current value {current_value:.3f}",
            'effort': 'MEDIUM',
            'risk': 'LOW',
            'targets': [metric_name]
        })
    
    def _calculate_success_probability(self, metric_name: str, predicted_benefit: float) -> float:
        """Calculate probability of successful optimization"""
        base_probability = 0.7  # Base success rate
        
        # Higher benefit = higher probability
        benefit_factor = predicted_benefit * 0.2
        
        # Metric-specific factors
        metric_factors = {
            'density': 0.8,           # Easy to add connections
            'avg_path_length': 0.6,   # Harder to optimize paths
            'clustering_coefficient': 0.7,  # Moderate difficulty
            'connectivity_score': 0.6,      # Requires careful balancing
            'quality_index': 0.5,          # Complex optimization
            'efficiency_ratio': 0.6,       # Requires strategic decisions
            'stability_measure': 0.5,      # Complex system property
            'growth_potential': 0.8        # Usually achievable
        }
        
        metric_factor = metric_factors.get(metric_name, 0.6)
        
        success_probability = base_probability * metric_factor + benefit_factor
        return min(success_probability, 0.95)  # Cap at 95%
    
    def generate_health_report(self) -> str:
        """Generate comprehensive network health report"""
        # Measure current health
        current_health = self.measure_current_health()
        
        # Analyze trends
        trends = self.analyze_trends()
        
        # Generate alerts
        alerts = self.generate_alerts(trends)
        
        # Generate optimization recommendations
        recommendations = self.generate_optimization_recommendations(current_health, trends)
        
        # Build report
        report = []
        report.append("# 🏥 Network Health Monitoring Report")
        report.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"**Monitoring Window**: {len(self.health_history)} measurements")
        report.append("")
        
        # Current health section
        report.append("## 📊 Current Network Health")
        report.append("")
        report.append(f"- **Density**: {current_health.density:.3f}")
        report.append(f"- **Average Path Length**: {current_health.avg_path_length:.2f}")
        report.append(f"- **Clustering Coefficient**: {current_health.clustering_coefficient:.3f}")
        report.append(f"- **Connectivity Score**: {current_health.connectivity_score:.3f}")
        report.append(f"- **Quality Index**: {current_health.quality_index:.3f}")
        report.append(f"- **Efficiency Ratio**: {current_health.efficiency_ratio:.3f}")
        report.append(f"- **Stability Measure**: {current_health.stability_measure:.3f}")
        report.append(f"- **Growth Potential**: {current_health.growth_potential:.3f}")
        report.append("")
        
        # Overall health score
        overall_health = (
            current_health.density * 0.15 +
            (4.0 - min(current_health.avg_path_length, 4.0)) / 4.0 * 0.15 +
            current_health.clustering_coefficient * 0.15 +
            current_health.connectivity_score * 0.15 +
            current_health.quality_index * 0.15 +
            current_health.efficiency_ratio * 0.10 +
            current_health.stability_measure * 0.10 +
            current_health.growth_potential * 0.05
        )
        
        report.append(f"**Overall Health Score**: {overall_health:.1%}")
        report.append("")
        
        # Trends section
        if trends:
            report.append("## 📈 Health Trends")
            report.append("")
            for trend in trends:
                icon = "📈" if trend.trend_direction == "improving" else "📉" if trend.trend_direction == "declining" else "➡️"
                report.append(f"- **{trend.metric_name}**: {icon} {trend.trend_direction.upper()}")
                report.append(f"  - Current: {trend.current_value:.3f}")
                report.append(f"  - Predicted: {trend.predicted_value:.3f}")
                report.append(f"  - Confidence: {trend.confidence:.1%}")
                report.append("")
        
        # Alerts section
        if alerts:
            report.append("## 🚨 Health Alerts")
            report.append("")
            
            by_severity = defaultdict(list)
            for alert in alerts:
                by_severity[alert.severity].append(alert)
            
            for severity in ['CRITICAL', 'HIGH', 'MEDIUM']:
                if by_severity[severity]:
                    report.append(f"### {severity} Severity")
                    report.append("")
                    for alert in by_severity[severity]:
                        report.append(f"**{alert.message}**")
                        report.append(f"- Type: {alert.alert_type}")
                        report.append(f"- Impact: {alert.predicted_impact}")
                        report.append(f"- Actions: {', '.join(alert.recommended_actions[:2])}")
                        report.append("")
        
        # Optimization recommendations section
        if recommendations:
            report.append("## ⚡ Optimization Recommendations")
            report.append("")
            
            high_priority = [r for r in recommendations if r.priority == 'HIGH']
            if high_priority:
                report.append("### High Priority Optimizations")
                report.append("")
                for rec in high_priority[:5]:
                    report.append(f"**{rec.description}**")
                    report.append(f"- Predicted Benefit: {rec.predicted_benefit:.1%}")
                    report.append(f"- Implementation Effort: {rec.implementation_effort}")
                    report.append(f"- Success Probability: {rec.success_probability:.1%}")
                    report.append("")
        
        # Add historical data point
        self.health_history.append(current_health)
        self._save_historical_data()
        
        return "\n".join(report)
    
    def start_continuous_monitoring(self):
        """Start continuous network health monitoring"""
        print(f"🔄 Starting continuous network health monitoring (interval: {self.monitoring_interval}s)")
        
        def monitoring_loop():
            while True:
                try:
                    # Generate health report
                    report = self.generate_health_report()
                    
                    # Save report
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    report_path = self.cache_path / f"health_report_{timestamp}.md"
                    report_path.write_text(report)
                    
                    print(f"📋 Health report generated: {report_path.name}")
                    
                    time.sleep(self.monitoring_interval)
                    
                except Exception as e:
                    print(f"❌ Monitoring error: {e}")
                    time.sleep(60)  # Wait before retrying
        
        # Start monitoring in background thread
        monitoring_thread = threading.Thread(target=monitoring_loop, daemon=True)
        monitoring_thread.start()
        
        return monitoring_thread


def main():
    """Main execution function"""
    monitor = NetworkHealthMonitor()
    
    print("🏥 Starting Network Health Analysis...")
    
    if not monitor.network_graph:
        print("❌ Could not load network graph")
        return 1
    
    # Generate initial health report
    print("📊 Generating health report...")
    report = monitor.generate_health_report()
    
    # Save report
    report_path = Path("operations/reports/current/network-health-analysis.md")
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)
    
    print(f"✅ Network health analysis complete!")
    print(f"📋 Report saved to: {report_path}")
    
    # Optionally start continuous monitoring
    if "--continuous" in sys.argv:
        monitor.start_continuous_monitoring()
        print("🔄 Continuous monitoring started. Press Ctrl+C to stop.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\n🛑 Monitoring stopped.")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())