# Local API Secret Vault — Security Requirements

**Status:** proposed implementation and acceptance requirements.

## Storage boundary
- Real provider API keys belong on the owner's PC only. Never commit, upload, synchronize, or back them up to this public GitHub repository.
- Use the operating system credential manager: Windows Credential Manager, macOS Keychain, or Linux Secret Service through Python Keyring.
- Fail closed if no secure backend is available. Never silently fall back to plaintext, JSON, TOML, YAML, SQLite, or .env.
- .env.example may contain variable names only. GitHub stores source code, security requirements, and empty templates only.

## Desktop UI contract
- Settings → API Security accepts a provider key in a password-masked field.
- Save directly to the OS credential manager. Never echo the key back.
- Show only Configured / Not configured; never show full or partial keys.
- Support replace and delete with confirmation.
- Never put secrets in clipboard, chat history, crash reports, analytics, logs, screenshots, support bundles, URLs, command-line arguments, or exception text.
- Clear the input field after save/cancel.

## Runtime boundary
- Retrieve a credential only immediately before constructing its provider client.
- Never expose credentials to prompts, agent messages, MCP arguments, or other providers.
- Keep provider network destinations fixed/allow-listed; reject arbitrary base URLs from model output.
- Do not log raw SDK exceptions. Return generic user-facing errors.
- UI masking cannot protect against malware, debuggers, administrator/root access, memory inspection, keyloggers, or a compromised OS.

## Billing safety
- Only explicitly approved free-tier models/plans may be enabled.
- No paid fallback, automatic upgrade, prepaid top-up, or billing-management permission.
- On quota exhaustion, stop with BLOCKED_FREE_QUOTA; never retry via a paid route.
- Never request bank credentials, payment card data, wallet access, or permission to spend money.
- Where a provider account can incur charges, the owner must independently disable billing/pay-as-you-go or set a hard provider-side budget before adding its key. A local app cannot guarantee a provider will not charge an account.
- GitHub MCP credentials must be separate and narrowly scoped. No billing or repository-secret-management permissions in desktop AI tools.

## Repository controls
- Keep .env, .env.* (except .env.example), secrets/, key files, logs, and local databases ignored.
- Enable GitHub secret scanning and push protection where available.
- If a key leaks, revoke/rotate it immediately. Removing it in a later commit does not erase Git history.
- Never run untrusted fork code in workflows that can access secrets.

## Acceptance checklist
- [ ] Masked key entry; key is not returned after save.
- [ ] Credentials persist using the OS vault.
- [ ] No plaintext fallback.
- [ ] Missing secure backend blocks saving/usage.
- [ ] No secret in UI errors or logs.
- [ ] No real secret in repository, history, tests, screenshots, or handoff.
- [ ] Quota exhaustion never invokes a paid route.
- [ ] Owner can replace and delete each stored key.
- [ ] Manual security review and desktop tests completed before release.

This design reduces accidental disclosure and protects secrets at rest. It cannot promise nobody can ever extract a key from a compromised or owner-controlled PC. Device security, OS updates, disk encryption, account lock, and malware protection remain necessary.
