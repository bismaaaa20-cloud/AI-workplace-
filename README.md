# AI Workplace

A model-independent coordination hub for the owner's **all current and future projects** and approved AI assistants.

## Start here — required for every new AI chat
1. [New AI assistant onboarding](AI_ONBOARDING.md)
2. [Shared AI memory](MEMORY.md)
3. [Current handoff](HANDOFF.md)
4. [Shared context and working rules](CONTEXT.md)
5. [Project map and boundaries](PROJECTS.md)
6. [Task board](TASKS.md)
7. [Decision log](DECISIONS.md)
8. [Security rules](SECURITY.md)
9. [Reusable shared AI prompts](PROMPTS.md)
10. [Public-safe message inbox](messages/INBOX.md)

## Architecture
- [Universal project workspace](docs/architecture/UNIVERSAL_PROJECT_WORKSPACE.md)
- [AI identities vs work surfaces](docs/architecture/AI_IDENTITY_AND_WORK_SURFACES.md)
- [Private Master Prompt Vault requirements](docs/security/MASTER_PROMPT_VAULT.md)
- [Rule hierarchy / internal constitution](constitution/HIERARCHY.md)
- [UAWA algorithm](engine/UAWA.md)

## Three separate information areas
- **Shared Memory:** durable, public-safe knowledge intentionally available to authorized workplace participants.
- **Personal AI Memory:** notes owned by an AI identity. A public GitHub folder is not private storage.
- **Private Master Prompt Vault:** storage-only private archive. Other AI identities cannot read or follow its contents; prompts are not automatically loaded or executed.

## Projects
Create a project using [the project profile template](templates/project/PROJECT_PROFILE.md). Each project has its own scope, resources, decisions, tasks, handoff, and explicit access permissions. AI Workplace is the coordination layer, not an AI model.

## Workflow
Every assistant joining in a new chat must read onboarding, shared memory, and handoff first. It should summarize the current state before acting. Use one executor per task, a dedicated branch and pull request, and update the handoff after meaningful work. The owner makes final decisions and approves merges.

## Security and privacy
This repository is public. All committed files, PRs, issues, commit messages, and workflow logs must be treated as public. Never store API keys, tokens, passwords, private prompts, private conversations, personal data, or confidential information here.

## Important limitation
These files provide shared project context, not live chat or automatic AI-to-AI communication. They do not authenticate AI identities or technically enforce private memory boundaries. Those require separate secure implementation and explicit owner approval.
