# Free Cloud AI + GitHub MCP Architecture

**Research date:** 2026-10-31  
**Project constraint:** no paid AI API, no local model inference, and no direct writes to `main`.

## 1. Goal

Run AI inference and repository automation in provider/GitHub cloud infrastructure. The desktop app, when eventually used, is only a lightweight client; it must not download model weights or run local inference.

The shared GitHub repository is the source of truth. AI agents communicate through issues, pull requests, an explicit handoff document, and approved memory records. This allows ChatGPT/OpenAI to catch up by reading the latest shared files instead of relying on another product's private chat history.

## 2. Candidate hosted inference providers

These are hosted API services. Model inference occurs in provider infrastructure, not the user's laptop. Free tiers are limited and can change; each provider must be checked in its account dashboard before activation.

| Provider | Free access checked on 2026-10-31 | Proposed role | Important guard |
|---|---|---|---|
| Groq | Free Plan exists. Official rate-limit docs expose per-model quotas; the current account Limits page is authoritative. | Primary cloud agent, especially `openai/gpt-oss-120b`. | Use Free Plan only. Never switch to Developer/paid plan. |
| Mistral Studio | Free mode is enabled by default; no card required; included monthly usage and limits apply. | Secondary independent reviewer. | Disable pay-as-you-go/prepaid top-ups; stop when included free usage is exhausted. |
| Cloudflare Workers AI | 10,000 Neurons/day on Workers Free; requests above free capacity fail unless the account upgrades. | Additional cloud model / privacy-sensitive candidate. | Use only models available on Workers Free, e.g. GLM-4.7-Flash; do not enable Workers Paid. |
| OpenRouter | `:free` model variants are $0, with a 20 RPM / 50 RPD limit for free variants. | Optional model discovery / temporary alternate. | Allow only model IDs ending in `:free`; disable paid credits and never use paid fallback. |
| Google Gemini API | Selected models have a free tier with free input/output tokens and limited model access. | Existing first prototype / optional reviewer. | Free-tier content may be used to improve Google's products; do not send confidential project material. |

### Recommended order

1. **Groq GPT-OSS 120B** as first additional provider. Groq serves an OpenAI open-weight model, so the OpenAI model family can participate without using the paid OpenAI API.
2. **Mistral Free mode** as an independent reviewer, after confirming the organization remains in Free mode and pay-as-you-go is off.
3. **Cloudflare Workers AI** as an additional free-quota provider, selecting a model explicitly marked available to Workers Free.
4. Keep **Gemini** as an option, but classify prompts sent through its free tier as non-confidential.
5. Treat **OpenRouter :free** as optional because model supply and per-model capacity can change.

The Groq-hosted `openai/gpt-oss-120b` model is **not ChatGPT and not the OpenAI API**. It is an OpenAI open-weight model served by Groq. ChatGPT stays a separate assistant and reviewer.

## 3. Cloud execution without laptop RAM

Use GitHub Actions standard hosted runners for short-lived orchestration jobs. For public repositories, standard GitHub-hosted runners are free and unlimited under the current GitHub Actions policy. The runner is a temporary cloud VM; it is not the user's device and does not keep an agent running forever.

Recommended triggers:
- `workflow_dispatch` for owner-started runs;
- approved issue labels/comments for task intake;
- pull-request events for review/check workflows.

Never run a privileged workflow against untrusted fork code. Use GitHub Actions secrets for provider keys. Secrets must never enter source files, artifacts, logs, prompts, issue comments, or memory records.

Cloud jobs may:
1. read current rules and task files;
2. call only explicitly allowlisted free model endpoints;
3. run tests and validation;
4. create a feature branch and pull request;
5. append a concise, non-sensitive handoff note.

Cloud jobs must not merge to `main), alter constitutional files, or publish shared memory without owner approval.

## 4. MCP connection

### Main tool server: GitHub's official remote MCP server

- Remote URL: `https://api.githubcopilot.com/mcp/`
- Hosted by GitHub; no local MCP process or laptop RAM is required.
- It supports repository/file access, issues, pull requests, and workflow operations.
- The server supports toolset/tool allow-lists. Prefer only the tools needed for this repository; do not expose every tool by default.
- Use OAuth or a narrowly scoped fine-grained token for this repository only.
- For model-driven GitHub writes, require human approval and preserve the branch + PR workflow.

