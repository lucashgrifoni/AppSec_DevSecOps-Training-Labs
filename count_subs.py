#!/usr/bin/env python3
import re

with open('.gitmodules', 'r', encoding='utf-8') as f:
    content = f.read()

# Encontrar todos os blocos de submodule
pattern = r'\[submodule "([^"]+)"\]\s+path = ([^\s]+)\s+url = ([^\s]+)'
matches = re.findall(pattern, content, re.MULTILINE)

print(f"Total encontrado: {len(matches)}")
print("\nPrimeiros 5:")
for i, (name, path, url) in enumerate(matches[:5]):
    print(f"{i+1}. {name} -> {path}")

print("\nÚltimos 5:")
for i, (name, path, url) in enumerate(matches[-5:]):
    print(f"{len(matches)-4+i}. {name} -> {path}")


