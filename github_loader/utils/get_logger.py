"""
Module for logger configuration
"""
import os
import logging
from logging.handlers import RotatingFileHandler


def make_logger(file_path, logger_name):
    """
    Function that return logger instance with all configuration we want
    :param file_path: log messages storage file
    :param logger_name: logger name
    :return: logger
    """
    logger = logging.getLogger(logger_name)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    file_handler = RotatingFileHandler(file_path, mode='a', maxBytes=10000000, backupCount=5)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    logger.setLevel(logging.INFO)

    return logger
