# AI Identities and Work Surfaces

## Why this distinction matters
One AI identity can appear in multiple products or execution environments. For example, ChatGPT Cloud and Codex Cloud may both be associated with OpenAI, while operating in different work surfaces.

## Terms
- **AI identity:** the model/provider assistant identity used for grouping personal memory and private prompt ownership.
- **Work surface:** the app, cloud runtime, IDE, agent session, or device through which that identity performs work.
- **Session:** one particular conversation or execution instance.

## Rules
- Do not create a new personal-memory owner for every work surface by default.
- The owner may map multiple work surfaces to one AI identity.
- Different work surfaces do not automatically share conversation history, files, permissions, credentials, or memory.
- Shared memory is separate from personal memory and requires its own access policy.
- Private master prompts belong to an AI identity and remain inaccessible to other identities.
- If identity mapping is uncertain, mark it UNKNOWN and ask the owner rather than guessing.

## Example mapping
| AI identity | Work surfaces (examples) |
|---|---|
| OpenAI | ChatGPT Cloud, Codex Cloud |
| Anthropic | Claude chat, Claude Code |
| Google | Gemini chat, other authorized Gemini work surfaces |

This table is illustrative only. It does not verify provider architecture or grant any product-level sharing capability.
