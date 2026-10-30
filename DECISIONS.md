# Decision Log

Record durable project decisions here. Do not include credentials or confidential details.

## Decisions

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
- Reason: The repository is currently public.
