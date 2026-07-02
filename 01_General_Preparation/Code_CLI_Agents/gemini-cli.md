# Gemini CLI — Windows Install & Config (Quick Reference)

**What it is:** Google's open-source terminal AI agent (Apache 2.0), powered by Gemini models with a large (1M token) context window. MCP support, built-in Google Search grounding.

> Note: as of mid-2026, Google is steering unpaid-tier / Google One users toward **Antigravity CLI** instead (see separate guide) — Gemini CLI remains fully usable for Gemini Code Assist licensees and API-key users.

## 1. Prerequisites

- Node.js 20+ (18+ works but 20+ recommended)
- A Google account (for free-tier OAuth) or a Gemini API key, or a Gemini Code Assist license (individual/Standard/Enterprise)

## 2. Install

```powershell
npm install -g @google/gemini-cli
```

Try without installing:
```powershell
npx @google/gemini-cli
```

Release channels — stable is default; opt into preview/nightly if needed:
```powershell
npm install -g @google/gemini-cli@preview
npm install -g @google/gemini-cli@nightly
```

## 3. Windows-specific notes

Gemini CLI runs natively on Windows via npm, but the three most common Windows install failures are:
1. **PATH not updating** after global npm install → `gemini` not recognized
2. **PowerShell execution policy** blocking the `gemini.ps1` wrapper
3. **Node.js version incompatibility** — avoid Node 24/25 for now due to a known npm cache issue; use **Node 22 LTS**

Fix for execution-policy blocks (elevated PowerShell):
```powershell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
```

If PATH issues persist, add your npm global bin folder manually via System Properties → Environment Variables, then reopen your terminal.

**WSL alternative:** if native Windows friction persists, WSL sidesteps all three failure modes since it manages its own npm prefix cleanly.

## 4. Authenticate

```powershell
gemini
```
First run walks you through choosing an auth method: Google OAuth (free tier — 60 requests/min, 1,000/day), a Gemini API key, or a Gemini Code Assist license.

## 5. Configuration essentials

- Project context file: **`GEMINI.md`** at repo root (analogous to `CLAUDE.md`/`AGENTS.md`) — describes project conventions to the agent.
- Ignore file: `.geminiignore` (like `.gitignore`) to exclude paths from the agent's view.
- Full settings reference: `gemini` → `/settings`, or edit the settings file directly (model temperature/thinking budget, themes, trusted folders, telemetry).
- MCP servers: configure to connect external tools/data sources.
- Sandboxing: for safer tool execution, Gemini CLI can run tool calls inside a Docker sandbox container via `--sandbox`.

## 6. Verify

```powershell
gemini --version
```

## 7. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `gemini` not recognized | npm global bin missing from PATH | Add npm prefix path to User PATH, reopen terminal |
| `PSSecurityException` on launch | Execution policy blocks the `.ps1` wrapper | `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| `ECOMPROMISED` npm cache error | Running Node 24/25 | Switch to Node 22 LTS |
| `FetchError: ETIMEDOUT` | Corporate proxy/firewall blocking Google APIs | `npm config set proxy http://your-proxy:port`; set `HTTPS_PROXY` env var |

## 8. Start using it

```powershell
cd C:\path\to\your\project
gemini
```
