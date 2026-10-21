"""Database-independent DTOs shared by repositories and services."""
from dataclasses import dataclass
from datetime import datetime
from enum import StrEnum


class PunishmentType(StrEnum):
    WARN = "warn"
    MUTE = "mute"
    BAN = "ban"


class PunishmentStatus(StrEnum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    REVOKED = "revoked"
    FAILED = "failed"


class ActorActionStatus(StrEnum):
    SUCCESS = "success"
    FAILURE = "failure"
    DENIED = "denied"


class ChatRole(StrEnum):
    OWNER = "owner"
    ADMIN = "admin"
    MODERATOR = "moderator"
    MEMBER = "member"


@dataclass(frozen=True, slots=True)
class Punishment:
    id: int
    chat_id: int
    target_user_id: int
    moderator_id: int
    punishment_type: PunishmentType
    reason: str
    status: PunishmentStatus
    created_at: datetime
    expires_at: datetime | None
    revoked_at: datetime | None
    revoked_by: int | None
    telegram_error: str | None = None


@dataclass(frozen=True, slots=True)
class ChatMemberRole:
    chat_id: int
    user_id: int
    role: ChatRole
    assigned_by: int
    assigned_at: datetime


@dataclass(frozen=True, slots=True)
class ActionLog:
    id: int
    chat_id: int
    actor_user_id: int
    action: str
    status: ActorActionStatus
    created_at: datetime
    target_user_id: int | None = None
    reason: str | None = None
    details: str | None = None
    punishment_id: int | None = None


@dataclass(frozen=True, slots=True)
class PunishmentCreate:
    chat_id: int
    target_user_id: int
    moderator_id: int
    punishment_type: PunishmentType
    reason: str
    expires_at: datetime | None = None


@dataclass(frozen=True, slots=True)
class ActionLogCreate:
    chat_id: int
    actor_user_id: int
    action: str
    status: ActorActionStatus
    target_user_id: int | None = None
    reason: str | None = None
    details: str | None = None
    punishment_id: int | None = None
