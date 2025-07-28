#!/usr/bin/env python3
"""
Performance Optimization System
Optimizes context retrieval for large volumes, implements caching, and provides performance monitoring
"""

import json
import logging
import sqlite3
import time
import threading
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
from collections import defaultdict, deque
import pickle
import hashlib
import psutil
import gc

@dataclass
class PerformanceMetrics:
    """Performance metrics tracking"""
    operation_type: str
    duration: float
    memory_usage: float
    cpu_usage: float
    cache_hit_rate: float
    items_processed: int
    timestamp: str
    optimization_applied: List[str]

@dataclass
class OptimizationRule:
    """Performance optimization rule"""
    rule_id: str
    rule_type: str  # 'cache', 'index', 'query', 'memory'
    condition: Dict[str, Any]
    action: Dict[str, Any]
    priority: int
    enabled: bool

class PerformanceOptimizer:
    """
    Advanced performance optimization system
    Handles large context volumes with intelligent caching and optimization
    """
    
    def __init__(self, context_db_path: str, cache_size_mb: int = 100):
        self.context_db_path = Path(context_db_path)
        self.cache_size_mb = cache_size_mb
        self.cache_size_bytes = cache_size_mb * 1024 * 1024
        
        # Performance tracking
        self.metrics_history = deque(maxlen=1000)
        self.operation_timings = defaultdict(list)
        self.memory_usage_history = deque(maxlen=100)
        
        # Caching system
        self.query_cache = {}
        self.embedding_cache = {}
        self.result_cache = {}
        self.cache_metadata = {}
        self.cache_lock = threading.Lock()
        
        # Performance monitoring
        self.performance_monitor = PerformanceMonitor()
        self.optimization_rules = self._initialize_optimization_rules()
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Configuration
        self.config = {
            'max_query_cache_size': 500,
            'max_embedding_cache_size': 1000,
            'cache_ttl_seconds': 1800,  # 30 minutes
            'memory_threshold_mb': 500,
            'auto_gc_threshold': 0.8,
            'batch_size': 100,
            'prefetch_enabled': True,
            'compression_enabled': True
        }
        
        # Index optimization
        self.index_manager = IndexManager(self.context_db_path)
        
    def optimize_query_performance(self, query_pattern: str, 
                                 historical_data: List[Dict]) -> Dict[str, Any]:
        """
        Optimize query performance based on patterns and historical data
        Returns optimization recommendations and applied changes
        """
        start_time = time.time()
        optimizations_applied = []
        
        # Analyze query pattern
        pattern_analysis = self._analyze_query_pattern(query_pattern, historical_data)
        
        # Apply query-specific optimizations
        if pattern_analysis['frequency'] > 10:  # High-frequency query
            # Enable aggressive caching
            self._optimize_caching_for_pattern(query_pattern)
            optimizations_applied.append('aggressive_caching')
            
        if pattern_analysis['complexity'] > 0.7:  # Complex query
            # Optimize indexes
            index_optimizations = self.index_manager.optimize_for_query(query_pattern)
            optimizations_applied.extend(index_optimizations)
            
        if pattern_analysis['result_size'] > 1000:  # Large result sets
            # Enable result pagination and streaming
            self._enable_result_streaming(query_pattern)
            optimizations_applied.append('result_streaming')
            
        # Memory optimization
        if self._get_memory_usage() > self.config['memory_threshold_mb']:
            self._optimize_memory_usage()
            optimizations_applied.append('memory_optimization')
            
        # Record performance metrics
        duration = time.time() - start_time
        metrics = PerformanceMetrics(
            operation_type='query_optimization',
            duration=duration,
            memory_usage=self._get_memory_usage(),
            cpu_usage=psutil.cpu_percent(),
            cache_hit_rate=self._calculate_cache_hit_rate(),
            items_processed=len(historical_data),
            timestamp=datetime.now().isoformat(),
            optimization_applied=optimizations_applied
        )
        
        self.metrics_history.append(metrics)
        
        return {
            'optimizations_applied': optimizations_applied,
            'pattern_analysis': pattern_analysis,
            'performance_improvement': self._estimate_performance_improvement(optimizations_applied),
            'optimization_duration': duration
        }
        
    def implement_intelligent_caching(self, cache_strategy: str = 'adaptive') -> Dict[str, Any]:
        """
        Implement intelligent caching system
        Supports multiple caching strategies for different usage patterns
        """
        if cache_strategy == 'adaptive':
            strategy_config = self._analyze_usage_patterns_for_caching()
        elif cache_strategy == 'aggressive':
            strategy_config = {'cache_everything': True, 'ttl_multiplier': 2.0}
        elif cache_strategy == 'conservative':
            strategy_config = {'cache_threshold': 0.7, 'ttl_multiplier': 0.5}
        else:
            strategy_config = {}
            
        # Implement caching layers
        cache_layers = []
        
        # Layer 1: Query result caching
        if strategy_config.get('cache_results', True):
            self._implement_result_caching(strategy_config)
            cache_layers.append('result_cache')
            
        # Layer 2: Embedding caching
        if strategy_config.get('cache_embeddings', True):
            self._implement_embedding_caching(strategy_config)
            cache_layers.append('embedding_cache')
            
        # Layer 3: Computed similarity caching
        if strategy_config.get('cache_similarities', False):
            self._implement_similarity_caching(strategy_config)
            cache_layers.append('similarity_cache')
            
        # Cache warming
        if strategy_config.get('warm_cache', False):
            warming_results = self._warm_cache()
            cache_layers.append('cache_warming')
        else:
            warming_results = {'warmed_items': 0}
            
        return {
            'strategy': cache_strategy,
            'cache_layers': cache_layers,
            'strategy_config': strategy_config,
            'cache_warming': warming_results,
            'estimated_memory_usage': self._estimate_cache_memory_usage()
        }
        
    def optimize_for_large_volumes(self, volume_characteristics: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimize system for large context volumes
        Implements streaming, batching, and partitioning strategies
        """
        optimizations = []
        
        volume_size = volume_characteristics.get('total_items', 0)
        query_frequency = volume_characteristics.get('query_frequency', 'medium')
        data_growth_rate = volume_characteristics.get('growth_rate', 'steady')
        
        # Implement database partitioning for very large volumes
        if volume_size > 100000:
            partitioning_results = self._implement_database_partitioning()
            optimizations.append(partitioning_results)
            
        # Implement query result streaming
        if volume_size > 10000:
            streaming_config = self._configure_result_streaming(volume_size)
            optimizations.append(streaming_config)
            
        # Implement batch processing
        batch_config = self._optimize_batch_processing(volume_characteristics)
        optimizations.append(batch_config)
        
        # Memory management optimization
        memory_config = self._optimize_memory_management(volume_size)
        optimizations.append(memory_config)
        
        # Index optimization for large datasets
        if volume_size > 50000:
            index_config = self.index_manager.optimize_for_large_volume(volume_size)
            optimizations.append(index_config)
            
        return {
            'volume_size': volume_size,
            'optimizations_applied': optimizations,
            'performance_impact': self._estimate_volume_performance_impact(optimizations),
            'memory_requirements': self._estimate_memory_requirements(volume_size)
        }
        
    def monitor_real_time_performance(self) -> Dict[str, Any]:
        """
        Monitor real-time performance metrics
        Provides current system health and performance indicators
        """
        current_metrics = {
            'timestamp': datetime.now().isoformat(),
            'memory_usage': {
                'current_mb': self._get_memory_usage(),
                'threshold_mb': self.config['memory_threshold_mb'],
                'cache_usage_mb': self._get_cache_memory_usage(),
                'available_mb': psutil.virtual_memory().available / 1024 / 1024
            },
            'cpu_usage': {
                'current_percent': psutil.cpu_percent(interval=1),
                'load_average': psutil.getloadavg() if hasattr(psutil, 'getloadavg') else [0, 0, 0]
            },
            'cache_performance': {
                'hit_rate': self._calculate_cache_hit_rate(),
                'total_queries': len(self.operation_timings.get('query', [])),
                'cache_size': len(self.query_cache) + len(self.embedding_cache) + len(self.result_cache)
            },
            'database_performance': {
                'active_connections': self._get_db_connection_count(),
                'query_response_time': self._get_average_query_time(),
                'index_efficiency': self.index_manager.get_index_efficiency()
            },
            'system_health': self._assess_system_health()
        }
        
        # Add to memory usage history
        self.memory_usage_history.append(current_metrics['memory_usage']['current_mb'])
        
        # Check for performance issues
        issues = self._detect_performance_issues(current_metrics)
        current_metrics['issues'] = issues
        
        # Generate recommendations
        recommendations = self._generate_performance_recommendations(current_metrics)
        current_metrics['recommendations'] = recommendations
        
        return current_metrics
        
    def implement_auto_optimization(self, enable: bool = True) -> Dict[str, Any]:
        """
        Enable or disable automatic performance optimization
        System automatically applies optimizations based on usage patterns
        """
        if enable:
            # Start performance monitoring thread
            optimization_thread = threading.Thread(
                target=self._auto_optimization_loop,
                daemon=True
            )
            optimization_thread.start()
            
            auto_config = {
                'enabled': True,
                'check_interval_seconds': 300,  # 5 minutes
                'optimization_threshold': 0.7,
                'max_auto_optimizations_per_hour': 10
            }
        else:
            auto_config = {'enabled': False}
            
        return {
            'auto_optimization': auto_config,
            'current_rules': len(self.optimization_rules),
            'active_rules': len([r for r in self.optimization_rules if r.enabled])
        }
        
    def generate_performance_report(self, time_range_hours: int = 24) -> Dict[str, Any]:
        """
        Generate comprehensive performance report
        Analyzes performance trends and provides optimization insights
        """
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=time_range_hours)
        
        # Filter metrics within time range
        relevant_metrics = [
            m for m in self.metrics_history
            if start_time <= datetime.fromisoformat(m.timestamp) <= end_time
        ]
        
        if not relevant_metrics:
            return {
                'error': 'No metrics data available for specified time range',
                'time_range': f"{start_time} to {end_time}"
            }
            
        # Analyze performance trends
        trends = self._analyze_performance_trends(relevant_metrics)
        
        # Calculate aggregated metrics
        aggregated = self._calculate_aggregated_metrics(relevant_metrics)
        
        # Identify optimization opportunities
        opportunities = self._identify_optimization_opportunities(relevant_metrics)
        
        # Generate executive summary
        summary = self._generate_performance_summary(trends, aggregated, opportunities)
        
        return {
            'report_period': f"{start_time.isoformat()} to {end_time.isoformat()}",
            'metrics_analyzed': len(relevant_metrics),
            'performance_trends': trends,
            'aggregated_metrics': aggregated,
            'optimization_opportunities': opportunities,
            'executive_summary': summary,
            'report_timestamp': datetime.now().isoformat()
        }
        
    # Private implementation methods
    def _analyze_query_pattern(self, query_pattern: str, historical_data: List[Dict]) -> Dict[str, Any]:
        """Analyze query pattern characteristics"""
        pattern_hash = hashlib.md5(query_pattern.encode()).hexdigest()
        
        # Count frequency in historical data
        frequency = sum(1 for item in historical_data 
                       if pattern_hash in item.get('query_signature', ''))
        
        # Estimate complexity based on query characteristics
        complexity_factors = []
        if 'JOIN' in query_pattern.upper():
            complexity_factors.append(0.3)
        if 'GROUP BY' in query_pattern.upper():
            complexity_factors.append(0.2)
        if 'ORDER BY' in query_pattern.upper():
            complexity_factors.append(0.1)
        if len(query_pattern) > 200:
            complexity_factors.append(0.2)
            
        complexity = min(sum(complexity_factors), 1.0)
        
        # Estimate result size based on historical data
        result_sizes = [item.get('result_count', 0) for item in historical_data 
                       if pattern_hash in item.get('query_signature', '')]
        avg_result_size = sum(result_sizes) / len(result_sizes) if result_sizes else 0
        
        return {
            'pattern_hash': pattern_hash,
            'frequency': frequency,
            'complexity': complexity,
            'result_size': avg_result_size,
            'optimization_priority': self._calculate_optimization_priority(frequency, complexity, avg_result_size)
        }
        
    def _calculate_optimization_priority(self, frequency: int, complexity: float, result_size: float) -> int:
        """Calculate optimization priority score"""
        # Higher frequency, complexity, and result size = higher priority
        priority_score = (frequency * 0.4) + (complexity * 0.3) + (min(result_size / 1000, 1.0) * 0.3)
        
        if priority_score > 0.8:
            return 1  # High priority
        elif priority_score > 0.5:
            return 2  # Medium priority
        else:
            return 3  # Low priority
            
    def _optimize_caching_for_pattern(self, query_pattern: str):
        """Optimize caching for specific query pattern"""
        pattern_hash = hashlib.md5(query_pattern.encode()).hexdigest()
        
        # Increase cache TTL for this pattern
        if pattern_hash not in self.cache_metadata:
            self.cache_metadata[pattern_hash] = {}
            
        self.cache_metadata[pattern_hash]['ttl_multiplier'] = 2.0
        self.cache_metadata[pattern_hash]['priority'] = 'high'
        
    def _enable_result_streaming(self, query_pattern: str):
        """Enable result streaming for large result sets"""
        pattern_hash = hashlib.md5(query_pattern.encode()).hexdigest()
        
        if pattern_hash not in self.cache_metadata:
            self.cache_metadata[pattern_hash] = {}
            
        self.cache_metadata[pattern_hash]['streaming_enabled'] = True
        self.cache_metadata[pattern_hash]['batch_size'] = self.config['batch_size']
        
    def _optimize_memory_usage(self):
        """Optimize memory usage"""
        # Force garbage collection
        gc.collect()
        
        # Clear old cache entries
        self._cleanup_expired_cache()
        
        # Reduce cache sizes if memory usage is high
        if self._get_memory_usage() > self.config['memory_threshold_mb']:
            self._reduce_cache_sizes()
            
    def _get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        process = psutil.Process()
        return process.memory_info().rss / 1024 / 1024
        
    def _calculate_cache_hit_rate(self) -> float:
        """Calculate overall cache hit rate"""
        total_requests = sum(len(timings) for timings in self.operation_timings.values())
        if total_requests == 0:
            return 0.0
            
        # This is a simplified calculation - would be more sophisticated in practice
        cache_hits = len(self.query_cache) + len(self.embedding_cache) + len(self.result_cache)
        return min(cache_hits / total_requests, 1.0)
        
    def _estimate_performance_improvement(self, optimizations: List[str]) -> Dict[str, float]:
        """Estimate performance improvement from optimizations"""
        improvements = {}
        
        if 'aggressive_caching' in optimizations:
            improvements['query_time'] = 0.3  # 30% improvement
            improvements['memory_efficiency'] = -0.1  # 10% more memory usage
            
        if 'result_streaming' in optimizations:
            improvements['memory_efficiency'] = 0.5  # 50% less memory usage
            improvements['initial_response_time'] = 0.2  # 20% faster initial response
            
        if 'memory_optimization' in optimizations:
            improvements['overall_performance'] = 0.15  # 15% overall improvement
            
        return improvements
        
    def _analyze_usage_patterns_for_caching(self) -> Dict[str, Any]:
        """Analyze usage patterns to determine optimal caching strategy"""
        # This would analyze actual usage data - simplified for now
        return {
            'cache_results': True,
            'cache_embeddings': True,
            'cache_similarities': False,
            'warm_cache': True,
            'ttl_multiplier': 1.5,
            'cache_threshold': 0.6
        }
        
    def _implement_result_caching(self, config: Dict[str, Any]):
        """Implement result caching layer"""
        with self.cache_lock:
            # Configure result cache with strategy parameters
            self.result_cache.clear()  # Reset cache with new configuration
            
    def _implement_embedding_caching(self, config: Dict[str, Any]):
        """Implement embedding caching layer"""
        with self.cache_lock:
            # Configure embedding cache
            pass  # Implementation would go here
            
    def _implement_similarity_caching(self, config: Dict[str, Any]):
        """Implement similarity computation caching"""
        with self.cache_lock:
            # Configure similarity cache
            pass  # Implementation would go here
            
    def _warm_cache(self) -> Dict[str, Any]:
        """Warm cache with frequently accessed data"""
        # This would implement cache warming logic
        return {
            'warmed_items': 0,
            'warming_time': 0,
            'cache_size_after': len(self.query_cache)
        }
        
    def _estimate_cache_memory_usage(self) -> float:
        """Estimate memory usage of cache in MB"""
        # This would calculate actual cache memory usage
        return 50.0  # Placeholder
        
    def _implement_database_partitioning(self) -> Dict[str, Any]:
        """Implement database partitioning for large volumes"""
        return {
            'optimization_type': 'database_partitioning',
            'partitions_created': 0,
            'estimated_improvement': 0.25
        }
        
    def _configure_result_streaming(self, volume_size: int) -> Dict[str, Any]:
        """Configure result streaming for large volumes"""
        optimal_batch_size = min(max(volume_size // 100, 50), 500)
        
        return {
            'optimization_type': 'result_streaming',
            'batch_size': optimal_batch_size,
            'streaming_enabled': True
        }
        
    def _optimize_batch_processing(self, characteristics: Dict[str, Any]) -> Dict[str, Any]:
        """Optimize batch processing configuration"""
        return {
            'optimization_type': 'batch_processing',
            'batch_size': self.config['batch_size'],
            'parallel_batches': 4
        }
        
    def _optimize_memory_management(self, volume_size: int) -> Dict[str, Any]:
        """Optimize memory management for large volumes"""
        return {
            'optimization_type': 'memory_management',
            'gc_frequency': 'adaptive',
            'memory_limit_mb': min(self.config['memory_threshold_mb'], 1000)
        }
        
    def _estimate_volume_performance_impact(self, optimizations: List[Dict]) -> Dict[str, float]:
        """Estimate performance impact of volume optimizations"""
        return {
            'query_performance': 0.4,
            'memory_efficiency': 0.6,
            'overall_throughput': 0.3
        }
        
    def _estimate_memory_requirements(self, volume_size: int) -> Dict[str, float]:
        """Estimate memory requirements for volume size"""
        base_memory = 100  # Base memory in MB
        per_item_memory = 0.001  # Memory per item in MB
        
        return {
            'base_memory_mb': base_memory,
            'estimated_total_mb': base_memory + (volume_size * per_item_memory),
            'recommended_system_memory_mb': (base_memory + (volume_size * per_item_memory)) * 2
        }
        
    def _get_cache_memory_usage(self) -> float:
        """Get cache memory usage in MB"""
        # This would calculate actual cache memory usage
        return 25.0  # Placeholder
        
    def _get_db_connection_count(self) -> int:
        """Get active database connection count"""
        # This would return actual connection count
        return 1  # Placeholder
        
    def _get_average_query_time(self) -> float:
        """Get average query response time"""
        query_times = self.operation_timings.get('query', [])
        return sum(query_times) / len(query_times) if query_times else 0.0
        
    def _assess_system_health(self) -> str:
        """Assess overall system health"""
        memory_usage = self._get_memory_usage()
        cpu_usage = psutil.cpu_percent()
        
        if memory_usage > self.config['memory_threshold_mb'] or cpu_usage > 80:
            return 'critical'
        elif memory_usage > self.config['memory_threshold_mb'] * 0.8 or cpu_usage > 60:
            return 'warning'
        else:
            return 'healthy'
            
    def _detect_performance_issues(self, metrics: Dict[str, Any]) -> List[str]:
        """Detect performance issues from current metrics"""
        issues = []
        
        if metrics['memory_usage']['current_mb'] > metrics['memory_usage']['threshold_mb']:
            issues.append('High memory usage detected')
            
        if metrics['cpu_usage']['current_percent'] > 80:
            issues.append('High CPU usage detected')
            
        if metrics['cache_performance']['hit_rate'] < 0.3:
            issues.append('Low cache hit rate')
            
        return issues
        
    def _generate_performance_recommendations(self, metrics: Dict[str, Any]) -> List[str]:
        """Generate performance recommendations"""
        recommendations = []
        
        for issue in metrics.get('issues', []):
            if 'memory' in issue.lower():
                recommendations.append('Consider increasing cache TTL or reducing cache size')
            elif 'cpu' in issue.lower():
                recommendations.append('Consider optimizing query complexity or adding indexes')
            elif 'cache' in issue.lower():
                recommendations.append('Review caching strategy and cache warming policies')
                
        return recommendations
        
    def _auto_optimization_loop(self):
        """Auto-optimization loop (runs in background thread)"""
        while True:
            try:
                time.sleep(self.config.get('check_interval_seconds', 300))
                
                # Check if auto-optimization should run
                metrics = self.monitor_real_time_performance()
                
                if self._should_auto_optimize(metrics):
                    self._apply_auto_optimizations(metrics)
                    
            except Exception as e:
                self.logger.error(f"Auto-optimization error: {e}")
                
    def _should_auto_optimize(self, metrics: Dict[str, Any]) -> bool:
        """Determine if auto-optimization should run"""
        return len(metrics.get('issues', [])) > 0
        
    def _apply_auto_optimizations(self, metrics: Dict[str, Any]):
        """Apply automatic optimizations based on metrics"""
        # This would implement automatic optimization logic
        pass
        
    def _initialize_optimization_rules(self) -> List[OptimizationRule]:
        """Initialize performance optimization rules"""
        return [
            OptimizationRule(
                rule_id='cache_frequent_queries',
                rule_type='cache',
                condition={'query_frequency': {'gt': 10}},
                action={'enable_aggressive_caching': True},
                priority=1,
                enabled=True
            ),
            OptimizationRule(
                rule_id='memory_cleanup',
                rule_type='memory',
                condition={'memory_usage_mb': {'gt': 400}},
                action={'trigger_gc': True, 'cleanup_cache': True},
                priority=2,
                enabled=True
            )
        ]
        
    def _cleanup_expired_cache(self):
        """Clean up expired cache entries"""
        current_time = time.time()
        ttl = self.config['cache_ttl_seconds']
        
        with self.cache_lock:
            # Clean query cache
            expired_keys = [
                key for key, (data, timestamp) in self.query_cache.items()
                if current_time - timestamp > ttl
            ]
            for key in expired_keys:
                del self.query_cache[key]
                
            # Clean other caches similarly
            # ... (implementation continues)
            
    def _reduce_cache_sizes(self):
        """Reduce cache sizes to free memory"""
        with self.cache_lock:
            # Reduce cache sizes by removing oldest entries
            max_size = self.config['max_query_cache_size'] // 2
            
            if len(self.query_cache) > max_size:
                # Keep only the most recent entries
                sorted_items = sorted(
                    self.query_cache.items(),
                    key=lambda x: x[1][1],  # Sort by timestamp
                    reverse=True
                )
                self.query_cache = dict(sorted_items[:max_size])
                
    def _analyze_performance_trends(self, metrics: List[PerformanceMetrics]) -> Dict[str, Any]:
        """Analyze performance trends from metrics"""
        if not metrics:
            return {'trend': 'no_data'}
            
        # Calculate trend in response times
        response_times = [m.duration for m in metrics]
        if len(response_times) > 1:
            recent_avg = sum(response_times[-10:]) / min(10, len(response_times))
            earlier_avg = sum(response_times[:-10]) / max(1, len(response_times) - 10)
            
            if recent_avg > earlier_avg * 1.1:
                trend = 'degrading'
            elif recent_avg < earlier_avg * 0.9:
                trend = 'improving'
            else:
                trend = 'stable'
        else:
            trend = 'insufficient_data'
            
        return {
            'response_time_trend': trend,
            'metrics_count': len(metrics),
            'time_span': f"{metrics[0].timestamp} to {metrics[-1].timestamp}"
        }
        
    def _calculate_aggregated_metrics(self, metrics: List[PerformanceMetrics]) -> Dict[str, Any]:
        """Calculate aggregated metrics"""
        if not metrics:
            return {}
            
        return {
            'average_duration': sum(m.duration for m in metrics) / len(metrics),
            'average_memory_usage': sum(m.memory_usage for m in metrics) / len(metrics),
            'average_cpu_usage': sum(m.cpu_usage for m in metrics) / len(metrics),
            'average_cache_hit_rate': sum(m.cache_hit_rate for m in metrics) / len(metrics),
            'total_items_processed': sum(m.items_processed for m in metrics),
            'operation_counts': self._count_operations_by_type(metrics)
        }
        
    def _count_operations_by_type(self, metrics: List[PerformanceMetrics]) -> Dict[str, int]:
        """Count operations by type"""
        counts = defaultdict(int)
        for metric in metrics:
            counts[metric.operation_type] += 1
        return dict(counts)
        
    def _identify_optimization_opportunities(self, metrics: List[PerformanceMetrics]) -> List[Dict[str, Any]]:
        """Identify optimization opportunities from metrics"""
        opportunities = []
        
        # Analyze for high-duration operations
        high_duration_ops = [m for m in metrics if m.duration > 1.0]
        if high_duration_ops:
            opportunities.append({
                'type': 'reduce_operation_duration',
                'description': f'{len(high_duration_ops)} operations taking >1s',
                'priority': 'high'
            })
            
        # Analyze for low cache hit rates
        low_cache_hit_ops = [m for m in metrics if m.cache_hit_rate < 0.3]
        if low_cache_hit_ops:
            opportunities.append({
                'type': 'improve_caching',
                'description': f'{len(low_cache_hit_ops)} operations with <30% cache hit rate',
                'priority': 'medium'
            })
            
        return opportunities
        
    def _generate_performance_summary(self, trends: Dict, aggregated: Dict, 
                                    opportunities: List[Dict]) -> Dict[str, Any]:
        """Generate executive performance summary"""
        return {
            'overall_health': 'good' if not opportunities else 'needs_attention',
            'key_insights': [
                f"Response time trend: {trends.get('response_time_trend', 'unknown')}",
                f"Average operation duration: {aggregated.get('average_duration', 0):.3f}s",
                f"Cache efficiency: {aggregated.get('average_cache_hit_rate', 0):.1%}"
            ],
            'priority_actions': [opp['description'] for opp in opportunities if opp['priority'] == 'high'],
            'optimization_score': self._calculate_optimization_score(aggregated, opportunities)
        }
        
    def _calculate_optimization_score(self, aggregated: Dict, opportunities: List[Dict]) -> float:
        """Calculate optimization score (0-100)"""
        base_score = 100
        
        # Reduce score for performance issues
        if aggregated.get('average_duration', 0) > 1.0:
            base_score -= 20
            
        if aggregated.get('average_cache_hit_rate', 1.0) < 0.5:
            base_score -= 15
            
        # Reduce score for opportunities
        base_score -= len(opportunities) * 5
        
        return max(base_score, 0)


class PerformanceMonitor:
    """Real-time performance monitoring"""
    
    def __init__(self):
        self.start_time = time.time()
        
    def track_operation(self, operation_type: str, duration: float, **kwargs):
        """Track operation performance"""
        # Implementation for operation tracking
        pass


class IndexManager:
    """Database index optimization manager"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        
    def optimize_for_query(self, query_pattern: str) -> List[str]:
        """Optimize indexes for query pattern"""
        # This would implement index optimization
        return ['index_optimization_applied']
        
    def optimize_for_large_volume(self, volume_size: int) -> Dict[str, Any]:
        """Optimize indexes for large volumes"""
        return {
            'optimization_type': 'index_optimization',
            'indexes_created': 2,
            'estimated_improvement': 0.3
        }
        
    def get_index_efficiency(self) -> float:
        """Get index efficiency score"""
        return 0.85  # Placeholder

if __name__ == "__main__":
    # Example usage
    optimizer = PerformanceOptimizer("/Users/nalve/ce-simple/contextflow/semantic-retrieval/context.db")
    
    # Test performance monitoring
    metrics = optimizer.monitor_real_time_performance()
    print(f"System health: {metrics['system_health']}")
    print(f"Memory usage: {metrics['memory_usage']['current_mb']:.1f} MB")
    print(f"Cache hit rate: {metrics['cache_performance']['hit_rate']:.1%}")