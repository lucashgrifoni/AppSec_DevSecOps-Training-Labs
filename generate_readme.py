#!/usr/bin/env python3
"""
Script para gerar README atualizado com todos os labs.
"""
import json
import re
import subprocess

def get_repo_slug(url: str) -> str:
    """Extrai slug do repositório da URL."""
    url = url.replace('.git', '')
    match = re.search(r'github\.com[/:]([^/]+)/([^/]+)', url)
    if match:
        return match.group(2).lower()
    match = re.search(r'gitlab\.com[/:]([^/]+)/([^/]+)', url)
    if match:
        return match.group(2).lower()
    parts = url.rstrip('/').split('/')
    return parts[-1].lower() if parts else 'unknown'

def get_project_description(name: str, url: str) -> str:
    """Gera descrição curta baseada no nome do projeto."""
    slug = get_repo_slug(url)
    name_clean = slug.replace('-', ' ').replace('_', ' ')
    
    descriptions = {
        'actions-goat': "Vulnerable GitHub Actions workflows for CI/CD security testing.",
        'cicd-goat': "Vulnerable CI/CD environment with multiple pipeline scenarios.",
        'devsecops-lab': "DevSecOps lab with CI/CD pipeline security practices.",
        'applying-dev-sec-ops-to-juice-shop': "DevSecOps pipeline integration with Juice Shop.",
        'vulhub': "Collection of vulnerable Docker environments via docker-compose.",
        'azuredevopslabs': "Azure DevOps labs with pipeline security scenarios.",
        'implement-security-through-pipeline-using-devops': "Microsoft Learning lab for Azure DevOps pipeline security.",
        'kubernetes-goat': "Vulnerable Kubernetes cluster for container security.",
        'www-project-eks-goat': "Vulnerable AWS EKS cluster for Kubernetes security.",
        'railsgoat-cicd-lab': "RailsGoat with CI/CD security scenarios.",
        'awsgoat': "Vulnerable AWS infrastructure for cloud security training.",
        'azuregoat': "Vulnerable Azure infrastructure for cloud security training.",
        'gcp-goat': "Vulnerable GCP infrastructure for cloud security training.",
        'dvwa': "Damn Vulnerable Web Application for security testing.",
        'dvws-node': "Damn Vulnerable Web Services (Node.js version).",
        'dvhma': "Damn Vulnerable Hybrid Mobile App for mobile security.",
        'damn-vulnerable-graphql-application': "Vulnerable GraphQL application for security testing.",
        'dvws': "Damn Vulnerable Web Services for API security testing.",
        'vampi': "Vulnerable API for security testing.",
        'dvsa': "Damn Vulnerable Serverless Application.",
        'dvta': "Damn Vulnerable Thick Client Application.",
        'dvja': "Damn Vulnerable Java Application.",
        'dvid': "Damn Vulnerable IoT Device.",
        'dvpwa': "Damn Vulnerable Python Web Application.",
        'damn-vulnerable-bank': "Vulnerable banking application.",
        'dvwps': "Damn Vulnerable WordPress Site.",
        'dvna': "Damn Vulnerable NodeJS Application.",
        'dvra': "Damn Vulnerable Ruby on Rails.",
        'dvgm': "Damn Vulnerable Grade Management.",
        'tiredful-api': "Tiredful API - Vulnerable REST API.",
        'dvcsharp-api': "Damn Vulnerable C# Application.",
        'dvia': "Damn Vulnerable iOS App.",
        'dvia-v2': "Damn Vulnerable iOS App 2.",
        'dvrf': "Damn Vulnerable Router Firmware.",
        'dvfaas-damn-vulnerable-functions-as-a-service': "Damn Vulnerable Functions as a Service.",
        'dvca': "Damn Vulnerable Cloud Application.",
        'crpya': "Certified Red Team Python Analyst.",
    }
    
    for key, desc in descriptions.items():
        if key in slug.lower():
            return desc
    
    return "Vulnerable application for security testing and training."

