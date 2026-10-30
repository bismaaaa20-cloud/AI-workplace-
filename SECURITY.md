# Security Rules

## Critical: repository is public
This repository is currently public. Assume every committed file, issue, pull request, commit message, and workflow log can be read by anyone.

## Never commit
- OpenAI API keys
- Anthropic API keys
- GitHub personal access tokens
- OAuth refresh/access tokens
- Passwords, private keys, recovery codes
- Private conversation contents or personal data

Deleting a secret from the latest file does not erase it from Git history. If a credential is exposed, revoke/rotate it immediately and review its usage.

## When an integration is implemented
1. Store credentials only in an approved secret manager (for GitHub Actions, repository or environment Actions secrets).
2. Use separate credentials for each provider and environment.
3. Grant minimum required permissions; avoid broad repository write permissions.
4. Never print secrets, request headers, or full environment variables in logs.
5. Validate webhook signatures and authenticate inbound requests.
6. Add rate limits, input validation, and replay protection where applicable.
7. Pin third-party actions to reviewed commit SHAs where practical.
8. Require human review before an AI-generated change is merged.
9. Rotate credentials periodically and immediately after suspected exposure.

## Important limitation
GitHub Actions secrets are not a substitute for a secure backend when a workflow needs to expose credentials to untrusted pull-request code. Do not pass secrets to workflows triggered by untrusted forks or unreviewed code.

## Reporting
If a credential is exposed, revoke it at the provider first. Then inspect GitHub history and workflow logs, remove the exposure where possible, and issue a replacement credential.
