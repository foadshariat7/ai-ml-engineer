# One-time-per-machine setup for Windows. Run this after switching from macOS.
#
# This project folder is a shared mac/windows drive, but a virtual
# environment is NOT portable across operating systems: the interpreter is
# a native binary, and the layout differs (Scripts/ + python.exe on Windows
# vs bin/ + symlinks on macOS). Putting .venv in the shared folder means
# each OS clobbers the other's environment.
#
# So: source stays on the share, the venv lives on local disk, one per
# machine. macOS has its own copy at scripts/setup.sh.
#
#   .\scripts\setup.ps1
$ErrorActionPreference = "Stop"

$ProjectDir = Split-Path -Parent $PSScriptRoot
$ProjectName = Split-Path -Leaf $ProjectDir
$VenvDir = Join-Path $env:USERPROFILE ".venvs\$ProjectName-$env:COMPUTERNAME"

Push-Location $ProjectDir
try {
    # Inherited from a macOS-side activation, this points at a /Volumes
    # path and only produces confusing warnings on Windows.
    Remove-Item Env:\VIRTUAL_ENV -ErrorAction SilentlyContinue

    Write-Host "==> Creating environment at $VenvDir"
    New-Item -ItemType Directory -Force -Path (Split-Path -Parent $VenvDir) | Out-Null
    $env:UV_PROJECT_ENVIRONMENT = $VenvDir
    uv sync
    if ($LASTEXITCODE -ne 0) { throw "uv sync failed" }

    # A .venv left behind by macOS is dead weight here.
    if (Test-Path ".venv") {
        Write-Host "==> Removing stale .venv from the shared drive"
        try {
            Remove-Item -Recurse -Force ".venv" -ErrorAction Stop
        }
        catch {
            Write-Host "    Could not remove it (likely still open on macOS)."
            Write-Host "    Harmless - nothing uses it now. Delete it later."
        }
    }

    Write-Host @"

Done. Run code with:

  .\scripts\dev.ps1 run src\ai_ml_engineer\04_data_structure.py
  .\scripts\dev.ps1 pytest
  .\scripts\dev.ps1 add <package>

To make a plain 'uv run' work too, paste scripts\profile-snippet.ps1 into
your PowerShell profile (`notepad `$PROFILE`) once, then open a new window.

VS Code: Command Palette -> "Python: Select Interpreter" -> Enter path:
  $VenvDir\Scripts\python.exe
"@
}
finally {
    Pop-Location
}
