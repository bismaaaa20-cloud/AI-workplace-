# AI Tools and Gateways

## FreeLLMAPI

**Category:** local-first LLM API gateway/router — not an AI model or model provider.

- Project: https://github.com/tashfeenahmed/freellmapi
- Website and model catalog: https://freellmapi.co/
- License: MIT (verify the current upstream repository before adopting a release).
- Purpose: expose multiple upstream model providers through a unified, OpenAI-compatible local API endpoint, with routing/fallback and provider-key management.
- Typical local endpoint: `http://localhost:3001/v1` (confirm the configured port and endpoint in the installed version).
- It can be used as a compatibility layer for clients that support a configurable OpenAI-compatible base URL.
- It can route to upstream free tiers, but **FreeLLMAPI does not make inference universally free**. Each upstream provider has its own eligibility, terms, rate limits, and quotas. Disable paid routes and stop when approved free quota is exhausted.
- The router runs locally, but cloud inference requests still go to the selected upstream providers. Do not send confidential data unless the upstream provider's data terms have been reviewed and approved.
- Keep the gateway bound to localhost/private trusted interfaces. Do not expose its dashboard or API publicly; protect the unified API key and local host.
- Store provider keys only in FreeLLMAPI's supported encrypted local store or the operating-system credential vault. Never place them in Git, shared memory, prompts, logs, or screenshots.
- Premium catalog updates are optional and paid; they are not required for the basic open-source router. Do not purchase Premium or enable paid services without explicit owner approval.

### Proposed AI Workplace role

Treat FreeLLMAPI as a **local gateway tool/work surface integration**, not as an AI identity. Individual models and upstream providers remain separately identified in task records and usage logs. Example: `FreeLLMAPI gateway → Groq provider → selected model`. Do not label that model as ChatGPT or as the original provider's first-party assistant.

### Integration status

**DOCUMENTED / NOT CONNECTED.** This entry records a candidate integration only. It does not install FreeLLMAPI, configure provider keys, open network ports, connect the desktop app, or authorize use of any provider.

Before implementation:
1. Owner confirms the target machine and approves installation.
2. Review the upstream repository, current docs, release, license, and provider terms.
3. Configure localhost-only access and a strong unified gateway key.
4. Allowlist only owner-approved free upstream routes; disable paid routes/fallbacks.
5. Integrate through an OpenAI-compatible client with a configurable base URL and local secret handling.
6. Test quota exhaustion, provider failover, network failure, invalid key, and ensure paid endpoints are never selected.
7. Record the actual provider/model used; never claim a response came from a model that did not serve it.
8. Do not send confidential project information through unreviewed free-tier providers.

## Classification rule

- **AI identity/provider:** the company or model family behind inference (for example Google, Groq, Mistral, or a named open model).
- **AI tool/gateway:** software that routes, exposes, or manages model access (for example FreeLLMAPI).
- **Work surface:** the client/session through which an AI performs work.
- **Model:** the specific inference model that generated a response.

Keep these fields distinct in the registry, UI, audit log, and handoff.
