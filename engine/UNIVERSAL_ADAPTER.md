# UAWA Universal Adapter

Use UTF-8 Markdown for documents and YAML for structured records. Model internals may differ; preserve field meaning.

    protocol:
      name: UAWA
      version: 1.0.0
    agent:
      id: AI-UNREGISTERED
      registry_status: unknown
    context:
      rules_loaded: false
      personal_notebook_loaded: false
      shared_memory_loaded: false
    task:
      id: ''
      status: NOT_STARTED
    permissions:
      read: unknown
      write_own_notebook: unknown
      propose_shared_memory: unknown
      approve_shared_memory: false
    result:
      status: NOT_STARTED
      evidence: []
      blockers: []

Unknown capabilities and permissions remain unknown, never implicitly allowed. This schema does not authenticate agents or enforce access control. Provide Markdown fallback if YAML tooling is unavailable.