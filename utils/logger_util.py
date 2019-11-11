# _*_ coding: utf-8 _*_
import logging
import time
from utils.configparam_util import ConfigEngine

class Logger(object):
    def __init__(self,logger_class_name):
        current_time = time.strftime('%Y%m%d',time.localtime(time.time()))
        log_name = ConfigEngine.get_param_default("logSetting","logDir")
        # 文件路径需要修改
        log_name = log_name+current_time+".log"
        print(log_name)
        # 根据传入的类名获取当前类的日志对象
        self.logger = logging.getLogger(logger_class_name)
        # 设置日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')        # handler添加格式
        # logger添加handler
        log_console = ConfigEngine.get_param_default("logSetting", "logConsole")
        if "file" in log_console:
            fh = logging.FileHandler(log_name,encoding='utf-8')
            fh.setLevel(logging.INFO)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)
        if "console" in log_console:
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(formatter)
            self.logger.addHandler(ch)

    def get_logger_with_level(self):
        level = ConfigEngine.get_param_default("logSetting","logLevel")
        final_leval = logging.NOTSET
        # fatal、error、warning、info、debug
        if level.lower() ==  "fatal":
            final_leval = logging.FATAL
        elif level.lower() ==  "error":
            final_leval = logging.ERROR
        elif level.lower() ==  "warning":
            final_leval = logging.WARNING
        elif level.lower() ==  "info":
            final_leval = logging.INFO
        elif level.lower() == "debug":
            final_leval = logging.DEBUG
        self.logger.setLevel(final_leval)
        return self.logger
