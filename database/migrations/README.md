# Database migrations

After configuring `.env` and starting PostgreSQL:

```bash
alembic revision --autogenerate -m "create initial tables"
alembic upgrade head
```

Review generated migration files before applying them. Never commit secrets from `.env`.
