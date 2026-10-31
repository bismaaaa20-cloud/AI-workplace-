# Muk Context-Aware Tool Selection

Status: DESIGN ONLY — no router, registry, or runtime integration has been implemented or tested.
Version: 0.1-draft

## Purpose

Muk must automatically select the most relevant available **Skill, MCP server/tool, and Plugin** for each user message. Selection is based on the request's meaning, context, required output, constraints, permissions, and the capabilities actually available at runtime. The owner should not need to choose tools manually for ordinary tasks.

This is a capability-selection layer inside Muk, not a replacement for Muk's planning/coordinator role and not a claim that any external service is already connected.

## Definitions

- **Skill:** reusable instructions, procedures, domain knowledge, or workflow guidance.
- **MCP:** a tool interface/server that exposes callable tools or resources.
- **Plugin/connector:** an integration with an external app or service, potentially including read or write actions.
- **Agent:** a specialist AI executor (for example ChatGPT, Claude, or Codex) to which Muk may hand off a task when a real, authorized route exists.
- **Capability:** a normalized description of what a Skill, MCP tool, Plugin action, or agent can do.

Do not treat these categories as interchangeable. A Skill may guide a workflow without providing an executable tool; an MCP server may expose tools but no reasoning model; a Plugin may require account connection and specific permissions.

## Required behavior

1. Inspect the user's message and relevant conversation/project context.
2. Identify the goal, requested deliverable, entities, data sources, constraints, risk level, and whether an action is requested.
3. Decide whether Muk can answer directly or needs a Skill, MCP, Plugin, specialist agent, or a combination.
4. Discover candidates only from the current capability registry/runtime inventory. Do not invent names, tools, connections, or permissions.
5. Match candidates to the task using capability fit, input/output compatibility, reliability, availability, permissions, privacy, cost, and user constraints.
6. Select the smallest sufficient tool set. Avoid redundant tools and unnecessary external calls.
7. Build an execution plan and dependency graph for multi-step tasks. Run independent safe subtasks in parallel only within configured limits.
8. Obtain explicit user approval before paid usage, account connection, write/send/delete/purchase/deploy actions, access expansion, or other consequential actions when required.
9. Execute only through real available interfaces. Validate tool outputs and distinguish successful actions from drafts, plans, and failures.
10. Explain briefly which capabilities were used when it materially affects the result; do not burden the user with internal routing details for routine tasks.

## Context understanding and routing

Muk should classify at least:
- Intent: ask/explain, research, create, code, debug, analyze, transform, retrieve, communicate, schedule, manage, or transact.
- Domain: software, documents, web research, email, calendar, files, data, and other registered domains.
- Deliverable: answer, code, report, edited file, draft, message, event, or external state change.
- Inputs: pasted text, uploaded files, repository content, connected app data, or public information.
- Constraints: language, format, deadline, budget, free-only, privacy, platform, and explicit exclusions.
- Risk/action class: read-only, local transformation, external write, communication, financial, destructive, or deployment.
- Confidence: high, medium, or low; ask one concise clarification when ambiguity materially changes the selected tool or action.

Context includes the current message and only relevant prior context. Do not pull unrelated personal history into tool selection.

## Capability registry

Every selectable capability must have a registry record with:
- Stable ID and display name.
- Kind: skill, MCP tool, plugin action, or agent.
- Description and supported intents/domains.
- Accepted input schema and output type.
- Required permissions, account/connection state, and confirmation requirements.
- Availability/health state and discovery source.
- Cost model (free, metered, paid, unknown) and any limits.
- Data sensitivity and whether data leaves the current environment.
- Read/write/destructive side-effect classification.
- Timeout, retry policy, and known limitations.
- Version and last verification time.

Only capabilities marked available and authorized may be selected for execution. Unknown cost or permission state must not be silently treated as free or approved.

## Selection policy

