"""demo for the log rotate"""
import logging
from logging.handlers import RotatingFileHandler

fmt_str = '%(asctime)s:%(levelname)s:%(name)s:%(filename)s:%(process)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log

fh = RotatingFileHandler('access.log', maxBytes=32, backupCount=5)  # where to log
fh.setFormatter(fmt)

logger = logging.getLogger('citrix')  # custom logger
logger.setLevel(logging.INFO)
logger.addHandler(fh)  # handler to logger
