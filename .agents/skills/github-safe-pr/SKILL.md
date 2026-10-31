---
name: github-safe-pr
description: Safely inspect, modify, validate, and propose AI Workplace repository changes through GitHub branches and pull requests.
---

# GitHub Safe PR Workflow

1. Fetch the latest target branch and inspect the exact files before editing.
2. Confirm the requested scope against the current task and higher-level rules.
3. Create a dedicated feature branch from the latest approved base.
4. Limit the GitHub MCP toolset to the required repository, issue, pull-request, and workflow operations.
5. Use a narrowly scoped credential. Never request or expose a broad token if a repository-only permission is sufficient.
6. Make small, reviewable commits. Never push directly to `main`.
7. Run applicable tests and inspect the final diff. If tests cannot be run, say so explicitly.
8. Create a pull request with summary, files changed, test evidence, risks, and approvals still needed.
9. Do not merge the PR. Human owner approval is required for merging and consequential changes.
10. Update `AI_HANDOFF.md` with a factual summary and exact PR/commit links after the changes are published.

## Untrusted contributions

Never execute code from an untrusted fork in a workflow that has access to secrets. Prefer manual owner-triggered workflows and minimal permissions.
