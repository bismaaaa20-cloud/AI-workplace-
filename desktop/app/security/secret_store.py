"""OS credential-vault access with an explicit fail-closed backend policy."""
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
# Accept only known OS-backed implementations. Unknown/custom backends may store
# credentials in plaintext, so they are rejected even if their priority is positive.
_TRUSTED_BACKEND_MODULE_PREFIXES = (
    "keyring.backends.Windows",
    "keyring.backends.macOS",
    "keyring.backends.SecretService",
    "keyring.backends.kwallet",
    "keyring.backends.libsecret",
)


def _backend():
    backend = keyring.get_keyring()
    module = type(backend).__module__
    if not any(module.startswith(prefix) for prefix in _TRUSTED_BACKEND_MODULE_PREFIXES):
        raise RuntimeError(
            "No supported OS credential vault is active. Use Windows Credential Manager, "
            "macOS Keychain, or Linux Secret Service/KWallet. Plaintext and custom backends are blocked."
        )
    if getattr(backend, "priority", 0) <= 0:
        raise RuntimeError("The OS credential vault is unavailable or locked.")
    return backend


def _account(provider: str) -> str:
    try:
        return SUPPORTED_PROVIDERS[provider]
    except KeyError:
        raise ValueError("Unsupported provider.") from None


def save_api_key(provider: str, value: str) -> None:
    account = _account(provider)
    if not isinstance(value, str):
        raise ValueError("The API key must be text.")
    value = value.strip()
    if not value or len(value) > 4096 or any(ch in value for ch in ("\r", "\n", "\x00")):
        raise ValueError("The API key is empty or has an invalid format.")
    _backend()
    keyring.set_password(SERVICE_NAME, account, value)


def get_api_key(provider: str) -> str | None:
    account = _account(provider)
    _backend()
    return keyring.get_password(SERVICE_NAME, account)


def delete_api_key(provider: str) -> None:
    account = _account(provider)
    _backend()
    try:
        keyring.delete_password(SERVICE_NAME, account)
    except keyring.errors.PasswordDeleteError:
        pass


def is_configured(provider: str) -> bool:
    return bool(get_api_key(provider))


def is_vault_available() -> bool:
    try:
        _backend()
        return True
    except Exception:
        return False


def safe_is_configured(provider: str) -> bool:
    try:
        return is_configured(provider)
    except Exception:
        return False
