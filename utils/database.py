import sqlite3  # Импортируем модуль для работы с SQLite

class Database():
    def __init__(self, db_name):
        # Инициализация базы данных
        self.connection = sqlite3.connect(db_name)  # Подключаемся к базе данных
        self.cursor = self.connection.cursor()  # Создаем объект курсора для выполнения запросов к базе данных
        self.create_db()  # Вызываем метод для создания таблицы, если она не существует

    def create_db(self):
        try:
            # Создаем таблицу users, если она не существует
            query = ("CREATE TABLE IF NOT EXISTS users("
                     "id INTEGER PRIMARY KEY,"
                     "user_name TEXT,"
                     "user_num TEXT,"
                     "telegram_id TEXT);")
            self.cursor.execute(query)  # Выполняем SQL-запрос
            self.connection.commit()  # Фиксируем изменения в базе данных
        except sqlite3.Error as Error:
            print("Ошибка при создании:", Error)

    def add_user(self, user_name, user_num, telegram_id):
        # Добавление нового пользователя в базу данных
        self.cursor.execute("INSERT INTO users (user_name, user_num, telegram_id) VALUES (?, ?, ?)", (user_name, user_num, telegram_id))
        self.connection.commit()  # Фиксируем изменения в базе данных

    def select_user_id(self, telegram_id):
        # Выборка пользователя по telegram_id
        users = self.cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        return users.fetchone()  # Возвращаем первого пользователя, найденного по telegram_id

    def select_user_num(self, telegram_id):
        # Выборка номера подгруппы пользователя по telegram_id
        self.cursor.execute("SELECT user_num FROM users WHERE telegram_id = ?", (telegram_id,))
        result = self.cursor.fetchone()  # Получаем результат выборки
        if result:
            return result[0]  # Возвращаем только первый элемент кортежа, который будет user_num
        else:
            return None  # Если нет результатов, возвращаем None
        
    def get_all_users(self):
        #Метод для получения всех пользователей из базы данных.
        self.cursor.execute("SELECT telegram_id FROM users")
        users = self.cursor.fetchall()
        return [user[0] for user in users]

    def __del__(self):
        # Закрытие соединения с базой данных при удалении объекта
        self.cursor.close()  # Закрываем курсор
        self.connection.close()  # Закрываем соединение с базой данных
