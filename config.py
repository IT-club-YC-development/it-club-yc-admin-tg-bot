import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True, slots=True)
class Settings:
    bot_token: str


def load_settings() -> Settings:
    token = os.getenv("BOT_TOKEN", "").strip()
    if not token or token == "put_your_bot_token_here":
        raise RuntimeError(
            "BOT_TOKEN is missing. Copy .env.example to .env and set BOT_TOKEN."
        )
    return Settings(bot_token=token)


settings = load_settings()
