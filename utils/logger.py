# -*- coding: UTF-8 -*-
'''
@Project ：Python_Workspace 
@File    ：my_logger.py
@IDE     ：PyCharm 
@Author  ：zjj
@Date    ：2023/8/19 15:13 
'''
import logging, time, os
from logging.handlers import TimedRotatingFileHandler

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():

    def __init__(self):
        # 定义日志文件名称，使用当前日期作为后缀
        self.logname = os.path.join(LOG_PATH, "{}.log".format(time.strftime("%Y%m%d")))

        # 创建一个 Logger 实例
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        # 定义日志输出格式
        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        # 使用 TimedRotatingFileHandler 来实现日志文件的按日期分割
        self.filelogger = TimedRotatingFileHandler(self.logname, when="midnight", interval=1, backupCount=7)
        self.console = logging.StreamHandler()
        # self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        # self.console = logging.StreamHandler()

        # 控制台日志级别设置为 WARNING，以避免大量冗余信息显示在控制台上
        self.console.setLevel(logging.WARNING)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)

        # self.console.setLevel(logging.DEBUG)
        # self.filelogger.setLevel(logging.DEBUG)
        # self.filelogger.setFormatter(self.formater)
        # self.console.setFormatter(self.formater)

        # 将文件日志处理器和控制台日志处理器添加到 Logger 实例中
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)



logger = Logger().logger

if __name__ == '__main__':
    # 向日志记录测试信息
    logger.info("---测试开始---")
    logger.debug("---测试结束---")
