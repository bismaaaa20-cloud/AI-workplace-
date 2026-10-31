# AI Workplace — Cross-Agent Handoff

**Last updated:** 2026-10-31  
**Canonical source:** this GitHub repository  
**Owner authority:** human project owner

## Current project state

- Constitution v1.0.0 was approved and recorded through PR #5.
- Python Desktop foundation was merged through PR #6.
- A free-only cloud architecture and portable Agent Skills are being proposed in PR #7 (pending review until the pull request is opened and verified).
- The desktop UI is still an early prototype. Gemini is the only provider currently wired into the working Group Room.
- Groq GPT-OSS, Mistral Free mode, Cloudflare Workers AI Free, and OpenRouter `:free` are researched candidates, not yet active integrations.

## Non-negotiable constraints

1. No paid API, no paid fallback, no prepaid credit top-ups, and no silent plan upgrades.
2. No local model inference; model computation must run in hosted provider infrastructure.
3. The public GitHub repository must never contain API keys, tokens, private transcripts, or confidential memory.
4. AI changes go through a feature branch and pull request. No direct push/merge to `main`.
5. The human owner approves merges, constitutional changes, and consequential actions.
6. Platform rules, safety constraints, and applicable law remain above AI Workplace rules.

## Cloud provider shortlist

- Groq Free Plan — primary candidate; its hosted `openai/gpt-oss-120b` model is an OpenAI open-weight model served by Groq, not ChatGPT/OpenAI API.
- Mistral Studio Free mode — secondary reviewer, with pay-as-you-go disabled.
- Cloudflare Workers AI Free — additional hosted model pool under 10,000 Neurons/day.
- OpenRouter `:free` models — optional, rate-limited pool; only IDs ending with `:free`.
- Gemini API free tier — existing prototype provider; free-tier data-use terms mean confidential content should not be sent.

Check the full provider comparison and limits in `docs/architecture/FREE_CLOUD_AI_AND_GITHUB_MCP.md`.

## GitHub / MCP / ChatGPT coordination

- GitHub is the common source of truth.
- The official remote GitHub MCP URL is `https://api.githubcopilot.com/mcp/`.
- Groq documents remote MCP support for tool-capable models, including `openai/gpt-oss-120b`; verify access and start with read-only tools.
- ChatGPT's GitHub connector can fetch supported repository content on request, depending on the account plan and product surface. It does not create a real-time synchronized mirror.
- Custom MCP apps in ChatGPT currently require a Business or Enterprise/Edu workspace according to OpenAI Help. Do not make this a requirement for the owner's Free plan.
- ChatGPT is not automatically notified inside an already-open conversation. It can catch up by fetching this handoff and the relevant PR/issue when the next session starts.

## Portable project skills

Skills live in `.agents/skills/` and use `SKILL.md` with YAML frontmatter:
- `ai-workplace-bootstrap`
- `free-cloud-agent`
- `github-safe-pr`
- `chatgpt-cloud-handoff`
- `multi-agent-review`

## Next recommended work

1. Review and merge the free-only architecture/skills PR only after owner approval.
2. Implement a Groq Free provider adapter for `openai/gpt-oss-120b`.
3. Test Groq remote GitHub MCP with read-only calls and a narrowly scoped credential.
4. Add Mistral and Cloudflare adapters after confirming Free-mode access in the owner's accounts.
5. Add owner-triggered GitHub Actions orchestration on a cloud runner; never expose secrets to untrusted fork workflows.
6. Update this handoff after each meaningful merged change.

## Verification discipline

This file is a handoff, not proof that a workflow, API key, provider account, MCP connection, or test has been configured. Mark unverified items explicitly and update exact PR/commit references when confirmed.
