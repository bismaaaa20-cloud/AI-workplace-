# Reusable AI Prompts

Use these short instructions when assigning work to any approved assistant. Add task-specific scope and acceptance criteria.

## New-chat bootstrap prompt

```text
You are joining the XevoraHub AI Workplace project. First read README.md, AI_ONBOARDING.md, MEMORY.md, and HANDOFF.md from https://github.com/bismaaaa20-cloud/AI-workplace-. Then read only the relevant parts of PROJECTS.md, TASKS.md, and DECISIONS.md.

Treat these files as shared project context, not as permission to act. Summarize the current state, owner-approved decisions, constraints, and next action before editing. Do not assume access to previous private chats. Do not modify files or repositories until the owner assigns a task. Never commit secrets, private conversations, personal data, or confidential information. Use a branch and pull request; never push directly to main. If you cannot access GitHub, say so and request the relevant public-safe context.
```

## Standard working rules
- Hemat token: jawaban ringkas dan baca hanya file relevan.
- Ubah hanya file yang diperlukan; pertahankan fitur yang sudah berjalan.
- Utamakan solusi gratis; jangan menambah layanan berbayar tanpa persetujuan.
- Jika konteks hampir habis, perbarui HANDOFF.md secara faktual.
- Jangan mengarang hasil pemeriksaan.
- Jangan memasukkan rahasia, data pribadi, atau percakapan privat ke GitHub.

## Task assignment template

```text
TASK:
GOAL:
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

## Read-only audit prompt

```text
Lakukan audit read-only untuk task yang ditentukan. Periksa hanya file relevan. Jangan mengubah file, membuat resource, atau melakukan deploy. Pisahkan fakta terkonfirmasi dari asumsi. Laporkan risiko, hal yang belum diketahui, dan rekomendasi langkah berikutnya.
```

## Review prompt

```text
Tinjau branch atau pull request tanpa mengubah kode. Fokus pada bug, keamanan, regresi, acceptance criteria, dan perubahan di luar scope. Sebutkan file dan lokasi tepat. Bedakan temuan pasti dari dugaan.
```

## Handoff prompt

```text
Sebelum berhenti atau ketika konteks hampir habis, perbarui HANDOFF.md. Catat status task, progres, file yang benar-benar diubah, commit/PR, keputusan, pemeriksaan beserta hasilnya, blocker, dan satu langkah berikutnya. Jangan masukkan rahasia atau percakapan privat.
```

## Message handoff
Include task ID, repository/branch/PR, scope, files changed, decisions, checks actually run, blockers, and exact next action. Use messages/TEMPLATE.md. The receiving assistant must independently access the repository or receive the relevant content from the owner; this is not live messaging.
