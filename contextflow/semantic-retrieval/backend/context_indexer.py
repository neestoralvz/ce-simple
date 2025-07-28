#!/usr/bin/env python3
"""
Semantic Context Indexer - Core Backend Component
Indexes command history, user voice data, cross-session continuity, and project evolution insights
"""

import json
import pickle
import hashlib
import logging
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from collections import defaultdict
import sqlite3
import numpy as np

# Vector embeddings for semantic similarity
try:
    from sentence_transformers import SentenceTransformer
    EMBEDDINGS_AVAILABLE = True
except ImportError:
    EMBEDDINGS_AVAILABLE = False
    logging.warning("sentence-transformers not available. Using fallback similarity methods.")

@dataclass
class ContextItem:
    """Core context item structure"""
    id: str
    content: str
    context_type: str  # 'command', 'user_voice', 'session', 'project_evolution'
    timestamp: str
    session_id: Optional[str] = None
    command_context: Optional[str] = None
    user_intent: Optional[str] = None
    embedding: Optional[List[float]] = None
    metadata: Optional[Dict[str, Any]] = None
    relevance_score: float = 0.0
    cross_references: Optional[List[str]] = None

class SemanticContextIndexer:
    """
    Production-ready semantic context indexing system
    Handles indexing, storage, and retrieval of contextflow patterns
    """
    
    def __init__(self, base_path: str = "/Users/nalve/ce-simple"):
        self.base_path = Path(base_path)
        self.context_db_path = self.base_path / "contextflow" / "semantic-retrieval" / "context.db"
        self.embeddings_cache_path = self.base_path / "contextflow" / "semantic-retrieval" / "embeddings.pkl"
        
        # Initialize embedding model
        if EMBEDDINGS_AVAILABLE:
            self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        else:
            self.embedding_model = None
            
        # Initialize database
        self._init_database()
        
        # Context sources configuration
        self.context_sources = {
            'commands': self.base_path / ".claude" / "commands",
            'narratives': self.base_path / "narratives",
            'handoffs': self.base_path / "handoff",
            'user_voice': self.base_path / "data" / "user-voice-preservation",
            'git_metrics': self.base_path / "data" / "git-metrics",
            'performance': self.base_path / "data" / "performance-metrics"
        }
        
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        
    def _init_database(self):
        """Initialize SQLite database for context storage"""
        self.context_db_path.parent.mkdir(parents=True, exist_ok=True)
        
        with sqlite3.connect(self.context_db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS context_items (
                    id TEXT PRIMARY KEY,
                    content TEXT NOT NULL,
                    context_type TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    session_id TEXT,
                    command_context TEXT,
                    user_intent TEXT,
                    relevance_score REAL DEFAULT 0.0,
                    metadata TEXT,
                    cross_references TEXT,
                    embedding_hash TEXT,
                    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
                    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_context_type ON context_items(context_type)
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_timestamp ON context_items(timestamp)
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_session_id ON context_items(session_id)
            ''')
            
            conn.execute('''
                CREATE INDEX IF NOT EXISTS idx_relevance_score ON context_items(relevance_score)
            ''')
            
    def _generate_embedding(self, text: str) -> Optional[List[float]]:
        """Generate semantic embedding for text"""
        if not self.embedding_model:
            return None
            
        try:
            embedding = self.embedding_model.encode(text, convert_to_tensor=False)
            return embedding.tolist()
        except Exception as e:
            self.logger.error(f"Error generating embedding: {e}")
            return None
            
    def _calculate_text_hash(self, text: str) -> str:
        """Calculate hash for text content"""
        return hashlib.sha256(text.encode()).hexdigest()[:16]
        
    def index_command_history(self) -> List[ContextItem]:
        """Index command files and their patterns"""
        indexed_items = []
        commands_path = self.context_sources['commands']
        
        if not commands_path.exists():
            self.logger.warning(f"Commands path not found: {commands_path}")
            return indexed_items
            
        for command_file in commands_path.rglob("*.md"):
            try:
                content = command_file.read_text()
                
                # Extract command metadata
                command_name = command_file.stem
                command_path = str(command_file.relative_to(commands_path))
                
                # Create context item
                context_item = ContextItem(
                    id=f"cmd_{self._calculate_text_hash(command_path)}",
                    content=content,
                    context_type="command",
                    timestamp=datetime.now().isoformat(),
                    command_context=command_path,
                    metadata={
                        "command_name": command_name,
                        "file_path": str(command_file),
                        "file_size": len(content),
                        "last_modified": datetime.fromtimestamp(command_file.stat().st_mtime).isoformat()
                    }
                )
                
                # Generate embedding
                context_item.embedding = self._generate_embedding(content)
                
                # Store in database
                self._store_context_item(context_item)
                indexed_items.append(context_item)
                
            except Exception as e:
                self.logger.error(f"Error indexing command {command_file}: {e}")
                
        self.logger.info(f"Indexed {len(indexed_items)} command files")
        return indexed_items
        
    def index_user_voice_data(self) -> List[ContextItem]:
        """Index user voice preservation data"""
        indexed_items = []
        narratives_path = self.context_sources['narratives']
        
        if not narratives_path.exists():
            self.logger.warning(f"Narratives path not found: {narratives_path}")
            return indexed_items
            
        for narrative_file in narratives_path.rglob("*.md"):
            try:
                content = narrative_file.read_text()
                
                # Extract user voice patterns
                context_item = ContextItem(
                    id=f"voice_{self._calculate_text_hash(str(narrative_file))}",
                    content=content,
                    context_type="user_voice",
                    timestamp=datetime.now().isoformat(),
                    metadata={
                        "file_path": str(narrative_file),
                        "narrative_type": self._classify_narrative(content),
                        "word_count": len(content.split()),
                        "last_modified": datetime.fromtimestamp(narrative_file.stat().st_mtime).isoformat()
                    }
                )
                
                context_item.embedding = self._generate_embedding(content)
                self._store_context_item(context_item)
                indexed_items.append(context_item)
                
            except Exception as e:
                self.logger.error(f"Error indexing narrative {narrative_file}: {e}")
                
        self.logger.info(f"Indexed {len(indexed_items)} user voice items")
        return indexed_items
        
    def index_session_continuity(self) -> List[ContextItem]:
        """Index cross-session continuity information"""
        indexed_items = []
        handoffs_path = self.context_sources['handoffs']
        
        if not handoffs_path.exists():
            self.logger.warning(f"Handoffs path not found: {handoffs_path}")
            return indexed_items
            
        for handoff_file in handoffs_path.rglob("*.md"):
            try:
                content = handoff_file.read_text()
                
                # Extract session metadata
                session_id = self._extract_session_id(handoff_file.name)
                
                context_item = ContextItem(
                    id=f"session_{self._calculate_text_hash(str(handoff_file))}",
                    content=content,
                    context_type="session",
                    timestamp=datetime.now().isoformat(),
                    session_id=session_id,
                    metadata={
                        "file_path": str(handoff_file),
                        "session_type": self._classify_session(content),
                        "handoff_completeness": self._assess_handoff_completeness(content),
                        "last_modified": datetime.fromtimestamp(handoff_file.stat().st_mtime).isoformat()
                    }
                )
                
                context_item.embedding = self._generate_embedding(content)
                self._store_context_item(context_item)
                indexed_items.append(context_item)
                
            except Exception as e:
                self.logger.error(f"Error indexing handoff {handoff_file}: {e}")
                
        self.logger.info(f"Indexed {len(indexed_items)} session continuity items")
        return indexed_items
        
    def index_project_evolution(self) -> List[ContextItem]:
        """Index project evolution insights"""
        indexed_items = []
        
        # Index git metrics
        git_metrics_path = self.context_sources['git_metrics']
        if git_metrics_path.exists():
            for metrics_file in git_metrics_path.rglob("*.json"):
                try:
                    content = metrics_file.read_text()
                    data = json.loads(content)
                    
                    context_item = ContextItem(
                        id=f"evolution_{self._calculate_text_hash(str(metrics_file))}",
                        content=content,
                        context_type="project_evolution",
                        timestamp=datetime.now().isoformat(),
                        metadata={
                            "file_path": str(metrics_file),
                            "metrics_type": metrics_file.stem,
                            "data_points": len(data) if isinstance(data, (list, dict)) else 1,
                            "last_modified": datetime.fromtimestamp(metrics_file.stat().st_mtime).isoformat()
                        }
                    )
                    
                    # Use summary for embedding instead of raw JSON
                    summary = self._generate_metrics_summary(data)
                    context_item.embedding = self._generate_embedding(summary)
                    
                    self._store_context_item(context_item)
                    indexed_items.append(context_item)
                    
                except Exception as e:
                    self.logger.error(f"Error indexing metrics {metrics_file}: {e}")
                    
        self.logger.info(f"Indexed {len(indexed_items)} project evolution items")
        return indexed_items
        
    def _store_context_item(self, item: ContextItem):
        """Store context item in database"""
        with sqlite3.connect(self.context_db_path) as conn:
            conn.execute('''
                INSERT OR REPLACE INTO context_items 
                (id, content, context_type, timestamp, session_id, command_context, 
                 user_intent, relevance_score, metadata, cross_references, embedding_hash)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                item.id,
                item.content,
                item.context_type,
                item.timestamp,
                item.session_id,
                item.command_context,
                item.user_intent,
                item.relevance_score,
                json.dumps(item.metadata) if item.metadata else None,
                json.dumps(item.cross_references) if item.cross_references else None,
                self._calculate_text_hash(str(item.embedding)) if item.embedding else None
            ))
            
    def full_reindex(self) -> Dict[str, int]:
        """Perform full reindexing of all context sources"""
        self.logger.info("Starting full reindex of context sources")
        
        results = {
            'commands': len(self.index_command_history()),
            'user_voice': len(self.index_user_voice_data()),
            'sessions': len(self.index_session_continuity()),
            'evolution': len(self.index_project_evolution())
        }
        
        total_indexed = sum(results.values())
        self.logger.info(f"Full reindex complete. Indexed {total_indexed} items total: {results}")
        
        return results
        
    def get_context_stats(self) -> Dict[str, Any]:
        """Get indexing statistics"""
        with sqlite3.connect(self.context_db_path) as conn:
            cursor = conn.execute('''
                SELECT context_type, COUNT(*) as count, 
                       MAX(timestamp) as latest,
                       AVG(relevance_score) as avg_relevance
                FROM context_items 
                GROUP BY context_type
            ''')
            
            stats = {}
            for row in cursor.fetchall():
                stats[row[0]] = {
                    'count': row[1],
                    'latest': row[2],
                    'avg_relevance': row[3]
                }
                
        return stats
        
    # Helper methods
    def _classify_narrative(self, content: str) -> str:
        """Classify narrative type based on content patterns"""
        content_lower = content.lower()
        if 'conversation' in content_lower or 'dialogue' in content_lower:
            return 'conversation'
        elif 'insight' in content_lower or 'analysis' in content_lower:
            return 'insight'
        elif 'handoff' in content_lower:
            return 'handoff'
        else:
            return 'general'
            
    def _extract_session_id(self, filename: str) -> str:
        """Extract session ID from filename"""
        # Extract timestamp or session identifier
        import re
        match = re.search(r'(\d{4}-\d{2}-\d{2}[-_]\d{2}[-_]\d{2})', filename)
        if match:
            return match.group(1)
        return filename.split('.')[0]
        
    def _classify_session(self, content: str) -> str:
        """Classify session type"""
        content_lower = content.lower()
        if 'planning' in content_lower:
            return 'planning'
        elif 'implementation' in content_lower:
            return 'implementation'
        elif 'analysis' in content_lower:
            return 'analysis'
        else:
            return 'general'
            
    def _assess_handoff_completeness(self, content: str) -> float:
        """Assess completeness of handoff information"""
        required_sections = ['context', 'progress', 'next_steps', 'decisions']
        content_lower = content.lower()
        
        present_sections = sum(1 for section in required_sections if section in content_lower)
        return present_sections / len(required_sections)
        
    def _generate_metrics_summary(self, data: Any) -> str:
        """Generate human-readable summary of metrics data"""
        if isinstance(data, dict):
            keys = list(data.keys())[:5]  # First 5 keys
            summary = f"Metrics data with keys: {', '.join(keys)}"
            if len(data) > 5:
                summary += f" and {len(data) - 5} more"
            return summary
        elif isinstance(data, list):
            return f"List of {len(data)} metric entries"
        else:
            return str(data)[:200]  # First 200 chars

if __name__ == "__main__":
    # Example usage
    indexer = SemanticContextIndexer()
    results = indexer.full_reindex()
    print(f"Indexing complete: {results}")
    print(f"Stats: {indexer.get_context_stats()}")