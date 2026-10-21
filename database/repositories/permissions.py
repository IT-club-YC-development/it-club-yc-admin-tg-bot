"""Public contract for chat-scoped role persistence."""
from typing import Protocol

from database.models import ChatMemberRole, ChatRole


class PermissionRepository(Protocol):
    async def get_role(
        self, *, chat_id: int, user_id: int
    ) -> ChatMemberRole | None:
        ...

    async def set_role(
        self,
        *,
        chat_id: int,
        user_id: int,
        role: ChatRole,
        assigned_by: int,
    ) -> ChatMemberRole:
        """Create or replace a role assignment within this chat only."""
        ...

    async def remove_role(self, *, chat_id: int, user_id: int) -> bool:
        """Return True if a custom role assignment was removed."""
        ...
