# Grok Build (xAI CLI) — Windows Install & Config (Quick Reference)

**What it is:** xAI's official terminal coding agent (early beta, launched May 2026), running on the `grok-build-0.1` model (256K context). Native Windows PowerShell installer. Requires a SuperGrok or X Premium+ subscription (or an xAI API key for headless/CI use).

> This is an **early beta** — expect breaking changes. Don't run it in auto-approve/"yolo" modes on systems or repos you care about.

## 1. Prerequisites

- SuperGrok or X Premium+ subscription, **or** an xAI API key (console.x.ai) for headless environments
- Windows 10/11, PowerShell

## 2. Install (native Windows)

```powershell
irm https://x.ai/cli/install.ps1 | iex
```

(macOS/Linux/WSL equivalent: `curl -fsSL https://x.ai/cli/install.sh | bash`)

## 3. Authenticate

```powershell
cd your-project
grok
```
First launch opens a browser for X-account authentication. For headless/CI/non-browser environments, use an API key instead:
```powershell
$env:XAI_API_KEY = "xai-..."
grok
```

## 4. Configuration essentials

- User-level config file: `%USERPROFILE%\.grok\config.toml` — add custom/self-hosted models here:
  ```toml
  [model.my-model]
  model = "model-id"
  base_url = "https://api.example.com/v1"
  name = "Display Name"
  env_key = "API_KEY"

  [models]
  default = "my-model"
  ```
- Project instructions: reads **`AGENTS.md`** (same convention as Codex/OpenCode) — plugins, hooks, skills, and MCP servers work with the same config format, so migrating from Claude Code/Codex configs is low-friction.
- Inspect what Grok Build discovered in the current directory (config sources, instructions, skills, MCP servers):
  ```powershell
  grok inspect
  ```
- **Plan mode** for complex/risky tasks — blocks edits until you review and approve the plan:
  ```powershell
  grok plan "task description"
  ```
- **Headless mode** for scripts/CI:
  ```powershell
  grok -p "explain this codebase" --output-format streaming-json
  ```
- Subagents run in parallel (up to 8) for larger tasks, each in its own git worktree if configured.

## 5. Verify

```powershell
grok --version
```

## 6. Check token usage / remaining budget

Inside a session:
```
/usage
```
Shows your current token and credit consumption. Same view is available via `/context` if you specifically want to see how much of the current context window is used.

For API-key/headless use, check remaining credits and spend at console.x.ai.

## 7. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Access denied / not available | Not a SuperGrok/X Premium+ subscriber | Subscribe, or use an xAI API key for API-based access instead |
| Auth fails on a headless/remote box | No browser available for OAuth | Set `XAI_API_KEY` instead of interactive login |
| Custom model not recognized | Missing `[models] default = "..."` entry | Confirm both the `[model.<name>]` block and the `default` pointer are set in `config.toml` |

## 7. Start using it

```powershell
cd C:\path\to\your\project
grok
```
Or one-shot: `grok exec "task description"`.
