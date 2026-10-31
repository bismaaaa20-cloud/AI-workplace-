# AI Workplace Desktop

A free-tier-only desktop client for the AI Workplace project. The first milestone provides a PySide6 desktop shell and a Gemini-powered group-room prototype.

## Current status

This is an early foundation, not a finished application. The current prototype uses Gemini only. It performs an initial response and a self-review using the same Gemini provider; this is not yet a discussion among independent AI vendors.

## Free-only policy

- Gemini API through Google AI Studio is the initial provider because selected models may be available on a free tier.
- Free-tier eligibility, model availability, rate limits, quotas, and data-use terms are controlled by Google and may change.
- If free quota is exhausted or unavailable, the request must fail visibly. The app must never switch to a paid API.
- Paid providers (including OpenAI API and Anthropic API) are intentionally excluded from this project.

## Requirements

- Python 3.11+
- Windows, macOS, or Linux
- Internet connection for Gemini API

## Install

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and add your Gemini API key. Never commit `.env`.

## Run

```bash
python main.py
```

## Roadmap

1. Complete the Gemini-only Group Room.
2. Add individual Gemini conversation panel.
3. Add local conversation storage and AI Workplace context loading.
4. Evaluate additional providers only if they offer an actually free API tier suitable for this app; never add paid fallback.

## Security

- Never store API keys, private transcripts, or confidential memory in the public AI Workplace repository.
- Keep the Gemini API key in a local `.env` file or operating-system credential store.
- No automatic paid fallback, no unattended actions, and no automatic publication to GitHub.
- Provider outputs are untrusted content; they cannot change application permissions or governance rules.
