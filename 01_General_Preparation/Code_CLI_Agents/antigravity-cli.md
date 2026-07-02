# Google Antigravity CLI — Windows Install & Config (Quick Reference)

**What it is:** Google's terminal-based agentic coding tool (the `agy` command), part of the broader Antigravity 2.0 platform (also has a standalone desktop app and an IDE). Runs natively on Windows — no WSL required. Note: as of mid-2026, Antigravity CLI has effectively replaced Gemini CLI for unpaid-tier/Google One users.

## 1. Prerequisites

- Windows 10/11
- A Google (Gmail) account
- Chrome recommended for browser-based sign-in

## 2. Install (native Windows)

PowerShell:
```powershell
irm https://antigravity.google/cli/install.ps1 | iex
```

CMD:
```cmd
curl -fsSL https://antigravity.google/cli/install.cmd -o install.cmd && install.cmd && del install.cmd
```

The installer places the `agy` binary at:
```
C:\Users\<Username>\AppData\Local\agy\bin
```

**Install script flags:**
- `--skip-aliases` — don't purge/update legacy `agy`/`antigravity` shell aliases
- `--skip-path` — don't modify your shell profile's PATH

## 3. Authenticate

```powershell
agy
```
On a local machine this opens your default browser for Google Sign-In automatically. Over SSH/remote sessions, it detects the remote context and prints a URL to complete login on a local browser. Credentials are stored via the system keyring, with Google Sign-In as fallback.

To sign out and purge saved credentials, run `/logout` inside the CLI prompt.

**Enterprise access:** connect your GCP project during onboarding — see Google's Antigravity Enterprise docs.

## 4. Configuration essentials

- Settings sync bidirectionally with the Antigravity desktop app / IDE — they share the same "Shared Agent Engine," so preferences set in one surface apply to the other.
- If a task grows too complex for the terminal UI, you can export the session to the full Antigravity GUI app for a richer view.
- On first launch inside a new project folder, you'll be asked to trust the folder before Antigravity CLI can read/edit/execute files there.

## 5. Verify

```powershell
agy --version
```

## 6. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `agy` not recognized | PATH not updated (used `--skip-path`, or terminal not reopened) | Reopen terminal, or manually add `%LOCALAPPDATA%\agy\bin` to User PATH |
| Old aliases conflicting | Legacy Gemini CLI / prior `agy` install | Re-run installer without `--skip-aliases` |
| Browser doesn't open on a remote box | SSH session detected | Copy the printed authorization URL to a local browser |

## 7. Start using it

```powershell
cd C:\path\to\your\project
agy
```
Say "Yes, I trust this folder" when prompted, then start prompting. Use `/help` inside the CLI for commands and shortcuts.

> **Security note:** Google explicitly warns that AI coding agents carry risks (autonomous code execution, data exfiltration, prompt injection, supply-chain risk). Review and monitor agent actions, especially on sensitive repos.
