# Импортируем все необходимые модули SQLAlchemy
from sqlalchemy import *
from sqlalchemy import MetaData

# Создаем движок для подключения к SQLite базе данных
engine = create_engine('sqlite:///database.db')

# Создаем объект метаданных для работы с таблицами
metadata = MetaData()

# Загружаем существующую таблицу 'users' из базы данных
# autoload_with=engine автоматически определяет структуру таблицы
users = Table('users', metadata, autoload_with=engine)

# Получение всех пользователей из базы данных
conn = engine.connect()
# Выполняем SELECT запрос
result = conn.execute(select(users))
# Получаем все записи
all_users = result.fetchall()

# Выводим результат
for user in all_users:
    print(user)