# Decision Log

Record durable decisions here. Do not include credentials or confidential details. Proposed items are not accepted until the owner explicitly approves them.

## Accepted decisions

### D-001 — Repository purpose
- Status: ACCEPTED
- Decision: This repository is the shared coordination hub for project context, tasks, decisions, and handoffs.
- Reason: Keep collaboration records separate from application/runtime source code.

### D-002 — Protect the default branch
- Status: ACCEPTED
- Decision: Make changes through a dedicated branch and pull request; do not push directly to main.
- Reason: Allow review before changes become the shared baseline.

### D-003 — Keep secrets out of Git
- Status: ACCEPTED
- Decision: Never commit API keys, tokens, passwords, or private credentials. Use an approved secret manager for runtime credentials.
- Reason: Git history and repository contents may be visible or retained even after a file is deleted.

### D-004 — Public-repository privacy
- Status: ACCEPTED
- Decision: Until repository visibility is changed, all content must be considered public.
- Reason: The repository is public.

### D-005 — Token-efficient collaboration
- Status: ACCEPTED
- Decision: Keep responses concise, inspect only relevant files, change only necessary files, preserve working features, and maintain a factual handoff when context is running low.
- Reason: Reduce repeated work and avoid losing project continuity.

### D-006 — Free-first implementation
- Status: ACCEPTED
- Decision: Prefer free solutions. Do not introduce paid APIs, Supabase, Firebase, or external cloud services unless the owner explicitly requests or approves them.
- Reason: Keep costs predictable and respect the owner's stated preference.

## Pending decisions
- Confirm the exact AI Cloud product and supported collaboration method.
- Decide whether this repository should remain public or become private.
- Review and approve or revise the proposed Get Key architecture in PROJECTS.md.
