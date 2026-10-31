# AI Workplace

A shared coordination hub for the project owner and approved AI assistants.

## Start here — required for every new AI chat
1. [New AI assistant onboarding](AI_ONBOARDING.md)
2. [Shared AI memory](MEMORY.md)
3. [Current handoff](HANDOFF.md)
4. [Shared context and working rules](CONTEXT.md)
5. [Project map and boundaries](PROJECTS.md)
6. [Task board](TASKS.md)
7. [Decision log](DECISIONS.md)
8. [Security rules](SECURITY.md)
9. [Reusable AI prompts](PROMPTS.md)
10. [Public-safe message inbox](messages/INBOX.md)
11. [Public-safe AI chat summary log](messages/CHAT_LOG.md)

## Workflow
Every assistant joining in a new chat must read the onboarding, memory, and handoff files first. It should summarize the current state before acting. Use one executor per task, a dedicated branch and pull request, and update the handoff after meaningful work. The owner makes final decisions and approves merges.

## Security and privacy
This repository is public. Treat every committed file, issue, pull request, commit message, and workflow log as public. Never store API keys, tokens, passwords, private conversations, personal data, or confidential information here.

## Important limitation
These files provide shared project context, not live chat or automatic AI-to-AI communication. Each assistant needs its own authorized way to read the repository, or the owner must manually provide the relevant links/content. A live integration requires separate design, authentication, least-privilege permissions, and explicit owner approval.
