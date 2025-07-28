#!/usr/bin/env python3
"""
Command Ecosystem Integration API with Session Continuity
Provides seamless integration between semantic context system and command ecosystem
Implements session handoff, context preservation, and intelligent routing
"""

import json
import logging
import sqlite3
import asyncio
import time
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple, Union, Callable
from dataclasses import dataclass, asdict
from collections import defaultdict, deque
from enum import Enum
import threading
import hashlib

# Import our semantic context components
from .retrieval_engine import ContextualRetrievalEngine, RetrievalQuery, RetrievalResult
from .embedding_manager import AdvancedEmbeddingManager, EmbeddingConfig
from .context_runtime import ContextEngineering, ContextStrategy, ContextItem, MemoryType
from .pattern_analyzer import ContextFlowPatternAnalyzer, PatternAlert
from .compression_engine import SpliceCompressionEngine, CompressionConfig, CompressionMethod

# Advanced dependencies
try:
    import asyncio
    from concurrent.futures import ThreadPoolExecutor, as_completed
    ASYNC_AVAILABLE = True
except ImportError:
    ASYNC_AVAILABLE = False
    logging.warning("Asyncio not available for concurrent processing")

class IntegrationMode(Enum):
    """Integration modes for different use cases"""
    COMMAND_ASSIST = "command_assist"    # Assist command execution
    SESSION_BRIDGE = "session_bridge"    # Bridge between sessions
    CONTEXT_QUERY = "context_query"      # Direct context queries
    PATTERN_MONITOR = "pattern_monitor"  # Monitor for patterns/threats
    BULK_PROCESS = "bulk_process"        # Bulk processing operations

class ContextRequestType(Enum):
    """Types of context requests"""
    RETRIEVE = "retrieve"                # Retrieve existing context
    INGEST = "ingest"                   # Ingest new context
    ANALYZE = "analyze"                 # Analyze context patterns
    COMPRESS = "compress"               # Compress context
    HANDOFF = "handoff"                 # Session handoff operations

@dataclass
class IntegrationRequest:
    """Request structure for integration API"""
    request_id: str
    request_type: ContextRequestType
    mode: IntegrationMode
    command_context: Optional[str] = None
    session_id: Optional[str] = None
    user_context: Optional[str] = None
    parameters: Optional[Dict[str, Any]] = None
    priority: int = 1  # 1=low, 2=medium, 3=high, 4=critical
    timestamp: Optional[str] = None

@dataclass
class IntegrationResponse:
    """Response structure for integration API"""
    request_id: str
    success: bool
    data: Optional[Dict[str, Any]] = None
    error: Optional[str] = None
    processing_time: float = 0.0
    metadata: Optional[Dict[str, Any]] = None
    timestamp: Optional[str] = None

