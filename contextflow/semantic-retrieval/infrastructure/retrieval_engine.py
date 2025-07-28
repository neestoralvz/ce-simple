#!/usr/bin/env python3
"""
Semantic Retrieval Engine - Technical Infrastructure Core
Implements fast retrieval, similarity matching, relevance scoring, and command ecosystem integration
"""

import json
import logging
import sqlite3
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Union
from dataclasses import dataclass, asdict
from pathlib import Path
import threading
import time
import pickle
import hashlib

# Import our custom components
import sys
sys.path.append(str(Path(__file__).parent.parent))

from backend.context_indexer import SemanticContextIndexer, ContextItem
from algorithms.context_correlator import ContextCorrelator, ContextCorrelation

@dataclass
class RetrievalQuery:
    """Structured query for context retrieval"""
    query_text: str
    query_type: str  # 'command', 'intent', 'semantic', 'temporal'
    filters: Dict[str, Any]
    max_results: int = 20
    min_relevance: float = 0.1
    session_id: Optional[str] = None
    include_cross_session: bool = True
    relevance_weights: Optional[Dict[str, float]] = None

@dataclass
class RetrievalResult:
    """Result from context retrieval"""
    context_item: ContextItem
    relevance_score: float
    correlation_metadata: Dict[str, Any]
    retrieval_timestamp: str
    query_id: str

