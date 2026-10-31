# Muk router prototype

This is a small Python-standard-library prototype of Muk's context-aware capability selector.

## What it does
- Classifies a message into a basic intent.
- Scores registered Skills, MCP tools, and Plugin actions.
- Selects only capabilities marked available and authorized.
- Excludes paid/metered/unknown-cost capabilities when `free_only=True` (the default).
- Gates write actions and returns confirmation requirements.
- Returns a routing plan; it does not execute tools.

## Quick start

```python
from muk.router import Capability, route_message

registry = [
    Capability(
        id="bugscout.gate_check",
        name="BugScout gate_check",
        kind="mcp",
        description="Check Lua script syntax and selected errors",
        intents=("code_debug",),
        keywords=("lua", "script", "bug"),
        available=True,       # set only after live health check
        authorized=True,      # set only after permission check
        cost="free",
    )
]

plan = route_message("Periksa bug script Lua ini", registry)
print(plan)
```

Run tests from the repository root:

```sh
python -m unittest discover -s tests -v
```

## Important integration boundary

The example registry deliberately marks every integration unavailable. A host application must discover real Skills/MCP/Plugin capabilities, verify connection health and permissions, then build Capability records. It must also supply actual executors, user-confirmation UI, audit logging, and agent handoff. Do not set `available=True` or `authorized=True` by assumption.

This prototype is not a complete Muk runtime, does not connect BugScout or Plugins, and does not call AI APIs. It is intentionally lightweight and free of third-party dependencies.
