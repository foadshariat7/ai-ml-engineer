# Wrapper around `uv` that keeps the virtual environment on local disk
# instead of on this shared mac/windows drive.
#
# Why: a venv created on one OS (symlinks, Lib/Scripts vs lib/bin, .exe
# shims) is not usable on the other, and syncing venv files over the
# network share is slow and prone to file locks. Each OS gets its own
# local venv at $env:USERPROFILE\.venvs\<project-name>, keyed by hostname
# so this also works if you hop between multiple Windows machines.
#
# Usage:
#   .\scripts\dev.ps1 sync
#   .\scripts\dev.ps1 run src\ai_ml_engineer\04_data_structure.py
#   .\scripts\dev.ps1 add requests
$ErrorActionPreference = "Stop"

$ProjectDir = Split-Path -Parent $PSScriptRoot
$ProjectName = Split-Path -Leaf $ProjectDir

$env:UV_PROJECT_ENVIRONMENT = Join-Path $env:USERPROFILE ".venvs\$ProjectName-$env:COMPUTERNAME"

# Left over from a macOS-side activation; on Windows it points at a
# /Volumes path and only produces a confusing warning.
Remove-Item Env:\VIRTUAL_ENV -ErrorAction SilentlyContinue

Push-Location $ProjectDir
try {
    uv @args
}
finally {
    Pop-Location
}
