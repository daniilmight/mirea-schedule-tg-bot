# Проект Telegram бота для отправки расписания

Этот проект представляет собой Telegram бота, который предоставляет расписание для студентов группы БПБО-02-22. Бот также позволяет студентам зарегистрироваться и получать персонализированное расписание.

## Установка и запуск

Для запуска бота, требуются следующие библиотеки:
```
pip install aiogram python-dotenv
```
Также необходимо в файле конфигурации `.env` заменить значения всех переменных на свои.

## Возможности бота:

1. **Получение расписания**:
Бот предоставляет возможность получить расписание на сегодня, завтра, на текущую неделю или на следующую неделю.

2. **Регистрация**:
Студенты могут зарегистрироваться в боте, указав своё ФИО и номер подгруппы.

3. **Персонализированное расписание**:
После регистрации студенты получают персонализированное расписание согласно их группе и номеру подгруппы.

4. **Рассылка сообщений**:
Администратор бота может отправлять сообщения всем зарегистрированным пользователям.

5. **Клавиатуры**:
Бот использует клавиатуры для удобного взаимодействия с пользователем, например, для выбора действий или ввода информации.


## Как использовать:

1. Запустите бота
2. Пользователи могут взаимодействовать с ботом, запрашивая расписание и выполняя другие действия.
3. Администратор может отправлять сообщения всем пользователям с помощью команды `/imessage <сообщение>`.

## Используемые технологии

- Python
- aiogram - фреймворк для создания Telegram ботов
- pydantic - для работы с настройками и секретами
- sqlite3 - для работы с базой данных SQLite

## Файлы и структура проекта

- `main.py`: основной файл, содержащий запуск бота.
- `handlers/`: обработчики сообщений и команд бота.
- `utils/`: директория с вспомогательными функциями и классами.
- `state/`: директория с состояниями для FSM (finite state machine).
- `keyboards/`: директория с клавиатурами для бота.
