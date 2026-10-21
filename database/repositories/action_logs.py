"""Public contract for append-only moderation audit logs."""
from typing import Protocol

from database.models import ActionLog, ActionLogCreate


class ActionLogRepository(Protocol):
    async def create(self, data: ActionLogCreate) -> ActionLog:
        ...

    async def list_for_chat(
        self, *, chat_id: int, limit: int = 100, offset: int = 0
    ) -> list[ActionLog]:
        ...
