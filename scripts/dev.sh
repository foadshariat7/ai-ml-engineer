#!/usr/bin/env bash
# Wrapper around `uv` that keeps the virtual environment on local disk
# instead of on this shared mac/windows drive.
#
# Why: a venv created on one OS (symlinks, Lib/Scripts vs lib/bin, .exe
# shims) is not usable on the other, and syncing venv files over the
# network share is slow and prone to file locks. Each OS gets its own
# local venv at ~/.venvs/<project-name>, keyed by hostname so this also
# works if you hop between multiple Macs.
#
# Usage:
#   ./scripts/dev.sh sync
#   ./scripts/dev.sh run src/ai_ml_engineer/04_data_structure.py
#   ./scripts/dev.sh add requests
set -euo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_NAME="$(basename "$PROJECT_DIR")"

export UV_PROJECT_ENVIRONMENT="$HOME/.venvs/${PROJECT_NAME}-$(hostname -s)"

# Left over from a Windows-side activation; on macOS it points at a D:\
# path and only produces a confusing warning.
unset VIRTUAL_ENV

cd "$PROJECT_DIR"
exec uv "$@"
