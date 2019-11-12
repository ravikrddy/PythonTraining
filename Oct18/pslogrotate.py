from pslogconfig import logger
from time import sleep

for item in range(1, 10):
    logger.info(f'dummy log content: {item}')
    sleep(.5)
