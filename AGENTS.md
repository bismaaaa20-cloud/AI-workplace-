# AI Workplace agent instructions

Before any work, read:
1. `AI_HANDOFF.md`
2. `constitution/HIERARCHY.md`
3. The applicable constitution/policy/project rules
4. `docs/architecture/FREE_CLOUD_AI_AND_GITHUB_MCP.md`
5. The relevant skill in `.agents/skills/`

## Secrets
- Never ask the owner to paste API keys into chat, issues, PRs, source files, or logs.
- For Codex Cloud, prefer Network secrets with an exact Allowed domains list; use direct environment variables only when the program genuinely needs to read the value.
- For GitHub Actions, use repository Actions secrets or OIDC where supported; never expose secrets to fork pull-request workflows.
- For local development, use an ignored `.env` file and OS credential storage. `.env.example` contains names only.
- If a credential is exposed, stop, revoke/rotate it, and inspect logs/history. Deleting the file alone is not enough.
- Never print environment variables or include secret values in test output.

## Cloud coding environments
- Codex Cloud and Claude Code must use hosted workspaces when the task requires cloud execution.
- Do not run local model inference or download model weights.
- Cloud execution does not imply free API usage. Only the project's allow-listed free tiers are permitted.
- Do not configure paid OpenAI API or Anthropic API providers.

## Token/context discipline
- Load only the skill needed for the task.
- Discover MCP tools on demand; do not preload every tool schema.
- Use a small GitHub MCP allow-list, initially read-only.
- Search for exact files/sections before reading whole documents.
- Return short structured summaries and diffs, not entire repository dumps.
- Keep agent-to-agent review to two rounds maximum.
- Never truncate security rules, owner approvals, or source citations to save tokens.

## Git workflow
- Use a feature branch and pull request. Never push directly to `main`.
- Owner approval is required for merge and consequential actions.
- State exactly which tests were run. Never invent test results.


## Secrets, cloud agents, and token discipline
- Never ask the owner to paste API keys into chat, issues, PRs, source files, or logs.
- For Codex Cloud, prefer Network secrets with exact Allowed domains; use direct environment variables only when code genuinely needs the raw value.
- For GitHub Actions, use repository/environment Actions secrets or OIDC where supported; never expose secrets to fork PR workflows.
- For local development, use an ignored .env file and OS credential storage. .env.example contains names only.
- If a credential is exposed, stop, revoke/rotate it, and inspect logs/history. Deleting a file alone is not enough.
- Never print environment variables or include secret values in test output.
- Codex Cloud and Claude Code cloud runners must use hosted workspaces when cloud execution is requested. No local model inference or model-weight downloads.
- Cloud execution does not imply free API usage. Only explicitly allow-listed free tiers are permitted.
- Load only the skill needed for the task; discover MCP tools on demand; use a small read-only allow-list first.
- Search exact paths and line ranges instead of reading whole files. Return concise summaries/diffs, not repository dumps.
- Limit multi-agent review to two rounds. Never omit governance, security rules, owner approvals, or citations to save tokens.
