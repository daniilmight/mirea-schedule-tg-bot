from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

async def set_commands(bot: Bot):
    # Создаем список команд для установки
    commands = [
        BotCommand(
            command='start',  # Команда '/start'
            description='Запуск бота'  # Описание команды
        ),
        BotCommand(
            command='reregister',  # Команда '/reregister'
            description='Изменить данные для аккаунта'  # Описание команды
        )
    ]

    # Устанавливаем команды бота с указанием области видимости по умолчанию
    await bot.set_my_commands(commands, BotCommandScopeDefault())