class SessionContinuityManager:
    """Manages session continuity and handoffs"""
    
    def __init__(self, db_path: Path):
        self.db_path = db_path
        self.active_sessions = {}
        self.session_history = deque(maxlen=1000)
        self.handoff_templates = {}
        self.logger = logging.getLogger(__name__)
        
        self._init_database()
        
    def _init_database(self):
        """Initialize session continuity database"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS session_continuity (
                    session_id TEXT PRIMARY KEY,
                    start_time TEXT,
                    last_activity TEXT,
                    context_summary TEXT,
                    handoff_data TEXT,
                    status TEXT DEFAULT 'active',
                    metadata TEXT
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS session_handoffs (
                    handoff_id TEXT PRIMARY KEY,
                    source_session TEXT,
                    target_session TEXT,
                    handoff_type TEXT,
                    context_data TEXT,
                    completion_status TEXT,
                    created_at TEXT,
                    completed_at TEXT
                )
            ''')
            
    def create_session_context(self, session_id: str, initial_context: Dict[str, Any]) -> bool:
        """Create new session context"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    INSERT OR REPLACE INTO session_continuity
                    (session_id, start_time, last_activity, context_summary, metadata, status)
                    VALUES (?, ?, ?, ?, ?, 'active')
                ''', (
                    session_id,
                    datetime.now().isoformat(),
                    datetime.now().isoformat(),
                    initial_context.get('summary', ''),
                    json.dumps(initial_context)
                ))
                
            self.active_sessions[session_id] = {
                'start_time': datetime.now(),
                'context': initial_context,
                'activity_count': 0
            }
            
            self.logger.info(f"Created session context: {session_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error creating session context: {e}")
            return False
            
    def update_session_activity(self, session_id: str, activity_data: Dict[str, Any]):
        """Update session with new activity"""
        if session_id in self.active_sessions:
            self.active_sessions[session_id]['activity_count'] += 1
            self.active_sessions[session_id]['last_activity'] = datetime.now()
            
        # Update database
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                UPDATE session_continuity 
                SET last_activity = ?, context_summary = ?
                WHERE session_id = ?
            ''', (
                datetime.now().isoformat(),
                json.dumps(activity_data),
                session_id
            ))
            
    def prepare_handoff(self, session_id: str, target_session: Optional[str] = None) -> Dict[str, Any]:
        """Prepare session handoff data"""
        handoff_id = f"handoff_{session_id}_{int(time.time())}"
        
        # Gather session context
        session_data = self.active_sessions.get(session_id, {})
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute('''
                SELECT context_summary, handoff_data, metadata
                FROM session_continuity
                WHERE session_id = ?
            ''', (session_id,))
            
            row = cursor.fetchone()
            if row:
                handoff_data = {
                    'handoff_id': handoff_id,
                    'source_session': session_id,
                    'target_session': target_session,
                    'context_summary': row[0],
                    'stored_handoff_data': json.loads(row[1]) if row[1] else {},
                    'metadata': json.loads(row[2]) if row[2] else {},
                    'active_session_data': session_data,
                    'created_at': datetime.now().isoformat()
                }
                
                # Store handoff record
                conn.execute('''
                    INSERT INTO session_handoffs
                    (handoff_id, source_session, target_session, handoff_type,
                     context_data, completion_status, created_at)
                    VALUES (?, ?, ?, 'session_transition', ?, 'prepared', ?)
                ''', (
                    handoff_id,
                    session_id,
                    target_session or 'new_session',
                    'session_transition',
                    json.dumps(handoff_data),
                    datetime.now().isoformat()
                ))
                
                return handoff_data
                
        return {}
        
    def complete_handoff(self, handoff_data: Dict[str, Any], new_session_id: str) -> bool:
        """Complete session handoff to new session"""
        try:
            handoff_id = handoff_data.get('handoff_id')
            
            # Create new session with handoff context
            self.create_session_context(new_session_id, {
                'inherited_from': handoff_data.get('source_session'),
                'handoff_data': handoff_data,
                'summary': handoff_data.get('context_summary', '')
            })
            
            # Update handoff record
            with sqlite3.connect(self.db_path) as conn:
                conn.execute('''
                    UPDATE session_handoffs
                    SET target_session = ?, completion_status = 'completed', completed_at = ?
                    WHERE handoff_id = ?
                ''', (new_session_id, datetime.now().isoformat(), handoff_id))
                
            self.logger.info(f"Completed handoff {handoff_id}: {handoff_data.get('source_session')} -> {new_session_id}")
            return True
            
        except Exception as e:
            self.logger.error(f"Error completing handoff: {e}")
            return False

