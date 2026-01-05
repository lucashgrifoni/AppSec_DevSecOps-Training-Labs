# Bootstrap script for Vulnerable Labs Hub (Windows PowerShell)
# Initializes git submodules and lists available labs

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Vulnerable Labs Hub - Bootstrap" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Check for git
try {
    $null = Get-Command git -ErrorAction Stop
} catch {
    Write-Host "ERROR: git is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Check for docker (optional, just a warning)
try {
    $null = Get-Command docker -ErrorAction Stop
} catch {
    Write-Host "WARNING: docker is not installed. Some labs may require Docker." -ForegroundColor Yellow
    Write-Host ""
}

Write-Host "Initializing git submodules..." -ForegroundColor Green
git submodule update --init --recursive

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Available Labs by Category" -ForegroundColor Cyan
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

# Count and list labs by category
$categories = @("web", "api", "mobile", "cloud", "cicd", "language", "misc")

foreach ($category in $categories) {
    $categoryPath = "labs\$category"
    if (Test-Path $categoryPath) {
        $labs = Get-ChildItem -Path $categoryPath -Directory -ErrorAction SilentlyContinue
        if ($labs) {
            Write-Host "[$category] $($labs.Count) lab(s):" -ForegroundColor Yellow
            foreach ($lab in $labs) {
                Write-Host "  - $($lab.Name)" -ForegroundColor White
            }
            Write-Host ""
        }
    }
}

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "Bootstrap complete!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "1. Navigate to a lab: cd labs\<category>\<lab-name>"
Write-Host "2. Check for docker-compose.yml: ls docker-compose.yml"
Write-Host "3. Start the lab: docker compose up -d"
Write-Host "4. Or follow the upstream README for specific instructions"
Write-Host ""

