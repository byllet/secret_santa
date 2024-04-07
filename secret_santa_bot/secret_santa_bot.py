from __init__ import bot
import telebot
from form_handler import process_fname_step

time = '01.02.4002'

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    create = telebot.types.KeyboardButton('/create')
    info_button = telebot.types.KeyboardButton('/info')
    markup.add(create)
    markup.add(info_button)
    bot.send_message(message.chat.id, 'Это тайный санта\n'
                                      f'Время события {time}\n' 
                                      'Для просмотра информации напишите /info',
                                                                                reply_markup=markup)

@bot.message_handler(commands=['create'])
def create_do(message):
    message = bot.reply_to(message, 'Ваша фамилия')
    bot.register_next_step_handler(message, process_fname_step)

@bot.message_handler(commands=['info'])
def info_send(message):
    bot.send_message(message.chat.id, 'ho-ho')

@bot.message_handler(content_types=["text"])
def variable_message(message):
    bot.send_message(message.chat.id, "Введите /start для начала")

if __name__ == "__main__":
    bot.infinity_polling()
