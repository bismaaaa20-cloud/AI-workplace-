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

## Universal AI Workplace Protocol
- [Rule hierarchy / internal constitution](constitution/HIERARCHY.md)
- [Foundation](constitution/FOUNDATION.md)
- [Master Charter](constitution/MASTER_CHARTER.md)
- [Amendment policy](constitution/AMENDMENT_POLICY.md)
- [UAWA algorithm](engine/UAWA.md)
- [Bootstrap protocol](engine/BOOTSTRAP.md)
- [Rule engine](engine/RULE_ENGINE.md)
- [Memory engine](engine/MEMORY_ENGINE.md)
- [Task engine](engine/TASK_ENGINE.md)
- [Conflict engine](engine/CONFLICT_ENGINE.md)
- [Validation engine](engine/VALIDATION_ENGINE.md)
- [Universal adapter](engine/UNIVERSAL_ADAPTER.md)
- [AI registry](registry/AI_REGISTRY.md)
- [Personal notebook templates](ai/TEMPLATE/NOTEBOOK.md)

All internal rules are proposed until explicitly approved by the owner. Platform constraints and applicable law remain outside and above this internal hierarchy. UAWA is a documented protocol, not technical enforcement.

## Workflow
Every assistant joining in a new chat must read the onboarding, memory, and handoff files first. It should summarize the current state before acting. Use one executor per task, a dedicated branch and pull request, and update the handoff after meaningful work. The owner makes final decisions and approves merges.

## Security and privacy
This repository is public. Treat every committed file, issue, pull request, commit message, and workflow log as public. Never store API keys, tokens, passwords, private conversations, personal data, or confidential information here.

## Important limitation
These files provide shared project context, not live chat or automatic AI-to-AI communication. Each assistant needs its own authorized way to read the repository, or the owner must manually provide the relevant links/content. A live integration requires separate design, authentication, least-privilege permissions, and explicit owner approval.
