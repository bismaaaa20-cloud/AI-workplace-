from __future__ import annotations

import os

from openai import AsyncOpenAI

from .base import AIProvider, ProviderReply


class OpenAIProvider(AIProvider):
    name = "OpenAI"
    is_paid = True

    def __init__(self, model: str = "gpt-4.1-mini") -> None:
        if os.getenv("ENABLE_PAID_PROVIDERS", "false").lower() != "true":
            raise RuntimeError("OpenAI API is disabled. Explicitly enable paid providers first.")
        api_key = os.getenv("OPENAI_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not configured.")
        self.client = AsyncOpenAI(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, *, system_instruction: str = "") -> ProviderReply:
        response = await self.client.responses.create(
            model=self.model,
            instructions=system_instruction or "You are an assistant in AI Workplace.",
            input=prompt,
        )
        return ProviderReply(self.name, self.model, response.output_text)
