
from base_manager import BaseManager
import unittest
from utils.browser_engine import BrowserEngine

class BaseCase(unittest.TestCase,BaseManager):
    # 执行用例前回到首页
    @classmethod
    def setUpClass(cls):
        cls.logger = cls.get_logger()
        cls.driver.refresh()
        # 每个入口记录类名
        cls.logger.info("-----执行用例类：" + cls.__name__)

    @classmethod
    def tearDownClass(cls):
        pass

    # 每个入口记录方法名
    def setUp(self):
        # self.get_logger().info("-----执行用例方法：" + self.get_func_name())
        # 打印出来是setUp方法
        pass

    def tearDown(self):
        pass

    # def get_func_name(self):
    #     import sys
    #     try:
    #         raise Exception
    #     except:
    #         exc_info = sys.exc_info()  # 返回 异常类型，异常，traceback对象
    #         traceObj = exc_info[2]  # traceback对象
    #         frameObj = traceObj.tb_frame  # 获取frame对象，即本函数的frame信息
    #         # print frameObj.f_code.co_name,frameObj.f_lineno                 #请在使用的时候将其注释
    #         Upframe = frameObj.f_back  # 获取该代码段的frame信息，即调用该函数的函数frame
    #         # print Upframe.f_code.co_name, Upframe.f_lineno                   #请在使用的时候将其注释
    #         return (Upframe.f_code.co_name, Upframe.f_lineno)[0]  # 获取名称
