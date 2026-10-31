"""Muk's lightweight context-aware Skill/MCP/Plugin selector.

This module plans tool selection only. It never executes external tools or performs
side effects. A host application must provide the live registry and executor.
Python standard library only.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Iterable
import re

@dataclass(frozen=True)
class Capability:
    id: str
    name: str
    kind: str                 # skill | mcp | plugin | agent
    description: str = ""
    intents: tuple[str, ...] = ()
    keywords: tuple[str, ...] = ()
    available: bool = False
    authorized: bool = False
    cost: str = "unknown"    # free | metered | paid | unknown
    read_only: bool = True
    requires_confirmation: bool = False
    input_types: tuple[str, ...] = ("text",)
    metadata: dict[str, Any] = field(default_factory=dict)

@dataclass
class Route:
    intent: str
    direct_answer: bool
    selected: list[dict[str, Any]]
    needs_confirmation: list[str]
    unavailable_matches: list[str]
    rationale: str

INTENT_TERMS = {
    "code_debug": ("debug", "bug", "error", "fix", "syntax", "luau", "lua", "python", "script", "kode"),
    "coding": ("buat fitur", "implement", "program", "coding", "function", "fungsi", "refactor"),
    "research": ("research", "riset", "cari informasi", "terbaru", "sumber", "bandingkan", "search"),
    "document_analysis": ("analisis dokumen", "ringkas dokumen", "pdf", "docx", "laporan", "summarize file"),
    "email": ("email", "gmail", "inbox", "surat elektronik"),
    "calendar": ("jadwal", "kalender", "meeting", "rapat", "schedule"),
    "file_search": ("cari file", "temukan dokumen", "file proyek", "repository"),
    "explain": ("apa itu", "jelaskan", "maksudnya", "how does", "what is"),
}
ACTION_TERMS = ("kirim", "send", "hapus", "delete", "buat event", "jadwalkan", "publish", "deploy", "purchase", "beli", "ubah", "edit")

def classify_intent(message: str) -> str:
    text = message.casefold()
    scores = {intent: sum(1 for term in terms if term in text) for intent, terms in INTENT_TERMS.items()}
    best = max(scores, key=scores.get)
    return best if scores[best] else "general"

def _score(message: str, intent: str, cap: Capability) -> int:
    text = message.casefold()
    score = 0
    if intent in cap.intents: score += 8
    for word in cap.keywords:
        if word.casefold() in text: score += 3
    for word in re.findall(r"[a-zA-Z0-9_+-]{3,}", cap.name + " " + cap.description):
        if word.casefold() in text: score += 1
    return score

def route_message(message: str, capabilities: Iterable[Capability], *,
                  free_only: bool = True, max_tools: int = 3) -> Route:
    """Return a safe selection plan; never calls tools.

    Unavailable/unauthorized candidates are reported, not selected. Paid/metered
    candidates are excluded by default. Non-read-only actions are gated.
    """
    intent = classify_intent(message)
    caps = list(capabilities)
    scored = sorted(((_score(message, intent, c), c) for c in caps),
                    key=lambda pair: pair[0], reverse=True)
    selected, confirmations, unavailable = [], [], []
    action_requested = any(t in message.casefold() for t in ACTION_TERMS)
    for score, cap in scored:
        if score < 3: continue
        if not cap.available or not cap.authorized:
            unavailable.append(cap.id); continue
        if free_only and cap.cost != "free": continue
        if not cap.read_only and not action_requested:
            continue
        item = {"id": cap.id, "name": cap.name, "kind": cap.kind,
                "score": score, "read_only": cap.read_only}
        selected.append(item)
        if cap.requires_confirmation or not cap.read_only:
            confirmations.append(cap.id)
        if len(selected) >= max_tools: break
    if intent == "general" or (intent == "explain" and not selected):
        direct = True
    else:
        direct = not bool(selected)
    reason = ("No eligible registered capability; answer directly or provide a manual handoff."
              if not selected else "Selected the highest-scoring available, authorized, policy-compliant capabilities.")
    return Route(intent, direct, selected, confirmations, unavailable, reason)

def capability_from_dict(data: dict[str, Any]) -> Capability:
    """Load a capability record from JSON-compatible data."""
    return Capability(
        id=str(data["id"]), name=str(data["name"]), kind=str(data["kind"]),
        description=str(data.get("description", "")),
        intents=tuple(data.get("intents", ())), keywords=tuple(data.get("keywords", ())),
        available=bool(data.get("available", False)),
        authorized=bool(data.get("authorized", False)),
        cost=str(data.get("cost", "unknown")),
        read_only=bool(data.get("read_only", True)),
        requires_confirmation=bool(data.get("requires_confirmation", False)),
        input_types=tuple(data.get("input_types", ("text",))),
        metadata=dict(data.get("metadata", {})),
    )
