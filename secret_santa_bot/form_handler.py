from __init__ import bot, users_map
from database.database import add_data
from User import sendInfo, User


def processFnameStep(message):
    try:
        user = User(message.text)
        users_map[message.chat.id] = user
        message = bot.reply_to(message, 'Введите вашу фамилию')
        bot.register_next_step_handler(message, processSnameStep)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'something was wrong')


def processSnameStep(message):
    try:
        user = users_map[message.chat.id]
        user.sname = message.text
        message = bot.reply_to(message, 'Укажите ваш курс')
        bot.register_next_step_handler(message, processYearStep)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'something was wrong')


def processYearStep(message):
    try:
        user = users_map[message.chat.id]
        user.setYear(int(message.text))

        message = bot.reply_to(message, 'Укажите вашу комнату')
        bot.register_next_step_handler(message, processRoomStep)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'Неверно указан курс')
        message = bot.reply_to(message, 'Укажите ваш курс')
        bot.register_next_step_handler(message, processYearStep)


def processRoomStep(message):
    try:
        user = users_map[message.chat.id]
        user.setRoom(int(message.text))

        message = bot.reply_to(message, 'Какой подарок вы хотите?')
        bot.register_next_step_handler(message, processPresentStep)
    except Exception as e:
        print(e)
        bot.reply_to(message, 'something was wrong')


def processPresentStep(message):
    try:
        user = users_map[message.chat.id]
        user.present = message.text
        sendInfo(message.chat.id, user)

        add_data(user.fname, user.sname, user.room, user.year, user.present, message.chat.id)

    except Exception as e:
        print(e)
        bot.reply_to(message, 'something was wrong')
