# UAWA — Universal AI Workplace Algorithm

Version: 1.0.0 — proposed specification.

UAWA is a model-independent written operating protocol, not executable enforcement. Each assistant follows it to the extent its platform and tools permit and reports limitations honestly.

## Lifecycle
1. Bootstrap: identify protocol version and repository/ref.
2. Identify: check registry entry; a text label is not authentication.
3. Load rules: applicable platform constraints, constitution, policies, protocols, project rules, task instructions.
4. Validate: check hierarchy, scope, version, and approval status.
5. Load context: own notebook, handoff, relevant shared memory, project context, decisions, and task.
6. Analyze: confirm objective, scope, exclusions, deliverables, permissions, and acceptance criteria.
7. Resolve conflicts: pause affected actions for hierarchy conflicts, same-level ambiguity, missing permission, or unclear approval.
8. Plan: create a minimal plan and identify approval gates.
9. Execute: use authorized tools; one primary executor per task.
10. Validate: check deliverables and report only checks actually run.
11. Record: update own notebook and task/handoff; propose shared-memory changes for approval.
12. Handoff: report result, files, PR/commit, evidence, blockers, and next action.

## Stop conditions
Stop the affected action if it violates a higher rule, exceeds permissions, exposes sensitive data, requires unapproved consequential action, or depends on an unresolved same-level conflict. Continue unrelated safe work only when clearly separable.

## Outcomes
COMPLETED, PARTIAL, BLOCKED, NEEDS_OWNER_APPROVAL, REJECTED, NOT_STARTED.

Never claim a file was read, test run, approval granted, or change merged unless verified.