---
name: ask
description: "Answer the user's question by reading and searching the codebase plus applying existing knowledge. Read-only: never edit files or execute code. Use when the user asks a question about the codebase or wants an explanation, not a change."
---

# Ask

Answer the user's question using the codebase and existing knowledge. This skill is strictly read-only.

## Rules

- Do not edit, write, or create any files. Do not run code or execute commands.
- You may search and read the codebase: use glob, grep, read, list, and similar read-only tools. Non-mutating shell commands used solely for searching (such as `grep`, `find`, `ls`) are acceptable; never run build, test, install, or any command that changes state.
- Prefer answering from existing knowledge and the codebase. Cite specific files and line numbers when referencing code.
- If the question cannot be answered from the codebase and knowledge, say so rather than guessing.
- Keep answers concise and direct. Do not make changes or propose patches unless the user explicitly asks for them.
