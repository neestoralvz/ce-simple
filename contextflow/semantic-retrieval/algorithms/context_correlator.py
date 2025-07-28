#!/usr/bin/env python3
"""
Context Correlation Algorithms - Intelligence Layer
Implements intent matching, relevance prioritization, cross-conversation bridging, and decision tree support
"""

import json
import math
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from collections import defaultdict, Counter
from pathlib import Path
import sqlite3
import numpy as np
import re

# NLP and similarity computation
try:
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    SKLEARN_AVAILABLE = True
except ImportError:
    SKLEARN_AVAILABLE = False
    logging.warning("scikit-learn not available. Using fallback similarity methods.")

@dataclass
class ContextCorrelation:
    """Represents correlation between context items"""
    source_id: str
    target_id: str
    correlation_type: str  # 'semantic', 'temporal', 'structural', 'intentional'
    strength: float  # 0.0 to 1.0
    metadata: Dict[str, Any]
    timestamp: str

@dataclass 
class IntentPattern:
    """Represents identified user intent pattern"""
    intent_id: str
    pattern_text: str
    keywords: List[str]
    context_types: List[str]
    frequency: int
    confidence: float
    examples: List[str]

class ContextCorrelator:
    """
    Advanced context correlation engine
    Implements intelligent matching and relevance algorithms
    """
    
    def __init__(self, context_db_path: str):
        self.context_db_path = Path(context_db_path)
        self.correlations_cache = {}
        self.intent_patterns = {}
        
        # Initialize TF-IDF vectorizer for semantic matching
        if SKLEARN_AVAILABLE:
            self.tfidf_vectorizer = TfidfVectorizer(
                max_features=5000,
                stop_words='english',
                ngram_range=(1, 3),
                max_df=0.8,
                min_df=2
            )
        else:
            self.tfidf_vectorizer = None
            
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
        # Correlation weights by type
        self.correlation_weights = {
            'semantic': 0.4,
            'temporal': 0.2,
            'structural': 0.2,
            'intentional': 0.2
        }
        
        # Intent keywords for pattern recognition
        self.intent_keywords = {
            'creation': ['create', 'build', 'generate', 'make', 'implement', 'develop'],
            'analysis': ['analyze', 'understand', 'explore', 'investigate', 'examine', 'study'],
            'modification': ['update', 'modify', 'change', 'edit', 'refactor', 'improve'],
            'debugging': ['debug', 'fix', 'error', 'issue', 'problem', 'troubleshoot'],
            'documentation': ['document', 'explain', 'describe', 'write', 'clarify'],
            'optimization': ['optimize', 'improve', 'enhance', 'performance', 'efficiency'],
            'integration': ['integrate', 'connect', 'merge', 'combine', 'link'],
            'validation': ['validate', 'test', 'verify', 'check', 'confirm', 'ensure']
        }
        
    def match_user_intent(self, query: str, context_items: List[Dict]) -> List[Tuple[Dict, float]]:
        """
        Match user intent to relevant contextual patterns
        Returns ranked list of (context_item, relevance_score) tuples
        """
        if not context_items:
            return []
            
        # Extract intent from query
        detected_intent = self._detect_intent(query)
        
        # Calculate relevance scores
        scored_items = []
        for item in context_items:
            relevance = self._calculate_intent_relevance(query, item, detected_intent)
            if relevance > 0.1:  # Threshold filter
                scored_items.append((item, relevance))
                
        # Sort by relevance score (descending)
        scored_items.sort(key=lambda x: x[1], reverse=True)
        
        self.logger.info(f"Intent matching: {detected_intent} → {len(scored_items)} relevant items")
        return scored_items
        
    def prioritize_context_by_recency(self, context_items: List[Dict], 
                                    recency_weight: float = 0.3) -> List[Tuple[Dict, float]]:
        """
        Prioritize context based on recency vs historical relevance
        Implements exponential decay for temporal relevance
        """
        current_time = datetime.now()
        weighted_items = []
        
        for item in context_items:
            try:
                item_time = datetime.fromisoformat(item.get('timestamp', current_time.isoformat()))
                time_diff = (current_time - item_time).total_seconds()
                
                # Exponential decay: more recent = higher weight
                # Half-life of 7 days for recency
                half_life_seconds = 7 * 24 * 3600
                recency_score = math.exp(-0.693 * time_diff / half_life_seconds)
                
                # Combine with existing relevance score
                base_relevance = item.get('relevance_score', 0.5)
                combined_score = (recency_weight * recency_score + 
                                (1 - recency_weight) * base_relevance)
                
                weighted_items.append((item, combined_score))
                
            except Exception as e:
                self.logger.warning(f"Error processing item timestamp: {e}")
                weighted_items.append((item, item.get('relevance_score', 0.1)))
                
        # Sort by combined score
        weighted_items.sort(key=lambda x: x[1], reverse=True)
        
        return weighted_items
        
    def bridge_cross_conversation_context(self, current_session_id: str, 
                                        query_context: str) -> List[Dict]:
        """
        Enable context bridging across different conversations
        Identifies relevant context from previous sessions
        """
        bridged_context = []
        
        # Get context from database
        with sqlite3.connect(self.context_db_path) as conn:
            # Find related sessions through content similarity
            cursor = conn.execute('''
                SELECT * FROM context_items 
                WHERE session_id != ? OR session_id IS NULL
                ORDER BY relevance_score DESC, timestamp DESC
                LIMIT 100
            ''', (current_session_id,))
            
            previous_items = [dict(zip([col[0] for col in cursor.description], row)) 
                            for row in cursor.fetchall()]
            
        # Calculate semantic similarity with current query
        if previous_items and self.tfidf_vectorizer is not None:
            try:
                # Prepare texts for similarity comparison
                texts = [query_context] + [item['content'] for item in previous_items]
                
                # Calculate TF-IDF similarity
                tfidf_matrix = self.tfidf_vectorizer.fit_transform(texts)
                similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()
                
                # Filter and rank by similarity
                for i, similarity in enumerate(similarities):
                    if similarity > 0.2:  # Similarity threshold
                        item = previous_items[i].copy()
                        item['cross_session_similarity'] = float(similarity)
                        bridged_context.append(item)
                        
            except Exception as e:
                self.logger.error(f"Error in cross-conversation bridging: {e}")
                
        # Sort by similarity score
        bridged_context.sort(key=lambda x: x.get('cross_session_similarity', 0), reverse=True)
        
        self.logger.info(f"Cross-conversation bridging: found {len(bridged_context)} relevant items")
        return bridged_context[:20]  # Limit to top 20 items
        
    def support_contextflow_decision_trees(self, decision_context: str, 
                                         available_options: List[str]) -> Dict[str, float]:
        """
        Support decision tree navigation through contextflow patterns
        Analyzes context to recommend decision paths
        """
        option_scores = {}
        
        # Get historical decision patterns
        with sqlite3.connect(self.context_db_path) as conn:
            cursor = conn.execute('''
                SELECT content, metadata FROM context_items 
                WHERE context_type IN ('command', 'session')
                AND content LIKE '%decision%' OR content LIKE '%choose%' OR content LIKE '%option%'
                ORDER BY timestamp DESC
                LIMIT 50
            ''')
            
            decision_history = cursor.fetchall()
            
        # Analyze patterns for each option
        for option in available_options:
            score = self._calculate_decision_pattern_score(
                option, decision_context, decision_history
            )
            option_scores[option] = score
            
        # Normalize scores
        if option_scores:
            max_score = max(option_scores.values())
            if max_score > 0:
                option_scores = {k: v/max_score for k, v in option_scores.items()}
                
        self.logger.info(f"Decision tree support: scored {len(option_scores)} options")
        return option_scores
        
    def generate_context_correlations(self, context_items: List[Dict]) -> List[ContextCorrelation]:
        """
        Generate comprehensive context correlations
        Identifies relationships between context items
        """
        correlations = []
        
        for i, item1 in enumerate(context_items):
            for item2 in context_items[i+1:]:
                correlation = self._calculate_comprehensive_correlation(item1, item2)
                if correlation.strength > 0.3:  # Correlation threshold
                    correlations.append(correlation)
                    
        # Sort by correlation strength
        correlations.sort(key=lambda x: x.strength, reverse=True)
        
        self.logger.info(f"Generated {len(correlations)} context correlations")
        return correlations
        
    def learn_intent_patterns(self, user_interactions: List[Dict]) -> List[IntentPattern]:
        """
        Learn and extract user intent patterns from interactions
        Builds intelligent pattern recognition
        """
        intent_patterns = []
        
        # Group interactions by detected intent
        intent_groups = defaultdict(list)
        for interaction in user_interactions:
            intent = self._detect_intent(interaction.get('content', ''))
            intent_groups[intent].append(interaction)
            
        # Generate patterns for each intent type
        for intent_type, interactions in intent_groups.items():
            if len(interactions) >= 3:  # Minimum frequency threshold
                pattern = self._create_intent_pattern(intent_type, interactions)
                intent_patterns.append(pattern)
                
        self.logger.info(f"Learned {len(intent_patterns)} intent patterns")
        return intent_patterns
        
    # Private helper methods
    def _detect_intent(self, text: str) -> str:
        """Detect primary intent from text"""
        text_lower = text.lower()
        intent_scores = {}
        
        for intent, keywords in self.intent_keywords.items():
            score = sum(1 for keyword in keywords if keyword in text_lower)
            if score > 0:
                intent_scores[intent] = score
                
        if intent_scores:
            return max(intent_scores.items(), key=lambda x: x[1])[0]
        return 'general'
        
    def _calculate_intent_relevance(self, query: str, context_item: Dict, 
                                  detected_intent: str) -> float:
        """Calculate relevance score between query intent and context item"""
        relevance_factors = []
        
        # 1. Semantic similarity (if available)
        if self.tfidf_vectorizer is not None and SKLEARN_AVAILABLE:
            try:
                texts = [query, context_item.get('content', '')]
                tfidf_matrix = self.tfidf_vectorizer.fit_transform(texts)
                semantic_sim = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
                relevance_factors.append(('semantic', semantic_sim))
            except:
                relevance_factors.append(('semantic', 0.1))
        
        # 2. Intent matching
        item_intent = self._detect_intent(context_item.get('content', ''))
        intent_match = 1.0 if item_intent == detected_intent else 0.3
        relevance_factors.append(('intent', intent_match))
        
        # 3. Context type relevance
        context_type = context_item.get('context_type', 'general')
        type_relevance = self._get_context_type_relevance(context_type, detected_intent)
        relevance_factors.append(('type', type_relevance))
        
        # 4. Existing relevance score
        existing_score = context_item.get('relevance_score', 0.5)
        relevance_factors.append(('existing', existing_score))
        
        # Weighted combination
        total_relevance = sum(score * self.correlation_weights.get(factor, 0.25) 
                            for factor, score in relevance_factors)
        
        return min(total_relevance, 1.0)
        
    def _get_context_type_relevance(self, context_type: str, intent: str) -> float:
        """Get relevance score for context type given intent"""
        relevance_matrix = {
            'command': {'creation': 0.9, 'modification': 0.8, 'analysis': 0.6},
            'user_voice': {'analysis': 0.9, 'documentation': 0.8, 'creation': 0.7},
            'session': {'analysis': 0.8, 'integration': 0.7, 'debugging': 0.6},
            'project_evolution': {'optimization': 0.9, 'analysis': 0.8, 'validation': 0.7}
        }
        
        return relevance_matrix.get(context_type, {}).get(intent, 0.5)
        
    def _calculate_decision_pattern_score(self, option: str, context: str, 
                                        history: List[Tuple]) -> float:
        """Calculate score for decision option based on historical patterns"""
        score = 0.0
        option_lower = option.lower()
        context_lower = context.lower()
        
        for content, metadata_str in history:
            content_lower = content.lower()
            
            # Check for option mentions in successful decisions
            if option_lower in content_lower:
                score += 0.3
                
            # Check for contextual similarity
            common_words = set(context_lower.split()) & set(content_lower.split())
            if len(common_words) > 2:
                score += 0.2 * len(common_words)
                
            # Parse metadata for success indicators
            try:
                metadata = json.loads(metadata_str) if metadata_str else {}
                if metadata.get('success', False):
                    score += 0.1
            except:
                pass
                
        return min(score, 1.0)
        
    def _calculate_comprehensive_correlation(self, item1: Dict, item2: Dict) -> ContextCorrelation:
        """Calculate comprehensive correlation between two context items"""
        correlation_scores = {}
        
        # Semantic correlation
        if self.tfidf_vectorizer is not None and SKLEARN_AVAILABLE:
            try:
                texts = [item1.get('content', ''), item2.get('content', '')]
                tfidf_matrix = self.tfidf_vectorizer.fit_transform(texts)
                semantic_score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
                correlation_scores['semantic'] = semantic_score
            except:
                correlation_scores['semantic'] = 0.1
                
        # Temporal correlation
        temporal_score = self._calculate_temporal_correlation(
            item1.get('timestamp'), item2.get('timestamp')
        )
        correlation_scores['temporal'] = temporal_score
        
        # Structural correlation (same context type, command, etc.)
        structural_score = self._calculate_structural_correlation(item1, item2)
        correlation_scores['structural'] = structural_score
        
        # Intentional correlation
        intent1 = self._detect_intent(item1.get('content', ''))
        intent2 = self._detect_intent(item2.get('content', ''))
        intentional_score = 1.0 if intent1 == intent2 else 0.3
        correlation_scores['intentional'] = intentional_score
        
        # Calculate overall strength
        overall_strength = sum(score * self.correlation_weights.get(corr_type, 0.25)
                             for corr_type, score in correlation_scores.items())
        
        # Determine primary correlation type
        primary_type = max(correlation_scores.items(), key=lambda x: x[1])[0]
        
        return ContextCorrelation(
            source_id=item1.get('id', ''),
            target_id=item2.get('id', ''),
            correlation_type=primary_type,
            strength=overall_strength,
            metadata=correlation_scores,
            timestamp=datetime.now().isoformat()
        )
        
    def _calculate_temporal_correlation(self, timestamp1: str, timestamp2: str) -> float:
        """Calculate temporal correlation between timestamps"""
        try:
            time1 = datetime.fromisoformat(timestamp1)
            time2 = datetime.fromisoformat(timestamp2)
            time_diff = abs((time1 - time2).total_seconds())
            
            # Exponential decay: closer in time = higher correlation
            # Half-life of 1 day
            half_life_seconds = 24 * 3600
            correlation = math.exp(-0.693 * time_diff / half_life_seconds)
            
            return correlation
        except:
            return 0.1
            
    def _calculate_structural_correlation(self, item1: Dict, item2: Dict) -> float:
        """Calculate structural correlation between items"""
        score = 0.0
        
        # Same context type
        if item1.get('context_type') == item2.get('context_type'):
            score += 0.4
            
        # Same session
        if (item1.get('session_id') and item2.get('session_id') and 
            item1.get('session_id') == item2.get('session_id')):
            score += 0.3
            
        # Same command context
        if (item1.get('command_context') and item2.get('command_context') and
            item1.get('command_context') == item2.get('command_context')):
            score += 0.3
            
        return min(score, 1.0)
        
    def _create_intent_pattern(self, intent_type: str, interactions: List[Dict]) -> IntentPattern:
        """Create intent pattern from interactions"""
        # Extract common keywords
        all_words = []
        examples = []
        
        for interaction in interactions:
            content = interaction.get('content', '')
            all_words.extend(content.lower().split())
            examples.append(content[:100])  # First 100 chars as example
            
        # Find most common keywords
        word_counts = Counter(all_words)
        common_keywords = [word for word, count in word_counts.most_common(10) 
                          if count > 1 and len(word) > 3]
        
        # Determine context types
        context_types = list(set(interaction.get('context_type', 'general') 
                               for interaction in interactions))
        
        return IntentPattern(
            intent_id=f"{intent_type}_{len(interactions)}",
            pattern_text=f"Pattern for {intent_type} intent",
            keywords=common_keywords,
            context_types=context_types,
            frequency=len(interactions),
            confidence=min(len(interactions) / 10.0, 1.0),  # Confidence based on frequency
            examples=examples[:3]  # Keep top 3 examples
        )

if __name__ == "__main__":
    # Example usage
    correlator = ContextCorrelator("/Users/nalve/ce-simple/contextflow/semantic-retrieval/context.db")
    
    # Test intent detection
    test_query = "I need to create a new documentation system"
    print(f"Detected intent: {correlator._detect_intent(test_query)}")