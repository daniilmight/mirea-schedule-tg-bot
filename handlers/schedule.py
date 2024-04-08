from datetime import datetime, timedelta

start_date = datetime(2024, 2, 9)

day_names = {
    'Monday': '<u>ПОНЕДЕЛЬНИК</u>',
    'Tuesday': '<u>ВТОРНИК</u>',
    'Wednesday': '<u>СРЕДА</u>',
    'Thursday': '<u>ЧЕТВЕРГ</u>',
    'Friday': '<u>ПЯТНИЦА</u>',
    'Saturday': '<u>СУББОТА</u>',
    'Sunday': '<u>ВОСКРЕСЕНЬЕ</u>'
}

# Функция для определения четности и номера недели
def get_week_parity_and_number(start_date, target_date):
    # Рассчитываем количество дней от начальной даты до целевой даты
    days_from_start = (target_date - start_date).days
    
    # Определяем день недели начальной даты
    start_weekday = start_date.weekday()
    
    # Вычисляем номер недели
    week_number = (days_from_start + start_weekday) // 7

    # Первая неделя всегда нечетная, даже если начало в середине недели
    week_parity = "нечетная" if (week_number % 2) == 0 else "четная"

    return week_parity, week_number + 1

def get_schedule_first_group(day_of_week, week_parity, week_number):
    if week_parity == "нечетная":
        schedule = {
            'Monday': {
                1: " - " if week_number in [1, 5, 9, 13, 17] else "Философия (ПР) ауд. А-234",
                2: " - " if week_number in [1, 5, 9, 13, 17] else "Философия (ПР) ауд. А-234",
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Tuesday': {
                1: 'Физические основы получения информации (ЛАБ) ауд. 188.2' if week_number in [5, 9, 13, 17] else " - ",
                2: 'Физические основы получения информации (ЛАБ) ауд. 188.2' if week_number in [5, 9, 13, 17] else " - ",
                3: ' - ' if week_number in [1, 3, 9, 13, 17] else 'Методы и средства цифровой обработки сигналов (ЛАБ) ауд. 112',
                4: ' - ' if week_number in [1, 3, 9, 13, 17] else 'Методы и средства цифровой обработки сигналов (ЛАБ) ауд. 112',
                5: ' - ',
                6: ' - '
            },
            'Wednesday': {
                1: 'Физические основы получения информации (ЛК) ауд. 110',
                2: ' - ',
                3: 'Теория вероятности и математическая статистика (ЛК) ауд. 326',
                4: 'Физическая культура и спорт (ПР)',
                5: ' - ',
                6: ' - '
            },
            'Thursday': {
                1: 'Методы и средства цифровой обработки сигналов (ЛК) ауд. 110',
                2: 'Методы и средства цифровой обработки сигналов (ПР) ауд. 188.1',
                3: ' - ',
                4: 'Методы и средства цифровой обработки сигналов (ПР) ауд. 188.1',
                5: 'Теория вероятности и математическая статистика (ПР) ауд. 415',
                6: ' - '
            },
            'Friday': {
                1: 'Физические основы получения информации (ЛК) ауд. 110',
                2: ' - ' if week_number == 17 else 'Физические основы получения информации (ПР) ауд. 188.3',
                3: 'Практика решения инженерных задач в приборостроении (ПР) ауд. 111',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Saturday': {
                1: ' - ',
                2: ' - ',
                3: 'Иностранный язык (ПР) ауд. И-320',
                4: 'Иностранный язык (ПР) ауд. И-320',
                5: ' - ',
                6: ' - '
            },
            'Sunday': {
                1: 'Выходной'
            }
        }
    else:
        schedule = {
            'Monday': {
                1: " - " if week_number in [4, 8, 12, 16] else 'Философия (ЛК) ауд. А-234',
                2: " - " if week_number in [4, 8, 12, 16] else 'Философия (ЛК) ауд. А-234',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Tuesday': {
                1: "Цифровые измерительные приборы (ЛАБ) ауд. 188.3" if week_number in [10, 14] else ' - ',
                2: "Цифровые измерительные приборы (ЛАБ) ауд. 188.3" if week_number in [10, 14] else ' - ',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Wednesday': {
                1: " - " if week_number == 17 else 'Цифровые измерительные приборы (ПР) ауд. 110',
                2: 'Цифровые измерительные приборы (ЛК) ауд. 188.3',
                3: 'Большие данные (ЛК) ауд. 330',
                4: 'Физическая культура и спорт (ПР)',
                5: ' - ',
                6: ' - '
            },
            'Thursday': {
                1: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ЛК) ауд. 110',
                2: '-',
                3: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ПР) ауд. 111',
                4: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ПР) ауд. 111',
                5: 'Теория вероятности и математическая статистика (ПР) ауд. 415',
                6: ' - '
            },
            'Friday': {
                1: 'Большие данные (ПР) ауд. 246',
                2: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111" if week_number in [4, 8, 12, 16] else ' - ',
                3: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111" if week_number in [4, 8, 12, 16] else ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Saturday': {
                1: ' - ',
                2: 'Практика решения инженерных задач в приборостроении (ЛК) ауд. 110',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Sunday': {
                1: 'Выходной'
            }
        }

    schedule_for_day = schedule[day_of_week]
    
    # Формирование текста расписания
    schedule_text = f'{day_names[day_of_week]} \nНеделя - {week_parity}, номер недели - {week_number}:'
    for lesson_number, lesson_description in schedule_for_day.items():
        schedule_text += f'\n{lesson_number}. {lesson_description}'

    return schedule_text

