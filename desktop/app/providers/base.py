from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class ProviderReply:
    provider: str
    model: str
    text: str


class AIProvider(ABC):
    name: str
    is_paid: bool = False

    @abstractmethod
    async def generate(self, prompt: str, *, system_instruction: str = "") -> ProviderReply:
        """Generate one response. Implementations must not perform hidden paid fallback."""
        raise NotImplementedError
