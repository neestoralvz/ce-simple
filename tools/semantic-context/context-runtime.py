#!/usr/bin/env python3
"""
Context Engineering Runtime with 2025 Research-Backed Strategies
Implements WRITE/SELECT/COMPRESS/ISOLATE paradigm for intelligent context management
Based on latest research in context engineering for LLM agents
"""

import json
import logging
import sqlite3
import time
import re
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Union, Set
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
from enum import Enum
import threading
import hashlib
from abc import ABC, abstractmethod

# Advanced dependencies with fallbacks
try:
    import numpy as np
    NUMPY_AVAILABLE = True
except ImportError:
    NUMPY_AVAILABLE = False

try:
    from transformers import AutoTokenizer
    TOKENIZER_AVAILABLE = True
except ImportError:
    TOKENIZER_AVAILABLE = False
    logging.warning("Transformers library not available. Using approximate token counting.")

class ContextStrategy(Enum):
    """Context engineering strategies based on 2025 research"""
    WRITE = "write"      # Structured runtime state objects
    SELECT = "select"    # Intelligent memory selection
    COMPRESS = "compress" # Context summarization with pruning
    ISOLATE = "isolate"  # Sub-agent context separation

class MemoryType(Enum):
    """Types of memory for SELECT strategy"""
    EPISODIC = "episodic"      # Specific events and experiences
    PROCEDURAL = "procedural"  # Skills and procedures
    SEMANTIC = "semantic"      # Facts and relationships
    WORKING = "working"        # Current active context

@dataclass
class ContextItem:
    """Enhanced context item with runtime metadata"""
    id: str
    content: str
    context_type: str
    memory_type: MemoryType
    priority: float
    timestamp: str
    session_id: Optional[str] = None
    access_count: int = 0
    last_accessed: Optional[str] = None
    compression_ratio: float = 1.0
    isolation_level: int = 0
    metadata: Optional[Dict[str, Any]] = None

@dataclass
class RuntimeState:
    """Runtime state object for WRITE strategy"""
    state_id: str
    active_contexts: List[str]
    memory_allocation: Dict[MemoryType, int]
    compression_targets: Dict[str, float]
    isolation_boundaries: Dict[str, Set[str]]
    performance_metrics: Dict[str, float]
    created_at: str
    updated_at: str

class ContextStrategy_Base(ABC):
    """Base class for context engineering strategies"""
    
    @abstractmethod
    def apply(self, contexts: List[ContextItem], params: Dict[str, Any]) -> List[ContextItem]:
        """Apply the strategy to context items"""
        pass
        
    @abstractmethod
    def get_metrics(self) -> Dict[str, Any]:
        """Get strategy-specific metrics"""
        pass

