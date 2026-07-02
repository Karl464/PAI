# Claude Code — Windows Install & Config (Quick Reference)

**What it is:** Anthropic's agentic terminal coding tool. Native CLI (`claude`), also bundled in the Claude desktop app (Pro/Max/Team/Enterprise for the Code tab).

## 1. Install (no admin needed)

Standard PowerShell (not elevated):

```powershell
irm https://claude.ai/install.ps1 | iex
```

Installs to `C:\Users\<you>\.local\bin\claude.exe`. Doesn't touch `Program Files`/`ProgramData` — no elevation needed.

**Desktop app (optional):** claude.com/download. Bundles Claude Code internally (no separate Node.js/CLI needed). Requires Pro/Max/Team/Enterprise for the Code tab. Not available on Linux (CLI only there).

## 2. Add to PATH

Use **User PATH**, not System PATH (install is per-user):

```powershell
$claudeBin = "$env:USERPROFILE\.local\bin"
$current = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($current -notlike "*$claudeBin*") {
    [Environment]::SetEnvironmentVariable("PATH", "$current;$claudeBin", "User")
}
```

GUI alternative: `Win+R` → `sysdm.cpl` → Advanced → Environment Variables → **User variables** → `Path` → New → `%USERPROFILE%\.local\bin`

Close and reopen your terminal afterward.

## 3. Verify

```powershell
$env:Path -split ';' | Select-String '\.local\\bin'
claude --version
claude doctor
```

`claude doctor` = full health check (PATH, install method, auth status, updates).

## 4. Configuration

Claude Code reads config at several layers, most-specific wins:

| Scope | Location | Purpose |
|---|---|---|
| User | `~/.claude/settings.json` (`%USERPROFILE%\.claude\settings.json`) | Personal defaults across all projects |
| Project (shared) | `.claude/settings.json` in repo root | Team-shared settings, commit to git |
| Project (local) | `.claude/settings.local.json` | Personal overrides for this repo, gitignore it |
| Enterprise | Managed policy file | IT-pushed, highest precedence |

**Project instructions — `CLAUDE.md`:** Place at repo root. Auto-loaded every session. Put build/test commands, code style, architecture notes, "don't touch X" rules here. Run `/init` inside a project to auto-generate a starter `CLAUDE.md`.

**Model selection:**
```powershell
$env:ANTHROPIC_MODEL = "claude-sonnet-5"
```
Or use `/model` inside a session to switch interactively.

**Third-party model backends** (e.g. routing to another provider's API): set `ANTHROPIC_BASE_URL` and `ANTHROPIC_AUTH_TOKEN` before launching `claude`. Useful if your org routes through a gateway.

**MCP servers:** configured in `.mcp.json` (project) or via `claude mcp add` (writes to user config). Lets Claude Code call external tools (databases, ticketing systems, internal APIs).

**Permissions:** `settings.json` supports an `permissions` block (`allow`/`ask`/`deny` lists per tool) so you can pre-approve safe commands (e.g. `git status`) and always gate risky ones (e.g. `rm`). Good practice for a security-review workflow where you want deterministic tool gating.

**Skills:** drop reusable methodology packages under `~/.claude/skills/<name>/SKILL.md` (user-level, all projects) or `.claude/skills/` (project-level). Claude auto-discovers and loads relevant ones — this is where a custom Ghidra/PyGhidra SAST skill would live.

## 5. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `claude` not recognized | PATH not picked up yet | Close & reopen terminal; re-check PATH (step 2) |
| Permission denied | Installed with `sudo`/elevated, or npm-based install | Don't use sudo — reinstall with the native installer |
| Can't write to a folder | Folder is outside your profile (e.g. inside `Program Files`) | Work in a user-owned folder, or grant write access |
| Unsure if PowerShell is elevated | — | Check window title ("Administrator:" prefix) |

## 6. Start using it

```powershell
cd C:\path\to\your\project
claude
```
First run opens a browser to log in with your Anthropic account.
