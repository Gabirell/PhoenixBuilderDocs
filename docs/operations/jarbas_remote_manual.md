# Jarbas Remote Operations & Agent Manual

This manual provides instructions for orchestrating **Jarbas** (the Antigravity intelligence engine) remotely across local Macs, cloud VPS environments, mobile devices, and Telegram bridges.

---

## 🤖 What is Jarbas?

In the Phoenix Ecosystem:
* **Jarbas** is the Lead Systems & DevOps AI Agent (powered by Google Antigravity / Gemini) responsible for multi-repo synchronization, test execution, procedural geometry algorithms, and architecture logs.
* **Claude**: In-Editor Assistant in Xcode for SwiftUI views and scene graphs.
* **ChatGPT**: High-level System Architect reviewing specifications and ADRs.

---

## 💻 Running Jarbas in the Cloud (24/7 VPS Headless Agent)

To enable Jarbas to edit code, execute tests, and commit changes 24/7 even when your MacBook Air is asleep or powered off:

### 1. The Antigravity Python SDK Setup (`google-antigravity`)
On your cloud VPS (Ubuntu / Debian), install the Python SDK:

```bash
pip install google-antigravity
```

### 2. Autonomous Cloud Runner Script (`jarbas_runner.py`)
```python
import asyncio
import sys
from google.antigravity import Agent, LocalAgentConfig, CapabilitiesConfig

async def run_task(instruction: str):
    config = LocalAgentConfig(
        system_instructions="You are Jarbas, lead developer of Phoenix Ecosystem.",
        capabilities=CapabilitiesConfig(),
    )
    async with Agent(config) as agent:
        print(f"[Jarbas] Executing task: {instruction}")
        response = await agent.chat(instruction)
        async for token in response:
            sys.stdout.write(token)
            sys.stdout.flush()
        print("\n[Jarbas] Task completed.")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        asyncio.run(run_task(" ".join(sys.argv[1:])))
```

Run directly:
```bash
python3 jarbas_runner.py "Run swift test in PhoenixEngine and update ARCHITECT_LOG.md if all pass"
```

---

## 📱 Mobile Operations with Termius & tmux

When controlling Jarbas from **iPhone** or **iPad** via Termius, always wrap long-running operations inside `tmux` so network switches between Wi-Fi and Cellular never kill the task.

### Essential `tmux` Commands for Termius:
```bash
# Start a new persistent Jarbas session
tmux new -s jarbas

# Inside tmux: run your builds, tests, or agent commands
# To detach (leave running in background): Press Ctrl+B then D

# Re-attach when opening Termius later:
tmux attach -t jarbas
```

---

## ⚡ Termius Quick Reference Toolkit

Add these aliases to your `~/.zshrc` on your Mac and VPS for one-tap execution from your phone:

```bash
# --- Phoenix Ecosystem Navigation ---
alias cdphx="cd ~/Documents/Programaciones/PhoenixEcosystem"
alias pstatus="cd ~/Documents/Programaciones/PhoenixEcosystem && git status"

# --- Agent Bridge & Architect Logs ---
alias pbridge="tail -n 30 ~/Documents/Programaciones/PhoenixEcosystem/PhoenixGAMES/HowNotToDie/HowToNotDie/AGENT_BRIDGE.md"
alias parch="tail -n 30 ~/Documents/Programaciones/PhoenixEcosystem/ARCHITECT_LOG.md"

# --- Test Execution ---
alias test-engine="cd ~/Documents/Programaciones/PhoenixEcosystem/PhoenixEngine && swift test"
alias test-builder="cd ~/Documents/Programaciones/PhoenixEcosystem/PhoenixBuilder && xcodebuild test -project 'Phoenix Builder/Phoenix Builder.xcodeproj' -scheme 'Phoenix Builder' -destination 'platform=macOS' -quiet"

# --- Remote Mac Power Management ---
alias pscreen="screencapture -x ~/Desktop/screen_$(date +%s).png"
alias psleepdisplay="pmset displaysleepnow"
```

---

## 💬 Telegram Bot Bridge (Pocket Chat Interface)

With the Telegram Bridge daemon running on your VPS or Mac:

| Telegram Command | Action Executed on Server / Mac |
| :--- | :--- |
| `/jarbas <prompt>` | Prompts Antigravity agent to make changes and commit. |
| `/sh <command>` | Runs shell command (e.g., `swift test`, `git status`). |
| `/screenshot` | Captures Mac display and replies with the image. |
| `/status` | Reports CPU, Memory, and active Git branch status. |
