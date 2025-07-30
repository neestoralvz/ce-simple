#!/usr/bin/env python3
"""
Sync Semantic Triggers Script
Sincroniza semantic triggers entre CLAUDE.md y commands para asegurar integración correcta.
Parte de la auditoría y depuración de comandos.
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set

class SemanticTriggerSyncer:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.claude_md_path = self.project_root / "CLAUDE.md"
        self.commands_dir = self.project_root / ".claude" / "commands"
        
        self.claude_triggers = {}
        self.command_triggers = {}
        self.sync_issues = []
        self.fixes_applied = []

    def extract_claude_triggers(self) -> Dict[str, Dict]:
        """Extrae semantic triggers de CLAUDE.md"""
        triggers = {}
        
        if not self.claude_md_path.exists():
            print(f"❌ CLAUDE.md no encontrado en {self.claude_md_path}")
            return triggers
        
        try:
            with open(self.claude_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Buscar patrones semantic_pattern
            pattern = r'### IF semantic_pattern=([^:]+):\s*\n\*\*LOAD\*\*:\s*([^\n]+)\s*\n\*\*EXECUTE\*\*:\s*([^\n]+)\s*\n\*\*VALIDATE\*\*:\s*([^\n]+)'
            
            matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
            
            for match in matches:
                trigger_name = match[0].strip()
                load_refs = match[1].strip()
                execute_action = match[2].strip()
                validate_refs = match[3].strip()
                
                triggers[trigger_name] = {
                    'load': load_refs,
                    'execute': execute_action,
                    'validate': validate_refs,
                    'source': 'CLAUDE.md'
                }
            
            print(f"✅ CLAUDE.md: Encontrados {len(triggers)} semantic triggers")
            return triggers
            
        except Exception as e:
            print(f"❌ Error leyendo CLAUDE.md: {e}")
            return triggers

    def extract_command_triggers(self) -> Dict[str, Dict]:
        """Extrae semantic triggers de archivos de commands"""
        triggers = {}
        
        if not self.commands_dir.exists():
            print(f"❌ Directorio commands no encontrado: {self.commands_dir}")
            return triggers
        
        command_files = list(self.commands_dir.rglob('*.md'))
        
        for cmd_file in command_files:
            try:
                with open(cmd_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Buscar semantic trigger patterns en commands
                patterns = [
                    r'### ([^#\n]+) Pattern\s*\n\*\*Triggers\*\*:\s*([^\n]+)\s*\n\*\*Auto-activation\*\*:\s*([^\n]+)',
                    r'## SEMANTIC TRIGGERS[^#]*?### ([^#\n]+)\s*\n\*\*Triggers\*\*:\s*([^\n]+)'
                ]
                
                for pattern in patterns:
                    matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
                    
                    for match in matches:
                        if len(match) >= 3:
                            trigger_name = match[0].strip()
                            trigger_conditions = match[1].strip()
                            auto_activation = match[2].strip()
                        else:
                            trigger_name = match[0].strip()
                            trigger_conditions = match[1].strip()
                            auto_activation = ""
                        
                        # Normalizar nombre del trigger
                        normalized_name = self.normalize_trigger_name(trigger_name)
                        
                        triggers[normalized_name] = {
                            'conditions': trigger_conditions,
                            'activation': auto_activation,
                            'source_file': str(cmd_file.relative_to(self.project_root)),
                            'original_name': trigger_name
                        }
                
            except Exception as e:
                print(f"❌ Error leyendo {cmd_file}: {e}")
        
        print(f"✅ Commands: Encontrados {len(triggers)} semantic triggers")
        return triggers

    def normalize_trigger_name(self, name: str) -> str:
        """Normaliza nombres de triggers para comparación"""
        # Convertir a lowercase y reemplazar espacios/caracteres especiales
        normalized = name.lower()
        normalized = re.sub(r'[^a-z0-9]+', '_', normalized)
        normalized = normalized.strip('_')
        
        # Mapear algunos patterns comunes
        mappings = {
            'technical_research': 'research_investigation',
            'domain_knowledge': 'research_investigation', 
            'problem_solution': 'research_investigation',
            'knowledge_distillation': 'documentation_creation',
            'system_evolution': 'architecture_system_change',
            'conversation_integration': 'development_implementation'
        }
        
        return mappings.get(normalized, normalized)

    def find_sync_issues(self) -> List[Dict]:
        """Encuentra problemas de sincronización entre CLAUDE.md y commands"""
        issues = []
        
        # Triggers en CLAUDE.md pero no en commands
        for claude_trigger in self.claude_triggers:
            if claude_trigger not in self.command_triggers:
                issues.append({
                    'type': 'missing_in_commands',
                    'trigger': claude_trigger,
                    'details': f"Trigger '{claude_trigger}' definido en CLAUDE.md pero no implementado en commands"
                })
        
        # Triggers en commands pero no en CLAUDE.md
        for cmd_trigger in self.command_triggers:
            if cmd_trigger not in self.claude_triggers:
                issues.append({
                    'type': 'missing_in_claude',
                    'trigger': cmd_trigger,
                    'details': f"Trigger '{cmd_trigger}' en commands pero no definido en CLAUDE.md",
                    'source_file': self.command_triggers[cmd_trigger]['source_file']
                })
        
        # Triggers con referencias inconsistentes
        for trigger in set(self.claude_triggers.keys()) & set(self.command_triggers.keys()):
            claude_refs = self.claude_triggers[trigger]['load']
            cmd_activation = self.command_triggers[trigger]['activation']
            
            if claude_refs and cmd_activation and claude_refs != cmd_activation:
                issues.append({
                    'type': 'inconsistent_references',
                    'trigger': trigger,
                    'details': f"Referencias inconsistentes para trigger '{trigger}'",
                    'claude_refs': claude_refs,
                    'command_refs': cmd_activation
                })
        
        return issues

    def generate_missing_triggers(self) -> List[str]:
        """Genera código para triggers faltantes en CLAUDE.md"""
        missing_triggers = []
        
        for trigger, details in self.command_triggers.items():
            if trigger not in self.claude_triggers:
                # Generar template de trigger para CLAUDE.md
                trigger_template = f"""
