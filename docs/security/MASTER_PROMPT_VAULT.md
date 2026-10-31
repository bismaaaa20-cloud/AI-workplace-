# Private Master Prompt Vault

**Status:** proposed security and product requirements.

## Purpose
Provide a storage-only vault where the owner or an authorized AI identity can keep its own master prompts and other prompts for later reference.

## Strict privacy and behavior rules
1. A prompt saved in this vault is private to its owning AI identity and the owner.
2. Other AI identities must not be able to list, read, search, summarize, quote, copy, or follow those prompts.
3. Prompts are stored as content only. Saving a prompt does not make it a workplace rule, system instruction, task assignment, or authorization.
4. Prompts are never automatically loaded into another AI's context or executed.
5. The owning AI may access its own prompt only through an explicit, authorized owner action or a future permissioned workflow. It must not silently auto-follow stored prompts.
6. No shared prompt folder is part of this private vault. If the owner later wants reusable prompts shared with other AIs, that must be a separate, explicit feature and approval.
7. Owner access and administrative controls must be documented; access must be deny-by-default and auditable.

## Identity vs work surface
The vault is organized by **AI identity**, not by every client/runtime. For example, ChatGPT Cloud and Codex Cloud can be associated with one OpenAI identity if the owner configures them that way. They remain separate work surfaces and do not automatically share sessions, credentials, or memory. The same principle applies to other providers.

## Storage requirement — critical
The current AI Workplace GitHub repository is public. **Never store private master prompts or private prompt contents in this repository**, including in commits, issues, PRs, logs, examples, or test fixtures.

The eventual vault must use a genuinely private storage boundary, such as:
- An encrypted local vault on the owner's device, or
- A separate private repository/service with verified access controls and no public mirrors.

A folder name such as `private/` or `master-prompts/` inside this public repository does not make its contents private. A .gitignore rule is only an accidental-commit safeguard, not an access-control system.

## Minimum product requirements
- Separate vault namespace per AI identity.
- Owner-controlled create, view, edit, export, and delete.
- Explicit identity-level permissions; deny other AI identities by default.
- No automatic prompt execution, injection, or context loading.
- No prompt content in logs, telemetry, chat transcripts, or shared memory.
- Encryption at rest and secure key handling if implemented locally.
- Clear status when secure storage is unavailable; no plaintext fallback.
- Audit metadata may record that an item changed, but must not reveal prompt content.
- Backup/export must preserve privacy and require owner intent.

## Not yet implemented
This document defines the intended behavior only. It does not create a vault, encrypt files, authenticate AI identities, or technically enforce access restrictions. Implementation requires a separate owner-approved design, threat model, and tests.
