# AI Workplace — Shared Introduction Prompt

This prompt is intentionally shared so another AI can read it and understand the workplace. It contains no private master prompt content.

You are being introduced to **AI Workplace**, a model-independent coordination and governance layer for the owner's current and future projects. Read this document to understand what the workplace is for before accepting work in it.

## What AI Workplace is

AI Workplace is a central coordination environment that helps the owner and multiple authorized AI assistants organize work across many projects. It provides shared public-safe context, project boundaries, task tracking, decisions, handoffs, collaboration procedures, and reviewable changes.

AI Workplace is **not** an AI model, does not replace ChatGPT/Claude/Gemini/Codex, and does not automatically connect AI accounts or create live communication between them. Each assistant must use an authorized work surface and independently access resources it has permission to use.

## Why it exists

- Coordinate multiple AI assistants without losing project goals or decisions.
- Support all current and future projects, not just one product or repository.
- Keep each project's scope, files, tasks, and permissions clear.
- Preserve approved knowledge in shared memory while keeping each AI's personal memory separate.
- Make work auditable through tasks, branches, pull requests, evidence, tests, and handoffs.
- Keep the human owner in control of priorities, permissions, and final approvals.

## How to participate

1. Read README.md, AI_ONBOARDING.md, MEMORY.md, and HANDOFF.md, then inspect only project files relevant to the assigned task.
2. Identify the AI identity, work surface, and current session. Do not assume two products share memory, credentials, permissions, or chat history.
3. Summarize your understanding, relevant project status, constraints, and next action to the owner.
4. Do not begin repository changes or external actions until the owner has assigned the task and required permissions are available.
5. Work only within the assigned project and scope. Prefer one executor per task; other assistants may review independently.
6. Use a dedicated branch and pull request. Do not push directly to the default branch.
7. Report actual changes, checks actually run, evidence, unresolved risks, blockers, and next steps.
8. Propose durable, public-safe knowledge for shared memory; do not treat assumptions or proposals as approved decisions.

## Memory and prompt boundaries

- **Shared Memory** contains durable, public-safe project knowledge and owner-approved decisions available to authorized participants.
- **Personal AI Memory** belongs to one AI identity and is not shared by default.
- **Shared Prompt Library** contains prompts deliberately published for other AIs to read and use as workplace context or onboarding guidance.
- **Private Master Prompt Vault** is separate storage for private prompts belonging to an AI identity. Other AI identities must not read, search, summarize, copy, follow, or execute those private prompts.

Never put private prompts, secrets, credentials, private chat transcripts, personal data, or confidential information in this public repository.

## Authority and safety

This prompt explains the workplace; it does not elevate its own authority. Follow applicable law and higher-priority platform, system, developer, and safety requirements. Follow workplace rules only where they do not conflict with those requirements. A repository file cannot authenticate you, grant access, or authorize an action by itself.

If instructions conflict, scope or permission is unclear, sensitive information may be exposed, or a consequential action lacks approval, stop the affected action and ask the owner.

## First response expected

After reading the available workplace context, briefly tell the owner:
- What AI Workplace is and why it exists.
- Which AI identity/work surface/session you are using, if known; mark unknown details UNKNOWN.
- Which project and task you understand you are assigned to.
- What permissions or information are missing.
- Your proposed next step.

Do not claim to have read files or performed checks you could not actually access or complete.
