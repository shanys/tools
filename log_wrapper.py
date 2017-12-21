#encoding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import logging
import logging.handlers
# logger池，防止创建多个同名logger
logger_list = {}
cur_file_dir = os.path.split(os.path.realpath(__file__))[0]


def get_logger(name='output'):
        if name in logger_list:
            return logger_list[name]
        formatter = logging.Formatter("[%(asctime)s] (%(levelname)s) %(filename)s:%(lineno)3d:  %(message)s")
        log_path = os.path.join(cur_file_dir, "../log")
        if not os.path.exists(log_path):
            os.makedirs(log_path)
        log_filename = os.path.join(log_path, name, ".log")
        if not os.path.exists(os.path.split(log_filename)[0]):
            os.mkdir(os.path.split(log_filename)[0])
        file_handler = logging.handlers.RotatingFileHandler(log_filename, maxBytes=10*1024*1024,backupCount=5)
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger = logging.getLogger(name)
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        logger_list[name] = logger
        return logger