import datetime
import psycopg2
import telebot
from telebot import types

token = "2120786897:AAGhuZCewyIIiEZZbGGNYorwa1AevPvIZXA"
bot = telebot.TeleBot(token)
date = datetime.date.today().isocalendar()[1]

conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="1234",
                        host="localhost",
                        port="5432")

cursor = conn.cursor()


def database_message(database, message):
    cursor.execute(
                "SELECT subject, room_numb, start_time FROM {} WHERE day='{}'".format(database, message))
    return cursor.fetchall()


def layout(table):
    display = []
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    for day in days:
            result = database_message(table, day)
            display.append(day + '\n' + '_________\n')
            for i in result:
                display.append(' | '.join(i) + '\n')
    return display



@bot.message_handler(commands=['start'])
def start(message):
    sti = open('AnimatedSticker.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)

    schedule = types.ReplyKeyboardMarkup(resize_keyboard=True)
    monday = types.KeyboardButton("Понедельник")
    tuesday = types.KeyboardButton("Вторник")
    wednesday = types.KeyboardButton("Среда")
    thursday = types.KeyboardButton("Четверг")
    friday = types.KeyboardButton("Пятница")
    next_week = types.KeyboardButton("Следующая неделя")
    nowadays = types.KeyboardButton("Эта неделя")
    schedule.add(monday, tuesday, wednesday, thursday, friday, next_week, nowadays)

    bot.send_message(message.chat.id, "Здравствуй, {0.first_name}!\nТут ты можешь узнать расписание БФИ2102".format(message.from_user), parse_mode='html', reply_markup=schedule)



@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот умеет отображать расписание группы БФИ2102\n'
                                      'Все команды:\n'
                                      '/start для старта бота\n'
                                      '/help руководство\n'
                                      '/stop остановить бота\n'
                                      '/mtuci ссылка на официальный сайт МТУСИ\n'
                                      '/week узнать текущую неделю')


@bot.message_handler(commands=['stop'])
def end_message(message):
    bot.send_message(message.chat.id, 'До встречи!')
    bot.stop_polling()


@bot.message_handler(commands=['mtuci'])
def mtuci(message):
    bot.send_message(message.chat.id, 'Официальный сайт МТУСИ: https://mtuci.ru/')



@bot.message_handler(commands=['week'])
def week(message):
    if date % 2 == 0:
        bot.send_message(message.chat.id, 'Сейчас нижняя неделя')
    if date % 2 == 1:
        bot.send_message(message.chat.id, 'Сейчас верхняя неделя')


@bot.message_handler(content_types=['text'])
def answer_timetable(message):
    week = datetime.date.today().isocalendar()[1] % 2
    table = 'timetable_odd' if week else 'timetable_even'
    response = message.text

    if response == "Понедельник" or response == "Вторник" or response == "Среда" or response == "Четверг" or response == "Пятница":
        try:
            result = database_message(table, response)
            display = []
            for i in result:
                display.append(' | '.join(i) + '\n')

            bot.send_message(message.chat.id, ''.join(display))
        except:
            bot.send_message(message.chat.id, 'Пар нет')

    elif response == 'Эта неделя':
        bot.send_message(message.chat.id, ''.join(layout(table)))

    elif response == 'Следующая неделя':
        table = 'timetable_odd' if table == 'timetable_even' else 'timetable_even'     
        bot.send_message(message.chat.id, ''.join(layout(table)))

    else:
        bot.send_message(message.chat.id, 'Извините, Я Вас не понял.')


bot.polling(none_stop=True)