# OptiBot

Telegram moderation bot MVP built with Python, aiogram 3, SQLAlchemy 2 async, and PostgreSQL.

## MVP scope

- `/start`
- `/info`
- `/warn`
- `/mute`
- `/ban`
- `/unban`
- Five warnings within a rolling 30-day window trigger a 30-minute mute and an admin notification.

Currently only `/start` is implemented. The other commands are tasks for contributors.

## Requirements

- Python 3.11+
- PostgreSQL 14+ (or another currently supported PostgreSQL release)
- Telegram bot token from BotFather

## Local setup

1. Create and activate a virtual environment:

   ```bash
   python3.11 -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a PostgreSQL database and user, then copy the example environment file:

   ```bash
   cp .env.example .env
   ```

   Set `BOT_TOKEN` and `DATABASE_URL` in `.env`.

4. Generate and review the initial database migration, then apply it:

   ```bash
   alembic revision --autogenerate -m "create initial tables"
   alembic upgrade head
   ```

5. Run the bot:

   ```bash
   python main.py
   ```

6. Run tests:

   ```bash
   pytest
   ```

## Project docs

- `docs/ARCHITECTURE.md` — responsibility of each layer.
- `docs/DATABASE.md` — table design and database rules.
- `docs/CONTRACTS.md` — function arguments, return values, and conventions.
- `docs/TASKS.md` — implementation tasks and acceptance criteria.

## Team rules

- Keep `.env` private.
- Work in feature branches and submit focused pull requests.
- Do not silently change shared contracts.
- Do not put SQL in handlers or Telegram API calls in database functions.
- Update documentation when a contract or behavior changes.
