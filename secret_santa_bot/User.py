from __init__ import bot


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

    def __str__(self):
        return f'{self.fname}'

def sendInfo(chat_id, user):
    bot.send_message(chat_id, f'Ваши данные:  {user.fname} {user.sname}\n Курс: {user.year}\n Комната: {user.room}\n Подарок: {user.present}')
