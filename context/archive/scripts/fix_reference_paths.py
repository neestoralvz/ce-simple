#!/usr/bin/env python3
"""
Fix Reference Paths Script
Corrige masivamente referencias rotas en commands y archivos core del sistema.
Desarrollado como parte de la auditoría y depuración de comandos.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set

# Mapping de referencias obsoletas a rutas reales
REFERENCE_MAPPING = {
    # Referencias principales del sistema
    '@context/TRUTH_SOURCE.md': '@context/architecture/core/truth-source.md',
    '@context/methodology.md': '@context/architecture/core/methodology.md', 
    '@context/authority.md': '@context/architecture/core/authority.md',
    '@context/standards.md': '@context/architecture/standards/README.md',
    '@context/simplicity.md': '@context/vision/simplicity.md',
    
    # Referencias en texto plano (sin @)
    'context/TRUTH_SOURCE.md': '@context/architecture/core/truth-source.md',
    'context/methodology.md': '@context/architecture/core/methodology.md',
    'context/authority.md': '@context/architecture/core/authority.md',
    'context/standards.md': '@context/architecture/standards/README.md',
    'context/simplicity.md': '@context/vision/simplicity.md',
    
    # Referencias a vision foundation
    'context/principles/vision_foundation.md': '@context/vision/vision_foundation.md',
    
    # Variaciones de TRUTH_SOURCE
    'TRUTH_SOURCE.md': '@context/architecture/core/truth-source.md',
    'truth-source.md': '@context/architecture/core/truth-source.md',
}

class ReferencePathFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.fixes_applied = []
        self.files_processed = 0
        self.total_fixes = 0

    def find_markdown_files(self, directories: List[str]) -> List[Path]:
        """Encuentra todos los archivos .md en los directorios especificados"""
        markdown_files = []
        for directory in directories:
            dir_path = self.project_root / directory
            if dir_path.exists():
                markdown_files.extend(dir_path.rglob('*.md'))
        return markdown_files

    def fix_references_in_file(self, file_path: Path) -> int:
        """Corrige referencias en un archivo específico"""
        fixes_in_file = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Aplicar cada mapping de referencias
            for old_ref, new_ref in REFERENCE_MAPPING.items():
                if old_ref in content:
                    content = content.replace(old_ref, new_ref)
                    fixes_count = original_content.count(old_ref)
                    fixes_in_file += fixes_count
                    
                    self.fixes_applied.append({
                        'file': str(file_path.relative_to(self.project_root)),
                        'old_ref': old_ref,
                        'new_ref': new_ref,
                        'count': fixes_count
                    })
            
            # Escribir archivo solo si hubo cambios
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ {file_path.relative_to(self.project_root)}: {fixes_in_file} referencias corregidas")
            
            return fixes_in_file
            
        except Exception as e:
            print(f"❌ Error procesando {file_path}: {e}")
            return 0

    def process_directories(self, directories: List[str]) -> None:
        """Procesa todos los archivos en los directorios especificados"""
        print(f"🔍 Buscando archivos .md en: {', '.join(directories)}")
        
        markdown_files = self.find_markdown_files(directories)
        print(f"📁 Encontrados {len(markdown_files)} archivos .md")
        
        for file_path in markdown_files:
            fixes = self.fix_references_in_file(file_path)
            self.files_processed += 1
            self.total_fixes += fixes

    def generate_report(self) -> None:
        """Genera reporte de correcciones aplicadas"""
        print("\n" + "="*60)
        print("📊 REPORTE DE CORRECCIONES APLICADAS")
        print("="*60)
        print(f"Archivos procesados: {self.files_processed}")
        print(f"Total correcciones: {self.total_fixes}")
        
        if self.fixes_applied:
            print("\n📝 Detalle de correcciones:")
            current_file = None
            for fix in self.fixes_applied:
                if fix['file'] != current_file:
                    current_file = fix['file']
                    print(f"\n📄 {current_file}:")
                print(f"  • {fix['old_ref']} → {fix['new_ref']} ({fix['count']}x)")
        
        print("\n✅ Proceso completado exitosamente")

def main():
    if len(sys.argv) < 2:
        print("Uso: python fix_reference_paths.py <proyecto_root> [directorios...]")
        print("Ejemplo: python fix_reference_paths.py /path/to/project .claude/commands context")
        sys.exit(1)
    
    project_root = sys.argv[1]
    directories = sys.argv[2:] if len(sys.argv) > 2 else ['.claude/commands', 'context']
    
    if not os.path.exists(project_root):
        print(f"❌ Error: El directorio {project_root} no existe")
        sys.exit(1)
    
    print("🚀 Iniciando corrección masiva de referencias...")
    print(f"📂 Directorio raíz: {project_root}")
    print(f"📁 Directorios objetivo: {', '.join(directories)}")
    
    fixer = ReferencePathFixer(project_root)
    fixer.process_directories(directories)
    fixer.generate_report()

if __name__ == "__main__":
    main()