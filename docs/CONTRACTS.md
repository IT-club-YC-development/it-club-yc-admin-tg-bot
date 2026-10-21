# OptiBot module contracts (MVP)

## General conventions
- Python 3.11+; aiogram 3; type hints required for public functions.
- Telegram identifiers are integers. Never use usernames as durable IDs.
- Database methods are async and perform persistence only.
- All datetimes are timezone-aware UTC.
- Repositories raise a documented persistence exception on DB failures; they must not silently return `None` for database errors.
- `None` means “record not found” only where the method explicitly returns an optional result.
- Pagination: `limit` and `offset`; implementations must validate or cap unsafe limits.
- `chat_id` is mandatory for all chat-scoped roles, punishments, and logs.
- `WARN` remains in history but is not considered an active restriction.
- `unban` changes the existing active ban record to `REVOKED`; it does not delete the original record.
- Failed Telegram API operations must be represented as `FAILED` and must never be treated as active.
- Audit logs should be append-only at application level.

## Repository API

### PunishmentRepository
- `create(data: PunishmentCreate) -> Punishment`: inserts a record in `PENDING`.
- `get_by_id(punishment_id: int) -> Punishment | None`.
- `get_active(chat_id, target_user_id, punishment_type=None, as_of=None) -> Punishment | None`.
- `list_history(chat_id, target_user_id, limit=50, offset=0) -> list[Punishment]`.
- `update_status(punishment_id, status, telegram_error=None) -> Punishment`.
- `revoke_active_ban(chat_id, target_user_id, revoked_by, revoked_at) -> Punishment | None`: atomic state change.

### PermissionRepository
- `get_role(chat_id, user_id) -> ChatMemberRole | None`.
- `set_role(chat_id, user_id, role, assigned_by) -> ChatMemberRole`.
- `remove_role(chat_id, user_id) -> bool`.

### ActionLogRepository
- `create(data: ActionLogCreate) -> ActionLog`.
- `list_for_chat(chat_id, limit=100, offset=0) -> list[ActionLog]`.

### UnitOfWork
Provides all repositories and transaction boundaries. Related persistence operations should be committed atomically. A concrete implementation owns commit/rollback behavior.

## Service API
- `PermissionService.has_permission(chat_id, user_id, action) -> bool`.
- `ModerationService.issue_punishment(...) -> Punishment`.
- `ModerationService.revoke_active_ban(...) -> Punishment | None`.
- `ModerationService.get_active_punishment(...) -> Punishment | None`.
- `ModerationService.get_punishment_history(...) -> list[Punishment]`.

## Suggested error model (implement before moderation commands)
Define domain exceptions such as:
- `PermissionDenied`
- `TargetNotFound`
- `InvalidPunishment`
- `PunishmentNotActive`
- `PersistenceError`
- `TelegramActionError`

Do not use broad `except Exception` to hide errors. Handlers should map known domain errors to user-facing replies and log unexpected exceptions.
