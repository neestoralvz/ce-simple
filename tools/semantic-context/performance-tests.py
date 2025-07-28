#!/usr/bin/env python3
"""
Performance Testing Suite for Semantic Context Retrieval System
Validates <100ms latency and >95% accuracy requirements based on 2025 research
Comprehensive benchmarking with real-world test scenarios
"""

import json
import time
import statistics
import random
import asyncio
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict
import logging
import threading
import concurrent.futures

# Import our semantic context components
from .retrieval_engine import ContextualRetrievalEngine, RetrievalQuery
from .embedding_manager import AdvancedEmbeddingManager, EmbeddingConfig
from .context_runtime import ContextEngineering, ContextStrategy, ContextItem, MemoryType
from .pattern_analyzer import ContextFlowPatternAnalyzer
from .compression_engine import SpliceCompressionEngine, CompressionConfig
from .integration_api import SemanticContextIntegrationAPI, IntegrationRequest, ContextRequestType, IntegrationMode

# Testing dependencies
try:
    import numpy as np
    from scipy.stats import pearsonr
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    logging.warning("SciPy not available for advanced statistical analysis")

try:
    import matplotlib.pyplot as plt
    import seaborn as sns
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    logging.warning("Matplotlib/Seaborn not available for visualization")

@dataclass
class PerformanceTarget:
    """Performance targets based on 2025 research requirements"""
    max_latency_ms: float = 100.0         # <100ms retrieval latency
    min_accuracy: float = 0.95            # >95% retrieval accuracy
    min_throughput_qps: float = 10.0      # Queries per second
    max_memory_mb: float = 500.0          # Memory usage limit
    min_compression_ratio: float = 0.6    # Compression efficiency
    min_preservation_score: float = 0.85  # Semantic preservation

@dataclass
class TestResult:
    """Individual test result"""
    test_name: str
    success: bool
    latency_ms: float
    accuracy_score: float
    throughput_qps: float
    memory_usage_mb: float
    metadata: Dict[str, Any]
    timestamp: str

@dataclass
class BenchmarkSuite:
    """Complete benchmark suite results"""
    suite_name: str
    total_tests: int
    passed_tests: int
    failed_tests: int
    average_latency: float
    average_accuracy: float
    average_throughput: float
    performance_targets: PerformanceTarget
    individual_results: List[TestResult]
    summary_metrics: Dict[str, Any]
    timestamp: str

