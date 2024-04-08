from aiogram.fsm.state import StatesGroup, State

# Определение состояний для процесса регистрации
class RegisterState(StatesGroup):
    regName = State()  # Состояние для ввода имени пользователя
    regNum = State()   # Состояние для ввода номера подгруппы
