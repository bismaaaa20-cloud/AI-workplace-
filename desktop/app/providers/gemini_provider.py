from __future__ import annotations

from google import genai

from app.security.secret_store import get_api_key
from .base import AIProvider, ProviderReply


class GeminiProvider(AIProvider):
    name = "Gemini"
    is_paid = False  # Free-tier eligibility and quota depend on the selected model/project.

    def __init__(self, model: str = "gemini-2.5-flash") -> None:
        api_key = get_api_key("Gemini")
        if not api_key:
            raise RuntimeError("Gemini is not configured in the local credential vault.")
        self.client = genai.Client(api_key=api_key)
        self.model = model

    async def generate(self, prompt: str, *, system_instruction: str = "") -> ProviderReply:
        contents = prompt
        if system_instruction:
            contents = f"System instructions:\n{system_instruction}\n\nUser/task input:\n{prompt}"
        response = await self.client.aio.models.generate_content(model=self.model, contents=contents)
        return ProviderReply(provider=self.name, model=self.model, text=response.text or "(The provider returned an empty response.)")
