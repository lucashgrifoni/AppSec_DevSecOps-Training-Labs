#!/usr/bin/env python3
"""
Script para processar novos labs e verificar duplicatas.
"""
import json
import re
import subprocess
import os

def get_repo_slug(url: str) -> str:
    """Extrai slug do repositório da URL."""
    url = url.replace('.git', '')
    match = re.search(r'github\.com[/:]([^/]+)/([^/]+)', url)
    if match:
        return match.group(2).lower()
    # GitLab
    match = re.search(r'gitlab\.com[/:]([^/]+)/([^/]+)', url)
    if match:
        return match.group(2).lower()
    # Outros
    parts = url.rstrip('/').split('/')
    return parts[-1].lower() if parts else 'unknown'

def normalize_url(url: str) -> str:
    """Normaliza URL para comparação."""
    url = url.strip().lower()
    if url.endswith('.git'):
        url = url[:-4]
    if url.endswith('/'):
        url = url[:-1]
    return url

def categorize_project(name: str, url: str) -> str:
    """Categoriza projeto baseado no nome e URL."""
    name_lower = name.lower()
    url_lower = url.lower()
    combined = f"{name_lower} {url_lower}"
    
    if any(x in combined for x in ['cicd', 'pipeline', 'ci/cd', 'github actions', 'gitlab ci', 'jenkins', 'azure devops', 'actions-goat', 'cicd-goat', 'devsecops']):
        return 'cicd'
    elif any(x in combined for x in ['web', 'juice', 'shepherd', 'flask', 'asp.net', 'node', 'express', 'react', 'wordpress', 'xslt', 'otp', 'log4shell', 'webgoat', 'webpentest', 'tiredful', 'dvwps', 'dvwa']):
        return 'web'
    elif any(x in combined for x in ['api', 'openapi', 'graphql', 'soap', 'rest', 'websocket', 'vampi', 'fastapi', 'vapi', 'webservice', 'dvws']):
        return 'api'
    elif any(x in combined for x in ['android', 'ios', 'hybrid', 'mobile', 'oversecured', 'dvhia', 'dvia', 'dvhma']):
        return 'mobile'
    elif any(x in combined for x in ['aws', 'azure', 'gcp', 'kubernetes', 'cloud', 'awsgoat', 'azuregoat', 'gcpgoat', 'dvca', 'eks', 'gke']):
        return 'cloud'
    elif any(x in combined for x in ['java', 'python', 'go', 'c#', 'ruby', 'languages', 'source code', 'dvja', 'dvpwa', 'dvcsharp', 'dvra', 'crpya']):
        return 'language'
    else:
        return 'misc'

