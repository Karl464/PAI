# AWS — Amazon Q Developer CLI (now Kiro CLI) — Windows Install & Config

**What it is:** AWS's terminal AI assistant for cloud/dev workflows — command autocompletion, natural-language chat, code generation, and deep AWS CLI integration. **Amazon Q Developer CLI has been renamed Kiro CLI.** No native Windows build exists yet (it's on AWS's roadmap) — Windows access is via **WSL**.

## 1. Prerequisites

- WSL installed with a Linux distro (Ubuntu recommended)
- An AWS Builder ID (free) for individual use, or AWS IAM Identity Center configured + a Q Developer Pro subscription for the Pro tier

## 2. Install WSL (if not already set up)

Elevated PowerShell:
```powershell
wsl --install
```
This enables WSL + the Virtual Machine Platform and installs Ubuntu by default (prompts you to set a username/password).

## 3. Install Kiro / Amazon Q CLI (inside WSL)

```bash
curl --proto '=https' --tlsv1.2 -sSf \
  "https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip" -o "q.zip"
unzip q.zip
./q/install.sh
```
Answer "Yes" when asked to modify your shell config. Restart WSL after install.

## 4. Authenticate

```bash
q login
```
Choose **Use for Free with Builder ID** (individual, free) or **Pro License** (org-managed via IAM Identity Center), then open the printed URL in a browser to complete auth.

## 5. Health check

```bash
q doctor
```
Flags any dependency or configuration issues.

## 6. Configuration essentials

- Start a chat: `q chat` (exit with `/q`).
- **MCP servers:** configure at `~/.aws/amazonq/mcp.json`, e.g. to add the AWS Documentation MCP server:
  ```json
  {
    "mcpServers": {
      "awslabs.aws-documentation-mcp-server": {
        "command": "uvx",
        "args": ["awslabs.aws-documentation-mcp-server@latest"],
        "env": { "FASTMCP_LOG_LEVEL": "ERROR" },
        "disabled": false,
        "autoApprove": []
      }
    }
  }
  ```
  Requires `uv`/`uvx` installed first: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- **VS Code integration:** install the WSL extension in VS Code, then use the AWS Toolkit alongside the CLI for a combined workflow.

## 7. Quick troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| No native Windows install | Not yet supported outside WSL | Use WSL2 (see above); track AWS's `amazon-q-developer-cli` GitHub issue #2063 for native Windows progress |
| Community "Windows-native" builds flagged by antivirus | Unofficial third-party compiled binaries | Prefer the official WSL path; treat unofficial binaries with caution |
| `q` command not found after install | Shell config not reloaded | Close and reopen WSL terminal, or `source ~/.bashrc` |

## 8. Start using it

```bash
cd ~/your-project
q chat
```
Or launch Ubuntu directly from the Start menu, then run `q chat` from there.
