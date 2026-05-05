$ErrorActionPreference = "Stop"

$script = Join-Path $PSScriptRoot "00_system\scripts\audit_system.py"
$candidates = @()

$python = Get-Command python -ErrorAction SilentlyContinue
if ($python) {
    $candidates += @($python.Source)
}

$bundledPython = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if (Test-Path $bundledPython) {
    $candidates += @($bundledPython)
}

$py = Get-Command py -ErrorAction SilentlyContinue
if ($py) {
    $candidates += @($py.Source)
}

foreach ($candidate in $candidates | Select-Object -Unique) {
    & $candidate $script
    if ($LASTEXITCODE -eq 0) {
        exit 0
    }
}

Write-Error "No working Python executable found. Install Python or run with the Codex bundled Python path."
exit 1
