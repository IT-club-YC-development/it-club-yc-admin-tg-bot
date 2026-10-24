

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="info")


@router.message(Command("info"))
async def info_command(message: Message) -> None:
    if message.reply_to_message is None:
        await message.answer(
            "Використовуй /info у відповідь на повідомлення користувача."
        )
        return

    user = message.reply_to_message.from_user

    if user is None:
        await message.answer(
            "Не вдалося визначити користувача."
        )
        return

    username = (
        f"@{user.username}"
        if user.username
        else "не вказан"
    )

    await message.answer(
        "👤 Інформація про користувача\n\n"
        f"🆔 ID: {user.id}\n"
        f"📛 Username: {username}\n"
        "⚠️ Попередження за 30 днів: "
        "дані поки не підключені\n"
        "📋 Історія покарань: "
        "дані поки не підключені"
    )