Rank eligible candidates by:
1. Exact capability match to the requested outcome.
2. Required input/output compatibility.
3. Actual availability and health.
4. Least privilege and privacy/data minimization.
5. User's cost and platform constraints.
6. Reliability and validation support.
7. Lowest complexity and smallest sufficient combination.

Use deterministic rules for filtering, permission checks, cost gates, and tie-breaking. Use model reasoning only to understand natural language, resolve semantic fit, and plan when needed. Never select a tool solely because its name sounds relevant.

If no eligible capability exists, Muk should answer within its own ability, ask for missing input, or provide a copyable manual handoff. It must clearly state when a requested integration is unavailable.

## Examples (illustrative, availability must be checked)

| User request | Possible route |
|---|---|
| Check a Lua script for syntax/freeze patterns | BugScout MCP gate tool + coding Skill for fixes |
| Implement a feature in a codebase | Coding Skill + authorized coding agent/repository tools |
| Research current AI developments | Research Skill + web/search capability |
| Summarize an uploaded report | Document-analysis Skill + file-reading capability |
| Find a project email | Email Plugin read/search action, if connected and authorized |
| Schedule a meeting | Calendar Plugin availability/create action; confirm before creating |
| Explain what an API is | Muk answers directly; no tool needed |

These are routing examples, not assertions that the listed connections are currently active.

## Multi-tool and multi-agent orchestration

For complex requests:
- Decompose into atomic subtasks with objective, inputs, expected output, acceptance criteria, dependencies, selected capability, permissions, and status.
- Represent dependencies as a directed acyclic graph (DAG); detect cycles before execution.
- Route each subtask independently; different subtasks may use different Skills, MCP tools, Plugins, or agents.
- Pass only the minimum necessary context to each tool/agent.
- Keep bounded concurrency, queue size, context size, timeouts, and retries.
- Consolidate results and resolve conflicts against the user's stated requirements; do not hide disagreements or missing evidence.

## Permissions, confirmation, privacy, and cost

- Read-only access is preferred when it satisfies the task.
- A user's request to find or analyze information does not automatically authorize sending, editing, deleting, purchasing, publishing, or deploying.
- Require explicit approval for consequential external writes and any action whose confirmation is required by the integration.
- Never bypass a Plugin's permission model or MCP server access controls.
- Do not send secrets, credentials, or unnecessary personal/private data to tools or agents.
- Respect user constraints such as free-only. Do not use paid or metered services without explicit approval and clear cost disclosure.
- If a tool's cost, data handling, or permission requirements are unknown, stop before using it and explain what needs verification.
- Public repository documentation must not contain credentials, private prompts, private conversation dumps, or personal data.

## Failure handling and fallback

- If discovery fails, report that tool inventory could not be verified; do not guess.
- If a capability is disconnected, unavailable, unhealthy, or unauthorized, do not invoke it.
- If the best candidate is ambiguous, ask one focused question rather than trying multiple risky tools.
- Retry only transient failures, within the configured retry limit; never repeat a non-idempotent action blindly.
- If a tool returns partial or untrusted output, label the limitation and validate before relying on it.
- Keep a concise audit record of selected capability IDs, rationale, permission checks, execution status, and output references. Do not store sensitive payloads unnecessarily.

## Acceptance criteria for implementation

The feature is implemented only when tests demonstrate that Muk:
- Correctly routes representative requests to Skills, MCP tools, Plugins, combinations, or direct response.
- Uses only capabilities present in the live registry and refuses unavailable/unconnected tools.
- Honors user constraints, permissions, cost gates, and confirmation requirements.
- Chooses the smallest sufficient capability set and avoids duplicate calls.
- Decomposes multi-step work, respects DAG dependencies, and bounds concurrency/retries.
- Handles ambiguity, tool errors, partial results, and fallback honestly.
- Does not claim a tool or agent ran unless execution evidence exists.
- Produces concise user-facing explanations and passes privacy/security tests.

## Not implemented

This document is a design specification only. It does not create a runtime router, capability registry, MCP client, Plugin connections, Skill loader, agent adapters, or automatic execution. Each integration must be implemented and tested separately.
