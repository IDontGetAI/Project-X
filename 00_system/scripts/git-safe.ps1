param(
    [switch]$NoPause
)

$ErrorActionPreference = "Stop"

function Write-Section {
    param([string]$Title)
    Write-Host ""
    Write-Host "== $Title ==" -ForegroundColor Cyan
}

Write-Host "Knowledge Hub Git Safety Check" -ForegroundColor Green
Write-Host "Rule summary: check status, add precisely, write commit messages as 'Action + Object', confirm branch before push."

Write-Section "Current Branch"
& git branch --show-current

Write-Section "Working Tree"
& git status --short

Write-Section "Staged Summary"
& git diff --cached --stat

Write-Section "Recent Commits"
& git log --oneline -3

Write-Section "Recommended Flow"
Write-Host "1. git status --short"
Write-Host "2. git add [specific file or directory]"
Write-Host "3. git diff --cached --stat"
Write-Host "4. git commit"
Write-Host "5. git push origin main"

if (-not $NoPause) {
    Write-Host ""
    Read-Host "Check complete. Press Enter to continue"
}
