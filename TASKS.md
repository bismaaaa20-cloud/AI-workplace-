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

### [MUK-001] Document Muk coordinator architecture
- Status: DONE (design only; no runtime script)
- Owner: Project owner
- Executor: ChatGPT
- Scope: Record Muk's role, approved settings, agent roles, planning pipeline, low-memory design, and free-first limits.
- Out of scope: Runtime implementation, live agent connections, paid APIs, deployment.
- Acceptance criteria: Muk is documented as a coordinator inside AI Workplace, not the whole application.
- Related files: docs/architecture/MUK_COORDINATOR_SPEC.md, docs/architecture/AI_AGENT_ROLES.md, prompts/shared/MUK_COORDINATOR_PROMPT.md

### [MUK-002] Build Muk-to-BugScout MCP adapter
- Status: OPEN
- Owner: Project owner
- Executor: To be assigned
- Scope: Implement and test an MCP client adapter for the supplied BugScout server.
- Out of scope: Rewriting BugScout, executing submitted scripts, claiming security scanning, paid services.
- Acceptance criteria: Actual MCP calls verified; blockers trigger up to three fix/recheck rounds; failures are disclosed.
- Related file: docs/architecture/BUGSCOUT_INTEGRATION.md

### [MUK-003] Implement Muk runtime script
- Status: BLOCKED
- Owner: Project owner
- Executor: To be assigned
- Scope: Implement Muk from the documented coordinator and tool-routing designs when the owner is ready.
- Out of scope: Adding future agents or integrations before the owner defines them.
- Acceptance criteria: Planning, decomposition, dependency DAG, context-aware Skill/MCP/Plugin selection, bounded scheduling, handoffs, validation, concise responses, and no unapproved paid APIs.
- Related files: docs/architecture/MUK_COORDINATOR_SPEC.md, docs/architecture/MUK_CONTEXT_AWARE_TOOL_ROUTING.md
- Notes: Owner has not written the script yet; no runtime exists.

### [MUK-004] Implement live capability registry and automatic tool router
- Status: OPEN (design documented; implementation not started)
- Owner: Project owner
- Executor: To be assigned
- Scope: Build a live registry for available Skills, MCP tools, Plugin actions, and agents; implement context classification, capability matching, least-privilege filtering, cost/permission gates, tool selection, fallback, and audit records.
- Out of scope: Claiming integrations are connected before they are configured and tested; enabling paid APIs or account connections without approval.
- Acceptance criteria: Automated tests prove routing by context, selection of the smallest sufficient capability set, refusal of unavailable/unauthorized tools, user confirmation for consequential actions, honest failure handling, and no unapproved paid usage.
- Related file: docs/architecture/MUK_CONTEXT_AWARE_TOOL_ROUTING.md

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
