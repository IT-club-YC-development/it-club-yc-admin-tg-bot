"""Unit-of-work contract to allow related DB changes to commit atomically."""
from typing import Protocol

from database.repositories.punishments import PunishmentRepository
from database.repositories.permissions import PermissionRepository
from database.repositories.action_logs import ActionLogRepository


class UnitOfWork(Protocol):
    punishments: PunishmentRepository
    permissions: PermissionRepository
    action_logs: ActionLogRepository

    async def __aenter__(self) -> "UnitOfWork":
        ...

    async def __aexit__(self, exc_type, exc, traceback) -> None:
        """Commit on success, rollback on exception; implementation decides details."""
        ...

    async def commit(self) -> None:
        ...

    async def rollback(self) -> None:
        ...
