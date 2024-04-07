import telebot
from __init__ import bot
class User:
    def __init__(self, fname):
        self.fname = fname
        self.sname = ''
        self.year = -1
        self.room = -1
        self.present = ''

users_map = {}

def process_fname_step(message):
    try:
        users_map[message.chat.id] = User(message.text)

        message = bot.reply_to(message, 'Укажите ваше имя')
        bot.register_next_step_handler(message, process_sname_step)
    except Exception as e:
        bot.reply_to(message, 'something was wrong')

def process_sname_step(message):
    try:
        users_map[message.chat.id].sname = message.text

        message = bot.reply_to(message, 'Укажите ваш курс')
        bot.register_next_step_handler(message, process_year_step)
    except Exception as e:
        bot.reply_to(message, 'something was wrong')

def process_year_step(message):
    try:
        user = users_map[message.chat.id]
        user.year = int(message.text)

        message = bot.reply_to(message, 'Укажите вашу комнату')
        bot.register_next_step_handler(message, process_room_step)
    except Exception as e:
        bot.reply_to(message, 'something was wrong')

def process_room_step(message):
    try:
        user = users_map[message.chat.id]
        user.room = int(message.text)

        message = bot.reply_to(message, 'Какой подарок вы хотите?')
        bot.register_next_step_handler(message, process_present_step)
    except Exception as e:
        bot.reply_to(message, 'something was wrong')
def process_present_step(message):
    try:
        user = users_map[message.chat.id]
        user.present = message.text
        bot.send_message(message.chat.id,
                         'Приятно познакомиться, \n' + user.fname + ' ' + user.sname +
                         '\n Курс: ' + str(user.year) +
                         '\n Комната: ' + str(user.room) +
                         '\n Present: ' + user.present)
        print(users_map)
    except Exception as e:
        bot.reply_to(message, 'something was wrong')