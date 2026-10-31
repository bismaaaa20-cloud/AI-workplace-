---
name: ai-workplace-companion
description: Apply AI Workplace governance, secret safety, GitHub PR workflow, cloud-agent handoff, and token-efficient MCP use.
---

# AI Workplace Companion

## Bootstrap
- Read `AI_HANDOFF.md`, `AGENTS.md`, the rule hierarchy, and task-specific rules before working.
- Treat GitHub as shared source of truth. Do not assume another AI sees this chat.
- Stop for owner approval on governance changes, permission ambiguity, or consequential writes.

## Secrets
- Never place API keys in source, prompts, PRs, issues, logs, or MCP config.
- Use OS credential storage locally, GitHub Actions secrets/OIDC in workflows, and Codex Cloud Network secrets with exact allowed domains.
- For Claude Code cloud runners, use the host secret store. Keep `.env` ignored and `.env.example` value-free.
- Rotate leaked credentials immediately. Deleting a committed key does not erase Git history.

## Cloud inference
- Use only provider/model combinations explicitly listed as free and currently available on the account.
- Never invoke paid OpenAI API or Anthropic API in this project.
- No paid fallback, prepaid credits, or automatic plan upgrades. On quota exhaustion, stop with `BLOCKED_FREE_QUOTA`.
- Run model inference in provider cloud; never download weights or run local inference.

## MCP and token efficiency
- Discover MCP tools on demand; do not preload every tool schema.
- Start with 3–6 relevant read-only tools. Add write tools only after explicit approval.
- Search exact files and read narrow line ranges. Return concise evidence summaries, not whole-repository dumps.
- Keep handoffs compact; link to canonical rules rather than duplicating them.
- Use prompt caching for stable prefixes when supported.
- Multi-agent reviews: one lead, targeted reviewers, maximum two rounds.
- Never remove security rules, approvals, citations, or uncertainty labels to save tokens.

## GitHub workflow
- Use a feature branch and pull request; never push directly to `main`.
- Do not merge. Human owner approval is mandatory.
- State exactly what tests were run and what remains unverified.
