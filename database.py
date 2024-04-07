import sqlite3

connect = sqlite3.connect('database.s3db')

cursor = connect.cursor()


def add_data(name: str, surname: str, room_number: int, grade_number: int, extra_info: str, chat_id: int):
    # gift_id_collect

    gift_id = 3
    cursor.execute(
        f"INSERT INTO Participants (name, surname, room_number, grade_number, extra_info, chat_id, gift_id) VALUES ('{name}', '{surname}', {room_number}, {grade_number}, '{extra_info}', {chat_id}, {gift_id}) ")
    connect.commit()


def update_gifts(id: int, gift_id: int):
    cursor.execute(f"UPDATE Participants SET gift_id = {gift_id} WHERE id = {id}")
    connect.commit()


def read_data():
    data = cursor.execute("SELECT * FROM Participants")
    return data.fetchall()


add_data("anrey", "zhmickh", 228, 3, "love cockroaches", 12223)
