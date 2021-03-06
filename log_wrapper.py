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


def get_logger(name='output', log_path=None):
    if name in logger_list:
        return logger_list[name]
    formatter = logging.Formatter("[%(asctime)s] (%(levelname)s) %(filename)s: %(funcName)s %(lineno)d:  %(message)s")
    log_path = os.path.join(cur_file_dir, "../log") if not log_path else log_path
    if not os.path.exists(log_path):
        os.makedirs(log_path)
    name = name if name.endswith(".log") else name + ".log"
    log_filename = os.path.join(log_path, name)
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


def info(msg):
    get_logger().info(msg)


def error(msg):
    get_logger().error(msg)


def warn(msg):
    get_logger().warning(msg)
