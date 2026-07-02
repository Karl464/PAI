# CodeMie — Windows Install & Config (Quick Reference)

**What it is:** EPAM's enterprise CLI wrapper/proxy that gives access to multiple AI coding agents (Claude, Codex, Gemini) through centralized Enterprise SSO — no personal API key or individual model subscription needed. Billing and access control are handled by EPAM centrally.

> This guide is based on internal EPAM documentation notes, not a public vendor site — verify specifics (flags, exact profile names) against your org's current CodeMie docs, since this tool isn't publicly documented.

## 1. Prerequisites

- Node.js installed (CLI is distributed via npm)
- EPAM VPN enabled (required to complete SSO authentication)
- Valid EPAM credentials
- **Windows note:** recommended to run PowerShell **as Administrator** for install

## 2. Install

```powershell
npm install -g @codemieai/code
```

## 3. Authenticate

```powershell
codemie setup
```
Choose **CodeMie SSO – Enterprise SSO Authentication**. This opens your browser to sign in with your EPAM credentials.

## 4. Install an agent

```powershell
codemie install claude
```
Other agents available the same way:
```powershell
codemie install codex
codemie install gemini
```

## 5. Launch

```powershell
codemie-claude
```
Starts a session and lets you prompt the AI directly from your terminal. Equivalent launchers exist per agent:
```powershell
codemie-codex
codemie-gemini
```

## 6. Configuration — profiles

- Profiles are attached to a specific model at setup time (e.g. `claude-sonnet-4-7`) but can be changed later without losing history — CodeMie's Single-Profile concept transforms the attribute set rather than erasing it.
- Add another profile any time: `codemie setup` → **Add new profile**.
- **Naming convention:** purpose-oriented and unique, e.g. `work-coding` for a standard dev profile. If you run multiple models for different tasks, name profiles so the model/use-case is obvious at a glance (e.g. `sast-review-claude`, `docs-gemini`).

## 7. Usage tracking

```powershell
codemie analytics show
```
Monitor your own token consumption and usage — useful for keeping tabs on a security-review workflow that may burn large context windows (e.g. Ghidra output triage).

## 8. Cost & licensing summary

| Item | Detail |
|---|---|
| Personal license/API key | Not required |
| Billing | Centralized via EPAM Enterprise SSO |
| Cost to individual employee | Free |
| Personal laptop use | Not explicitly forbidden; requires EPAM VPN + Node.js during auth/setup |
| Models available | Claude (recommended: `claude-4-5-sonnet` or `claude-4-6-sonnet`), OpenAI Codex (`--model gpt-4.1`), Google Gemini (`--model gemini-2.5-flash`) |

## 9. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `codemie` not recognized | npm global bin not on PATH, or install ran without admin rights | Re-open elevated PowerShell, re-run install |
| SSO login hangs/fails | VPN not connected | Confirm EPAM VPN is active before `codemie setup` |
| Agent launch command not found | Agent not installed for that profile | Run `codemie install <agent>` again |
