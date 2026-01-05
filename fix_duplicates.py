#!/usr/bin/env python3
"""
Script para encontrar e remover duplicatas do .gitmodules.
"""
import re

with open('.gitmodules', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar todos os submodules
submodules = {}
lines = content.split('\n')
i = 0
current_submodule = None
current_path = None
current_url = None

while i < len(lines):
    line = lines[i].strip()
    
    if line.startswith('[submodule "'):
        # Salvar submodule anterior
        if current_submodule and current_path and current_url:
            if current_path in submodules:
                print(f"DUPLICADO encontrado: {current_path}")
                print(f"  Original: {submodules[current_path]['url']}")
                print(f"  Duplicado: {current_url}")
            else:
                submodules[current_path] = {
                    'name': current_submodule,
                    'path': current_path,
                    'url': current_url,
                    'start_line': None,
                    'end_line': None
                }
        
        # Novo submodule
        match = re.search(r'\[submodule "([^"]+)"\]', line)
        if match:
            current_submodule = match.group(1)
            current_path = None
            current_url = None
    elif line.startswith('path = '):
        current_path = line.replace('path = ', '').strip()
    elif line.startswith('url = '):
        current_url = line.replace('url = ', '').strip()
    
    i += 1

# Adicionar último
if current_submodule and current_path and current_url:
    if current_path in submodules:
        print(f"DUPLICADO encontrado: {current_path}")
    else:
        submodules[current_path] = {
            'name': current_submodule,
            'path': current_path,
            'url': current_url
        }

print(f"\nTotal de submodules únicos: {len(submodules)}")


