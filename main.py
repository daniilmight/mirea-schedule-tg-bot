import asyncio
from aiogram import Bot, Dispatcher, F
from handlers import questions, different_types  # Импортируем модули с обработчиками команд
from handlers.register import start_register, register_name, register_num
from state.register import RegisterState
from utils.commands import set_commands  # Импортируем функцию для установки команд
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('BOT_TOKEN')

# Основная функция, запускающая бота
async def main():
    # Создаем объект бота, используя токен из конфигурации
    bot = Bot(token=token)
    dp = Dispatcher()  # Создаем диспетчер для обработки сообщений

    await set_commands(bot)  # Устанавливаем команды бота
    dp.message.register(start_register, F.text == 'Регистрация')
    dp.message.register(register_name, RegisterState.regName)
    dp.message.register(register_num, RegisterState.regNum)

    dp.include_routers(questions.router, different_types.router)  # Подключаем обработчики команд

    # Удаляем вебхук и ожидающие обновления перед запуском
    await bot.delete_webhook(drop_pending_updates=True)
    
    # Запускаем бота
    await dp.start_polling(bot)


if __name__ == "__main__":
    # Запускаем основную функцию в асинхронном режиме
    asyncio.run(main())
