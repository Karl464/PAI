# OpenCode — Windows Install & Config (Quick Reference)

**What it is:** Open-source, provider-agnostic terminal coding agent (build/plan agent modes). Not tied to one model — works with Claude, ChatGPT, Gemini, Copilot, OpenRouter, local Ollama models, and more. Free/open under a permissive license.

## 1. Prerequisites

- Windows 10/11 (x64 or ARM64)
- A package manager (npm/Scoop/Chocolatey) or Bun/Node
- API key(s) for whichever LLM provider(s) you plan to use — or Ollama running locally for a fully offline setup

## 2. Install (native Windows)

Scoop (recommended on Windows — handles PATH automatically):
```powershell
scoop install opencode
```

Chocolatey:
```powershell
choco install opencode
```

npm:
```powershell
npm i -g opencode-ai@latest
```

**Known Windows npm-install issue:** a broken symlink can cause `EPERM` errors on install or `cannot execute binary file` errors on run. Workarounds:
1. Enable **Developer Mode** in Windows Settings before installing (grants the needed symlink permission), **or**
2. If already broken: locate `node_modules\opencode-ai\bin\` under your npm global folder, and replace the shim with a direct copy of `node_modules\opencode-windows-x64\bin\opencode.exe`.

If this is fiddly, Scoop or Chocolatey avoid the issue entirely — prefer those on Windows.

**Desktop app (optional, separate from CLI):** download the Windows `.exe`/MSI from opencode.ai/download.

## 3. Authenticate / connect a provider

```powershell
opencode
```
On first launch it prompts you to connect a provider. Interactively:
```
/connect
```
Walks you through selecting a provider (OpenAI, Google, Anthropic, OpenRouter, etc.) and entering an API key. Credentials are stored at `~/.local/share/opencode/auth.json` (Windows equivalent path under your user profile).

For local models via Ollama (no API key needed):
```powershell
ollama pull qwen2.5-coder:32b
```
OpenCode auto-detects Ollama running on `localhost:11434`.

> Note: some Anthropic-model access through third-party wrapper tools like OpenCode has been restricted at times — if Claude models aren't available through your OpenCode setup, fall back to Claude Code directly, or use OpenAI/Gemini/local models within OpenCode.

## 4. Configuration essentials

- Project context file: run `opencode init` inside a project to generate an **`AGENTS.md`** describing project structure and conventions — commit this to git.
- Built-in agent modes, toggle with `Tab`:
  - `build` — default, full-access agent for development
  - `plan` — read-only, denies file edits by default; good for exploring an unfamiliar codebase (e.g. a binary security review target) before letting the agent touch anything
- `@general` subagent for complex multi-step searches.
- MCP servers, plugins, and GitHub/GitLab integrations available — see `opencode.ai/docs`.

## 5. Verify

```powershell
opencode --version
```

## 6. Check token usage / remaining budget

```powershell
opencode stats
opencode stats --days 7
```
Shows token usage and cost statistics for your OpenCode sessions: total cost, avg cost/day, tokens by category (input/output/cache read/cache write), session and message counts, over a chosen window. Since OpenCode is provider-agnostic, "budget" here means your token spend against whichever provider(s) you've connected — check the provider's own console (e.g. Anthropic Console, OpenAI Platform) for the actual dollar balance/limit.

```powershell
opencode debug config
```
Useful alongside `stats` to confirm which provider/model config is actually active when spend looks unexpected.

## 7. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `EPERM` during npm install | Symlink permission issue on standard Windows account | Enable Developer Mode, or install via Scoop/Chocolatey instead |
| `cannot execute binary file` in Git Bash/PowerShell | Broken shim from a failed symlink | Replace shim with a direct copy of the platform `.exe` (see above), or reinstall via Scoop |
| Claude models unavailable | Provider access restriction on third-party tools | Use Claude Code directly for Claude, or switch to another provider in OpenCode |

## 7. Start using it

```powershell
cd C:\path\to\your\project
opencode
```
