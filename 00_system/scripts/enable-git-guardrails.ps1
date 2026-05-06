param()

$ErrorActionPreference = "Stop"

$repoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$hooksPath = ".githooks"
$commitTemplate = "00_system/templates/git-commit-template.txt"

Write-Host "Enabling Git guardrails for $repoRoot" -ForegroundColor Green

Push-Location $repoRoot
try {
    & git config --local core.hooksPath $hooksPath
    & git config --local commit.template $commitTemplate

    Write-Host ""
    Write-Host "Enabled local Git settings:" -ForegroundColor Cyan
    Write-Host "core.hooksPath = $hooksPath"
    Write-Host "commit.template = $commitTemplate"
    Write-Host ""
    Write-Host "Use this before a commit:"
    Write-Host "& '.\00_system\scripts\git-safe.ps1'"
}
finally {
    Pop-Location
}
