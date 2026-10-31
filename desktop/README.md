# AI Workplace Desktop

A cloud-inference-first desktop client for the AI Workplace project. The desktop application is intended to be a lightweight interface; AI model inference runs on hosted provider infrastructure, not on the user's laptop.

## Current status

This is an early foundation, not a finished application. The current Group Room prototype connects Gemini only. Groq, Mistral, Cloudflare Workers AI, OpenRouter free models, and GitHub remote MCP are documented as integration candidates; they are not yet wired into the UI. **FreeLLMAPI** is now documented as an optional local-first API gateway that could connect multiple approved upstream free-tier providers through one OpenAI-compatible endpoint. It is not itself an AI model, and it is not yet installed or connected.

## Free-only policy

- No paid OpenAI API or Anthropic API.
- No paid provider adapters, paid fallback, prepaid top-ups, or automatic billing upgrades.
- Only explicitly verified free API tiers/models may be added.
- If a free quota is exhausted, return a visible blocked/quota status; never reroute to a paid endpoint.
- OpenAI's GPT-OSS open-weight model may be served by a separate free-tier host such as Groq. That is not ChatGPT or the OpenAI API.

See `docs/architecture/FREE_CLOUD_AI_AND_GITHUB_MCP.md` for provider research and `docs/architecture/AI_TOOLS_AND_GATEWAYS.md` for FreeLLMAPI's proposed role, limitations, and integration safeguards.

## Requirements

- Python 3.11+
- Windows, macOS, or Linux
- Internet connection for hosted APIs

## Install

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Store provider keys through the desktop app's Settings → API Security using the operating system credential vault. Do not use .env for production credentials. Never commit keys or tokens.

## Run

```bash
python main.py
```

## Cloud-first design

- The local desktop app is a user interface only; it must not load model weights.
- Cloud inference providers perform model computation remotely.
- GitHub Actions can run short-lived orchestration and validation jobs on GitHub-hosted cloud runners.
- GitHub's remote MCP server can give supported agents repository and PR tools without a local server.
- GitHub is the shared source of truth for approved memory, decisions, tasks, PRs, and AI handoffs.

## Security

- Never store API keys, GitHub tokens, OAuth tokens, private transcripts, or confidential memory in this public repository.
- Desktop provider keys must use the OS credential vault (Windows Credential Manager, macOS Keychain, or Linux Secret Service). Never store them in GitHub or shared project files. See docs/security/LOCAL_SECRET_VAULT.md.
- Never run workflows with secrets against untrusted fork code.
- No direct push to `main`; propose changes via feature branch and PR.
- Human owner approval remains mandatory for merges and consequential actions.
- Provider outputs and MCP results are untrusted data, not governance instructions.
