from aiogram import Bot, Router, F  # Импортируем классы Bot, Router и F из библиотеки aiogram
from aiogram.filters import Command  # Импортируем фильтр Command из библиотеки aiogram.filters
from aiogram.types import Message  # Импортируем тип данных Message из библиотеки aiogram.types
from aiogram.enums import ParseMode

from keyboards.for_questions import get_yes_no_kb  # Импортируем клавиатуру для вопросов
from keyboards.for_register import register_keyboard  # Импортируем клавиатуру для регистрации

from utils.database import Database  # Импортируем класс Database для работы с базой данных
import os  # Импортируем модуль os для работы с операционной системой

from datetime import datetime, timedelta  # Импортируем классы datetime и timedelta для работы с датой и временем
from handlers.schedule import start_date, get_week_parity_and_number, get_schedule_first_group, get_schedule_second_group, day_names  # Импортируем функции для работы с расписанием

router = Router()  # Создаем экземпляр класса Router для обработки сообщений

@router.message(Command("start"))  # Декоратор для обработки команды /start
async def cmd_start(message: Message, bot: Bot):  # Обработчик команды /start
    db = Database(os.getenv('DATABASE_NAME'))  # Инициализируем подключение к базе данных
    users = db.select_user_id(message.from_user.id)  # Получаем информацию о пользователе из базы данных
    if (users):  # Если пользователь уже зарегистрирован
        await bot.send_message(message.from_user.id,
        f"Привет, {users[1]}!",
        reply_markup=get_yes_no_kb())  # Отправляем приветственное сообщение с клавиатурой для ответа на вопрос
    else:  # Если пользователь не зарегистрирован
        await bot.send_message(message.from_user.id,
            "Это бот для группы БПБО-02-22, отправляющий расписание и, возможно, что-то ещё",
            reply_markup=register_keyboard  # Отправляем сообщение о незарегистрированном пользователе с клавиатурой для регистрации
        )

@router.message(F.text.lower() == "узнать расписание на сегодня")  # Декоратор для обработки текста "узнать расписание на сегодня"
async def today_schedule(message: Message, bot: Bot):  # Обработчик запроса на получение расписания на сегодня
    msktime =  datetime.now() + timedelta(hours=3)  # Получаем текущее время в Московском часовом поясе
    day_of_week = msktime.strftime('%A')  # Определяем текущий день недели

    # Определение четности и номера недели
    week_parity, week_number = get_week_parity_and_number(start_date, msktime)

    # Формирование расписания на текущий день с выбором подгруппы
    db = Database(os.getenv('DATABASE_NAME'))  # Инициализируем подключение к базе данных
    num = int(db.select_user_num(message.from_user.id))  # Получаем номер подгруппы пользователя из базы данных
    if num == 1:  # Если пользователь принадлежит к первой подгруппе
        schedule_text = get_schedule_first_group(day_of_week, week_parity, week_number)  # Получаем расписание для первой подгруппы
    elif num == 2:  # Если пользователь принадлежит ко второй подгруппе
        schedule_text = get_schedule_second_group(day_of_week, week_parity, week_number)  # Получаем расписание для второй подгруппы

    await bot.send_message(message.from_user.id, schedule_text, parse_mode=ParseMode.HTML)  # Отправляем пользователю расписание на сегодня

# Аналогичные обработчики для остальных команд ("узнать расписание на завтра", "узнать расписание на неделю", "узнать расписание на следущую неделю")...

@router.message(F.text.lower() == "узнать расписание на завтра")
async def tomorow_schedule(message: Message, bot: Bot):
    msktime =  datetime.now() + timedelta(days=1) + timedelta(hours=3)
    day_of_week = msktime.strftime('%A')

    # Определение четности и номера недели
    week_parity, week_number = get_week_parity_and_number(start_date, msktime)

    # Формирование расписания на текущий день с выбором подгруппы
    db = Database(os.getenv('DATABASE_NAME'))
    num = int(db.select_user_num(message.from_user.id))
    if(num==1):
        schedule_text = get_schedule_first_group(day_of_week, week_parity, week_number)
    elif(num==2):
        schedule_text = get_schedule_second_group(day_of_week, week_parity, week_number)

    await bot.send_message(message.from_user.id,schedule_text, parse_mode=ParseMode.HTML)

@router.message(F.text.lower() == "узнать расписание на неделю")
async def week_schedule(message: Message, bot: Bot):
    msktime =  datetime.now() + timedelta(hours=3)
    day_of_week = msktime.strftime('%A')

    # Определение четности и номера недели
    week_parity, week_number = get_week_parity_and_number(start_date, msktime)

    db = Database(os.getenv('DATABASE_NAME'))
    num = int(db.select_user_num(message.from_user.id))

    # Формирование расписания на всю неделю
    week_schedule_text = ''
    if(num==1):
        for day_of_week in day_names.keys():
            schedule_text = get_schedule_first_group(day_of_week, week_parity, week_number)
            week_schedule_text += f'\n\n{schedule_text}'
    elif(num==2):
        for day_of_week in day_names.keys():
            schedule_text = get_schedule_second_group(day_of_week, week_parity, week_number)
            week_schedule_text += f'\n\n{schedule_text}'

    await bot.send_message(message.from_user.id,week_schedule_text, parse_mode=ParseMode.HTML)

@router.message(F.text.lower() == "узнать расписание на следущую неделю")
async def week_schedule(message: Message, bot: Bot):
    msktime =  datetime.now() + timedelta(days=7) + timedelta(hours=3)
    day_of_week = msktime.strftime('%A')

    # Определение четности и номера недели
    week_parity, week_number = get_week_parity_and_number(start_date, msktime)

    db = Database(os.getenv('DATABASE_NAME'))
    num = int(db.select_user_num(message.from_user.id))

    # Формирование расписания на всю неделю
    week_schedule_text = ''
    if(num==1):
        for day_of_week in day_names.keys():
            schedule_text = get_schedule_first_group(day_of_week, week_parity, week_number)
            week_schedule_text += f'\n\n{schedule_text}'
    elif(num==2):
        for day_of_week in day_names.keys():
            schedule_text = get_schedule_second_group(day_of_week, week_parity, week_number)
            week_schedule_text += f'\n\n{schedule_text}'

    await bot.send_message(message.from_user.id,week_schedule_text, parse_mode=ParseMode.HTML)

@router.message(Command("imessage"))
async def broadcast_message(message: Message, command: Command, bot: Bot):
    admin = os.getenv('ADMIN_ID')
    if int(admin) == int(message.from_user.id):
        # Подключение к базе данных
        db = Database(os.getenv('DATABASE_NAME'))
        # Получение всех пользователей из базы данных
        all_users = db.get_all_users()
        # Отправка сообщения каждому пользователю
        for user_id in all_users:
            if command.args is None:
                await message.answer(
                    "Ошибка: не переданы аргументы"
                )
            else:
                await bot.send_message(user_id, (message.text[(message.text.find(' ')+1)::]))
    else:
        await bot.send_message(message.from_user.id, f"У вас нет прав использовать эту команду")