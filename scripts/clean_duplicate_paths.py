#!/usr/bin/env python3
"""
Clean Duplicate Paths Script
Limpia referencias duplicadas/triplicadas generadas por el script fix_reference_paths.py
"""

import os
import re
import sys
from pathlib import Path

class DuplicatePathCleaner:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.fixes_applied = 0
        self.files_processed = 0

    def clean_file(self, file_path: Path) -> int:
        """Limpia duplicaciones en un archivo"""
        fixes_in_file = 0
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # Patrones de duplicación a limpiar
            duplicate_patterns = [
                # Triples
                (r'@context/architecture/core/@context/architecture/core/@context/architecture/core/', r'@context/architecture/core/'),
                # Dobles  
                (r'@context/architecture/core/@context/architecture/core/', r'@context/architecture/core/'),
                # Otros patterns similares
                (r'@context/vision/@context/vision/', r'@context/vision/'),
                (r'@context/architecture/standards/@context/architecture/standards/', r'@context/architecture/standards/'),
                # Limpiar @ duplicados
                (r'@@context/', r'@context/'),
            ]
            
            for pattern, replacement in duplicate_patterns:
                if pattern in content:
                    content = content.replace(pattern, replacement)
                    fixes_in_file += content.count(replacement) - original_content.count(replacement)
            
            # Escribir solo si hubo cambios
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ {file_path.relative_to(self.project_root)}: {fixes_in_file} duplicaciones limpiadas")
            
            return fixes_in_file
            
        except Exception as e:
            print(f"❌ Error procesando {file_path}: {e}")
            return 0

    def clean_directories(self, directories: list) -> None:
        """Limpia duplicaciones en directorios especificados"""
        for directory in directories:
            dir_path = self.project_root / directory
            if dir_path.exists():
                md_files = list(dir_path.rglob('*.md'))
                for file_path in md_files:
                    fixes = self.clean_file(file_path)
                    self.fixes_applied += fixes
                    self.files_processed += 1

    def generate_report(self) -> None:
        """Genera reporte de limpieza"""
        print(f"\n📊 REPORTE DE LIMPIEZA DE DUPLICACIONES")
        print(f"Archivos procesados: {self.files_processed}")
        print(f"Duplicaciones corregidas: {self.fixes_applied}")
        
        if self.fixes_applied > 0:
            print("✅ Limpieza completada exitosamente")
        else:
            print("✅ No se encontraron duplicaciones")

def main():
    if len(sys.argv) < 2:
        print("Uso: python clean_duplicate_paths.py <proyecto_root> [directorios...]")
        sys.exit(1)
    
    project_root = sys.argv[1]
    directories = sys.argv[2:] if len(sys.argv) > 2 else ['.claude/commands', 'context', '.']
    
    print("🧹 Iniciando limpieza de duplicaciones...")
    print(f"📂 Directorio raíz: {project_root}")
    
    cleaner = DuplicatePathCleaner(project_root)
    cleaner.clean_directories(directories)
    cleaner.generate_report()

if __name__ == "__main__":
    main()