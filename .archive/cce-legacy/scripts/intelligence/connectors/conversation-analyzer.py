#!/usr/bin/env python3
"""
Conversation Intelligence Analyzer - Historical Intelligence Phase 1
=====================================

**Purpose**: Parse and analyze Claude Code conversation JSONL files for pattern recognition
and historical intelligence extraction.

**Authority Integration**: Historical Intelligence Architecture (Principle #110)
**P55/P56 Compliance**: MANDATORY multi-source pattern analysis integration

This script implements Tier 1 conversation intelligence analysis for /system-update,
/knowledge-sync, and /intelligent-reorganization commands.
"""

import json
import os
import glob
import datetime
import re
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
import argparse


@dataclass
class ConversationPattern:
    """Structure for conversation pattern analysis results"""
    topic: str
    frequency: int
    confidence: float
    decision_patterns: List[str]
    success_indicators: List[str]
    related_files: List[str]
    temporal_context: Dict[str, Any]


@dataclass
class AnalysisResults:
    """Complete conversation analysis results"""
    total_conversations: int
    analysis_period: str
    patterns: List[ConversationPattern]
    knowledge_gaps: List[str]
    success_methodologies: List[str]
    optimization_opportunities: List[str]
    metadata: Dict[str, Any]


class ConversationAnalyzer:
    """Core conversation intelligence analysis engine"""
    
    def __init__(self, claude_projects_path: str = None):
        """Initialize analyzer with Claude projects path"""
        self.claude_projects_path = claude_projects_path or os.path.expanduser("~/.claude/projects")
        self.patterns_cache = {}
        self.analysis_results = None
        
    def find_conversation_files(self, project_id: str = None) -> List[str]:
        """Find all conversation JSONL files"""
        if project_id:
            pattern = f"{self.claude_projects_path}/{project_id}/conversation.jsonl"
            return glob.glob(pattern)
        else:
            pattern = f"{self.claude_projects_path}/*/conversation.jsonl"
            return glob.glob(pattern)
    
    def parse_jsonl_conversation(self, file_path: str) -> List[Dict]:
        """Parse JSONL conversation file"""
        conversations = []
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    if line.strip():
                        try:
                            conversations.append(json.loads(line))
                        except json.JSONDecodeError as e:
                            print(f"⚠️  JSON decode error in {file_path}: {e}")
                            continue
        except FileNotFoundError:
            print(f"❌ Conversation file not found: {file_path}")
        except Exception as e:
            print(f"❌ Error parsing {file_path}: {e}")
        
        return conversations
    
    def extract_decision_patterns(self, conversations: List[Dict]) -> List[str]:
        """Extract decision-making patterns from conversations"""
        decision_patterns = []
        
        # Common decision indicators
        decision_keywords = [
            'decidir', 'elegir', 'optar', 'seleccionar',
            'implementar', 'usar', 'aplicar', 'adoptar',
            'preferir', 'recomendar', 'sugerir'
        ]
        
        for conv in conversations:
            content = conv.get('content', '')
            if isinstance(content, str):
                for keyword in decision_keywords:
                    if keyword in content.lower():
                        # Extract context around decision
                        pattern = self._extract_context_around_keyword(content, keyword)
                        if pattern and pattern not in decision_patterns:
                            decision_patterns.append(pattern)
        
        return decision_patterns[:20]  # Top 20 patterns
    
    def identify_success_patterns(self, conversations: List[Dict]) -> List[str]:
        """Identify successful implementation patterns"""
        success_patterns = []
        
        success_indicators = [
            'éxito', 'exitoso', 'funcionó', 'resuelto', 'completado',
            'optimizado', 'mejorado', 'eficiente', 'correcto'
        ]
        
        for conv in conversations:
            content = conv.get('content', '')
            if isinstance(content, str):
                for indicator in success_indicators:
                    if indicator in content.lower():
                        pattern = self._extract_context_around_keyword(content, indicator)
                        if pattern and pattern not in success_patterns:
                            success_patterns.append(pattern)
        
        return success_patterns[:15]  # Top 15 success patterns
    
    def detect_knowledge_gaps(self, conversations: List[Dict]) -> List[str]:
        """Detect knowledge gaps from frequent questions"""
        gaps = []
        
        question_patterns = [
            r'¿cómo\s+(.+?)\?',
            r'¿qué\s+(.+?)\?',
            r'¿por qué\s+(.+?)\?',
            r'¿dónde\s+(.+?)\?',
            r'¿cuándo\s+(.+?)\?'
        ]
        
        for conv in conversations:
            content = conv.get('content', '')
            if isinstance(content, str):
                for pattern in question_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    for match in matches:
                        if len(match) < 100:  # Reasonable length
                            gap = f"Cómo {match.strip()}"
                            if gap not in gaps:
                                gaps.append(gap)
        
        return gaps[:10]  # Top 10 knowledge gaps
    
    def analyze_temporal_patterns(self, conversations: List[Dict]) -> Dict[str, Any]:
        """Analyze temporal patterns in conversations"""
        temporal_data = {
            'peak_hours': {},
            'day_patterns': {},
            'development_cycles': [],
            'session_durations': []
        }
        
        for conv in conversations:
            timestamp = conv.get('timestamp')
            if timestamp:
                try:
                    dt = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    hour = dt.hour
                    day = dt.strftime('%A')
                    
                    temporal_data['peak_hours'][hour] = temporal_data['peak_hours'].get(hour, 0) + 1
                    temporal_data['day_patterns'][day] = temporal_data['day_patterns'].get(day, 0) + 1
                    
                except (ValueError, AttributeError):
                    continue
        
        return temporal_data
    
    def extract_file_references(self, conversations: List[Dict]) -> List[str]:
        """Extract file references from conversations"""
        file_refs = []
        
        # Pattern for file references
        file_patterns = [
            r'docs/[a-zA-Z0-9/_.-]+\.md',
            r'scripts/[a-zA-Z0-9/_.-]+\.[a-zA-Z]+',
            r'[a-zA-Z0-9/_.-]+\.py',
            r'[a-zA-Z0-9/_.-]+\.sh',
            r'[a-zA-Z0-9/_.-]+\.js'
        ]
        
        for conv in conversations:
            content = conv.get('content', '')
            if isinstance(content, str):
                for pattern in file_patterns:
                    matches = re.findall(pattern, content)
                    file_refs.extend(matches)
        
        # Remove duplicates and return most frequent
        unique_refs = list(set(file_refs))
        return unique_refs[:50]  # Top 50 file references
    
    def generate_conversation_insights(self, timeframe_days: int = 30) -> AnalysisResults:
        """Generate comprehensive conversation insights"""
        print(f"🧠 **INTELIGENCIA CONVERSACIONAL** → Análisis de patrones ({timeframe_days} días)")
        
        # Find conversation files
        conv_files = self.find_conversation_files()
        if not conv_files:
            print(f"⚠️  No se encontraron archivos de conversación en {self.claude_projects_path}")
            return AnalysisResults(0, f"últimos {timeframe_days} días", [], [], [], [], {})
        
        print(f"📊 Archivos encontrados: {len(conv_files)}")
        
        all_conversations = []
        for file_path in conv_files:
            conversations = self.parse_jsonl_conversation(file_path)
            all_conversations.extend(conversations)
        
        if not all_conversations:
            print("⚠️  No se encontraron conversaciones válidas")
            return AnalysisResults(0, f"últimos {timeframe_days} días", [], [], [], [], {})
        
        print(f"💬 Conversaciones analizadas: {len(all_conversations)}")
        
        # Filter by timeframe
        cutoff_date = datetime.datetime.now() - datetime.timedelta(days=timeframe_days)
        recent_conversations = []
        
        for conv in all_conversations:
            timestamp = conv.get('timestamp')
            if timestamp:
                try:
                    dt = datetime.datetime.fromisoformat(timestamp.replace('Z', '+00:00'))
                    if dt > cutoff_date:
                        recent_conversations.append(conv)
                except (ValueError, AttributeError):
                    # Include conversations without valid timestamps
                    recent_conversations.append(conv)
            else:
                recent_conversations.append(conv)
        
        print(f"🕒 Conversaciones recientes ({timeframe_days} días): {len(recent_conversations)}")
        
        # Extract patterns
        decision_patterns = self.extract_decision_patterns(recent_conversations)
        success_patterns = self.identify_success_patterns(recent_conversations)
        knowledge_gaps = self.detect_knowledge_gaps(recent_conversations)
        file_refs = self.extract_file_references(recent_conversations)
        temporal_patterns = self.analyze_temporal_patterns(recent_conversations)
        
        # Create pattern objects
        patterns = []
        
        # Decision patterns
        for i, pattern in enumerate(decision_patterns):
            patterns.append(ConversationPattern(
                topic=f"Patrón de Decisión {i+1}",
                frequency=1,
                confidence=0.8,
                decision_patterns=[pattern],
                success_indicators=[],
                related_files=file_refs[:5] if file_refs else [],
                temporal_context=temporal_patterns
            ))
        
        # Success patterns  
        for i, pattern in enumerate(success_patterns):
            patterns.append(ConversationPattern(
                topic=f"Patrón de Éxito {i+1}",
                frequency=1,
                confidence=0.9,
                decision_patterns=[],
                success_indicators=[pattern],
                related_files=file_refs[:5] if file_refs else [],
                temporal_context=temporal_patterns
            ))
        
        # Optimization opportunities
        optimization_opportunities = [
            "Automatización de patrones de decisión recurrentes",
            "Documentación de metodologías exitosas identificadas",
            "Consolidación de preguntas frecuentes en base de conocimiento",
            "Optimización de navegación basada en archivos más referenciados"
        ]
        
        results = AnalysisResults(
            total_conversations=len(recent_conversations),
            analysis_period=f"últimos {timeframe_days} días",
            patterns=patterns,
            knowledge_gaps=knowledge_gaps,
            success_methodologies=success_patterns,
            optimization_opportunities=optimization_opportunities,
            metadata={
                'analysis_timestamp': datetime.datetime.now().isoformat(),
                'source_files': len(conv_files),
                'temporal_patterns': temporal_patterns,
                'file_references': file_refs
            }
        )
        
        self.analysis_results = results
        return results
    
    def _extract_context_around_keyword(self, text: str, keyword: str, context_length: int = 100) -> str:
        """Extract context around a keyword"""
        index = text.lower().find(keyword.lower())
        if index == -1:
            return ""
        
        start = max(0, index - context_length)
        end = min(len(text), index + len(keyword) + context_length)
        
        context = text[start:end].strip()
        # Clean up context
        context = ' '.join(context.split())  # Normalize whitespace
        
        return context if len(context) > 20 else ""
    
    def export_analysis_results(self, output_path: str) -> bool:
        """Export analysis results to JSON"""
        if not self.analysis_results:
            print("❌ No hay resultados de análisis para exportar")
            return False
        
        try:
            # Convert dataclasses to dict for JSON serialization
            export_data = {
                'total_conversations': self.analysis_results.total_conversations,
                'analysis_period': self.analysis_results.analysis_period,
                'patterns': [
                    {
                        'topic': p.topic,
                        'frequency': p.frequency,
                        'confidence': p.confidence,
                        'decision_patterns': p.decision_patterns,
                        'success_indicators': p.success_indicators,
                        'related_files': p.related_files,
                        'temporal_context': p.temporal_context
                    } for p in self.analysis_results.patterns
                ],
                'knowledge_gaps': self.analysis_results.knowledge_gaps,
                'success_methodologies': self.analysis_results.success_methodologies,
                'optimization_opportunities': self.analysis_results.optimization_opportunities,
                'metadata': self.analysis_results.metadata
            }
            
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, indent=2, ensure_ascii=False)
            
            print(f"✅ Resultados exportados a: {output_path}")
            return True
            
        except Exception as e:
            print(f"❌ Error exportando resultados: {e}")
            return False


