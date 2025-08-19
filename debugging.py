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
logger.propagate = False # Отключаем передачу в родительский лог

logger.debug('Подробная информация для отладки')   # DEBUG
logger.info('Информационное сообщение')            # INFO

logger.warning('Предупреждение об ошибке')         # WARNING
logger.error('Ошибка в программе')                 # ERROR
logger.critical('Критическая ошибка')              # CRITICAL