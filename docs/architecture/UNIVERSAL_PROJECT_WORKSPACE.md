# Universal Project Workspace

**Status:** proposed architecture for owner review.

## Purpose
AI Workplace is the owner's central coordination environment for **all current and future projects**. It is not itself an AI model. AI assistants and their authorized work surfaces collaborate through the workplace, subject to owner-approved permissions.

## Core model
- **Workplace:** shared coordination layer, governance, task tracking, handoffs, and project registry.
- **AI identity:** the underlying assistant/provider identity (for example OpenAI, Anthropic, or Google), not every app, cloud runtime, IDE, or session where it appears.
- **Work surface:** a place/session where an AI operates (for example ChatGPT Cloud, Codex Cloud, Claude Code, or a desktop client). Different work surfaces may belong to the same AI identity.
- **Project:** an independently scoped body of work with its own goals, repositories, status, decisions, and permissions.

Do not assume two work surfaces share memory or credentials merely because they use the same provider. Sharing is an explicit workplace capability and must be permission-checked.

## Project isolation
Every project must have:
- A stable project ID and human-readable name.
- A purpose, owner, status, and scope.
- Its own repository/resource links.
- Project-specific rules, tasks, decisions, and handoffs.
- Explicitly listed AI identities/work surfaces allowed to access it.
- A record of owner-approved changes.

An AI should load only the project context needed for its assigned task. Project A's instructions or secrets must not leak into Project B.

## Suggested repository organization
```text
AI-Workplace/
├── foundation/          # workplace-wide governance
├── registry/            # AI identities and work surfaces
├── projects/
│   ├── PROJECT_TEMPLATE/
│   └── <project-id>/     # public-safe coordination only
├── memory/
│   ├── shared/           # owner-approved shared facts
│   └── personal/         # public repo is NOT private storage
├── prompts/              # reusable prompts approved for sharing
└── docs/
    ├── architecture/
    └── security/
```

This is a logical organization, not an access-control boundary. In a public repository, all committed content remains public. Private project data and private AI notes must live in a genuinely private system.

## Project lifecycle
1. Owner creates a project record from the template.
2. Owner assigns project scope, repository links, and permitted AI identities/work surfaces.
3. AI reads workplace rules plus only the relevant project context.
4. AI proposes a plan; owner approval is required where policy or task scope requires it.
5. Work happens in the target project's authorized branch/repository.
6. AI reports evidence, tests actually run, blockers, and next steps.
7. Durable public-safe decisions are proposed for the shared project record.

## Boundaries
- A project record does not grant access to an external repository or account.
- A work surface is not a separate AI identity by default.
- Provider branding does not prove two sessions share context, memory, or credentials.
- Do not store secrets, private chats, or personal data in this public repository.
- Owner approval and higher-priority platform/safety constraints remain in force.
