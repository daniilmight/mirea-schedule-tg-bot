from aiogram.types import ReplyKeyboardMarkup  # Импортируем класс ReplyKeyboardMarkup из библиотеки aiogram.types
from aiogram.utils.keyboard import ReplyKeyboardBuilder  # Импортируем класс ReplyKeyboardBuilder из библиотеки aiogram.utils.keyboard

def get_yes_no_kb() -> ReplyKeyboardMarkup:
    # Создаем экземпляр класса ReplyKeyboardBuilder для построения клавиатуры
    kb = ReplyKeyboardBuilder()
    
    # Добавляем кнопки с текстом на клавиатуру
    kb.button(text="Узнать расписание на сегодня")
    kb.button(text="Узнать расписание на завтра")
    kb.button(text="Узнать расписание на неделю")
    kb.button(text="Узнать расписание на следующую неделю")
    
    # Устанавливаем ширину клавиатуры (в данном случае все кнопки будут в одном столбце)
    kb.adjust(1)
    
    # Преобразуем построенную клавиатуру в разметку ReplyKeyboardMarkup
    return kb.as_markup(resize_keyboard=True)
