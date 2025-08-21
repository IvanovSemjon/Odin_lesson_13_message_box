import logging
import colorlog


handler = colorlog.StreamHandler()
handler.setFormatter(colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
))

logger = colorlog.getLogger('example')
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

# logger.debug('Подробная информация для отладки')   # DEBUG
# logger.info('Информационное сообщение')            # INFO
# logger.warning('Предупреждение об ошибке')         # WARNING
# logger.error('Ошибка в программе')                 # ERROR
# logger.critical('Критическая ошибка')              # CRITICAL


from typing import Union

def add_numbers(a: Union[int, str, float], b: Union[int, str, float]) -> Union[float, None]:
    """Функция с примерами логирования"""
    logger.debug(f"Начало выполнения add_bumbers с параметрами a={a}, b={b}")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        try:
            logger.warning(f'Попытка преобразовать к числу: {a}={type(a)}, {b}={type(b)}')
            a = float(a)
            b = float(b)
        except:
            logger.critical(f'Не удалось преобразовать к числу: {a}={type(a)}, {b}={type(b)}')
            return None
    logger.info(f"Сложение чисел {a} и {b}")
    return a + b

logger.debug('Программа запущена')
result = add_numbers(5, 3)
logger.info(f"Результат сложения: {result}")

result = add_numbers(5, '30')
logger.info(f"Результат сложения: {result}")

result = add_numbers(5, 'hello')
logger.info(f"Результат сложения: {result}")

name = 'John'

def add_a_b(a: int, b: int) -> float:
    """Функция с примерами логирования"""
    return a + b

result = add_a_b(5, 10)