class SemanticRetrievalEngine:
    """
    Production-ready semantic retrieval engine
    High-performance context retrieval with intelligent scoring
    """
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.retrieval_path = self.base_path / "contextflow" / "semantic-retrieval"
        self.context_db_path = self.retrieval_path / "context.db"
        
        # Initialize core components
        self.indexer = SemanticContextIndexer(str(self.base_path))
        self.correlator = ContextCorrelator(str(self.context_db_path))
        
        # Performance caching
        self.result_cache = {}
        self.cache_ttl = 300  # 5 minutes
        self.cache_lock = threading.Lock()
        
        # Query performance tracking
        self.query_stats = {
            'total_queries': 0,
            'average_response_time': 0.0,
            'cache_hit_rate': 0.0,
            'last_updated': datetime.now().isoformat()
        }
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Default relevance weights
        self.default_weights = {
            'semantic': 0.35,
            'temporal': 0.25,
            'structural': 0.20,
            'intentional': 0.20
        }
        
        # Command ecosystem integration patterns
        self.command_patterns = {
            'start': {'context_types': ['session', 'project_evolution'], 'priority': 'high'},
            'create-doc': {'context_types': ['command', 'user_voice'], 'priority': 'high'},
            'analyze': {'context_types': ['all'], 'priority': 'medium'},
            'implement': {'context_types': ['command', 'session'], 'priority': 'high'},
            'debug': {'context_types': ['session', 'project_evolution'], 'priority': 'high'},
            'explore': {'context_types': ['all'], 'priority': 'medium'}
        }
        
    def retrieve_context(self, query: RetrievalQuery) -> List[RetrievalResult]:
        """
        Main context retrieval method
        Returns ranked, relevant context based on query
        """
        start_time = time.time()
        query_id = self._generate_query_id(query)
        
        # Check cache first
        if self._should_use_cache(query):
            cached_result = self._get_cached_result(query_id)
            if cached_result:
                self._update_query_stats(time.time() - start_time, cache_hit=True)
                return cached_result
                
        try:
            # Execute retrieval pipeline
            results = self._execute_retrieval_pipeline(query, query_id)
            
            # Cache results
            self._cache_results(query_id, results)
            
            # Update performance stats
            self._update_query_stats(time.time() - start_time, cache_hit=False)
            
            self.logger.info(f"Retrieved {len(results)} results for query: {query.query_text[:50]}...")
            return results
            
        except Exception as e:
            self.logger.error(f"Error in context retrieval: {e}")
            return []
            
    def retrieve_for_command(self, command_name: str, context: str, 
                           session_id: Optional[str] = None) -> List[RetrievalResult]:
        """
        Specialized retrieval for command ecosystem integration
        Optimized for specific command patterns
        """
        command_config = self.command_patterns.get(command_name, {})
        
        # Build optimized query
        query = RetrievalQuery(
            query_text=context,
            query_type='command',
            filters={
                'context_types': command_config.get('context_types', ['all']),
                'priority': command_config.get('priority', 'medium')
            },
            max_results=15,
            min_relevance=0.2,
            session_id=session_id,
            include_cross_session=True
        )
        
        results = self.retrieve_context(query)
        
        # Post-process for command-specific needs
        if command_name == 'start':
            results = self._prioritize_for_session_start(results)
        elif command_name == 'create-doc':
            results = self._prioritize_for_document_creation(results)
        elif command_name == 'debug':
            results = self._prioritize_for_debugging(results)
            
        return results
        
    def get_contextual_suggestions(self, current_context: str, 
                                 context_type: str = 'general') -> List[Dict[str, Any]]:
        """
        Get contextual suggestions based on current work
        Enables intelligent context-aware assistance
        """
        query = RetrievalQuery(
            query_text=current_context,
            query_type='semantic',
            filters={'context_type': context_type},
            max_results=10,
            min_relevance=0.3
        )
        
        results = self.retrieve_context(query)
        
        # Generate actionable suggestions
        suggestions = []
        for result in results:
            suggestion = self._generate_contextual_suggestion(result)
            if suggestion:
                suggestions.append(suggestion)
                
        return suggestions
        
    def analyze_context_patterns(self, session_id: Optional[str] = None,
                               time_range_days: int = 30) -> Dict[str, Any]:
        """
        Analyze patterns in context usage and retrieval
        Provides insights for system optimization
        """
        end_date = datetime.now()
        start_date = end_date - timedelta(days=time_range_days)
        
        with sqlite3.connect(self.context_db_path) as conn:
            # Query context items in range
            cursor = conn.execute('''
                SELECT context_type, COUNT(*) as count,
                       AVG(relevance_score) as avg_relevance,
                       MAX(timestamp) as latest_usage
                FROM context_items 
                WHERE timestamp >= ? AND timestamp <= ?
                AND (session_id = ? OR ? IS NULL)
                GROUP BY context_type
            ''', (start_date.isoformat(), end_date.isoformat(), session_id, session_id))
            
            type_stats = {}
            for row in cursor.fetchall():
                type_stats[row[0]] = {
                    'count': row[1],
                    'avg_relevance': row[2],
                    'latest_usage': row[3]
                }
                
        # Analyze query patterns
        query_patterns = self._analyze_query_patterns()
        
        # Generate insights
        insights = self._generate_pattern_insights(type_stats, query_patterns)
        
        return {
            'type_statistics': type_stats,
            'query_patterns': query_patterns,
            'insights': insights,
            'performance_stats': self.query_stats,
            'analysis_timestamp': datetime.now().isoformat()
        }
        
    def optimize_context_scoring(self, feedback_data: List[Dict[str, Any]]) -> Dict[str, float]:
        """
        Optimize relevance scoring based on user feedback
        Implements learning from usage patterns
        """
        # Analyze feedback patterns
        successful_retrievals = [f for f in feedback_data if f.get('rating', 0) >= 4]
        failed_retrievals = [f for f in feedback_data if f.get('rating', 0) <= 2]
        
        # Calculate optimal weights
        optimized_weights = self.default_weights.copy()
        
        if successful_retrievals:
            # Analyze what made successful retrievals work
            success_factors = self._analyze_success_factors(successful_retrievals)
            
            # Adjust weights based on success patterns
            for factor, impact in success_factors.items():
                if factor in optimized_weights:
                    optimized_weights[factor] = min(optimized_weights[factor] * (1 + impact), 1.0)
                    
        # Normalize weights
        total_weight = sum(optimized_weights.values())
        optimized_weights = {k: v / total_weight for k, v in optimized_weights.items()}
        
        self.logger.info(f"Optimized scoring weights: {optimized_weights}")
        return optimized_weights
        
    def export_context_for_handoff(self, session_id: str, 
                                 include_correlations: bool = True) -> Dict[str, Any]:
        """
        Export context data for session handoffs
        Enables seamless session continuity
        """
        with sqlite3.connect(self.context_db_path) as conn:
            # Get session context
            cursor = conn.execute('''
                SELECT * FROM context_items 
                WHERE session_id = ?
                ORDER BY timestamp DESC
            ''', (session_id,))
            
            session_context = [dict(zip([col[0] for col in cursor.description], row))
                             for row in cursor.fetchall()]
                             
        # Get correlations if requested
        correlations = []
        if include_correlations and session_context:
            correlations = self.correlator.generate_context_correlations(session_context)
            
        # Generate handoff summary
        summary = self._generate_handoff_summary(session_context, correlations)
        
        return {
            'session_id': session_id,
            'context_items': session_context,
            'correlations': [asdict(c) for c in correlations],
            'summary': summary,
            'export_timestamp': datetime.now().isoformat(),
            'total_items': len(session_context)
        }
        
    def import_context_from_handoff(self, handoff_data: Dict[str, Any]) -> bool:
        """
        Import context data from session handoff
        Enables context restoration across sessions
        """
        try:
            context_items = handoff_data.get('context_items', [])
            
            # Import context items
            imported_count = 0
            for item_data in context_items:
                # Convert to ContextItem if needed
                if isinstance(item_data, dict):
                    context_item = ContextItem(**item_data)
                else:
                    context_item = item_data
                    
                # Store in database
                self.indexer._store_context_item(context_item)
                imported_count += 1
                
            self.logger.info(f"Imported {imported_count} context items from handoff")
            return True
            
        except Exception as e:
            self.logger.error(f"Error importing handoff data: {e}")
            return False
            
    # Private implementation methods
    def _execute_retrieval_pipeline(self, query: RetrievalQuery, query_id: str) -> List[RetrievalResult]:
        """Execute the full retrieval pipeline"""
        # Step 1: Get candidate context items
        candidates = self._get_candidate_items(query)
        
        # Step 2: Apply filters
        filtered_candidates = self._apply_filters(candidates, query.filters)
        
        # Step 3: Calculate relevance scores
        scored_candidates = self._calculate_relevance_scores(filtered_candidates, query)
        
        # Step 4: Apply cross-session context if enabled
        if query.include_cross_session:
            cross_session_items = self.correlator.bridge_cross_conversation_context(
                query.session_id or '', query.query_text
            )
            scored_candidates.extend(self._score_cross_session_items(cross_session_items, query))
            
        # Step 5: Sort and limit results
        scored_candidates.sort(key=lambda x: x[1], reverse=True)
        top_candidates = scored_candidates[:query.max_results]
        
        # Step 6: Convert to RetrievalResult objects
        results = []
        for item, score in top_candidates:
            if score >= query.min_relevance:
                result = RetrievalResult(
                    context_item=ContextItem(**item) if isinstance(item, dict) else item,
                    relevance_score=score,
                    correlation_metadata=self._get_correlation_metadata(item, query),
                    retrieval_timestamp=datetime.now().isoformat(),
                    query_id=query_id
                )
                results.append(result)
                
        return results
        
    def _get_candidate_items(self, query: RetrievalQuery) -> List[Dict]:
        """Get candidate context items for query"""
        with sqlite3.connect(self.context_db_path) as conn:
            # Build SQL query based on query type
            if query.query_type == 'temporal':
                cursor = conn.execute('''
                    SELECT * FROM context_items 
                    ORDER BY timestamp DESC
                    LIMIT 100
                ''')
            elif query.query_type == 'command':
                cursor = conn.execute('''
                    SELECT * FROM context_items 
                    WHERE context_type = 'command'
                    ORDER BY relevance_score DESC
                    LIMIT 100
                ''')
            else:
                # Semantic/general query
                cursor = conn.execute('''
                    SELECT * FROM context_items 
                    ORDER BY relevance_score DESC, timestamp DESC
                    LIMIT 200
                ''')
                
            candidates = [dict(zip([col[0] for col in cursor.description], row))
                         for row in cursor.fetchall()]
                         
        return candidates
        
    def _apply_filters(self, candidates: List[Dict], filters: Dict[str, Any]) -> List[Dict]:
        """Apply filters to candidate items"""
        if not filters:
            return candidates
            
        filtered = []
        for item in candidates:
            passes_filters = True
            
            # Context type filter
            if 'context_types' in filters:
                allowed_types = filters['context_types']
                if allowed_types != ['all'] and item.get('context_type') not in allowed_types:
                    passes_filters = False
                    
            # Session filter
            if 'session_id' in filters:
                if item.get('session_id') != filters['session_id']:
                    passes_filters = False
                    
            # Timestamp filter
            if 'after_timestamp' in filters:
                if item.get('timestamp', '') < filters['after_timestamp']:
                    passes_filters = False
                    
            if passes_filters:
                filtered.append(item)
                
        return filtered
        
    def _calculate_relevance_scores(self, items: List[Dict], query: RetrievalQuery) -> List[Tuple[Dict, float]]:
        """Calculate relevance scores for items"""
        scored_items = []
        
        for item in items:
            # Use correlator for intelligent scoring
            relevance = self.correlator._calculate_intent_relevance(
                query.query_text, item, 
                self.correlator._detect_intent(query.query_text)
            )
            
            # Apply query-specific weight adjustments
            if query.relevance_weights:
                relevance = self._apply_weight_adjustments(relevance, query.relevance_weights)
                
            scored_items.append((item, relevance))
            
        return scored_items
        
    def _score_cross_session_items(self, items: List[Dict], query: RetrievalQuery) -> List[Tuple[Dict, float]]:
        """Score cross-session context items"""
        scored_items = []
        
        for item in items:
            # Cross-session items have slightly reduced relevance
            base_score = item.get('cross_session_similarity', 0.5)
            adjusted_score = base_score * 0.8  # Cross-session penalty
            
            scored_items.append((item, adjusted_score))
            
        return scored_items
        
    def _generate_query_id(self, query: RetrievalQuery) -> str:
        """Generate unique query ID for caching"""
        query_string = f"{query.query_text}:{query.query_type}:{str(query.filters)}"
        return hashlib.md5(query_string.encode()).hexdigest()
        
    def _should_use_cache(self, query: RetrievalQuery) -> bool:
        """Determine if query should use cache"""
        # Cache for semantic and general queries, not for temporal
        return query.query_type in ['semantic', 'command', 'intent']
        
    def _get_cached_result(self, query_id: str) -> Optional[List[RetrievalResult]]:
        """Get cached result if available and fresh"""
        with self.cache_lock:
            if query_id in self.result_cache:
                cached_data, timestamp = self.result_cache[query_id]
                if time.time() - timestamp < self.cache_ttl:
                    return cached_data
                else:
                    del self.result_cache[query_id]
        return None
        
    def _cache_results(self, query_id: str, results: List[RetrievalResult]):
        """Cache retrieval results"""
        with self.cache_lock:
            self.result_cache[query_id] = (results, time.time())
            
            # Cleanup old cache entries
            current_time = time.time()
            expired_keys = [k for k, (_, timestamp) in self.result_cache.items() 
                          if current_time - timestamp > self.cache_ttl]
            for key in expired_keys:
                del self.result_cache[key]
                
    def _update_query_stats(self, response_time: float, cache_hit: bool):
        """Update query performance statistics"""
        self.query_stats['total_queries'] += 1
        
        # Update average response time
        total_queries = self.query_stats['total_queries']
        current_avg = self.query_stats['average_response_time']
        self.query_stats['average_response_time'] = (
            (current_avg * (total_queries - 1) + response_time) / total_queries
        )
        
        # Update cache hit rate
        if cache_hit:
            # Simple approximation - could be more sophisticated
            current_rate = self.query_stats['cache_hit_rate']
            self.query_stats['cache_hit_rate'] = (
                (current_rate * (total_queries - 1) + 1.0) / total_queries
            )
        else:
            current_rate = self.query_stats['cache_hit_rate']
            self.query_stats['cache_hit_rate'] = (
                (current_rate * (total_queries - 1)) / total_queries
            )
            
        self.query_stats['last_updated'] = datetime.now().isoformat()
        
    def _prioritize_for_session_start(self, results: List[RetrievalResult]) -> List[RetrievalResult]:
        """Prioritize results for session start command"""
        # Boost recent session data and project evolution
        for result in results:
            if result.context_item.context_type in ['session', 'project_evolution']:
                result.relevance_score *= 1.2
                
        results.sort(key=lambda r: r.relevance_score, reverse=True)
        return results
        
    def _prioritize_for_document_creation(self, results: List[RetrievalResult]) -> List[RetrievalResult]:
        """Prioritize results for document creation"""
        # Boost user voice and command patterns
        for result in results:
            if result.context_item.context_type in ['user_voice', 'command']:
                result.relevance_score *= 1.3
                
        results.sort(key=lambda r: r.relevance_score, reverse=True)
        return results
        
    def _prioritize_for_debugging(self, results: List[RetrievalResult]) -> List[RetrievalResult]:
        """Prioritize results for debugging"""
        # Boost session data and recent issues
        for result in results:
            if result.context_item.context_type == 'session':
                result.relevance_score *= 1.4
                
        results.sort(key=lambda r: r.relevance_score, reverse=True)
        return results
        
    def _get_correlation_metadata(self, item: Dict, query: RetrievalQuery) -> Dict[str, Any]:
        """Get correlation metadata for item"""
        return {
            'query_type': query.query_type,
            'item_type': item.get('context_type'),
            'temporal_distance': self._calculate_temporal_distance(item.get('timestamp')),
            'session_match': item.get('session_id') == query.session_id
        }
        
    def _calculate_temporal_distance(self, timestamp: str) -> float:
        """Calculate temporal distance from now"""
        try:
            item_time = datetime.fromisoformat(timestamp)
            current_time = datetime.now()
            time_diff = (current_time - item_time).total_seconds()
            return time_diff / (24 * 3600)  # Days
        except:
            return 999.0  # Very old
            
    def _apply_weight_adjustments(self, base_score: float, weights: Dict[str, float]) -> float:
        """Apply custom weight adjustments to relevance score"""
        # This is a simplified version - could be more sophisticated
        adjustment_factor = sum(weights.values()) / len(weights)
        return base_score * adjustment_factor
        
    def _generate_contextual_suggestion(self, result: RetrievalResult) -> Optional[Dict[str, Any]]:
        """Generate actionable suggestion from retrieval result"""
        item = result.context_item
        
        if item.context_type == 'command':
            return {
                'type': 'command_suggestion',
                'action': f"Consider using command pattern from {item.command_context}",
                'relevance': result.relevance_score,
                'context': item.content[:200]
            }
        elif item.context_type == 'user_voice':
            return {
                'type': 'voice_reference',
                'action': "Reference user preference patterns",
                'relevance': result.relevance_score,
                'context': item.content[:200]
            }
            
        return None
        
    def _analyze_query_patterns(self) -> Dict[str, Any]:
        """Analyze patterns in query usage"""
        # This would analyze actual query logs - simplified for now
        return {
            'most_common_types': ['semantic', 'command', 'temporal'],
            'average_results_returned': 8.5,
            'peak_usage_hours': [9, 14, 16],
            'session_continuity_usage': 0.65
        }
        
    def _generate_pattern_insights(self, type_stats: Dict, query_patterns: Dict) -> List[str]:
        """Generate insights from pattern analysis"""
        insights = []
        
        # Context type insights
        if type_stats:
            most_used = max(type_stats.items(), key=lambda x: x[1]['count'])
            insights.append(f"Most used context type: {most_used[0]} ({most_used[1]['count']} items)")
            
        # Performance insights
        if self.query_stats['average_response_time'] > 1.0:
            insights.append("Consider optimizing query performance - average response time is high")
            
        if self.query_stats['cache_hit_rate'] < 0.3:
            insights.append("Low cache hit rate - consider adjusting cache TTL or query patterns")
            
        return insights
        
    def _analyze_success_factors(self, successful_retrievals: List[Dict]) -> Dict[str, float]:
        """Analyze factors that made retrievals successful"""
        factors = {}
        
        for retrieval in successful_retrievals:
            # Analyze what correlation types were most successful
            correlation_data = retrieval.get('correlation_metadata', {})
            for factor, value in correlation_data.items():
                if factor not in factors:
                    factors[factor] = []
                factors[factor].append(value)
                
        # Calculate impact scores
        impact_scores = {}
        for factor, values in factors.items():
            if values:
                impact_scores[factor] = sum(values) / len(values) if isinstance(values[0], (int, float)) else 0.1
                
        return impact_scores
        
    def _generate_handoff_summary(self, context_items: List[Dict], 
                                 correlations: List[ContextCorrelation]) -> Dict[str, Any]:
        """Generate summary for handoff"""
        if not context_items:
            return {'summary': 'No context items found', 'key_topics': [], 'recommendations': []}
            
        # Analyze key topics
        content_texts = [item.get('content', '') for item in context_items]
        
        # Simple keyword extraction (could be enhanced with NLP)
        all_words = ' '.join(content_texts).lower().split()
        word_freq = {}
        for word in all_words:
            if len(word) > 4:  # Filter short words
                word_freq[word] = word_freq.get(word, 0) + 1
                
        key_topics = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Generate recommendations
        recommendations = []
        if correlations:
            recommendations.append(f"Found {len(correlations)} strong correlations between context items")
        if len(context_items) > 20:
            recommendations.append("Consider context compaction due to high item count")
            
        return {
            'summary': f"Session contains {len(context_items)} context items with {len(correlations)} correlations",
            'key_topics': [topic[0] for topic in key_topics],
            'recommendations': recommendations,
            'context_distribution': self._get_context_type_distribution(context_items)
        }
        
    def _get_context_type_distribution(self, context_items: List[Dict]) -> Dict[str, int]:
        """Get distribution of context types"""
        distribution = {}
        for item in context_items:
            context_type = item.get('context_type', 'unknown')
            distribution[context_type] = distribution.get(context_type, 0) + 1
        return distribution

if __name__ == "__main__":
    # Example usage
    engine = SemanticRetrievalEngine()
    
    # Test retrieval
    query = RetrievalQuery(
        query_text="help me create documentation",
        query_type="semantic",
        filters={'context_types': ['command', 'user_voice']},
        max_results=5
    )
    
    results = engine.retrieve_context(query)
    print(f"Retrieved {len(results)} results")
    
    for result in results[:3]:
        print(f"- {result.context_item.context_type}: {result.relevance_score:.3f}")