import sqlite3

connect = sqlite3.connect('/home/hardski1l/PycharmProjects/Bot-Project/bot.db')
cursor = connect.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, phone INTEGER, longitude TEXT NULL, latitude TEXT NULL,fullname TEXT NULL)")


async def add_user(user_id, tel_number):
    cursor.execute('INSERT INTO users(user_id, phone) VALUES (?, ?)', (user_id, tel_number))
    connect.commit()


async def update_location(user_id, longitude, latitude):
    cursor.execute("UPDATE users SET longitude = ?, latitude = ? WHERE user_id = ?",
                   (longitude, latitude, user_id))
    connect.commit()


async def update_fullname(user_id, fullname):
    cursor.execute("UPDATE users SET fullname = ? WHERE user_id = ?",
                   (fullname, user_id))
    connect.commit()