def main():
    """Main execution function"""
    parser = argparse.ArgumentParser(description='Análisis de Inteligencia Conversacional')
    parser.add_argument('--timeframe', '-t', type=int, default=30, 
                       help='Periodo de análisis en días (default: 30)')
    parser.add_argument('--output', '-o', type=str,
                       help='Archivo de salida para resultados (JSON)')
    parser.add_argument('--claude-path', type=str,
                       help='Ruta a directorio de proyectos Claude')
    
    args = parser.parse_args()
    
    print("🧠 **CONVERSATION INTELLIGENCE ANALYZER** - Fase 1 Implementación")
    print("=" * 60)
    
    # Initialize analyzer
    analyzer = ConversationAnalyzer(args.claude_path)
    
    # Generate insights
    results = analyzer.generate_conversation_insights(args.timeframe)
    
    # Display summary
    print("\n📊 **RESUMEN DE ANÁLISIS**:")
    print(f"⟳ Conversaciones analizadas: {results.total_conversations}")
    print(f"⟳ Período: {results.analysis_period}")
    print(f"⟳ Patrones identificados: {len(results.patterns)}")
    print(f"⟳ Gaps de conocimiento: {len(results.knowledge_gaps)}")
    print(f"⟳ Metodologías exitosas: {len(results.success_methodologies)}")
    print(f"⟳ Oportunidades de optimización: {len(results.optimization_opportunities)}")
    
    # Export results if requested
    if args.output:
        analyzer.export_analysis_results(args.output)
    else:
        # Default output location
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        default_output = f"/Users/nalve/claude-context-engineering/scripts/results/intelligence/conversation-analysis-{timestamp}.json"
        os.makedirs(os.path.dirname(default_output), exist_ok=True)
        analyzer.export_analysis_results(default_output)
    
    print("\n🎯 **ANÁLISIS COMPLETADO** → Patrones listos para integración en comandos")


if __name__ == "__main__":
    main()