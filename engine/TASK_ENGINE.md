# UAWA Task Engine

Every task records: unique ID, title, owner, one primary executor, optional reviewer, objective, scope, exclusions, applicable rules, permissions, deliverables, acceptance criteria, approval gates, risk, status, timestamps, related branch/PR, and evidence.

Lifecycle: OPEN → ASSIGNED → IN_PROGRESS → REVIEW → NEEDS_OWNER_APPROVAL → DONE.

Alternative states: BLOCKED, CANCELLED, REJECTED. Mark DONE only when acceptance criteria and required approvals are satisfied. Avoid concurrent edits to the same files.