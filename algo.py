import random
import database

class SecretSanta:

    def __init__(self):
        self.info = dict()
        self.selection = dict()
        self.participants = 0
 
    def get_info(self):
        data = database.read_data()
        for elem in data:
            id = int(elem[0])
            name = elem[1] + ' ' + elem[2]
            room = int(elem[3])
            course_number = int(elem[4])
            self.info[id] = [name, room, course_number]
        
    def assign(self):
        choices = [name for name in self.info] # кому дарить
        delta = 6
        different_rooms = True
        for gift_giver in self.info:
            gift_receiver = random.choice(choices) 
            while (gift_receiver == gift_giver or gift_receiver in self.selection or self.info[gift_giver][1] == self.info[gift_receiver][1]):
                gift_receiver = random.choice(choices)
                receiver_course_number = self.info[gift_receiver][2]
                giver_course_number = self.info[gift_giver][2]
                if different_rooms:
                    if gift_receiver in self.selection and self.selection[gift_receiver] == gift_giver and self.info[gift_giver][1] == self.info[gift_receiver][1] \
                        and different_rooms and abs(receiver_course_number - giver_course_number) != delta:
                        continue
                    elif gift_giver == gift_receiver or self.info[gift_giver][1] == self.info[gift_receiver][1] and different_rooms and abs(receiver_course_number - giver_course_number) != delta:
                        different_rooms = False
                        for gift_receiver in choices:
                            if self.info[gift_giver][1] != self.info[gift_receiver][1]:
                                different_rooms = True
                                break
                        delta -= 1
                else:
                    if gift_receiver in self.selection and self.selection[gift_receiver] == gift_giver and abs(receiver_course_number - giver_course_number) != delta:
                        continue
                    elif gift_giver == gift_receiver and abs(receiver_course_number - giver_course_number) != delta:
                        delta -= 1
                        continue
                break
            self.selection[gift_giver] = gift_receiver
            ind = choices.index(gift_receiver)
            choices.pop(ind)
        for person in self.info:
            database.update_gifts(person, self.selection[person])
            
    def start(self):
        self.get_info()
        self.assign()


if __name__ == '__main__':
    secret_santa = SecretSanta()
    secret_santa.start()


  
