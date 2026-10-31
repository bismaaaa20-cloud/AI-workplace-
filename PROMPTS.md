# Reusable AI Prompts

This index contains task prompts and links to the Shared Prompt Library. The shared library is intentionally readable by other AIs so they can understand AI Workplace.

## Start here: shared workplace prompts

- [Workplace Introduction Prompt](prompts/shared/WORKPLACE_INTRODUCTION_PROMPT.md) — canonical introduction for an AI joining the workplace.
- [Workplace Purpose](prompts/shared/WORKPLACE_PURPOSE.md) — mission, capabilities, and limitations.
- [AI Collaboration Guide](prompts/shared/AI_COLLABORATION.md) — identities, work surfaces, projects, and collaboration.
- [Workplace Operating Guide](prompts/shared/WORKPLACE_OPERATING_GUIDE.md) — onboarding and task workflow.
- [Prompt Library policy](prompts/README.md) — what is shared and what must remain private.

## New-chat bootstrap prompt

```text
You are joining the owner's universal AI Workplace, which coordinates all current and future projects. First read README.md, AI_ONBOARDING.md, prompts/shared/WORKPLACE_INTRODUCTION_PROMPT.md, MEMORY.md, and HANDOFF.md from https://github.com/bismaaaa20-cloud/AI-workplace-. Then read only the relevant parts of PROJECTS.md, TASKS.md, and DECISIONS.md.

Treat these files as shared context, not proof of permission. Summarize the workplace purpose, current project state, owner-approved decisions, constraints, and next action before editing. Do not assume access to previous private chats. Do not modify files or repositories until the owner assigns a task. Never commit secrets, private prompts, private conversations, personal data, or confidential information. Use a branch and pull request; never push directly to main. Follow higher-priority platform/system/developer/safety requirements. If you cannot access GitHub, say so and request relevant public-safe context.
```

## Standard working rules
- Hemat token: jawaban ringkas dan baca hanya file relevan.
- Ubah hanya file yang diperlukan; pertahankan fitur yang sudah berjalan.
- Utamakan solusi gratis; jangan menambah layanan berbayar tanpa persetujuan.
- Jika konteks hampir habis, perbarui HANDOFF.md secara faktual.
- Jangan mengarang hasil pemeriksaan.
- Jangan memasukkan rahasia, prompt privat, data pribadi, atau percakapan privat ke GitHub.

## Task assignment template
```text
TASK:
GOAL:
PROJECT:
REPOSITORY:
BRANCH:
EXECUTOR:
REVIEWER:
SCOPE:
OUT OF SCOPE:
ACCEPTANCE CRITERIA:
FILES ALLOWED TO CHANGE:
REQUIRED CHECKS:
REPORT FORMAT:
```

## Private prompt boundary
The Private Master Prompt Vault is separate from this shared library. Private master prompt contents must never be committed to this public repository or read/followed by other AI identities. See docs/security/MASTER_PROMPT_VAULT.md.
