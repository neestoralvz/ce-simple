#!/usr/bin/env python3
"""
Script final para corregir las 359 referencias rotas restantes
Mapea archivos faltantes a equivalentes existentes
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

class FinalReferenceFixer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.fixes_applied = 0
        self.files_processed = 0
        
        # Mapeo de archivos faltantes a equivalentes existentes
        self.missing_to_existing = {
            # Archivos principales faltantes → equivalentes reales
            '@context/MIGRATION_RULES.md': 'context/architecture/adr/ADR-005-reference-architecture-migration-protocol.md',
            'context/MIGRATION_RULES.md': 'context/architecture/adr/ADR-005-reference-architecture-migration-protocol.md',
            '@context/CROSS_REFERENCE_SYSTEM.md': 'context/architecture/reference/README.md',
            'context/CROSS_REFERENCE_SYSTEM.md': 'context/architecture/reference/README.md',
            '@context/COMPONENT_DECISION_MATRIX.md': 'context/architecture/ux/component-decision-flowchart.md',
            'context/COMPONENT_DECISION_MATRIX.md': 'context/architecture/ux/component-decision-flowchart.md',
            '@context/README_NAVIGATION_INTEGRATION.md': 'context/architecture/README.md',
            'context/README_NAVIGATION_INTEGRATION.md': 'context/architecture/README.md',
            
            # Archivos de templates faltantes
            '@context/templates.md': 'context/architecture/templates/README.md',
            'context/templates.md': 'context/architecture/templates/README.md',
            
            # Archivos críticos que no existen
            '@context/critical_violations_action_plan.md': 'context/architecture/adr/ADR-025-systematic-quality-violations-action-plan.md',
            'context/critical_violations_action_plan.md': 'context/architecture/adr/ADR-025-systematic-quality-violations-action-plan.md',
            '@context/standards_evolution_framework.md': 'context/architecture/standards/README.md',
            'context/standards_evolution_framework.md': 'context/architecture/standards/README.md',
            'context/guardian_system_integration_protocols.md': 'context/architecture/standards/README.md',
            
            # Archivos de simplicity y patterns mal referenciados
            'context/patterns/simplicity.md': 'context/vision/simplicity.md',
            'context/patterns/documentation_style.md': 'context/architecture/patterns/enforcement_integration_patterns.md',
            'context/patterns/orchestrator_methodology.md': 'context/architecture/patterns/command_orchestration_patterns.md',
            'context/patterns/README.md': 'context/architecture/patterns/README.md',
            
            # Referencias a directorios sin README
            'context/system/standards/': 'context/architecture/standards/',
            'context/system/principles/': 'context/architecture/core/',
            'context/enforcement/': 'context/architecture/core/',
            'context/planning/': 'context/architecture/core/methodology.md',
            
            # Referencias problemáticas específicas
            'context/enforcement/core_reminders.md': 'context/architecture/core/methodology.md',
            'context/system/principles/authority.md': 'context/architecture/core/authority.md',
            'context/planning/current.md': 'context/architecture/core/methodology.md',
            'context/user-vision/': 'context/vision/',
            
            # Patrones de duplicación a limpiar
            '@@context/': '@context/',
            '@@': '@',
        }
        
        # Patrones regex adicionales para limpiar
        self.regex_patterns = [
            # Limpiar duplicaciones de @
            (r'@@context/', r'@context/'),
            (r'@@([^@])', r'@\1'),
            
            # Corregir rutas malformadas
            (r'context/user-vision/@context/', r'@context/'),
            (r'context/user-vision/context/', r'context/'),
            
            # Limpiar referencias específicas conocidas
            (r'@context/MIGRATION_RULES\.md', r'context/architecture/adr/ADR-005-reference-architecture-migration-protocol.md'),
            (r'@context/CROSS_REFERENCE_SYSTEM\.md', r'context/architecture/reference/README.md'),
            (r'@context/COMPONENT_DECISION_MATRIX\.md', r'context/architecture/ux/component-decision-flowchart.md'),
            (r'@context/README_NAVIGATION_INTEGRATION\.md', r'context/architecture/README.md'),
            (r'@context/templates\.md', r'context/architecture/templates/README.md'),
            
            # Limpiar archivos críticos
            (r'@context/critical_violations_action_plan\.md', r'context/architecture/adr/ADR-025-systematic-quality-violations-action-plan.md'),
            (r'@context/standards_evolution_framework\.md', r'context/architecture/standards/README.md'),
            (r'context/guardian_system_integration_protocols\.md', r'context/architecture/standards/README.md'),
        ]

    def process_file(self, file_path: Path) -> int:
        """Procesa un archivo aplicando todas las correcciones finales"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            original_content = content
            fixes_in_file = 0
            
            # Aplicar mapeo directo
            for old_ref, new_ref in self.missing_to_existing.items():
                if old_ref in content:
                    content = content.replace(old_ref, new_ref)
                    fixes_in_file += 1
            
            # Aplicar patrones regex
            for pattern, replacement in self.regex_patterns:
                new_content = re.sub(pattern, replacement, content)
                if new_content != content:
                    content = new_content
                    fixes_in_file += 1
            
            # Escribir solo si hubo cambios
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
                    print(f"✅ {file_path.relative_to(self.project_root)}: {fixes} correcciones finales")
                    total_fixes += fixes
                files_processed += 1
        
        return files_processed, total_fixes

    def run_final_fix(self):
        """Ejecuta corrección final del sistema"""
        print("🎯 INICIANDO CORRECCIÓN FINAL DE REFERENCIAS")
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
                    print(f"✅ {target.name}: {fixes} correcciones finales")
                    total_fixes += fixes
                total_files += 1
            elif target.is_dir():
                # Procesar directorio
                print(f"\n📁 Procesando {target.relative_to(self.project_root)}/")
                files, fixes = self.scan_and_fix_directory(target)
                total_files += files
                total_fixes += fixes
        
        print("\n" + "=" * 60)
        print(f"📊 RESUMEN DE CORRECCIÓN FINAL:")
        print(f"   • Archivos procesados: {total_files}")
        print(f"   • Correcciones finales aplicadas: {total_fixes}")
        
        if total_fixes > 0:
            print(f"\n✅ ÉXITO: {total_fixes} referencias finales corregidas")
            return True
        else:
            print(f"\n⚠️  No se encontraron referencias para corrección final")
            return False

def main():
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = os.getcwd()
    
    if not Path(project_root).exists():
        print(f"❌ Error: El directorio {project_root} no existe")
        sys.exit(1)
    
    fixer = FinalReferenceFixer(project_root)
    success = fixer.run_final_fix()
    
    if success:
        print("\n🏁 Ejecuta validate_references.py para verificar resultado final")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()