# Function contracts

These contracts are the shared interface for the team. If a task needs a change, discuss it before changing function names or return types.

## Database functions (`database/queries.py`)

All functions are `async`. The first parameter is an active SQLAlchemy `AsyncSession`. These functions flush pending changes but do not commit. The caller owns the transaction.

### `get_user(session, chat_id, user_id) -> User | None`
Returns the user row, or `None` if the user is not in the database.

### `upsert_user(session, chat_id, user_id, username) -> User`
Creates the user if absent; otherwise updates the username. Does not reset `first_seen_at`.

### `create_action(session, *, chat_id, user_id, moderator_id, action_type, reason=None, expires_at=None) -> Action`
Adds a `warn`, `mute`, or `ban` record and flushes it. Does not call Telegram.

### `get_warning_count(session, chat_id, user_id, since) -> int`
Counts non-revoked warning actions created on or after the supplied timezone-aware datetime.

### `get_user_actions(session, chat_id, user_id) -> list[Action]`
Returns the user's action history, newest first.

### `get_active_punishments(session, chat_id, user_id, now) -> list[Action]`
Returns non-revoked mute/ban records whose expiry is in the future or absent. A `NULL` expiry is treated as permanent; callers should only create permanent bans this way.

### `get_role(session, chat_id, user_id) -> str | None`
Returns `moderator`, `admin`, or `None`.

### `log_action(session, *, chat_id, actor_id, action, result, target_user_id=None, details=None) -> None`
Adds an audit-log entry. `result` should be `success`, `failure`, or `unknown`.

## Handler conventions

- Commands target the user whose message is replied to.
- Validate that a target exists before calling a service.
- Never construct raw SQL in a handler.
- User-facing command errors should be short and clear.
- Do not swallow unexpected exceptions silently.

## Service conventions

- Services implement business rules and coordinate database functions and Telegram API calls.
- Services must not depend on `Message` objects; pass primitive IDs, values, or explicit data structures.
- Do not report an action as successful until Telegram confirms it.
- The fifth warning in a rolling 30-day window triggers a 30-minute mute and admin notification. Ensure repeated warnings do not retrigger the same threshold event.

## Transaction ownership

Database functions call `flush()` but never `commit()`. A handler or service should use `async with SessionFactory.begin() as session:` to make a group of database changes atomic. Telegram API calls cannot participate in a PostgreSQL transaction; if a Telegram call fails, record the failure separately and do not persist a false successful punishment.