class TestDataGenerator:
    """Generates realistic test data for benchmarking"""
    
    def __init__(self):
        self.command_templates = [
            "Create a new command for {task} with {complexity} complexity",
            "Implement {feature} using {technology} framework", 
            "Analyze {dataset} for {insights} patterns",
            "Debug {issue} in {component} system",
            "Optimize {process} for better {metric}",
            "Document {functionality} with examples and usage",
            "Test {implementation} against {requirements}",
            "Deploy {application} to {environment} infrastructure"
        ]
        
        self.context_types = [
            'command', 'user_voice', 'session', 'project_evolution',
            'documentation', 'implementation', 'analysis', 'testing'
        ]
        
        self.complexity_levels = ['simple', 'moderate', 'complex', 'advanced']
        self.technologies = ['Python', 'JavaScript', 'Docker', 'AWS', 'React', 'FastAPI']
        self.features = ['authentication', 'database', 'API', 'UI', 'analytics', 'monitoring']
        
        self.logger = logging.getLogger(__name__)
        
    def generate_test_contexts(self, count: int = 100) -> List[Dict[str, Any]]:
        """Generate realistic test contexts"""
        contexts = []
        
        for i in range(count):
            # Generate content based on templates
            template = random.choice(self.command_templates)
            content = template.format(
                task=random.choice(['data processing', 'user management', 'content analysis']),
                complexity=random.choice(self.complexity_levels),
                feature=random.choice(self.features),
                technology=random.choice(self.technologies),
                dataset='user behavior data',
                insights='performance',
                issue='memory leak',
                component='authentication',
                process='deployment pipeline',
                metric='response time',
                functionality='API endpoints',
                requirements='security standards',
                implementation='user interface',
                application='web service',
                environment='production'
            )
            
            # Add realistic details
            content += f"\n\nDetailed implementation notes:\n"
            content += f"- Primary objective: {random.choice(['performance', 'security', 'usability', 'scalability'])}\n"
            content += f"- Technical constraints: {random.choice(['memory limited', 'high throughput', 'real-time', 'batch processing'])}\n"
            content += f"- Success criteria: {random.choice(['90% accuracy', '<100ms latency', '99.9% uptime', 'zero data loss'])}\n"
            
            context = {
                'id': f'test_context_{i:04d}',
                'content': content,
                'context_type': random.choice(self.context_types),
                'session_id': f'session_{random.randint(1, 10)}',
                'timestamp': (datetime.now() - timedelta(hours=random.randint(0, 72))).isoformat(),
                'metadata': {
                    'complexity': random.choice(self.complexity_levels),
                    'priority': random.choice(['low', 'medium', 'high']),
                    'source': 'test_generator'
                }
            }
            contexts.append(context)
            
        self.logger.info(f"Generated {count} test contexts")
        return contexts
        
    def generate_test_queries(self, count: int = 50) -> List[str]:
        """Generate realistic test queries"""
        query_patterns = [
            "how to implement {feature}",
            "best practices for {technology}",
            "debug {issue} in production",
            "optimize {component} performance", 
            "create {task} automation",
            "analyze {data} patterns",
            "deploy {service} securely",
            "test {functionality} thoroughly"
        ]
        
        queries = []
        for i in range(count):
            pattern = random.choice(query_patterns)
            query = pattern.format(
                feature=random.choice(self.features),
                technology=random.choice(self.technologies),
                issue=random.choice(['memory leak', 'slow response', 'authentication failure']),
                component=random.choice(['database', 'API', 'frontend', 'cache']),
                task=random.choice(['deployment', 'monitoring', 'backup', 'scaling']),
                data=random.choice(['user behavior', 'system metrics', 'error logs']),
                service=random.choice(['web application', 'microservice', 'database']),
                functionality=random.choice(['user login', 'data export', 'file upload'])
            )
            queries.append(query)
            
        return queries

class AccuracyEvaluator:
    """Evaluates retrieval accuracy using multiple metrics"""
    
    def __init__(self):
        self.ground_truth = {}  # Will store expected results
        self.logger = logging.getLogger(__name__)
        
    def create_ground_truth(self, contexts: List[Dict[str, Any]], queries: List[str]) -> Dict[str, List[str]]:
        """Create ground truth mappings for accuracy evaluation"""
        ground_truth = {}
        
        for query in queries:
            # Simple relevance scoring based on keyword overlap
            relevant_contexts = []
            query_words = set(query.lower().split())
            
            for context in contexts:
                content_words = set(context['content'].lower().split())
                overlap = len(query_words.intersection(content_words))
                relevance_score = overlap / len(query_words) if query_words else 0
                
                # Consider relevant if significant overlap
                if relevance_score > 0.3:
                    relevant_contexts.append(context['id'])
                    
            ground_truth[query] = relevant_contexts[:10]  # Top 10 relevant
            
        self.ground_truth = ground_truth
        self.logger.info(f"Created ground truth for {len(queries)} queries")
        return ground_truth
        
    def evaluate_accuracy(self, query: str, retrieved_results: List[Dict[str, Any]]) -> float:
        """Evaluate accuracy using precision@k and recall"""
        if query not in self.ground_truth:
            return 0.5  # Neutral score for unknown queries
            
        expected_ids = set(self.ground_truth[query])
        retrieved_ids = set([r.get('id', r.get('context_id', '')) for r in retrieved_results])
        
        if not expected_ids:
            return 1.0 if not retrieved_ids else 0.0
            
        # Calculate precision and recall
        true_positives = len(expected_ids.intersection(retrieved_ids))
        precision = true_positives / len(retrieved_ids) if retrieved_ids else 0
        recall = true_positives / len(expected_ids) if expected_ids else 0
        
        # F1 score as accuracy metric
        if precision + recall > 0:
            f1_score = 2 * (precision * recall) / (precision + recall)
        else:
            f1_score = 0.0
            
        return f1_score

