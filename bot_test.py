import telebot
import sqlite3
import psycopg2


connection = psycopg2.connect(
    host = "127.0.0.1",
    user = "postgres",
    password = "xkleeps123",
    database = "postgres"
)
connection.autocommit = True

bot = telebot.TeleBot('6341306871:AAGa2N1ZUQSZT6pbir9TMQ367lJN158QAUk')

name = None
total_seats = 100  # Общее количество мест в концертном зале

@bot.message_handler(commands = ['start'])
def main(message):
    bot.send_message(message.chat.id,'Добро пожаловать в бота для покупки билетов в театре /help для большей ниформации')

@bot.message_handler(commands = ['help'])
def help(message):
    bot.send_message(message.chat.id,'Узнать основную информация (Название спектакля, Дата и время спектакля) /info')

@bot.message_handler(commands = ['info'])
def info(message):
    # bot.send_message(message.chat.id,'Выберите концерт')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM cinema;")
    data = cursor.fetchall()
    response = "Выберите номер концерта\n"
    for row in data:
            response += f"\n Концерт №: {row[0]}\n Название: {row[1]}\n Дата: {row[2]}\n Время: {row[3]}\n Описание: {row[4]}\n"
    bot.reply_to(message, response)
    bot.send_message(message.chat.id,f"Для бронирования место введите /buy\nПосмотреть свободные места /mesto")



@bot.message_handler(commands=['buy'])
def enter_concert_number(message):
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(id) FROM cinema;")
    max_concert_number = cursor.fetchone()[0]
    cursor.close()
    bot.send_message(message.chat.id, f'Введите номер концерта для бронирования места (от 1 до {max_concert_number})')
    bot.register_next_step_handler(message, enter_name)


def enter_name(message):
    user_concert_number = int(message.text)
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(id) FROM cinema;")
    max_concert_number = cursor.fetchone()[0]
    cursor.close()

    if user_concert_number > max_concert_number:
        bot.send_message(message.chat.id, f'Введенное число превышает максимальный номер концерта. Пожалуйста, введите номер концерта для бронирования места (от 1 до {max_concert_number})')
        bot.register_next_step_handler(message, enter_name)
    else:
        try:
            concert_number = int(message.text)
            bot.send_message(message.chat.id, 'Введите свое имя')
            bot.register_next_step_handler(message, reserve_seat, concert_number)
        except ValueError:
            bot.send_message(message.chat.id, 'Пожалуйста, введите корректный номер концерта (целое число)')


def reserve_seat(message, concert_number):
    try:
        name = message.text
        # bot.send_photo(message.chat.id, open('mests.jpg', 'rb'))
        bot.send_message(message.chat.id, 'Введите ряд и место через пробел (например, "3 5")')
        bot.register_next_step_handler(message, process_reservation, concert_number, name)
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректное имя')


def process_reservation(message, concert_number, name):
    try:
        row, seat = map(int, message.text.split())
        
        # Проверка находятся ли значения row и seat в диапазоне от 1 до 10
        if (row < 1 or row > 10) or (seat < 1 or seat > 10):
            bot.send_message(message.chat.id, 'Пожалуйста, выберите места в допустимом диапазоне от 1 до 10.')
            bot.register_next_step_handler(message, process_reservation, concert_number, name)
            return

        cursor = connection.cursor()

        while True:
            # Проверяем наличие уже существующего бронирования с такими же значениями concert_number, row и seat
            cursor.execute(
                "SELECT * FROM user_data WHERE cinemas = %s AND place = %s AND row = %s", (concert_number, row, seat))
            existing_reservation = cursor.fetchone()

            if existing_reservation:
                bot.send_message(message.chat.id, 'Место занято. Пожалуйста, выберите другое место.')
                # Выводим картинку перед запросом новых данных
                bot.send_message(message.chat.id, 'Введите другие данные для ряда и места (два целых числа через пробел)')
                bot.register_next_step_handler(message, process_reservation, concert_number, name)
                return
                
            else:
                # Получить последний вставленный ID из таблицы user_data
                cursor.execute("SELECT MAX(name_id) FROM user_data")
                last_name_id = cursor.fetchone()[0]

                if last_name_id:
                    name_id = last_name_id + 1  # Увеличить последний name_id на 1
                else:
                    name_id = 1  # Если таблица пуста, установить name_id равным 1

                cursor.execute("INSERT INTO user_data (name_id, cinemas, name, place, row) VALUES (%s, %s, %s, %s, %s)",
                               (name_id, concert_number, name, row, seat))
                connection.commit()
                cursor.close()

                bot.send_message(message.chat.id, f'Место {row}, {seat} на концерте № {concert_number} успешно забронировано!')
                break
    except ValueError:
        bot.send_message(message.chat.id, 'Пожалуйста, введите корректные данные для ряда и места (два целых числа через пробел)')

@bot.message_handler(commands=['mesto'])
def show_available_seats(message):
    cursor = connection.cursor()
    cursor.execute("SELECT MAX(id) FROM cinema;")
    max_concert_number = cursor.fetchone()[0]
    cursor.close()
    bot.send_message(message.chat.id, f'Введите номер концерта (от 1 до {max_concert_number})')
    # bot.send_message(
    #     message.chat.id,
    #     'Введите номер концерта для просмотра свободных мест (от 1 до максимального номера концерта)'
    # )
    bot.register_next_step_handler(message, display_seats_info)

def display_seats_info(message):
    try:
        concert_number = int(message.text)
        cursor = connection.cursor()
        cursor.execute(
            "SELECT place, row FROM user_data WHERE cinemas = %s", 
            (concert_number,)
        )
        reserved_seats = cursor.fetchall()
        cursor.close()

        # Создаем словарь, где ключ - ряд, значение - список мест в этом ряду
        seats_dict = {}
        for row in range(1, 11):
            seats_dict[row] = [''] * 10

        # Заполняем словарь посещенными местами
        for seat in reserved_seats:
            row, place = seat
            seats_dict[row][place - 1] = 'X'  # Помечаем занятые места 'X'

        # Формируем строку со свободными и занятыми местами в виде матрицы
        seats_matrix_str = '```\n      1 2 3 4  5 6 7  8 9 10\n'
        for row, seats in seats_dict.items():
            seats_matrix_str += f'{row:>2} | '
            for seat in seats:
                if seat == '':
                    seats_matrix_str += '⬜️'  # Свободные места
                else:
                    seats_matrix_str += '🔴'  # Занятые места
            seats_matrix_str = seats_matrix_str.strip() + f' | {row}\n'
        seats_matrix_str += '```'

        response = f'Состояние мест на концерте №{concert_number}:\n{seats_matrix_str}'
        
        bot.send_message(message.chat.id, response, parse_mode='Markdown')
    except ValueError:
        bot.send_message(
            message.chat.id, 
            'Пожалуйста, введите корректный номер концерта (целое число)'
        )

bot.polling(non_stop=True)