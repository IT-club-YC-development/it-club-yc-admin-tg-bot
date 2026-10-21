from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="info")


@router.message(Command("info"))
async def info_command(message: Message) -> None:
    await message.answer(
        "🤖 <b>Інформація про бота</b>\n\n"
        "Бот допомагає адміністраторам керувати чатом.\n\n"
        "📋 <b>Команди:</b>\n"
        "/info - інформація про бота\n"
        "/help - список доступних команд",
    )