class WriteStrategy(ContextStrategy_Base):
    """
    WRITE Strategy: Structured runtime state objects for selective memory access
    Maintains structured state for intelligent context management
    """
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.active_states: Dict[str, RuntimeState] = {}
        self.state_history: deque = deque(maxlen=100)
        self.logger = logging.getLogger(__name__)
        
    def apply(self, contexts: List[ContextItem], params: Dict[str, Any]) -> List[ContextItem]:
        """Apply WRITE strategy to create structured runtime state"""
        session_id = params.get('session_id', 'default')
        state_id = f"state_{session_id}_{int(time.time())}"
        
        # Analyze contexts to create runtime state
        memory_allocation = self._analyze_memory_allocation(contexts)
        compression_targets = self._identify_compression_targets(contexts)
        isolation_boundaries = self._define_isolation_boundaries(contexts)
        performance_metrics = self._calculate_performance_metrics(contexts)
        
        # Create runtime state
        runtime_state = RuntimeState(
            state_id=state_id,
            active_contexts=[ctx.id for ctx in contexts],
            memory_allocation=memory_allocation,
            compression_targets=compression_targets,
            isolation_boundaries=isolation_boundaries,
            performance_metrics=performance_metrics,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat()
        )
        
        # Store and activate state
        self.active_states[state_id] = runtime_state
        self.state_history.append(state_id)
        self._persist_state(runtime_state)
        
        # Update contexts with state information
        updated_contexts = []
        for ctx in contexts:
            ctx.metadata = ctx.metadata or {}
            ctx.metadata['runtime_state_id'] = state_id
            ctx.metadata['memory_allocation'] = memory_allocation.get(ctx.memory_type, 0)
            updated_contexts.append(ctx)
            
        self.logger.info(f"WRITE strategy applied: created state {state_id} with {len(contexts)} contexts")
        return updated_contexts
        
    def _analyze_memory_allocation(self, contexts: List[ContextItem]) -> Dict[MemoryType, int]:
        """Analyze optimal memory allocation across memory types"""
        allocation = defaultdict(int)
        
        # Count contexts by memory type
        for ctx in contexts:
            allocation[ctx.memory_type] += 1
            
        # Apply research-backed allocation ratios
        total_contexts = len(contexts)
        if total_contexts > 0:
            # Optimal ratios based on cognitive load research
            ratios = {
                MemoryType.WORKING: 0.3,    # 30% for active work
                MemoryType.EPISODIC: 0.4,   # 40% for recent experiences
                MemoryType.PROCEDURAL: 0.2, # 20% for procedures
                MemoryType.SEMANTIC: 0.1    # 10% for facts
            }
            
            for memory_type, ratio in ratios.items():
                allocation[memory_type] = max(allocation[memory_type], int(total_contexts * ratio))
                
        return dict(allocation)
        
    def _identify_compression_targets(self, contexts: List[ContextItem]) -> Dict[str, float]:
        """Identify contexts that should be compressed"""
        targets = {}
        
        for ctx in contexts:
            # Target compression based on age and access patterns
            age_days = self._calculate_age_days(ctx.timestamp)
            access_frequency = ctx.access_count / max(age_days, 1)
            
            # Compression formula based on usage patterns
            if age_days > 7 and access_frequency < 0.1:
                targets[ctx.id] = 0.5  # 50% compression
            elif age_days > 3 and access_frequency < 0.5:
                targets[ctx.id] = 0.7  # 30% compression
            elif ctx.memory_type == MemoryType.SEMANTIC and len(ctx.content) > 1000:
                targets[ctx.id] = 0.8  # 20% compression for large semantic content
                
        return targets
        
    def _define_isolation_boundaries(self, contexts: List[ContextItem]) -> Dict[str, Set[str]]:
        """Define isolation boundaries between context groups"""
        boundaries = defaultdict(set)
        
        # Group contexts by session and type
        session_groups = defaultdict(list)
        for ctx in contexts:
            key = f"{ctx.session_id}_{ctx.context_type}"
            session_groups[key].append(ctx.id)
            
        # Create isolation boundaries
        for group_key, context_ids in session_groups.items():
            boundaries[group_key] = set(context_ids)
            
        return dict(boundaries)
        
    def _calculate_performance_metrics(self, contexts: List[ContextItem]) -> Dict[str, float]:
        """Calculate performance metrics for the context set"""
        if not contexts:
            return {}
            
        total_size = sum(len(ctx.content) for ctx in contexts)
        avg_compression = sum(ctx.compression_ratio for ctx in contexts) / len(contexts)
        memory_efficiency = sum(1 for ctx in contexts if ctx.access_count > 0) / len(contexts)
        
        return {
            'total_contexts': len(contexts),
            'total_size_chars': total_size,
            'average_compression': avg_compression,
            'memory_efficiency': memory_efficiency,
            'working_memory_ratio': sum(1 for ctx in contexts if ctx.memory_type == MemoryType.WORKING) / len(contexts)
        }
        
    def _calculate_age_days(self, timestamp: str) -> float:
        """Calculate age in days from timestamp"""
        try:
            created_time = datetime.fromisoformat(timestamp)
            return (datetime.now() - created_time).days
        except:
            return 0.0
            
    def _persist_state(self, state: RuntimeState):
        """Persist runtime state to database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS runtime_states (
                    state_id TEXT PRIMARY KEY,
                    state_data TEXT,
                    created_at TEXT,
                    updated_at TEXT
                )
            ''')
            
            conn.execute('''
                INSERT OR REPLACE INTO runtime_states 
                (state_id, state_data, created_at, updated_at)
                VALUES (?, ?, ?, ?)
            ''', (
                state.state_id,
                json.dumps(asdict(state)),
                state.created_at,
                state.updated_at
            ))
            
    def get_metrics(self) -> Dict[str, Any]:
        """Get WRITE strategy metrics"""
        return {
            'active_states': len(self.active_states),
            'total_states_created': len(self.state_history),
            'average_contexts_per_state': np.mean([len(state.active_contexts) for state in self.active_states.values()]) if self.active_states else 0
        }

class SelectStrategy(ContextStrategy_Base):
    """
    SELECT Strategy: Intelligent memory selection (episodic/procedural/semantic)
    Optimizes memory selection based on cognitive load and relevance
    """
    
    def __init__(self):
        self.selection_history = defaultdict(list)
        self.performance_tracker = defaultdict(float)
        self.logger = logging.getLogger(__name__)
        
    def apply(self, contexts: List[ContextItem], params: Dict[str, Any]) -> List[ContextItem]:
        """Apply SELECT strategy for intelligent memory selection"""
        query_context = params.get('query_context', '')
        max_contexts = params.get('max_contexts', 20)
        memory_priorities = params.get('memory_priorities', {
            MemoryType.WORKING: 1.0,
            MemoryType.EPISODIC: 0.8,
            MemoryType.PROCEDURAL: 0.6,
            MemoryType.SEMANTIC: 0.4
        })
        
        # Score contexts based on multiple factors
        scored_contexts = []
        for ctx in contexts:
            score = self._calculate_selection_score(ctx, query_context, memory_priorities)
            scored_contexts.append((ctx, score))
            
        # Sort by score and select top contexts
        scored_contexts.sort(key=lambda x: x[1], reverse=True)
        selected_contexts = [ctx for ctx, score in scored_contexts[:max_contexts]]
        
        # Update selection history
        session_id = params.get('session_id', 'default')
        self.selection_history[session_id].append({
            'timestamp': datetime.now().isoformat(),
            'selected_count': len(selected_contexts),
            'total_available': len(contexts),
            'selection_ratio': len(selected_contexts) / len(contexts) if contexts else 0
        })
        
        self.logger.info(f"SELECT strategy: selected {len(selected_contexts)} from {len(contexts)} contexts")
        return selected_contexts
        
    def _calculate_selection_score(self, ctx: ContextItem, query_context: str, 
                                 memory_priorities: Dict[MemoryType, float]) -> float:
        """Calculate context selection score"""
        score = 0.0
        
        # Base priority from memory type
        score += memory_priorities.get(ctx.memory_type, 0.5) * 10
        
        # Recency bonus
        age_days = self._calculate_age_days(ctx.timestamp)
        recency_score = max(0, 5 - age_days * 0.5)  # Decay over time
        score += recency_score
        
        # Usage frequency bonus
        frequency_score = min(ctx.access_count * 0.1, 2.0)  # Cap at 2.0
        score += frequency_score
        
        # Content relevance (simple keyword matching - could be enhanced)
        if query_context:
            relevance_score = self._calculate_content_relevance(ctx.content, query_context)
            score += relevance_score * 3
            
        # Priority boost
        score += ctx.priority * 2
        
        # Compression penalty (compressed content is less accessible)
        if ctx.compression_ratio < 1.0:
            score *= ctx.compression_ratio
            
        return score
        
    def _calculate_content_relevance(self, content: str, query_context: str) -> float:
        """Calculate content relevance to query context"""
        if not query_context:
            return 0.0
            
        # Simple word overlap - could be enhanced with embeddings
        content_words = set(re.findall(r'\w+', content.lower()))
        query_words = set(re.findall(r'\w+', query_context.lower()))
        
        if not query_words:
            return 0.0
            
        overlap = len(content_words.intersection(query_words))
        return overlap / len(query_words)
        
    def _calculate_age_days(self, timestamp: str) -> float:
        """Calculate age in days"""
        try:
            created_time = datetime.fromisoformat(timestamp)
            return (datetime.now() - created_time).days
        except:
            return 0.0
            
    def get_metrics(self) -> Dict[str, Any]:
        """Get SELECT strategy metrics"""
        if not self.selection_history:
            return {}
            
        all_selections = []
        for session_selections in self.selection_history.values():
            all_selections.extend(session_selections)
            
        if not all_selections:
            return {}
            
        avg_selection_ratio = np.mean([s['selection_ratio'] for s in all_selections]) if NUMPY_AVAILABLE else 0
        avg_selected_count = np.mean([s['selected_count'] for s in all_selections]) if NUMPY_AVAILABLE else 0
        
        return {
            'total_selections': len(all_selections),
            'average_selection_ratio': avg_selection_ratio,
            'average_selected_count': avg_selected_count,
            'active_sessions': len(self.selection_history)
        }

class CompressStrategy(ContextStrategy_Base):
    """
    COMPRESS Strategy: Context summarization with pruning heuristics
    Implements intelligent compression to reduce context size while preserving meaning
    """
    
    def __init__(self):
        self.compression_stats = defaultdict(list)
        self.tokenizer = None
        self.logger = logging.getLogger(__name__)
        
        # Initialize tokenizer if available
        if TOKENIZER_AVAILABLE:
            try:
                self.tokenizer = AutoTokenizer.from_pretrained('gpt2')
            except:
                self.logger.warning("Could not load tokenizer for precise compression")
                
    def apply(self, contexts: List[ContextItem], params: Dict[str, Any]) -> List[ContextItem]:
        """Apply COMPRESS strategy for context summarization"""
        target_compression = params.get('target_compression', 0.7)  # 30% reduction
        preserve_working_memory = params.get('preserve_working_memory', True)
        compression_method = params.get('compression_method', 'adaptive')
        
        compressed_contexts = []
        total_original_size = 0
        total_compressed_size = 0
        
        for ctx in contexts:
            original_size = len(ctx.content)
            total_original_size += original_size
            
            # Skip compression for working memory if requested
            if preserve_working_memory and ctx.memory_type == MemoryType.WORKING:
                compressed_contexts.append(ctx)
                total_compressed_size += original_size
                continue
                
            # Determine compression level
            compression_ratio = self._determine_compression_ratio(ctx, target_compression)
            
            if compression_ratio < 1.0:
                compressed_content = self._compress_content(ctx.content, compression_ratio, compression_method)
                
                # Create compressed context
                compressed_ctx = ContextItem(
                    id=ctx.id,
                    content=compressed_content,
                    context_type=ctx.context_type,
                    memory_type=ctx.memory_type,
                    priority=ctx.priority,
                    timestamp=ctx.timestamp,
                    session_id=ctx.session_id,
                    access_count=ctx.access_count,
                    last_accessed=ctx.last_accessed,
                    compression_ratio=compression_ratio,
                    isolation_level=ctx.isolation_level,
                    metadata=ctx.metadata or {}
                )
                
                # Update metadata
                compressed_ctx.metadata['original_size'] = original_size
                compressed_ctx.metadata['compressed_at'] = datetime.now().isoformat()
                compressed_ctx.metadata['compression_method'] = compression_method
                
                compressed_contexts.append(compressed_ctx)
                total_compressed_size += len(compressed_content)
                
                # Record compression stats
                self.compression_stats[ctx.context_type].append({
                    'original_size': original_size,
                    'compressed_size': len(compressed_content),
                    'ratio': compression_ratio,
                    'method': compression_method
                })
            else:
                compressed_contexts.append(ctx)
                total_compressed_size += original_size
                
        overall_compression = total_compressed_size / total_original_size if total_original_size > 0 else 1.0
        self.logger.info(f"COMPRESS strategy: {len(contexts)} contexts, {overall_compression:.2f} compression ratio")
        
        return compressed_contexts
        
    def _determine_compression_ratio(self, ctx: ContextItem, target_compression: float) -> float:
        """Determine appropriate compression ratio for context"""
        # Base compression from target
        compression_ratio = target_compression
        
        # Adjust based on context age
        age_days = self._calculate_age_days(ctx.timestamp)
        if age_days > 7:
            compression_ratio *= 0.8  # More aggressive compression for old content
        elif age_days < 1:
            compression_ratio = max(compression_ratio, 0.9)  # Light compression for recent content
            
        # Adjust based on access patterns
        if ctx.access_count > 5:
            compression_ratio = max(compression_ratio, 0.8)  # Preserve frequently accessed content
        elif ctx.access_count == 0:
            compression_ratio *= 0.7  # Aggressive compression for unused content
            
        # Adjust based on memory type
        if ctx.memory_type == MemoryType.PROCEDURAL:
            compression_ratio = max(compression_ratio, 0.9)  # Preserve procedures
        elif ctx.memory_type == MemoryType.SEMANTIC:
            compression_ratio *= 0.8  # Facts can be compressed more
            
        return max(compression_ratio, 0.3)  # Minimum 30% retention
        
    def _compress_content(self, content: str, compression_ratio: float, method: str) -> str:
        """Compress content using specified method"""
        if method == 'adaptive':
            return self._adaptive_compression(content, compression_ratio)
        elif method == 'extractive':
            return self._extractive_compression(content, compression_ratio)
        elif method == 'keyword':
            return self._keyword_compression(content, compression_ratio)
        else:
            return self._truncate_compression(content, compression_ratio)
            
    def _adaptive_compression(self, content: str, ratio: float) -> str:
        """Adaptive compression combining multiple techniques"""
        # Start with extractive summarization
        sentences = self._split_into_sentences(content)
        if len(sentences) <= 2:
            return content  # Too short to compress meaningfully
            
        # Score sentences by importance
        sentence_scores = self._score_sentences(sentences, content)
        
        # Select sentences to keep
        target_sentences = max(1, int(len(sentences) * ratio))
        top_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)[:target_sentences]
        
        # Reconstruct in original order
        kept_sentences = sorted(top_sentences, key=lambda x: sentences.index(x[0]))
        compressed = ' '.join([sent[0] for sent in kept_sentences])
        
        # If still too long, apply keyword compression
        if len(compressed) > len(content) * ratio:
            compressed = self._keyword_compression(compressed, ratio)
            
        return compressed
        
    def _extractive_compression(self, content: str, ratio: float) -> str:
        """Extractive summarization by sentence selection"""
        sentences = self._split_into_sentences(content)
        target_count = max(1, int(len(sentences) * ratio))
        
        if target_count >= len(sentences):
            return content
            
        # Simple frequency-based selection
        word_freq = self._calculate_word_frequencies(content)
        sentence_scores = []
        
        for sentence in sentences:
            words = re.findall(r'\w+', sentence.lower())
            score = sum(word_freq.get(word, 0) for word in words) / len(words) if words else 0
            sentence_scores.append((sentence, score))
            
        # Select top sentences
        top_sentences = sorted(sentence_scores, key=lambda x: x[1], reverse=True)[:target_count]
        return ' '.join([sent[0] for sent in top_sentences])
        
    def _keyword_compression(self, content: str, ratio: float) -> str:
        """Keyword-based compression focusing on important terms"""
        words = re.findall(r'\w+', content)
        target_length = int(len(content) * ratio)
        
        # Calculate word importance
        word_freq = self._calculate_word_frequencies(content)
        important_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        
        # Build compressed version with important words
        compressed_words = []
        char_count = 0
        
        for word, freq in important_words:
            if char_count + len(word) + 1 <= target_length:
                compressed_words.append(word)
                char_count += len(word) + 1
            else:
                break
                
        return ' '.join(compressed_words)
        
    def _truncate_compression(self, content: str, ratio: float) -> str:
        """Simple truncation compression"""
        target_length = int(len(content) * ratio)
        return content[:target_length] + "..." if len(content) > target_length else content
        
    def _split_into_sentences(self, text: str) -> List[str]:
        """Split text into sentences"""
        # Simple sentence splitting - could be enhanced with NLP
        sentences = re.split(r'[.!?]+', text)
        return [s.strip() for s in sentences if s.strip()]
        
    def _score_sentences(self, sentences: List[str], full_content: str) -> List[Tuple[str, float]]:
        """Score sentences by importance"""
        word_freq = self._calculate_word_frequencies(full_content)
        scored_sentences = []
        
        for sentence in sentences:
            words = re.findall(r'\w+', sentence.lower())
            # Score based on word frequency and sentence position
            freq_score = sum(word_freq.get(word, 0) for word in words) / len(words) if words else 0
            length_bonus = min(len(sentence) / 100, 1.0)  # Prefer medium-length sentences
            
            total_score = freq_score + length_bonus
            scored_sentences.append((sentence, total_score))
            
        return scored_sentences
        
    def _calculate_word_frequencies(self, text: str) -> Dict[str, float]:
        """Calculate word frequencies"""
        words = re.findall(r'\w+', text.lower())
        word_count = defaultdict(int)
        
        for word in words:
            if len(word) > 3:  # Skip short words
                word_count[word] += 1
                
        # Normalize frequencies
        total_words = sum(word_count.values())
        return {word: count / total_words for word, count in word_count.items()} if total_words > 0 else {}
        
    def _calculate_age_days(self, timestamp: str) -> float:
        """Calculate age in days"""
        try:
            created_time = datetime.fromisoformat(timestamp)
            return (datetime.now() - created_time).days
        except:
            return 0.0
            
    def get_metrics(self) -> Dict[str, Any]:
        """Get COMPRESS strategy metrics"""
        if not self.compression_stats:
            return {}
            
        all_compressions = []
        for context_type, compressions in self.compression_stats.items():
            all_compressions.extend(compressions)
            
        if not all_compressions:
            return {}
            
        avg_ratio = np.mean([c['ratio'] for c in all_compressions]) if NUMPY_AVAILABLE else 0
        total_saved = sum(c['original_size'] - c['compressed_size'] for c in all_compressions)
        
        return {
            'total_compressions': len(all_compressions),
            'average_compression_ratio': avg_ratio,
            'total_bytes_saved': total_saved,
            'compression_by_type': {ct: len(comps) for ct, comps in self.compression_stats.items()}
        }

class IsolateStrategy(ContextStrategy_Base):
    """
    ISOLATE Strategy: Sub-agent context separation for specialized processing
    Implements context isolation to prevent interference between different processing contexts
    """
    
    def __init__(self):
        self.isolation_boundaries = defaultdict(set)
        self.cross_boundary_accesses = defaultdict(int)
        self.logger = logging.getLogger(__name__)
        
    def apply(self, contexts: List[ContextItem], params: Dict[str, Any]) -> List[ContextItem]:
        """Apply ISOLATE strategy for context separation"""
        isolation_mode = params.get('isolation_mode', 'session')  # 'session', 'type', 'agent'
        max_isolation_level = params.get('max_isolation_level', 3)
        allow_cross_boundary = params.get('allow_cross_boundary', False)
        
        # Group contexts by isolation criteria
        isolation_groups = self._create_isolation_groups(contexts, isolation_mode)
        
        # Apply isolation levels
        isolated_contexts = []
        for group_id, group_contexts in isolation_groups.items():
            # Determine isolation level for this group
            isolation_level = self._calculate_isolation_level(group_contexts, max_isolation_level)
            
            # Apply isolation
            for ctx in group_contexts:
                isolated_ctx = self._apply_isolation(ctx, isolation_level, group_id, allow_cross_boundary)
                isolated_contexts.append(isolated_ctx)
                
        # Update isolation boundaries
        for group_id, group_contexts in isolation_groups.items():
            context_ids = {ctx.id for ctx in group_contexts}
            self.isolation_boundaries[group_id] = context_ids
            
        self.logger.info(f"ISOLATE strategy: created {len(isolation_groups)} isolation groups")
        return isolated_contexts
        
    def _create_isolation_groups(self, contexts: List[ContextItem], mode: str) -> Dict[str, List[ContextItem]]:
        """Create isolation groups based on specified mode"""
        groups = defaultdict(list)
        
        for ctx in contexts:
            if mode == 'session':
                group_key = ctx.session_id or 'default'
            elif mode == 'type':
                group_key = ctx.context_type
            elif mode == 'agent':
                # Extract agent info from metadata
                agent_id = ctx.metadata.get('agent_id', 'default') if ctx.metadata else 'default'
                group_key = agent_id
            elif mode == 'hybrid':
                # Combine session and type
                group_key = f"{ctx.session_id}_{ctx.context_type}"
            else:
                group_key = 'default'
                
            groups[group_key].append(ctx)
            
        return dict(groups)
        
    def _calculate_isolation_level(self, contexts: List[ContextItem], max_level: int) -> int:
        """Calculate appropriate isolation level for context group"""
        if not contexts:
            return 0
            
        # Factors influencing isolation level
        factors = []
        
        # Size factor: larger groups need more isolation
        size_factor = min(len(contexts) / 10, 1.0)
        factors.append(size_factor)
        
        # Diversity factor: more diverse content needs isolation
        context_types = len(set(ctx.context_type for ctx in contexts))
        diversity_factor = min(context_types / 5, 1.0)
        factors.append(diversity_factor)
        
        # Sensitivity factor: based on content sensitivity
        sensitive_count = sum(1 for ctx in contexts if self._is_sensitive_content(ctx))
        sensitivity_factor = sensitive_count / len(contexts)
        factors.append(sensitivity_factor)
        
        # Calculate isolation level
        average_factor = sum(factors) / len(factors)
        isolation_level = int(average_factor * max_level)
        
        return max(0, min(isolation_level, max_level))
        
    def _is_sensitive_content(self, ctx: ContextItem) -> bool:
        """Check if content is sensitive and needs higher isolation"""
        sensitive_indicators = [
            'user_voice', 'personal', 'private', 'confidential',
            'api_key', 'password', 'token', 'secret'
        ]
        
        content_lower = ctx.content.lower()
        context_type_lower = ctx.context_type.lower()
        
        return any(indicator in content_lower or indicator in context_type_lower 
                  for indicator in sensitive_indicators)
        
    def _apply_isolation(self, ctx: ContextItem, isolation_level: int, 
                        group_id: str, allow_cross_boundary: bool) -> ContextItem:
        """Apply isolation to context item"""
        isolated_ctx = ContextItem(
            id=ctx.id,
            content=ctx.content,
            context_type=ctx.context_type,
            memory_type=ctx.memory_type,
            priority=ctx.priority,
            timestamp=ctx.timestamp,
            session_id=ctx.session_id,
            access_count=ctx.access_count,
            last_accessed=ctx.last_accessed,
            compression_ratio=ctx.compression_ratio,
            isolation_level=isolation_level,
            metadata=ctx.metadata or {}
        )
        
        # Add isolation metadata
        isolated_ctx.metadata.update({
            'isolation_group': group_id,
            'isolation_level': isolation_level,
            'isolation_applied_at': datetime.now().isoformat(),
            'cross_boundary_allowed': allow_cross_boundary
        })
        
        # Apply isolation-specific modifications based on level
        if isolation_level >= 2:
            # Level 2+: Add access restrictions
            isolated_ctx.metadata['access_restrictions'] = self._generate_access_restrictions(isolation_level)
            
        if isolation_level >= 3:
            # Level 3: Apply content obfuscation for cross-boundary access
            isolated_ctx.metadata['obfuscated_preview'] = self._create_obfuscated_preview(ctx.content)
            
        return isolated_ctx
        
    def _generate_access_restrictions(self, isolation_level: int) -> Dict[str, Any]:
        """Generate access restrictions based on isolation level"""
        restrictions = {
            'min_clearance_level': isolation_level,
            'allowed_operations': ['read'] if isolation_level < 3 else ['metadata_only'],
            'cross_boundary_penalty': isolation_level * 0.1,
            'audit_required': isolation_level >= 2
        }
        
        return restrictions
        
    def _create_obfuscated_preview(self, content: str) -> str:
        """Create obfuscated preview for high-isolation content"""
        # Simple obfuscation - could be enhanced
        words = content.split()
        preview_length = min(20, len(words))
        
        # Keep first few words, obfuscate middle, keep last few
        if preview_length <= 6:
            return f"[ISOLATED CONTENT - {len(words)} words]"
        else:
            start = ' '.join(words[:2])
            end = ' '.join(words[-2:])
            return f"{start} [...{len(words)-4} words isolated...] {end}"
            
    def check_boundary_access(self, requesting_group: str, target_context_id: str) -> bool:
        """Check if cross-boundary access is allowed"""
        # Find which group the target context belongs to
        target_group = None
        for group_id, context_ids in self.isolation_boundaries.items():
            if target_context_id in context_ids:
                target_group = group_id
                break
                
        if not target_group:
            return True  # Unknown context, allow access
            
        if requesting_group == target_group:
            return True  # Same group, allow access
            
        # Cross-boundary access - record and potentially allow
        self.cross_boundary_accesses[f"{requesting_group}->{target_group}"] += 1
        
        # Could implement more sophisticated access control here
        return True  # For now, allow but track
        
    def get_metrics(self) -> Dict[str, Any]:
        """Get ISOLATE strategy metrics"""
        return {
            'isolation_groups': len(self.isolation_boundaries),
            'total_isolated_contexts': sum(len(contexts) for contexts in self.isolation_boundaries.values()),
            'cross_boundary_accesses': dict(self.cross_boundary_accesses),
            'average_group_size': np.mean([len(contexts) for contexts in self.isolation_boundaries.values()]) if self.isolation_boundaries and NUMPY_AVAILABLE else 0
        }

class ContextEngineering:
    """
    Main Context Engineering Runtime implementing all four strategies
    Coordinates WRITE/SELECT/COMPRESS/ISOLATE for optimal context management
    """
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.db_path = self.base_path / "tools" / "semantic-context" / "context_runtime.db"
        
        # Initialize strategies
        self.write_strategy = WriteStrategy(self.db_path)
        self.select_strategy = SelectStrategy()
        self.compress_strategy = CompressStrategy()
        self.isolate_strategy = IsolateStrategy()
        
        # Runtime configuration
        self.strategy_weights = {
            ContextStrategy.WRITE: 1.0,
            ContextStrategy.SELECT: 1.0,
            ContextStrategy.COMPRESS: 0.8,
            ContextStrategy.ISOLATE: 0.9
        }
        
        # Performance tracking
        self.execution_history = deque(maxlen=1000)
        self.performance_metrics = defaultdict(float)
        
        self.logger = logging.getLogger(__name__)
        
    def engineer_context(self, contexts: List[ContextItem], 
                        strategies: List[ContextStrategy],
                        params: Dict[str, Any]) -> Tuple[List[ContextItem], Dict[str, Any]]:
        """
        Apply context engineering strategies in optimal order
        Returns engineered contexts and execution metrics
        """
        start_time = time.time()
        execution_id = f"exec_{int(start_time)}"
        
        # Initialize execution tracking
        execution_log = {
            'execution_id': execution_id,
            'input_contexts': len(contexts),
            'strategies_applied': [],
            'performance_metrics': {},
            'start_time': start_time
        }
        
        current_contexts = contexts.copy()
        
        # Apply strategies in research-backed optimal order
        strategy_order = self._optimize_strategy_order(strategies, params)
        
        for strategy in strategy_order:
            strategy_start = time.time()
            
            try:
                if strategy == ContextStrategy.WRITE:
                    current_contexts = self.write_strategy.apply(current_contexts, params)
                elif strategy == ContextStrategy.SELECT:
                    current_contexts = self.select_strategy.apply(current_contexts, params)
                elif strategy == ContextStrategy.COMPRESS:
                    current_contexts = self.compress_strategy.apply(current_contexts, params)
                elif strategy == ContextStrategy.ISOLATE:
                    current_contexts = self.isolate_strategy.apply(current_contexts, params)
                    
                strategy_time = time.time() - strategy_start
                execution_log['strategies_applied'].append({
                    'strategy': strategy.value,
                    'execution_time': strategy_time,
                    'contexts_after': len(current_contexts)
                })
                
            except Exception as e:
                self.logger.error(f"Error applying {strategy.value} strategy: {e}")
                execution_log['strategies_applied'].append({
                    'strategy': strategy.value,
                    'error': str(e),
                    'execution_time': time.time() - strategy_start
                })
                
        # Finalize execution metrics
        total_time = time.time() - start_time
        execution_log.update({
            'total_execution_time': total_time,
            'output_contexts': len(current_contexts),
            'efficiency_ratio': len(current_contexts) / len(contexts) if contexts else 1.0,
            'completed_at': datetime.now().isoformat()
        })
        
        # Store execution history
        self.execution_history.append(execution_log)
        self._update_performance_metrics(execution_log)
        
        self.logger.info(f"Context engineering complete: {len(contexts)} -> {len(current_contexts)} contexts in {total_time:.3f}s")
        
        return current_contexts, execution_log
        
    def _optimize_strategy_order(self, strategies: List[ContextStrategy], 
                               params: Dict[str, Any]) -> List[ContextStrategy]:
        """Optimize strategy execution order based on context and parameters"""
        # Research-backed optimal order for most scenarios
        optimal_order = [
            ContextStrategy.WRITE,    # First: Create structured state
            ContextStrategy.ISOLATE,  # Second: Apply isolation boundaries
            ContextStrategy.SELECT,   # Third: Select relevant contexts
            ContextStrategy.COMPRESS  # Last: Compress selected contexts
        ]
        
        # Filter to only requested strategies in optimal order
        return [s for s in optimal_order if s in strategies]
        
    def _update_performance_metrics(self, execution_log: Dict[str, Any]):
        """Update overall performance metrics"""
        self.performance_metrics['total_executions'] += 1
        self.performance_metrics['total_execution_time'] += execution_log['total_execution_time']
        self.performance_metrics['average_execution_time'] = (
            self.performance_metrics['total_execution_time'] / 
            self.performance_metrics['total_executions']
        )
        
        # Update efficiency metrics
        efficiency = execution_log.get('efficiency_ratio', 1.0)
        self.performance_metrics['total_efficiency'] += efficiency
        self.performance_metrics['average_efficiency'] = (
            self.performance_metrics['total_efficiency'] / 
            self.performance_metrics['total_executions']
        )
        
    def get_comprehensive_metrics(self) -> Dict[str, Any]:
        """Get comprehensive metrics from all strategies and runtime"""
        return {
            'runtime_metrics': dict(self.performance_metrics),
            'write_strategy_metrics': self.write_strategy.get_metrics(),
            'select_strategy_metrics': self.select_strategy.get_metrics(),
            'compress_strategy_metrics': self.compress_strategy.get_metrics(),
            'isolate_strategy_metrics': self.isolate_strategy.get_metrics(),
            'execution_history_size': len(self.execution_history),
            'average_strategies_per_execution': np.mean([len(exec_log.get('strategies_applied', [])) for exec_log in self.execution_history]) if self.execution_history and NUMPY_AVAILABLE else 0
        }

if __name__ == "__main__":
    # Example usage
    runtime = ContextEngineering()
    
    # Create test contexts
    test_contexts = [
        ContextItem(
            id="test_1",
            content="This is a test context for demonstrating the context engineering runtime",
            context_type="test",
            memory_type=MemoryType.WORKING,
            priority=1.0,
            timestamp=datetime.now().isoformat()
        ),
        ContextItem(
            id="test_2", 
            content="Another test context with different memory type and priority",
            context_type="test",
            memory_type=MemoryType.EPISODIC,
            priority=0.5,
            timestamp=(datetime.now() - timedelta(hours=2)).isoformat()
        )
    ]
    
    # Apply all strategies
    strategies = [ContextStrategy.WRITE, ContextStrategy.SELECT, ContextStrategy.COMPRESS, ContextStrategy.ISOLATE]
    params = {
        'session_id': 'test_session',
        'query_context': 'test demonstration',
        'max_contexts': 10,
        'target_compression': 0.8
    }
    
    engineered_contexts, execution_log = runtime.engineer_context(test_contexts, strategies, params)
    
    print(f"Engineered {len(engineered_contexts)} contexts from {len(test_contexts)} originals")
    print(f"Execution time: {execution_log['total_execution_time']:.3f}s")
    
    # Show comprehensive metrics
    metrics = runtime.get_comprehensive_metrics()
    print(f"Runtime metrics: {metrics['runtime_metrics']}")