class LatencyBenchmark:
    """Benchmark latency performance across different scenarios"""
    
    def __init__(self, api: SemanticContextIntegrationAPI):
        self.api = api
        self.results = defaultdict(list)
        self.logger = logging.getLogger(__name__)
        
    def benchmark_retrieval_latency(self, queries: List[str], 
                                  session_id: str = "benchmark") -> Dict[str, float]:
        """Benchmark retrieval latency"""
        latencies = []
        
        for query in queries:
            request = IntegrationRequest(
                request_id=f"latency_test_{int(time.time())}_{random.randint(1000, 9999)}",
                request_type=ContextRequestType.RETRIEVE,
                mode=IntegrationMode.CONTEXT_QUERY,
                user_context=query,
                session_id=session_id,
                parameters={'max_contexts': 10}
            )
            
            start_time = time.time()
            try:
                if hasattr(self.api, 'process_request'):
                    # Async API
                    response = asyncio.run(self.api.process_request(request))
                else:
                    # Sync API
                    response = self.api.process_request(request)
                    
                latency_ms = (time.time() - start_time) * 1000
                latencies.append(latency_ms)
                
                self.results['retrieval_latencies'].append(latency_ms)
                
            except Exception as e:
                self.logger.error(f"Latency benchmark error: {e}")
                latencies.append(float('inf'))  # Mark as failed
                
        return {
            'average_latency': statistics.mean(latencies),
            'median_latency': statistics.median(latencies), 
            'p95_latency': np.percentile(latencies, 95) if SCIPY_AVAILABLE else max(latencies),
            'p99_latency': np.percentile(latencies, 99) if SCIPY_AVAILABLE else max(latencies),
            'min_latency': min(latencies),
            'max_latency': max(latencies)
        }
        
    def benchmark_concurrent_latency(self, queries: List[str], 
                                   concurrency: int = 5) -> Dict[str, float]:
        """Benchmark latency under concurrent load"""
        results = []
        
        def process_query(query):
            request = IntegrationRequest(
                request_id=f"concurrent_{int(time.time())}_{random.randint(1000, 9999)}",
                request_type=ContextRequestType.RETRIEVE,
                mode=IntegrationMode.CONTEXT_QUERY,
                user_context=query,
                session_id=f"concurrent_{threading.current_thread().ident}",
                parameters={'max_contexts': 10}
            )
            
            start_time = time.time()
            try:
                if hasattr(self.api, 'process_request'):
                    response = asyncio.run(self.api.process_request(request))
                else:
                    response = self.api.process_request(request)
                    
                return (time.time() - start_time) * 1000
            except Exception as e:
                self.logger.error(f"Concurrent benchmark error: {e}")
                return float('inf')
                
        # Execute concurrent requests
        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            future_to_query = {executor.submit(process_query, query): query 
                             for query in queries[:concurrency * 2]}  # 2x queries per thread
            
            for future in concurrent.futures.as_completed(future_to_query):
                try:
                    latency_ms = future.result()
                    results.append(latency_ms)
                except Exception as e:
                    self.logger.error(f"Concurrent execution error: {e}")
                    results.append(float('inf'))
                    
        valid_results = [r for r in results if r != float('inf')]
        
        if not valid_results:
            return {'error': 'All concurrent requests failed'}
            
        return {
            'concurrent_average': statistics.mean(valid_results),
            'concurrent_median': statistics.median(valid_results),
            'concurrent_p95': np.percentile(valid_results, 95) if SCIPY_AVAILABLE else max(valid_results),
            'success_rate': len(valid_results) / len(results),
            'total_requests': len(results)
        }

