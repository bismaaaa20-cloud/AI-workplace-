# AI Workplace Operating Guide

## Join a workplace

1. Read README.md, AI_ONBOARDING.md, MEMORY.md, and HANDOFF.md.
2. Read the shared introduction prompt.
3. Identify the relevant project in PROJECTS.md; inspect only task-relevant records.
4. Tell the owner what you understood and ask for a task if none was assigned.

## Execute a task

1. Confirm goal, scope, acceptance criteria, allowed files/resources, and required permissions.
2. Check relevant owner-approved decisions and higher-priority constraints.
3. Make a concise plan. Ask before expanding scope or taking consequential external actions.
4. Use a dedicated branch and pull request; do not push directly to main.
5. Run appropriate checks where possible. Clearly label checks not run and environment limitations.
6. Review the diff for regressions, accidental secrets, and unrelated changes.
7. Update task and handoff records with factual status.

## Stop conditions

Stop the affected action and ask the owner when:
- Permission or task scope is missing or ambiguous.
- A proposed change conflicts with an owner-approved decision.
- A secret, private prompt, private conversation, or confidential data may be exposed.
- A paid service, billing change, deployment, destructive action, or external commitment is not explicitly approved.
- The required environment or evidence is unavailable.

## Outcome labels

Use COMPLETED, PARTIAL, BLOCKED, NEEDS_OWNER_APPROVAL, REJECTED, or NOT_STARTED accurately. Do not label work completed merely because documentation was written or a PR was opened.
