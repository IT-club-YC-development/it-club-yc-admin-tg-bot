from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart())
async def start_command(message: Message) -> None:
    await message.answer(
        "OptiBot is running.\n"
        "Команды модерации будут добавлены в следующих задачах."
    )
