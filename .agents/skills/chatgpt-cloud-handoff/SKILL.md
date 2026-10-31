---
name: chatgpt-cloud-handoff
description: Keep ChatGPT, cloud agents, and other assistants aligned through a factual GitHub handoff record.
---

# ChatGPT and Cloud Handoff

1. Read the latest `AI_HANDOFF.md`, main branch, open issues, and relevant PR before resuming.
2. Do not assume external agents can see this chat or that ChatGPT receives a live message from another provider.
3. At the end of a task, summarize:
   - task and outcome;
   - changed files and exact commit/PR;
   - tests actually run and results;
   - decisions made by the owner;
   - blockers and next recommended task.
4. Propose updates to `AI_HANDOFF.md` through a branch and PR, or use an issue/PR comment if a documentation update is not in scope.
5. Mark unverified information as `UNVERIFIED`, stale information as `OUTDATED`, and unresolved work as `BLOCKED`.
6. Do not include private conversation transcripts, API keys, OAuth tokens, or sensitive user information.
7. Make the handoff understandable without access to the original conversation.
8. Do not say that ChatGPT/OpenAI was notified directly. Say the shared GitHub handoff was updated and can be fetched by a connected ChatGPT surface.
