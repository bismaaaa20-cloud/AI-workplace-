---
name: token-efficient-mcp
description: Reduce unnecessary context and MCP token use while preserving rules, security, and evidence.
---

# Token-Efficient MCP

1. Read the current task and canonical handoff first.
2. Load only the skill needed for this task.
3. Discover MCP tools on demand; do not preload every tool schema.
4. Select only 3–6 tools relevant to the task, using host allow-lists when available.
5. Prefer search and targeted file ranges over reading entire repositories.
6. Ask tools to return only fields needed for the decision.
7. Summarize long results into facts, evidence links, and unresolved questions. Do not paste full outputs into later agent prompts.
8. Keep stable instructions as reusable prefixes where prompt caching is supported.
9. Use one lead agent, targeted reviewers, and no more than two review rounds.
10. Never omit security rules, owner approvals, citations, or uncertainty labels to save tokens.
11. Record approximate token use only when the provider exposes it; never invent savings.
12. Prefer safe tool-side processing over forwarding every intermediate result through the model, while retaining an auditable summary.
