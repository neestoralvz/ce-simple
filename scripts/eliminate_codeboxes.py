#!/usr/bin/env python3
"""
Script para eliminación masiva de codeboxes en documentación
Convierte code blocks (```) a texto directo preservando información
"""

import os
import re
import sys
from pathlib import Path

def process_codebox_content(content_inside_box, context_before="", context_after=""):
    """
    Convierte contenido de codebox a texto directo apropiado
    """
    lines = content_inside_box.strip().split('\n')
    
    # Si es lista o estructura, mantenerla como lista
    if any(line.strip().startswith(('-', '*', '1.', '2.', '3.')) for line in lines):
        return '\n'.join(lines)
    
    # Si es comando o code, convertir a texto inline
    if len(lines) == 1 and not lines[0].startswith('#'):
        return lines[0]
    
    # Si es estructura multi-línea, mantener con headers
    if any(line.strip().startswith('#') for line in lines):
        return '\n'.join(lines)
    
    # Default: convertir a lista numerada
    processed_lines = []
    for i, line in enumerate(lines, 1):
        if line.strip():  # Skip empty lines
            processed_lines.append(f"{i}. {line.strip()}")
    
    return '\n'.join(processed_lines)

def eliminate_codeboxes_from_content(content, filename):
    """
    Elimina codeboxes de contenido preservando información
    """
    changes = []
    
    # Pattern para detectar codeboxes: ```optional_lang ... ```
    codebox_pattern = r'```(?:[a-z]*\n)?(.*?)```'
    
    def replace_codebox(match):
        codebox_content = match.group(1)
        
        # Buscar contexto antes y después del codebox
        start_pos = match.start()
        end_pos = match.end()
        
        context_before = content[max(0, start_pos-100):start_pos]
        context_after = content[end_pos:min(len(content), end_pos+100)]
        
        # Procesar contenido
        processed = process_codebox_content(codebox_content, context_before, context_after)
        
        changes.append({
            'original': match.group(0),
            'replacement': processed,
            'context': context_before[-50:] + " [CODEBOX] " + context_after[:50]
        })
        
        return processed
    
    # Aplicar reemplazos
    new_content = re.sub(codebox_pattern, replace_codebox, content, flags=re.DOTALL)
    
    return new_content, changes

def process_file(filepath):
    """
    Procesa un archivo eliminando codeboxes
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        new_content, changes = eliminate_codeboxes_from_content(original_content, filepath.name)
        
        if changes:  # Solo escribir si hay cambios
            # Backup original
            backup_path = str(filepath) + '.backup'
            with open(backup_path, 'w', encoding='utf-8') as f:
                f.write(original_content)
            
            # Escribir nueva versión
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            
            print(f"✓ Processed {filepath}: {len(changes)} codeboxes eliminated")
            return len(changes), changes
        else:
            print(f"- No codeboxes found in {filepath}")
            return 0, []
            
    except Exception as e:
        print(f"✗ Error processing {filepath}: {e}")
        return 0, []

def main():
    """
    Main execution: procesa todos los archivos en context/
    """
    print("🚀 Iniciando eliminación masiva de codeboxes...")
    print("📊 Target: 317 codeboxes across 52 files (detected previamente)")
    
    context_path = Path("/Users/nalve/ce-simple/context")
    
    if not context_path.exists():
        print(f"✗ Context directory not found: {context_path}")
        sys.exit(1)
    
    total_changes = 0
    all_changes = {}
    processed_files = 0
    
    # Procesar todos los archivos .md en context/
    for md_file in context_path.rglob("*.md"):
        file_changes, changes_detail = process_file(md_file)
        if file_changes > 0:
            total_changes += file_changes
            all_changes[str(md_file)] = changes_detail
            processed_files += 1
    
    # Generar reporte
    print(f"\n📈 REPORTE FINAL:")
    print(f"📁 Archivos procesados: {processed_files}")
    print(f"🔧 Total codeboxes eliminados: {total_changes}")
    print(f"🎯 Target alcanzado: {total_changes}/317 ({total_changes/317*100:.1f}%)")
    
    # Generar log detallado
    log_path = context_path / "codebox_elimination_log.md"
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(f"# Codebox Elimination Log\n\n")
        f.write(f"**29/07/2025** | Mass codebox elimination execution\n\n")
        f.write(f"## Summary\n")
        f.write(f"- Target: 317 codeboxes across 52 files\n")
        f.write(f"- Eliminated: {total_changes} codeboxes\n")
        f.write(f"- Files processed: {processed_files}\n")
        f.write(f"- Success rate: {total_changes/317*100:.1f}%\n\n")
        
        f.write(f"## Changes by File\n")
        for filepath, changes in all_changes.items():
            f.write(f"### {filepath}\n")
            f.write(f"Changes: {len(changes)}\n\n")
            for i, change in enumerate(changes, 1):
                f.write(f"{i}. **Original**: {change['original'][:100]}...\n")
                f.write(f"   **Replacement**: {change['replacement'][:100]}...\n")
                f.write(f"   **Context**: {change['context']}\n\n")
    
    print(f"📋 Detailed log created: {log_path}")
    
    if total_changes > 0:
        print(f"\n✅ SUCCESS: Eliminación sistémica completada")
        print(f"💾 Backups created with .backup extension")
        print(f"🔍 Review changes before committing")
    else:
        print(f"\n⚠️  No codeboxes found to eliminate")

if __name__ == "__main__":
    main()