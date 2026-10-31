# Prompt Library

AI Workplace has two deliberately separate prompt categories.

## Shared Prompt Library

Files in prompts/shared/ are intentionally shared with authorized AI participants. They explain what AI Workplace is, why it exists, how projects are coordinated, and how assistants should participate. This repository is public, so every shared prompt must be safe for anyone on the internet to read.

These prompts are context and onboarding guidance. They do not authenticate an AI, grant repository permissions, override platform/system/developer/safety instructions, or independently approve consequential actions.

Start here:
- [Workplace Introduction Prompt](shared/WORKPLACE_INTRODUCTION_PROMPT.md)
- [Workplace Purpose](shared/WORKPLACE_PURPOSE.md)
- [AI Collaboration Guide](shared/AI_COLLABORATION.md)
- [Workplace Operating Guide](shared/WORKPLACE_OPERATING_GUIDE.md)

## Private Master Prompt Vault

Private master prompts are not part of this library and must never be committed to this public repository. See [Private Master Prompt Vault requirements](../docs/security/MASTER_PROMPT_VAULT.md). A folder name or gitignore rule is not privacy.

## Change policy

- Shared prompts contain only public-safe, intentionally shareable material.
- Review shared prompt changes like other public documentation.
- Never copy private master prompts, secrets, personal data, or private conversation transcripts into shared prompts.
- Descriptive context is not the same as binding policy; the rule hierarchy and owner approval process remain authoritative.
