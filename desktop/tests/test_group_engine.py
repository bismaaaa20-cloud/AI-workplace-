import asyncio

from app.core.group_engine import GroupEngine
from app.providers.base import AIProvider, ProviderReply


class FakeProvider(AIProvider):
    def __init__(self, name: str) -> None:
        self.name = name

    async def generate(self, prompt: str, *, system_instruction: str = "") -> ProviderReply:
        return ProviderReply(self.name, "fake", f"reply from {self.name}")


def test_group_engine_runs_initial_and_review_rounds():
    engine = GroupEngine([FakeProvider("A"), FakeProvider("B")], max_rounds=2)
    turns = asyncio.run(engine.discuss("Discuss the architecture"))
    assert len(turns) == 4
    assert turns[0].provider == "A"
    assert turns[2].provider == "A · review"


def test_group_engine_caps_rounds():
    engine = GroupEngine([FakeProvider("A")], max_rounds=99)
    assert engine.max_rounds == 3
