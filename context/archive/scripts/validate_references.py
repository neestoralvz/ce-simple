#!/usr/bin/env python3
"""
Validate References Script
Valida automáticamente la integridad de todas las referencias @context/* en el sistema.
Parte de la auditoría y depuración de comandos.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set

class ReferenceValidator:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.all_references = []
        self.broken_references = []
        self.valid_references = []
        self.files_scanned = 0
        
        # Patrones para detectar referencias
        self.reference_patterns = [
            r'@context/[^\s\)]+\.md',  # @context/path/file.md
            r'context/[^\s\)]+\.md',   # context/path/file.md
            r'→\s*@context/[^\s\)]+\.md',  # → @context/path/file.md
            r'←\s*@context/[^\s\)]+\.md',  # ← @context/path/file.md
            r'↔\s*@context/[^\s\)]+\.md',  # ↔ @context/path/file.md
        ]

    def find_markdown_files(self, directories: List[str]) -> List[Path]:
        """Encuentra todos los archivos .md en los directorios especificados"""
        markdown_files = []
        for directory in directories:
            dir_path = self.project_root / directory
            if dir_path.exists():
                markdown_files.extend(dir_path.rglob('*.md'))
            else:
                print(f"⚠️  Directorio no encontrado: {directory}")
        return markdown_files

    def extract_references_from_file(self, file_path: Path) -> List[Dict]:
        """Extrae todas las referencias @context/* de un archivo"""
        references = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            for line_num, line in enumerate(lines, 1):
                for pattern in self.reference_patterns:
                    matches = re.findall(pattern, line)
                    for match in matches:
                        # Limpiar la referencia
                        clean_ref = match.strip()
                        if clean_ref.startswith('→') or clean_ref.startswith('←') or clean_ref.startswith('↔'):
                            clean_ref = re.sub(r'^[→←↔]\s*', '', clean_ref)
                        
                        references.append({
                            'file': str(file_path.relative_to(self.project_root)),
                            'line': line_num,
                            'reference': clean_ref,
                            'context': line.strip()
                        })
            
        except Exception as e:
            print(f"❌ Error leyendo {file_path}: {e}")
            
        return references

    def validate_reference(self, reference: str) -> Tuple[bool, str]:
        """Valida si una referencia apunta a un archivo existente"""
        # Normalizar la referencia
        if reference.startswith('@context/'):
            # @context/path/file.md → context/path/file.md
            file_path = self.project_root / reference[1:]  # Remove @
        elif reference.startswith('context/'):
            # context/path/file.md
            file_path = self.project_root / reference
        else:
            return False, f"Formato de referencia no reconocido: {reference}"
        
        if file_path.exists():
            return True, str(file_path)
        else:
            return False, f"Archivo no encontrado: {file_path}"

    def scan_directories(self, directories: List[str]) -> None:
        """Escanea todos los directorios y extrae referencias"""
        print(f"🔍 Escaneando directorios: {', '.join(directories)}")
        
        markdown_files = self.find_markdown_files(directories)
        print(f"📁 Encontrados {len(markdown_files)} archivos .md")
        
        for file_path in markdown_files:
            references = self.extract_references_from_file(file_path)
            self.all_references.extend(references)
            self.files_scanned += 1
            
            if references:
                print(f"📄 {file_path.relative_to(self.project_root)}: {len(references)} referencias")

    def validate_all_references(self) -> None:
        """Valida todas las referencias encontradas"""
        print(f"\n🔍 Validando {len(self.all_references)} referencias...")
        
        for ref_info in self.all_references:
            is_valid, result = self.validate_reference(ref_info['reference'])
            
            if is_valid:
                self.valid_references.append(ref_info)
            else:
                ref_info['error'] = result
                self.broken_references.append(ref_info)

    def generate_report(self) -> None:
        """Genera reporte completo de validación"""
        print("\n" + "="*70)
        print("📊 REPORTE DE VALIDACIÓN DE REFERENCIAS")  
        print("="*70)
        print(f"Archivos escaneados: {self.files_scanned}")
        print(f"Referencias encontradas: {len(self.all_references)}")
        print(f"Referencias válidas: {len(self.valid_references)}")
        print(f"Referencias rotas: {len(self.broken_references)}")
        
        if self.broken_references:
            print("\n❌ REFERENCIAS ROTAS:")
            print("-" * 50)
            current_file = None
            for ref in self.broken_references:
                if ref['file'] != current_file:
                    current_file = ref['file']
                    print(f"\n📄 {current_file}:")
                
                print(f"  Línea {ref['line']}: {ref['reference']}")
                print(f"    Error: {ref['error']}")
                print(f"    Contexto: {ref['context'][:80]}...")
        
        # Authority Chain Analysis
        self.analyze_authority_chain()
        
        # Summary
        if self.broken_references:
            print(f"\n⚠️  ACCIÓN REQUERIDA: {len(self.broken_references)} referencias necesitan corrección")
        else:
            print(f"\n✅ SISTEMA ÍNTEGRO: Todas las referencias son válidas")

    def analyze_authority_chain(self) -> None:
        """Analiza la integridad de la cadena de autoridad"""
        print("\n🔗 ANÁLISIS DE CADENA DE AUTORIDAD")
        print("-" * 50)
        
        # Buscar referencias a archivos de autoridad clave
        key_authority_files = [
            'truth-source.md',
            'methodology.md', 
            'authority.md',
            'vision_foundation.md',
            'simplicity.md'
        ]
        
        authority_refs = {}
        for ref in self.all_references:
            for key_file in key_authority_files:
                if key_file in ref['reference']:
                    if key_file not in authority_refs:
                        authority_refs[key_file] = []
                    authority_refs[key_file].append(ref)
        
        for key_file, refs in authority_refs.items():
            print(f"📋 {key_file}: {len(refs)} referencias")
            valid_count = sum(1 for ref in refs if ref not in self.broken_references)
            if valid_count < len(refs):
                print(f"  ⚠️  {len(refs) - valid_count} referencias rotas")

    def export_broken_references(self, output_file: str = "broken_references.md") -> None:
        """Exporta las referencias rotas a un archivo markdown"""
        if not self.broken_references:
            return
            
        output_path = self.project_root / output_file
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("# Referencias Rotas - Reporte de Validación\n\n")
            f.write(f"**Fecha**: {self.get_current_date()}\n")
            f.write(f"**Total referencias rotas**: {len(self.broken_references)}\n\n")
            
            current_file = None
            for ref in self.broken_references:
                if ref['file'] != current_file:
                    current_file = ref['file']
                    f.write(f"## {current_file}\n\n")
                
                f.write(f"**Línea {ref['line']}**: `{ref['reference']}`\n")
                f.write(f"- **Error**: {ref['error']}\n")
                f.write(f"- **Contexto**: {ref['context']}\n\n")
        
        print(f"📄 Reporte exportado a: {output_file}")

    def get_current_date(self) -> str:
        """Obtiene la fecha actual en formato CDMX"""
        from datetime import datetime
        return datetime.now().strftime("%d/%m/%Y %H:%M CDMX")

def main():
    if len(sys.argv) < 2:
        print("Uso: python validate_references.py <proyecto_root> [directorios...]")
        print("Ejemplo: python validate_references.py /path/to/project .claude/commands context")
        sys.exit(1)
    
    project_root = sys.argv[1]
    directories = sys.argv[2:] if len(sys.argv) > 2 else ['.claude/commands', 'context', '.']
    
    if not os.path.exists(project_root):
        print(f"❌ Error: El directorio {project_root} no existe")
        sys.exit(1)
    
    print("🚀 Iniciando validación de referencias...")
    print(f"📂 Directorio raíz: {project_root}")
    print(f"📁 Directorios objetivo: {', '.join(directories)}")
    
    validator = ReferenceValidator(project_root)
    validator.scan_directories(directories)
    validator.validate_all_references()
    validator.generate_report()
    
    if validator.broken_references:
        validator.export_broken_references()
        sys.exit(1)  # Exit con error si hay referencias rotas
    else:
        print("\n🎉 Validación completada exitosamente - Sin referencias rotas")

if __name__ == "__main__":
    main()