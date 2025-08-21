import sqlite3

conn = sqlite3.connect('database.db')

cursor = conn.cursor()

# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS users (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         username TEXT NOT NULL,
#         password TEXT NOT NULL
#     )
# ''')

# users = [
#     ('user9', 'password9'),
#     ('user10', 'password10'),
#     ('Vin Diesel', 'password11'),
# ]

# cursor.executemany('''
#     INSERT INTO users (username, password) VALUES (?, ?)
# ''', users)

# cursor.execute('''
#     INSERT INTO users (username, password) VALUES ('admin2', 'admin2')
# ''')

# cursor.execute('''SELECT * FROM users''')   # ДОСТАТЬ ВСЕХ
# users = cursor.fetchall()
# print(*users, sep='\n')

# conn.commit()
# print('Данные добавлены')

# cursor.execute("SELECT * FROM users WHERE username='Vin Diesel'")  # ДОСТАТЬ ОПРЕДЕЛЕННОГО ЮЗЕРА 
# users = cursor.fetchall()
# print(*users, sep='\n')

# cursor.execute("SELECT username FROM users WHERE id >= 5")  # ДОСТАТЬ ОПРЕДЕЛЕННОГО ЮЗЕРА И ЧАСТЬ СТРОКИ
# users = cursor.fetchall()
# print(*users, sep='\n')

# for user in users:
#     print(user[1])

# cursor.execute("UPDATE users SET username='Наруто' WHERE id>1")  # ИЗМЕНИТЬ ЮЗЕРА 
# users = cursor.fetchall()
# print(*users, sep='\n')


cursor.execute("DELETE FROM users WHERE id = 1")  # ИЗМЕНИТЬ ЮЗЕРА 
users = cursor.fetchall()
print(*users, sep='\n')

conn.commit()
print('Данные обновлены')