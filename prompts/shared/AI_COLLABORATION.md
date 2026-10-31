# AI Collaboration Guide

## Identities, work surfaces, and sessions

- **AI identity:** the assistant/provider identity used to organize personal memory and private prompt ownership.
- **Work surface:** the app, cloud runtime, IDE, desktop client, or agent environment used to perform work.
- **Session:** one conversation or execution instance.

One AI identity may appear in multiple work surfaces. That does not mean those work surfaces share chat history, files, credentials, memory, or permissions. Treat unknown mappings as UNKNOWN and ask the owner.

## Collaboration model

- Owner assigns the task, scope, project, and permissions.
- One AI is the executor for a task unless the owner explicitly chooses otherwise.
- Other authorized AIs may independently review, research, or provide recommendations.
- Each AI reports its own evidence and does not claim another AI's actions as its own.
- The owner resolves disagreements and approves consequential decisions and merges.

## Project boundaries

Use only project context and resources needed for the assigned task. Do not move code, secrets, or private project data between projects without explicit authorization. A project registry entry is not an access grant.

## Work and handoff

Use a task record, dedicated branch, pull request, and clear acceptance criteria. A handoff should include task ID, project, branch/PR, scope, files changed, decisions, checks actually run, blockers, risks, and one exact next action.

## Shared and personal knowledge

Propose only durable, public-safe facts and approved decisions for Shared Memory. Keep each AI's private notes in its own approved private storage. Shared prompts are intentionally readable by other AIs; private master prompts are not. Never place secrets, credentials, private chats, or confidential content in the public repository.
