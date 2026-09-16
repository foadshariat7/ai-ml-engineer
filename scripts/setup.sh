#!/usr/bin/env bash
# One-time-per-machine setup for macOS. Run this after switching from Windows.
#
# This project folder is a shared mac/windows drive, but a virtual
# environment is NOT portable across operating systems: the interpreter is
# a native binary, and the layout differs (bin/ + symlinks on macOS vs
# Scripts/ + python.exe on Windows). Putting .venv in the shared folder
# means each OS clobbers the other's environment. Venv files over SMB are
# also slow and prone to file locks.
#
# So: source stays on the share, the venv lives on local disk, one per
# machine. Windows has its own copy at scripts/setup.ps1.
#
#   ./scripts/setup.sh
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"
VENV_DIR="$HOME/.venvs/${PROJECT_NAME}-$(hostname -s)"

cd "$PROJECT_DIR"

# Inherited from a Windows-side activation, this points at a D:\ path and
# only produces confusing warnings on macOS.
unset VIRTUAL_ENV

echo "==> Creating environment at $VENV_DIR"
mkdir -p "$(dirname "$VENV_DIR")"
UV_PROJECT_ENVIRONMENT="$VENV_DIR" uv sync

# A .venv left behind by Windows is dead weight here. It often cannot be
# deleted from macOS while the Windows side still holds an SMB lock on
# Scripts/python.exe, so this is best-effort.
if [[ -e .venv ]]; then
  echo "==> Removing stale .venv from the shared drive"
  if ! rm -rf .venv 2>/dev/null; then
    echo "    Could not remove it (locked over SMB, likely open on Windows)."
    echo "    Harmless - nothing uses it now. Delete it from Windows when convenient."
  fi
fi

cat <<EOF

Done. Run code with:

  ./scripts/dev.sh run src/ai_ml_engineer/04_data_structure.py
  ./scripts/dev.sh pytest
  ./scripts/dev.sh add <package>

Plain 'uv run' also works in any NEW terminal (a hook in ~/.zshrc exports
UV_PROJECT_ENVIRONMENT for projects on /Volumes). It will keep failing in
terminals opened earlier - dev.sh works in those too.

VS Code: Command Palette -> "Python: Select Interpreter" -> Enter path:
  $VENV_DIR/bin/python
EOF
