# OpenAI Codex CLI — Windows Install & Config (Quick Reference)

**What it is:** OpenAI's open-source terminal coding agent, built in Rust. Included free with ChatGPT Plus/Pro/Business/Edu/Enterprise, or usable with an API key.

## 1. Prerequisites

- ChatGPT Plus/Pro/Business/Edu/Enterprise account, **or** an OpenAI API key with credits
- Node.js 22+ (only if installing via npm)
- Git 2.23+ recommended
- `winget` available (built into modern Windows; update Windows if missing)

## 2. Install (native Windows — PowerShell)

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"
```

Alternative — npm (correct package name matters, the unscoped `codex` on npm is an unrelated project):
```powershell
npm install -g @openai/codex
```

For unattended/scripted installs:
```powershell
$env:CODEX_NON_INTERACTIVE=1; irm https://chatgpt.com/codex/install.ps1 | iex
```

## 3. Windows execution modes

Codex CLI on native Windows runs in PowerShell with an **AppContainer-based sandbox** (restricts filesystem writes, blocks network by default) — still labeled experimental by OpenAI. For a more mature Linux-grade sandbox (Landlock/seccomp), run inside **WSL2** instead:

```powershell
wsl --install
wsl
```
Inside WSL, keep repos under your Linux home (`~/code/...`) rather than `/mnt/c/...` for better I/O and fewer permission issues. WSL1 is **not** supported (Codex 0.115+ requires bubblewrap, which needs WSL2).

## 4. Authenticate

```powershell
codex
```
First run prompts you to sign in — choose **Sign in with ChatGPT** (ties usage to your subscription, no API key management) or provide an API key (uses API credits instead of subscription quota). Credentials are stored in Windows Credential Manager.

## 5. Configuration essentials

- Home directory: `~/.codex` (Windows: `%USERPROFILE%\.codex`)
- If you also run Codex inside WSL, that instance uses its own Linux home by default and won't share config/auth with the Windows-native install. To sync them, set in your WSL shell profile:
  ```bash
  export CODEX_HOME=/mnt/c/Users/<windows-user>/.codex
  ```
- Approval modes control how much Codex can do without asking:
  - `--approval-mode full-auto` runs without confirmation prompts (use with care — it can act outside your project directory)
  - Default/interactive mode asks before risky actions
- Project instructions: supports `AGENTS.md` at repo root (same convention Codex helped popularize) for build/test commands, code style, and constraints.
- Sandbox permissions can be set to **Default** for guardrails; "full access" mode removes the project-directory boundary and can cause unintended destructive actions — avoid it on machines with sensitive data.

## 6. Verify

```powershell
codex --version
```

## 7. Check token usage / remaining budget

Inside a session:
```
/status
```
Shows remaining percentage for both the rolling 5-hour window and the weekly window, plus current model and plan tier.

- Web dashboard (subscription users): `chatgpt.com/codex/settings/usage` — exact reset timestamps for both windows; lags a few minutes but has the numbers `/status` doesn't (reset time, historical trend).
- API/pay-as-you-go billing: `platform.openai.com/usage` — token and cost history.
- **Known caveat:** there's an open bug class where `/status`, the in-app warning banner, and the actual error state can disagree on remaining quota. If the numbers look contradictory, cross-check the web dashboard rather than trusting a single readout.

## 8. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Command not found after npm install | Wrong package (`codex` instead of `@openai/codex`) | `npm uninstall -g codex` then `npm install -g @openai/codex` |
| Sandbox setup fails on managed/corporate machine | Enterprise policy blocks AppContainer setup | Try elevated sandbox setup and approve the admin prompt, or fall back to WSL2 |
| Slow I/O / permission errors in WSL | Working under `/mnt/c/...` | Move repo to `~/code/...` inside WSL |

## 8. Start using it

```powershell
cd C:\path\to\your\project
codex
```
