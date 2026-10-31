# AI Workplace Desktop

A cross-provider desktop client for the AI Workplace project. The first milestone provides a PySide6 desktop shell, a moderated group-discussion engine, and provider adapters.

## Current status

This is an early foundation, not a finished application. The UI shell and orchestration logic are being built in stages. Provider API access requires the user's own credentials and is subject to each provider's quotas and terms.

## Cost-first setup

- Gemini API: Google AI Studio currently offers a free tier for selected models, subject to model-specific quotas and data-use terms.
- OpenAI API: usage is generally billed separately from ChatGPT. Do not assume a ChatGPT Free subscription includes API credits.
- Anthropic API: API usage is separately billed; Claude's consumer free plan is not API access.

The application must never silently switch to a paid model or provider. Paid providers remain disabled until the owner explicitly enables them.

## Requirements

- Python 3.11+
- Windows, macOS, or Linux
- Internet connection for hosted model APIs

## Install

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add only the API keys you intend to use. Never commit `.env`.

## Run

```bash
python main.py
```

## Initial implementation scope

1. Desktop shell with Group Room and individual AI tabs.
2. Provider interface so each vendor is isolated behind an adapter.
3. Moderated discussion with bounded rounds and owner-controlled start.
4. Local-only settings and conversation storage.
5. Later: GitHub sync for approved public-safe rules and memory.

## Security

- Never store API keys, private transcripts, or confidential memory in the public AI Workplace repository.
- Keep secrets in local environment variables or the operating system's secure credential store.
- No automatic paid fallback, no unattended actions, and no automatic publication to GitHub.
- Provider outputs are untrusted content; they cannot change application permissions or governance rules.
