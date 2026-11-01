"""Versioned, dependency-free schemas for Plug Native AI Bridge."""

from __future__ import annotations

import re
from typing import Any

PROTOCOL_VERSION = "plug-native-v1"
SERVICE_NAME = "ai-workplace-bridge"
MAX_REQUEST_ID_LENGTH = 128
MAX_MESSAGE_LENGTH = 256_000
_REQUEST_ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._:-]{0,127}$")


class ProtocolValidationError(ValueError):
    """Raised when a bridge payload does not match the protocol."""


def validate_request_id(value: Any) -> str:
    if not isinstance(value, str) or not _REQUEST_ID_RE.fullmatch(value):
        raise ProtocolValidationError("request_id must be 1-128 safe characters")
    return value


def validate_chat_request(payload: Any) -> dict[str, Any]:
    """Validate the future v1 chat request shape; no chat endpoint exists yet."""
    if not isinstance(payload, dict):
        raise ProtocolValidationError("request body must be a JSON object")

    allowed = {"protocol_version", "request_id", "session_id", "message", "context", "mode"}
    unknown = set(payload) - allowed
    if unknown:
        raise ProtocolValidationError(f"unknown request fields: {', '.join(sorted(unknown))}")

    if payload.get("protocol_version") != PROTOCOL_VERSION:
        raise ProtocolValidationError("unsupported or missing protocol_version")

    validate_request_id(payload.get("request_id"))

    message = payload.get("message")
    if not isinstance(message, str) or not message.strip():
        raise ProtocolValidationError("message must be a non-empty string")
    if len(message.encode("utf-8")) > MAX_MESSAGE_LENGTH:
        raise ProtocolValidationError("message exceeds maximum size")

    session_id = payload.get("session_id")
    if session_id is not None and (
        not isinstance(session_id, str) or not session_id.strip() or len(session_id) > 128
    ):
        raise ProtocolValidationError("session_id must be null or a non-empty string of at most 128 characters")

    context = payload.get("context", [])
    if not isinstance(context, list):
        raise ProtocolValidationError("context must be a list")
    if any(not isinstance(item, (str, dict)) for item in context):
        raise ProtocolValidationError("context items must be strings or objects")

    mode = payload.get("mode", "direct")
    if mode != "direct":
        raise ProtocolValidationError("only mode='direct' is defined in protocol v1")

    return {
        "protocol_version": PROTOCOL_VERSION,
        "request_id": payload["request_id"],
        "session_id": session_id,
        "message": message,
        "context": context,
        "mode": mode,
    }


def validate_chat_response(payload: Any, *, expected_request_id: str | None = None) -> dict[str, Any]:
    """Validate the future v1 chat response shape; no chat endpoint exists yet."""
    if not isinstance(payload, dict):
        raise ProtocolValidationError("response body must be a JSON object")

    allowed = {"protocol_version", "request_id", "status", "answer", "tasks", "error"}
    unknown = set(payload) - allowed
    if unknown:
        raise ProtocolValidationError(f"unknown response fields: {', '.join(sorted(unknown))}")

    if payload.get("protocol_version") != PROTOCOL_VERSION:
        raise ProtocolValidationError("unsupported or missing protocol_version")
    request_id = validate_request_id(payload.get("request_id"))
    if expected_request_id is not None and request_id != expected_request_id:
        raise ProtocolValidationError("response request_id does not match request")

    status = payload.get("status")
    if status not in {"completed", "failed"}:
        raise ProtocolValidationError("status must be 'completed' or 'failed'")

    answer = payload.get("answer")
    if status == "completed" and not isinstance(answer, str):
        raise ProtocolValidationError("completed response requires string answer")
    if status == "failed" and answer is not None and not isinstance(answer, str):
        raise ProtocolValidationError("failed response answer must be null or a string")

    tasks = payload.get("tasks", [])
    if not isinstance(tasks, list):
        raise ProtocolValidationError("tasks must be a list")

    error = payload.get("error")
    if error is not None and not isinstance(error, dict):
        raise ProtocolValidationError("error must be null or an object")

    return dict(payload)


def health_payload() -> dict[str, Any]:
    return {
        "protocol_version": PROTOCOL_VERSION,
        "service": SERVICE_NAME,
        "status": "ok",
    }


def capabilities_payload() -> dict[str, Any]:
    """Advertise only endpoints that are implemented and available."""
    return {
        "protocol_version": PROTOCOL_VERSION,
        "service": SERVICE_NAME,
        "capabilities": {
            "health": True,
            "capabilities": True,
            "chat": False,
            "planning": False,
            "task_decomposition": False,
            "tool_use": False,
            "streaming": False,
            "persistent_memory": False,
        },
        "endpoints": {
            "health": "GET /v1/health",
            "capabilities": "GET /v1/capabilities",
        },
    }
