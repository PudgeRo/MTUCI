import telebot
from telebot import types
import sys


token = "2120786897:AAGhuZCewyIIiEZZbGGNYorwa1AevPvIZXA"
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
	sti = open('AnimatedSticker.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)

	startup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	schedule_bfi2102 = types.KeyboardButton("Расписание БФИ2102")
	work_schedule = types.KeyboardButton("График работы")

	startup.add(work_schedule, schedule_bfi2102)

	bot.send_message(message.chat.id, "Привет, {0.first_name}!\nЧто ты хочешь узнать?".format(message.from_user), parse_mode='html', reply_markup=startup)


@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Бот умеет отображать расписание группы БФИ2102 и графики работы ЖКО, профкома МТУСИ\n/start для старта бота\n/help руководство\n/stop остановить бота')


@bot.message_handler(commands=['stop'])
def end_message(message):
	bot.send_message(message.chat.id, 'До встречи!')
	bot.stop_polling()


@bot.message_handler(content_types=['text'])
def answer(message):
	if message.chat.type == 'private':
		if message.text == "Расписание БФИ2102":
			schedule = types.InlineKeyboardMarkup(row_width=3)
			monday = types.InlineKeyboardButton("Понедельник", callback_data='понедельник')
			tuesday = types.InlineKeyboardButton("Вторник", callback_data='вторник')
			wednesday = types.InlineKeyboardButton("Среда", callback_data='среда')
			thursday = types.InlineKeyboardButton("Четверг", callback_data='четверг')
			friday = types.InlineKeyboardButton("Пятница", callback_data='пятница')

			schedule.add(monday, tuesday, wednesday, thursday, friday)

			bot.send_message(message.chat.id, 'Выберите день', reply_markup=schedule)

		elif message.text == "График работы":
			work = types.ReplyKeyboardMarkup(resize_keyboard=True)
			jko = types.KeyboardButton("ЖКО")
			tuc = types.KeyboardButton("ПРОФКОМ")
			back = types.KeyboardButton("НАЗАД")

			work.add(jko, tuc, back)

			bot.send_message(message.chat.id, 'Выберите отдел', reply_markup=work)

		elif message.text == "ПРОФКОМ":
			bot.send_message(message.chat.id, 'Рабочие дни: пн. вт. ср. чт. пт\nЧасы работы: с 11:00 до 16:00\nОбеденный перерыв: с 13:00 до 14:00')

		elif message.text == "ЖКО":
			bot.send_message(message.chat.id, 'Рабочие дни: пн. вт. ср. чт. пт\nЧасы работы: с 11:00 до 17:00\nОбеденный перерыв: с 13:00 до 14:00')
		elif message.text == "НАЗАД":
			start(message)
		else:
			bot.send_message(message.chat.id, 'О чём идет речь?😐')	
	else:
		bot.send_message(message.chat.id, 'Я не понимаю, о чем ты...🤔')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.message:
		if call.data == 'понедельник':
			bot.send_message(call.message.chat.id, '9:30-11:05  - Компьютерная графика (пр.)\n11:20-12:55 - Философия (пр.)')
		elif call.data == 'вторник':
			bot.send_message(call.message.chat.id, '13:10-14:45 - Алгебра и геометрияя (пр.)\n15:25-17:00 - Высшая математика (пр.)\n17:15-18:50 - Вычислительная техника (чёт. пр.)\n                         Социология (нечёт. пр.)')
		elif call.data == 'среда':
			bot.send_message(call.message.chat.id, '9:30-11:05  - Социология (нечёт. лек.)\n11:20-12:55 - Философия (чёт. лек.)\nВведение в ИТ (нечёт. лек.)\n13:10-14:45 - Введение в ИТ (лаб.)\n15:25-17:00 - Физическая культура \n17:15-18:50 - Вычислительная техника (лаб.)')
		elif call.data == 'четверг':
			bot.send_message(call.message.chat.id, '9:30-11:05  - Вычислительная техника (чёт. лек.)\n11:20-12:55 - Алгебра и геометри (чёт. лек.)\n13:10-14:45 - Высшая математика (чёт. лек.)\n15:25-17:00 - Компьютерная графика (чёт. лек.)')
		elif call.data == 'пятница':
			bot.send_message(call.message.chat.id, '9:30-11:05  - Физическая культура \n11:20-12:55 - Ин. яз. (пр.)\n13:10-14:45 - Введение в ИТ (пр.)')
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Расписание на {}".format(call.data),
			reply_markup=None)


bot.polling(none_stop=True)