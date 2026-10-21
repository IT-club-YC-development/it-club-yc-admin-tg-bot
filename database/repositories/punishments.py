"""Public contract for punishment persistence. No database implementation yet."""
from datetime import datetime
from typing import Protocol

from database.models import Punishment, PunishmentCreate, PunishmentStatus, PunishmentType


class PunishmentRepository(Protocol):
    async def create(self, data: PunishmentCreate) -> Punishment:
        """Insert a punishment with PENDING status and return persisted record."""
        ...

    async def get_by_id(self, *, punishment_id: int) -> Punishment | None:
        ...

    async def get_active(
        self,
        *,
        chat_id: int,
        target_user_id: int,
        punishment_type: PunishmentType | None = None,
        as_of: datetime | None = None,
    ) -> Punishment | None:
        """Return one active, non-expired punishment; WARN is history-only."""
        ...

    async def list_history(
        self,
        *,
        chat_id: int,
        target_user_id: int,
        limit: int = 50,
        offset: int = 0,
    ) -> list[Punishment]:
        ...

    async def update_status(
        self,
        *,
        punishment_id: int,
        status: PunishmentStatus,
        telegram_error: str | None = None,
    ) -> Punishment:
        """Update status after the external Telegram operation has a result."""
        ...

    async def revoke_active_ban(
        self,
        *,
        chat_id: int,
        target_user_id: int,
        revoked_by: int,
        revoked_at: datetime,
    ) -> Punishment | None:
        """Atomically revoke only an active ban; retain its history record."""
        ...