def get_project_description(name: str, url: str) -> str:
    """Gera descrição curta baseada no nome do projeto."""
    slug = get_repo_slug(url)
    name_clean = slug.replace('-', ' ').replace('_', ' ')
    
    if 'actions-goat' in name_clean.lower() or 'github actions' in name_clean.lower():
        return "Vulnerable GitHub Actions workflows for CI/CD security testing."
    elif 'cicd-goat' in name_clean.lower() or 'cicd goat' in name_clean.lower():
        return "Vulnerable CI/CD environment with multiple pipeline scenarios."
    elif 'devsecops' in name_clean.lower():
        return "DevSecOps lab with CI/CD pipeline security practices."
    elif 'jenkins' in name_clean.lower():
        return "Vulnerable Jenkins environment for pipeline security testing."
    elif 'azure devops' in name_clean.lower() or 'azuredevops' in name_clean.lower():
        return "Azure DevOps labs with pipeline security scenarios."
    elif 'kubernetes-goat' in name_clean.lower() or 'k8s-goat' in name_clean.lower():
        return "Vulnerable Kubernetes cluster for container security."
    elif 'eks-goat' in name_clean.lower():
        return "Vulnerable AWS EKS cluster for Kubernetes security."
    elif 'gke-goat' in name_clean.lower():
        return "Vulnerable GCP GKE cluster for Kubernetes security."
    elif 'awsgoat' in name_clean.lower():
        return "Vulnerable AWS infrastructure for cloud security training."
    elif 'azuregoat' in name_clean.lower():
        return "Vulnerable Azure infrastructure for cloud security training."
    elif 'gcp-goat' in name_clean.lower() or 'gcpgoat' in name_clean.lower():
        return "Vulnerable GCP infrastructure for cloud security training."
    elif 'dvwa' in name_clean.lower():
        return "Damn Vulnerable Web Application for security testing."
    elif 'dvws' in name_clean.lower():
        return "Damn Vulnerable Web Services for API security testing."
    elif 'dvhma' in name_clean.lower():
        return "Damn Vulnerable Hybrid Mobile App for mobile security."
    elif 'graphql' in name_clean.lower():
        return "Vulnerable GraphQL application for security testing."
    elif 'vampi' in name_clean.lower():
        return "Vulnerable API for security testing."
    elif 'dvsa' in name_clean.lower():
        return "Damn Vulnerable Serverless Application."
    elif 'dvta' in name_clean.lower():
        return "Damn Vulnerable Thick Client Application."
    elif 'dvja' in name_clean.lower():
        return "Damn Vulnerable Java Application."
    elif 'dvid' in name_clean.lower():
        return "Damn Vulnerable IoT Device."
    elif 'dvpwa' in name_clean.lower():
        return "Damn Vulnerable Python Web Application."
    elif 'bank' in name_clean.lower():
        return "Vulnerable banking application."
    elif 'dvwps' in name_clean.lower():
        return "Damn Vulnerable WordPress Site."
    elif 'dvna' in name_clean.lower():
        return "Damn Vulnerable NodeJS Application."
    elif 'dvra' in name_clean.lower():
        return "Damn Vulnerable Ruby on Rails."
    elif 'dvgm' in name_clean.lower():
        return "Damn Vulnerable Grade Management."
    elif 'tiredful' in name_clean.lower():
        return "Tiredful API - Vulnerable REST API."
    elif 'dvcsharp' in name_clean.lower():
        return "Damn Vulnerable C# Application."
    elif 'dvia' in name_clean.lower():
        return "Damn Vulnerable iOS App."
    elif 'dvrf' in name_clean.lower():
        return "Damn Vulnerable Router Firmware."
    elif 'dvfaas' in name_clean.lower() or 'faas' in name_clean.lower():
        return "Damn Vulnerable Functions as a Service."
    elif 'dvca' in name_clean.lower():
        return "Damn Vulnerable Cloud Application."
    elif 'crpya' in name_clean.lower():
        return "Certified Red Team Python Analyst."
    else:
        return "Vulnerable application for security testing and training."

# Novos labs de CI/CD
cicd_labs = [
    "https://github.com/step-security/github-actions-goat",
    "https://github.com/cider-security-research/cicd-goat",
    "https://github.com/Cloufish/DevSecOps-Lab",
    "https://gitlab.com/devsecops8471116/applying-dev-sec-ops-to-juice-shop",
    "https://github.com/vulhub/vulhub",
    "https://github.com/microsoft/azuredevopslabs",
    "https://github.com/MicrosoftLearning/implement-security-through-pipeline-using-devops",
    "https://github.com/madhuakula/kubernetes-goat",
    "https://github.com/OWASP/www-project-eks-goat",
    "https://github.com/dachiefjustice/railsgoat-cicd-lab",
]