class ThroughputBenchmark:
    """Benchmark throughput performance"""
    
    def __init__(self, api: SemanticContextIntegrationAPI):
        self.api = api
        self.logger = logging.getLogger(__name__)
        
    def benchmark_throughput(self, queries: List[str], duration_seconds: int = 30) -> Dict[str, float]:
        """Benchmark queries per second throughput"""
        start_time = time.time()
        end_time = start_time + duration_seconds
        
        query_count = 0
        successful_queries = 0
        errors = 0
        
        while time.time() < end_time:
            query = random.choice(queries)
            
            request = IntegrationRequest(
                request_id=f"throughput_{int(time.time())}_{query_count}",
                request_type=ContextRequestType.RETRIEVE,
                mode=IntegrationMode.CONTEXT_QUERY,
                user_context=query,
                session_id="throughput_test",
                parameters={'max_contexts': 5}  # Smaller for faster processing
            )
            
            try:
                if hasattr(self.api, 'process_request'):
                    response = asyncio.run(self.api.process_request(request))
                else:
                    response = self.api.process_request(request)
                    
                if response.success:
                    successful_queries += 1
                else:
                    errors += 1
                    
            except Exception as e:
                errors += 1
                self.logger.warning(f"Throughput test error: {e}")
                
            query_count += 1
            
        actual_duration = time.time() - start_time
        
        return {
            'total_queries': query_count,
            'successful_queries': successful_queries,
            'failed_queries': errors,
            'queries_per_second': query_count / actual_duration,
            'successful_qps': successful_queries / actual_duration,
            'error_rate': errors / query_count if query_count > 0 else 0,
            'actual_duration': actual_duration
        }

class MemoryBenchmark:
    """Benchmark memory usage patterns"""
    
    def __init__(self):
        self.baseline_memory = 0
        self.peak_memory = 0
        self.logger = logging.getLogger(__name__)
        
    def get_memory_usage(self) -> float:
        """Get current memory usage in MB"""
        try:
            import psutil
            process = psutil.Process()
            return process.memory_info().rss / 1024 / 1024  # MB
        except ImportError:
            # Fallback using gc
            import gc
            import sys
            
            # Rough approximation
            total_size = 0
            for obj in gc.get_objects():
                try:
                    total_size += sys.getsizeof(obj)
                except (TypeError, AttributeError):
                    pass
                    
            return total_size / 1024 / 1024  # MB
            
    def benchmark_memory_usage(self, test_function: callable, *args, **kwargs) -> Dict[str, float]:
        """Benchmark memory usage during test execution"""
        # Record baseline
        self.baseline_memory = self.get_memory_usage()
        
        # Execute test
        start_memory = self.get_memory_usage()
        result = test_function(*args, **kwargs)
        end_memory = self.get_memory_usage()
        
        # Calculate peak memory during short monitoring period
        peak_samples = []
        for _ in range(10):
            peak_samples.append(self.get_memory_usage())
            time.sleep(0.1)
            
        self.peak_memory = max(peak_samples) if peak_samples else end_memory
        
        return {
            'baseline_memory_mb': self.baseline_memory,
            'start_memory_mb': start_memory,
            'end_memory_mb': end_memory,
            'peak_memory_mb': self.peak_memory,
            'memory_increase_mb': end_memory - start_memory,
            'peak_increase_mb': self.peak_memory - self.baseline_memory,
            'test_result': result
        }

