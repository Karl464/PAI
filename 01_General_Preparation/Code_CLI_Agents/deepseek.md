# DeepSeek — Windows Install & Config (Quick Reference)

**What it is:** DeepSeek doesn't ship one official first-party CLI coding agent. Instead, DeepSeek's official docs recommend **BYOK (bring your own key)**: point an existing coding CLI (Claude Code, GitHub Copilot CLI, OpenCode, etc.) at DeepSeek's Anthropic-compatible or OpenAI-compatible API endpoint. There's also **Deep Code CLI**, a community-built terminal agent listed in DeepSeek's own integration docs, plus several independent community DeepSeek CLIs.

## Option A — BYOK into Claude Code (official, recommended)

Reuses the Claude Code install (see the `claude-code.md` guide in this folder) but points it at DeepSeek instead of Anthropic's API:

```powershell
$env:ANTHROPIC_BASE_URL = "https://api.deepseek.com/anthropic"
$env:ANTHROPIC_AUTH_TOKEN = "<your DeepSeek API Key>"
$env:ANTHROPIC_MODEL = "deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_OPUS_MODEL = "deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_SONNET_MODEL = "deepseek-v4-pro[1m]"
$env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "deepseek-v4-flash"
```
Get your API key from the DeepSeek Platform (platform.deepseek.com). Then run `claude` as normal.

## Option B — BYOK into GitHub Copilot CLI

```powershell
$env:COPILOT_PROVIDER_TYPE = "anthropic"
$env:COPILOT_PROVIDER_BASE_URL = "https://api.deepseek.com/anthropic"
$env:COPILOT_PROVIDER_API_KEY = "sk-your-deepseek-api-key"
$env:COPILOT_MODEL = "deepseek-v4-pro"
```
**Important:** use `anthropic` as the provider type, not `openai` — DeepSeek's thinking mode requires `reasoning_content` to be echoed back on subsequent requests, which Copilot CLI's OpenAI-mode integration doesn't support; the Anthropic-compatible endpoint avoids the issue. Since `deepseek-v4-pro` isn't in Copilot's built-in model catalog, also set token limits explicitly (see DeepSeek's Copilot integration doc for current values).

## Option C — Deep Code CLI (community, DeepSeek-listed)

```powershell
npm install -g @vegamo/deepcode-cli
deepcode --version
```
Config file at `~/.deepcode/settings.json` (Windows: `%USERPROFILE%\.deepcode\settings.json`):
```json
{
  "env": {
    "MODEL": "deepseek-v4-pro",
    "BASE_URL": "https://api.deepseek.com",
    "API_KEY": "sk-..."
  },
  "thinkingEnabled": true,
  "reasoningEffort": "max"
}
```
Windows support is documented but less battle-tested than macOS/Linux — if `deepcode` isn't found post-install, the fix is almost always the npm global bin path missing from PATH (see Quick troubleshooting).

## Option D — direct API (no CLI)

For scripting/automation without any agent CLI, DeepSeek exposes an OpenAI-compatible endpoint directly:
```powershell
curl https://api.deepseek.com/chat/completions `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:DEEPSEEK_API_KEY" `
  -d '{"model":"deepseek-v4-pro","messages":[{"role":"user","content":"Hello!"}]}'
```

## Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `400` error on Copilot CLI with DeepSeek | Provider type set to `openai` | Switch `COPILOT_PROVIDER_TYPE` to `anthropic` |
| `deepcode`/community CLI command not found | npm global bin not on PATH | `npm config get prefix`, add `<prefix>` to User PATH, reopen terminal |
| Env vars don't persist across sessions | Set with `$env:` (session-only) | Add to PowerShell profile, or set permanently via System Properties → Environment Variables |

## Which option to pick

- Already using Claude Code or GitHub Copilot CLI for your security-review workflow? **Option A/B** — zero new tooling, just swap the backend.
- Want a DeepSeek-native terminal experience with its own settings file? **Option C**.
- Building your own automation/pipeline step? **Option D**.