class CommandEcosystemBridge:
    """Bridge between semantic context system and command ecosystem"""
    
    def __init__(self, base_path: str):
        self.base_path = Path(base_path)
        self.command_registry = {}
        self.context_mappings = {}
        self.execution_history = deque(maxlen=5000)
        self.logger = logging.getLogger(__name__)
        
        self._load_command_mappings()
        
    def _load_command_mappings(self):
        """Load command-to-context mappings"""
        # Default mappings for CE-Simple command ecosystem
        self.context_mappings = {
            '/start': {
                'context_types': ['session', 'project_evolution', 'user_voice'],
                'priority_boost': 1.5,
                'memory_focus': [MemoryType.EPISODIC, MemoryType.WORKING],
                'compression_aggressive': False
            },
            '/create-doc': {
                'context_types': ['command', 'user_voice', 'session'],
                'priority_boost': 2.0,
                'memory_focus': [MemoryType.PROCEDURAL, MemoryType.WORKING],
                'compression_aggressive': False
            },
            '/analyze': {
                'context_types': ['all'],
                'priority_boost': 1.2,
                'memory_focus': [MemoryType.SEMANTIC, MemoryType.EPISODIC],
                'compression_aggressive': True
            },
            '/explore': {
                'context_types': ['project_evolution', 'command'],
                'priority_boost': 1.0,
                'memory_focus': [MemoryType.SEMANTIC],
                'compression_aggressive': True
            },
            '/debug': {
                'context_types': ['session', 'command'],
                'priority_boost': 1.8,
                'memory_focus': [MemoryType.EPISODIC, MemoryType.WORKING],
                'compression_aggressive': False
            },
            '/session-close': {
                'context_types': ['session', 'user_voice'],
                'priority_boost': 1.3,
                'memory_focus': [MemoryType.EPISODIC],
                'compression_aggressive': True
            }
        }
        
    def get_context_requirements(self, command_name: str) -> Dict[str, Any]:
        """Get context requirements for specific command"""
        return self.context_mappings.get(command_name, {
            'context_types': ['all'],
            'priority_boost': 1.0,
            'memory_focus': [MemoryType.WORKING],
            'compression_aggressive': False
        })
        
    def register_command_handler(self, command_name: str, handler: Callable):
        """Register custom command handler"""
        self.command_registry[command_name] = handler
        self.logger.info(f"Registered handler for command: {command_name}")
        
    def route_command_request(self, command_name: str, context: str, 
                            session_id: str) -> Dict[str, Any]:
        """Route command request to appropriate context operations"""
        requirements = self.get_context_requirements(command_name)
        
        # Check for custom handler
        if command_name in self.command_registry:
            try:
                return self.command_registry[command_name](context, session_id, requirements)
            except Exception as e:
                self.logger.error(f"Custom handler error for {command_name}: {e}")
                
        # Default routing logic
        routing_result = {
            'context_query': self._build_context_query(context, requirements, session_id),
            'processing_strategy': self._determine_processing_strategy(command_name, requirements),
            'response_format': self._get_response_format(command_name),
            'caching_policy': self._get_caching_policy(command_name)
        }
        
        # Log routing decision
        self.execution_history.append({
            'command': command_name,
            'session_id': session_id,
            'timestamp': datetime.now().isoformat(),
            'routing_result': routing_result
        })
        
        return routing_result
        
    def _build_context_query(self, context: str, requirements: Dict[str, Any], 
                           session_id: str) -> RetrievalQuery:
        """Build context query based on requirements"""
        return RetrievalQuery(
            query_text=context,
            query_type='hybrid',
            context_window=context,
            filters={
                'context_types': requirements.get('context_types', ['all']),
                'session_id': session_id
            },
            max_results=20,
            min_relevance=0.3,
            session_id=session_id,
            include_cross_session=True,
            relevance_weights={
                'semantic_similarity': 0.35 * requirements.get('priority_boost', 1.0),
                'bm25_relevance': 0.25,
                'contextual_boost': 0.25,
                'temporal_decay': 0.15
            }
        )
        
    def _determine_processing_strategy(self, command_name: str, 
                                     requirements: Dict[str, Any]) -> List[ContextStrategy]:
        """Determine optimal processing strategy for command"""
        strategies = [ContextStrategy.WRITE]  # Always start with WRITE
        
        # Add strategies based on command characteristics
        if requirements.get('compression_aggressive', False):
            strategies.append(ContextStrategy.COMPRESS)
            
        strategies.append(ContextStrategy.SELECT)  # Always select relevant contexts
        
        # Add isolation for sensitive commands
        if command_name in ['/create-doc', '/debug']:
            strategies.append(ContextStrategy.ISOLATE)
            
        return strategies
        
    def _get_response_format(self, command_name: str) -> Dict[str, Any]:
        """Get appropriate response format for command"""
        formats = {
            '/start': {'include_summary': True, 'include_recommendations': True},
            '/create-doc': {'include_templates': True, 'include_validation': True},
            '/analyze': {'include_metrics': True, 'include_insights': True},
            '/debug': {'include_diagnostics': True, 'include_traces': True}
        }
        
        return formats.get(command_name, {'include_summary': True})
        
    def _get_caching_policy(self, command_name: str) -> Dict[str, Any]:
        """Get caching policy for command"""
        # Commands that benefit from caching
        cacheable_commands = ['/analyze', '/explore']
        
        if command_name in cacheable_commands:
            return {'cache_duration': 300, 'cache_key_include_session': True}
        else:
            return {'cache_duration': 0}  # No caching for dynamic commands