def get_schedule_second_group(day_of_week, week_parity, week_number):
    if week_parity == "нечетная":
        schedule = {
            'Monday': {
                1: " - " if week_number in [1, 5, 9, 13, 17] else "Философия (ПР) ауд. А-234",
                2: " - " if week_number in [1, 5, 9, 13, 17] else "Философия (ПР) ауд. А-234",
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Tuesday': {
                1: ' - ' if week_number in [1, 3, 9, 13, 17] else 'Методы и средства цифровой обработки сигналов (ЛАБ) ауд. 112',
                2: ' - ' if week_number in [1, 3, 9, 13, 17] else 'Методы и средства цифровой обработки сигналов (ЛАБ) ауд. 112',
                3: 'Физические основы получения информации (ЛАБ) ауд. 188.2' if week_number in [5, 9, 13, 17] else " - ",
                4: 'Физические основы получения информации (ЛАБ) ауд. 188.2' if week_number in [5, 9, 13, 17] else " - ",
                5: ' - ',
                6: ' - '
            },
            'Wednesday': {
                1: 'Физические основы получения информации (ЛК) ауд. 110',
                2: 'Физические основы получения информации (ПР) ауд. 188.2',
                3: 'Теория вероятности и математическая статистика (ЛК) ауд. 326',
                4: 'Физическая культура и спорт (ПР)',
                5: ' - ',
                6: ' - '
            },
            'Thursday': {
                1: 'Методы и средства цифровой обработки сигналов (ЛК) ауд. 110',
                2: ' - ',
                3: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ПР) ауд. 111',
                4: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ПР) ауд. 111',
                5: 'Теория вероятности и математическая статистика (ПР) ауд. 415',
                6: ' - '
            },
            'Friday': {
                1: 'Физические основы получения информации (ЛК) ауд. 110',
                2: ' - ',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Saturday': {
                1: ' - ',
                2: ' - ',
                3: 'Иностранный язык (ПР) ауд. И-320',
                4: 'Иностранный язык (ПР) ауд. И-320',
                5: ' - ',
                6: ' - '
            },
            'Sunday': {
                1: 'Выходной'
            }
        }
    else:
        schedule = {
            'Monday': {
                1: " - " if week_number in [4, 8, 12, 16] else 'Философия (ЛК) ауд. А-234',
                2: " - " if week_number in [4, 8, 12, 16] else 'Философия (ЛК) ауд. А-234',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Tuesday': {
                1: "Цифровые измерительные приборы (ЛАБ) ауд. 188.3" if week_number in [12, 16] else ' - ',
                2: "Цифровые измерительные приборы (ЛАБ) ауд. 188.3" if week_number in [12, 16] else ' - ',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Wednesday': {
                1: " - ",
                2: 'Цифровые измерительные приборы (ЛК) ауд. 188.3',
                3: 'Большие данные (ЛК) ауд. 330',
                4: 'Физическая культура и спорт (ПР)',
                5: ' - ',
                6: ' - '
            },
            'Thursday': {
                1: 'Компьютерные средства трёхмерного моделирования и конструирования приборов и систем (ЛК) ауд. 110',
                2: 'Методы и средства цифровой обработки сигналов (ПР) ауд. 188.1',
                3: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111",
                4: 'Методы и средства цифровой обработки сигналов (ПР) ауд. 188.1',
                5: 'Теория вероятности и математическая статистика (ПР) ауд. 415',
                6: ' - '
            },
            'Friday': {
                1: 'Большие данные (ПР) ауд. 246',
                2: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111" if week_number in [2, 6, 10, 14] else ' - ',
                3: "Практика решения инженерных задач в приборостроении (ПР) ауд. 111" if week_number in [2, 6, 10, 14] else ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Saturday': {
                1: 'Цифровые измерительные приборы (ПР) ауд. 110',
                2: 'Практика решения инженерных задач в приборостроении (ЛК) ауд. 110',
                3: ' - ',
                4: ' - ',
                5: ' - ',
                6: ' - '
            },
            'Sunday': {
                1: 'Выходной'
            }
        }

    schedule_for_day = schedule[day_of_week]
    
    # Формирование текста расписания
    schedule_text = f'{day_names[day_of_week]} \nНеделя - {week_parity}, номер недели - {week_number}:'
    for lesson_number, lesson_description in schedule_for_day.items():
        schedule_text += f'\n{lesson_number}. {lesson_description}'

    return schedule_text