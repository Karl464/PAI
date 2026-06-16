# Claude Code — Windows Install Guide (Quick Reference)

## 1. Install (no admin needed)

Open PowerShell as your normal **standard user** (no need to run as Administrator) and run:

```powershell
irm https://claude.ai/install.ps1 | iex
```

This installs `claude.exe` into your own user profile:
```
C:\Users\<you>\.local\bin\claude.exe
```
It does **not** touch `Program Files` or `ProgramData`, so no elevation is required.

## 2. Desktop app — optional

The Claude desktop app is a GUI alternative, not a requirement. It bundles Claude Code internally (no separate CLI/Node.js needed).

- Download from claude.com/download
- Requires a Pro, Max, Team, or Enterprise plan to use the **Code** tab
- Not available on Linux (CLI only there)

You can use the CLI, the desktop app, or both — they're independent.

## 3. Add it to PATH

Use **User PATH**, not System PATH — the install is per-user, and editing System PATH needs admin rights you don't need here.

```powershell
$claudeBin = "$env:USERPROFILE\.local\bin"
$current = [Environment]::GetEnvironmentVariable("PATH", "User")
if ($current -notlike "*$claudeBin*") {
    [Environment]::SetEnvironmentVariable("PATH", "$current;$claudeBin", "User")
}
```

Or via GUI: `Win + R` → `sysdm.cpl` → Advanced → Environment Variables → **User variables** → `Path` → Edit → New → `%USERPROFILE%\.local\bin`

**Important:** close and reopen your terminal afterward — PATH changes don't apply to already-open windows.

## 4. Verify

```powershell
$env:Path -split ';' | Select-String '\.local\\bin'
claude --version
claude doctor
```

`claude doctor` gives a full health check (PATH, install method, auth status, updates) — useful to run any time something seems off, and good info to share if you need to ask for help.

## 5. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `claude` not recognized | PATH not picked up yet | Close & reopen terminal; re-check PATH (step 3) |
| Permission denied | Installed with `sudo`/elevated, or npm-based install | Don't use sudo — reinstall with the native installer |
| Can't write to a folder | Folder is outside your profile (e.g. inside `Program Files`) | Either work in a normal user-owned folder, or grant write access to that folder |
| Unsure if PowerShell is elevated | `whoami`/`net user` don't show this | Check window title (says "Administrator:" if elevated), or run `([Security.Principal.WindowsIdentity]::GetCurrent()).Groups -contains "S-1-5-32-544"` |

## 6. Start using it

```powershell
cd C:\path\to\your\project
claude
```
First run opens a browser window to log in with your Anthropic account.
