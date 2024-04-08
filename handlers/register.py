from aiogram import Bot  # Импортируем класс Bot из библиотеки aiogram
from aiogram.types import Message, ReplyKeyboardRemove  # Импортируем типы данных Message и ReplyKeyboardRemove из библиотеки aiogram.types
from aiogram.fsm.context import FSMContext  # Импортируем контекст конечного автомата из библиотеки aiogram.fsm.context
from keyboards.for_questions import get_yes_no_kb  # Импортируем клавиатуру для вопросов
from state.register import RegisterState  # Импортируем состояние регистрации
import os  # Импортируем модуль os для работы с операционной системой
from utils.database import Database  # Импортируем класс Database для работы с базой данных

async def start_register(message: Message, state: FSMContext, bot: Bot):
    # Инициализируем подключение к базе данных
    db = Database(os.getenv('DATABASE_NAME'))
    users = db.select_user_id(message.from_user.id)  # Получаем информацию о пользователе из базы данных
    if (users):  # Если пользователь уже зарегистрирован
        await bot.send_message(message.from_user.id, f'{users[1]} \nВы уже зарегистрированы',
                               reply_markup=ReplyKeyboardRemove())  # Отправляем сообщение о том, что пользователь уже зарегистрирован
    else:  # Если пользователь не зарегистрирован
        await bot.send_message(message.from_user.id, 'Напишите своё ФИО')  # Просим пользователя ввести ФИО
        await state.set_state(RegisterState.regName)  # Устанавливаем состояние FSM для ожидания ФИО пользователя

async def register_name(message: Message, state: FSMContext, bot: Bot):
    await bot.send_message(message.from_user.id, 'Отлично, теперь введите номер вашей подгруппы')  # Просим пользователя ввести номер подгруппы

    await state.update_data(regname=message.text)  # Обновляем данные состояния, сохраняя введенное ФИО
    await state.set_state(RegisterState.regNum)  # Устанавливаем состояние FSM для ожидания номера подгруппы

async def register_num(message: Message, state: FSMContext, bot: Bot):
    reg_num = message.text.strip()  # Убираем лишние пробелы
    if reg_num not in ('1', '2'):  # Проверяем корректность введенного номера подгруппы
        await bot.send_message(message.from_user.id,
                               "Номер подгруппы должен быть равен 1 или 2. Пожалуйста, введите номер еще раз.")
        return  # Завершаем выполнение функции, чтобы ожидать нового ввода от пользователя

    # Если номер подгруппы корректный, продолжаем регистрацию
    await state.update_data(regnum=reg_num)  # Обновляем данные состояния, сохраняя введенный номер подгруппы
    reg_data = await state.get_data()
    reg_name = reg_data.get('regname')  # Получаем сохраненное ФИО пользователя

    msg = f'Регистрация успешно пройдена!'  # Сообщение об успешной регистрации
    await bot.send_message(message.from_user.id, msg, reply_markup=get_yes_no_kb())  # Отправляем пользователю сообщение о успешной регистрации и клавиатуру для ответа на вопросы

    db = Database(os.getenv('DATABASE_NAME'))  # Инициализируем подключение к базе данных
    db.add_user(reg_name, reg_num, message.from_user.id)  # Добавляем пользователя в базу данных

    await state.clear()  # Очищаем состояние FSM, завершая процесс регистрации
