# Project Map

This file describes project boundaries and current status. It is a coordination note, not a source of deployment credentials or private configuration.

## 1. XevoraHub Roblox / GUI
- Repository: https://github.com/bismaaaa20-cloud/GUI
- Purpose: Roblox/Lua-related source and UI assets.
- Boundary: keep runtime scripts and assets separate from AI coordination documents.
- Protected by default: loader, game mappings, key logic, UI code, and assets. Change only when a task explicitly names the required files and the owner approves.
- Coordination documents were removed from this repository through merged PR #2. The AI Workplace remains separate.

## 2. XevoraHub Get Key website
- Repository: not recorded here yet; do not guess or create one.
- Status: architecture proposal only; no code change or infrastructure deployment is authorized by this note.
- Proposed stack from the AI Cloud assistant:
  - Frontend: Cloudflare Pages static site.
  - API: Pages Functions with Hono.
  - Database: Cloudflare D1.
  - Scheduled cleanup: a small Cron-triggered Worker.
  - Login: Discord OAuth (GitHub OAuth as a possible alternative).
  - CAPTCHA: Cloudflare Turnstile.
  - Initial billing: manual owner confirmation.
- Important design notes from the proposal:
  - Store generated keys as hashes; show the raw key only once.
  - Store session tokens as hashes.
  - Use prepared SQL statements, server-side authorization, secure cookies, input validation, rate limits, and secret storage outside Git.
  - Keep preview and production environments separate.
  - Do not expose provider secrets in client-side code or repository files.
- Not yet verified: exact current free-tier quotas, CPU limits under real workload, rate-limiting coverage, backup/restore availability, OAuth provider requirements, link-gate provider rules, and deployment workflow details.
- Pending owner decisions: approve/revise the stack, Discord login, manual billing, repository privacy, Turnstile, and GitHub Actions.

## 3. AI Workplace
- Repository: https://github.com/bismaaaa20-cloud/AI-workplace-
- Purpose: public-safe coordination, task ownership, decisions, and handoffs.
- It must not become a place to store app secrets or private user data.

## General rule
A plan is not approval. Do not create infrastructure, deploy services, add paid dependencies, or modify application repositories until the owner explicitly approves the relevant task.
