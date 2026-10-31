# Universal Project Workspace

**Status:** proposed architecture for owner review.

## Purpose
AI Workplace is the owner's central coordination environment for **all current and future projects**. It is not itself an AI model. AI assistants and their authorized work surfaces collaborate through the workplace, subject to owner-approved permissions.

## Core model
- **Workplace:** shared coordination layer, governance, task tracking, handoffs, prompt guidance, and project registry.
- **AI identity:** the underlying assistant/provider identity, not every app, cloud runtime, IDE, or session where it appears.
- **Work surface:** a place/session where an AI operates. Different work surfaces may belong to the same AI identity.
- **Project:** an independently scoped body of work with its own goals, repositories, status, decisions, and permissions.
- **Shared Memory:** durable, public-safe knowledge and owner-approved decisions available to authorized participants.
- **Personal AI Memory:** private notes owned by one AI identity, not shared by default.
- **Shared Prompt Library:** prompts intentionally published for other AIs to read and understand the workplace and its collaboration process.
- **Private Master Prompt Vault:** separate private storage for an AI identity's own prompts; never stored in this public repository.

Do not assume two work surfaces share memory or credentials merely because they use the same provider. Sharing is an explicit workplace capability and must be permission-checked.

## Project isolation
Every project must have a stable project ID, purpose, owner, status, scope, repository/resource links, project-specific rules/tasks/decisions/handoffs, explicit AI access list, and owner-approved change record.

An AI should load only the project context needed for its assigned task. Project A's instructions or secrets must not leak into Project B.

## Suggested repository organization
```text
AI-Workplace/
├── foundation/
├── registry/
├── projects/
├── memory/
│   ├── shared/
│   └── personal/         # public repo is NOT private storage
├── prompts/
│   └── shared/           # intentionally public-safe prompts
└── docs/
    ├── architecture/
    └── security/
```

This is a logical organization, not an access-control boundary. In a public repository, all committed content remains public. Private project data, personal AI notes, and private master prompts must live in a genuinely private system.

## Project lifecycle
1. Owner creates a project record from the template.
2. Owner assigns project scope, repository links, and permitted AI identities/work surfaces.
3. AI reads workplace rules, shared introduction prompt, and only relevant project context.
4. AI proposes a plan; owner approval is required where policy or task scope requires it.
5. Work happens in the target project's authorized branch/repository.
6. AI reports evidence, tests actually run, blockers, and next steps.
7. Durable public-safe decisions are proposed for the shared project record.

## Boundaries
A project record does not grant access to an external repository or account. A work surface is not a separate AI identity by default. Shared prompts explain the workplace but do not grant access or override higher-priority instructions. Do not store secrets, private chats, or personal data in this public repository.