### IF semantic_pattern={trigger}:
**LOAD**: {details.get('activation', '@context/architecture/core/methodology.md')}
**EXECUTE**: {details.get('original_name', trigger)} template per methodology authority
**VALIDATE**: @context/architecture/standards/README.md
"""
                missing_triggers.append(trigger_template.strip())
        
        return missing_triggers

    def fix_inconsistent_references(self) -> None:
        """Corrige referencias inconsistentes en commands"""
        for issue in self.sync_issues:
            if issue['type'] == 'inconsistent_references':
                trigger = issue['trigger']
                claude_refs = issue['claude_refs']
                
                # Buscar archivo de command con esta inconsistencia
                cmd_info = self.command_triggers[trigger]
                cmd_file_path = self.project_root / cmd_info['source_file']
                
                try:
                    with open(cmd_file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Reemplazar la referencia inconsistente
                    old_ref = cmd_info['activation']
                    new_ref = claude_refs
                    
                    if old_ref in content:
                        content = content.replace(old_ref, new_ref)
                        
                        with open(cmd_file_path, 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        self.fixes_applied.append({
                            'file': cmd_info['source_file'],
                            'trigger': trigger,
                            'old_ref': old_ref,
                            'new_ref': new_ref
                        })
                        
                        print(f"✅ Corregida referencia inconsistente en {cmd_info['source_file']}")
                
                except Exception as e:
                    print(f"❌ Error corrigiendo {cmd_file_path}: {e}")

    def generate_report(self) -> None:
        """Genera reporte completo de sincronización"""
        print("\n" + "="*70)
        print("📊 REPORTE DE SINCRONIZACIÓN DE SEMANTIC TRIGGERS")
        print("="*70)
        
        print(f"Triggers en CLAUDE.md: {len(self.claude_triggers)}")
        print(f"Triggers en Commands: {len(self.command_triggers)}")
        print(f"Problemas encontrados: {len(self.sync_issues)}")
        print(f"Correcciones aplicadas: {len(self.fixes_applied)}")
        
        if self.sync_issues:
            print("\n⚠️  PROBLEMAS DE SINCRONIZACIÓN:")
            print("-" * 50)
            
            for issue in self.sync_issues:
                print(f"🔶 {issue['type'].upper()}: {issue['trigger']}")
                print(f"   {issue['details']}")
                
                if 'source_file' in issue:
                    print(f"   Archivo: {issue['source_file']}")
                
                if issue['type'] == 'inconsistent_references':
                    print(f"   CLAUDE.md: {issue['claude_refs']}")
                    print(f"   Command: {issue['command_refs']}")
                print()
        
        # Mostrar triggers faltantes que se pueden agregar
        missing_triggers = self.generate_missing_triggers()
        if missing_triggers:
            print("\n📝 TRIGGERS SUGERIDOS PARA CLAUDE.md:")
            print("-" * 50)
            for trigger in missing_triggers:
                print(trigger)
                print()
        
        if self.fixes_applied:
            print("\n✅ CORRECCIONES APLICADAS:")
            print("-" * 50)
            for fix in self.fixes_applied:
                print(f"📄 {fix['file']}")
                print(f"   Trigger: {fix['trigger']}")
                print(f"   {fix['old_ref']} → {fix['new_ref']}")
                print()

    def sync_triggers(self) -> None:
        """Ejecuta sincronización completa"""
        print("🔍 Extrayendo triggers de CLAUDE.md...")
        self.claude_triggers = self.extract_claude_triggers()
        
        print("🔍 Extrayendo triggers de commands...")
        self.command_triggers = self.extract_command_triggers()
        
        print("🔍 Analizando problemas de sincronización...")
        self.sync_issues = self.find_sync_issues()
        
        if self.sync_issues:
            print(f"🔧 Aplicando correcciones automáticas...")
            self.fix_inconsistent_references()
        
        self.generate_report()

def main():
    if len(sys.argv) < 2:
        print("Uso: python sync_semantic_triggers.py <proyecto_root>")
        print("Ejemplo: python sync_semantic_triggers.py /path/to/project")
        sys.exit(1)
    
    project_root = sys.argv[1]
    
    if not os.path.exists(project_root):
        print(f"❌ Error: El directorio {project_root} no existe")
        sys.exit(1)
    
    print("🚀 Iniciando sincronización de semantic triggers...")
    print(f"📂 Directorio raíz: {project_root}")
    
    syncer = SemanticTriggerSyncer(project_root)
    syncer.sync_triggers()
    
    if syncer.sync_issues:
        print(f"\n⚠️  Se encontraron {len(syncer.sync_issues)} problemas de sincronización")
        if syncer.fixes_applied:
            print(f"✅ {len(syncer.fixes_applied)} correcciones aplicadas automáticamente")
        print("📋 Revisar reporte para acciones adicionales requeridas")
    else:
        print("\n🎉 ¡Semantic triggers sincronizados correctamente!")

if __name__ == "__main__":
    main()