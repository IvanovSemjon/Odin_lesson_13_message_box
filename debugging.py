import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Подробная информация для отладки')   # DEBUG
logging.info('Информационное сообщение')            # INFO

logging.warning('Предупреждение об ошибке')         # WARNING
logging.error('Ошибка в программе')                 # ERROR
logging.critical('Критическая ошибка')              # CRITICAL