# URLs da seção External Resources (resolvidas)
external_resources = [
    "https://github.com/ine-labs/AWSGoat",
    "https://github.com/ine-labs/AzureGoat",
    "https://github.com/JOSHUAJEBARAJ/GCP-Goat",
    "https://github.com/digininja/DVWA",
    "https://github.com/snoopysecurity/dvws-node",
    "https://github.com/logicalhacking/DVHMA",
    "https://github.com/dolevf/Damn-Vulnerable-GraphQL-Application",
    "https://github.com/snoopysecurity/dvws",
    "https://github.com/erev0s/VAmPI",
    "https://github.com/OWASP/DVSA",
    "https://github.com/srini0x00/dvta",
    "https://github.com/appsecco/dvja",
    "https://github.com/Vulcainreo/DVID",
    "https://github.com/anxolerd/dvpwa",
    "https://github.com/rewanthtammana/Damn-Vulnerable-Bank/",
    "https://github.com/vianasw/dvwps",
    "https://github.com/appsecco/dvna",
    "https://github.com/guilleiguaran/dvra",
    "https://git.logicalhacking.com/BrowserSecurity/DVGM",
    "https://github.com/payatu/Tiredful-API/",
    "https://github.com/appsecco/dvcsharp-api",
    "https://github.com/prateek147/DVIA",
    "https://github.com/prateek147/DVIA-v2",
    "https://github.com/praetorian-inc/DVRF",
    "https://github.com/we45/DVFaaS-Damn-Vulnerable-Functions-as-a-Service",
    "https://github.com/m6a-UdS/dvca",
    "https://github.com/CyberSecurityUP/CRPYA",
]

# Ler projetos existentes
existing_projects = {}
if os.path.exists('.gitmodules'):
    with open('.gitmodules', 'r', encoding='utf-8') as f:
        content = f.read()
        # Extrair URLs dos submodules existentes
        for line in content.split('\n'):
            if line.strip().startswith('url = '):
                url = line.strip().replace('url = ', '')
                normalized = normalize_url(url)
                existing_projects[normalized] = url

def main():
    all_new_labs = cicd_labs + external_resources
    new_projects = []
    duplicates = []
    
    print("Processando novos labs...")
    print(f"Total: {len(all_new_labs)}")
    print()
    
    for url in all_new_labs:
        normalized = normalize_url(url)
        slug = get_repo_slug(url)
        
        # Verificar duplicatas
        if normalized in existing_projects:
            duplicates.append((url, existing_projects[normalized]))
            print(f"[DUPLICADO] {url}")
            print(f"  -> Já existe: {existing_projects[normalized]}")
            continue
        
        # Verificar duplicatas por nome similar
        slug_normalized = slug.replace('-', '').replace('_', '')
        is_duplicate = False
        for existing_norm, existing_url in existing_projects.items():
            existing_slug = get_repo_slug(existing_url)
            existing_slug_norm = existing_slug.replace('-', '').replace('_', '')
            if slug_normalized == existing_slug_norm and slug_normalized != '':
                duplicates.append((url, existing_url))
                print(f"[DUPLICADO POR NOME] {url}")
                print(f"  -> Já existe: {existing_url}")
                is_duplicate = True
                break
        
        if is_duplicate:
            continue
        
        category = categorize_project(slug, url)
        name = slug.replace('-', ' ').replace('_', ' ').title()
        description = get_project_description(slug, url)
        
        new_projects.append({
            'name': name,
            'slug': slug,
            'url': url,
            'category': category,
            'description': description
        })
        print(f"[NOVO] {name} -> {category}")
    
    print()
    print("=" * 80)
    print("RESUMO")
    print("=" * 80)
    print(f"Novos projetos: {len(new_projects)}")
    print(f"Duplicados encontrados: {len(duplicates)}")
    
    # Organizar por categoria
    by_category = {}
    for project in new_projects:
        cat = project['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(project)
    
    print()
    print("Por categoria:")
    for cat in sorted(by_category.keys()):
        print(f"  {cat}: {len(by_category[cat])}")
    
    # Salvar JSON
    output = {
        'new_projects': new_projects,
        'by_category': by_category,
        'duplicates': duplicates
    }
    
    with open('new_projects_data.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    
    print()
    print("Dados salvos em new_projects_data.json")
    
    return output

if __name__ == '__main__':
    main()