### Groq + remote MCP

Groq's Responses API documents remote MCP support for tool-capable models, including `openai/gpt-oss-120b`. MCP is currently documented as beta. The API can discover tools from a remote server and execute calls, so a Groq-hosted model can work with the official GitHub remote MCP without a local MCP process.

This capability must be smoke-tested with read-only tools first. Only add write tools after testing, and require approval before opening or modifying a PR.

### OpenAI / ChatGPT path

- The ChatGPT GitHub app/connector can read allowed repository content and cite files. It does not create a continuously synchronized mirror; it fetches on request and availability depends on plan and surface.
- ChatGPT custom MCP apps can expose read/write tools, but OpenAI's current Help Center lists custom MCP connections for Business and Enterprise/Edu workspaces. This project owner currently uses ChatGPT Free, so do not make custom MCP installation a prerequisite.
- OpenAI's public Docs MCP at `https://developers.openai.com/mcp` is read-only documentation search; it is useful for current OpenAI docs, not for writing to this project repository.
- No OpenAI API key is required for ChatGPT to review repository context through an eligible GitHub connector surface. OpenAI API calls are excluded from this free-only project.

## 5. Keeping ChatGPT and every cloud agent current

GitHub is the common handoff layer. Maintain:
- `AI_HANDOFF.md`: concise current state, latest commit/PR, blockers, next task, and owner decisions;
- `docs/decisions/`: approved decisions only;
- `memory/shared/`: owner-approved, public-safe reusable facts;
- issue/PR comments: task progress and review findings;
- `CHANGELOG.md`: durable changes.

At the start of every AI session, the agent must fetch the current handoff, rules, and relevant task files. At the end, it must publish a concise handoff through an issue/PR or a proposed file update. This is a pull-based shared-memory design, **not a hidden broadcast into an already-open ChatGPT conversation**.

## 6. Free-only cost guard

The orchestrator must enforce:
- provider allow-list containing only approved free endpoints/models;
- provider mode check (Free/Workers Free);
- no paid API keys or paid provider modules in the desktop app;
- no prepaid top-ups or pay-as-you-go activation;
- no automatic fallback to a paid model;
- on quota exhaustion, return `BLOCKED_FREE_QUOTA` and wait for the next reset or owner action;
- record provider, model, timestamp, free-tier status, and quota/error status without storing API keys or full private prompts.

Do not treat a provider as free just because it offers a free web chat. Confirm API free mode separately.

## 7. Public repository security

This repository is public. Never store provider keys, GitHub tokens, OAuth tokens, private chat transcripts, or confidential project memory in repository files. Use GitHub Actions secrets or a suitable secret manager. Grant only the minimum GitHub permissions needed. Keep all generated changes on a branch and open a pull request for owner review.

## 8. Official references

- Groq rate limits: https://console.groq.com/docs/rate-limits
- Groq remote MCP: https://console.groq.com/docs/tool-use/remote-mcp
- Mistral Free mode key setup: https://docs.mistral.ai/getting-started/quickstarts/studio/activate-and-generate-api-key
- Mistral usage and limits: https://docs.mistral.ai/admin/billing-usage/usage-limits
- Cloudflare Workers AI pricing: https://developers.cloudflare.com/workers-ai/platform/pricing/
- Cloudflare Workers AI data usage: https://developers.cloudflare.com/workers-ai/platform/data-usage/
- OpenRouter free models and limits: https://openrouter.ai/collections/free-models
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- GitHub Actions runners: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job
- GitHub Actions secrets: https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions
- GitHub remote MCP: https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md
- ChatGPT + GitHub: https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt
- ChatGPT custom MCP availability: https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt
- OpenAI Docs MCP: https://developers.openai.com/resources/docs-mcp
- OpenAI plugin skills: https://developers.openai.com/plugins/concepts/skills
