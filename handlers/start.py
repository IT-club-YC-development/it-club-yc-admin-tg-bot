from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router(name="start")


@router.message(CommandStart())
async def start_handler(message: Message) -> None:
    await message.answer(
        "Hi! I'm OptiBot — a bot for moderators and admins.\n\n"
        "I am currently under development."
    )
