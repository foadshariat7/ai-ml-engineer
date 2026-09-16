# ai-ml-engineer

Course work and notes, managed with [uv](https://docs.astral.sh/uv/).

## Working across macOS and Windows

This folder lives on a drive shared between a Mac and a Windows machine, so the
setup has one rule behind it:

> Source code and `uv.lock` live on the shared drive. The virtual environment
> does **not**.

A venv isn't portable across operating systems — the interpreter is a native
binary and the layout differs (`bin/` with symlinks on macOS vs `Scripts/` with
`python.exe` on Windows). A `.venv` in the shared folder means each OS clobbers
the other's, and venv files over SMB are slow and prone to file locks.

Instead each machine gets its own venv at `~/.venvs/<project>-<hostname>`, and
the scripts in [`scripts/`](scripts/) point `uv` there by setting
`UV_PROJECT_ENVIRONMENT`. The hostname suffix means this also works across
several Macs or several Windows boxes.

### macOS

One time per Mac:

```bash
./scripts/setup.sh
```

That creates the local venv and installs a hook in `~/.zshrc`. After it, plain
`uv` just works, because the hook sets `UV_PROJECT_ENVIRONMENT` on every `cd`
into a project under `/Volumes/*`:

```bash
uv run src/ai_ml_engineer/04_data_structure.py
uv run pytest
uv add requests
uv sync                  # after pulling changes made on Windows
```

The hook only applies to terminals opened *after* setup ran. If `uv` complains
about a `D:\` path or starts rebuilding a `.venv` in the project folder, you're
in a stale shell. The wrapper works regardless:

```bash
./scripts/dev.sh run pytest
```

### Windows

One time per Windows machine:

```powershell
.\scripts\setup.ps1
```

Then use the wrapper:

```powershell
.\scripts\dev.ps1 run src\ai_ml_engineer\04_data_structure.py
.\scripts\dev.ps1 pytest
.\scripts\dev.ps1 add requests
.\scripts\dev.ps1 sync          # after pulling changes made on macOS
```

To get a bare `uv run` working like on the Mac, paste
[`scripts/profile-snippet.ps1`](scripts/profile-snippet.ps1) into your
PowerShell profile once (`notepad $PROFILE`) and open a new window. Check the
drive letter first: the snippet matches paths under `D:\`. If the share is
mounted elsewhere, edit that line — otherwise the hook silently does nothing
and `uv` goes back to creating a `.venv` on the share.

### Switching machines

Whichever side you land on, run that OS's sync after pulling — `uv sync` on
macOS, `.\scripts\dev.ps1 sync` on Windows. The lock file is shared, the venvs
aren't, so each machine has to catch up on its own. It's a cheap no-op when
nothing changed.

### VS Code

Don't commit an interpreter path to `.vscode/settings.json` — that file is on
the shared drive, so a hardcoded path breaks the other OS. Select it per
machine instead: Command Palette → **Python: Select Interpreter** → *Enter
interpreter path*.

| OS      | Path                                                       |
| ------- | ---------------------------------------------------------- |
| macOS   | `~/.venvs/ai-ml-engineer-<hostname>/bin/python`             |
| Windows | `%USERPROFILE%\.venvs\ai-ml-engineer-<COMPUTERNAME>\Scripts\python.exe` |

### Script reference

| Script                      | Purpose                                              |
| --------------------------- | ---------------------------------------------------- |
| `scripts/setup.sh`          | One-time macOS setup: local venv + `~/.zshrc` hook   |
| `scripts/dev.sh`            | `uv` wrapper for macOS, works in any shell            |
| `scripts/setup.ps1`         | One-time Windows setup: local venv                    |
| `scripts/dev.ps1`           | `uv` wrapper for Windows                              |
| `scripts/profile-snippet.ps1` | Optional PowerShell profile hook for bare `uv run` |
