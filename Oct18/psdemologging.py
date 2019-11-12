import logging

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
dt_fmt_str='%d-%m-%Y %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=fmt_str, datefmt=dt_fmt_str)
logging.debug('debugging messages')
logging.info('confirmation messages')
logging.warning('warn message')
logging.error('an error notes')
logging.critical('panic errors')
