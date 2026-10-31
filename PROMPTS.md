# Reusable AI Prompts

Use these short instructions when assigning work to ChatGPT or the AI Cloud assistant. Add task-specific scope and acceptance criteria after the relevant block.

## Standard working rules

> **ATURAN KERJA**
> - Hemat token: jawaban ringkas; baca hanya file yang relevan, jangan audit ulang seluruh proyek tanpa alasan.
> - Ubah hanya file yang diperlukan. Jangan hapus atau ubah fitur yang sudah berjalan tanpa alasan dan persetujuan pemilik.
> - Utamakan solusi gratis. Hindari API berbayar, Supabase, Firebase, dan layanan cloud eksternal kecuali diminta atau disetujui pemilik.
> - Jika konteks hampir habis, perbarui HANDOFF.md: progres, file yang diubah, keputusan, masalah, dan langkah berikutnya.
> - Jangan mengarang hasil. Laporkan apa yang benar-benar selesai dan pemeriksaan yang benar-benar dijalankan.
> - Jangan memasukkan API key, token, password, data pribadi, atau percakapan privat ke GitHub.

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
Lakukan audit read-only untuk task yang ditentukan. Periksa hanya file yang relevan. Jangan mengubah file, membuat resource, atau melakukan deploy. Pisahkan fakta yang terkonfirmasi dari asumsi. Laporkan struktur yang relevan, risiko, hal yang belum diketahui, dan rekomendasi langkah kecil berikutnya. Jangan menyatakan pemeriksaan lulus jika tidak dijalankan.
```

## Review prompt

```text
Tinjau branch atau pull request yang diberikan tanpa mengubah kode. Fokus pada bug, keamanan, regresi, ketidaksesuaian acceptance criteria, dan perubahan di luar scope. Sebutkan file dan lokasi yang tepat. Bedakan temuan pasti dari dugaan. Jika tidak ada temuan, jelaskan batas review dan pemeriksaan yang tidak dapat dijalankan.
```

## Handoff prompt

```text
Sebelum berhenti atau ketika konteks hampir habis, perbarui HANDOFF.md secara ringkas dan faktual. Catat status task, progres, file yang benar-benar diubah, commit/PR, keputusan, pemeriksaan beserta hasilnya, blocker, dan satu langkah berikutnya. Jangan masukkan rahasia atau percakapan privat.
```

## Message handoff

When passing work between assistants, include:
- Task ID and repository/branch/PR link.
- What was requested and what is in/out of scope.
- Files inspected or changed.
- Decisions and assumptions.
- Checks actually run and results.
- Remaining questions or blockers.
- Exact next action for the receiving assistant.

A message in this repository is not a live notification and does not automatically transfer context or grant repository access. The receiving assistant must be given the relevant link/content through a supported integration or by the owner.
