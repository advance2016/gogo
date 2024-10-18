# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import os
import logging.handlers
'''
日志模块
'''

def get_logger(filename, level='DEBUG'):
    # 创建日志收集器
    log = logging.getLogger(os.path.basename(filename))

    # 设置日志收集器的等级
    log.setLevel(level)

    # 设置日志输出渠道
    current_dir = os.path.dirname(__file__)
    LOG_FILENAME = os.path.join(current_dir, filename)
    fh = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=104857600, backupCount=5, encoding="utf-8")

    # 设置输出渠道的日志等级
    fh.setLevel(level)

    # 绑定输出渠道到日志收集器
    log.addHandler(fh)

    # 设置日志输出渠道到控制台
    #sh = logging.StreamHandler()
    #sh.setLevel('INFO')
    #log.addHandler(sh)

    # 创建格式对象
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    # 为输出渠道设置日志格式
    fh.setFormatter(formatter)
    #sh.setFormatter(formatter)

    return log

def get_logger_old(filename):
    current_dir = os.path.dirname(__file__)
    LOG_FILENAME = os.path.join(current_dir, filename)
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                  '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=104857600, backupCount=5,
                                                        encoding="utf-8")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

'''    
class loggerAPI:
    def __init__(self, filename):
        current_dir = os.path.dirname(__file__)
        LOG_FILENAME = os.path.join(current_dir, filename)
        self.logger = logging.getLogger()

        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(process)d-%(threadName)s - '
                                      '%(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        file_handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=104857600, backupCount=5, encoding="utf-8")
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
'''

