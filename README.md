# Урок 13 - Учебные модули

## Описание файлов

### Базы данных
- **study_bd.py** - Работа с SQLite базой данных (создание, вставка, выборка, обновление, удаление)
- **study_bd_alchemy.py** - Работа с базой данных через SQLAlchemy ORM
- **database.db** - SQLite база данных с таблицей users

### GUI приложения
- **study_check_box.py** - Изучение чекбоксов в tkinter
- **study_radio_button.py** - Изучение радиокнопок в tkinter
- **study_key_logger.py** - Кейлоггер для отслеживания нажатий клавиш

### Веб-парсинг
- **parsing.py** - Парсер автомобилей с сайта drom.ru (спецразмещение)

### Игры
- **arkanoid.py** - Игра Арканоид на tkinter

### Утилиты
- **app.py** - Основное приложение
- **my_module.py** - Пользовательский модуль
- **debugging.py** - Модуль для отладки

## Зависимости
```
requests
beautifulsoup4
pandas
sqlalchemy
```

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Запуск
Каждый файл можно запустить отдельно:
```bash
python study_bd.py
python parsing.py
python arkanoid.py
```