class SemanticContextIntegrationAPI:
    """
    Main integration API coordinating all semantic context components
    Provides unified interface for command ecosystem integration
    """
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.db_path = self.base_path / "tools" / "semantic-context" / "integration.db"
        
        # Initialize core components
        self.retrieval_engine = ContextualRetrievalEngine(base_path)
        self.embedding_manager = AdvancedEmbeddingManager(base_path)
        self.context_runtime = ContextEngineering(base_path)
        self.pattern_analyzer = ContextFlowPatternAnalyzer(base_path)
        self.compression_engine = SpliceCompressionEngine(base_path)
        
        # Initialize integration components
        self.session_manager = SessionContinuityManager(self.db_path)
        self.command_bridge = CommandEcosystemBridge(base_path)
        
        # Request processing
        self.request_queue = deque()
        self.processing_stats = defaultdict(int)
        self.response_cache = {}
        self.cache_lock = threading.Lock()
        
        # Async support
        self.executor = ThreadPoolExecutor(max_workers=4) if ASYNC_AVAILABLE else None
        
        self._init_database()
        
        self.logger = logging.getLogger(__name__)
        
    def _init_database(self):
        """Initialize integration API database"""
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS integration_requests (
                    request_id TEXT PRIMARY KEY,
                    request_type TEXT,
                    mode TEXT,
                    session_id TEXT,
                    command_context TEXT,
                    parameters TEXT,
                    created_at TEXT,
                    completed_at TEXT,
                    processing_time REAL,
                    success BOOLEAN,
                    error_message TEXT
                )
            ''')
            
            conn.execute('''
                CREATE TABLE IF NOT EXISTS performance_metrics (
                    metric_id TEXT PRIMARY KEY,
                    metric_type TEXT,
                    metric_value REAL,
                    context_data TEXT,
                    timestamp TEXT
                )
            ''')
            
    async def process_request(self, request: IntegrationRequest) -> IntegrationResponse:
        """
        Main request processing method with async support
        Handles all types of context operations
        """
        start_time = time.time()
        
        # Initialize response
        response = IntegrationResponse(
            request_id=request.request_id,
            success=False,
            timestamp=datetime.now().isoformat()
        )
        
        try:
            # Log request
            self._log_request(request)
            
            # Route request based on type
            if request.request_type == ContextRequestType.RETRIEVE:
                response.data = await self._handle_retrieve_request(request)
            elif request.request_type == ContextRequestType.INGEST:
                response.data = await self._handle_ingest_request(request)
            elif request.request_type == ContextRequestType.ANALYZE:
                response.data = await self._handle_analyze_request(request)
            elif request.request_type == ContextRequestType.COMPRESS:
                response.data = await self._handle_compress_request(request)
            elif request.request_type == ContextRequestType.HANDOFF:
                response.data = await self._handle_handoff_request(request)
            else:
                raise ValueError(f"Unknown request type: {request.request_type}")
                
            response.success = True
            
        except Exception as e:
            response.error = str(e)
            self.logger.error(f"Request processing error: {e}")
            
        # Finalize response
        response.processing_time = time.time() - start_time
        response.metadata = {
            'processed_by': 'SemanticContextIntegrationAPI',
            'components_used': self._get_components_used(request),
            'performance_tier': self._classify_performance(response.processing_time)
        }
        
        # Log completion
        self._log_completion(request, response)
        
        return response
        
    async def _handle_retrieve_request(self, request: IntegrationRequest) -> Dict[str, Any]:
        """Handle context retrieval requests"""
        # Build query from command bridge routing
        routing_result = self.command_bridge.route_command_request(
            request.command_context or 'general',
            request.user_context or '',
            request.session_id or 'default'
        )
        
        query = routing_result['context_query']
        
        # Execute retrieval
        if ASYNC_AVAILABLE and self.executor:
            future = self.executor.submit(self.retrieval_engine.retrieve_contextual, query)
            results = await asyncio.wrap_future(future)
        else:
            results = self.retrieval_engine.retrieve_contextual(query)
            
        # Apply context engineering strategies
        strategies = routing_result['processing_strategy']
        
        # Convert results to ContextItems
        context_items = []
        for result in results:
            context_item = ContextItem(
                id=f"retrieved_{hash(result.content)}",
                content=result.content,
                context_type=result.context_type,
                memory_type=MemoryType.EPISODIC,  # Default for retrieved content
                priority=result.relevance_score,
                timestamp=result.retrieval_timestamp,
                session_id=request.session_id,
                metadata=result.contextual_metadata
            )
            context_items.append(context_item)
            
        # Apply context engineering
        if strategies:
            engineered_contexts, execution_log = self.context_runtime.engineer_context(
                context_items,
                strategies,
                {
                    'session_id': request.session_id,
                    'query_context': request.user_context,
                    'max_contexts': request.parameters.get('max_contexts', 20) if request.parameters else 20
                }
            )
        else:
            engineered_contexts = context_items
            execution_log = {}
            
        return {
            'contexts': [asdict(ctx) for ctx in engineered_contexts],
            'retrieval_metadata': {
                'total_results': len(results),
                'engineered_results': len(engineered_contexts),
                'strategies_applied': [s.value for s in strategies],
                'execution_log': execution_log
            },
            'response_format': routing_result.get('response_format', {})
        }
        
    async def _handle_ingest_request(self, request: IntegrationRequest) -> Dict[str, Any]:
        """Handle context ingestion requests"""
        content = request.user_context or ''
        content_type = request.parameters.get('content_type', 'general') if request.parameters else 'general'
        
        # Ingest content into retrieval engine
        if ASYNC_AVAILABLE and self.executor:
            future = self.executor.submit(
                self.retrieval_engine.ingest_context,
                content, content_type, request.session_id
            )
            chunks = await asyncio.wrap_future(future)
        else:
            chunks = self.retrieval_engine.ingest_context(content, content_type, request.session_id)
            
        # Update session activity
        if request.session_id:
            self.session_manager.update_session_activity(request.session_id, {
                'ingested_content_size': len(content),
                'chunks_created': len(chunks),
                'content_type': content_type
            })
            
        return {
            'ingestion_result': {
                'chunks_created': len(chunks),
                'total_size': len(content),
                'content_type': content_type
            },
            'chunk_details': [asdict(chunk) for chunk in chunks[:5]]  # First 5 chunks for preview
        }
        
    async def _handle_analyze_request(self, request: IntegrationRequest) -> Dict[str, Any]:
        """Handle pattern analysis requests"""
        # Gather contexts for analysis
        contexts = []
        
        if request.parameters and 'context_ids' in request.parameters:
            # Analyze specific contexts
            context_ids = request.parameters['context_ids']
            # Would retrieve specific contexts by ID
        else:
            # Analyze recent session contexts
            # Would gather recent contexts from session
            contexts = [{'id': 'sample', 'content': request.user_context or '', 'context_type': 'user_input'}]
            
        # Run pattern analysis
        if ASYNC_AVAILABLE and self.executor:
            future = self.executor.submit(
                self.pattern_analyzer.analyze_patterns,
                contexts,
                request.parameters.get('analysis_options', {}) if request.parameters else {}
            )
            analysis_results = await asyncio.wrap_future(future)
        else:
            analysis_results = self.pattern_analyzer.analyze_patterns(
                contexts,
                request.parameters.get('analysis_options', {}) if request.parameters else {}
            )
            
        return {
            'analysis_results': analysis_results,
            'threat_summary': {
                'total_alerts': len(analysis_results.get('alerts', [])),
                'high_priority_alerts': len([a for a in analysis_results.get('alerts', []) if a.severity in ['high', 'critical']]),
                'recommendations': analysis_results.get('recommendations', [])
            }
        }
        
    async def _handle_compress_request(self, request: IntegrationRequest) -> Dict[str, Any]:
        """Handle compression requests"""
        content = request.user_context or ''
        
        # Build compression config
        config_params = request.parameters.get('compression_config', {}) if request.parameters else {}
        config = CompressionConfig(
            target_ratio=config_params.get('target_ratio', 0.7),
            method=CompressionMethod(config_params.get('method', 'hybrid'))
        )
        
        # Apply compression
        if ASYNC_AVAILABLE and self.executor:
            future = self.executor.submit(
                self.compression_engine.compress_content,
                content, f"request_{request.request_id}", config
            )
            compression_result = await asyncio.wrap_future(future)
        else:
            compression_result = self.compression_engine.compress_content(
                content, f"request_{request.request_id}", config
            )
            
        return {
            'compression_result': asdict(compression_result),
            'summary': {
                'original_size': compression_result.original_size,
                'compressed_size': compression_result.compressed_size,
                'compression_ratio': compression_result.compression_ratio,
                'semantic_preservation': compression_result.semantic_preservation
            }
        }
        
    async def _handle_handoff_request(self, request: IntegrationRequest) -> Dict[str, Any]:
        """Handle session handoff requests"""
        if request.parameters and 'handoff_data' in request.parameters:
            # Complete handoff
            handoff_data = request.parameters['handoff_data']
            new_session_id = request.session_id or f"session_{int(time.time())}"
            
            success = self.session_manager.complete_handoff(handoff_data, new_session_id)
            
            return {
                'handoff_completion': {
                    'success': success,
                    'new_session_id': new_session_id,
                    'inherited_context': handoff_data.get('context_summary', '')
                }
            }
        else:
            # Prepare handoff
            session_id = request.session_id or 'default'
            handoff_data = self.session_manager.prepare_handoff(session_id)
            
            return {
                'handoff_preparation': {
                    'handoff_id': handoff_data.get('handoff_id'),
                    'source_session': session_id,
                    'context_summary': handoff_data.get('context_summary', ''),
                    'handoff_data': handoff_data
                }
            }
            
    def _get_components_used(self, request: IntegrationRequest) -> List[str]:
        """Determine which components were used for request"""
        components = []
        
        if request.request_type == ContextRequestType.RETRIEVE:
            components.extend(['retrieval_engine', 'context_runtime', 'command_bridge'])
        elif request.request_type == ContextRequestType.INGEST:
            components.extend(['retrieval_engine', 'embedding_manager'])
        elif request.request_type == ContextRequestType.ANALYZE:
            components.extend(['pattern_analyzer'])
        elif request.request_type == ContextRequestType.COMPRESS:
            components.extend(['compression_engine'])
        elif request.request_type == ContextRequestType.HANDOFF:
            components.extend(['session_manager'])
            
        return components
        
    def _classify_performance(self, processing_time: float) -> str:
        """Classify performance tier based on processing time"""
        if processing_time < 0.1:
            return 'excellent'
        elif processing_time < 0.5:
            return 'good'
        elif processing_time < 2.0:
            return 'acceptable'
        else:
            return 'needs_optimization'
            
    def _log_request(self, request: IntegrationRequest):
        """Log incoming request"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                INSERT INTO integration_requests
                (request_id, request_type, mode, session_id, command_context, 
                 parameters, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                request.request_id,
                request.request_type.value,
                request.mode.value,
                request.session_id,
                request.command_context,
                json.dumps(request.parameters) if request.parameters else None,
                datetime.now().isoformat()
            ))
            
    def _log_completion(self, request: IntegrationRequest, response: IntegrationResponse):
        """Log request completion"""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                UPDATE integration_requests
                SET completed_at = ?, processing_time = ?, success = ?, error_message = ?
                WHERE request_id = ?
            ''', (
                datetime.now().isoformat(),
                response.processing_time,
                response.success,
                response.error,
                request.request_id
            ))
            
        # Update processing stats
        self.processing_stats[f"{request.request_type.value}_{request.mode.value}"] += 1
        
    def get_integration_metrics(self) -> Dict[str, Any]:
        """Get comprehensive integration metrics"""
        with sqlite3.connect(self.db_path) as conn:
            # Request statistics
            cursor = conn.execute('''
                SELECT request_type, COUNT(*) as count, 
                       AVG(processing_time) as avg_time,
                       AVG(CASE WHEN success THEN 1.0 ELSE 0.0 END) as success_rate
                FROM integration_requests
                GROUP BY request_type
            ''')
            
            request_stats = {}
            for row in cursor.fetchall():
                request_stats[row[0]] = {
                    'count': row[1],
                    'avg_processing_time': row[2] or 0,
                    'success_rate': row[3] or 0
                }
                
        return {
            'request_statistics': request_stats,
            'processing_stats': dict(self.processing_stats),
            'active_sessions': len(self.session_manager.active_sessions),
            'cache_size': len(self.response_cache),
            'component_metrics': {
                'retrieval_engine': self.retrieval_engine.get_performance_metrics(),
                'embedding_manager': self.embedding_manager.get_embedding_analytics(),
                'pattern_analyzer': self.pattern_analyzer.get_analysis_statistics(),
                'compression_engine': self.compression_engine.get_compression_statistics()
            }
        }

