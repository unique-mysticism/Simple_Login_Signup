import sqlite3



insert_user_table = "INSERT INTO `profile`(username, password, first_name, last_name, email_address, phone_num) VALUES(?, ?, ?, ?, ?, ?)"
found_user = "SELECT * FROM `profile` WHERE `username` = ? and `password` = ?"
update_password = "Update `profile` set password = (?) WHERE username = (?)"


def database():
    """
    Connect to the "users_info" database, create it if it doesn't exist
    """
    global conn, cursor
    conn = sqlite3.connect("db/users_info.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS `profile` (
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                    username TEXT,
                    password TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    email_address TEXT,
                    phone_num TEXT
                    )""")
    return [conn, cursor]


def duplicate_found(username):
    database()
    cursor.execute("SELECT * FROM `profile` WHERE `username` = ?", (username,))
    if cursor.fetchone() is not None:
        return True
    return False








# def user_found(info):
#     database()
#     cursor.execute("""SELECT * FROM `profile`
#                    WHERE `username` = ? and `password` = ?""",
#                    tuple(value for value in info.values())
#                    )
#     info = cursor.fetchone()
#     if info is not None:
#         return True
#     return False
            
            
# def user_save(info):
#     database()
#     cursor.execute("""INSERT INTO `profile`
#                    (username, password, first_name, last_name, email_address, phone_num)
#                     VALUES(?, ?, ?, ?, ?, ?)""",
#                     tuple(value for value in info.values())
#                     )
#     conn.commit()
#     cursor.close()
#     conn.close()
    
    
# def change_password(info):
#     database()
#     cursor.execute("""Update `profile` set password = (?) WHERE username = (?)""",
#                    tuple(value for value in info.values())[::-1]
#                    )
#     conn.commit()
#     cursor.close()
#     conn.close()