# Architecture

## Request flow

`Telegram update -> handler -> service -> database functions -> PostgreSQL`

Handlers are responsible for Telegram input/output and basic argument validation.
Services contain moderation rules and coordinate database and Telegram operations.
Database functions run SQLAlchemy queries and return model objects or simple values.
Models define the four database tables.

## Rules

- Keep handlers small; do not put SQL queries in handlers.
- Do not call Telegram APIs from database functions.
- Use async functions for Telegram and database I/O.
- Do not commit `.env` or bot tokens.
- Use timezone-aware datetimes; store and compare timestamps in UTC.
- Use Alembic migrations for schema changes; do not use `Base.metadata.create_all()` in production.
- Keep pull requests focused and explain how to test the change.

## MVP commands

- `/start`: confirm the bot is alive.
- `/info`: information about the user targeted by replying to their message.
- `/warn`: add a warning; on the fifth active warning within 30 days, mute for 30 minutes and notify admins.
- `/mute`: restrict a replied-to user for a specified duration.
- `/ban`: ban a replied-to user temporarily or permanently.
- `/unban`: unban a replied-to user.

Targeting by replying to a message is the MVP convention. Username lookup is out of scope initially.
