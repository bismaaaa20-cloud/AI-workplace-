# Secrets, Cloud Coding Agents, MCP, and Token Budget

**Status:** proposed implementation guide. **Policy:** free-tier services only; no paid fallback.

## 1. Secret storage

Never store actual credentials in this public repository.

| Runtime | Preferred storage | Notes |
|---|---|---|
| Local Python desktop | OS credential store (Windows Credential Manager, macOS Keychain, Linux Secret Service); ignored local `.env` for development | Never sync secrets to GitHub or shared memory. |
| GitHub Actions | Repository/Environment Actions secrets; OIDC federation where supported | Use environment protection and minimal workflow permissions. Never expose secrets to fork PRs. |
| Codex Cloud | Network secrets for HTTPS credentials with exact Allowed domains; direct environment variables only when code must read the raw value | Network secrets use placeholders in the task and proxy-side substitution for allowed HTTPS destinations. |
| Claude Code cloud runner | Managed secret store or runner secret injection | Never place values in `.mcp.json`, settings, shell history, prompts, or logs. |
| MCP server | OAuth or narrowly scoped token managed by the MCP host | Prefer repository-only access and read-only toolsets first. |

### Environment file policy
- `desktop/.env.example` contains names only.
- Actual `desktop/.env` is ignored by `desktop/.gitignore`.
- Keep any root `.env` ignored if introduced.
- Never put real keys in screenshots, chat, issues, PRs, terminal recordings, logs, or build artifacts.
- If a key leaks: revoke/rotate it immediately, inspect provider usage, and assess Git history exposure. Deleting a key in a later commit does not erase public Git history.

### Variable names
- `GROQ_API_KEY`
- `MISTRAL_API_KEY`
- `GEMINI_API_KEY`
- `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`
- `OPENROUTER_API_KEY`
- Prefer GitHub Actions' built-in short-lived `GITHUB_TOKEN` within workflows, with minimal permissions.

Do not add `OPENAI_API_KEY` or `ANTHROPIC_API_KEY` to the free-only desktop application.

## 2. Codex and Codex Cloud

Repository template: `.codex/config.toml`.

- Codex supports provider-specific environment variable names through provider `env_key` configuration. Never hardcode secrets in TOML.
- Codex Cloud supports Environment variables and Network secrets. Prefer Network secrets for credentials used only for HTTPS calls; restrict Allowed domains to exact destinations.
- Network secrets are substituted by a cloud proxy for allowed HTTPS requests, rather than placing the raw credential in the task process.
- Configure and publish the environment in Codex Cloud settings. Tasks run in isolated hosted workspaces, not on the laptop.
- Start with a small, read-only GitHub MCP tool allow-list. Add write tools only after owner-approved testing.
- Codex Cloud availability/usage depends on the user's ChatGPT plan. Cloud compute does not make third-party API inference free.

## 3. Claude Code and cloud coding agents

Repository templates: `.mcp.json` and `.claude/settings.json`.

- Claude Code supports project MCP configuration and `/mcp` to inspect connection status.
- Authenticate through OAuth/client prompts or the managed runner's secret store.
- Never put literal tokens in `.mcp.json`.
- Deny rules for env/key files are defense in depth, not a substitute for keeping secrets out of untrusted code.
- Claude Code subscription/API billing is separate from the free-only AI Workplace provider policy. Do not add paid Anthropic API usage to the desktop app.

## 4. GitHub MCP

Remote URL: `https://api.githubcopilot.com/mcp/`.

Start with read-only access:
- repository metadata;
- search/read files;
- list issues and pull requests;
- inspect workflow runs.

Do not initially enable:
- merge/push to main;
- deleting repositories or branches;
- changing repository settings/secrets;
- triggering privileged workflows;
- release/deploy actions.

Use GitHub OAuth or a fine-grained token limited to this repository. Avoid classic personal access tokens. Prefer the minimum read permissions and add write permissions only for a specific approved task.

## 5. Token/context budget

Token reduction must preserve governance, security, and evidence.

### Progressive disclosure
- Keep skill names/descriptions short.
- Load only the skill relevant to the current task.
- Store detailed references separately and load them only when needed.
- Keep `AI_HANDOFF.md` concise; archive old task details in dated records.
- Link to canonical rules rather than copying the same long policy into every prompt.

### MCP tool discovery/filtering
- Do not preload every MCP tool definition on every request.
- Discover tools on demand and load only the 3–6 relevant tools.
- Use `enabled_tools`, server-side allow-lists, or tool search where supported.
- Cap large tool outputs and request only the fields needed.
- Cloudflare MCP Portal offers `optimize_context=minimize_tools` (documented up to 5x smaller tool-definition context) and `search_and_execute` for on-demand discovery/execution. This requires a Cloudflare MCP Portal; do not append the parameter to unrelated MCP URLs.

### Smaller repository payload
- Search exact paths/symbols and read relevant line ranges instead of whole files.
- For code review, send diffs and relevant tests, not full repository copies.
- Filter/summarize large command output before returning it to the model.
- Never truncate constitution, security rules, owner approvals, or citations to save tokens.

### Bounded multi-agent review
- One lead agent creates a concise task brief.
- Ask independent reviewers only when needed.
- Maximum two review rounds.
- Ask reviewers for risks and disagreements, not another full implementation.
- Synthesize once; do not forward every intermediate tool result to every agent.

### Prompt caching
- Keep stable instructions/tool definitions at the beginning of requests where the provider supports prompt caching.
- Reuse identical prefixes.
- Prompt caching can reduce billed input cost but does not necessarily reduce logical context size or tokens sent.

## 6. Documentation MCP and Context7

- OpenAI Docs MCP: `https://developers.openai.com/mcp`, read-only OpenAI developer documentation search.
- Context7: documentation lookup for libraries/frameworks; invoke only when current package documentation is relevant.
- Neither is a GitHub write tool. GitHub MCP handles repository operations.

## 7. Plugin packaging

The proposed plugin manifest is in `.codex-plugin/`. It packages skills and remote MCP endpoints. Compatibility must be tested separately for each host; a plugin installed in one product does not automatically appear in another.

## 8. Official references

- Codex environment variables: https://learn.chatgpt.com/docs/config-file/environment-variables
- Codex Cloud environments and network secrets: https://learn.chatgpt.com/docs/environments/cloud-environments
- Codex Cloud usage: https://help.openai.com/en/articles/20001545-using-codex-cloud
- OpenAI API key safety: https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety
- OpenAI sandbox security: https://developers.openai.com/api/docs/guides/agents-api/environments/security
- OpenAI Docs MCP: https://developers.openai.com/resources/docs-mcp
- OpenAI plugin packaging: https://developers.openai.com/api/docs/guides/agents-api/tools/plugins
- OpenAI skills: https://developers.openai.com/plugins/concepts/skills
- Claude tool context management: https://platform.claude.com/docs/en/agents-and-tools/tool-use/manage-tool-context
- Cloudflare MCP context optimization: https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/mcp-portal/
- OpenAI MCP tool filtering: https://developers.openai.com/cookbook/examples/mcp/mcp_tool_guide
