"""Local, loopback-only Plug Native AI Bridge.

This package currently exposes health and capability discovery only. It does
not execute prompts or provide a Muk runtime.
"""

from app.bridge.schemas import PROTOCOL_VERSION

__all__ = ["PROTOCOL_VERSION"]