def read_gitmodules():
    """Lê todos os submodules do .gitmodules."""
    projects = []
    
    try:
        with open('.gitmodules', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            
        current_path = None
        current_url = None
        i = 0
        
        while i < len(lines):
            line = lines[i].strip()
            
            if line.startswith('[submodule "'):
                # Salvar projeto anterior se existir
                if current_path and current_url:
                    slug = current_path.split('/')[-1]
                    category = current_path.split('/')[1] if '/' in current_path else 'misc'
                    name = slug.replace('-', ' ').replace('_', ' ').title()
                    description = get_project_description(name, current_url)
                    
                    projects.append({
                        'name': name,
                        'slug': slug,
                        'url': current_url,
                        'category': category,
                        'description': description,
                        'path': current_path
                    })
                
                # Novo submodule
                match = re.search(r'\[submodule "([^"]+)"\]', line)
                if match:
                    current_path = match.group(1)
                    current_url = None
            elif line.startswith('path = '):
                path_value = line.replace('path = ', '').strip()
                # Se o path não corresponde ao current_path, atualizar
                if path_value != current_path:
                    current_path = path_value
            elif line.startswith('url = '):
                current_url = line.replace('url = ', '').strip()
            
            i += 1
        
        # Adicionar último projeto
        if current_path and current_url:
            slug = current_path.split('/')[-1]
            category = current_path.split('/')[1] if '/' in current_path else 'misc'
            name = slug.replace('-', ' ').replace('_', ' ').title()
            description = get_project_description(name, current_url)
            
            projects.append({
                'name': name,
                'slug': slug,
                'url': current_url,
                'category': category,
                'description': description,
                'path': current_path
            })
    except FileNotFoundError:
        print("Arquivo .gitmodules não encontrado")
    
    return projects

def generate_readme():
    """Gera o README completo."""
    projects = read_gitmodules()
    
    # Organizar por categoria
    by_category = {}
    for project in projects:
        cat = project['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(project)
    
    # Ordenar por nome em cada categoria
    for cat in by_category:
        by_category[cat].sort(key=lambda x: x['name'].lower())
    
    # Contagens
    counts = {cat: len(by_category[cat]) for cat in by_category}
    
    # Gerar README
    readme = """# Vulnerable Labs Hub

A centralized repository (monorepo) indexing dozens of vulnerable labs for security training and testing. This hub organizes vulnerable applications across multiple categories: Web, API, Mobile, Cloud, CI/CD, Language-specific, and Miscellaneous.

**⚠️ WARNING: For educational purposes in isolated environments only. Do not deploy these applications in production or expose them to public networks.**

## Table of Contents

- [Quick Start](#quick-start)
- [Running Labs](#running-labs)
- [Labs by Category](#labs-by-category)
"""
    
    # Adicionar links do índice
    if 'web' in counts:
        readme += f"  - [Web Applications](#web-applications) ({counts['web']})\n"
    if 'api' in counts:
        readme += f"  - [API](#api) ({counts['api']})\n"
    if 'mobile' in counts:
        readme += f"  - [Mobile](#mobile) ({counts['mobile']})\n"
    if 'cloud' in counts:
        readme += f"  - [Cloud](#cloud) ({counts['cloud']})\n"
    if 'cicd' in counts:
        readme += f"  - [CI/CD](#cicd) ({counts['cicd']})\n"
    if 'language' in counts:
        readme += f"  - [Language-Specific](#language-specific) ({counts['language']})\n"
    if 'misc' in counts:
        readme += f"  - [Miscellaneous](#miscellaneous) ({counts['misc']})\n"
    
    readme += """- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Quick Start

### Clone the repository with submodules

```bash
git clone --recurse-submodules https://github.com/lucashgrifoni/AppSec_DevSecOps-Training-Labs.git
cd AppSec_DevSecOps-Training-Labs
```

If you've already cloned without submodules:

```bash
git submodule update --init --recursive
```

### Initialize all labs

**Linux/macOS:**
```bash
./scripts/bootstrap.sh
```

**Windows:**
```powershell
.\scripts\bootstrap.ps1
```

## Running Labs

### Standard Approach (Docker-first)

Most labs support Docker. The recommended approach:

1. Navigate to the lab directory:
   ```bash
   cd labs/<category>/<lab-name>
   ```

2. Check for Docker Compose:
   ```bash
   ls docker-compose.yml  # or docker-compose.yaml
   ```

3. If Docker Compose exists:
   ```bash
   docker compose up -d
   ```

4. If no Docker Compose, check for Dockerfile:
   ```bash
   docker build -t <lab-name> .
   docker run -d -p <port>:<port> <lab-name>
   ```

5. If neither exists, follow the upstream README:
   ```bash
   cat README.md
   ```

### General Guidelines

- **Ports**: Check the upstream README for default ports. Common ports: 3000, 8080, 8000, 5000
- **Dependencies**: Some labs may require specific runtime environments (Node.js, Python, Java, etc.)
- **Database**: Some labs include database setup instructions
- **Configuration**: Review environment variables or config files before starting

## Labs by Category

"""
    
    # Gerar seções por categoria
    category_order = ['web', 'api', 'mobile', 'cloud', 'cicd', 'language', 'misc']
    category_titles = {
        'web': 'Web Applications',
        'api': 'API',
        'mobile': 'Mobile',
        'cloud': 'Cloud',
        'cicd': 'CI/CD',
        'language': 'Language-Specific',
        'misc': 'Miscellaneous'
    }
    
    for cat in category_order:
        if cat not in by_category:
            continue
        
        title = category_titles[cat]
        count = len(by_category[cat])
        readme += f"### {title} ({count})\n\n"
        readme += "| Name | Description | Link | Path |\n"
        readme += "|------|-------------|------|------|\n"
        
        for project in by_category[cat]:
            # Extrair nome do repositório da URL para link
            repo_name = project['url'].split('/')[-1].replace('.git', '')
            if 'gitlab.com' in project['url']:
                repo_path = '/'.join(project['url'].split('/')[-2:]).replace('.git', '')
                link_text = f"[GitLab]({project['url']})"
            elif 'github.com' in project['url']:
                repo_path = '/'.join(project['url'].split('/')[-2:]).replace('.git', '')
                link_text = f"[GitHub]({project['url']})"
            else:
                link_text = f"[Link]({project['url']})"
            
            readme += f"| {project['name']} | {project['description']} | {link_text} | `{project['path']}` |\n"
        
        readme += "\n"
    
    readme += """## Known Issues

### Windows Path Length Limitations

Some labs may fail to clone on Windows due to the 260-character path length limitation:
- `labs/web/owasp-security-shepherd` - Contains very long Android build paths
- `labs/misc/application-security-dev-labs` - Contains long Drupal module paths
- `labs/web/unsafe-bank-application-security-web-android-and-ios` - Contains long iOS Pod paths

**Workaround**: Enable long path support in Windows 10/11:
1. Run PowerShell as Administrator
2. Execute: `New-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force`
3. Restart your computer
4. Re-run: `git submodule update --init --recursive`

Alternatively, clone these specific labs to a shorter path manually.

## Troubleshooting

### Docker Issues

- **Port conflicts**: If a port is already in use, either stop the conflicting service or change the port in the lab's configuration
- **Permission denied**: On Linux, you may need to add your user to the docker group: `sudo usermod -aG docker $USER`
- **Docker not running**: Ensure Docker daemon is running: `docker ps`

### Submodule Issues

- **Submodules not initialized**: Run `git submodule update --init --recursive`
- **Submodule out of sync**: Update submodules: `git submodule update --remote`
- **Submodule path issues**: Ensure you're in the repository root when running submodule commands

### Port Issues

- Check the upstream README for default ports
- Common ports: 3000 (Node.js), 8080 (Java/Spring), 8000 (Python), 5000 (Flask)
- Use `netstat -an | grep LISTEN` (Linux/macOS) or `netstat -an | findstr LISTEN` (Windows) to check available ports

### Permission Issues

- Some labs may require specific file permissions
- On Linux/macOS, you may need `chmod +x` for scripts
- Check the upstream README for specific requirements

### Missing Dependencies

- Install required runtime environments (Node.js, Python, Java, etc.)
- Some labs may require specific versions - check the upstream README
- Database setup may be required for some labs

## Credits

All labs are maintained by their respective authors and organizations. This hub serves as a centralized index. For detailed information, licensing, and contributions, please refer to each lab's original repository.

### Lab Sources

All labs are sourced from:
- [lucashgrifoni GitHub organization](https://github.com/lucashgrifoni)
- [OWASP projects](https://owasp.org)
- [Various security researchers and organizations](https://github.com)

### Hub Maintainer

This hub is maintained as a community resource for security education and training purposes.

---

**Disclaimer**: This repository is for educational purposes only. The vulnerable applications contained herein should only be used in isolated, controlled environments. The maintainers are not responsible for any misuse of these resources.
"""
    
    return readme

if __name__ == '__main__':
    readme_content = generate_readme()
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("README.md atualizado com sucesso!")
    print(f"Total de projetos: {len(read_gitmodules())}")

