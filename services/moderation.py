"""Business-level moderation interface; implementation intentionally omitted."""
from typing import Protocol

from database.models import Punishment, PunishmentType


class ModerationService(Protocol):
    async def issue_punishment(
        self,
        *,
        chat_id: int,
        moderator_id: int,
        target_user_id: int,
        punishment_type: PunishmentType,
        reason: str,
        duration_seconds: int | None = None,
    ) -> Punishment:
        """Validate policy, create a pending record, apply Telegram action,
        then persist the final status/result. Raises domain errors on failure.
        """
        ...

    async def revoke_active_ban(
        self, *, chat_id: int, moderator_id: int, target_user_id: int
    ) -> Punishment | None:
        """Revoke the active ban; preserve the original punishment record."""
        ...

    async def get_active_punishment(
        self, *, chat_id: int, target_user_id: int,
        punishment_type: PunishmentType | None = None,
    ) -> Punishment | None:
        ...

    async def get_punishment_history(
        self, *, chat_id: int, target_user_id: int, limit: int = 50, offset: int = 0
    ) -> list[Punishment]:
        ...
