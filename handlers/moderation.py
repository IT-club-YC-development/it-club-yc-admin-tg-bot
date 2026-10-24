from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message

router = Router(name="moderation_router")

@router.message(Command("warn"))
async def warn_command(message: Message, command: CommandObject) -> None:
    if message.reply_to_message is None:
        await message.answer("Використовувати /warn у відповідь повідомлення користувача.")
        return
    
    user = message.reply_to_message.from_user
    if user is None:
        await message.answer("Користувача не знайдено!")
        return

    username = (f"@{user.username}" if user.username else "Username не вказано")
    args = (f"{command.args}" if command.args else "Причина попередження не вказано.")

    await message.answer(
        f"Попередження користувачу {user.first_name}\n"
        f"Причина: {args}\n"
        f"Username: {username}"
    )

@router.message(Command("mute"))
async def mute_command(message: Message, command: CommandObject) -> None:
    pass

@router.message(Command("ban"))
async def ban_command(message: Message, command: CommandObject) -> None:
    pass

@router.message(Command("unban"))
async def unban_command(message: Message, command: CommandObject) -> None:
    pass




