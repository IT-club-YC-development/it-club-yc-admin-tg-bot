# MVP task board

## Before parallel implementation
- [ ] Tech lead reviews architecture and contracts.
- [ ] Create repository and protect `main` by convention: changes via pull requests.
- [ ] Add `.env` locally; never commit it.
- [ ] Agree on permission policy: Telegram admins only, or Telegram admins plus custom OptiBot roles.

## Task 1 — Database
Owner: database contributor
- [ ] Review `docs/DATABASE.md` and `docs/CONTRACTS.md`.
- [ ] Review/complete SQLAlchemy models.
- [ ] Generate and review initial Alembic migration.
- [ ] Implement remaining query functions as needed without changing contracts silently.
- [ ] Add database tests and setup instructions.
- Acceptance: clean PostgreSQL database can be migrated; query functions match contracts.

## Task 2 — `/info`
Owner: command contributor
- [ ] Implement `handlers/info.py`.
- [ ] Target user by reply.
- [ ] Show Telegram ID, username, warnings in the last 30 days, and active punishment history.
- [ ] Handle missing target and missing database user.
- [ ] Add tests or a manual test checklist.
- Acceptance: command uses service/database contracts, not raw SQL.

## Task 3 — `/warn`
Owner: command contributor
- [ ] Implement `handlers/warn.py` and warning service.
- [ ] Save warning with optional reason.
- [ ] Count warnings over rolling 30 days.
- [ ] On crossing the fifth-warning threshold, apply a 30-minute mute and notify admins.
- [ ] Prevent duplicate auto-mutes for the same threshold event.
- [ ] Log success/failure/unknown outcomes.
- Acceptance: old warnings do not count; a fifth warning triggers once; failed Telegram call is not shown as successful.

## Task 4 — `/mute`, `/ban`, `/unban`
Owner: moderation command contributor
- [ ] Implement handlers and service functions.
- [ ] Target by reply.
- [ ] Validate duration and reason.
- [ ] Check permissions and bot rights.
- [ ] Save confirmed actions and retain history on unban/revocation.
- [ ] Log failed or ambiguous API outcomes.
- Acceptance: valid actions work; invalid durations and insufficient rights return clear errors.

## Tech lead
- [ ] Maintain contracts and resolve interface questions.
- [ ] Review PRs.
- [ ] Integrate routers in `main.py`.
- [ ] Run full test checklist.
- [ ] Update README and docs as implementation evolves.