class ComprehensivePerformanceTester:
    """Main performance testing orchestrator"""
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.results_path = self.base_path / "tools" / "semantic-context" / "performance_results"
        self.results_path.mkdir(exist_ok=True)
        
        # Initialize components
        self.api = SemanticContextIntegrationAPI(base_path)
        self.data_generator = TestDataGenerator()
        self.accuracy_evaluator = AccuracyEvaluator()
        self.latency_benchmark = LatencyBenchmark(self.api)
        self.throughput_benchmark = ThroughputBenchmark(self.api)
        self.memory_benchmark = MemoryBenchmark()
        
        # Performance targets
        self.targets = PerformanceTarget()
        
        # Results storage
        self.test_results = []
        self.suite_results = []
        
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)
        
    def run_full_benchmark_suite(self) -> BenchmarkSuite:
        """Run complete benchmark suite"""
        suite_start = time.time()
        self.logger.info("Starting comprehensive performance benchmark suite")
        
        # Generate test data
        test_contexts = self.data_generator.generate_test_contexts(200)
        test_queries = self.data_generator.generate_test_queries(100)
        
        # Create ground truth for accuracy evaluation
        self.accuracy_evaluator.create_ground_truth(test_contexts, test_queries)
        
        # Ingest test contexts
        self.logger.info("Ingesting test contexts...")
        self._ingest_test_contexts(test_contexts)
        
        # Run individual benchmarks
        benchmark_results = {}
        
        # 1. Latency Benchmarks
        self.logger.info("Running latency benchmarks...")
        benchmark_results['latency'] = self._run_latency_benchmarks(test_queries)
        
        # 2. Accuracy Benchmarks  
        self.logger.info("Running accuracy benchmarks...")
        benchmark_results['accuracy'] = self._run_accuracy_benchmarks(test_queries)
        
        # 3. Throughput Benchmarks
        self.logger.info("Running throughput benchmarks...")
        benchmark_results['throughput'] = self._run_throughput_benchmarks(test_queries)
        
        # 4. Memory Benchmarks
        self.logger.info("Running memory benchmarks...")
        benchmark_results['memory'] = self._run_memory_benchmarks(test_queries)
        
        # 5. Component-Specific Benchmarks
        self.logger.info("Running component benchmarks...")
        benchmark_results['components'] = self._run_component_benchmarks(test_contexts)
        
        # Analyze results
        suite_results = self._analyze_suite_results(benchmark_results)
        
        # Generate report
        suite_duration = time.time() - suite_start
        
        suite = BenchmarkSuite(
            suite_name="Comprehensive Performance Benchmark",
            total_tests=len(self.test_results),
            passed_tests=len([r for r in self.test_results if r.success]),
            failed_tests=len([r for r in self.test_results if not r.success]),
            average_latency=suite_results.get('average_latency', 0),
            average_accuracy=suite_results.get('average_accuracy', 0),
            average_throughput=suite_results.get('average_throughput', 0),
            performance_targets=self.targets,
            individual_results=self.test_results,
            summary_metrics=suite_results,
            timestamp=datetime.now().isoformat()
        )
        
        # Save results
        self._save_results(suite)
        
        # Generate visualizations if available
        if PLOTTING_AVAILABLE:
            self._generate_visualizations(suite)
            
        self.logger.info(f"Benchmark suite completed in {suite_duration:.2f}s")
        self.logger.info(f"Results: {suite.passed_tests}/{suite.total_tests} tests passed")
        
        return suite
        
    def _ingest_test_contexts(self, contexts: List[Dict[str, Any]]):
        """Ingest test contexts into the system"""
        for context in contexts:
            request = IntegrationRequest(
                request_id=f"ingest_{context['id']}",
                request_type=ContextRequestType.INGEST,
                mode=IntegrationMode.BULK_PROCESS,
                user_context=context['content'],
                session_id=context['session_id'],
                parameters={'content_type': context['context_type']}
            )
            
            try:
                if hasattr(self.api, 'process_request'):
                    response = asyncio.run(self.api.process_request(request))
                else:
                    response = self.api.process_request(request)
                    
                if not response.success:
                    self.logger.warning(f"Failed to ingest context {context['id']}")
                    
            except Exception as e:
                self.logger.error(f"Ingestion error for {context['id']}: {e}")
                
    def _run_latency_benchmarks(self, queries: List[str]) -> Dict[str, Any]:
        """Run latency benchmark tests"""
        results = {}
        
        # Single-threaded latency
        single_thread_results = self.latency_benchmark.benchmark_retrieval_latency(queries[:20])
        results['single_thread'] = single_thread_results
        
        # Record individual test results
        avg_latency = single_thread_results.get('average_latency', float('inf'))
        passed = avg_latency <= self.targets.max_latency_ms
        
        test_result = TestResult(
            test_name="Single Thread Latency",
            success=passed,
            latency_ms=avg_latency,
            accuracy_score=0.0,  # Not applicable
            throughput_qps=0.0,  # Not applicable
            memory_usage_mb=self.memory_benchmark.get_memory_usage(),
            metadata=single_thread_results,
            timestamp=datetime.now().isoformat()
        )
        self.test_results.append(test_result)
        
        # Concurrent latency
        concurrent_results = self.latency_benchmark.benchmark_concurrent_latency(queries[:10], concurrency=3)
        results['concurrent'] = concurrent_results
        
        concurrent_avg = concurrent_results.get('concurrent_average', float('inf'))
        concurrent_passed = concurrent_avg <= self.targets.max_latency_ms * 1.5  # Allow 50% degradation
        
        test_result = TestResult(
            test_name="Concurrent Latency",
            success=concurrent_passed,
            latency_ms=concurrent_avg,
            accuracy_score=concurrent_results.get('success_rate', 0.0),
            throughput_qps=0.0,
            memory_usage_mb=self.memory_benchmark.get_memory_usage(),
            metadata=concurrent_results,
            timestamp=datetime.now().isoformat()
        )
        self.test_results.append(test_result)
        
        return results
        
    def _run_accuracy_benchmarks(self, queries: List[str]) -> Dict[str, Any]:
        """Run accuracy benchmark tests"""
        results = {}
        accuracy_scores = []
        
        for query in queries[:25]:  # Test subset for performance
            request = IntegrationRequest(
                request_id=f"accuracy_{int(time.time())}_{hash(query)}",
                request_type=ContextRequestType.RETRIEVE,
                mode=IntegrationMode.CONTEXT_QUERY,
                user_context=query,
                session_id="accuracy_test",
                parameters={'max_contexts': 10}
            )
            
            try:
                if hasattr(self.api, 'process_request'):
                    response = asyncio.run(self.api.process_request(request))
                else:
                    response = self.api.process_request(request)
                    
                if response.success and response.data:
                    retrieved_contexts = response.data.get('contexts', [])
                    accuracy = self.accuracy_evaluator.evaluate_accuracy(query, retrieved_contexts)
                    accuracy_scores.append(accuracy)
                else:
                    accuracy_scores.append(0.0)
                    
            except Exception as e:
                self.logger.error(f"Accuracy test error for query '{query}': {e}")
                accuracy_scores.append(0.0)
                
        avg_accuracy = statistics.mean(accuracy_scores) if accuracy_scores else 0.0
        results['average_accuracy'] = avg_accuracy
        results['accuracy_distribution'] = {
            'min': min(accuracy_scores) if accuracy_scores else 0.0,
            'max': max(accuracy_scores) if accuracy_scores else 0.0,
            'median': statistics.median(accuracy_scores) if accuracy_scores else 0.0,
            'std_dev': statistics.stdev(accuracy_scores) if len(accuracy_scores) > 1 else 0.0
        }
        
        # Record test result
        passed = avg_accuracy >= self.targets.min_accuracy
        test_result = TestResult(
            test_name="Retrieval Accuracy",
            success=passed,
            latency_ms=0.0,  # Not applicable
            accuracy_score=avg_accuracy,
            throughput_qps=0.0,
            memory_usage_mb=self.memory_benchmark.get_memory_usage(),
            metadata=results,
            timestamp=datetime.now().isoformat()
        )
        self.test_results.append(test_result)
        
        return results
        
    def _run_throughput_benchmarks(self, queries: List[str]) -> Dict[str, Any]:
        """Run throughput benchmark tests"""
        results = {}
        
        # Standard throughput test
        throughput_results = self.throughput_benchmark.benchmark_throughput(queries, duration_seconds=15)
        results['standard'] = throughput_results
        
        # Record test result
        qps = throughput_results.get('successful_qps', 0.0)
        passed = qps >= self.targets.min_throughput_qps
        
        test_result = TestResult(
            test_name="Throughput Performance",
            success=passed,
            latency_ms=0.0,
            accuracy_score=1.0 - throughput_results.get('error_rate', 0.0),
            throughput_qps=qps,
            memory_usage_mb=self.memory_benchmark.get_memory_usage(),
            metadata=throughput_results,
            timestamp=datetime.now().isoformat()
        )
        self.test_results.append(test_result)
        
        return results
        
    def _run_memory_benchmarks(self, queries: List[str]) -> Dict[str, Any]:
        """Run memory usage benchmark tests"""
        results = {}
        
        # Memory usage during retrieval
        def retrieval_test():
            query = random.choice(queries)
            request = IntegrationRequest(
                request_id=f"memory_test_{int(time.time())}",
                request_type=ContextRequestType.RETRIEVE,
                mode=IntegrationMode.CONTEXT_QUERY,
                user_context=query,
                session_id="memory_test",
                parameters={'max_contexts': 20}
            )
            
            if hasattr(self.api, 'process_request'):
                return asyncio.run(self.api.process_request(request))
            else:
                return self.api.process_request(request)
                
        memory_results = self.memory_benchmark.benchmark_memory_usage(retrieval_test)
        results['retrieval_memory'] = memory_results
        
        # Record test result
        peak_memory = memory_results.get('peak_memory_mb', float('inf'))
        passed = peak_memory <= self.targets.max_memory_mb
        
        test_result = TestResult(
            test_name="Memory Usage",
            success=passed,
            latency_ms=0.0,
            accuracy_score=0.0,
            throughput_qps=0.0,
            memory_usage_mb=peak_memory,
            metadata=memory_results,
            timestamp=datetime.now().isoformat()
        )
        self.test_results.append(test_result)
        
        return results
        
    def _run_component_benchmarks(self, contexts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Run component-specific benchmarks"""
        results = {}
        
        # Compression benchmark
        test_content = "\n\n".join([ctx['content'] for ctx in contexts[:5]])
        
        start_time = time.time()
        compression_result = self.api.compression_engine.compress_content(test_content)
        compression_time = (time.time() - start_time) * 1000
        
        results['compression'] = {
            'processing_time_ms': compression_time,
            'compression_ratio': compression_result.compression_ratio,
            'semantic_preservation': compression_result.semantic_preservation,
            'quality_metrics': compression_result.quality_metrics
        }
        
        # Record compression test
        compression_passed = (
            compression_result.compression_ratio >= self.targets.min_compression_ratio and
            compression_result.semantic_preservation >= self.targets.min_preservation_score
        )
        
        test_result = TestResult(
            test_name="Compression Performance",
            success=compression_passed,
            latency_ms=compression_time,
            accuracy_score=compression_result.semantic_preservation,
            throughput_qps=0.0,
            memory_usage_mb=self.memory_benchmark.get_memory_usage(),
            metadata=results['compression'],
            timestamp=datetime.now().isoformat()
        )
        self.test_results.append(test_result)
        
        return results
        
    def _analyze_suite_results(self, benchmark_results: Dict[str, Any]) -> Dict[str, Any]:
        """Analyze overall suite results"""
        analysis = {}
        
        # Calculate averages
        latency_results = benchmark_results.get('latency', {})
        analysis['average_latency'] = latency_results.get('single_thread', {}).get('average_latency', 0)
        
        accuracy_results = benchmark_results.get('accuracy', {})
        analysis['average_accuracy'] = accuracy_results.get('average_accuracy', 0)
        
        throughput_results = benchmark_results.get('throughput', {})
        analysis['average_throughput'] = throughput_results.get('standard', {}).get('successful_qps', 0)
        
        # Performance target compliance
        analysis['targets_met'] = {
            'latency': analysis['average_latency'] <= self.targets.max_latency_ms,
            'accuracy': analysis['average_accuracy'] >= self.targets.min_accuracy,
            'throughput': analysis['average_throughput'] >= self.targets.min_throughput_qps
        }
        
        analysis['overall_score'] = sum(analysis['targets_met'].values()) / len(analysis['targets_met'])
        
        return analysis
        
    def _save_results(self, suite: BenchmarkSuite):
        """Save benchmark results to file"""
        results_file = self.results_path / f"benchmark_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(results_file, 'w') as f:
            json.dump(asdict(suite), f, indent=2, default=str)
            
        self.logger.info(f"Results saved to {results_file}")
        
    def _generate_visualizations(self, suite: BenchmarkSuite):
        """Generate performance visualization charts"""
        try:
            # Latency distribution
            latencies = [r.latency_ms for r in suite.individual_results if r.latency_ms > 0]
            
            if latencies:
                plt.figure(figsize=(12, 8))
                
                plt.subplot(2, 2, 1)
                plt.hist(latencies, bins=20, alpha=0.7, color='blue')
                plt.axvline(self.targets.max_latency_ms, color='red', linestyle='--', label='Target')
                plt.xlabel('Latency (ms)')
                plt.ylabel('Frequency')
                plt.title('Latency Distribution')
                plt.legend()
                
                # Accuracy distribution
                accuracies = [r.accuracy_score for r in suite.individual_results if r.accuracy_score > 0]
                
                plt.subplot(2, 2, 2)
                plt.hist(accuracies, bins=20, alpha=0.7, color='green')
                plt.axvline(self.targets.min_accuracy, color='red', linestyle='--', label='Target')
                plt.xlabel('Accuracy Score')
                plt.ylabel('Frequency')
                plt.title('Accuracy Distribution')
                plt.legend()
                
                # Performance over time
                timestamps = [datetime.fromisoformat(r.timestamp) for r in suite.individual_results]
                
                plt.subplot(2, 2, 3)
                plt.plot(timestamps[:len(latencies)], latencies, 'o-', alpha=0.7)
                plt.xlabel('Time')
                plt.ylabel('Latency (ms)')
                plt.title('Latency Over Time')
                plt.xticks(rotation=45)
                
                # Memory usage
                memory_usage = [r.memory_usage_mb for r in suite.individual_results if r.memory_usage_mb > 0]
                
                plt.subplot(2, 2, 4)
                plt.plot(timestamps[:len(memory_usage)], memory_usage, 's-', alpha=0.7, color='orange')
                plt.axhline(self.targets.max_memory_mb, color='red', linestyle='--', label='Target')
                plt.xlabel('Time')
                plt.ylabel('Memory Usage (MB)')
                plt.title('Memory Usage Over Time')
                plt.xticks(rotation=45)
                plt.legend()
                
                plt.tight_layout()
                
                viz_file = self.results_path / f"benchmark_visualizations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                plt.savefig(viz_file, dpi=300, bbox_inches='tight')
                plt.close()
                
                self.logger.info(f"Visualizations saved to {viz_file}")
                
        except Exception as e:
            self.logger.error(f"Visualization generation failed: {e}")

if __name__ == "__main__":
    # Run comprehensive performance test
    tester = ComprehensivePerformanceTester()
    
    print("Starting comprehensive performance benchmark...")
    print("This may take several minutes to complete.")
    
    suite_results = tester.run_full_benchmark_suite()
    
    print("\n" + "="*80)
    print("PERFORMANCE BENCHMARK RESULTS")
    print("="*80)
    
    print(f"Suite: {suite_results.suite_name}")
    print(f"Total Tests: {suite_results.total_tests}")
    print(f"Passed: {suite_results.passed_tests}")
    print(f"Failed: {suite_results.failed_tests}")
    print(f"Success Rate: {(suite_results.passed_tests/suite_results.total_tests)*100:.1f}%")
    
    print(f"\nPerformance Metrics:")
    print(f"Average Latency: {suite_results.average_latency:.2f}ms (Target: <{tester.targets.max_latency_ms}ms)")
    print(f"Average Accuracy: {suite_results.average_accuracy:.3f} (Target: >{tester.targets.min_accuracy})")
    print(f"Average Throughput: {suite_results.average_throughput:.2f}qps (Target: >{tester.targets.min_throughput_qps}qps)")
    
    print(f"\nTarget Compliance:")
    targets_met = suite_results.summary_metrics.get('targets_met', {})
    for target, met in targets_met.items():
        status = "✓ PASS" if met else "✗ FAIL"
        print(f"  {target.upper()}: {status}")
        
    overall_score = suite_results.summary_metrics.get('overall_score', 0)
    print(f"\nOverall Score: {overall_score*100:.1f}%")
    
    if overall_score >= 0.8:
        print("🎉 EXCELLENT: System meets 2025 research-backed performance requirements!")
    elif overall_score >= 0.6:
        print("✅ GOOD: System meets most performance requirements with minor optimizations needed.")
    else:
        print("⚠️  NEEDS IMPROVEMENT: System requires optimization to meet performance targets.")
        
    print(f"\nDetailed results saved to: {tester.results_path}")
    print("="*80)