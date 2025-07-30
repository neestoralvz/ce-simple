#!/usr/bin/env python3
"""
Script de integración Architecture-Commands para optimizar coherencia
Sincroniza semantic triggers entre CLAUDE.md y comandos, mejora templates
"""

import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple, Set
import json

class ArchitectureCommandsIntegrator:
    def __init__(self, project_root: str):
        self.project_root = Path(project_root)
        self.claude_md_path = self.project_root / "CLAUDE.md"
        self.commands_dir = self.project_root / ".claude" / "commands"
        self.context_dir = self.project_root / "context"
        
        self.integration_fixes = 0
        self.files_processed = 0
        
        # Patrones de semantic triggers en CLAUDE.md
        self.semantic_patterns = {}
        self.command_triggers = {}
        
    def analyze_claude_md_triggers(self) -> Dict[str, Dict]:
        """Analiza semantic triggers en CLAUDE.md"""
        try:
            with open(self.claude_md_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            triggers = {}
            
            # Buscar patrones IF semantic_pattern
            pattern = r'### IF semantic_pattern=([^:]+):\s*\*\*LOAD\*\*:\s*([^\n]+)\s*\*\*EXECUTE\*\*:\s*([^\n]+)'
            matches = re.findall(pattern, content, re.MULTILINE)
            
            for pattern_name, load_context, execute_action in matches:
                triggers[pattern_name.strip()] = {
                    'load': load_context.strip(),
                    'execute': execute_action.strip(),
                    'type': 'conditional_loading'
                }
            
            print(f"📋 Encontrados {len(triggers)} semantic triggers en CLAUDE.md")
            return triggers
            
        except Exception as e:
            print(f"❌ Error analizando CLAUDE.md: {e}")
            return {}
    
    def analyze_command_structure(self) -> Dict[str, Dict]:
        """Analiza estructura y triggers de comandos"""
        commands = {}
        
        for command_file in self.commands_dir.rglob("*.md"):
            try:
                with open(command_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                rel_path = command_file.relative_to(self.commands_dir)
                
                # Extraer semantic triggers del comando
                triggers = []
                
                # Buscar patrones **Triggers**:
                trigger_pattern = r'\*\*Triggers\*\*:\s*([^\n]+)'
                trigger_matches = re.findall(trigger_pattern, content)
                triggers.extend(trigger_matches)
                
                # Buscar **Auto-activation**:
                auto_pattern = r'\*\*Auto-activation\*\*:\s*([^\n]+)'
                auto_matches = re.findall(auto_pattern, content)
                
                # Buscar LOAD: references
                load_pattern = r'\*\*LOAD:\*\*\s*([^\n]+)'
                load_matches = re.findall(load_pattern, content)
                
                commands[str(rel_path)] = {
                    'triggers': triggers,
                    'auto_activation': auto_matches,
                    'loads': load_matches,
                    'content': content,
                    'path': command_file
                }
                
            except Exception as e:
                print(f"⚠️  Error procesando {command_file}: {e}")
        
        print(f"📁 Analizados {len(commands)} archivos de comandos")
        return commands
    
    def validate_reference_consistency(self, commands: Dict) -> List[Dict]:
        """Valida consistencia de referencias entre comandos y contexto"""
        issues = []
        
        for command_path, command_data in commands.items():
            content = command_data['content']
            
            # Buscar referencias @context/
            context_refs = re.findall(r'@context/([^)\s\n]+)', content)
            
            for ref in context_refs:
                full_path = self.context_dir / ref
                if not full_path.exists():
                    issues.append({
                        'command': command_path,
                        'issue': 'missing_context_reference',
                        'reference': f'@context/{ref}',
                        'severity': 'high'
                    })
        
        return issues
    
    def optimize_command_templates(self, commands: Dict) -> int:
        """Optimiza templates de comandos para mayor coherencia"""
        optimizations = 0
        
        # Patrones de optimización comunes
        optimizations_patterns = [
            # Estandarizar headers de autoridad
            (r'\*\*AUTORIDAD SUPREMA\*\*\s*\n([^\n]+)', 
             r'## AUTORIDAD SUPREMA\n\1'),
            
            # Estandarizar formato LOAD
            (r'\*\*LOAD:\*\*\s*([^\n]+)', 
             r'**LOAD:** \1'),
            
            # Estandarizar formato de triggers
            (r'\*\*Triggers\*\*:\s*([^\n]+)', 
             r'**Triggers**: \1'),
            
            # Corregir referencias duplicadas
            (r'@context/@context/', 
             r'@context/'),
        ]
        
        for command_path, command_data in commands.items():
            content = command_data['content']
            original_content = content
            
            # Aplicar optimizaciones
            for pattern, replacement in optimizations_patterns:
                content = re.sub(pattern, replacement, content, flags=re.MULTILINE)
            
            # Si hubo cambios, escribir archivo
            if content != original_content:
                try:
                    with open(command_data['path'], 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    optimizations += 1
                    print(f"✅ Optimizado: {command_path}")
                    
                except Exception as e:
                    print(f"❌ Error optimizando {command_path}: {e}")
        
        return optimizations
    
    def synchronize_semantic_triggers(self, claude_triggers: Dict, commands: Dict) -> int:
        """Sincroniza semantic triggers entre CLAUDE.md y comandos"""
        synchronizations = 0
        
        # Mapeo de patrones semánticos a comandos
        pattern_to_command = {
            'research_investigation': 'actions/research.md',
            'documentation_creation': 'actions/write.md',
            'architecture_system_change': 'roles/orchestrator.md',
            'development_implementation': 'workflows/execute.md',
            'workflow_command_creation': 'workflows/plan.md',
            'multi_conversation_orchestration': 'roles/orchestrator.md',
            'session_management': 'workflows/close.md',
            'content_placement': 'actions/context.md',
            'error_problem_resolution': 'actions/validate.md'
        }
        
        for pattern, command_file in pattern_to_command.items():
            if pattern in claude_triggers and command_file in commands:
                command_data = commands[command_file]
                claude_trigger = claude_triggers[pattern]
                
                # Verificar si el comando tiene el trigger correcto
                has_trigger = any(pattern in trigger for trigger in command_data['triggers'])
                
                if not has_trigger:
                    # Agregar trigger al comando
                    content = command_data['content']
                    
                    # Buscar sección SEMANTIC TRIGGERS
                    if '## SEMANTIC TRIGGERS' in content:
                        # Agregar nuevo trigger
                        trigger_section = f"""
### {pattern.replace('_', ' ').title()} Pattern
**Triggers**: {claude_trigger['execute']}
**Auto-activation**: {claude_trigger['load']}
**Execute**: Per CLAUDE.md semantic pattern
**Validate**: Context authority compliance
"""
                        content = content.replace('## SEMANTIC TRIGGERS', 
                                                f'## SEMANTIC TRIGGERS{trigger_section}')
                    else:
                        # Crear sección SEMANTIC TRIGGERS
                        authority_section = content.find('## AUTORIDAD SUPREMA')
                        if authority_section != -1:
                            insert_pos = content.find('\n\n', authority_section + 50)
                            if insert_pos != -1:
                                trigger_section = f"""
## SEMANTIC TRIGGERS

### {pattern.replace('_', ' ').title()} Pattern  
**Triggers**: {claude_trigger['execute']}
**Auto-activation**: {claude_trigger['load']}
**Execute**: Per CLAUDE.md semantic pattern
**Validate**: Context authority compliance
"""
                                content = content[:insert_pos] + trigger_section + content[insert_pos:]
                    
                    # Escribir archivo actualizado
                    try:
                        with open(command_data['path'], 'w', encoding='utf-8') as f:
                            f.write(content)
                        
                        synchronizations += 1
                        print(f"🔄 Sincronizado trigger '{pattern}' en {command_file}")
                        
                    except Exception as e:
                        print(f"❌ Error sincronizando {command_file}: {e}")
        
        return synchronizations
    
    def generate_integration_report(self, claude_triggers: Dict, commands: Dict, issues: List) -> str:
        """Genera reporte de integración"""
        report = f"""# Integration Architecture-Commands Report

**Fecha**: {os.popen('date').read().strip()}
**Archivos procesados**: {len(commands)}
**Correcciones aplicadas**: {self.integration_fixes}

## Semantic Triggers Analysis

### CLAUDE.md Triggers ({len(claude_triggers)})
"""
        
        for pattern, trigger in claude_triggers.items():
            report += f"- **{pattern}**: {trigger['execute']}\n"
        
        report += f"""
### Commands with Triggers
"""
        
        commands_with_triggers = {k: v for k, v in commands.items() if v['triggers']}
        for command, data in commands_with_triggers.items():
            report += f"- **{command}**: {len(data['triggers'])} triggers\n"
        
        if issues:
            report += f"""
## Issues Found ({len(issues)})
"""
            for issue in issues[:10]:  # Mostrar primeros 10
                report += f"- **{issue['command']}**: {issue['issue']} - {issue['reference']}\n"
        
        report += f"""
## Recommendations

1. **Complete trigger synchronization** between CLAUDE.md and commands
2. **Standardize command templates** for consistency
3. **Resolve missing references** in context structure
4. **Implement automated validation** in CI/CD pipeline

---
**Status**: Integration analysis completed
**Next Steps**: Apply optimizations and synchronizations
"""
        
        return report
    
    def run_integration_analysis(self):
        """Ejecuta análisis completo de integración"""
        print("🔗 INICIANDO INTEGRACIÓN ARCHITECTURE-COMMANDS")
        print("=" * 60)
        
        # Paso 1: Analizar CLAUDE.md
        print("\n📋 Analizando CLAUDE.md semantic triggers...")
        claude_triggers = self.analyze_claude_md_triggers()
        
        # Paso 2: Analizar comandos
        print("\n📁 Analizando estructura de comandos...")
        commands = self.analyze_command_structure()
        
        # Paso 3: Validar referencias
        print("\n🔍 Validando consistencia de referencias...")
        issues = self.validate_reference_consistency(commands)
        print(f"⚠️  Encontrados {len(issues)} issues de consistencia")
        
        # Paso 4: Optimizar templates
        print("\n⚡ Optimizando templates de comandos...")
        optimizations = self.optimize_command_templates(commands)
        print(f"✅ Aplicadas {optimizations} optimizaciones")
        
        # Paso 5: Sincronizar triggers
        print("\n🔄 Sincronizando semantic triggers...")
        synchronizations = self.synchronize_semantic_triggers(claude_triggers, commands)
        print(f"✅ Sincronizados {synchronizations} triggers")
        
        self.integration_fixes = optimizations + synchronizations
        
        # Paso 6: Generar reporte
        print("\n📄 Generando reporte de integración...")
        report = self.generate_integration_report(claude_triggers, commands, issues)
        
        report_path = self.project_root / "INTEGRATION_ARCHITECTURE_COMMANDS_REPORT.md"
        with open(report_path, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print("\n" + "=" * 60)
        print(f"📊 RESUMEN DE INTEGRACIÓN:")
        print(f"   • CLAUDE.md triggers: {len(claude_triggers)}")
        print(f"   • Comandos analizados: {len(commands)}")
        print(f"   • Issues encontrados: {len(issues)}")
        print(f"   • Optimizaciones aplicadas: {optimizations}")
        print(f"   • Sincronizaciones realizadas: {synchronizations}")
        print(f"   • Reporte generado: {report_path}")
        
        if self.integration_fixes > 0:
            print(f"\n✅ ÉXITO: {self.integration_fixes} mejoras de integración aplicadas")
            return True
        else:
            print(f"\n⚠️  Sistema ya está bien integrado")
            return True

def main():
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = os.getcwd()
    
    if not Path(project_root).exists():
        print(f"❌ Error: El directorio {project_root} no existe")
        sys.exit(1)
    
    integrator = ArchitectureCommandsIntegrator(project_root)
    success = integrator.run_integration_analysis()
    
    if success:
        print("\n🎯 Integración Architecture-Commands completada")
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()