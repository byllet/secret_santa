import telebot
from __init__ import bot
from form_handler import processFnameStep
from User import sendInfo, User
from database.database import get_user_by_chat_id

time = '01.02.4002'

admins = [702426433]

def get_from_DB(chat_id):
    raw_data = get_user_by_chat_id(chat_id)
    if (len(raw_data) == 0):
        return False

    raw_data = raw_data[0]
    user = User('')
    user.fname = raw_data[1]
    user.sname = raw_data[2]
    user.setRoom(raw_data[3])
    user.setYear(raw_data[4])
    user.present = raw_data[5]
    return user

@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    create_button = telebot.types.KeyboardButton('/create')
    view_button = telebot.types.KeyboardButton('/view')
    info_button = telebot.types.KeyboardButton('/info')
    markup.add(create_button)
    markup.add(view_button)
    markup.add(info_button)
    bot.send_message(message.chat.id, f'Это тайный санта\n\
                                      Время события {time}\n\
                                      Для просмотра информации напишите /info',
                                                                                reply_markup=markup)


@bot.message_handler(commands=['create'])
def create(message):
    if get_from_DB(message.chat.id) != False:
        bot.send_message(message.chat.id, "Уже существует")
        return
    message = bot.reply_to(message, 'Введите ваше имя')
    bot.register_next_step_handler(message, processFnameStep)


@bot.message_handler(commands=['view'])
def show_form(message):
    chat_id = message.chat.id
    user = get_from_DB(chat_id)
    if not user:
        bot.send_message(message.chat.id, "Вашей формы не существует")
        return

    sendInfo(chat_id, user)


@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, 'Подробная инфа что и как деать')


def send_notifications(chat_ids, message):
    for id in chat_ids:
        bot.send_message(id, message)


@bot.message_handler(commands=['send'])
def send(message):
    if (message.chat.id in admins):
        send_notifications([841859120, 966484522], "вам осталось 5 дней до ... конца хахатона")


@bot.message_handler(content_types=["text"])
def unknown(message):
    bot.send_message(message.chat.id, "Введите /start для начала")


if __name__ == "__main__":
    bot.infinity_polling()