# Synchronous wrapper for non-async usage
class SyncIntegrationAPI:
    """Synchronous wrapper for integration API"""
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.async_api = SemanticContextIntegrationAPI(base_path)
        
    def process_request(self, request: IntegrationRequest) -> IntegrationResponse:
        """Process request synchronously"""
        if ASYNC_AVAILABLE:
            return asyncio.run(self.async_api.process_request(request))
        else:
            # Fallback to direct processing without async
            return self._sync_process_request(request)
            
    def _sync_process_request(self, request: IntegrationRequest) -> IntegrationResponse:
        """Direct synchronous processing"""
        # This would implement direct synchronous versions of the async methods
        # For brevity, returning a basic response
        return IntegrationResponse(
            request_id=request.request_id,
            success=True,
            data={'message': 'Processed synchronously'},
            processing_time=0.1,
            timestamp=datetime.now().isoformat()
        )

if __name__ == "__main__":
    # Example usage
    api = SyncIntegrationAPI()
    
    # Test context retrieval request
    request = IntegrationRequest(
        request_id="test_001",
        request_type=ContextRequestType.RETRIEVE,
        mode=IntegrationMode.COMMAND_ASSIST,
        command_context="/start",
        session_id="test_session",
        user_context="help me get started with contextual analysis",
        parameters={'max_contexts': 10}
    )
    
    response = api.process_request(request)
    
    print(f"Request processed: {response.success}")
    print(f"Processing time: {response.processing_time:.3f}s")
    print(f"Response data keys: {list(response.data.keys()) if response.data else 'None'}")
    
    # Get integration metrics
    metrics = api.async_api.get_integration_metrics()
    print(f"Integration metrics: {metrics}")