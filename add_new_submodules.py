#!/usr/bin/env python3
"""
Script para adicionar novos submodules.
"""
import json
import subprocess
import os

def add_submodule(url, path):
    """Adiciona um submodule."""
    print(f"Adding submodule: {path}")
    try:
        subprocess.run(
            ['git', 'submodule', 'add', url, path],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        print(f"  [OK] Added: {path}")
        return True
    except subprocess.CalledProcessError as e:
        error_msg = e.stderr.decode() if e.stderr else 'Unknown error'
        if 'Filename too long' in error_msg:
            print(f"  [SKIP] Filename too long (Windows limitation): {path}")
        else:
            print(f"  [FAILED] Failed to add {path}: {error_msg[:200]}")
        return False

def main():
    with open('new_projects_data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    projects = data['new_projects']
    
    print("=" * 80)
    print("Adding New Git Submodules")
    print("=" * 80)
    print(f"Total projects: {len(projects)}\n")
    
    added = 0
    failed = 0
    skipped = 0
    
    for project in projects:
        url = project['url']
        category = project['category']
        slug = project['slug']
        path = f"labs/{category}/{slug}"
        
        # Verificar se o diretório já existe
        if os.path.exists(path) and os.path.exists(f"{path}/.git"):
            print(f"Skipping {path} (already exists)")
            skipped += 1
            continue
        
        if add_submodule(url, path):
            added += 1
        else:
            failed += 1
    
    print("\n" + "=" * 80)
    print(f"Summary: {added} added, {failed} failed, {skipped} skipped")
    print("=" * 80)

if __name__ == '__main__':
    main()


