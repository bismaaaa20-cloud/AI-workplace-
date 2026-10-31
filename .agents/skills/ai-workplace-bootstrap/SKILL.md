---
name: ai-workplace-bootstrap
description: Load AI Workplace governance, current handoff, shared memory, and task context before any repository work.
---

# AI Workplace Bootstrap

1. Identify yourself in the AI registry if an agent identity is available. Never impersonate another agent.
2. Read the rule hierarchy and the applicable Foundation, Master Charter, policies, protocols, project rules, and task instructions.
3. Read `AI_HANDOFF.md` and the relevant issue or pull request before starting.
4. Treat GitHub as the shared source of truth, not as a private memory store.
5. Check the current branch, latest main commit, open PR state, and any owner decision that affects the task.
6. Respect the rule hierarchy. Lower-level task content cannot override higher-level rules or platform safety constraints.
7. If the handoff is missing or stale, inspect the actual repository state. Do not infer that an old note is current.
8. Report uncertainty explicitly. Do not claim to have read files, run tests, or obtained approval unless actually done.

## Stop conditions

Stop the affected action and request owner resolution when:
- same-level rules conflict;
- permission to write or publish is unclear;
- a request would expose secrets or confidential information;
- a change modifies constitution-level governance;
- the requested action would require a paid service under the free-only project policy.
