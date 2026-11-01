"""Loopback-only HTTP bridge exposing health and capability discovery.

Run from the desktop directory with:
    PLUG_BRIDGE_TOKEN='<shared random secret>' python -m app.bridge.server

No chat endpoint or AI inference backend is implemented in this phase.
"""

from __future__ import annotations

import hmac
import ipaddress
import json
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import Any
from urllib.parse import urlsplit

from app.bridge.schemas import capabilities_payload, health_payload

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8765
MIN_TOKEN_LENGTH = 32
MAX_CONCURRENT_REQUESTS = 16


class _BridgeHTTPServer(ThreadingHTTPServer):
    daemon_threads = True
    allow_reuse_address = False


def _json_bytes(payload: dict[str, Any]) -> bytes:
    return json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def create_server(
    token: str,
    *,
    host: str = DEFAULT_HOST,
    port: int = DEFAULT_PORT,
    max_concurrency: int = MAX_CONCURRENT_REQUESTS,
) -> ThreadingHTTPServer:
    """Create the bridge server. Host must resolve to a loopback IP."""
    try:
        address = ipaddress.ip_address(host)
    except ValueError as exc:
        raise ValueError("bridge host must be a loopback IP address") from exc
    if not address.is_loopback:
        raise ValueError("bridge may bind only to a loopback IP address")
    if not isinstance(token, str) or len(token) < MIN_TOKEN_LENGTH:
        raise ValueError(f"bridge token must contain at least {MIN_TOKEN_LENGTH} characters")
    if isinstance(port, bool) or not isinstance(port, int) or not 0 <= port <= 65535:
        raise ValueError("port must be an integer between 0 and 65535")
    if isinstance(max_concurrency, bool) or not isinstance(max_concurrency, int) or max_concurrency < 1:
        raise ValueError("max_concurrency must be a positive integer")

    request_slots = threading.BoundedSemaphore(max_concurrency)

    class BridgeHandler(BaseHTTPRequestHandler):
        server_version = "PlugNativeBridge/1"
        sys_version = ""

        def log_message(self, _format: str, *_args: Any) -> None:
            # Avoid logging request headers or any potentially sensitive material.
            return

        def _send_json(self, status: int, payload: dict[str, Any]) -> None:
            body = _json_bytes(payload)
            self.send_response(status)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.end_headers()
            self.wfile.write(body)

        def do_GET(self) -> None:
            if not request_slots.acquire(blocking=False):
                self._send_json(503, {"error": {"code": "busy", "message": "bridge concurrency limit reached"}})
                return
            try:
                supplied = self.headers.get("Authorization", "")
                expected = f"Bearer {token}"
                if not hmac.compare_digest(supplied, expected):
                    self._send_json(401, {"error": {"code": "unauthorized", "message": "valid bearer token required"}})
                    return

                path = urlsplit(self.path).path
                if path == "/v1/health":
                    self._send_json(200, health_payload())
                elif path == "/v1/capabilities":
                    self._send_json(200, capabilities_payload())
                else:
                    self._send_json(404, {"error": {"code": "not_found", "message": "endpoint not found"}})
            finally:
                request_slots.release()

        def do_POST(self) -> None:
            self._send_json(404, {"error": {"code": "not_found", "message": "endpoint not found"}})

        def do_PUT(self) -> None:
            self._send_json(404, {"error": {"code": "not_found", "message": "endpoint not found"}})

        def do_DELETE(self) -> None:
            self._send_json(404, {"error": {"code": "not_found", "message": "endpoint not found"}})

    server = _BridgeHTTPServer((host, port), BridgeHandler)
    return server


def main() -> int:
    token = os.environ.get("PLUG_BRIDGE_TOKEN", "")
    if not token:
        raise SystemExit(
            "PLUG_BRIDGE_TOKEN is required. Generate a random local secret and "
            "configure the same value in the Plug client environment."
        )
    host = os.environ.get("PLUG_BRIDGE_HOST", DEFAULT_HOST)
    port_text = os.environ.get("PLUG_BRIDGE_PORT", str(DEFAULT_PORT))
    try:
        port = int(port_text)
        server = create_server(token, host=host, port=port)
    except (ValueError, OSError) as exc:
        raise SystemExit(f"Unable to start Plug Native AI Bridge: {exc}") from exc

    print(f"Plug Native AI Bridge listening on http://{host}:{server.server_port}")
    print("Available endpoints: GET /v1/health, GET /v1/capabilities")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
