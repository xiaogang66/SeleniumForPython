# driver	获取浏览器驱动
# 	        浏览器全局设置（关闭浏览器，最大化）
# logger	获取logger对象，用于输出日志
from utils.browser_engine import BrowserEngine
from utils.logger_util import Logger

class BaseManager(object):
    def __init__(self):
        # logger初始化
        self.logger = Logger(self.__class__.__name__)
        self.logger = self.logger.get_logger_with_level()
        # 浏览器初始化操作
        self.driver = BrowserEngine.get_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
