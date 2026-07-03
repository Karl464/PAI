# Mistral Vibe CLI — Windows Install & Config (Quick Reference)

**What it is:** Mistral's official open-source (Apache 2.0) terminal coding agent, powered by the Devstral 2 model family (also works with other providers/local models). "Vibe Code" is included with Mistral Free/Pro plans, or usable pay-as-you-go with an API key.

> Mistral officially supports and targets UNIX environments but confirms Vibe **works on Windows**.

## 1. Prerequisites

- Python 3.12+ (for manual/uv-based installs)
- (Optional) a Mistral account, for Mistral-hosted models — Vibe also runs fully offline against local models or any OpenAI-compatible API key you supply

## 2. Install (Windows)

Install `uv` (Astral's Python tool installer) first via PowerShell, then:
```powershell
uv tool install mistral-vibe
```
The installer checks for `uv`, installs/upgrades `mistral-vibe`, and exposes the `vibe` and `vibe-acp` commands — provided your PATH is configured (uv normally handles this automatically).

Confirm Python version if installing manually:
```powershell
python3 --version
```

## 3. Authenticate / configure a key

```powershell
vibe
```
First run (or any time the API key is missing) triggers an interactive setup wizard, or run it explicitly:
```powershell
vibe --setup
```
Choose:
- **Mistral account** (Free/Pro/higher — Vibe Code included, rate limits apply, with pay-as-you-go beyond included budget where available), or
- **API key** from Mistral Studio/console.mistral.ai (pasted into the wizard, saved to `~/.vibe/.env`)

Or set directly:
```powershell
$env:MISTRAL_API_KEY = "<your key>"
```

## 4. Configuration essentials

- Config file: `.vibe/config.toml` (project-level, checked first) falling back to `~/.vibe/config.toml` (user-level). Override the whole home dir with `VIBE_HOME`.
- **Agent profiles** (switch with a flag or slash command):
  - `default` — requires approval for tool executions
  - `plan` — read-only, auto-approves safe tools (grep/read) — good first pass on an unfamiliar/untrusted codebase
  - `accept-edits` — auto-approves file edits only
  - `auto-approve` — approves everything; use with caution
- Skills: `~/.vibe/skills/` (user-level) and `~/.agents/skills/` (shared cross-tool location — same convention some other agents use).
- Trusted folders: first run in a project containing a `.vibe/` directory asks whether you trust it before loading local config.
- ACP (Agent Client Protocol) support lets Vibe plug into editors — VS Code, JetBrains, Zed — via the same engine as the CLI.
- If config gets into a bad state:
  ```powershell
  mv ~/.vibe/config.toml ~/.vibe/config.toml.bkp
  vibe
  ```
  regenerates a fresh default config.

## 5. Verify

```powershell
vibe --version
```
Or check for updates:
```powershell
vibe --check-upgrade
```

## 6. Check usage / remaining budget

Vibe doesn't currently expose a dedicated `/usage` slash command. Options instead:

- **Cap spend per run:** `vibe --prompt "..." --max-price 2.00` sets a hard dollar ceiling for that session — the agent stops rather than overspending. Good default to add for unattended/scripted runs.
- **Session logs:** enabled by default, written to `~/.vibe/logs/session` (configurable via `[session_logging]` in `config.toml`) — contains per-session token/request detail you can review after the fact.
- **Mistral account users:** check consumption and remaining plan budget at your Mistral account dashboard (console.mistral.ai / your plan's billing page) — this is the authoritative source since Vibe itself doesn't surface a live quota meter.
- **API-key users:** the same console shows API spend directly against your key.

## 7. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `vibe` not recognized | `uv` didn't add its tool-install bin dir to PATH | Reopen terminal; check `uv tool dir` and add it to User PATH manually if needed |
| CLI misbehaves after manual config edit | Malformed `config.toml` | Move it aside (see above) and let Vibe regenerate a default |
| Auto-approve caused an unwanted change | `auto-approve` profile in use | Switch to `default` or `plan` profile for review-gated work |

## 7. Start using it

```powershell
cd C:\path\to\your\project
vibe
```
