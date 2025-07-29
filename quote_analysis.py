#!/usr/bin/env python3
import os
import re
from pathlib import Path

def analyze_user_quotes(conversations_dir):
    """Analyze all user quotes in conversation files."""
    
    quote_patterns = [
        # Direct quote patterns with > 
        (r'^>\s*"([^"]+)"', 'blockquote_double'),
        (r'^>\s*\'([^\']+)\'', 'blockquote_single'),
        (r'^>\s*([^"\']+)$', 'blockquote_plain'),
        
        # Usuario: patterns
        (r'Usuario:\s*"([^"]+)"', 'usuario_double'),
        (r'Usuario:\s*\'([^\']+)\'', 'usuario_single'),
        (r'Usuario:\s*([^"\']+)$', 'usuario_plain'),
        
        # **Human**: patterns
        (r'\*\*Human\*\*:\s*`([^`]+)`', 'human_backtick'),
        (r'\*\*Human\*\*:\s*"([^"]+)"', 'human_double'),
        (r'\*\*Human\*\*:\s*\'([^\']+)\'', 'human_single'),
        (r'\*\*Human\*\*:\s*([^"`\']+)$', 'human_plain'),
        
        # **User**: patterns
        (r'\*\*User[^:]*\*\*:\s*"([^"]+)"', 'user_double'),
        (r'\*\*User[^:]*\*\*:\s*\'([^\']+)\'', 'user_single'),
        (r'\*\*User[^:]*\*\*:\s*([^"\']+)$', 'user_plain'),
        
        # **User Voice patterns
        (r'\*\*User Voice[^:]*\*\*:\s*"([^"]+)"', 'user_voice_double'),
        
        # Narrative content patterns (from transcripts)
        (r'###\s*\[[0-9:]+\]\s*Usuario\s*-\s*(.+)', 'transcript_usuario'),
        
        # Other contextual patterns
        (r'Context[^:]*:\s*Usuario[^:]*:\s*(.+)', 'context_usuario'),
    ]
    
    results = {}
    total_quotes = 0
    file_stats = {}
    
    conversations_path = Path(conversations_dir)
    
    for md_file in conversations_path.glob("*.md"):
        file_quotes = []
        
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
                
                for line_num, line in enumerate(lines, 1):
                    line = line.strip()
                    if not line:
                        continue
                        
                    for pattern, pattern_type in quote_patterns:
                        matches = re.findall(pattern, line, re.MULTILINE)
                        for match in matches:
                            if isinstance(match, tuple):
                                quote_text = match[0] if match[0] else match[1] if len(match) > 1 else str(match)
                            else:
                                quote_text = match
                            
                            # Filter out obvious false positives
                            if len(quote_text.strip()) > 5 and not quote_text.startswith('**'):
                                file_quotes.append({
                                    'line': line_num,
                                    'type': pattern_type,
                                    'text': quote_text.strip()[:100] + ('...' if len(quote_text.strip()) > 100 else ''),
                                    'full_line': line[:150] + ('...' if len(line) > 150 else '')
                                })
        
        except Exception as e:
            print(f"Error reading {md_file}: {e}")
            continue
        
        # Remove duplicates based on similar text
        unique_quotes = []
        for quote in file_quotes:
            is_duplicate = False
            for existing in unique_quotes:
                if quote['text'].lower() == existing['text'].lower():
                    is_duplicate = True
                    break
            if not is_duplicate:
                unique_quotes.append(quote)
        
        file_stats[md_file.name] = {
            'total_quotes': len(unique_quotes),
            'quotes': unique_quotes
        }
        total_quotes += len(unique_quotes)
    
    return {
        'total_quotes': total_quotes,
        'files_analyzed': len(file_stats),
        'file_breakdown': file_stats
    }

def main():
    conversations_dir = "/Users/nalve/ce-simple/user-vision/raw/conversations"
    
    print("🔍 Analyzing user quotes in conversation files...")
    print("=" * 60)
    
    results = analyze_user_quotes(conversations_dir)
    
    print(f"\n📊 SUMMARY RESULTS")
    print("=" * 60)
    print(f"Total conversation files analyzed: {results['files_analyzed']}")
    print(f"Total distinct user quotes found: {results['total_quotes']}")
    print(f"Average quotes per file: {results['total_quotes'] / results['files_analyzed']:.1f}")
    
    print(f"\n📋 BREAKDOWN BY FILE")
    print("=" * 60)
    
    # Sort by number of quotes (descending)
    sorted_files = sorted(results['file_breakdown'].items(), 
                         key=lambda x: x[1]['total_quotes'], 
                         reverse=True)
    
    for filename, data in sorted_files:
        if data['total_quotes'] > 0:
            print(f"{filename}: {data['total_quotes']} quotes")
    
    print(f"\n🔍 QUOTE FORMAT PATTERNS FOUND")
    print("=" * 60)
    
    pattern_counts = {}
    example_quotes = {}
    
    for filename, data in results['file_breakdown'].items():
        for quote in data['quotes']:
            pattern_type = quote['type']
            pattern_counts[pattern_type] = pattern_counts.get(pattern_type, 0) + 1
            if pattern_type not in example_quotes:
                example_quotes[pattern_type] = quote
    
    for pattern_type, count in sorted(pattern_counts.items(), key=lambda x: x[1], reverse=True):
        example = example_quotes[pattern_type]
        print(f"\n{pattern_type}: {count} instances")
        print(f"  Example: {example['text']}")
        print(f"  From line: {example['full_line']}")
    
    print(f"\n📝 FILES WITH MOST QUOTES (Top 10)")
    print("=" * 60)
    
    for i, (filename, data) in enumerate(sorted_files[:10]):
        if data['total_quotes'] > 0:
            print(f"{i+1:2d}. {filename}")
            print(f"    {data['total_quotes']} quotes")
            if data['quotes']:
                print(f"    Sample: \"{data['quotes'][0]['text']}\"")
            print()

if __name__ == "__main__":
    main()