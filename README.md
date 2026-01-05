# Vulnerable Labs Hub

A centralized repository (monorepo) indexing dozens of vulnerable labs for security training and testing. This hub organizes vulnerable applications across multiple categories: Web, API, Mobile, Cloud, CI/CD, Language-specific, and Miscellaneous.

**⚠️ WARNING: For educational purposes in isolated environments only. Do not deploy these applications in production or expose them to public networks.**

## Table of Contents

- [Quick Start](#quick-start)
- [Running Labs](#running-labs)
- [Labs by Category](#labs-by-category)
  - [Web Applications](#web-applications) (15)
  - [API](#api) (7)
  - [Mobile](#mobile) (5)
  - [Cloud](#cloud) (3)
  - [CI/CD](#cicd) (0)
  - [Language-Specific](#language-specific) (5)
  - [Miscellaneous](#miscellaneous) (22)
- [External Resources](#external-resources)
- [Troubleshooting](#troubleshooting)
- [Credits](#credits)

## Quick Start

### Clone the repository with submodules

```bash
git clone --recurse-submodules https://github.com/lucashgrifoni/Vulnerable-Labs-Hub.git
cd Vulnerable-Labs-Hub
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

### Web Applications (15)

| Name | Description | Link | Path |
|------|-------------|------|------|
| Application Juice Shop | Modern web application with OWASP Top 10 vulnerabilities. | [GitHub](https://github.com/lucashgrifoni/Application-Juice-Shop) | `labs/web/application-juice-shop` |
| Application React Vulnerable | Vulnerable React web application. | [GitHub](https://github.com/lucashgrifoni/Application-React-Vulnerable) | `labs/web/application-react-vulnerable` |
| Application Vulnerable Log4Shell | Application demonstrating Log4Shell vulnerability. | [GitHub](https://github.com/lucashgrifoni/Application-Vulnerable-Log4Shell) | `labs/web/application-vulnerable-log4shell` |
| Application Vulnerable Node Express | Vulnerable Node.js/Express application. | [GitHub](https://github.com/lucashgrifoni/Application-Vulnerable-Node-Express) | `labs/web/application-vulnerable-node-express` |
| Application Vulnerable Otp | Vulnerable OTP (One-Time Password) implementation. | [GitHub](https://github.com/lucashgrifoni/Application-Vulnerable-OTP) | `labs/web/application-vulnerable-otp` |
| Application Vulnerable Xslt Console | Vulnerable XSLT console application. | [GitHub](https://github.com/lucashgrifoni/Application-Vulnerable-Xslt-Console) | `labs/web/application-vulnerable-xslt-console` |
| Damn Vulnerable Nodejs Application Dvna | Vulnerable Node.js/Express application. | [GitHub](https://github.com/lucashgrifoni/Damn-Vulnerable-NodeJS-Application-DVNA) | `labs/web/damn-vulnerable-nodejs-application-dvna` |
| Owasp Security Shepherd | Web and mobile application security training platform. | [GitHub](https://github.com/lucashgrifoni/OWASP-Security-Shepherd) | `labs/web/owasp-security-shepherd` |
| Owasp Vulnerable Web Applications Directory Project | Directory of vulnerable web applications. | [GitHub](https://github.com/lucashgrifoni/OWASP-Vulnerable-Web-Applications-Directory-Project) | `labs/web/owasp-vulnerable-web-applications-directory-project` |
| Owasp Webgoat.Net Docker Container | OWASP WebGoat vulnerable web application. | [GitHub](https://github.com/lucashgrifoni/OWASP-WebGoat.NET-Docker-Container) | `labs/web/owasp-webgoat.net-docker-container` |
| Unsafe Bank Application Security Web Android And Ios | Vulnerable banking application. | [GitHub](https://github.com/lucashgrifoni/UnSAFE-Bank-Application-Security-Web-Android-and-iOS) | `labs/web/unsafe-bank-application-security-web-android-and-ios` |
| Vulnerable Flask App | Vulnerable Flask web application. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Flask-App) | `labs/web/vulnerable-flask-app` |
| Vulnerable Web Application | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Web-Application) | `labs/web/vulnerable-web-application` |
| Vulnlab Web Application Vulnerability Lab Project | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/VulnLab-Web-Application-Vulnerability-Lab-Project) | `labs/web/vulnlab-web-application-vulnerability-lab-project` |
| Web Application Vulnerable Asp.Net Core 2.0 | Vulnerable ASP.NET Core application. | [GitHub](https://github.com/lucashgrifoni/Web-Application-Vulnerable-ASP.NET-Core-2.0) | `labs/web/web-application-vulnerable-asp.net-core-2.0` |

### API (7)

| Name | Description | Link | Path |
|------|-------------|------|------|
| Damn Vulnerable Graphql Application | Vulnerable GraphQL application for security testing. | [GitHub](https://github.com/lucashgrifoni/Damn-Vulnerable-GraphQL-Application) | `labs/api/damn-vulnerable-graphql-application` |
| Openapi 3 The Vulnerable Api | Vulnerable API demonstrating OpenAPI security issues. | [GitHub](https://github.com/lucashgrifoni/OpenAPI-3-The-Vulnerable-API) | `labs/api/openapi-3-the-vulnerable-api` |
| Sample Application With Rest Api Endpoints | Vulnerable REST API endpoints. | [GitHub](https://github.com/lucashgrifoni/Sample-Application-with-REST-API-Endpoints) | `labs/api/sample-application-with-rest-api-endpoints` |
| Vulnerable Api Security Application | Vulnerable API demonstrating OpenAPI security issues. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-API-Security-Application) | `labs/api/vulnerable-api-security-application` |
| Vulnerable Fastapi | Vulnerable FastAPI application for API security testing. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-FastAPI) | `labs/api/vulnerable-fastapi` |
| Vulnerable Soap Service | Vulnerable SOAP web service. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Soap-Service) | `labs/api/vulnerable-soap-service` |
| Vyapi The Modern Cloud Based Vulnerable Hybrid Android App | Vulnerable API demonstrating OpenAPI security issues. | [GitHub](https://github.com/lucashgrifoni/VyAPI-The-Modern-Cloud-Based-Vulnerable-Hybrid-Android-App) | `labs/api/vyapi-the-modern-cloud-based-vulnerable-hybrid-android-app` |

### Mobile (5)

| Name | Description | Link | Path |
|------|-------------|------|------|
| Damn Vulnerable Hybrid Mobile App | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Damn-Vulnerable-Hybrid-Mobile-App) | `labs/mobile/damn-vulnerable-hybrid-mobile-app` |
| Insecure And Vulnerable Android Application | Vulnerable Android application for mobile security testing. | [GitHub](https://github.com/lucashgrifoni/Insecure-and-Vulnerable-Android-Application) | `labs/mobile/insecure-and-vulnerable-android-application` |
| Oversecured Vulnerable Android App | Vulnerable Android application for mobile security testing. | [GitHub](https://github.com/lucashgrifoni/Oversecured-Vulnerable-Android-App) | `labs/mobile/oversecured-vulnerable-android-app` |
| Oversecured Vulnerable Ios App | Vulnerable iOS application for mobile security testing. | [GitHub](https://github.com/lucashgrifoni/Oversecured-Vulnerable-IOS-App) | `labs/mobile/oversecured-vulnerable-ios-app` |
| Vulnerable Android Application | Vulnerable Android application for mobile security testing. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Android-Application) | `labs/mobile/vulnerable-android-application` |

### Cloud (3)

| Name | Description | Link | Path |
|------|-------------|------|------|
| Application Vulnerable Kubernetes Goat | Vulnerable Kubernetes environment for container security. | [GitHub](https://github.com/lucashgrifoni/Application-Vulnerable-Kubernetes-Goat) | `labs/cloud/application-vulnerable-kubernetes-goat` |
| Awsgoat A Damn Vulnerable Aws Infrastructure | Vulnerable AWS infrastructure for cloud security training. | [GitHub](https://github.com/lucashgrifoni/AWSGoat-A-Damn-Vulnerable-AWS-Infrastructure) | `labs/cloud/awsgoat-a-damn-vulnerable-aws-infrastructure` |
| Vulnerable Google Cloud Platform | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Google-Cloud-Platform) | `labs/cloud/vulnerable-google-cloud-platform` |

### CI/CD (0)

No labs in this category yet.

### Language-Specific (5)

| Name | Description | Link | Path |
|------|-------------|------|------|
| Application Java Spring Vulny | Vulnerable Java/Spring application. | [GitHub](https://github.com/lucashgrifoni/Application-Java-Spring-Vulny) | `labs/language/application-java-spring-vulny` |
| Goof Snyk S Vulnerable Demo Application | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Goof-Snyk-s-Vulnerable-Demo-Application) | `labs/language/goof-snyk-s-vulnerable-demo-application` |
| Java Application Vulnerable Lab | Vulnerable Java/Spring application. | [GitHub](https://github.com/lucashgrifoni/Java-Application-Vulnerable-Lab) | `labs/language/java-application-vulnerable-lab` |
| Python Source Code Analysis | Vulnerable Python application. | [GitHub](https://github.com/lucashgrifoni/Python-Source-Code-Analysis) | `labs/language/python-source-code-analysis` |
| Vulnerable Languages | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Languages) | `labs/language/vulnerable-languages` |

### Miscellaneous (22)

| Name | Description | Link | Path |
|------|-------------|------|------|
| Andro Vuln Test | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/andro-vuln-test) | `labs/misc/andro-vuln-test` |
| Application Authentication Vulnerable Lab | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Application-Authentication-Vulnerable-Lab) | `labs/misc/application-authentication-vulnerable-lab` |
| Application Broken Crystals | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Application-Broken-Crystals) | `labs/misc/application-broken-crystals` |
| Application Docker Vulnerable | Vulnerable Docker containerized application. | [GitHub](https://github.com/lucashgrifoni/Application-Docker-Vulnerable) | `labs/misc/application-docker-vulnerable` |
| Application Security | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Application-Security) | `labs/misc/application-security` |
| Application Security Dev Labs | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Application-Security-Dev-Labs) | `labs/misc/application-security-dev-labs` |
| Application Vulnerable Lab Ssrf | Application vulnerable to SSRF attacks. | [GitHub](https://github.com/lucashgrifoni/Application-Vulnerable-Lab-SSRF) | `labs/misc/application-vulnerable-lab-ssrf` |
| Cors Misconfiguration Vulnerable Lab | Application with CORS misconfiguration vulnerabilities. | [GitHub](https://github.com/lucashgrifoni/CORS-misconfiguration-vulnerable-Lab) | `labs/misc/cors-misconfiguration-vulnerable-lab` |
| Damn Vulnerable Bank | Vulnerable banking application. | [GitHub](https://github.com/lucashgrifoni/Damn-Vulnerable-Bank) | `labs/misc/damn-vulnerable-bank` |
| Dvfaas Damn Vulnerable Functions As A Service | Vulnerable microservices application. | [GitHub](https://github.com/lucashgrifoni/DVFaaS-Damn-Vulnerable-Functions-as-a-Service) | `labs/misc/dvfaas-damn-vulnerable-functions-as-a-service` |
| Dvms Damn Vulnerable Micro Services | Vulnerable microservices application. | [GitHub](https://github.com/lucashgrifoni/DVMS-Damn-Vulnerable-Micro-Services) | `labs/misc/dvms-damn-vulnerable-micro-services` |
| Examples Of Different Vulnerabilities Useful For Testing Dast And Sast Tools | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Examples-of-different-vulnerabilities-Useful-for-testing-DAST-and-SAST-tools) | `labs/misc/examples-of-different-vulnerabilities-useful-for-testing-dast-and-sast-tools` |
| Owasp Complete Vulnerable Labs Application Security | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/OWASP-Complete-Vulnerable-Labs-Application-Security) | `labs/misc/owasp-complete-vulnerable-labs-application-security` |
| Owasp Vulnerable App | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/OWASP-Vulnerable-App) | `labs/misc/owasp-vulnerable-app` |
| Owasp Wrongsecrets | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/OWASP-WrongSecrets) | `labs/misc/owasp-wrongsecrets` |
| Public Pentesting Reports | Collection of public pentesting reports. | [GitHub](https://github.com/lucashgrifoni/Public-Pentesting-Reports) | `labs/misc/public-pentesting-reports` |
| Spring4Shell Poc Application | Vulnerable Java/Spring application. | [GitHub](https://github.com/lucashgrifoni/Spring4Shell-PoC-Application) | `labs/misc/spring4shell-poc-application` |
| Sqlite Lab | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/sqlite-lab) | `labs/misc/sqlite-lab` |
| Template Injection Workshop | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Template-Injection-Workshop) | `labs/misc/template-injection-workshop` |
| Vulhub Vulnerable Docker Application | Vulnerable Docker containerized application. | [GitHub](https://github.com/lucashgrifoni/Vulhub-Vulnerable-Docker-Application) | `labs/misc/vulhub-vulnerable-docker-application` |
| Vulnerable Adversely Programmed Interface | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Adversely-Programmed-Interface) | `labs/misc/vulnerable-adversely-programmed-interface` |
| Vulnerable Client Server Application Vucsa | Vulnerable application for security testing and training. | [GitHub](https://github.com/lucashgrifoni/Vulnerable-Client-Server-Application-VuCSA) | `labs/misc/vulnerable-client-server-application-vucsa` |

## External Resources

The following resources are referenced but not included as submodules (external links, non-GitHub repositories, or resources that require manual access):

- **AWSGoat**: A Damn Vulnerable AWS Infrastructure - [Link](https://lnkd.in/dq2cYPG2)
- **AzureGoat**: A Damn Vulnerable Azure Infrastructure - [Link](https://lnkd.in/dKMMrESA)
- **GCPGoat**: A Damn Vulnerable GCP Infrastructure - [Link](https://lnkd.in/dMVmNuvZ)
- **DeFi**: Damn Vulnerable DeFi - [Link](https://lnkd.in/dbWesvxW)
- **Webpentest**: A Damn Vulnerable Web Application - [Link](https://lnkd.in/dNJxX-Fe)
- **WebSockets**: A Damn Vulnerable Web Sockets - [Link](https://lnkd.in/dMbJgP5h)
- **DVHMA**: Damn Vulnerable Hybrid Mobile App - [Link](https://lnkd.in/dSMZMuzZ)
- **CICD**: Deliberately vulnerable CI/CD environment - [Link](https://lnkd.in/dCxZb88q)
- **GraphQL**: Damn Vulnerable GraphQL Application - [Link](https://lnkd.in/d5V6P9HA)
- **WebServices**: Damn Vulnerable Web Services - [Link](https://lnkd.in/dAu8HAyd)
- **VamPI**: Vulnerable API - [Link](https://lnkd.in/dRPpBNjj)
- **DVSA**: Damn Vulnerable Serverless Application - [Link](https://lnkd.in/dnvdNcfq)
- **DVTA**: DVTA is a Vulnerable Thick Client Application - [Link](https://lnkd.in/dDhEDgdx)
- **DVJA**: Damn Vulnerable Java Application - [Link](https://lnkd.in/dqFyjYWP)
- **DVID**: Damn Vulnerable IoT Device - [Link](https://lnkd.in/dNV2RjUj)
- **DVPWA**: Damn Vulnerable Python Web Application - [Link](https://lnkd.in/diDvsz8u)
- **DVAS**: Damn Vulnerable Application Scanner - [Link](https://lnkd.in/dq_aC4pX)
- **DVB**: Damn Vulnerable Bank - [Link](https://lnkd.in/dyGWJzxD)
- **DVWPS**: Damn Vulnerable WordPress Site - [Link](https://lnkd.in/dkY-tXHe)
- **DVNA**: Damn Vulnerable NodeJS Application - [Link](https://lnkd.in/ds3JReM5)
- **DVRA**: Damn Vulnerable Ruby on Rails - [Link](https://lnkd.in/djQ_ehzi)
- **DVGM**: Damn Vulnerable Grade Management - [Link](https://lnkd.in/dAepn4K7)
- **Tiredful**: Tiredful API - [Link](https://lnkd.in/d3NjivMu)
- **DVCSharp**: Damn Vulnerable C# Application - [Link](https://lnkd.in/d8cZxdnr)
- **DVIA**: Damn Vulnerable iOS App - [Link](https://lnkd.in/dJqPp-d9)
- **DVIA2**: Damn Vulnerable iOS App 2 - [Link](https://lnkd.in/dhGUXurv)
- **DVRF**: Damn Vulnerable Router Firmware - [Link](https://lnkd.in/dUda_XsF)
- **DVFaaS**: Damn Vulnerable Functions as a Service - [Link](https://lnkd.in/drVpszwD)
- **DVCA**: Damn Vulnerable Cloud Application - [Link](https://lnkd.in/dPyKYKw4)
- **CRPYA**: Certified Red Team Python Analyst - [Link](https://lnkd.in/d-e_nXVW)

*Note: These external resources may require manual access or may point to repositories outside GitHub. Please follow the upstream documentation for setup instructions.*

## Known Issues

### Windows Path Length Limitations

Some labs may fail to clone on Windows due to the 260-character path length limitation:
- `labs/web/owasp-security-shepherd` - Contains very long Android build paths
- `labs/misc/application-security-dev-labs` - Contains long Drupal module paths
- `labs/web/unsafe-bank-application-security-web-android-and-ios` - Contains long iOS Pod paths

**Workaround**: Enable long path support in Windows 10/11:
1. Run PowerShell as Administrator
2. Execute: `New-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Control\FileSystem" -Name "LongPathsEnabled" -Value 1 -PropertyType DWORD -Force`
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

### Hub Maintainer

This hub is maintained as a community resource for security education and training purposes.

---

**Disclaimer**: This repository is for educational purposes only. The vulnerable applications contained herein should only be used in isolated, controlled environments. The maintainers are not responsible for any misuse of these resources.

