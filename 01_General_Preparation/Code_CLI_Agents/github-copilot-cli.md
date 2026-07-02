# GitHub Copilot CLI — Windows Install & Config (Quick Reference)

**What it is:** GitHub's terminal AI coding agent, using the same agentic harness as Copilot's coding agent. Included with all Copilot plans (Free, Pro, Pro+, Max, Business, Enterprise) — no separate billing. Natively supports Windows.

## 1. Prerequisites

- A GitHub account with an active Copilot subscription (Business/Enterprise admins must enable Copilot CLI for the org)
- Node.js 22+ and npm 10+ (if installing via npm)
- PowerShell 6+ recommended on Windows for npm-based install

## 2. Install (native Windows)

WinGet:
```powershell
winget install GitHub.Copilot
```
Prerelease channel:
```powershell
winget install GitHub.Copilot.Prerelease
```

npm (cross-platform):
```powershell
npm install -g @github/copilot
```

You can also download a Windows installer / source bundle directly from the `copilot-cli` GitHub releases page if you need to pin a version or your environment blocks the commands above.

Close and reopen your terminal after install so `copilot` is picked up.

## 3. Authenticate

```powershell
copilot
```
Then inside the CLI:
```
/login
```
Follow the on-screen device-auth flow to sign in with GitHub.

**Alternative — fine-grained PAT:** create a token at `github.com/settings/personal-access-tokens/new` with the **Copilot Requests** permission, then set it as an environment variable (checked in this precedence order): `COPILOT_GITHUB_TOKEN`, `GH_TOKEN`, `GITHUB_TOKEN`.

```powershell
$env:GITHUB_TOKEN = "<your-pat>"
```

## 4. Configuration essentials

- Default model is Claude Sonnet 4.5; switch with `/model` inside a session (also supports GPT-5, Claude Sonnet 4, and others depending on plan).
- Environment variable override: `$env:COPILOT_MODEL = "<model-name>"`.
- **LSP support:** for richer code intelligence (go-to-definition, diagnostics), configure Language Server Protocol servers:
  - User-level: `~/.copilot/lsp-config.json` (all projects)
  - Repo-level: `.github/lsp.json` (this project only)
  - Example config: `{ "lspServers": { "typescript": { "command": "typescript-language-server", "args": ["--stdio"] } } }`
  - Check what's active with `/lsp` inside the CLI.
- **Experimental mode:** `copilot --experimental` or `/experimental` inside the CLI. Setting persists after first use.
- **Autopilot mode:** press `Shift+Tab` to cycle modes; Autopilot keeps the agent working until the task is done.
- Non-interactive/scripted use: `copilot -p "<prompt>"`, add `-s` for response-only output (no usage banner) — good for CI pipelines.

## 5. Verify

```powershell
copilot --version
```

## 6. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Copilot CLI not available for your account | Free plan, or org admin hasn't enabled it | Confirm a paid Copilot plan; ask your GitHub org admin to enable Copilot CLI |
| Install fails via npm | Node/npm too old | Upgrade to Node 22+, npm 10+ |
| `copilot` not recognized | Terminal not reopened, or npm/WinGet path not refreshed | Close and reopen terminal |
| Session feels slow on long conversations | Context window filling up | Run `/compact`, or switch to a faster model with `/model` (e.g. Claude Haiku 4.5) |

## 7. Start using it

```powershell
cd C:\path\to\your\project
copilot
```
Confirm you trust the current directory when prompted, then start prompting.
