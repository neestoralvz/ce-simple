#!/usr/bin/env python3
"""
Script para corregir las 871 referencias rotas identificadas por validate_references.py
Basado en las rutas reales existentes en el sistema.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class ComprehensiveReferenceFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.fixes_applied = 0
        self.files_processed = 0
        
        # Mapeo completo de referencias rotas → rutas correctas
        self.reference_mapping = {
            # Archivos principales que se movieron
            'context/patterns/simplicity.md': 'context/vision/simplicity.md',
            'context/patterns/documentation_style.md': 'context/architecture/patterns/enforcement_integration_patterns.md',
            'context/patterns/orchestrator_methodology.md': 'context/architecture/patterns/command_orchestration_patterns.md',
            'context/enforcement/core_reminders.md': 'context/architecture/core/methodology.md',
            'context/system/principles/authority.md': 'context/architecture/core/authority.md',
            
            # Archivos de planning inexistentes - crear referencias a metodología
            'context/planning/current.md': 'context/architecture/core/methodology.md',
            'context/planning/': 'context/architecture/core/methodology.md',
            
            # Referencias duplicadas o malformadas
            'context/user-vision/@context/architecture/core/truth-source.md': '@context/architecture/core/truth-source.md',
            'context/user-vision/context/architecture/core/truth-source.md': 'context/architecture/core/truth-source.md',
            
            # Patrones comunes malformados
            'context/system/standards/': 'context/architecture/standards/',
            'context/system/': 'context/architecture/',
            'context/roles/': '@context/architecture/claude_code/',
            'context/enforcement/': 'context/architecture/core/',
            'context/claude_code/': '@context/architecture/claude_code/',
            
            # Referencias específicas que se encuentran en el archivo de patrones
            'context/patterns/': 'context/architecture/patterns/',
            
            # Templates y cross-references
            'context/templates/': '@context/templates.md',
            'context/CROSS_REFERENCE_SYSTEM.md': '@context/CROSS_REFERENCE_SYSTEM.md',
            'context/COMPONENT_DECISION_MATRIX.md': '@context/COMPONENT_DECISION_MATRIX.md',
            'context/MIGRATION_RULES.md': '@context/MIGRATION_RULES.md',
            'context/README_NAVIGATION_INTEGRATION.md': '@context/README_NAVIGATION_INTEGRATION.md',
        }
        
        # Patrones de regex para limpiar referencias duplicadas
        self.cleanup_patterns = [
            # Eliminar duplicaciones de @context
            (r'@context/@context/', '@context/'),
            (r'context/@context/', '@context/'),
            
            # Corregir referencias con user-vision duplicadas
            (r'context/user-vision/@context/', '@context/'),
            (r'context/user-vision/context/', 'context/'),
            
            # Limpiar referencias malformadas
            (r'context/system/standards/README\.md', 'context/architecture/standards/README.md'),
            (r'context/system/principles/', 'context/architecture/core/'),
            
            # Corregir patrones de archivos específicos
            (r'context/patterns/simplicity\.md', 'context/vision/simplicity.md'),
            (r'context/patterns/documentation_style\.md', 'context/architecture/patterns/enforcement_integration_patterns.md'),
            (r'context/patterns/orchestrator_methodology\.md', 'context/architecture/patterns/command_orchestration_patterns.md'),
            (r'context/enforcement/core_reminders\.md', 'context/architecture/core/methodology.md'),
            
            # Referencias de planning inexistentes
            (r'context/planning/current\.md', 'context/architecture/core/methodology.md'),
        ]

    def process_file(self, file_path: Path) -> int:
        """Procesa un archivo aplicando todas las correcciones"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            fixes_in_file = 0
            
            # Aplicar mapeo directo de referencias
            for old_ref, new_ref in self.reference_mapping.items():
                if old_ref in content:
                    content = content.replace(old_ref, new_ref)
                    fixes_in_file += 1
            
            # Aplicar patrones de regex para limpiezas complejas
            for pattern, replacement in self.cleanup_patterns:
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    content = new_content
                    fixes_in_file += 1
            
            # Escribir archivo solo si hubo cambios
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return fixes_in_file
                
            return 0
            
        except Exception as e:
            print(f"❌ Error procesando {file_path}: {e}")
            return 0

    def scan_and_fix_directory(self, directory: Path, pattern: str = "*.md") -> Tuple[int, int]:
        """Escanea y corrige archivos en un directorio"""
        files_processed = 0
        total_fixes = 0
        
        for file_path in directory.rglob(pattern):
            if file_path.is_file():
                fixes = self.process_file(file_path)
                if fixes > 0:
                    print(f"✅ {file_path.relative_to(self.project_root)}: {fixes} correcciones")
                    total_fixes += fixes
                files_processed += 1
        
        return files_processed, total_fixes

    def run_comprehensive_fix(self):
        """Ejecuta corrección completa del sistema"""
        print("🔧 INICIANDO CORRECCIÓN COMPLETA DE REFERENCIAS")
        print("=" * 60)
        
        # Directorios principales a procesar
        directories_to_fix = [
            self.project_root / ".claude" / "commands",
            self.project_root / "context",
            self.project_root / "CLAUDE.md",
        ]
        
        total_files = 0
        total_fixes = 0
        
        for target in directories_to_fix:
            if target.is_file():
                # Procesar archivo individual
                fixes = self.process_file(target)
                if fixes > 0:
                    print(f"✅ {target.name}: {fixes} correcciones")
                    total_fixes += fixes
                total_files += 1
            elif target.is_dir():
                # Procesar directorio
                print(f"\n📁 Procesando {target.relative_to(self.project_root)}/")
                files, fixes = self.scan_and_fix_directory(target)
                total_files += files
                total_fixes += fixes
        
        print("\n" + "=" * 60)
        print(f"📊 RESUMEN DE CORRECCIÓN COMPLETA:")
        print(f"   • Archivos procesados: {total_files}")
        print(f"   • Correcciones aplicadas: {total_fixes}")
        
        if total_fixes > 0:
            print(f"\n✅ ÉXITO: {total_fixes} referencias corregidas")
            return True
        else:
            print(f"\n⚠️  No se encontraron referencias para corregir")
            return False

def main():
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = os.getcwd()
    
    if not Path(project_root).exists():
        print(f"❌ Error: El directorio {project_root} no existe")
        sys.exit(1)
    
    fixer = ComprehensiveReferenceFixer(project_root)
    success = fixer.run_comprehensive_fix()
    
    if success:
        print("\n🎯 Ejecuta validate_references.py para verificar el resultado")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()