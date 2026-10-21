"""Future database composition root.

Create the SQLAlchemy async engine/sessionmaker and concrete repositories here.
Do not create an engine at import time. Keep this module free of Telegram logic.
"""
from typing import Protocol

from database.repositories.uow import UnitOfWork


class UnitOfWorkFactory(Protocol):
    def __call__(self) -> UnitOfWork:
        """Return a fresh unit-of-work for one application operation."""
        ...
