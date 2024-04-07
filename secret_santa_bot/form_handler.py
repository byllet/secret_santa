import telebot
from __init__ import bot, users_map
from database.database import add_data
class User:
    def __init__(self, fname):
        self.fname = fname
        self.sname = ''
        self.year = -1
        self.room = -1
        self.present = ''

    def setYear(self, year):
        if year < 0 or year > 6:
            raise Exception('year is incorrect')
        self.year = year

    def setRoom(self, room):
        if room <= 0:
            raise Exception('room is incorrect')
        self.room = room

    def __str(self):
        return f'{self.fname}'

def sendInfo(message, user):
    bot.send_message(message.chat.id,
                     f'Ваши данные:  {user.fname} {user.sname}\n Курс: {user.year}\n Комната: {user.room}\n Подарок: {user.present}')

def processFnameStep(message):
    try:
        user = User(message.text)
        users_map[message.chat.id] = user
        message = bot.reply_to(message, 'Введите вашу фамилию')
        bot.register_next_step_handler(message, processSnameStep)

    except Exception as e:
        bot.reply_to(message, 'something was wrong')

def processSnameStep(message):
    try:
        user = users_map[message.chat.id]
        user.sname = message.text
        message = bot.reply_to(message, 'Укажите ваш курс')
        bot.register_next_step_handler(message, processYearStep)

    except Exception as e:
        bot.reply_to(message, 'something was wrong')

def processYearStep(message):
    try:
        user = users_map[message.chat.id]
        user.setYear(int(message.text))

        message = bot.reply_to(message, 'Укажите вашу комнату')
        bot.register_next_step_handler(message, processRoomStep)
    except Exception as e:
        bot.reply_to(message, 'неверно указан курс')
        message = bot.reply_to(message, 'Укажите ваш курс')
        bot.register_next_step_handler(message, processYearStep)

def processRoomStep(message):
    try:
        user = users_map[message.chat.id]
        user.setRoom(int(message.text))

        message = bot.reply_to(message, 'Какой подарок вы хотите?')
        bot.register_next_step_handler(message, processPresentStep)
    except Exception as e:
        bot.reply_to(message, 'something was wrong')
def processPresentStep(message):
    try:
        user = users_map[message.chat.id]
        user.present = message.text
        sendInfo(message, user)

        add_data(user.fname, user.sname, user.room, user.year, user.present, message.chat.id)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'something was wrong')