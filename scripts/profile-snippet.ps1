# Optional: makes a bare `uv run ...` work on Windows without going
# through scripts\dev.ps1, mirroring the zsh hook used on macOS.
#
# Install once per Windows machine:
#   notepad $PROFILE      # create it if prompted, then paste the block below
#
# It only applies to projects on the shared drive, so normal local
# projects keep using their own .\.venv as usual. Adjust the drive letter
# if the share is mounted somewhere other than D:.

function Set-UvLocalEnv {
    $root = (Get-Location).Path
    while ($root -and -not (Test-Path (Join-Path $root "pyproject.toml"))) {
        $root = Split-Path -Parent $root
    }
    if ($root -and $root -like "D:\*") {
        $name = Split-Path -Leaf $root
        $env:UV_PROJECT_ENVIRONMENT = Join-Path $env:USERPROFILE ".venvs\$name-$env:COMPUTERNAME"
    }
    else {
        Remove-Item Env:\UV_PROJECT_ENVIRONMENT -ErrorAction SilentlyContinue
    }
}

# PowerShell has no chpwd hook, so re-evaluate at each prompt.
function prompt {
    Set-UvLocalEnv
    "PS $($executionContext.SessionState.Path.CurrentLocation)$('>' * ($nestedPromptLevel + 1)) "
}
