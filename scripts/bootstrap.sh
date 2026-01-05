#!/bin/bash
# Bootstrap script for Vulnerable Labs Hub
# Initializes git submodules and lists available labs

set -e

echo "=========================================="
echo "Vulnerable Labs Hub - Bootstrap"
echo "=========================================="
echo ""

# Check for git
if ! command -v git &> /dev/null; then
    echo "ERROR: git is not installed or not in PATH"
    exit 1
fi

# Check for docker (optional, just a warning)
if ! command -v docker &> /dev/null; then
    echo "WARNING: docker is not installed. Some labs may require Docker."
    echo ""
fi

echo "Initializing git submodules..."
git submodule update --init --recursive

echo ""
echo "=========================================="
echo "Available Labs by Category"
echo "=========================================="
echo ""

# Count and list labs by category
categories=("web" "api" "mobile" "cloud" "cicd" "language" "misc")

for category in "${categories[@]}"; do
    if [ -d "labs/$category" ]; then
        count=$(find "labs/$category" -mindepth 1 -maxdepth 1 -type d | wc -l)
        if [ "$count" -gt 0 ]; then
            echo "[$category] $count lab(s):"
            for lab in labs/$category/*/; do
                if [ -d "$lab" ]; then
                    lab_name=$(basename "$lab")
                    echo "  - $lab_name"
                fi
            done
            echo ""
        fi
    fi
done

echo "=========================================="
echo "Bootstrap complete!"
echo "=========================================="
echo ""
echo "Next steps:"
echo "1. Navigate to a lab: cd labs/<category>/<lab-name>"
echo "2. Check for docker-compose.yml: ls docker-compose.yml"
echo "3. Start the lab: docker compose up -d"
echo "4. Or follow the upstream README for specific instructions"
echo ""

