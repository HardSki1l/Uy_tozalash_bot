import sqlite3
from data.config import DB_PATH
category_all = [
    "Hamma changini olish",
    "Gilamni changini olish",
    "Oboy changini olish",
    "Qandillarning changini olish",
    "Shift changini olish",
    "Hammom tozalash",
    "Tualet tozalash",
    "Oynalarni tozalash",
    "Mebellarni changini olish",
    "Polni changini olish",
    "Sanuzel tozalash",
    "Gilamlarni joyida yuvish",
    "Divan ximchistka",
    "Matras ximchistka",
    "Idishlarni yuvish",
    "Kiyimlarni tartibga keltirish",
    "Padvalni tartibga keltirish",
    "Buyumlarni tartibga keltirish",
    "Kiyimlarni dazmollash",
    "Bruschatka tozalash",
    "Alikafon tozalash",
    "Gazonakosilka",
    "Fasad yuvish",
    "Dezinfeksiya",
    "Pardalarni yuvib dazmollash"
]
connect = sqlite3.connect(f"{DB_PATH}/bot.db")
cursor = connect.cursor()
cursor.execute(
    "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, phone TEXT, longitude TEXT NULL, latitude TEXT NULL,fullname TEXT NULL)")


cursor.execute("CREATE TABLE IF NOT EXISTS choise_table (id INTEGER PRIMARY KEY AUTOINCREMENT,message_id INTEGER,choises TEXT,user_id INTEGER UNIQUE)")
async def add_choise_category(message_id, user_id, choises):
    result = cursor.execute("SELECT * FROM choise_table WHERE user_id=?", (int(user_id),)).fetchone()
    print(result)
    if result is None:
        cursor.execute(
            "INSERT INTO choise_table (message_id, choises, user_id) VALUES (?, ?, ?)",
            (message_id, str(choises + "//"), user_id)
        )
        connect.commit()
        print("A")
        return choises + "//"
    else:
        print("B")
        cursor.execute("SELECT choises FROM choise_table WHERE user_id=?", (int(user_id),))
        old_choises = cursor.fetchone()
        print(old_choises)
        if old_choises:
            print("C")
            old_choises = old_choises[0]
            updated_choises = f"{old_choises}{choises}//"
            cursor.execute("UPDATE choise_table SET choises=? WHERE user_id=?", (updated_choises, int(user_id)))
            connect.commit()

            return updated_choises


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


async def update_phone_number(user_id, phone):
    cursor.execute("UPDATE users SET phone = ? WHERE user_id = ?",
                   (phone, user_id))
    connect.commit()


async def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))
    connect.commit()
