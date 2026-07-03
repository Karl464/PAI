# Windsurf (Cascade) — Windows Install & Config (Quick Reference)

**What it is:** A full VS Code-based IDE (not a bare CLI) built by Codeium/Cognition, centered on the **Cascade** AI agent. Now also branded "Devin Desktop" — same product, settings and plans carry over, some menus still say "Windsurf."

## 1. Prerequisites

- Windows 10 or later
- A free Windsurf/Codeium account (no credit card required to start)

## 2. Install

Download the installer from **windsurf.com** (auto-detects Windows) and run the `.exe`. Default install path:
```
C:\Users\<username>\AppData\Local\Programs\Windsurf
```

## 3. First launch

- Sign in with a free Codeium account, then choose Free / Pro / Team.
- You'll be offered **Import from VS Code/Cursor** — pulls in your extensions, themes, and keybindings for a near-zero-friction switch, or choose **Start Fresh**.
- Note: a handful of Microsoft-published proprietary VS Code extensions aren't available (Open VSX licensing) — check anything you depend on before committing.

## 4. Optional: enable the `windsurf` terminal command

Command Palette (`Ctrl+Shift+P`) → **Install 'windsurf' command in PATH**. Then from any terminal:
```powershell
windsurf C:\path\to\your\project
windsurf .
```

## 5. Configuration essentials

- Open Cascade: `Ctrl+L`. Command Palette: `Ctrl+Shift+P`.
- Cascade has two modes: **Write** (creates/edits files, runs terminal commands) and **Chat** (read-only Q&A/planning).
- **Model selection:** Settings (`Ctrl+,`) → AI section → choose the model powering Cascade / autocomplete. Pro+ unlocks more models.
- **Ignore file — `.codeiumignore`:** place at workspace root (same syntax as `.gitignore`) to keep Cascade from viewing/editing/creating files in given paths. For enterprise-wide rules across all repos, put a global `.codeiumignore` in `~/.codeium/`.
- **Auto-run terminal commands:** toggle in settings — disable if you want to approve every shell command Cascade wants to run (recommended for a security-review workflow on untrusted binaries).
- **File creation permissions:** restrict Cascade to editing existing files only, if desired.
- Global rules (cross-project conventions: formatting, docs style) live in user settings, separate from any per-project rules file.

## 6. Check credits / remaining budget

Three ways to view usage:
- Overflow menu → **Cascade Usage** — direct usage view.
- **Windsurf Settings** (status bar) → **Plan Info** tab.
- **windsurf.com/plan** (after authenticating in browser).

> **Recent/upcoming changes to be aware of:** In March 2026 Windsurf moved from a pure prompt-credit system to a combined daily/weekly quota system for free-tier users (paid plans still use credits). On June 2, 2026 Windsurf was officially renamed **Devin Desktop** under Cognition — existing settings/plans carried over automatically, though some UI still says "Windsurf." Cascade itself is slated for discontinuation around July 1, 2026, auto-migrating to a successor called **Devin Local** with a similar UX. If credit/usage screens look different from this guide, that migration is almost certainly why — check status.windsurf.com or the in-app plan page for the current state.

Basic models (e.g. Cascade Base) are free/unlimited — a good fallback if you're out of credits or want to conserve them for complex tasks.

## 7. Verify

```powershell
windsurf --version
```

## 8. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `windsurf` not recognized in terminal | PATH command not run during/after install | Command Palette → Install 'windsurf' command in PATH |
| Windsurf hijacks `.md`/`.json` file associations | Default file-type registration on install | Right-click file → Open With → choose preferred app → "Always use this app" |
| App won't launch | Antivirus interference, or corrupted install | Reinstall; check antivirus exclusions |
| Missing a familiar VS Code extension | Not available on Open VSX (proprietary MS extension) | Check availability before switching fully; use VS Code side-by-side if needed |

## 9. Start using it

Open a real project folder (not a scratch file — Cascade's value compounds with codebase context), press `Ctrl+L`, and describe what you want built or changed.
