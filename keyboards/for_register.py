from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Создание клавиатуры для регистрации
register_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text='Регистрация'
            )
        ]
    ],
    resize_keyboard=True,  # Разрешить автоматическое изменение размера клавиатуры в зависимости от кнопок
    one_time_keyboard=True,  # Одноразовая клавиатура исчезает после выбора пользователем кнопки
    input_field_placeholder='Для продолжения нажмите кнопку ниже'  # Текстовое поле с подсказкой для пользователя
)
