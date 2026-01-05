#!/usr/bin/env python3
import re

with open('.gitmodules', 'r', encoding='utf-8') as f:
    lines = f.readlines()

current_path = None
current_url = None
projects = []
i = 0

while i < len(lines):
    line = lines[i].strip()
    
    if line.startswith('[submodule "'):
        if current_path and current_url:
            projects.append((current_path, current_url))
        match = re.search(r'\[submodule "([^"]+)"\]', line)
        if match:
            current_path = match.group(1)
            current_url = None
    elif line.startswith('url = '):
        current_url = line.replace('url = ', '').strip()
    
    i += 1

if current_path and current_url:
    projects.append((current_path, current_url))

print(f"Total de projetos encontrados: {len(projects)}")
for path, url in projects[:5]:
    print(f"  {path} -> {url}")


