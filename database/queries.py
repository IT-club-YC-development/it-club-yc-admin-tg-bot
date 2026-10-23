"""Small database functions shared by handlers and services.

These are intentionally ordinary functions, not a repository class hierarchy.
More functions can be added when command tasks are implemented.
"""
from datetime import datetime

from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Action, ActionLog, Moderator, User


async def get_user(
    session: AsyncSession, chat_id: int, user_id: int
) -> User | None:
    return await session.get(User, (chat_id, user_id))


async def upsert_user(
    session: AsyncSession,
    chat_id: int,
    user_id: int,
    username: str | None,
) -> User:
    user = await get_user(session, chat_id, user_id)
    if user is None:
        user = User(chat_id=chat_id, user_id=user_id, username=username)
        session.add(user)
    else:
        user.username = username
    await session.flush()
    return user


async def create_action(
    session: AsyncSession,
    *,
    chat_id: int,
    user_id: int,
    moderator_id: int,
    action_type: str,
    reason: str | None = None,
    expires_at: datetime | None = None,
) -> Action:
    action = Action(
        chat_id=chat_id,
        user_id=user_id,
        moderator_id=moderator_id,
        action_type=action_type,
        reason=reason,
        expires_at=expires_at,
    )
    session.add(action)
    await session.flush()
    return action


async def get_warning_count(
    session: AsyncSession,
    chat_id: int,
    user_id: int,
    since: datetime,
) -> int:
    statement = select(func.count()).select_from(Action).where(
        Action.chat_id == chat_id,
        Action.user_id == user_id,
        Action.action_type == "warn",
        Action.created_at >= since,
        Action.revoked_at.is_(None),
    )
    return int((await session.scalar(statement)) or 0)


async def get_user_actions(
    session: AsyncSession, chat_id: int, user_id: int
) -> list[Action]:
    statement = (
        select(Action)
        .where(Action.chat_id == chat_id, Action.user_id == user_id)
        .order_by(Action.created_at.desc())
    )
    return list((await session.scalars(statement)).all())


async def get_active_punishments(
    session: AsyncSession,
    chat_id: int,
    user_id: int,
    now: datetime,
) -> list[Action]:
    statement = select(Action).where(
        Action.chat_id == chat_id,
        Action.user_id == user_id,
        Action.action_type.in_(("mute", "ban")),
        Action.revoked_at.is_(None),
        # Permanent bans have no expiry. Mutes should always have one.
        (Action.expires_at.is_(None) | (Action.expires_at > now)),
    )
    return list((await session.scalars(statement)).all())


async def get_role(
    session: AsyncSession, chat_id: int, user_id: int
) -> str | None:
    moderator = await session.get(Moderator, (chat_id, user_id))
    return moderator.role if moderator else None


async def log_action(
    session: AsyncSession,
    *,
    chat_id: int,
    actor_id: int,
    action: str,
    result: str,
    target_user_id: int | None = None,
    details: str | None = None,
) -> None:
    session.add(
        ActionLog(
            chat_id=chat_id,
            actor_id=actor_id,
            target_user_id=target_user_id,
            action=action,
            result=result,
            details=details,
        )
    )
    await session.flush()
