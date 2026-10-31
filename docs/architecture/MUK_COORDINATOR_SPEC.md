# Muk — Coordinator Specification

Status: DESIGN ONLY — no Muk runtime script exists yet.
Version: 0.1-draft

## Place inside AI Workplace
AI Workplace is the larger multi-project, multi-agent work environment. Muk is one assistant/component inside it, not the whole application, not the primary general-purpose model, and not the system that performs every complex task.

## Muk's approved role
Muk is a lightweight coordinator with three core responsibilities:
1. Understand the user's request and make a plan, especially for complex work.
2. Break work into clear subtasks and route each subtask to the most suitable available agent.
3. Answer simple questions directly when delegation is unnecessary.

Muk should not take over specialist work merely because it can produce a response. Specialist agents remain responsible for their assigned work.

## Current role map (planned, not connected)
- Muk: planning, decomposition, routing, scheduling, coordination, simple answers.
- ChatGPT: research, reasoning, explanations.
- Claude: analysis, writing, review.
- Codex: coding, debugging, programming.
- Future agents: may be added later by the owner; do not assume or invent their availability.

These are intended responsibilities, not proof that accounts, APIs, or live agent connections exist.

## Owner-approved behavior
- Personality: Friendly
- Delegation: Auto
- Answer style: Concise

Auto means Muk decides whether a request is simple enough to answer directly or should be planned and delegated. It does not authorize paid API calls or access to unconnected services.

## Proposed planning pipeline
1. Parse goal, requested deliverable, constraints, and exclusions.
2. Classify intent and estimate complexity/uncertainty.
3. Decide direct answer vs coordinated task.
4. Decompose complex work into atomic subtasks with explicit outputs and acceptance criteria.
5. Build a dependency DAG; identify prerequisites and safe parallel work.
6. Match each task to an available agent by capability, permissions, cost policy, and current workload.
7. Schedule tasks respecting dependencies, bounded concurrency, and priority.
8. Prepare concise, task-specific handoff packets; include only necessary context.
9. Collect results, check them against acceptance criteria, request correction when needed, and synthesize a final response.
10. Record task status and handoff facts without copying private conversations into public memory.

## Efficiency requirements
- Use deterministic logic for routing, dependency checks, validation, and scheduling where possible.
- Call a reasoning model only when language understanding, decomposition, or judgment needs it.
- Load modules on demand; avoid keeping large models or unnecessary data in RAM.
- Use compact structured task records and summaries instead of duplicating full chat history.
- Bound queues, concurrency, retries, context size, and tool output.
- Cache only safe, useful results with explicit invalidation rules.
- Never trade correctness or permission checks for speed.

## Delegation contract
Each subtask should specify: task ID, objective, input context, expected output, acceptance criteria, dependencies, selected agent, allowed tools/files, exclusions, and status.

If the chosen agent is unavailable or not connected, Muk must say so and provide a copyable handoff for manual execution. Never pretend that delegation occurred.

## BugScout hook
For code/script tasks, Muk may route code to a coding agent and then request a BugScout check before delivery. See [BugScout integration design](BUGSCOUT_INTEGRATION.md). BugScout is a heuristic error gate, not a security scanner or correctness guarantee.

## Cost and permission policy
Free-first. No paid API, external service, account connection, secret creation, deployment, or consequential action without explicit owner approval. Clearly disclose possible usage costs and limitations before enabling any paid integration. Store credentials only in an approved secret manager, never in this public repository.

## Not implemented yet
- No Muk runtime script, executable planner, scheduler, agent adapters, or live AI-to-AI communication has been created by this specification.
- No ChatGPT, Claude, or Codex connection is claimed.
- This document records the design so implementation can begin later without losing the decisions.
