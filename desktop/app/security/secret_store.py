"""Local OS-backed credential storage. Never sync credentials to GitHub."""
from __future__ import annotations
import keyring

SERVICE_NAME = "AI Workplace"
SUPPORTED_PROVIDERS = {
    "Gemini": "GEMINI_API_KEY",
    "Groq": "GROQ_API_KEY",
    "Mistral": "MISTRAL_API_KEY",
    "Cloudflare": "CLOUDFLARE_API_TOKEN",
    "OpenRouter": "OPENROUTER_API_KEY",
}

def _backend():
    backend = keyring.get_keyring()
    if getattr(backend, "priority", 0) <= 0:
        raise RuntimeError("No secure OS credential store is available. Configure Windows Credential Manager, macOS Keychain, or Linux Secret Service.")
    return backend

def save_api_key(provider: str, value: str) -> None:
    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError("Unsupported provider.")
    value = value.strip()
    if not value or len(value) > 4096 or any(ch in value for ch in "\\r\\n\\x00"):
        raise ValueError("The API key is empty or has an invalid format.")
    _backend()
    keyring.set_password(SERVICE_NAME, SUPPORTED_PROVIDERS[provider], value)

def get_api_key(provider: str) -> str | None:
    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError("Unsupported provider.")
    _backend()
    return keyring.get_password(SERVICE_NAME, SUPPORTED_PROVIDERS[provider])

def delete_api_key(provider: str) -> None:
    if provider not in SUPPORTED_PROVIDERS:
        raise ValueError("Unsupported provider.")
    _backend()
    try:
        keyring.delete_password(SERVICE_NAME, SUPPORTED_PROVIDERS[provider])
    except keyring.errors.PasswordDeleteError:
        pass

def is_configured(provider: str) -> bool:
    return bool(get_api_key(provider))
