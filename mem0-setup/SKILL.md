---
name: mem0-setup
description: "Set up Mem0 for OpenCode or another agent using an existing API key, including CLI initialization and OpenCode MCP registration. Use when the user asks to install, configure, or connect Mem0 memory, especially with an existing key, and across multiple agents."
---

# Mem0 Setup

## Before you start

- Reuse an existing API key when one already exists. Do not create another agent account if a key is already stored in `~/.mem0/config.json` under `platform.api_key`.
- Keep the same `user_id` everywhere so memories stay visible across agents. The agent-mode default used here is `user_bbbf96e175f1`.
- Keep the API key out of chat logs and git commits. Read it from local config instead of asking the user to paste it.

## Check whether Mem0 is installed

```powershell
Get-Command mem0 -ErrorAction SilentlyContinue
```

If it is missing, install the CLI:

```bash
npm install -g @mem0/cli
```

## Configure the CLI with an existing key

```bash
mem0 init --api-key "<key from ~/.mem0/config.json>" --user-id user_bbbf96e175f1
```

If the key must be attributed to another agent name, run after setup:

```bash
mem0 identify <agent-name>
```

## Configure OpenCode MCP

Register the hosted Mem0 MCP server with the same key:

```powershell
opencode mcp add mem0-mcp --url "https://mcp.mem0.ai/mcp" --header "Authorization=Bearer <key>" --global
```

Confirm it is available:

```powershell
opencode mcp list
```

## Agent prompt for other agents

Use this when asking another agent to set itself up:

```
Set up Mem0 using my existing API key.
1. Install @mem0/cli if it is missing.
2. Read platform.api_key from ~/.mem0/config.json.
3. Run: mem0 init --api-key "<key>" --user-id user_bbbf96e175f1
4. If the client supports MCP, add https://mcp.mem0.ai/mcp with header Authorization: Bearer "<key>".
5. Use user_id user_bbbf96e175f1 for every Mem0 call.
6. Do not delete or rewrite existing memories, and do not sign up a new agent account.
```

## Claiming the account

Agent-mode accounts are unclaimed until an owner verifies an email. To claim without changing the API key or memories:

```bash
mem0 init --email you@example.com
```

After claiming, all configured agents keep working with the same key. Browser OAuth sign-in also becomes available for clients that support it.

## Limits

- Agent-mode accounts are limited to 5 signups per day per IP address.
- Memories are scoped by user_id, agent_id, app_id, and run_id. Without the correct user_id, a client can authenticate but see no memories.
- Do not commit API keys in repository files. Store them in local config or environment variables.