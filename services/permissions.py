"""Business-level permission interface."""
from typing import Protocol


class PermissionService(Protocol):
    async def has_permission(
        self, *, chat_id: int, user_id: int, action: str
    ) -> bool:
        """Return whether user_id may perform action in chat_id."""
        ...
