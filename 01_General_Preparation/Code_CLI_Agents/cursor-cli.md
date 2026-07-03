# Cursor CLI (cursor-agent) — Windows Install & Config (Quick Reference)

**What it is:** Terminal agent from Cursor (the VS Code-based AI IDE). Gives access to Claude, GPT, Gemini, and Cursor's own models from the command line. MCP support via `mcp.json`.

> **Windows caveat:** Cursor CLI does **not** ship an official native Windows build as of mid-2026 — it officially requires **WSL2**. Community-patched native Windows builds exist but are unofficial (use at your own risk; one has triggered Windows Defender false positives).

## 1. Prerequisites

- WSL2 with a Linux distro installed (Ubuntu recommended)
- A Cursor account

## 2. Install (via WSL2 — official path)

```powershell
wsl --list
wsl -d <your-distro-name>
```
Inside the WSL shell, run Cursor's official install script (from cursor.com/docs/cli/installation — fetch it fresh, since the exact curl command is updated periodically) and then:
```bash
cursor-agent
```
It prompts you to log in via your browser.

**Restart the shell** (or reopen the terminal) after install so the `cursor-agent` command is picked up.

## 3. Optional: integrate with Windows tools

- **VS Code / Visual Studio via WSL:** set the integrated terminal's shell to `C:\WINDOWS\system32\wsl.exe` with argument `-d {your_distro_name}`, then run `cursor-agent` from that integrated terminal.
- For best performance, keep your git repo and toolchain (e.g. .NET SDK, Node) inside the WSL filesystem rather than mounted Windows paths — better I/O, fewer permission issues.

## 4. Configuration essentials

- MCP servers: Cursor CLI auto-detects your `mcp.json` — same format used by Cursor's IDE, so a config that already works there works here too.
- Model selection: `/model` inside a session to switch between available models.
- Non-interactive/scripted use: `cursor-agent chat "<prompt>"` for CI or scripting contexts.
- Background agents: Cursor CLI supports running longer tasks in the background so they don't block your terminal session.

## 5. Verify

```bash
cursor-agent --version
```

## 6. Check token usage / remaining budget

There's no reliable built-in slash command for this yet — use the web dashboard:

- **cursor.com/dashboard/usage** — the source of truth for premium/fast requests, tokens, and any on-demand (usage-based) spend across all your devices.
- **Billing & Invoices** (from the dashboard): shows **Included Usage** (covered by your subscription) vs **On-Demand Usage** (billed at API rates once you exceed included usage). You can disable on-demand usage or set a spend cap here.
- **Known caveat:** `cursor-agent`'s own JSON response includes a `usage` field (`inputTokens`/`outputTokens`/`cacheReadTokens`/`cacheWriteTokens`), but community reports show these numbers can disagree with the dashboard — treat the dashboard as authoritative.

## 7. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `cursor-agent` not found in PowerShell/CMD | No native Windows build; you're outside WSL | Run it from inside your WSL distro shell |
| Semantic code search / shell features degraded on Windows | Unofficial community Windows patch has stubbed features | Prefer the official WSL2 path for full functionality |
| Windows Defender flags a Windows binary | Unofficial community-built `.exe`/`.ps1` | Only use official WSL install, or verify the source carefully before trusting a third-party binary |

## 7. Start using it

```bash
cd ~/code/your-project
cursor-agent
```
