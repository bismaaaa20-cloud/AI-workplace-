# Shared Task Board

Keep entries concise, public-safe, and actionable.

## Status definitions
- **OPEN** — ready to be picked up
- **IN PROGRESS** — an executor has been assigned
- **BLOCKED** — waiting for access, information, or a decision
- **REVIEW** — implementation or proposal is ready for review
- **DONE** — accepted by the project owner

## Active tasks

### [AW-002] Review shared AI memory and onboarding
- Status: REVIEW
- Owner: Project owner
- Executor: ChatGPT
- Scope: Review MEMORY.md, AI_ONBOARDING.md, messages/CHAT_LOG.md, messages/TEMPLATE.md, and related documentation changes.
- Out of scope: Live chat integration, API credentials, private chat archives, and application code.
- Acceptance criteria: New AI assistants have clear first-read instructions; public-repository safety and access limitations are explicit.
- Related PR: Pending
- Notes: Documentation-only. Does not automatically connect AI accounts.

### [AW-001] Confirm AI collaboration workflow
- Status: OPEN
- Owner: Project owner
- Executor: Project owner + assistants
- Scope: Confirm which AI services are used, how each assistant will read/write this repository, and whether the repository should remain public or become private.
- Out of scope: Sharing credentials in chat or Git.
- Acceptance criteria: Tool access and repository visibility are understood; no credentials are exposed.

### [GETKEY-001] Review Get Key architecture proposal
- Status: REVIEW
- Owner: Project owner
- Executor: ChatGPT (read-only review after assignment)
- Scope: Review the proposed Cloudflare Pages + Pages Functions (Hono) + D1 + Cron architecture, free-tier assumptions, OAuth, Turnstile, deployment, and security risks.
- Out of scope: Creating code, resources, secrets, databases, or deployments before explicit approval.
- Acceptance criteria: Current official limits are verified; risks and open decisions are listed; owner approves or changes the architecture.
- Notes: Proposal is not approved. See PROJECTS.md.

## Completed tasks
- **AW-000:** Initial documentation-only coordination workspace merged into main (PR #1).
- **AW-001 workflow expansion:** merged in PR #2.

## Task template

### [TASK-ID] Short title
- Status: OPEN
- Owner:
- Executor:
- Scope:
- Out of scope:
- Acceptance criteria:
- Related PR:
- Notes (non-sensitive):
