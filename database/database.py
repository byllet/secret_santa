import sqlite3
import time

from selenium import webdriver as wd
from selenium.webdriver.common.by import By

connect = sqlite3.connect('D:\python_projects\secret_santa\secret_santa_bot\database.s3db', check_same_thread=False)
cursor = connect.cursor()


def add_data(name: str, surname: str, room_number: int, grade_number: int, extra_info: str, chat_id: int):
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


def get_user_by_chat_id(chat_id):
    data = cursor.execute(f"SELECT * FROM Participants WHERE chat_id = {chat_id}")
    return data.fetchall()

def get_users():
    data = cursor.execute(f"SELECT chat_id FROM Participants")
    return data.fetchall()


def pulling():
    local_db_path = "D:\python_projects\secret_santa\secret_santa_bot\database.s3db"
    driver = wd.Chrome()
    while True:
        driver.get("https://inloop.github.io/sqlite-viewer/")
        file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
        file_input.send_keys(local_db_path)
        time.sleep(10)
        pass


