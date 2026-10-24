import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import settings
from database.connection import close_database, init_database
from handlers.start import router as start_router
from handlers.moderation import router as moderation_router


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )

    bot = Bot(
        token=settings.bot_token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(moderation_router)

    await init_database()
    try:
        await dp.start_polling(bot)
    finally:
        await close_database()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
