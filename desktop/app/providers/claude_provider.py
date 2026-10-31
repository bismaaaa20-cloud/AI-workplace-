from __future__ import annotations

import os

from anthropic import AsyncAnthropic

from .base import AIProvider, ProviderReply


class ClaudeProvider(AIProvider):
    name = "Claude"
    is_paid = True

    def __init__(self, model: str = "claude-sonnet-4-5") -> None:
        if os.getenv("ENABLE_PAID_PROVIDERS", "false").lower() != "true":
            raise RuntimeError("Anthropic API is disabled. Explicitly enable paid providers first.")
        api_key = os.getenv("ANTHROPIC_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY is not configured.")
        self.client = AsyncAnthropic(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, *, system_instruction: str = "") -> ProviderReply:
        response = await self.client.messages.create(
            model=self.model,
            max_tokens=1200,
            system=system_instruction or "You are an assistant in AI Workplace.",
            messages=[{"role": "user", "content": prompt}],
        )
        text = "\n".join(block.text for block in response.content if getattr(block, "type", "") == "text")
        return ProviderReply(self.name, self.model, text)
